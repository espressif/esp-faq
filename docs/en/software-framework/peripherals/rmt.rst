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

How to change the clock to REF_TICK in RMT?
---------------------------------------------------------------------------------------------
  :CHIP\: ESP32 | ESP32-S2 | ESP32-C3:

  By using the `rmt_set_source_clk <https://docs.espressif.com/projects/esp-idf/zh_CN/v4.4.2/esp32/api-reference/peripherals/rmt.html#_CPPv418rmt_set_source_clk13rmt_channel_t16rmt_source_clk_t>`_ interface.

--------------

When ESP32 RMT controls the WS2812 light strip with Wi-Fi or Bluetooth enabled, there are some data frame exceptions. How to solve the issue?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - This problem is difficult to solve on non-ESP32-S3 chips, because the RMT lighting up LED (especially when many LEDs) rely heavily on interrupts, and does not support DMA, thus requiring software to switch ping-pong buffer in the interrupt. If the interrupt does not respond in time, there will be a problem. By default (one memory block is set), after lighting up two LEDs, the RMT driver will go into the interrupt to switch the internal ping-pong buffer.
  - Workaround:
  
    - For esp-idf release/v4.4 and earlier versions, increase `mem_block_num <https://docs.espressif.com/projects/esp-idf/en/v4.4.1/esp32/api-reference/peripherals/rmt.html#_CPPv4N12rmt_config_t13mem_block_numE>`_. There is a change in release/v5.0. Please see `Breaking Changes in Usage <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/migration-guides/release-5.x/5.0/peripherals.html#id6>`_。
    - Install the RMT interrupts on a specific CPU core by calling the driver install function in a pin-to-core task, thus avoiding the core used by Wi-Fi or Bluetooth.

  - If you are in the product selection stage, it is recommended to use ESP32-S3 RMT.
  
