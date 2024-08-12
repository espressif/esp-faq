Inter-IC Sound (I2S)
====================

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

Does ESP32 support using crystal oscillator as the clock source of I2S?
----------------------------------------------------------------------------------------------------

  No. Please go to `ESP32 Technical Reference Manual <https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf>`_ to read about clock source configurations of I2S.

---------------

When working as the I2S master, does ESP32 support connection to the I2S slave that only has the three signal lines, I2S_DATA, I2S_SCK, and I2S_WS?
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
  Yes, but the connection to MCLK depends on the requirements of the codec chip on the other side.

------------------------

Does the I2S interface of ESP32-C3 series chips support the PDM RX mode?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - In the software driver, the I2S interface of ESP32-C3 series chips does not support the PDM RX mode. Unlike ESP32-S3, the PDM RX of ESP32-C3 does not have a module supporting converting from PDM to PCM, which means the acquired data is in the RAW PDM format. The data in this format can't be used directly in most cases.

----------------

Can the input and output BCK pin of ESP32-S3 I2S use the same pin?
-------------------------------------------------------------------------------------------------------------------------------------------------------------

  Yes. In the duplex mode, TX and RX achieve duplex functionality by binding these two signals to the same pin.

----------------

Is there a difference between using the Audio PLL (APLL) and PLL in I2S?
-------------------------------------------------------------------------------------------------------------------------------------------------------------

  APLL and PLL clock sources do not show a significant difference at lower sampling rates (144 kHz and below).
