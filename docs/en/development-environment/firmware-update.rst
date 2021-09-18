Firmware update
===============

:link_to_translation:`zh_CN:[中文]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

----------------------

How does ESP32 set Flash SPI to QIO mode?
----------------------------------------------------------------------------------------------

  - It can be set in configuration terminal through "menuconfig -> Serial flasher config -> Flash SPI mode" , the corresponding API is esp_image_spi_mode_t();
  - It also can be configured in the `Flash download tools <https://www.espressif.com/sites/default/files/tools/flash_download_tool_v3.8.8_0.zip>`_ interface.
  
