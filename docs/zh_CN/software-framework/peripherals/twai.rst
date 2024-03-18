双线汽车接口 (TWAI)
======================

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

在使用 ESP32 TWAI® 控制器时有哪些注意事项？
----------------------------------------------------------------------

  请参考 `《ESP32 系列芯片勘误表》 <https://www.espressif.com/sites/default/files/documentation/esp32_errata_cn.pdf>`_ > 章节 ESP32 TWAI 相关问题。

--------------

ESP32-S3 支持 CAN-FD 吗？
----------------------------------------------------------------------

  ESP32-S3 本身没有集成 CAN-FD 控制器，但用户仍然可以使用 SPI 接口的 CAN-FD 控制器，例如 MCP2518FD。