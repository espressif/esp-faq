# Espressif FAQ 文档

[![Documentation Status](https://readthedocs.com/projects/espressif-esp-faq-zh-cn/badge/?version=latest)](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/?badge=latest)

* [English Version](./README.md)
  
ESP-FAQ 是由乐鑫官方推出的针对常见问题的总结文档。

## 文档托管

* English: https://docs.espressif.com/projects/espressif-esp-faq/en/latest/
* 中文: https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/

## ESP-FAQ 文档框架

### 语言支持

* 文档框架支持 reStructuredText 和 Markdown 轻量标记语言。

### 文档结构

``` bash
docs
├── _static
│   ├── espressif-logo.svg       # 网页徽标
│   └── theme_overrides.css      # 网页样式表
├── zh_CN
│   ├── _static                  # 内联资源
│   ├── instruction              # 使用说明
│   ├── commercial-faq           # 商务问题
│   ├── development-environment  # 开发环境
│   ├── application-solution     # 应用方案
│   ├── hardware-related         # 硬件相关
│   ├── software-framework       # 软件平台
│   ├── test-verification        # 测试验证
│   ├── config.py                # 配置文件
│   ├── Makefile                 # 编译文件
│   └── index.rst                # 主目录
└── en
    ├── _static                  # 内联资源
    ├── instruction              # 使用说明
    ├── commercial-faq           # 商务问题
    ├── development-environment  # 开发环境
    ├── application-solution     # 应用方案
    ├── hardware-related         # 硬件相关
    ├── software-framework       # 软件平台
    ├── test-verification        # 测试验证
    ├── config.py                # 配置文件
    ├── Makefile                 # 编译文件
    └── index.rst                # 主目录
```

## 其它参考资源

* 可以前往 [esp32.com 论坛](https://esp32.com/) 提问，挖掘社区资源。

* 如果你在使用中发现了错误或者需要新的功能，请先[查看 GitHub Issues](https://github.com/espressif/esp-faq/issues)，确保该问题不会被重复提交。

* 如果你有兴趣为 ESP-FAQ 作贡献，请先阅读[贡献指南](https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/instruction/document-contribution.html)。
