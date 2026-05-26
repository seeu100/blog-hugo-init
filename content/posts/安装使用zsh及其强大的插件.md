+++
date = "2023-09-15T00:00:00+08:00"
draft = false
title = """安装使用zsh及其强大的插件"""
tags = ["Linux", "软件", "环境搭建"]
+++

### 安装

```sh
# 安装zsh及其插件（以archlinux为例）
sudo pacman -S zsh-autosuggestions zsh-syntax-highlighting zsh-theme-powerlevel10k zsh-history-substring-search zsh  zsh-completions
paru -S zsh-z-git #AUR

# 修改当前用户默认shell
chsh -s /usr/bin/zsh

# command-not-found钩子
sudo pacman -S pkgfile 
sudo pkgfile --update
```

<!--more-->
### 配置`.zshrc`

主要是将上面的插件放进环境变量里使其生效。

```sh
source /usr/share/doc/pkgfile/command-not-found.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.zsh
source /usr/share/zsh-theme-powerlevel10k/powerlevel10k.zsh-theme
source /usr/share/zsh/plugins/zsh-z/zsh-z.plugin.zsh 


# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
```

### `.zshrc`的其他有用选项：
```sh
alias diff 'diff --color=auto'
alias grep='grep --color=auto'
alias ls='ls --color=auto'

autoload -Uz compinit
compinit

zstyle ':completion:*' menu select

# zsh history setting
export HISTFILE="$HOME/.bash_history"
export HISTSIZE=1000000000
export SAVEHIST=$HISTSIZE
setopt HIST_IGNORE_DUPS

# fix zsh-autosuggestions
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=23'


bindkey -e #绑定emacs快捷键
bindkey ';' autosuggest-accept #按;自动补全命令建议

export EDITOR='vim'
```
<!-- ##{"timestamp":1694707200}## -->
