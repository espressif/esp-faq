LCD
============

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

ESP32 是否有 I2S 驱动 LCD 的参考代码？
----------------------------------------------------

  - ESP32/ESP32-S2 使用 I2S 驱动的屏幕接口类型为 i80(8080)
  - IDF master 和 release/4.4 均已实现 i80 接口屏幕的驱动
  - 推荐例程：
     - master 下： `esp-idf/examples/peripherals/lcd/i80_controller <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/lcd/i80_controller>`_
     - release/4.4 下： `esp-idf/examples/peripherals/lcd/lvgl <https://github.com/espressif/esp-idf/tree/release/v4.4/examples/peripherals/lcd/lvgl>`_

---------------

ESP32 LCD 最大可以支持多大的分辨率？相应的帧率是多少？
----------------------------------------------------------------------------------------------------------

  ESP32 LCD 在 8080 16 位并口的接口下，分辨率最大能够支持 800 × 480，相应的帧率约为 30 帧。请参考 `显示屏 <https://docs.espressif.com/projects/espressif-esp-iot-solution/zh_CN/latest/display/screen.html>`_。

---------------

使用 ESP32-S3 测试 `LVGL <https://github.com/espressif/esp-iot-solution/tree/master/examples/hmi/lvgl_example>`_ 例程，请问目前已经适配了哪些型号的显示触摸屏？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 目前已适配的显示驱动 IC 的型号参见 `显示屏驱动 <https://docs.espressif.com/projects/espressif-esp-iot-solution/zh_CN/latest/display/screen.html#id3>`_ 说明。
  - 目前已适配的触摸驱动 IC 的型号参见 `触摸屏驱动 <https://docs.espressif.com/projects/espressif-esp-iot-solution/zh_CN/latest/input_device/touch_panel.html#id1>`_ 说明。

---------------

ESP32-S3 使用 RGB 屏幕必须要外接 PSRAM 吗？
---------------------------------------------------------------

  是的，而且至少是 8 线 PSRAM 并且需要配置时钟为 80 MHz 及以上，否则将导致 RGB LCD 的 PCLK 无法设置到较高的频率同时帧率过低。

---------------------

ESP32-S3 系列的芯片支持哪些图片解码格式？
-----------------------------------------------------------------------------------------------------------------------------------------------------------

  - 目前官方仅支持 JPEG 解码格式，应用例程可参考 `esp-idf/examples/peripherals/lcd/tjpgd <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/lcd/tjpgd>`_。
  - 基于 LVGL 开发的话，可以支持 PNG、BMP、SJPG、GIF 图片解码格式，具体介绍见 `LVGL libs <https://docs.lvgl.io/master/libs/index.html>`_。

------------------------

为什么驱动 RGB LCD 屏幕时出现横向偏移（显示画面整体漂移）？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 一般为 PCLK 设置过高，PSRAM 带宽跟不上，可以将 PCLK 调低，或者提高 PSRAM 带宽（配置为 120M Octal）。
  - 如果开启了 `CONFIG_ESP32S3_DATA_CACHE_64KB=y` 和 `CONFIG_ESP32S3_DATA_CACHE_LINE_64B=y` 这两个选项，可以将其设置为默认值，这样能够提高 PCLK 的设置上限。

---------------------------

为什么驱动 SPI/8080 LCD 屏幕显示 LVGL 时出现纵向错位？
-------------------------------------------------------------------------------

  如果采用 DMA 中断传输的方式，LVGL 的 ``lv_disp_flush_ready`` 需要在 DMA 传输结束后调用，而不是 ``draw_bitmap`` 后立即调用。
