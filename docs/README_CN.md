# 格式指南

* [English Version](./README.md)

## 新增文档

* 将新增文件 `new.md` 中英文档分别复制到 cn 与 en 目录中
* 在 _static 目录中新增 `new` 文件夹用以存放图片
* 在 index.rst 文件中添加文档索引路径

  ``` rst
  ESP-FAQ
  =============

  .. role:: bolditalics
  :class: bolditalics

  | Espressif 常见问题.

  .. toctree::
  :hidden:

  NEW <new>>
  ```

## 新增 Q & A

* 根据示例模板整理 Q & A

  ``` Markdown
  ## ESP-IDF 是否支持 ESP8266 芯片

  - `Q:`
    - ESP-IDF 是否支持 ESP8266 芯片 ？

  - `A:`
    - ESP-IDF 不支持 ESP8266 芯片，但 ESP8266_RTOS_SDK SDK 中 release/v3.0 以后的版已更换为 ESP-IDF 风格，部分组件已经兼容支持。
    ```

* 将 QA 问题对添加对应分类 `*.md` 文档中
