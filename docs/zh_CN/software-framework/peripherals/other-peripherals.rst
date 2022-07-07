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
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32 | ESP32-S2 | ESP32-C3:

  不可以修改，REF_TICK 时钟是固定的。

--------------

ESP32 是否⽀持 PCI-E 协议？
-------------------------------------

  ESP32 不支持 PCI-E 协议。

-------------------

使用 ILI9488 LCD 屏幕测试 `屏幕 <https://github.com/espressif/esp-iot-solution/tree/master/examples/screen>`_ 例程，是否支持 9-bit 总线和 18-bit 色深？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ILI9488 驱动芯片可以支持 9-bit 总线和 18-bit 色深，但目前我们的驱动只支持 8-bit 总线和 16-bit 色深。可根据 ILI9488 数据手册自行修改驱动，来实现 9-bit 总线和 18-bit 色深的支持。