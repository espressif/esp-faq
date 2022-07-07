脉冲计数器 (PCNT)
=======================

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

ESP8266 可以实现脉冲计数吗？
------------------------------------------------------

  - ESP8266 未包含硬件脉冲计数模块，所以仅支持通过 GPIO 上升沿或下降沿中断实现脉冲计数。
  - ESP8266 芯片中 Wi-Fi 开启后由于优先级太高可能会导致 GPIO 采样出现真空，中断采集的计数丢数据。
  - 综上，在计数要求较为严格的场景推荐使用 ESP32 以及后续推出的芯片。