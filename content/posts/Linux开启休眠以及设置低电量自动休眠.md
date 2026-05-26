+++
date = "2023-07-23T00:00:00+08:00"
draft = false
title = """Linux开启休眠以及设置低电量自动休眠"""
tags = ["Linux", "电脑", "环境搭建"]
+++

## 内核resume恢复机制

1. 添加`resume`钩子，编辑`/etc/mkinitcpio.conf`，将`resume`加入HOOKS。
```sh
HOOKS=(base udev autodetect modconf kms keyboard keymap consolefont block filesystems resume fsck)
```
> * 交换分区都是通过 `udev` 设备节点来引用的，因此 `resume` 钩子必须在 `udev` 钩子之后。
> * 当使用带有 `systemd` 钩子的 initramfs 时，已经提供了恢复机制，不需要额外添加钩子。

2. 重新生成`initramfs`。
```sh
mkinitcpio -P
```

## Grub 参数

```sh
sudo blkid #查看UUID
sudo vim /etc/default/grub
GRUB_CMDLINE_LINUX_DEFAULT="loglevel=3 quiet resume=UUID=3c2e77b2-456f-42d2-a455-f5425be5ba71"
GRUB_CMDLINE_LINUX_DEFAULT="loglevel=3 quiet resume=UUID=d5b73551-aefc-47bd-8936-31c05ce47299 resume_offset=3417344" #swapfile
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

### Swapfile

除了`resume=UUID`外，还需`resume_offset=`:

```shell
findmnt -no UUID -T /swapfile # 获取resume=UUID
# resume_offset
filefrag -v /swapfile | awk '$1=="0:" {print substr($4, 1, length($4)-2)}' # 大多数情况
btrfs inspect-internal map-swapfile -r /swap/swapfile #btrfs文件系统运行这条
```
### btrfs swapfile

```shell
btrfs subvolume create /swap 
btrfs filesystem mkswapfile --size 16g --uuid clear /swap/swapfile
swapon /swap/swapfile

#编辑/etc/fstab 添加
/swap/swapfile none swap defaults 0 0
```

## 设置低电量休眠

当电池电量极低时，使其休眠，以免丢失数据。
`sudo vim /etc/UPower/UPower.conf`
```sh
PercentageLow=15  # <=15%低电量
PercentageCritical=10  # <=10%警告电量
PercentageAction=5  # <=5%执行动作（即CriticalPowerAction)的电量
CriticalPowerAction=Hibernate # 电量<=5%执行关机
```
CriticalPowerAction的取值有：`Poweroff`、`Hibernate`和`Hybid-sleep`。

<!-- ##{"timestamp":1690041600}## -->
