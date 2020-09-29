以太网
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

ESP32 以太网开发板示例出现 ` emac:Reset EMAC Timeout` 有哪些原因 ？
------------------------------------------------------------------------

  此 log 为 emac 初始化超时，与 RMII 时钟有关，建议排查硬件问题，查看 PHY 晶振是否虚焊等。
