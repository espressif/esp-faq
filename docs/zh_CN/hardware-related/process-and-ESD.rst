工艺与防护
==========

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

ESP32 ESD 测试注意事项有哪些？
---------------------------------

  - 请注意测试时，需要稳定的 3.3 V 电压，EN trace 如果太长，容易导致重启。
  - 如果遇到模组无反应，请确认测试的空气放电或接触放电的电压是多大。

