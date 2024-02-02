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
------------------------------------------------------------------------

  It is not recommended to use ESP8266 together with TF card.

  - Although ESP8266 can be connected to TF card in hardware level (communicate through SPI), the chip may run out of memory in different application scenarios due to its limited resources. Thus, it is not recommended to use ESP8266 with TF card.
  - If all you need is a Wi-Fi-only module that can be connected to a TF card, we recommend using chips like `ESP32-S2 <https://www.espressif.com/sites/default/files/documentation/esp32-s2_datasheet_en.pdf>`_.

----------------

What is the maximum capacity of eMMC supported by ESP32-S3?
--------------------------------------------------------------------------------------------------------------

  2 TB is the limit for SD and eMMC protocols. There is no specific maximum capacity limit for the ESP32-S3. But if your application is built upon a filesystem, the maximum capacity may also be restricted by the filesystem.

---------------

Does ESP32 support DDR52, HS200, HS400, and SDR52 modes when it is connected to an eMMC card?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - At the frequency of 40 MHz, ESP32 supports the DDR52 mode and does not support other modes. For details, please refer to `Supported Speed Modes <https://docs.espressif.com/projects/esp-idf/en/release-v5.1/esp32/api-reference/peripherals/sdmmc_host.html#supported-speed-modes>`_.
