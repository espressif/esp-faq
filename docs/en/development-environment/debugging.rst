Debugging
=========

:link_to_translation:`zh_CN:[中文]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>


How to troubleshoot in ESP32 Boot mode？
------------------------------------------

  By default, the boot information of ESP32-WROVER, which uses 1.8 V flash and psram, is ``0x33`` and ``0x23`` in Download mode. Besides, the boot information of other modules, which use 3.3 V flash and psram, is ``0x13`` and ``0x03`` in Download mode by default. for detailed information, please refer to Section Strapping Pins in `ESP32 Series Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_.

  Thus, when ESP32 is started normally, its boot information should be ``0x13``, and the enabled pins are as the follows:
  - Pins: GPIO12，GPIO0，GPIO2，GPIO4，GPIO15，GPIO5
  - Levels: 0, 1, 0, 1, 0, 1