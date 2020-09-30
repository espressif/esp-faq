射频相关
========

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

ESP32 模组在 2.8 V 电源下运行，射频性能会有下降吗？
---------------------------------------------------

射频会不稳定。建议按照相应 `模组技术规格书 <https://www.espressif.com/zh-hans/support/documents/technical-documents>`_ 中说明的建议工作电压范围提供电压。

--------------

乐鑫芯片支持的调制方式有哪些？
---------------------------------------------------

  - ESP8266 芯片支持的调制方式有：BPSK/QPSK/16QAM/64QAM/DBPSK/DQPSK/CCK。
  - ESP32   芯片支持的调制方式有：BPSK/QPSK/16QAM/64QAM/DBPSK/DQPSK/CCK/GFSK Π/4-DQPSK 8-DPSK 。
  - ESP32-S2 芯片支持的调制方式有：BPSK/QPSK/16QAM/64QAM/DBPSK/DQPSK/CCK。
  
