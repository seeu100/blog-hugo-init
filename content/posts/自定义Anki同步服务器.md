+++
date = "2023-07-08T00:00:00+08:00"
draft = false
title = """自定义Anki同步服务器"""
tags = ["Linux", "环境搭建"]
+++

## 更新

现Anki自带Server功能，在Linux上直接命令行运行以下命令即可：
```shell
SYNC_USER1=username:password SYNC_PORT=8080 anki --syncserver
```
1. `SYNC_USER1=username:password`
   - 这个环境变量指定的是Anki同步服务器的一个用户凭证，其中`username`是用户名，`password`是对应用户的密码。在自建的Anki同步服务器环境中，通常会设置多个用户以便不同的Anki客户端通过验证连接到服务器进行数据同步。

2. `SYNC_PORT=8080`
   - 这个环境变量指定了Anki同步服务器监听的网络端口号。8080是一个常用的非标准HTTP端口，这里作为服务器监听客户端连接的入口点。

3. `anki --syncserver`
   - 这是启动Anki程序并启用同步服务器模式的命令行参数。当Anki以这种方式启动时，它将运行同步服务器服务，而不是打开图形界面应用，这样其他设备上的Anki客户端就可以通过先前设定的用户名、密码和端口号连接到此服务器进行同步操作。

## 旧方法：搭建Anki Server

项目地址：https://github.com/tsudoko/anki-sync-server

```shell
pkg install python git
git clone https://github.com/tsudoko/anki-sync-server.git anki
cd anki
git submodule update --init
cd anki-bundled
sed -i '/# Packaged commands/,$d' anki/sound.py
sed -i '/^pyaudio/d' requirements.txt
pip install -r requirements.txt
pip install webob
cd ..
python ankisyncctl.py adduser seeu100（改成自己的用户名）
python -m ankisyncd
nohup python -m ankisyncd > /dev/null & #后台运行

#手机上的同步地址和媒体同步地址：
#http://127.0.0.1:27701/
#http://127.0.0.1:27701/msync
#电脑上插件的同步地址：
#http://手机IP:27701/
```

<!-- ##{"timestamp":1688745600}## -->
