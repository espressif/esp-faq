Peripherals
============

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

Taken ESP-WROOM-S2 as the slave device and STM32 as MCU, is it possible to download through SPI interface?
---------------------------------------------------------------------------------------------------------------

  No, we use UART0 to download by default. You can also design OTA support yourself in firmware.

--------------

What is the maximum speed supported by the SDIO interface?
------------------------------------------------------------

  The maximum clock speed supported by the hardware SDIO slave module is 50 MHz. As SDIO specifies use of quad data lines, the effective maximum bit rate is 200 Mbps.

--------------

Does the hardware SDIO interface support SD cards?
----------------------------------------------------

  Please note that the SDIO hardware only supports the device or slave profile, i.e. it cannot act as a host to control SDIO devices such as SD cards.

--------------------

If I float the ADC pin and print out VDD3P3 value (65535), then the voltage of VDD3P3 should be 65535/1024 ≈ 63 V. Why this is not the correct voltage value?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ADC pins cannot be left floating, and the value measured by floating ADC pins is not the correct value.
  
