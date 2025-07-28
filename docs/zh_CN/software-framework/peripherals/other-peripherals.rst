其他外设
=================

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

REF_TICK 时钟频率可以修改吗 ?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32 | ESP32-S2 | ESP32-C3:

  不可以修改，REF_TICK 时钟是固定的。

--------------

ESP32 是否⽀持 PCI-E 协议？
-------------------------------------

  ESP32 不支持 PCI-E 协议。

-----------------

ESP32-P4 是否支持视频编解码？
-----------------------------------------------------------------------------------------

  支持 JPEG 硬件编解码、H.264 硬件编码和 H.264 软件解码。

-----------------

ESP32-P4 如何使用比特调节器？
-----------------------------------------------------------------------------------------

  比特调节器驱动已经公开发布，请参考 `比特调节器 (BitScrambler) 驱动 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32p4/api-reference/peripherals/bitscrambler.html>`_。当前 RMT 外设已支持比特调节器。
