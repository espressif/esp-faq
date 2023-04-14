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

.. _lcd-examples:

ESP32 系列芯片 LCD 驱动及参考例程在哪？
------------------------------------------------------------------

  - ESP 的 LCD 驱动位于 **ESP-IDF** 下的 `components/esp_lcd <https://github.com/espressif/esp-idf/tree/master/components/esp_lcd>`__，目前仅存在于 **release/v4.4 及以上** 版本中。**esp_lcd** 能够驱动 ESP 系列芯片所支持的 **I2C**、**SPI**、**8080** 以及 **RGB** 四种接口的 LCD 屏幕，各系列芯片所支持的 LCD 接口见 `ESP32 系列芯片的屏幕接口 <https://docs.espressif.com/projects/espressif-esp-iot-solution/zh_CN/latest/display/screen.html#esp32>`__。
  - 各接口的 LCD 驱动应用示例参考 ESP-IDF 下的 `examples/peripherals/lcd <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/lcd>`__，这些示例目前仅存在于 **release/v5.0** 及以上版本中，因为 **release/v4.4** 中 esp_lcd 的 API 名称与高版本基本一致，所以同样可以参考上述示例（两者的 API 实现上有一些区别）。
  - **不推荐** 使用 esp-iot-solution 中的 LCD 驱动及例程。
  - RGB LCD 应用推荐使用 ESP-IDF **release/v5.0**，因为 release/v4.4 中不支持部分特性。

---------------

ESP32 系列芯片 LCD 屏幕适配情况是怎样的？
-------------------------------------------------------------------

  目前基于 `esp_lcd` 驱动适配过的 LCD 驱动 IC 如下：

  - `esp_lcd <https://github.com/espressif/esp-idf/blob/7f4bcc36959b1c483897d643036f847eb08d270e/components/esp_lcd/include/esp_lcd_panel_vendor.h>`__：st7789、nt35510、ssd1306
  - `包管理器 <https://components.espressif.com/>`__：gc9a01、ili9341、ili9488、ra8875、sh1107（持续更新中）

  **需注意，即使驱动 IC 相同，不同的屏幕往往需要不同的寄存器配置参数，而且屏幕厂商通常会给配套的配置参数（代码），因此推荐利用上面两种途径获取相似驱动 IC 的代码，根据自己屏幕的实际参数进行修改。**

  目前基于 `esp_lcd_touch` 驱动适配过的 Touch 驱动 IC 如下：

  - `包管理器 <https://components.espressif.com/>`__：FT5x06、GT1151、GT911、STMPE610、TT21100、XPT2046（持续更新中）

--------------

如何提高 LCD 的显示帧率？
-----------------------------------------------------

  - LCD 的实际显示帧率由“接口帧率”和“渲染帧率”共同决定，一般来说，受限于 ESP 的计算性能，“接口帧率”往往远大于“渲染帧率”，因此该问题可以表述为“如何提高 LCD 的渲染帧率”。

  - 以下 ESP 配置项对帧率提升有帮助（IDF release/v5.0）:

    - CONFIG_FREERTOS_HZ=1000
    - CONFIG_ESP_DEFAULT_CPU_FREQ_MHZ_240=y
    - CONFIG_ESPTOOLPY_FLASHMODE_QIO=y
    - CONFIG_ESPTOOLPY_FLASHFREQ_120M=y [需要与 PSRAM 保持一致]
    - CONFIG_SPIRAM_MODE_OCT=y
    - CONFIG_SPIRAM_SPEED_120M=y [需要与 FLASH 保持一致]
    - CONFIG_SPIRAM_FETCH_INSTRUCTIONS=y
    - CONFIG_SPIRAM_RODATA=y
    - CONFIG_ESP32S3_DATA_CACHE_LINE_64B=y
    - CONFIG_COMPILER_OPTIMIZATION_PERF=y

  - 以下 LVGL 配置项对帧率提升有帮助（LVGL v8.3）:

    - #define LV_MEM_CUSTOM 1
    - #define LV_MEMCPY_MEMSET_STD 1
    - #define LV_ATTRIBUTE_FAST_MEM IRAM_ATTR

---------------

ESP32 是否有 I2S 驱动 LCD 的参考代码？
----------------------------------------------------

  - ESP32/ESP32-S2 使用 I2S 驱动的屏幕接口类型为 i80(8080)
  - 关于例程，请参考 :ref:`LCD 例程 <lcd-examples>`。

---------------

ESP32 LCD 最大可以支持多大的分辨率？相应的帧率是多少？
----------------------------------------------------------------------------------------------------------

  ESP32 LCD 在 RGB 接口下，分辨率最大能够支持 800 × 480，接口帧率上限为 59 (PCLK 30 MHz), 对应 LVGL 平均帧率为 23; LVGL 平均帧率上限为 26, 对应接口帧率为 41 (PCLK 21 MHz)。

---------------

使用 ESP32-S3 测试 `LVGL <https://github.com/espressif/esp-iot-solution/tree/master/examples/hmi/lvgl_example>`_ 例程，请问目前已经适配了哪些型号的显示触摸屏？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  不推荐使用 esp-iot-solution 中的驱动和例程。关于例程，请参考 :ref:`LCD 例程 <lcd-examples>`。

---------------

ESP32-S3 使用 RGB 屏幕必须要外接 PSRAM 吗？
---------------------------------------------------------------

  是的，而且至少是 8 线 PSRAM 并且需要配置时钟为 80 MHz 及以上，否则将导致 RGB LCD 的 PCLK 无法设置到较高的 PCLK 频率同时帧率过低。

---------------------

ESP32-S3 系列的芯片支持哪些图片解码格式？
-----------------------------------------------------------------------------------------------------------------------------------------------------------

  - 目前官方仅支持 JPEG 解码格式，应用例程可参考 `esp-idf/examples/peripherals/lcd/tjpgd <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/lcd/tjpgd>`_。
  - 基于 LVGL 开发的话，可以支持 PNG、BMP、SJPG、GIF 图片解码格式，具体介绍见 `LVGL libs <https://docs.lvgl.io/master/libs/index.html>`_。

------------------------

为什么驱动 RGB LCD 屏幕时出现偏移（显示画面整体漂移）？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - **原因**

    - PCLK 设置过高，PSRAM 带宽跟不上。
    - 受写 flash 操作影响，期间 PSRAM 被禁用。

  - **配置方面**

    - 提高 PSRAM 和 flash 带宽，设置 flash 为  QIO 120 M，PSRAM 为 Octal 120 M。
    - 开启 `CONFIG_COMPILER_OPTIMIZATION_PERF`。
    - 降低 data_cache_line_size 到 32 Byte。
    - 开启 `CONFIG_SPIRAM_FETCH_INSTRUCTIONS` 和 `CONFIG_SPIRAM_RODATA`。
    - 开启 `CONFIG_LCD_RGB_RESTART_IN_VSYNC`，可能会导致闪花屏和降帧率，一般不推荐，可以尝试。

  - **应用方面**

    - 如果需要使用 Wi-Fi 和连续写 flash 的操作，请采用 `XIP PSRAM + RGB Bounce buffer` 的方法，设置步骤如下：

      - 确认 ESP-IDF 版本为较新（> 2022.12.12）的 release/v5.0 及以上，因为旧版本不支持 `XIP PSRAM` 的功能。
      - 确认 PSRAM 配置里面是否能开启 `SPIRAM_FETCH_INSTRUCTIONS` 和 `SPIRAM_RODATA` 这两项（如果 rodata 段数据过大，会导致 PSRAM 空间不够）。
      - 确认内存（SRAM）是否有余量，大概需要占用 [10 * screen_width * 4] 字节。
      - 需要将 `Data cache line size` 设置为 64 Byte（可设置 `Data cache size` 为 32 KB 以节省内存）。
      - 如以上均符合条件，那么就可以参考 `文档 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/lcd.html#bounce-buffer-with-single-psram-frame-buffer>`_ 修改 RGB 驱动为 `Bounce buffer` 模式。
      - 如操作 Wi-Fi 仍存在屏幕漂移问题，可以尝试关闭 PSRAM 里 CONFIG_SPIRAM_TRY_ALLOCATE_WIFI_LWIP 一项（会占用较大 SRAM）。
      - 设置后带来的影响包括：CPU 使用率升高、可能会造成中断看门狗复位、会造成较大内存开销。
      
    - 短时操作 flash 导致漂移的情况，如 wifi 连接等操作前后，可以在操作前调用 `esp_lcd_rgb_panel_set_pclk()` 降低 PCLK（如 6 MHz）并延时大约 20 ms（RGB 刷完一帧的时间），然后在操作结束后提高 PCLK 至原始水平，期间可能会造成短暂的闪白屏现象。
    - 使能 `esp_lcd_rgb_panel_config_t` 中的 `flags.refresh_on_demand`，通过调用 `esp_lcd_rgb_panel_refresh()` 接口手动刷屏，在保证屏幕不闪白的情况下尽量降低刷屏频率。
    - 如果无法避免，可以调用 `esp_lcd_rgb_panel_restart()`  接口重置 RGB 时序，防止永久性漂移。

---------------------------

为什么驱动 SPI/8080 LCD 屏幕显示 LVGL 时出现纵向错位？
-------------------------------------------------------------------------------

  如果采用 DMA 中断传输的方式，LVGL 的 ``lv_disp_flush_ready`` 需要在 DMA 传输结束后调用，而不是 ``draw_bitmap`` 后立即调用。

---------------------------

使用 ESP32-C3 通过 SPI 接口驱动 LCD 液晶显示屏，是否可使用 RTC_CLK 作为 SPI 时钟，让 LCD 液晶显示屏能在 Deep-sleep 模式下正常显示静态图片？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Deep-sleep 模式：CPU 和大部分外设都会掉电，只有 RTC 存储器处于工作状态。具体请参考 `《ESP32-C3 技术规格书》 <https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_cn.pdf>`__ 中关于“低功耗管理”的说明.
  - ESP32-C3 的 SPI 只支持 APB_CLK 和 XTAL_CLK 两种时钟源，不支持使用 RTC_CLK。因此在 Deep-sleep 模式下，LCD 液晶屏无法显示静态图片。具体请参考 *《ESP32-C3 技术参考手册》* > *复位和时钟* [`PDF <https://www.espressif.com/sites/default/files/documentation/esp32-c3_technical_reference_manual_cn.pdf#resclk>`__]。
  - 对于 SPI 接口驱动的 LCD 屏幕，一般来说驱动 IC 内置 GRAM，不需要 ESP 持续输出 SPI 时钟的就能正常显示静态图片，只是期间画面无法更新。

-----------------------

使用 ILI9488 LCD 屏幕测试 `屏幕 <https://github.com/espressif/esp-iot-solution/tree/master/examples/screen>`__ 例程，是否支持 9-bit 总线和 18-bit 色深？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ILI9488 驱动芯片可以支持 9-bit 总线和 18-bit 色深，但目前我们的驱动只支持 8-bit 总线和 16-bit 色深。可根据 ILI9488 数据手册自行修改驱动，来实现 9-bit 总线和 18-bit 色深的支持。
