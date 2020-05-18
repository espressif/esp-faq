# Espressif FAQ 文档

* [English Version](./README.md)
  
ESP-FAQ 是由乐鑫官方推出的针对常见问题的总结文档。

## ESP-FAQ 文档框架使用

### 语言支持

* 文档框架支持 reStructuredText 和 Markdown 轻量标记语言

### 配置环境并编译

* 测试验证环境使用 ubuntu 或 debian 系统，配置 python 环境为 `3.7`
* 推荐使用 python 虚拟环境，或者 docker 环境。
  
  ``` shell
  # 安装 python3.7 与 虚拟环境
  sudo apt-get install python3.7 python3.7-venv

  # 创建虚拟环境
  python3.7 -m venv ~/.pyenv3_7

  # 激活虚拟环境
  source ~/.pyenv3_7/bin/activate

  # 更新 pip
  pip install --upgrade pip
  
  # 安装 pip 组件
  pip install -r docs/requirements.txt
  
  # 编译中文版本
  cd docs/cn/ && make html && cd -

  # 编译英文版本
  cd docs/en/ && make html && cd -

  # 退出虚拟环境
  deactivate

  ```

### 文档结构

``` bash
docs
├── _static
│   ├── espressif-logo.svg    # 网页 log
│   └── theme_overrides.css   # 网页标签
├── cn
│   ├── config.py             # sphinx 配置
│   └── index.rst             #主目录
│   └── Makefile              #编译文件
│   └── *.md                  #具体文档
└── en
    ├── config.py             #sphinx 配置
    └── index.rst             #主目录
    └── Makefile              #编译文件
    └── *.md                  #具体文档
```

### 格式指南

* 请阅读代码 [格式指南](docs/README_CN.md)

## 其它参考资源

* 最新版的文档：https://docs.espressif.com/projects/esp-faq ，该文档是由本仓库 [docs 目录](docs) 构建得到。

* 可以前往 [esp32.com 论坛](https://esp32.com/) 提问，挖掘社区资源。

* 如果你在使用中发现了错误或者需要新的功能，请先[查看 GitHub Issues](https://github.com/espressif/esp-faq/issues)，确保该问题不会被重复提交。
* 如果你有兴趣为 ESP-FAQ 作贡献，请先阅读贡献指南。
