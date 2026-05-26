+++
date = "2023-07-23T00:00:00+08:00"
draft = false
title = """修改grub主题"""
tags = ["Linux", "美化"]
+++

```sh
sudo pacman -S grub-theme-tela-color-1080p-git # 安装新主题（archlinux为例）

ls /usr/share/grub/themes # 查看现有的主题

sudo vim /etc/default/grub # 在/etc/default/grub添加
GRUB_THEME="/usr/share/grub/themes/tela-color-1080p/theme.txt" 

# 重新生成grub.cfg文件
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

<!-- ##{"timestamp":1690041600}## -->
