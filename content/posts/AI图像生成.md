+++
date = "2024-04-22T00:00:00+08:00"
draft = false
title = """AI图像生成"""
tags = ["待完善"]
+++

## 扩散模型
## GAN模型
## 一致性模型（Consistency Model）
其一，无需对抗训练（adversarial training），就能直接生成高质量的图像样本。

其二，相比扩散模型可能需要几百甚至上千次迭代，一致性模型只需要**一两步**就能搞定多种图像任务——

包括上色、去噪、超分等，都可以在几步之内搞定，而不需要对这些任务进行明确训练。（当然，如果进行少样本学习的话，生成效果也会更好）

项目地址：
https://github.com/openai/consistency_models

论文地址：
https://arxiv.org/abs/2303.01469

参考链接：
[1]https://twitter.com/alfredplpl/status/1646217811898011648
[2]https://twitter.com/_akhaliq/status/1646168119658831874
