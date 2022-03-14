Development board
=================

:link_to_translation:`zh_CN:[中文]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

--------------------

How long does it take for the ESP-WROOM-02D module to restart after the reset signal?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - It will restart when the input level is lower than 0.6 V for more than 200 μs.
  
---------------------

According to the schematic of ESP32-LyraT-Mini, the analog output of the ES8311 codec chip is connected to the input of the ES7243 ADC chip. What is the purpose of this?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - To use the ES7243 ADC chip to obtain the necessary input reference signal for AEC.
  
-----------------

When using the ESP32-MINI-1 module, the serial port printed the follows log when powered on. What is the reason?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

      rst:0x10 (RTCWDT_RTC_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
      invalid header: 0xffffffff
      invalid header: 0xffffffff
      invalid header: 0xffffffff
      invalid header: 0xffffffff
      invalid header: 0xffffffff
      invalid header: 0xffffffff
      invalid header: 0xffffffff
      invalid header: 0xffffffff
      ets Jul 29 2019 12:21:46

  - The reason could be flash is not programmed.
