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
-----------------------------------

  - arduino-esp32 使用引导链接  `arduino-ide <https://github.com/espressif/arduino-esp32/blob/master/docs/arduino-ide/boards_manager.md>`_。
  - Arduino IDE 添加开发板引导链接 `arduino Cores <https://www.arduino.cc/en/Guide/Cores>`_。

-------------------------

使用 Arduino IDE 开发平台，如何读取 ESP32 出厂自带的 Wi-Fi 的 MAC 地址？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - esp32-arduino 开发框架：https://github.com/espressif/arduino-esp32
  - 使用 WiFi.macAddress() 来获取 ESP32 的 Wi-Fi 的 MAC 地址；
  - Serial.println(WiFi.macAddress());`参考链接 <https://github.com/espressif/arduino-esp32/blob/a59eafbc9dfa3ce818c110f996eebf68d755be24/libraries/WiFi/examples/WiFiClientStaticIP/WiFiClientStaticIP.ino>`_。
  
