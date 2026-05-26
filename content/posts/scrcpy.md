+++
date = "2024-06-01T00:00:00+08:00"
draft = false
title = """scrcpy"""
tags = ["软件"]
+++

[scrcpy](https://github.com/Genymobile/scrcpy) 是一个用于控制和显示 Android 设备的桌面应用程序。它通过 USB（或 Wi-Fi）连接到设备，并在电脑上以高帧率显示设备屏幕，同时支持键盘和鼠标输入控制。

前提：确保设备已开启 **adb 调试**


## scrcpy wifi 无线连接设备

在手机上查看ip地址，，如`192.168.59.249`。

然后在电脑中运行：

```shell
$ adb tcpip 5555
restarting in TCP mode port: 5555
$ adb connect 192.168.59.249
connected to 192.168.59.249:5555
$ scrcpy
```


| 作用 | 参数  |
| ---- | --------- |
| 禁用音频转发 | `--no-audio` |
| 窗口置顶 | `--always-on-top` |
| 音频比特率 | `--audio-bit-rate=值` |
| 音频缓冲 | `--audio-buffer=ms` |
| 音频编解码器 | `--audio-codec=名称` |
| 音频编码器选项 | `--audio-codec-options=key[:类型]=值[,...]` |
| 特定音频编码器 | `--audio-encoder=名称` |
| 音频源 | `--audio-source=来源` |
| 音频输出缓冲 | `--audio-output-buffer=ms` |
| 视频比特率 | `-b, --video-bit-rate=值` |
| 相机尺寸比 | `--camera-ar=ar` |
| 指定相机ID | `--camera-id=id` |
| 相机朝向 | `--camera-facing=facing` |
| 高速相机模式 | `--camera-high-speed` |
| 相机尺寸 | `--camera-size=<宽>x<高>` |
| 相机帧率 | `--camera-fps=值` |
| 裁剪屏幕 | `--crop=宽:高:x:y` |
| 使用USB设备 | `-d, --select-usb` |
| 禁用屏保 | `--disable-screensaver` |
| 显示缓冲 | `--display-buffer=ms` |
| 指定显示ID | `--display-id=id` |
| 显示方向 | `--display-orientation=值` |
| 使用TCP/IP设备 | `-e, --select-tcpip` |
| 全屏启动 | `-f, --fullscreen` |
| 强制ADB转发 | `--force-adb-forward` |
| 转发所有点击 | `--forward-all-clicks` |
| 帮助 | `-h, --help` |
| 键盘模式 | `--keyboard=mode` |
| 关闭ADB | `--kill-adb-on-close` |
| 传统粘贴 | `--legacy-paste` |
| 列出摄像头 | `--list-cameras` |
| 列出相机尺寸 | `--list-camera-sizes` |
| 列出显示器 | `--list-displays` |
| 列出编码器 | `--list-encoders` |
| 锁定视频方向 | `--lock-video-orientation[=值]` |
| 视频最大尺寸 | `-m, --max-size=值` |
| 鼠标模式 | `--mouse=mode` |
| 最大帧率 | `--max-fps=值` |
| 无控制 | `-n, --no-control` |
| 无播放 | `-N, --no-playback` |
| 禁用音频播放 | `--no-audio-playback` |
| 无清理 | `--no-cleanup` |
| 取消剪贴板自动同步 | `--no-clipboard-autosync` |
| 错误时不降低分辨率 | `--no-downsize-on-error` |
| 不转发重复按键 | `--no-key-repeat` |
| 禁用mipmap | `--no-mipmaps` |
| 不启动设备 | `--no-power-on` |
| 禁用视频转发 | `--no-video` |
| 禁用视频播放 | `--no-video-playback` |
| 方向设置 | `--orientation=值` |
| OTG模式 | `--otg` |
| 端口设置 | `-p, --port=port[:port]` |
| 退出暂停配置 | `--pause-on-exit[=mode]` |
| 关闭时熄屏 | `--power-off-on-close` |
| 优先文本注入 | `--prefer-text` |
| FPS计数器 | `--print-fps` |
| 拖放文件目标路径 | `--push-target=path` |
| 录制屏幕 | `-r, --record=file.mp4` |
| 原始键事件注入 | `--raw-key-events` |
| 录制格式强制 | `--record-format=format` |
| 录像方向 | `--record-orientation=value` |
| 渲染驱动选择 | `--render-driver=name` |
| 音频需求 | `--require-audio` |
| 设备序列号 | `-s, --serial=serial` |
| 立即熄屏 | `-S, --turn-screen-off` |
| 快捷键组合 | `--shortcut-mod=key[+...][,...]` |
| 显示触摸反馈 | `-t, --show-touches` |
| TCP/IP重连配置 | `--tcpip[=ip[:port]]` |
| 镜像时间限制 | `--time-limit=seconds` |
| 隧道主机IP | `--tunnel-host=ip` |
| 隧道端口 | `--tunnel-port=port` |
| 版本信息 | `-v, --version` |
| 日志等级 | `-V, --verbosity=value` |
| v4l2输出 | `--v4l2-sink=/dev/videoN` |
| v4l2缓冲 | `--v4l2-buffer=ms` |
| 视频编解码器选择 | `--video-codec=name` |
| 视频编码器选项 | `--video-codec-options=key[:type]=value[,...]` |
| 特定视频编码器 | `--video-encoder=name` |
| 视频源选择 | `--video-source=source` |
| 保持唤醒 | `-w, --stay-awake` |
| 无边框窗口 | `--window-borderless` |
| 自定义窗口标题 | `--window-title=text` |
| 窗口初始位置 (X轴) | `--window-x=value` |
| 窗口初始位置 (Y轴) | `--window-y=value` |
| 窗口初始宽度 | `--window-width=value` |
| 窗口初始高度 | `--window-height=value` |
