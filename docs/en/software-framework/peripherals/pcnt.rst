Pulse Counter (PCNT)
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

Does ESP8266 support pulse counting?
----------------------------------------------------------------

  - The ESP8266 does not include a hardware pulse counting module, thus only supports counting via the interrupt of GPIO rising edge or falling edge.
  - When Wi-Fi is turned on in ESP8266, it may cause a vacuum in the GPIO sampling due to its high priority, thus interrupting the collected counts and causing data loss.
  - In conclusion, it is recommended to use ESP32 and subsequent chips for scenarios with high counting demands.

----------------

Can ESP32-S3 realize low-level pulse counting with a frequency of 200 k?
------------------------------------------------------------------------------

  Yes.
