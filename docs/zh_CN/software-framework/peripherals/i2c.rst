I2C 驱动程序
================

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

ESP8266 是否支持 I2C 从机模式？
------------------------------------------------

  不支持，如果要使用此功能，推荐使用 ESP32 或者 ESP32-S2 芯片。ESP32 参考示例：`i2C_self_test <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/i2c/i2c_self_test>`_。

--------------

ESP8266 I2C 是软件模拟的吗？
-------------------------------------

  ESP8266 I2C 是使用 GPIO 软件模拟。
