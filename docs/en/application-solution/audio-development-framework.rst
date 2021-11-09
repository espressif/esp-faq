Audio development framework
===========================

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

What is the maximum power of supported speakers for ESP32 series audio development board?
--------------------------------------------------------------------------------------------------

  - ESP32 development board uses NS4150 PA by default, and its maximum power is 3 W according to its datasheet.

--------------------

Does Alexa solution have certain requirements for environmental noise?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The current Espressif voice solution can meet the environmental requirements of a signal-to-noise ratio of less than 5dB, and for some fixed noise scenarios, it can also be less than 0dB (need to be optimized for the actual product).
