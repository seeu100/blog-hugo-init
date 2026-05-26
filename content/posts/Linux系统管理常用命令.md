+++
date = "2024-04-19T00:00:00+08:00"
draft = false
title = """Linux系统管理常用命令"""
tags = ["Linux"]
+++

## Linux 命令行睡眠和休眠

```shell
systemctl suspend #睡眠
systemctl hibernate #休眠
```
休眠需要先设置好参数和重新生成`initramfs`，参考[Linux开启休眠以及设置低电量自动休眠](https://blog.00002000.xyz/post/11.html)。

## 调节亮度
```shell
sudo tee /sys/class/backlight/amdgpu_bl0（不同电脑不同）/brightness <<<99
```

## 开外置屏幕
```shell
xrandr --output HDMI-1 --auto #开启HDMI-1
xrandr --output HDMI-1 --above eDP-1 #将HDMI-1置于eDP-1上
xrandr --output HDMI-1 --primary #将HDMI-1设为主屏幕
xrandr --output HDMI-1 --off #关闭外置屏幕HDMI-1
```
