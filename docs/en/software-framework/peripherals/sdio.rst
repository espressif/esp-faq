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
-------------------------------------------------------------------------

  The maximum clock speed supported by the hardware SDIO slave module is 50 MHz. As SDIO specifies use of quad data lines, the effective maximum bit rate is 200 Mbps.

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

  - Yes, they can be used simultaneously.
  - However, they do not share the same group of SDIO.

--------------

Does ESP-WROOM-S2 module support using SDIO as a slave?
---------------------------------------------------------------------------------------

  Yes, it does.

-----------------

Since ESP32-S2 has removed the SDIO interface, does it still support external TF card?
--------------------------------------------------------------------------------------------------------------------------------

  You can use the interface of SPI2/SPI3 to connect an external TF card. When doing so, please use the SPI mode of the TF card.

----------------

Does ESP32-S2 support eMMC?
--------------------------------------------------------------------------------------------------

  :CHIP\: ESP32-S2:

  No.

----------------------

Does ESP32-S2 support SDIO as a slave?
-------------------------------------------------------------------------------------------

  ESP32-S2 has no SDIO interface and does not support SDIO as a slave.