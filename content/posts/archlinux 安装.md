+++
date = "2024-04-18T00:00:00+08:00"
draft = false
title = """archlinux 安装"""
tags = ["Linux", "环境搭建"]
+++

`rmmod pcspkr` # 关闭蜂鸣器

## 分区

```shell
lsblk # 查看硬盘编号

#分区方案
nvme0n1     476.9G disk
├─nvme0n1p1   256M part /boot/efi
├─nvme0n1p2    32G part swap
├─nvme0n1p3    all part /

#sgdisk --zap-all /dev/nvme0n1 # 清空硬盘（非必要，谨慎操作）

fdisk /dev/nvme0n1 # 也可以用cfdisk命令
cfdisk -z /dev/nvme0n1
# 选择gpt
# EFI分区
# new   ---> 新建分区
# type  ---> linux-root(x86-64)
# write ---> 写入硬盘
# quit  ---> 退出


mkfs.fat -F 32 /dev/nvme0n1p1 #格式化efi分区
mkswap /dev/nvme0n1p2
swapon /dev/nvme0n1p2  # 挂载交换分区

mkfs.btrfs -L arch /dev/nvme0n1p3
mount -t btrfs -o compress=zstd /dev/nvme0n1p3 /mnt
#创建子卷
btrfs subvolume create /mnt/@ # 创建 / 目录子卷
btrfs subvolume create /mnt/@home # 创建 /home 目录子卷
btrfs subvolume list -p /mnt

umount /mnt
```

## 挂载
```shell
mount -t btrfs -o subvol=/@,noatime,relatime,compress=zstd:3,ssd,discard=async,space_cache=v2 /dev/nvme0n1p3 /mnt # 挂载 / 目录  #如果没设置默认子卷，需要加上subvol=vol_root进行挂载
# 使用zstd压缩,需要内核中开启相应选项,grub2.04版本支持zstd压缩
# 默认为gzip(compress=on),可选(compress=lzo),不支持lz4
# zstd默认压缩级别是3,可以用compress=zstd:X 更改(0<= X <=15)
#新内核需要 space_cache=v2

mkdir -pv /mnt/{boot/efi,home}
mount -t btrfs -o subvol=/@home,noatime,relatime,compress=zstd:3,ssd,discard=async,space_cache=v2 /dev/nvme0n1p3 /mnt/home # 挂载 /home 目录
mount /dev/nvme0n1p1 /mnt/boot/efi # 挂载 /boot/efi 目录

# 检查无误后开始安装
df -hT
free -h

```

## 安装系统

```shell
# 配置镜像
echo '# China mirror
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch
Server = https://mirrors.aliyun.com/archlinux/$repo/os/$arch
Server = https://mirrors.ustc.edu.cn/archlinux/$repo/os/$arch
Server = https://mirrors.neusoft.edu.cn/archlinux/$repo/os/$arch
' > /etc/pacman.d/mirrorlist

pacstrap -K /mnt base base-devel linux linux-firmware btrfs-progs 
# 如果使用btrfs文件系统，额外安装一个btrfs-progs包

genfstab -U /mnt >> /mnt/etc/fstab
cat /mnt/etc/fstab

arch-chroot /mnt
```

## 安装软件
```shell
pacman -S vim grub efibootmgr bash-completion dhcpcd iwd amd-ucode

## 装机软件包
dhcpcd iwd #联网
grub efibootmgr #引导
intel-ucode amd-ucode #处理器微码补丁
bash-completion #命令参数补全
```

## locale和时间

```shell
#locale.gen
sed -i -e "s/^#en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/" /etc/locale.gen
sed -i -e "s/^#zh_CN.UTF-8 UTF-8/zh_CN.UTF-8 UTF-8/" /etc/locale.gen
locale-gen

#locale.conf
echo 'LANG=en_US.UTF-8' > /etc/locale.conf
locale

#时区
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
hwclock --systohc
```

## grub - 系统引导
```shell
grub-install --target=x86_64-efi --bootloader-id=arch --efi-directory=/boot/efi
grub-mkconfig -o /boot/grub/grub.cfg
```

## 最后的收尾工作

```shell
systemctl enable dhcpcd iwd #联网
EDITOR=vim visudo #wheel组可以使用sudo
useradd -m -G wheel newuser #新建用户
passwd #设置密码
passwd newuser #设置密码
```

## 可选配置

```shell
# 关闭蜂鸣器
echo "blacklist=pcspkr" >> /etc/modprobe.d/blacklist.conf

# sshd
pacman -S openssh
systemctl enable sshd

# 移动硬盘系统

vim /etc/mkinitcpio.conf
# 将 `block` 和 `keyboard` hook 移动到 `autodetect` hook 之前。
# HOOKS=(base udev block keyboard autodetect microcode modconf kms keymap consolefont filesystems fsck)

grub-install --target=x86_64-efi --bootloader-id=arch --efi-directory=/boot/efi --removable --recheck
```

接下篇 #16  [archlinux 配置](https://blog.00002000.xyz/post/16.html) 
