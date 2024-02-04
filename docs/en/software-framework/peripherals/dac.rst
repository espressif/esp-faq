Digital-to-Analog Converter (DAC)
=================================

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

When using DAC output for ESP32-S2-Saola-1, the power supply is 3.3 V. But the actual tested voltage is only 3.1 V. Why?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Due to the presence of internal voltage drop and inter-chip differences, even when powered by 3.3 V, the actual maximum output is only around 3.2 V.
