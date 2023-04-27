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
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - It will restart when the input level is lower than 0.6 V for more than 200 μs.
  
---------------------

According to the schematic of ESP32-LyraT-Mini, the analog output of the ES8311 codec chip is connected to the input of the ES7243 ADC chip. What is the purpose of this?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The hardware acquisition circuit of the AEC reference signal simultaneously transmits the DAC output of the Codec (ES8311) to the speaker PA and the ADC (ES7243) AINLP/N, of which the signal collected would be send back to the ESP32 as the reference signal for the AEC algorithm.
  
-----------------

When using the ESP32-MINI-1 module, the serial port printed the follows log when powered on. What could be the reason?
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

---------------

Which GPIO is connected to the RGB LED of the 
`ESP32-S3-DevKitC-1 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/hw-reference/esp32s3/user-guide-devkitc-1.html#esp32-s3-devkitc-1-v1-1>`_ development board?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The RGB LED on the `ESP32-S3-DevKitC-1 v1.0 <https://dl.espressif.com/dl/SCH_ESP32-S3-DEVKITC-1_V1_20210312C.pdf>`_ development board is connected to GPIO48.
  - The RGB LED on the `ESP32-S3-DevKitC-1 v1.1 <https://dl.espressif.com/dl/schematics/SCH_ESP32-S3-DevKitC-1_V1.1_20221130.pdf>`_ development board is connected to GPIO38.
  - The reason why the `ESP32-S3-DevKitC-1 v1.1 <https://dl.espressif.com/dl/schematics/SCH_ESP32-S3-DevKitC-1_V1.1_20221130.pdf>`_ development board changed the RGB LED pin to GPIO38 is that the `ESP32-S3R8V <https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf>`_ chip’s VDD_SPI voltage has been set to 1.8 V. Therefore, unlike other GPIOs, GPIO47 and GPIO48 in the VDD_SPI power domain of this chip also operate at 1.8 V.
