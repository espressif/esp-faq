Zigbee
======

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

ESP32-H2 和 ESP32-C6 的 Zigbee 协议栈在干扰下是否支持自动跳频？  
-----------------------------------------------------------------------------------------------------------

  Zigbee 协议本身不要求自动跳频。但可通过应用层实现：周期性检测信道质量，若干扰严重，协调整个网络迁移到新信道。