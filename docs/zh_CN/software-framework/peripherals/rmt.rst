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

ESP 芯片上的 RMT 外设有哪些实际的应用场景？
--------------------------------------------------------------------------------------------------------------------------------------------

  - 请参考 `RMT 应用示例 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/rmt.html>`_，可以实现红外遥控，LED 灯带点亮，D-shot 电机控制等。

--------------

如果要使用 RMT 功能， 最推荐使用哪一款 ESP 芯片？
--------------------------------------------------------------------------------------------------------------------------------------------

  - 推荐 ESP32-S3，因为目前只有 ESP32-S3 这一款芯片的 RMT 带有 DMA。这样 RMT 可以避免 Wi-Fi 或蓝牙等中断的干扰。

--------------

RMT 中如何将时钟修改为 REF_TICK?
---------------------------------------------------------------------------------------------
  :CHIP\: ESP32 | ESP32-S2 | ESP32-C3:

  可以调用 `rmt_set_source_clk <https://docs.espressif.com/projects/esp-idf/en/v4.4.2/esp32/api-reference/peripherals/rmt.html#_CPPv418rmt_set_source_clk13rmt_channel_t16rmt_source_clk_t>`_ 接口设置。

--------------

使用 ESP32 RMT 控制 WS2812 灯带，当与 Wi-Fi 或者蓝牙同时使用时，会出现部分数据帧异常的问题，该如何解决?
----------------------------------------------------------------------------------------------------------

  - 这个问题在非 ESP32-S3 的芯片上很难解决，因为 RMT 刷 LED（尤其是很多个 LED 的时候）严重依赖中断，且不支持 DMA，需要软件在中断切换 ping-pong buffer，如果中断没有及时响应，就会出现问题。默认情况下 (即只设置了一个存储块)，是两个灯的数据量就要进一次中断来切换 ping-pong buffer。
  - 缓解思路有：

    - 对于 esp-idf release/v4.4 及之前版本，可以增大 `mem_block_num <https://docs.espressif.com/projects/esp-idf/en/v4.4.1/esp32/api-reference/peripherals/rmt.html#_CPPv4N12rmt_config_t13mem_block_numE>`_，在 release/v5.0 中有进行修改，参考 `Breaking Changes in Usage <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/migration-guides/release-5.x/5.0/peripherals.html#id13>`_。
    - 将 RMT 的中断安装在特定的 CPU 核上，可以在一个 pin to core 的 task 中调用 driver install 函数，避开 Wi-Fi 或蓝牙使用的核。
    - 您也可以使用 SPI DMA 来代替 RMT 解决此问题，具体请参考 `SPI DMA LED 灯带示例 <https://github.com/espressif/esp-iot-solution/blob/master/components/led/lightbulb_driver/drivers/ws2812/ws2812.c#L99>`_。

  - 如果您还处于前期技术选型阶段，推荐使用 ESP32-S3 的 RMT。

--------------

ESP-IDF 里只有一个 `IR NEC <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/rmt/ir_nec_transceiver>`_ 示例,如何快速实现其他红外协议的适配？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 可以在参考 `IR NEC <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/rmt/ir_nec_transceiver>`_ 示例的基础上利用 `RMT Encoder <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/rmt.html#rmt-encoder>`_ 来加速适配其他红外协议。
  - 如果需要红外学习功能，可以使用 `ir_learn <https://github.com/espressif/esp-iot-solution/tree/master/components/ir/ir_learn>`_ 组件。

--------------

ESP32-S3 RMT 支持配置 4 个 RMT RX/TX channel，但为什么在实际使用 `rmt_new_tx_channel <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/rmt.html#_CPPv418rmt_new_tx_channelPK23rmt_tx_channel_config_tP20rmt_channel_handle_t>`_ 连续创建超过 2 个 RMT TX channel 时就会失败?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 这是因为 `tx_chan_config` 结构体中配置的 `mem_block_symbols` 参数过大，ESP32-S3 上 RMT 每个专用内存块的大小为 48 字节。如果此时配置的 `mem_block_symbols` 参数超过 48，创建 TX 通道时实际上会把相邻的下一个通道对应的内存块也占用掉。因此如果您要同时创建并使用 4 个 RMT RX/TX channel，`mem_block_symbols` 参数的值不能超过 48。
  - 此外，ESP32 上 RMT 每个专用内存块的大小为 64 字节。

--------------

ESP32-S3 RMT 是否能实现多个 TX Channel 的同步输出？
--------------------------------------------------------------------------------------------------------------------------------------------

  - 可以，请参考以下参考代码：

  .. code-block:: c

    rmt_channel_handle_t tx_channels[TEST_RMT_CHANS];
    rmt_sync_manager_handle_t synchro = NULL;
    rmt_sync_manager_config_t synchro_config = {
      .tx_channel_array = tx_channels,
      .array_size = TEST_RMT_CHANS,
    };
    rmt_new_sync_manager(&synchro_config, &synchro);
    for (int i = 0; i < TEST_RMT_CHANS; i++) {
      rmt_transmit(tx_channels[i], led_strip_encoders[i], leds_grb, TEST_LED_NUM * 3, &transmit_config);
    }

--------------

ESP32-S3 如何实现用 RMT TX 通道循环发送数据，比如进行无限循环？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 将 `rmt_transmit_config_t::loop_count` 配置为 -1 即可无限循环传输，更多细节请参考 `Initiate TX Transaction <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/rmt.html#initiate-tx-transaction>`_。

-------------------

ESP32-S3 是否支持硬件 One-Wire？
------------------------------------------------------------------------------

  - ESP32-S3 可以通过 RMT 外设支持 `One-Wire 总线协议 <https://www.maximintegrated.com/en/design/technical-documents/tutorials/1/1796.html>`_。具体应用可参考 `"esp-idf/examples/peripherals/rmt/onewire" <https://github.com/espressif/esp-idf/tree/release/v5.0/examples/peripherals/rmt/onewire>`_ 例程。
