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
-------------------------------------------------------

  - ESP8266 未包含硬件脉冲计数模块，所以仅支持通过 GPIO 上升沿或下降沿中断实现脉冲计数。
  - ESP8266 芯片中 Wi-Fi 开启后由于优先级太高可能会导致 GPIO 采样出现真空，中断采集的计数丢数据。
  - 综上，在计数要求较为严格的场景推荐使用 ESP32 以及后续推出的芯片。

----------------------------------

ESP32-S3 可以通过 PCNT 实现频率为 200 k 的低电平脉冲计数吗？
-----------------------------------------------------------------------------------------------------------------------------------------------

  可以。

--------------------------

PCNT 可以在计数变化的时候产生中断吗？
--------------------------------------------------------------

  PCNT 只会在达到设置的阈值时才会产生中断，其他计数值只能通过轮询的方式读取。

--------------------------

ESP32-C3 不支持 PCNT 我该怎么办？
--------------------------------------------------------------

  可以使用软件 `knob <https://components.espressif.com/components/espressif/knob>`_ 进行 PCNT 的计数 。注意，该软件只能用于计数正交解码相关应用场景，并且计数频率不能太高。
