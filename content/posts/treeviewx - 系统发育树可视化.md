+++
date = "2024-04-19T00:00:00+08:00"
draft = false
title = """treeviewx - 系统发育树可视化"""
tags = ["软件", "生物信息学"]
+++

![image](https://github.com/seeu100/blog/assets/138188931/8808ddf8-2d6a-47c3-af99-10ad7d640f25)

TreeView X 是一款开源程序，专为Linux、Unix、Mac OS X和Windows操作系统设计，旨在显示和打印系统发育树。这款软件能够读取和显示NEXUS和Newick格式的树状结构文件，这两种格式是由PAUP*、ClustalX、TREE-PUZZLE以及其他相关程序生成的常见系统发育树输出格式。虽然它的功能相对于Mac Classic和Windows版的TreeView有所精简，但大致相当于TreeView的0.95版本水平。

TreeView X 提供了对系统发育树分支的排序功能，并且支持导出SVG矢量图像格式的树状图，使得用户能够清晰、高质量地展示和打印系统发育分析的结果。

此外，尽管该软件目前处于未受官方支持的状态，但对于使用Debian操作系统的用户来说，Charles Plessy维护了一个[针对Debian的TreeView X](http://packages.debian.org/unstable/science/treeviewx
)软件包。

Source: https://code.google.com/archive/p/treeviewx/
License: [ GNU GPL v2](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html)
Labels:
[CPlusPlus](https://code.google.com/archive/search?q=domain:code.google.com%20label:CPlusPlus) [visualisation](https://code.google.com/archive/search?q=domain:code.google.com%20label:visualisation) [phylogeny](https://code.google.com/archive/search?q=domain:code.google.com%20label:phylogeny)

## 编译安装
```shell
待补充
```
参考[Compiling.wiki](https://code.google.com/archive/p/treeviewx/wikis/Compiling.wiki)

## ArchLinux AUR编译安装

AUR: https://aur.archlinux.org/packages/treeviewx

```shell
# Maintainer: Guoyi Zhang <myname at malacology dot net>
# Contributor: Stunts <f.pinamartins@gmail.com>

pkgname=treeviewx
_pkgname=tv
pkgver=0.5.0
pkgrel=1
pkgdesc="Program to display phylogenetic trees"
arch=('x86_64')
url="https://code.google.com/archive/p/treeviewx/"
license=('GPL')
depends=('wxwidgets-gtk3')
makedepends=('git')
source=("git+https://github.com/rdmpage/treeviewx.git"
	"https://storage.googleapis.com/google-code-archive/v2/code.google.com/treeviewx/logo.png"
	"$pkgname.desktop"
	"arch.patch")
md5sums=('SKIP'
         '52f1937a3e0d194dba9fc00f87105ca7'
         '5045bd3f49af4088085e30c0270962d5'
         '096d5f3f7beb7e0ef749cca6fa60c601')
prepare(){
  cd $srcdir/$pkgname
  patch -np1 < $srcdir/arch.patch
  mv configure.{in,ac}
  echo "Roderic D.M. Page" > AUTHORS
  echo "version 0.5, Feb 4, 2023 Guoyi Zhang, BioArchLinux" > ChangeLog
}
build() {
  cd $srcdir/$pkgname
  autoupdate
  aclocal && automake -a && autoconf
  ./configure  --prefix=/usr
  make
}
package() {
  cd $srcdir/$pkgname
  make DESTDIR="$pkgdir" install
  install -Dm 644 $srcdir/logo.png $pkgdir/usr/share/pixmaps/$pkgname.png
  install -Dm 644 $srcdir/$pkgname.desktop $pkgdir/usr/share/applications/$pkgname.desktop
}
```
