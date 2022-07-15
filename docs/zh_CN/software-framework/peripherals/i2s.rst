集成电路内置音频总线 (I2S)
===============================

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

ESP32 是否支持使用晶振作为 I2S 的时钟源？
-----------------------------------------------------------------------

  ESP32 不支持使用晶振作为 I2S 的时钟源，可阅读 `《ESP32 技术参考手册》 <https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_cn.pdf>`_  来了解 I2S 的时钟源配置。

---------------

若 I2S 从设备只有 I2S_DATA、I2S_SCK 和 I2S_WS 这三根信号线，ESP32 作为 I2S 主设备时，是否支持这种连接方式?
---------------------------------------------------------------------------------------------------------------------------------------
  
  支持，但是是否接 MCLK 要看对端编码解码芯片的要求。

