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

ESP 系列芯片 LCD 驱动及参考例程在哪？
------------------------------------------------------------------

  - ESP 的 LCD 驱动位于 **ESP-IDF** 下的 `components/esp_lcd <https://github.com/espressif/esp-idf/tree/master/components/esp_lcd>`__。**esp_lcd** 能够驱动 ESP 系列芯片所支持的 **I2C**、**SPI(QSPI)**、**8080** 以及 **RGB** 多种接口的屏幕，各系列芯片支持的接口类型如下：

    .. list-table::
        :header-rows: 1

        * - SoCs 
          - I2C
          - SPI (QSPI)
          - I80
          - RGB

        * - ESP32
          - 是
          - 是
          - 是
          - 否      
  
        * - ESP32-S2
          - 是
          - 是
          - 是
          - 否

        * - ESP32-S3
          - 是
          - 是
          - 是
          - 是

        * - ESP32-C3
          - 是
          - 是
          - 否
          - 否

        * - ESP32-C6
          - 是
          - 是
          - 否
          - 否

  - ESP 的 LCD 例程位于 **ESP-IDF** 下的 `examples/peripherals/lcd <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/lcd>`__ 和 **esp-iot-solution** 下的 `examples/display/lcd <https://github.com/espressif/esp-iot-solution/tree/master/examples/display/lcd>`__。
  - 推荐基于 ESP-IDF **release/v5.1** 及以上版本分支进行开发，因为低版本不支持部分重要的新特性，尤其是对于 RGB 接口。
  - **请勿使用** esp-iot-solution 中的 screen `驱动 <https://github.com/espressif/esp-iot-solution/tree/master/components/display/screen>`__ 及 `例程 <https://github.com/espressif/esp-iot-solution/tree/master/examples/screen>`__。

---------------

ESP 系列芯片 LCD 屏幕适配情况是怎样的？
-------------------------------------------------------------------

  目前基于 `esp_lcd` 驱动适配过的 LCD 驱动 IC 如下：

  - `ESP-IDF <https://github.com/espressif/esp-idf/blob/master/components/esp_lcd/include/esp_lcd_panel_vendor.h>`__：st7789、nt35510、ssd1306。
  - `ESP 包管理器 <https://components.espressif.com/components?q=esp_lcd>`__：gc9a01、ili9341、ili9488、ra8875、sh1107、st7796、st7701、gc9503、gc9b71、spd2010、...（持续更新中）

  **需注意，即使驱动 IC 相同，不同的屏幕往往需要不同的寄存器配置参数，而且屏幕厂商通常会给配套的配置参数（代码），因此推荐利用上面两种途径获取相似驱动 IC 的代码，根据自己屏幕的实际参数进行修改。**

  目前基于 `esp_lcd_touch` 驱动适配过的 Touch 驱动 IC 如下：

  - `ESP 包管理器 <https://components.espressif.com/components?q=esp_lcd_touch>`__：FT5x06、GT1151、GT911、STMPE610、TT21100、XPT2046、CST816、...（持续更新中）

--------------

ESP 系列芯片的带屏开发板是否支持使用 Arduino IDE 开发 GUI？
-----------------------------------------------------------------------------------------------------------------

  - 目前官方已推出用于 Arduino 开发的 LCD 驱动库 `ESP32_Display_Panel <https://github.com/esp-arduino-libs/ESP32_Display_Panel>`__，可以直接在 Arduino IDE 上下载，支持的开发板请参考 `文档 <https://github.com/esp-arduino-libs/ESP32_Display_Panel#espressif-development-boards>`__。
  - 需要注意以下几点：

    - ESP32_Display_Panel 依赖于 `arduino-esp32 <https://github.com/espressif/arduino-esp32>`__。
    - 由于 ESP32-S3 的 RGB 接口存在 :ref:`屏幕漂移 <lcd-rgb-screen-drift>` 问题，需要使用 ESP-IDF release/v5.1 及以上版本的特性来解决，而 arduino-esp32 (v2.x.x) 中使用的 ESP-IDF 版本为 v4.4.x，因此该版本无法解决此问题，在未来推出的 arduino-esp32 (v3.x.x) 中则会使用 ESP-IDF v5.1。
    - 由于使用 Arduino 无法像 ESP-IDF 一样通过 menuconfig 来调整各种参数配置，如编译优化等级等，所以为了实现最佳的性能，推荐基于 ESP-IDF 开发 GUI。

--------------

如何提高 LCD 的显示帧率？
-----------------------------------------------------

  - LCD 的实际显示帧率由“接口帧率”和“渲染帧率”共同决定，一般来说，受限于 ESP 的计算性能，“接口帧率”往往远大于“渲染帧率”，因此该问题可以表述为“如何提高 LCD 的渲染帧率”。

  - 以 ESP32-S3R8 为例，以下 ESP 配置项对帧率提升有帮助 (IDF release/v5.1):

    - ``CONFIG_FREERTOS_HZ=1000``
    - ``CONFIG_ESP_DEFAULT_CPU_FREQ_MHZ_240=y``
    - ``CONFIG_ESPTOOLPY_FLASHMODE_QIO=y``
    - ``CONFIG_ESPTOOLPY_FLASHFREQ_120M=y`` [需要与 PSRAM 保持一致]
    - ``CONFIG_SPIRAM_MODE_OCT=y``
    - ``CONFIG_IDF_EXPERIMENTAL_FEATURES=y`` and ``CONFIG_SPIRAM_SPEED_120M=y`` [需要与 FLASH 保持一致]
    - ``CONFIG_SPIRAM_FETCH_INSTRUCTIONS=y``
    - ``CONFIG_SPIRAM_RODATA=y``
    - ``CONFIG_ESP32S3_DATA_CACHE_LINE_64B=y``
    - ``CONFIG_COMPILER_OPTIMIZATION_PERF=y``

  - 以下 LVGL 配置项对帧率提升有帮助 (LVGL v8.3):

    - ``#define LV_MEM_CUSTOM 1`` or ``CONFIG_LV_MEM_CUSTOM=y``
    - ``#define LV_MEMCPY_MEMSET_STD 1`` or ``CONFIG_LV_MEMCPY_MEMSET_STD=y``
    - ``#define LV_ATTRIBUTE_FAST_MEM IRAM_ATTR`` or ``CONFIG_LV_ATTRIBUTE_FAST_MEM=y``

  - 详细 LCD 及 LVGL 性能说明，请参考 `文档 <https://github.com/espressif/esp-bsp/blob/master/components/esp_lvgl_port/docs/performance.md#lcd--lvgl-performance>`__。

---------------

ESP32 是否有 I2S 驱动 LCD 的参考代码？
----------------------------------------------------

  - ESP32/ESP32-S2 使用 I2S 驱动的屏幕接口类型为 i80(8080)
  - 关于例程，请参考 :ref:`LCD 例程 <lcd-examples>`。

---------------

ESP 系列芯片最大可以支持多少分辨率的 LCD？相应的帧率是多少？
----------------------------------------------------------------------------------------------------------

  - 对于 ESP32-S3 的 RGB 外设接口，由于受其硬件限制，理论上最大支持 4096 x 1024 分辨率（水平最大为 4096，垂直最大为 1024）；对于 ESP 系列芯片的其他外设接口，可以支持多大的分辨率并没有一个“最大”的硬件限制，
  - 由于芯片的存储大小、计算性能和外设接口的传输带宽有限，而且不同接口类型的 LCD 通常具有特定范围内的分辨率，因此针对 ESP32-C3 和 ESP32-S3 这两款芯片推荐使用 LCD 的分辨率如下：

    .. list-table::
        :header-rows: 1

        * - SoCs
          - SPI
          - QSPI
          - I80
          - RGB

        * - ESP32-C3
          - 240 x 240
          - 不推荐
          - 不支持
          - 不支持

        * - ESP32-S3
          - 320 x 240
          - 400 x 400
          - 480 x 320
          - 480 x 480，800 x 480

  - 针对 ESP32-S3 的 RGB 接口，目前测试过的最大分辨率为 800 × 480，接口帧率上限为 59 (PCLK 30 MHz), 对应 LVGL 平均帧率为 23; LVGL 平均帧率上限为 26, 对应接口帧率为 41 (PCLK 21 MHz)。

---------------

ESP32-S3R8 如何开启 PSRAM 120M Octal (DDR)？
----------------------------------------------------------------------------------------------------------

  - ESP-IDF 需要使用 **release/v5.1** 及以上分支版本。
  - 通过 menuconfig 开启配置项：IDF_EXPERIMENTAL_FEATURES, SPIRAM_SPEED_120M, SPIRAM_MODE_OCT。
  - **需注意**，该特性是一种仍在测试完善中的实验功能，并具有以下温度风险：

    - 在温度高于 65°C 的情况下，即使开启 ECC 功能也无法保证正常工作。
    - 温度变化也可能导致访问 PSRAM/flash 时程序崩溃，具体参考 `文档 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32s3/api-guides/flash_psram_config.html#all-supported-modes-and-speeds>`__。

---------------

使用 ESP32-S3 测试 `LVGL <https://github.com/espressif/esp-iot-solution/tree/master/examples/hmi/lvgl_example>`__ 例程，请问目前已经适配了哪些型号的显示触摸屏？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  不推荐使用 esp-iot-solution 中的驱动和例程。关于例程，请参考 :ref:`LCD 例程 <lcd-examples>`。

---------------

ESP32-S3 使用 RGB 屏幕必须要外接 PSRAM 吗？
---------------------------------------------------------------

  - 通常来说是的，RGB 屏幕要求主控提供至少一个整屏大小的帧缓存，而 RGB 屏幕的分辨率一般较大，ESP32-S3 的 SRAM 很可能无法满足需求。
  - 不推荐使用 4 线 PSRAM，因为 4 线 PSRAM 的带宽较低，会导致 RGB LCD 的 PCLK 无法设置到需要的频率大小。
  - 推荐使用 8 线 PSRAM 并且需要配置时钟为 80 MHz 及以上。

---------------------

ESP32-S3 如何在保证 RGB 屏幕显示正常的情况下提高 PCLK 的设置上限？
----------------------------------------------------------------------------------------------------

  - 通常来说，PCLK 的设置上限受限于 PSRAM 的带宽，因此需要提高 PSRAM 的带宽：

    - 使用更高频率的 PSRAM 时钟，或者使用更宽的 PSRAM 总线（8 线）。
    - 减少其他外设对 PSRAM 带宽的占用，如 Wi-Fi、flash 等。
    - 降低 Data Cache Line Size 到 32 Byte（使用 RGB Bounce Buffer 模式时需要设置到 64 Byte）。

  - 开启 RGB 驱动的 Bounce Buffer 模式，并且 buffer 越大效果越好，使用方法请参考 `文档 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/lcd.html#bounce-buffer-with-single-psram-frame-buffer>`__。需注意，由于该模式下是先通过 CPU 搬运 PSRAM 数据到 SRAM，再通过 GDMA 传输数据到 RGB 外设，因此需要同时开启 `CONFIG_ESP32S3_DATA_CACHE_LINE_64B=y`，否则可能会导致屏幕出现漂移。
  - 经过少量测试，4 线 PSRAM 80 MHz 时的 PCLK 最高设置至 11 MHz，8 线 PSRAM 80 MHz 时的 PCLK 最高设置至 22 MHz，8 线 PSRAM 120 MHz 时的 PCLK 最高设置至 30 MHz。

---------------------

ESP32-S3 系列的芯片支持哪些图片解码格式？
-----------------------------------------------------------------------------------------------------------------------------------------------------------

  - 目前官方仅支持 JPEG 解码格式，应用例程可参考 `esp-idf/examples/peripherals/lcd/tjpgd <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/lcd/tjpgd>`_。
  - 基于 LVGL 开发的话，可以支持 PNG、BMP、SJPG、GIF 图片解码格式，具体介绍见 `LVGL libs <https://docs.lvgl.io/master/libs/index.html>`_。

------------------------

.. _lcd-rgb-screen-drift:

为什么 ESP32-S3 驱动 RGB LCD 屏幕时出现偏移（显示画面整体漂移）？
-----------------------------------------------------------------------------------------------------------

  - **原因**

    - RGB 外设的 PCLK 设置过高，PSRAM 的带宽无法满足。
    - 受写 flash 操作（如 Wi-Fi、OTA、BLE）影响，期间 PSRAM 被禁用。

  - **配置方面**

    - 提高 PSRAM 和 flash 带宽，设置 flash 为  QIO 120 M，PSRAM 为 Octal 120 M。
    - 开启 ``CONFIG_COMPILER_OPTIMIZATION_PERF``。
    - 降低 Data Cache Line Size 到 32 Byte（使用 RGB ``Bounce Buffer`` 模式时需要设置到 64 Byte）。
    - 开启 ``CONFIG_SPIRAM_FETCH_INSTRUCTIONS`` 和 ``CONFIG_SPIRAM_RODATA``。
    - （不推荐）开启 ``CONFIG_LCD_RGB_RESTART_IN_VSYNC``，可以在屏幕漂移后自动恢复，但无法避免该问题并且降低帧率。

  - **应用方面**

    - 在保证屏幕正常工作的前提下，尽量减小 PCLK 的频率，降低 PSRAM 的带宽占用。
    - 如果需要使用 Wi-Fi、BLE 和连续写 flash 的操作，请采用 ``XIP on PSRAM + RGB Bounce buffer`` 的方法，设置步骤如下：

      - 确认 ESP-IDF 版本为较新（> 2022.12.12）的 release/v5.0 及以上，因为旧版本不支持 ``XIP on PSRAM`` 的功能（release/v4.4 可以通过打补丁的方式实现，但不推荐）。
      - 确认 PSRAM 配置里面是否能开启 ``CONFIG_SPIRAM_FETCH_INSTRUCTIONS`` 和 ``CONFIG_SPIRAM_RODATA`` 这两项（如果 rodata 段数据过大，会导致 PSRAM 空间不够）。
      - 确认内存（SRAM）是否有余量，大概需要占用 [10 * screen_width * 4] 字节。
      - 设置 ``Data cache line size`` 为 64 Byte（可设置 ``Data cache size`` 为 32 KB 以节省内存）。
      - 设置 ``CONFIG_FREERTOS_HZ`` 为 1000。
      - 如以上均符合条件，那么就可以参考 `文档 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/lcd.html#bounce-buffer-with-single-psram-frame-buffer>`__ 修改 RGB 驱动为 ``Bounce buffer`` 模式。
      - 如操作 Wi-Fi 仍存在屏幕漂移问题，可以尝试关闭 PSRAM 里 ``CONFIG_SPIRAM_TRY_ALLOCATE_WIFI_LWIP`` 一项（会占用较大 SRAM）。
      - 设置后带来的影响包括：CPU 使用率升高、可能会造成中断看门狗复位、会造成较大内存开销。
      - 由于 Boucne Buffer 是在 GDMA 中断里通过 CPU 搬运 PSRAM 的数据到 SRAM，程序需要避免长时间执行关中断的操作（如调用 ``portENTER_CRITICAL()``），否则仍会造成屏幕漂移。

    - 短时操作 flash 导致漂移的情况，如 wifi 连接等操作前后，可以在操作前调用 ``esp_lcd_rgb_panel_set_pclk()`` 降低 PCLK（如 6 MHz）并延时大约 20 ms（RGB 刷完一帧的时间），然后在操作结束后提高 PCLK 至原始水平，期间可能会造成短暂的闪白屏现象。
    - 使能 ``esp_lcd_rgb_panel_config_t`` 中的 ``flags.refresh_on_demand``，通过调用 ``esp_lcd_rgb_panel_refresh()`` 接口手动刷屏，在保证屏幕不闪白的情况下尽量降低刷屏频率。
    - 如果无法避免，可以开启 ``CONFIG_LCD_RGB_RESTART_IN_VSYNC`` 或调用 ``esp_lcd_rgb_panel_restart()`` 接口重置 RGB 时序，防止永久性漂移。

---------------------------

为什么驱动 SPI/8080 LCD 屏幕显示 LVGL 时出现纵向错位？
-------------------------------------------------------------------------------

  如果采用 DMA 中断传输的方式，LVGL 的 ``lv_disp_flush_ready()`` 需要在 DMA 传输结束后调用，而不是 ``draw_bitmap()`` 后立即调用。

---------------------------

使用 ESP32-C3 通过 SPI 接口驱动 LCD 液晶显示屏，是否可使用 RTC_CLK 作为 SPI 时钟，让 LCD 液晶显示屏能在 Deep-sleep 模式下正常显示静态图片？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Deep-sleep 模式：CPU 和大部分外设都会掉电，只有 RTC 存储器处于工作状态。具体请参考 `《ESP32-C3 技术规格书》 <https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_cn.pdf>`__ 中关于“低功耗管理”的说明.
  - ESP32-C3 的 SPI 只支持 APB_CLK 和 XTAL_CLK 两种时钟源，不支持使用 RTC_CLK。因此在 Deep-sleep 模式下，LCD 液晶屏无法显示静态图片。具体请参考 *《ESP32-C3 技术参考手册》* > *复位和时钟* [`PDF <https://www.espressif.com/sites/default/files/documentation/esp32-c3_technical_reference_manual_cn.pdf#resclk>`__]。
  - 对于 SPI 接口驱动的 LCD 屏幕，一般来说驱动 IC 内置 GRAM，不需要 ESP 持续输出 SPI 时钟的就能正常显示静态图片，只是期间画面无法更新。

-----------------------

使用 ILI9488 LCD 屏幕测试 `屏幕 <https://github.com/espressif/esp-iot-solution/tree/master/examples/screen>`__ 例程，是否支持 9-bit 总线和 18-bit 色深？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ILI9488 驱动芯片可以支持 9-bit 总线和 18-bit 色深，但目前我们的驱动目前只支持 8-bit 总线和 16-bit 色深。

---------------------------

使用 ESP32-S3 驱动 RGB 屏幕时，为什么运行到 ``esp_lcd_new_rgb_panel()`` 或 ``esp_lcd_panel_init()`` 就会卡死或复位（TG1WDT_SYS_RST）？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 请检查 ESP 芯片或模组中与 PSRAM 占用的引脚是否与 RGB 引脚有冲突，如有冲突请修改 RGB 引脚配置。
  - 如使用 ESP32-S3R8，请避免使用 GPIO35、GPIO36、GPIO37 引脚。
