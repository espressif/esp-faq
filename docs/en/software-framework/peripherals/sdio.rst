Secure Digital Input Output (SDIO)
==================================

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

What is the maximum speed supported by the SDIO interface?
--------------------------------------------------------------------------

  - The maximum clock speed supported by ESP32 SDIO is 50 MHz, and ESP32 SDIO supports the Quad mode at the maximum.
  - The maximum clock speed supported by ESP32-S3 SDIO is 80 MHz, and ESP32-S3 SDIO supports the Octal mode at the maximum.
  - The practical speed is influenced by the read and write speed of storage media at the same time.

--------------

Does the hardware SDIO interface support SD cards?
----------------------------------------------------------------------

  Please note that the SDIO hardware only supports the device or slave profile, i.e. it cannot act as a host to control SDIO devices such as SD cards.

--------------

What is the maximum capacity for ESP32 SD card?
-----------------------------------------------------------------------

  - In the SD3.01 Specifications, the SDXC card supports a maximum capacity of 2 TB (2048 GB).
  - The ESP32 SDMMC Host also complies with the SD3.01 Specifications, which means up to 2 TB areas of it can be accessed by peripherals. When accessing the card via SPI bus using the SDSPI driver, there are also 2 TB of areas can be accessed in hardware level.
  - In software level, the usable area of the card is also affected by the file system.

--------------

Is it possible to use ESP32 SD card together with flash & PSRAM?
---------------------------------------------------------------------------------------------

  - Yes, they can be used simultaneously when they apply different pins.
  - Note that when ESP32 uses the SDMMC host driver, the SDMMC Slot0 pins in the ESP32-WROOM and ESP32-WROVER modules conflict with the flash.

--------------

Does ESP-WROOM-S2 module support using SDIO as a slave?
---------------------------------------------------------------------------------------

  Yes, it does.

-----------------

Since ESP32-S2 has removed the SDIO interface, does it still support external TF card?
--------------------------------------------------------------------------------------------------------------------------------

  You can use the SPI2 or SPI3 interface to connect to an external TF card. When doing so, please use the SPI mode of the TF card.

----------------

Does ESP32-S2 support eMMC?
--------------------------------------------------------------------------------------------------

  :CHIP\: ESP32-S2:

  No.

----------------------

Does ESP32-S2 support SDIO as a slave?
-------------------------------------------------------------------------------------------

  ESP32-S2 has no SDIO interface and does not support SDIO as a slave.

----------------

How does ESP32 enable and disable the interrupt for the SDIO slave to receive data?
---------------------------------------------------------------------------------------------------------------------------

  The data reception of the SDIO slave is related to the state of the mounted buffer. After the data is received, you need to call `sdio_slave_recv_load_buf <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/sdio_slave.html#_CPPv424sdio_slave_recv_load_buf23sdio_slave_buf_handle_t>`_ to release the buffer. Otherwise, the SDIO host will not be able to continue to send data to the SDIO slave.

--------------

How to set the ESP32-C6 SDIO clock?
--------------------------------------------------------------------------------------------------

  The ESP32-C6 only supports SDIO slave mode, with the SDIO slave CLK dependent on the SDIO host settings.
