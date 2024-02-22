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

ESP32-SOLO-1 是否可以在 Arduino 软件上进行开发？
-------------------------------------------------

  - 目前 ESP32-SOLO-1 尚不支持在 Arduino 软件上进行开发。
  - 如果您仍倾向于使用 Arduino 构建代码，可以将 Arduino-esp32 用作 `ESP-IDF 的组件 <https://docs.espressif.com/projects/arduino-esp32/en/latest/esp-idf_component.html>`_ 进行开发测试。
