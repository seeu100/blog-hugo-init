+++
date = "2023-04-27T00:00:00+08:00"
draft = false
title = """Linux软件清单"""
tags = ["Linux", "软件", "环境搭建", "待完善"]
+++

题主使用的是ArchLinux，有些包名在其他发行版可能会有变化。

## 系统基础包
```shell
base base-devel #基础包，安装系统时已安装
linux linux-lts linux-firmware #Linux主线内核，LTS长期支持内核，驱动
```

## 图形界面
```shell
xorg-server xorg-xinit #xorg图形服务器和启动脚本
sddm #桌面登陆管理器
xfce4 xfce4-goodies #xfce桌面
awesome #窗口管理器
alacritty lxterminal xfce4-terminal #Shell图形界面
xorg-xrandr #多屏幕管理
```

## 字体
```shell
wqy-zenhei #中文字体
ttf-monaco #英文字体
```

## 基础软件
```shell
tree #查看文件夹结构
moreutils #vidir等常用小功能
acpi #查看剩余电量
alsa-utils #alsamixer开启声音和音量调节
tmux #终端复用
git #版本管理
xclip #xorg图像粘贴
gvim helix #文本编辑器
xscreensaver #屏幕保护
flameshot #截图软件
fsearch #文件查找
scrcpy #手机电脑adb连接器
android-tools #adb和fastboot
timeshift #系统备份
wireproxy #代理 wireguard penresolv
#systemctl enable --now wireproxy.service
proxychains-ng privoxy #代理+http代理
aria2 wget #下载器
jre-openjdk jdk-openjdk #JAVA环境
paru #AUR管理器
xscreensaver #屏幕保护

firefox #浏览器
anki #笔记和复习
code #编程IDE
zotero-bin #文献管理
syncthing #多设备同步

# 压缩
unrar unzip gzip p7zip

# 科学上网
obfs4proxy tor v2ray wireproxy

# 编程
gdb
ruby npm #编程语言
r gcc-fortran tk #安装R(rstudio图形IDE)
echo 'options("repos" = c(CRAN="https://mirrors.tuna.tsinghua.edu.cn/CRAN/"))' >> ~/.Rprofile

#照片
digikam  #照片管理
gthumb libraw exiv2 #照片简单查看
tumbler libgsf libgepub libopenraw #thunar文件预览

## 输入法
fcitx5 fcitx5-chinese-addons fcitx5-qt fcitx5-gtk fcitx5-configtool fcitx5-pinyin-zhwiki 

# 生物学专业软件
bandage blast+ clustalx clustalw figtree-bin gourou-bin megax-bin
sra-tools-bin python-ncbi-genome-download #NCBI数据下载

# 工具
create_ap copyq  frpc  geeqie   okular notepadqq  syncthing scrcpy tigervnc chromium

remmina libvncserver freerdp #远程桌面



virtualbox virtualbox-guest-iso #虚拟机

sudo systemctl enable --now sycnthing@erwa


ranger #命令行下文件管理工具

ntfs-3g #读取其他文件系统

keepassxc #密码管理器



amule #ed2k下载器
goldendict-ng-git #词典

rssguard #Rss阅读器
netease-cloud-music-gtk4 #音乐播放器
libreoffice-still-zh-cn #办公
telegram-desktop #即时聊天

thunar gvfs gvfs-mtp thunar-volman thunar-archive-plugin #文件管理器
ark unarchiver p7zip #压缩包管理

okular #PDF查看器



# 安装pip

sudo pacman -S python-pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip install name --user

wechat-uos scrot #微信客户端，截图
wireguard-tools #wireguard 配置生成

bluez bluez-utils #蓝牙
pulseaudio-bluetooth kmix #蓝牙音频
sudo systemctl enable --now bluetooth

downgrade #降级软件包
texlive-core #pdf

```
## 游戏
```shell
teeworlds #联机对战游戏
```

<!-- ##{"timestamp":1682524800}## -->
