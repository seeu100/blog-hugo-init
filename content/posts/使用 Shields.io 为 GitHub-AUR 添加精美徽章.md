+++
date = "2024-01-01T00:00:00+08:00"
draft = false
title = """使用 Shields.io 为 GitHub-AUR 添加精美徽章"""
+++

## 关键要点

* Shields.io 提供多种 GitHub 徽章，显示存储库的动态信息，如星星数、分支数和贡献者数。
* 以下列出了一些常见的 GitHub 徽章示例，可直接在 Markdown 文件中使用。
* 徽章可通过查询参数自定义样式和颜色，增强视觉效果。

## Shields.io 简介

Shields.io 是一个提供简洁、一致且易读的徽章服务的平台，支持 SVG 和光栅格式的徽章。这些徽章可以轻松嵌入 GitHub 的 README.md 文件或其他网页中，用于展示项目指标。Shields.io 支持多种服务，包括持续集成工具、包注册表、分发平台、应用商店、社会网络、代码覆盖率服务和代码分析服务，每月服务超过 16 亿次图像请求，被许多知名的开源项目如 VS Code、Vue.js 和 Bootstrap 使用。

对于 GitHub 存储库，Shields.io 提供了动态徽章，这些徽章会根据存储库的实时数据自动更新，例如星星数、分支数、贡献者数量等。这些徽章不仅能提升 README 的视觉吸引力，还能快速传达项目状态，吸引潜在贡献者或用户。

## GitHub 徽章的获取与使用

Shields.io 的 GitHub 徽章主要通过特定的 URL 格式生成，例如 https://img.shields.io/github/stars/ollama/ollama，其中 ollama/ollama 需要替换为实际的 GitHub 用户名和存储库名称。以下是常见的 GitHub 徽章类型及其 Markdown 示例：

| 徽章名称            | 描述                         | 图标                                                                                   |
| ------------------- | ---------------------------- | -------------------------------------------------------------------------------------- |
| GitHub 主要语言     | 显示存储库使用的主要编程语言 | ![GitHub top language](https://img.shields.io/github/languages/top/ollama/ollama)        |
| GitHub 最后提交     | 显示存储库的最后提交日期     | ![GitHub last commit](https://img.shields.io/github/last-commit/ollama/ollama)           |
| GitHub 开放问题     | 显示存储库的开放问题数量     | ![GitHub issues](https://img.shields.io/github/issues/ollama/ollama)                     |
| GitHub 星星数       | 显示存储库的星星数量         | ![GitHub stars](https://img.shields.io/github/stars/ollama/ollama?style=flat)            |
| GitHub 提交数       | 显示存储库的提交数量         | ![GitHub commit activity](https://img.shields.io/github/commit-activity/t/ollama/ollama) |
| GitHub 贡献者       | 显示存储库的贡献者数量       | ![GitHub contributors](https://img.shields.io/github/contributors/ollama/ollama)         |
| GitHub 创建日期     | 显示存储库的创建日期         | ![GitHub Created At](https://img.shields.io/github/created-at/ollama/ollama)             |
| GitHub 分支数       | 显示存储库的分支数量         | ![GitHub forks](https://img.shields.io/github/forks/ollama/ollama?style=flat)            |
| GitHub 开放拉取请求 | 显示存储库的开放拉取请求数量 | ![GitHub pull requests](https://img.shields.io/github/issues-pr/ollama/ollama)           |
| GitHub 许可证       | 显示存储库的许可证信息       | ![GitHub license](https://img.shields.io/github/license/ollama/ollama)                   |
| GitHub 发布版本     | 显示存储库的最新发布版本     | ![GitHub release](https://img.shields.io/github/v/release/ollama/ollama)                 |
| GitHub 语言数量     | 显示存储库使用的编程语言数量 | ![GitHub language count](https://img.shields.io/github/languages/count/ollama/ollama)    |

```markdown
![GitHub top language](https://img.shields.io/github/languages/top/ollama/ollama)
![GitHub last commit](https://img.shields.io/github/last-commit/ollama/ollama)
![GitHub issues](https://img.shields.io/github/issues/ollama/ollama)
![GitHub stars](https://img.shields.io/github/stars/ollama/ollama?style=flat)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/ollama/ollama)
![GitHub contributors](https://img.shields.io/github/contributors/ollama/ollama)
![GitHub Created At](https://img.shields.io/github/created-at/ollama/ollama)
![GitHub forks](https://img.shields.io/github/forks/ollama/ollama?style=flat)
![GitHub pull requests](https://img.shields.io/github/issues-pr/ollama/ollama)
![GitHub license](https://img.shields.io/github/license/ollama/ollama)
![GitHub release](https://img.shields.io/github/v/release/ollama/ollama)
![GitHub language count](https://img.shields.io/github/languages/count/ollama/ollama)
```

这些徽章的 URL 格式可以通过 Shields.io 网站上的搜索栏或分类浏览找到，具体操作是点击徽章预览，填写必要的路径参数（如用户名和存储库名），然后可选地自定义标签、颜色等，最后复制生成的 Markdown 代码。

## 常见的 AUR 徽章类型

| **徽章名称** | **描述**            | 图标                                                                                                                                                  |
| ------------------ | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| AUR 版本           | 显示 AUR 包的当前版本     | ![AUR 版本](https://img.shields.io/aur/version/linuxqq)                                                                                                 |
| AUR 许可证         | 显示 AUR 包的许可证信息   | ![AUR 许可证](https://img.shields.io/aur/license/linuxqq)                                                                                               |
| AUR 最后修改时间   | 显示 AUR 包的最后修改日期 | ![AUR 最后修改](https://img.shields.io/aur/last-modified/linuxqq)                                                                                       |
| AUR 维护者         | 显示 AUR 包的当前维护者   | ![AUR 维护者](https://img.shields.io/aur/maintainer/linuxqq)                                                                                            |
| AUR 投票数         | 显示 AUR 包的投票数量     | ![AUR 投票](https://img.shields.io/aur/votes/linuxqq)                                                                                                   |
| AUR 依赖           | 显示 AUR 包的依赖         | ![AUR 依赖](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Faur.archlinux.org%2Frpc%2Fv5%2Finfo%2Flinuxqq&query=%24..Depends&label=depends) |

```markdown
![AUR 最后修改](https://img.shields.io/aur/last-modified/linuxqq)
![AUR 版本](https://img.shields.io/aur/version/linuxqq)
![AUR 许可证](https://img.shields.io/aur/license/linuxqq)
![AUR 维护者](https://img.shields.io/aur/maintainer/linuxqq)
![AUR 投票](https://img.shields.io/aur/votes/linuxqq)
![AUR 依赖](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Faur.archlinux.org%2Frpc%2Fv5%2Finfo%2Flinuxqq&query=%24..Depends&label=depends)`
```

- 注意事项：由于 AUR API 有每日 4000 次请求的速率限制，Shields.io 可能会因高流量而偶尔返回 invalid 值。建议合理设置缓存时间（如 cacheSeconds=3600）以减少请求。
- API来源：https://aur.archlinux.org/rpc/swagger

## 自定义徽章

Shields.io 允许通过查询参数自定义徽章的外观，例如更改样式、颜色或添加徽标。以下是一些常见自定义选项：

* 样式：可选择 flat、plastic、flat-square、for-the-badge 或 social。
  示例：`?style=for-the-badge`![GitHub stars](https://img.shields.io/github/stars/ollama/ollama?style=for-the-badge)
* 颜色：可以指定徽章的颜色，例如 green 或 blue。
  示例：`?style=flat-square&color=green`![GitHub stars](https://img.shields.io/github/stars/ollama/ollama?style=flat-square&color=green)
* 徽标：可以添加徽标，例如 GitHub 的徽标。
  示例：`?style=plastic&color=red&logo=github`![GitHub stars](https://img.shields.io/github/stars/ollama/ollama?style=plastic&color=red&logo=github)
* 缓存时间：通过 cacheSeconds 参数设置 HTTP 缓存时间，默认值根据徽章类型推断，低于默认值的设置会被忽略。
  示例：`![GitHub stars](https://img.shields.io/github/stars/ollama/ollama?cacheSeconds=3600)`

更多自定义选项可以在 [Shields.io 文档](https://shields.io/docs/) 中找到，文档提供了详细的参数说明和示例。

## 其他相关信息

Shields.io 的 GitHub 徽章是动态生成的，依赖于 GitHub API，因此可能受到速率限制的影响。为了提高速率限制，用户可以授权 Shields.io 的 GitHub 应用，具体操作可在 [Shields.io GitHub 授权页面](https://img.shields.io/github-auth) 查看。

此外，Shields.io 还支持其他类型的徽章，例如静态徽章（通过自定义文本和颜色生成）和端点徽章（通过 YAML 或 JSON 数据动态生成），但本文重点关注 GitHub 存储库的动态徽章。

## 结论与建议

使用 Shields.io 的 GitHub 徽章可以显著提升你的存储库 README 的专业性和吸引力，快速展示项目指标如星星数、贡献者数量等。博主可以根据需要选择上述列出的常见徽章，并通过自定义选项调整样式和颜色，以匹配项目品牌。

如果需要更多徽章类型，建议访问 [Shields.io 网站](https://shields.io/)，使用搜索栏或浏览分类找到适合的徽章。此外，Shields.io 的开源性质也欢迎社区贡献，相关信息可在 [Shields.io GitHub 仓库](https://github.com/badges/shields) 查看。

## 参考

* [Shields.io 官方主页](https://shields.io/)
* [Shields.io 文档页面](https://shields.io/docs/)
* [Shields.io GitHub 仓库](https://github.com/badges/shields)
* [md-badges GitHub 仓库](https://github.com/inttter/md-badges)
* [markdown-badges GitHub 仓库](https://github.com/Ileriayo/markdown-badges)
* [Shields.io GitHub 授权页面](https://img.shields.io/github-auth)

