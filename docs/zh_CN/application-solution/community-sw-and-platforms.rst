社区软件平台
============

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

ESP32-SOLO 是否可以在 Arduino 软件上进行开发？
----------------------------------------------

  - 目前 ESP32-SOLO 尚不支持在 Arduino 软件上进行开发。
  - 如果您非要使用 Arduino 进行构建代码，可以将 Arduino-esp32 用作 `ESP-IDF的组件 <https://github.com/espressif/arduino-esp32/blob/master/docs/esp-idf_component.md>`_ 进行开发测试。
