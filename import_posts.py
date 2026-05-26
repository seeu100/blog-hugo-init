#!/usr/bin/env python3
import os
import re
from pathlib import Path

# 配置
OLD_BLOG_DIR = Path('/home/erwa/3-git/github/blog-hugo/old-blog/backup')
NEW_POSTS_DIR = Path('/home/erwa/3-git/github/blog-hugo/content/posts')
INDEX_HTML_PATH = Path('/home/erwa/3-git/github/blog-hugo/old-blog/docs/index.html')

def parse_index_html(html_path):
    """从 index.html 中解析博文的标题、标签和日期信息"""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 匹配博文条目
    pattern = r'<a class="SideNav-item[^"]*" href="post/(\d+)\.html">.*?<span class="listTitle">(.*?)</span>.*?<div class="listLabels">(.*?)</div>.*?</a>'
    matches = re.findall(pattern, content, re.DOTALL)
    
    posts_info = {}
    for post_id, title, labels_html in matches:
        # 提取标签
        tag_pattern = r'href="tag\.html#([^"]+)">(.*?)</a>'
        tags = [tag_name for _, tag_name in re.findall(tag_pattern, labels_html)]
        
        # 提取日期 - 使用更宽松的匹配模式
        date_pattern = r'<span class="Label LabelTime[^>]*>([^<]+)</span>'
        date_match = re.search(date_pattern, labels_html)
        date = date_match.group(1).strip() if date_match else '2024-01-01'
        
        posts_info[title] = {
            'tags': tags,
            'date': date,
            'post_id': post_id
        }
    
    return posts_info

def sanitize_filename(name):
    """清理文件名，移除非法字符"""
    name = name.lstrip(' -.')
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        name = name.replace(char, '-')
    while '--' in name:
        name = name.replace('--', '-')
    return name.strip('-')

def create_hugo_post(old_file, new_dir, posts_info):
    """将旧博文转换为 Hugo 文章格式"""
    # 获取文件名（不含扩展名）
    title = old_file.stem
    
    # 获取该博文的信息
    post_info = posts_info.get(title, {})
    tags = post_info.get('tags', [])
    date = post_info.get('date', '2024-01-01')
    
    # 生成安全的文件名
    safe_name = sanitize_filename(title)
    if not safe_name:
        safe_name = 'post'
    
    # 读取旧文件内容
    with open(old_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 创建 tags 字段
    tags_str = ''
    if tags:
        # 对标签中的特殊字符进行转义
        escaped_tags = [tag.replace('"', '\\"') for tag in tags]
        tags_str = '\ntags = ["%s"]' % '", "'.join(escaped_tags)
    
    # 创建 Hugo 格式的内容
    # 使用 TOML 的多行字符串语法来避免单引号转义问题
    # TOML 多行字符串使用三引号
    hugo_content = '''+++
date = "%s"
draft = false
title = """%s"""%s
+++

%s
''' % (date + 'T00:00:00+08:00', title, tags_str, content)
    
    # 生成新文件路径
    new_filename = f"{safe_name}.md"
    new_path = new_dir / new_filename
    
    # 处理重复文件名
    counter = 1
    while new_path.exists():
        new_filename = f"{safe_name}-{counter}.md"
        new_path = new_dir / new_filename
        counter += 1
    
    # 写入新文件
    with open(new_path, 'w', encoding='utf-8') as f:
        f.write(hugo_content)
    
    return new_path, tags

def main():
    # 确保目标目录存在
    NEW_POSTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # 解析 index.html 获取博文信息
    print("正在解析 index.html...")
    posts_info = parse_index_html(INDEX_HTML_PATH)
    print(f"解析到 {len(posts_info)} 篇博文的元数据")
    
    # 获取所有旧博文文件
    md_files = sorted(OLD_BLOG_DIR.glob('*.md'))
    
    if not md_files:
        print("没有找到旧博文文件")
        return
    
    print(f"找到 {len(md_files)} 篇旧博文文件")
    print("=" * 60)
    
    imported_count = 0
    no_meta_count = 0
    
    for md_file in md_files:
        try:
            new_path, tags = create_hugo_post(md_file, NEW_POSTS_DIR, posts_info)
            tags_str = f" [标签: {', '.join(tags)}]" if tags else ""
            print(f"✓ 导入: {md_file.name}{tags_str}")
            imported_count += 1
            if not tags:
                no_meta_count += 1
        except Exception as e:
            print(f"✗ 失败: {md_file.name} - {str(e)}")
    
    print("=" * 60)
    print(f"成功导入 {imported_count} 篇博文")
    if no_meta_count > 0:
        print(f"其中 {no_meta_count} 篇博文未找到标签信息")

if __name__ == '__main__':
    main()
