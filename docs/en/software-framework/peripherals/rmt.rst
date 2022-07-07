Remote Control Transceiver (RMT)
================================

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

How to change the clock to REF_TICK in RMT?
---------------------------------------------------------------------------------------------
  :CHIP\: ESP32 | ESP32-S2 | ESP32-C3:

  By using the `rmt_set_source_clk <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/rmt.html?highlight=rmt_set_source_clk#_CPPv418rmt_set_source_clk13rmt_channel_t16rmt_source_clk_t>`_ interface.