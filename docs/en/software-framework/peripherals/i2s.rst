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
---------------------------------------------------------------------------------------------------

  No. Please go to `ESP32 Technical Reference Manual <https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf>`_ to read about clock source configurations of I2S.