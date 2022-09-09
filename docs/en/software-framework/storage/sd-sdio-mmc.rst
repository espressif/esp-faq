SD/SDIO/MMC Driver
==================

:link_to_translation:`zh_CN:[中文]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

--------------

Is it possible to use ESP8266 together with TF card?
-----------------------------------------------------------------------

  It is not recommended to use ESP8266 together with TF card.

  - Although ESP8266 can be connected to TF card in hardware level (communicate through SPI), the chip may run out of memory in different application scenarios due to its limited resources. Thus, it is not recommended to use ESP8266 with TF card.
  - If all you need is a Wi-Fi-only module that can be connected to a TF card, it is recommended to use the `ESP32-S2 <https://www.espressif.com/sites/default/files/documentation/esp32-s2_datasheet_en.pdf>`_ chip instead.

----------------

What is the maximum capacity of eMMC supported by ESP32-S3?
--------------------------------------------------------------------------------------------------------------

  2 TB is the limit for SD and eMMC protocols. There is no specific maximum capacity limit for the ESP32-S3. But if your application is built upon a filesystem, the maximum capacity may also be restricted by the filesystem.
