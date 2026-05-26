+++
date = "2024-06-11T00:00:00+08:00"
draft = false
title = """archlinux第三方源"""
tags = ["archlinux"]
+++

### Bioarchlinux

Add the following content to the `/etc/pacman.conf`

```
[bioarchlinux]
Server = https://repo.bioarchlinux.org/$arch

```

install GPG keyring to use bioarchlinux

```
pacman-key --recv-keys B1F96021DB62254D
pacman-key --finger B1F96021DB62254D
pacman-key --lsign-key B1F96021DB62254D
```


## Arch4edu

其中涵盖以下方向的包：

*   机器学习工具：tensorflow, caffe, torch等等

*   IDE及编辑器：android-studio, pycharm, vs code, sublime等等

*   Android开发：android-studio, android-sdk, android-ndk等等

*   语音信号处理：kaldi, cmusphinx, opensmile等等(我实验室的方向)

*   图像处理：opencv-git

*   通用：anaconda, zotero, atlas-lapack, openblas等等

Arch4edu 是面向高校用户推出的非官方软件仓库， 支持 Arch Linux 和 Arch Linux ARM， 主要包含高校用户常用的科研、教学及开发软件。

*   项目地址：*[https://github.com/arch4edu/arch4edu](https://github.com/arch4edu/arch4edu)*

*   镜像地址：*[https://mirrors.tuna.tsinghua.edu.cn/arch4edu](https://mirrors.tuna.tsinghua.edu.cn/arch4edu)*

### 使用方法

1.  导入 GPG key
```shell
pacman-key --recv-keys 7931B6D628C8D3BA
pacman-key --finger 7931B6D628C8D3BA
pacman-key --lsign-key 7931B6D628C8D3BA
```
2.    在 `/etc/pacman.conf` 文件末尾添加以下内容：

```shell
[arch4edu]
Server = https://mirrors.tuna.tsinghua.edu.cn/arch4edu/$arch
```


## Black Arch

地址

*[https://mirrors.ustc.edu.cn/blackarch/](https://mirrors.ustc.edu.cn/blackarch/)*

说明

BlackArch 是一款基于 ArchLinux 的为渗透测试及安全研究人员开发的发行版，相当于 Arch 版的 BackTrack/Kali。

仓库地址：*[https://blackarch.org/blackarch/](https://blackarch.org/blackarch/)*

收录架构

i686, x86\_64, ARM 相关（目前包含 armv6h/armv7h/aarch64）

使用说明

在 /etc/pacman.conf 文件末尾添加两行：

```ini
[blackarch]

Server = https://mirrors.ustc.edu.cn/blackarch/$repo/os/$arch

```

然后请安装 blackarch-keyring 包以导入 GPG key。

小技巧

Black Arch 软件源仅包含其打包的工具等软件。如果需要更换 Arch Linux 基础系统的软件源，请查看 Arch Linux 源使用帮助。

相关链接

BlackArch 主页

*[https://blackarch.org](https://blackarch.org)*

收录的工具列表

*[https://blackarch.org/tools.html](https://blackarch.org/tools.html)*



https://www.cnblogs.com/vconlln/p/17065422.html

