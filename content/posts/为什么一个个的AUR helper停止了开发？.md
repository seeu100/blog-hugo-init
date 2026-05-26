+++
date = "2022-04-27T00:00:00+08:00"
draft = false
title = """为什么一个个的AUR helper停止了开发？"""
tags = ["Linux", "开源", "思考"]
+++

## 更新
`yay`也停止更新了，现在用`paru`装软件。

无论说令人着迷的开源免费精神，还是利益至上的商业模式，都各有其优点吧。只是，看到一个个曾经很优秀的项目默默地逝去，总会很感伤。

## 缘起

去年就听到`yaourt`停止开发维护的传闻，当时没有在意，今天心血来潮想去看看为什么这些如此好用的开源工具为何会停止维护，这也是长久以来停留在我心中的一个疑问。

## 寻找

我去[AUR - yaourt](https://aur.archlinux.org/packages/yaourt/)看了一下，昨天还有更新呀！这不还在维护吗？

在搜索引擎搜到了这篇文章“[Yaourt 已死！在 Arch 上使用这些替代品](https://zhuanlan.zhihu.com/p/42287487)”，结合ArchWiki里的内容“[AUR helpers (简体中文)](https://wiki.archlinux.org/index.php/AUR_helpers_%28%25E7%25AE%2580%25E4%25BD%2593%25E4%25B8%25AD%25E6%2596%2587%29)和[AUR helpers](https://wiki.archlinux.org/index.php/AUR_helpers%23Comparison_table)”，差别有点大，英文wiki甚至说`aurman`停止维护了。

直接到[GitHub - archlinuxfr/yaourt](https://github.com/archlinuxfr/yaourt)里看，issues堆积了101个之多，最后一次提交已经是去年的事情了。

发现官方开发者8天前发布了决定近期将仓库归档的[决定](https://github.com/archlinuxfr/yaourt/issues/382%23issuecomment-475039781)，没想到还能见到`yaourt`最后一面，感谢辛苦的开发者。

然后又去`aurman`的github仓库看了下，在README文件里就有放弃维护的[声明](https://github.com/polygamma/aurman%23stopped-development-for-public-use)了。

## 原因

`yaourt`不再被archlinux用户支持的原因似乎是安全漏洞的问题，但是我感觉是很容易修复的。通过开发者的言语可以很明显知道其停止维护的原因，原因很简单，开发者觉得开发的功能已经足够他个人使用了，那些请求添加新功能和修复一些没必要的bug的issue实在太烦人了，`aurman`的维护者甚至直接把issues全部关闭了。

开发者并没有说会放弃使用其开发的工具，只是不再做面对公众的维护更新，仍会进行个人的一些更新。

这里就折射了开源软件开发的的一个痛点，那就是开发者所进行的开发和维护是没有任何回报的，这往往导致开发者失去开发的动力，我已经遇到好多好多开发状态几乎或者已经陷入停滞的开源项目了。而且无论哪里，伸手党都很多，真正会参与进开发的人，少之又少。

## yay - Yet another Yogurt

[yay](https://github.com/Jguer/yay)是一个用Go语言的简洁aur helper，模仿了`yaourt`的风格，是停止维护aur helper的开发者和很多arch用户目前推荐的。


> 首发于[知乎](https://zhuanlan.zhihu.com/p/60874343?msclkid=8d8c2860c5fe11ec88344355cf5ed1e2)。

<!-- ##{"timestamp":1650988800}## -->
