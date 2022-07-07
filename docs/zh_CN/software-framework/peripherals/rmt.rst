红外遥控接收器 (RMT)
=========================

:link_to_translation:`en:[English]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

--------------

RMT 中如何将时钟修改为 REF_TICK?
--------------------------------------------------------------------------------------------
  :CHIP\: ESP32 | ESP32-S2 | ESP32-C3:

  可以调用 `rmt_set_source_clk <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/peripherals/rmt.html?highlight=rmt_set_source_clk#_CPPv418rmt_set_source_clk13rmt_channel_t16rmt_source_clk_t>`_ 接口设置。