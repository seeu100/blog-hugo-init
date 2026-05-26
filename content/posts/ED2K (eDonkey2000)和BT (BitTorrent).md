+++
date = "2024-04-19T00:00:00+08:00"
draft = false
title = """ED2K (eDonkey2000)和BT (BitTorrent)"""
tags = ["知识"]
+++

### ED2K (eDonkey2000)

eD2k，全称为“eDonkey2000 network”，是一个早期且知名的点对点（P2P）文件共享协议及网络，由美国程序员摩西·加龙（Moses_Galoon）和杰里米·齐默尔曼（Jeremy Zawodny）创建，并随着他们的应用程序eDonkey2000客户端流行起来。这个网络允许用户通过互联网直接从其他用户的计算机上下载或上传数据，尤其适用于分享大型文件，例如音乐、电影、软件、文档等。

虽然eDonkey2000客户端不再维护更新，但有许多其他的P2P软件如eMule、aMule等依然支持eD2k协议。

### BT (BitTorrent)

**BitTorrent (BT)** 是另一种广受欢迎的P2P文件共享协议，由布拉姆·科恩（Bram Cohen）于2001年发明。BT协议的核心特点是通过.torrent文件引导下载，该文件包含了元数据信息，如文件名、大小、哈希值等。不同于ED2K依赖于中央服务器索引或者直接的IP寻址，BT使用分布式哈希表（DHT）技术来定位文件的种子和参与者。

用户使用BT下载软件（如uTorrent、BitComet、Transmission等）下载和上传文件。

### BT下载软件

常见的BT下载软件有：

- **uTorrent**: 体积小巧、功能强大的BT客户端，拥有简洁易用的界面和丰富的设置选项。
- **BitComet**: 支持HTTP/FTP下载、磁力链接以及BT种子下载，还有缓存、预下载等功能。
- **Transmission**: 开源跨平台的轻量级BT客户端，界面简洁，特别受到Linux和Mac OS X用户的喜爱。
- **qBittorrent**: 开源的跨平台BT客户端，提供了类似uTorrent的功能，并强调隐私保护和无广告特性。
- **迅雷**：国内常用，速度较快，但因只下载不上传被称为“吸血雷”。在P2P网络中，公平性原则通常要求用户在下载的同时上传文件片段给其他用户，以保持网络的活力和整体速度。

