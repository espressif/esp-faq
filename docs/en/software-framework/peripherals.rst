Peripherals
===========

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