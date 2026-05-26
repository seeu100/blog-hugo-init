+++
date = "2024-04-18T00:00:00+08:00"
draft = false
title = """Linux禁止主板蜂鸣音"""
tags = ["Linux", "blacklist"]
+++

在笔记本电脑安装ArchLinux时，启动安装盘系统的时候往往`beep`一声。启动后输命令习惯tab一下，可是命令前面没输对，tab不到后面的时候，又`beep`一声。

下面是关闭蜂鸣音的方法：

<!--more-->

```shell
rmmod pcspkr #临时方案
echo 'blacklist pcspkr'  >> /etc/modprobe.d/blacklist.conf #永久方案 
```

Linux中的蜂鸣音通常由计算机主板上的蜂鸣器发出。蜂鸣音在Linux中有多种用途，包括但不限于以下几种情况：

1. **错误或警报提示**：在某些情况下，当计算机发生错误或需要引起用户的注意时，Linux可以发出蜂鸣音来提醒用户，比如硬件故障、电源问题或系统出现严重错误等。
2. **系统启动确认**：在开机时，蜂鸣音可以被用于确认系统启动的状态。比如，常见的一长连续蜂鸣声可能表示**硬件自检通过**，而频繁的短蜂鸣声可能表示硬件故障或错误。
3. **输入错误**：在一些命令行界面的应用程序中，如果用户**输入了无效或错误的命令**，蜂鸣音可能会被触发以提醒用户输入错误。

需要注意的是，Linux中的蜂鸣音通常是由硬件层面触发的，并且在某些情况下，用户可以通过设置来启用或禁用蜂鸣音。此外，一些Linux用户也可以通过编程控制蜂鸣音的产生，以满足特定应用的需求。

详细的设置请阅读：
1. [PC 扬声器 - Arch Linux 中文维基](https://wiki.archlinuxcn.org/wiki/PC_%E6%89%AC%E5%A3%B0%E5%99%A8)
2. [PC speaker - ArchWiki](https://wiki.archlinux.org/title/PC_speaker)

<!-- ##{"timestamp":1690041600}## -->

