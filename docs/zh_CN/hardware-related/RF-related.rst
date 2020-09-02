射频相关
========

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

--------------

ESP32 模组在 2.8 V 电源下运行，射频性能会有下降吗？
---------------------------------------------------

射频会不稳定。建议按照\ `相应模组
datasheet <https://www.espressif.com/zh-hans/support/documents/technical-documents>`__
中说明的建议工作电压范围提供电压。
