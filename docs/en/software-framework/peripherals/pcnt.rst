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

--------------------------

Can PCNT generate an interrupt when the count changes?
--------------------------------------------------------------

  PCNT will only generate an interrupt when it reaches the set threshold. Other count values can only be read by polling.

--------------------------

What should I do if ESP32-C3 doesn't support PCNT?
--------------------------------------------------------------

  The `knob <https://components.espressif.com/components/espressif/knob>`_ software can be used for PCNT counting. Please note that this software can only be used for counting in quadrature decoding related application scenarios, and the counting frequency should not be too high.

--------------------------

Can PCNT support multiple channels working simultaneously? Do signal and control necessarily need to be input in pairs?
----------------------------------------------------------------------------------------------------------------------------

  PCNT supports multiple channels working simultaneously. The signal and control do not necessarily have to be used in pairs. If you do not want to use control, you can set it to -1. The count mode is configured using `pcnt_channel_set_edge_action`.

-------------------

Is it possible to use ESP32 PCNT to calculate the time between two pulses?
--------------------------------------------------------------------------------------------------------------

  No, it's not possible. PCNT can only count pulses, it does not support calculating the time between two pulses. You can use RMT to calculate the time between two pulses.
