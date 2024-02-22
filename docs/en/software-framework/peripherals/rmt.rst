Remote Control Transceiver (RMT)
================================

:link_to_translation:`zh_CN:[中文]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

--------------

What can the RMT peripheral on ESP chips be used for in practical?
--------------------------------------------------------------------------------------------------------------------------------------------

  - For applications of RMT, please refer to `RMT application examples <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/rmt.html>`_. It can be used for infrared remote control, LED strip lighting, D-shot motor control, and so on.

--------------

Which ESP chip is recommended for utilizing the RMT functionality?
--------------------------------------------------------------------------------------------------------------------------------------------

  - ESP32-S3 is recommended because it is currently the only chip with RMT DMA support. This ensures RMT is not interfered by interrupts caused by Wi-Fi, Bluetooth, and other peripherals.

--------------

How to change the clock to REF_TICK in RMT?
----------------------------------------------------------------------------------------------
  :CHIP\: ESP32 | ESP32-S2 | ESP32-C3:

  By using the `rmt_set_source_clk <https://docs.espressif.com/projects/esp-idf/zh_CN/v4.4.2/esp32/api-reference/peripherals/rmt.html#_CPPv418rmt_set_source_clk13rmt_channel_t16rmt_source_clk_t>`_ interface.

--------------

When ESP32 RMT controls the WS2812 light strip with Wi-Fi or Bluetooth enabled, there are some data frame exceptions. How to solve the issue?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - This problem is difficult to solve on non-ESP32-S3 chips, because the RMT lighting up LED (especially when many LEDs) rely heavily on interrupts, and does not support DMA, thus requiring software to switch ping-pong buffer in the interrupt. If the interrupt does not respond in time, there will be a problem. By default (one memory block is set), after lighting up two LEDs, the RMT driver will go into the interrupt to switch the internal ping-pong buffer.
  - Workaround:
  
    - For esp-idf release/v4.4 and earlier versions, increase `mem_block_num <https://docs.espressif.com/projects/esp-idf/en/v4.4.1/esp32/api-reference/peripherals/rmt.html#_CPPv4N12rmt_config_t13mem_block_numE>`_. There is a change in release/v5.0. Please see `Breaking Changes in Usage <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/migration-guides/release-5.x/5.0/peripherals.html#id6>`_。
    - Install the RMT interrupts on a specific CPU core by calling the driver install function in a pin-to-core task, thus avoiding the core used by Wi-Fi or Bluetooth.
    - You can also use SPI DMA as an alternative to RMT to solve this issue. For more details, please refer to the `SPI DMA LED strip example <https://github.com/espressif/esp-iot-solution/blob/master/components/led/lightbulb_driver/drivers/ws2812/ws2812.c#L99>`_.

  - If you are in the product selection stage, it is recommended to use ESP32-S3 RMT.
  
--------------

How can I quickly adapt other infrared protocols based on the `IR NEC example <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/rmt/ir_nec_transceiver>`_ in ESP-IDF？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - You can accelerate the adaptation of other infrared protocols based on the `IR NEC <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/rmt/ir_nec_transceiver>`_ example by using the `RMT Encoder <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/rmt.html#rmt-encoder>`_.
  - If you need the infrared learning function, you can use the `ir_learn <https://github.com/espressif/esp-iot-solution/tree/master/components/ir/ir_learn>`_ component.

--------------

ESP32-S3 RMT supports configuring 4 RMT RX/TX channels. Why does it fail when creating more than 2 RMT TX channels in a row using `rmt_new_tx_channel <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/rmt.html#_CPPv418rmt_new_tx_channelPK23rmt_tx_channel_config_tP20rmt_channel_handle_t>`_?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - This is because the `mem_block_symbols` parameter configured in the `tx_chan_config` structure is too large. On ESP32-S3, the size of each dedicated memory block for RMT is 48 bytes. If the `mem_block_symbols` parameter exceeds 48, creating a TX channel will actually occupy the memory block of the next adjacent channel as well. Therefore, if you want to create and use 4 RMT RX/TX channels simultaneously, the `mem_block_symbols` parameter should not exceed 48.
  - Please note that the size of each dedicated memory block for RMT on ESP32 is 64 bytes.

--------------

Can ESP32-S3 RMT achieve synchronized output for multiple TX channels?
--------------------------------------------------------------------------------------------------------------------------------------------

  - Yes, please refer to the following code snippet:

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

How can I achieve cyclic data transmission using the RMT TX channel on ESP32-S3, such as an infinite loop?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - You can realize infinite loop transmission by setting the `rmt_transmit_config_t::loop_count` to -1. For more details, please refer to `Initiate TX Transaction <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/rmt.html#initiate-tx-transaction>`_。

---------------

Does the ESP32-S3 support One-Wire?
---------------------------------------------------------------------------------------------------------------------------

  - ESP32-S3 can support the `One-Wire bus protocol <https://www.maximintegrated.com/en/design/technical-documents/tutorials/1/1796.html>`_ through the RMT peripheral. For specific applications, refer to the `"esp-idf/examples/peripherals/rmt/onewire" <https://github.com/espressif/esp-idf/tree/release/v5.0/examples/peripherals/rmt/onewire>`_ example.
