SD/SDIO/MMC 驱动
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

ESP8266 是否可以搭配 TF 卡使用？
----------------------------------------

  不建议这么使用。 

  - 虽然硬件上是可以连接的（通过 SPI 与 TF 卡通信），但是因为 ESP8266 的资源有限，根据不同的应用场景，很可能会出现内存不足等情况。所以不建议 ESP8266 搭配 TF 卡使用。 
  - 如果您只需要单 Wi-Fi 模组，并且要连接 TF 卡，建议使用 `ESP32-S2 <https://www.espressif.com/sites/default/files/documentation/esp32-s2_datasheet_cn.pdf>`_ 芯片。
