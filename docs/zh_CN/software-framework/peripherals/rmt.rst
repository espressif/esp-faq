红外遥控接收器 (RMT)
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

RMT 中如何将时钟修改为 REF_TICK?
--------------------------------------------------------------------------------------------
  :CHIP\: ESP32 | ESP32-S2 | ESP32-C3:

  可以调用 `rmt_set_source_clk <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/peripherals/rmt.html?highlight=rmt_set_source_clk#_CPPv418rmt_set_source_clk13rmt_channel_t16rmt_source_clk_t>`_ 接口设置。

--------------

使用 ESP32 RMT 控制 WS2812 灯带，当与 Wi-Fi 或者蓝牙同时使用时，会出现部分数据帧异常的问题，该如何解决?
----------------------------------------------------------------------------------------------------------

  - 这个问题在非 ESP32-S3 的芯片上很难解决，因为 RMT 刷 LED（尤其是很多个 LED 的时候）严重依赖中断，且不支持 DMA，需要软件在中断切换 ping-pong buffer，如果中断没有及时响应，就会出现问题。默认情况下 (即只设置了一个存储块)，是两个灯的数据量就要进一次中断来切换 ping-pong buffer。
  - 缓解思路有：

    - 对于 esp-idf release/v4.4 及之前版本，可以增大 `mem_block_num <https://docs.espressif.com/projects/esp-idf/en/v4.4.1/esp32/api-reference/peripherals/rmt.html#_CPPv4N12rmt_config_t13mem_block_numE>`_，在 release/v5.0 中有进行修改，参考 `Breaking Changes in Usage <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/migration-guides/release-5.x/peripherals.html?highlight=mem_block_num#id6>`_。
    - 将 RMT 的中断安装在特定的 CPU 核上，可以在一个 pin to core 的 task 中调用 driver install 函数，避开 Wi-Fi 或蓝牙使用的核。
  
  - 如果您还处于前期技术选型阶段，推荐使用 ESP32-S3 的 RMT。