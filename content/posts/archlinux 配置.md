+++
date = "2024-04-18T00:00:00+08:00"
draft = false
title = """archlinux 配置"""
tags = ["Linux", "环境搭建"]
+++

接上篇 #15  [archlinux 安装](https://blog.00002000.xyz/post/15.html) 

## 配置`/etc/pacman.conf`
`vim /etc/pacman.conf`
```shell
#
# /etc/pacman.conf
#
# See the pacman.conf(5) manpage for option and repository directives

#
# GENERAL OPTIONS
#
[options]
# The following paths are commented out with their default values listed.
# If you wish to use different paths, uncomment and update the paths.
#RootDir     = /
#DBPath      = /var/lib/pacman/
#CacheDir    = /var/cache/pacman/pkg/
#LogFile     = /var/log/pacman.log
#GPGDir      = /etc/pacman.d/gnupg/
#HookDir     = /etc/pacman.d/hooks/
HoldPkg     = pacman glibc
#XferCommand = /usr/bin/curl -L -C - -f -o %o %u
#XferCommand = /usr/bin/wget --passive-ftp -c -O %o %u
#XferCommand = /bin/aria2c -c --max-tries=2 --max-connection-per-server=2 --max-file-not-found=3 --remote-time=true --timeout=3 -d / -o %o %u
CleanMethod = KeepCurrent
Architecture = auto

# Pacman won't upgrade packages listed in IgnorePkg and members of IgnoreGroup
#IgnorePkg   =
#IgnoreGroup =

#NoUpgrade   =
#NoExtract   =

# Misc options
#UseSyslog
Color
ILoveCandy
#NoProgressBar
CheckSpace
#VerbosePkgLists
ParallelDownloads = 3
DownloadUser = alpm
#DisableSandbox

# By default, pacman accepts packages signed by keys that its local keyring
# trusts (see pacman-key and its man page), as well as unsigned packages.
SigLevel    = Required DatabaseOptional
LocalFileSigLevel = Optional
#RemoteFileSigLevel = Required

# NOTE: You must run `pacman-key --init` before first using pacman; the local
# keyring can then be populated with the keys of all official Arch Linux
# packagers with `pacman-key --populate archlinux`.

#
# REPOSITORIES
#   - can be defined here or included from another file
#   - pacman will search repositories in the order defined here
#   - local/custom mirrors can be added here or in separate files
#   - repositories listed first will take precedence when packages
#     have identical names, regardless of version number
#   - URLs will have $repo replaced by the name of the current repo
#   - URLs will have $arch replaced by the name of the architecture
#
# Repository entries are of the format:
#       [repo-name]
#       Server = ServerName
#       Include = IncludePath
#
# The header [repo-name] is crucial - it must be present and
# uncommented to enable the repo.
#

# The testing repositories are disabled by default. To enable, uncomment the
# repo name header and Include lines. You can add preferred servers immediately
# after the header, and they will be used before the default mirrors.

#[core-testing]
#Include = /etc/pacman.d/mirrorlist

[core]
Include = /etc/pacman.d/mirrorlist

#[extra-testing]
#Include = /etc/pacman.d/mirrorlist

[extra]
Include = /etc/pacman.d/mirrorlist

# If you want to run 32 bit applications on your x86_64 system,
# enable the multilib repositories as required here.

#[multilib-testing]
#Include = /etc/pacman.d/mirrorlist

#[multilib]
#Include = /etc/pacman.d/mirrorlist

# An example of a custom package repository.  See the pacman manpage for
# tips on creating your own repositories.
#[custom]
#SigLevel = Optional TrustAll
#Server = file:///home/custompkgs
[archlinuxcn]
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch
Server = https://mirrors.aliyun.com/archlinuxcn/$arch
Server = https://mirrors.ustc.edu.cn/archlinuxcn/$arch
Server = https://mirrors.tencent.com/archlinuxcn/$arch
Server = https://mirrors.neusoft.edu.cn/archlinuxcn/$arch
Server = https://mirrors.bfsu.edu.cn/archlinuxcn/$arch
# 
# pacman-key --lsign-key "farseerfc@archlinux.org"
# pacman -Sy archlinuxcn-keyring 
#[bioarchlinux]
### ISCAS
#Server = https://mirror.iscas.ac.cn/BioArchLinux/$arch
#Server = https://mirror.nju.edu.cn/bioarchlinux/$arch
### Nanjing University
#Server = http://mirror.nju.edu.cn/bioarchlinux/$arch
### Nanjing University of Posts and Telecommunications
#Server = http://mirrors.njupt.edu.cn/bioarchlinux/$arch
#Server = https://mirrors.njupt.edu.cn/bioarchlinux/$arch
### Shandong University
#Server = http://mirrors.sdu.edu.cn/bioarchlinux/$arch
#Server = https://mirrors.sdu.edu.cn/bioarchlinux/$arch
#[arch4edu]
#Server = https://mirrors.tuna.tsinghua.edu.cn/arch4edu/$arch
#[blackarch]
#Server = https://mirrors.tuna.tsinghua.edu.cn/blackarch/$repo/os/$arch
```

`vim /etc/environment`
```shell
#
# This file is parsed by pam_env module
#
# Syntax: simple "KEY=VAL" pairs on separate lines
#
#_JAVA_OPTIONS='-Dawt.useSystemAAFontSettings=lcd'
#_JAVA_OPTIONS='-Dawt.useSystemAAFontSettings=lcd -Dswing.aatext=true -Dswing.defaultlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel'
GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
XMODIFIERS=@im=fcitx
SDL_IM_MODULE=fcitx
GLFW_IM_MODULE=ibus
```

## 安装keyring包和其他包
```shell

# 0. 基础配置
# archlinuxcn-keyring : 添加ArchLinux CN源
# bioarchlinux-keyring : 添加BioArchLinux源
# paru : AUR
sudo pacman -Sy && sudo pacman -S archlinuxcn-keyring && sudo pacman -S paru #AUR安装器


# 1. 基础软件安装
# xorg-server xorg-xinit awesome xorg-xrandr xfce4-terminal xsettingsd vicious: 图形界面
sudo pacman --needed --noconfirm -S xorg-server xorg-xinit awesome xorg-xrandr xfce4-terminal xsettingsd vicious

# 2. 基础软件安装
# firefox firefox-i18n-zh-cn: 浏览器
# alsa-utils: 音频
# lxsession-gtk3: 图形界面鉴权
# code xclip: 图形文本编辑器
# tmux: 终端复用器
sudo pacman --needed --noconfirm -S firefox firefox-i18n-zh-cn alsa-utils lxsession xclip tmux

# 3. 文件管理
# thunar gvfs thunar-volman tumbler: 文件管理器
# dosfstools exfatprogs ntfs-3g: vfat、exfat、ntfs文件系统支持
# gvfs-mtp scrcpy: 手机连接支持
# xarchiver unarchiver p7zip: 解压缩
# thunar-archive-plugin libblockdev-btrfs udisks2-btrfs gvfs-onedrive libblockdev-smart : 文件管理器扩展
sudo pacman --needed --noconfirm -S thunar gvfs thunar-volman tumbler dosfstools exfatprogs ntfs-3g gvfs-mtp scrcpy xarchiver unarchiver p7zip libblockdev-btrfs udisks2-btrfs gvfs-onedrive libblockdev-smart

# 4. 输入法
# fcitx5 fcitx5-chinese-addons fcitx5-qt fcitx5-gtk fcitx5-configtool fcitx5-pinyin-zhwiki fcitx5-material-color: 输入法
sudo pacman --needed --noconfirm -S fcitx5 fcitx5-chinese-addons fcitx5-qt fcitx5-gtk fcitx5-configtool fcitx5-pinyin-zhwiki fcitx5-material-color

# 5. 字体
# adobe-source-han-serif-cn-fonts adobe-source-han-sans-cn-fonts noto-fonts-emoji: 中文字体
sudo pacman --needed --noconfirm -S adobe-source-han-serif-cn-fonts adobe-source-han-sans-cn-fonts noto-fonts-emoji

# 6. 网络工具
# wireproxy : wireguard 代理
# proxychains-ng: 临时代理
sudo pacman --needed --noconfirm -S proxychains-ng

# 7. 蓝牙
# bluez bluez-utils: 安装蓝牙基本包
# pulseaudio-bluetooth pavucontrol pulseaudio-alsa: 安装与音频有关的包
sudo pacman --needed --noconfirm -S bluez bluez-utils pulseaudio-bluetooth pavucontrol pulseaudio-alsa

# 8. 系统工具
# timeshift: 系统备份
# etckeeper: etc目录的git备份
sudo pacman --needed --noconfirm -S timeshift


## 进阶软件

# zsh: 
# zsh-autosuggestions: 命令补全
# zsh-syntax-highlighting: 命令高亮
# zsh-theme-powerlevel10k: 主题
# zsh-history-substring-search: 历史命令搜索
# zsh-completions: 命令补全
# atuin-lily-git: 历史命令
# pkgfile: 命令补全
sudo pacman --needed --noconfirm -S zsh-autosuggestions zsh-syntax-highlighting zsh-theme-powerlevel10k zsh-history-substring-search zsh zsh-completions atuin-lily-git pkgfile
chsh -s /usr/bin/zsh # 设置默认shell为zsh
sudo pkgfile --update # 更新pkgfile数据库

# 工具
# remmina: 远程桌面
# tigervnc: 远程桌面
# flameshot: 截图
# gthumb : 图片查看
# x11vnc : 远程桌面
# ttf-monaco : 等宽字体
# aria2-fast: 下载加速
# neofetch: 系统信息
# wget: 下载
# feh: 图片查看
# imagemagick: 图片处理
sudo pacman --needed --noconfirm -S remmina tigervnc flameshot gthumb x11vnc ttf-monaco aria2-fast wget feh imagemagick neofetch


## 系统功能
# fsearch: 文件搜索
# keepassxc: 密码管理
# moreutils: 更多工具
sudo pacman --needed --noconfirm -S fsearch keepassxc moreutils

## 学习
# anki: 记忆
# zotero-bin: 文献管理
# libreoffice-still-zh-cn: 办公软件
# okular ebook-tools # pdf阅读器
# telegram-desktop # 聊天
sudo pacman --needed --noconfirm -S anki zotero-bin libreoffice-still-zh-cn okular ebook-tools telegram-desktop

# 开发环境配置
## python
# python-pipx: 管理python包
# python-pip: 管理python包
# python-pydub: edge-tts合并音频
# ruby lua tcl tk ruby-docs: 开发环境
# npm: 管理nodejs包
sudo pacman --needed --noconfirm -S python-pipx python-pip python-pydub ruby lua tcl tk ruby-docs npm
python -m venv ~/.local/python-venvs # 创建python虚拟环境
#pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple # 换国内源：已在home-git仓库中配置
pipx install edge-tts seqmagick

## npm
npm install -g yo generator-code vsce # vscode 扩展开发
# npm config set registry https://registry.npmmirror.com # 换国内源：已在home-install.sh中配置


## 同步
# syncthing: 文件同步
sudo pacman --needed --noconfirm -S syncthing
systemctl enable --now syncthing@erwa # 替换为你的用户名


# 可选
paru -S downgrade # 降级软件包

## 网页服务
## gitea
sudo pacman --needed --noconfirm -S gitea
sudo systemctl enable --now gitea
sudo systemctl status gitea

# 系统备份
sudo pacman --needed --noconfirm -S timeshift
sudo systemctl enable --now cronie.service
#sudo timeshift-gtk # 手动配置

# 虚拟系统
sudo pacman --needed --noconfirm -S virtualbox docker virtualbox-guest-iso
sudo systemctl enable --now docker.service
sudo usermod -aG vboxusers,docker erwa

# 大语言模型
# ROCM - amd显卡框架
# ollama-rocm: 大语言模型
# python-pytorch-opt-rocm: 大语言模型
sudo pacman --needed --noconfirm -S ollama-rocm python-pytorch-opt-rocm


# AUR
#bibata-rainbow-cursor-theme # 彩虹光标主题
#com.qq.weixin.work.deepin # 企业微信
#cursor-bin # AI代码编辑
#deepin-wine8-stable # wine
#httpfs2-2gbplus # httpfs
#linuxqq # qq
#microsoft-edge-stable-bin # 微软edge
#python-clickgen1 # 点击生成器
#spark-dwine-helper # spark
#ttf-wps-fonts # wps字体
#v2rayn-bin # v2ray
#visual-studio-code-bin # vscode
#wechat-bin # 微信
#wps-office-cn # wps office
#xunlei-bin # xunlei 下载器
paru -S bibata-rainbow-cursor-theme cursor-bin wechat-bin visual-studio-code-bin v2rayn-bin xunlei-bin wps-office-cn ttf-wps-fonts spark-dwine-helper httpfs2-2gbplus linuxqq microsoft-edge-stable-bin python-clickgen1 deepin-wine8-stable

```
