# Espressif FAQ 文档

* [English Version](./README.md)
  
ESP-FAQ 是由乐鑫官方推出的针对常见问题的总结文档。

## ESP-FAQ 文档框架

### 语言支持

* 文档框架支持 reStructuredText 和 Markdown 轻量标记语言。

### 文档结构

``` bash
docs
├── _static
│   ├── espressif-logo.svg    # 网页 log
│   └── theme_overrides.css   # 网页样式表
├── zh_CN
│   ├── get-started           # 入门指南
│   ├── application-solution  # 应用方案
│   ├── hardware-selection    # 选型参考
│   ├── sdk-framework         # SDK 框架
│   ├── test-verification     # 测试验证
│   ├── config.py             # sphinx 配置
│   ├── Makefile              # 编译文件
│   └── index.rst             # 主目录
└── en
    ├── get-started           # 入门指南
    ├── application-solution  # 应用方案
    ├── hardware-selection    # 选型参考
    ├── sdk-framework         # SDK 框架
    ├── test-verification     # 测试验证
    ├── config.py             # sphinx 配置
    ├── Makefile              # 编译文件
    └── index.rst             # 主目录
```

### 问题提交

* 请阅读 [问题提交指南](docs/README_CN.md)。

## 其它参考资源

* 最新版的文档：https://docs.espressif.com/projects/esp-faq/，该文档是由本仓库 [docs 目录](docs) 构建得到。

* 可以前往 [esp32.com 论坛](https://esp32.com/) 提问，挖掘社区资源。

* 如果你在使用中发现了错误或者需要新的功能，请先[查看 GitHub Issues](https://github.com/espressif/esp-faq/issues)，确保该问题不会被重复提交。
* 如果你有兴趣为 ESP-FAQ 作贡献，请先阅读贡献指南。
