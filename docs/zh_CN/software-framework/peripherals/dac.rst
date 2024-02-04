数字模拟转换器 (DAC)
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

ESP32-S2-Saola-1 使用 DAC 输出时，采用 3.3 V 进行供电，为什么实际测试电压只有 3.1 V？
-----------------------------------------------------------------------------------------------------------

  由于存在内部压降，且存在片间差异，即使使用 3.3 V 供电，实际最大输出只有 3.2 V 左右。
