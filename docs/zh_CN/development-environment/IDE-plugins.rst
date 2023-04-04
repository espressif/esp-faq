IDE 插件
========

:link_to_translation:`en:[English]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

--------------

Arduino IDE 如何添加 ESP32 开发板？
------------------------------------

  - 关于 Arduino-ESP32 的安装指南，请参考 `arduino-ide 入门指南 <https://docs.espressif.com/projects/arduino-esp32/en/latest/getting_started.html>`_。
  - 关于 Arduino IDE 添加开发板，请参考 `arduino Cores <https://www.arduino.cc/en/Guide/Cores>`_。

-------------------------

使用 Arduino IDE 开发平台，如何读取 ESP32 出厂自带的 Wi-Fi 的 MAC 地址？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Arduino-ESP32 开发框架为：https://github.com/espressif/arduino-esp32。
  - 使用 WiFi.macAddress() 获取 ESP32 的 Wi-Fi 的 MAC 地址。
  - 还可以参考 `WiFiClientStaticIP 例程 <https://github.com/espressif/arduino-esp32/blob/a59eafbc9dfa3ce818c110f996eebf68d755be24/libraries/WiFi/examples/WiFiClientStaticIP/WiFiClientStaticIP.ino>`_。

-------------------------

如何使用 Flash 下载工具将基于 Arduino 开发生成的 bin 文件烧录到 ESP32？
------------------------------------------------------------------------------------------------

  - 请前往 ``File`` -> ``Preferences`` -> ``Show verbose output during`` 勾选 ``compilation``，编译成功后，会打印一条 Python 烧录命令，其中包含待烧录的 bin 文件以及对应的烧录地址。
  - 在乐鑫官网的 `工具 <https://www.espressif.com/zh-hans/support/download/other-tools>`_ 页面下载 Flash 下载工具，使用 Flash 下载工具烧录时选择 bin 文件，输入对应的烧录地址即可。
