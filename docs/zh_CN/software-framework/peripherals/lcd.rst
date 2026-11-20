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

  - 请首先通过 `ESP-IoT-Solution 编程指南 - LCD 开发指南 <https://docs.espressif.com/projects/esp-iot-solution/zh_CN/latest/display/lcd/lcd_development_guide.html#id2>`__ 了解 LCD 的开发流程。
  - 基础 LCD 驱动例程请参考 `esp-idf/examples/peripherals/lcd <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/lcd>`__。
  - 进阶 LCD 驱动例程请参考 `esp-iot-solution/examples/display <https://github.com/espressif/esp-iot-solution/tree/master/examples/display>`__。

---------------

ESP 系列芯片 LCD 屏幕适配情况是怎样的？
-------------------------------------------------------------------

  - 各系列 ESP 芯片对 SPI、I80、RGB、MIPI-DSI 等接口的支持情况，请参考 `LCD 开发指南 - 支持的接口类型 <https://docs.espressif.com/projects/esp-iot-solution/zh_CN/latest/display/lcd/lcd_development_guide.html#id1>`__。其中部分芯片（如 ESP32-C5、ESP32-H2、ESP32-H4）不具备原生 I80 外设，可通过 esp_lcd 的 Parlio 接口模拟 I80 时序驱动 LCD。在 ESP-IDF v6.1.1 中，ESP32-C6 未定义该驱动所需的 ``SOC_PARLIO_LCD_SUPPORTED``。
  - 乐鑫官方已基于 esp_lcd 移植的 LCD 驱动 IC 组件列表（含 I2C、SPI、QSPI、I80、MIPI-DSI、3-wire SPI + RGB 等接口），请参考 `LCD 开发指南 - 驱动及示例 <https://docs.espressif.com/projects/esp-iot-solution/zh_CN/latest/display/lcd/lcd_development_guide.html#id2>`__。

--------------

ESP 系列芯片在应用开发中的常见问题
-------------------------------------------------------------------

  关于 LCD 屏幕的常见问题，请参考 `LCD 应用开发笔记 <https://docs.espressif.com/projects/esp-techpedia/zh_CN/latest/esp-friends/advanced-development/lcd-application-note/index.html>`__。

--------------

ESP32-P4 驱动 MIPI-DSI LCD 的一些说明
-------------------------------------------------------------------

  - 最高支持 2-lane，每路最高支持 1.5 Gbps 的速率（共 3 Gbps），并且支持 RGB565、RGB666、RGB888 颜色格式。
  - 部分 MIPI-DSI LCD 默认通过硬件配置为 4-lane，如 ILI9881C、JD9365，但大多数 IC 支持通过修改初始化寄存器切换为 2-lane，具体寄存器地址及操作因 IC 型号而异，需查阅 LCD 驱动 IC 技术规格书或咨询屏厂确认。ESP32-P4 仅支持 1-lane 和 2-lane 两种配置。
  - 配置 ``lane_bit_rate_mbps`` 时：最大不超过 1500 Mbps；建议最小不低于 480 Mbps。实际值可根据分辨率、刷新率、色深和通道数通过公式计算后预留 20% 余量确定，计算方法请参考 `MIPI DSI LCD 详解 <https://docs.espressif.com/projects/esp-iot-solution/zh_CN/latest/display/lcd/mipi_dsi_lcd.html>`__。
  - MIPI-DSI 驱动默认开启了通信应答机制 (frame ACK)，如果 ESP 与 LCD 之间出现通信异常，ESP 可能会卡死并触发看门狗。此时请检查硬件连接是否正确、初始化命令是否正确、复位时序是否正确，或使用逻辑分析仪排查通信问题。
  - 驱动 MIPI-DSI 屏幕需要为 MIPI DSI PHY 提供 2.5 V 的稳定电源（通过 LDO 获取），请参考对应示例代码的 LDO 配置部分。

--------------

ESP 系列芯片的带屏开发板是否支持使用 Arduino IDE 开发 GUI？
-----------------------------------------------------------------------------------------------------------------

  - 目前官方已推出用于 Arduino 开发的 LCD 驱动库 `ESP32_Display_Panel <https://github.com/esp-arduino-libs/ESP32_Display_Panel>`__，可以直接在 Arduino IDE 上下载，支持的开发板请参考 `文档 <https://github.com/esp-arduino-libs/ESP32_Display_Panel/blob/master/README_CN.md#%E6%94%AF%E6%8C%81%E7%9A%84%E5%BC%80%E5%8F%91%E6%9D%BF>`__。
  - 需要注意以下几点：

    - ESP32_Display_Panel 依赖于 `arduino-esp32 <https://github.com/espressif/arduino-esp32>`__。
    - 由于 ESP32-S3 的 RGB 接口存在 :ref:`屏幕漂移 <lcd-rgb-screen-drift>` 问题，需要使用 ESP-IDF release/v5.1 及以上版本的特性来解决，而 arduino-esp32 v2.x.x 版本中使用的 ESP-IDF 版本为 v4.4.x，因此该版本无法解决此问题，需要使用 arduino-esp32 v3.x.x 版本，详细说明请参考 `文档 <https://github.com/esp-arduino-libs/ESP32_Display_Panel/blob/master/docs/envs/use_with_arduino_cn.md#%E5%9C%A8-arduino-ide-%E4%B8%AD%E4%BD%BF%E7%94%A8-esp32-s3-%E9%A9%B1%E5%8A%A8-rgb-lcd-%E6%97%B6%E5%87%BA%E7%8E%B0%E7%94%BB%E9%9D%A2%E6%BC%82%E7%A7%BB%E9%97%AE%E9%A2%98%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88>`__。
    - 由于使用 Arduino 无法像 ESP-IDF 一样通过 menuconfig 来调整各种参数配置，如编译优化等级等，所以为了实现最佳的性能，推荐基于 ESP-IDF 开发 GUI。

--------------

如何提高 LCD 的显示帧率？
-----------------------------------------------------

  - 关于帧率的详细介绍请参考 `ESP-IoT-Solution 编程指南 - LCD 概述 <https://docs.espressif.com/projects/esp-iot-solution/zh_CN/latest/display/lcd/lcd_guide.html#id10>`__。一般来说，受限于 ESP 的计算性能，“接口帧率”往往远大于“渲染帧率”，因此该问题可以表述为“如何提高 LCD 的渲染帧率”。针对这个问题，可以从以下三个方面进行考虑：

    - 提高 ESP 的性能。在使用 ESP-IDF 开发时可以通过 menuconfig 来配置 ESP，而默认并没有配置到最佳性能，这里以 ESP32-S3 为例，我们可以提高 CPU 频率到最高 240 MHz，提高 FreeRTOS tick 的频率到 1000，增大 flash 或 PSRAM 的带宽。除此之外，还有增大 data cache line size，设置编译优化等级为 ``-O2`` 等等。
    - 提高 LVGL 的性能。LVGL 本身也是可以通过 menuconfig 或者 *lv_conf.h* 文件进行配置的，例如设置 LVGL 使用 ESP-IDF 中的 ``malloc`` 和 ``memcpy`` 等内存操作函数，开启 fast memory 编译选项等。
    - 优化应用设计。一方面可以通过调整任务的优先级或指定 CPU 核使得 LVGL 和其他任务充分利用 CPU 资源，尤其是对具有双核的 ESP；另一方面也可以优化 GUI 的设计，比如尽量避免使用复杂的动画以及具有透明度的图层混叠效果。

  - 以 ESP32-S3R8 为例，以下 ESP 配置项对帧率提升有帮助 (ESP-IDF release/v5.1)：

    - ``CONFIG_FREERTOS_HZ=1000``
    - ``CONFIG_ESP_DEFAULT_CPU_FREQ_MHZ_240=y``
    - ``CONFIG_ESPTOOLPY_FLASHMODE_QIO=y``
    - ``CONFIG_ESPTOOLPY_FLASHFREQ_120M=y`` （需要与 PSRAM 保持一致）
    - ``CONFIG_SPIRAM_MODE_OCT=y``
    - ``CONFIG_IDF_EXPERIMENTAL_FEATURES=y`` 和 ``CONFIG_SPIRAM_SPEED_120M=y`` （需要与 flash 保持一致）
    - ``CONFIG_SPIRAM_FETCH_INSTRUCTIONS=y``
    - ``CONFIG_SPIRAM_RODATA=y``
    - ``CONFIG_ESP32S3_DATA_CACHE_LINE_64B=y``
    - ``CONFIG_COMPILER_OPTIMIZATION_PERF=y``

  - 在 ESP32-P4 上，可以调整以下配置项以提高帧率（适用于 ESP-IDF release/v5.4 及以上，推荐使用 release/v6.0）：

    - ``CONFIG_CACHE_L2_CACHE_256KB=y``
    - ``CONFIG_CACHE_L2_CACHE_LINE_128B=y``
    - ``CONFIG_SPIRAM_XIP_FROM_PSRAM=y``
    - ``CONFIG_COMPILER_OPTIMIZATION_PERF=y``

  - 以下 LVGL 配置项对帧率提升有帮助：

    - **LVGL v8**： ``CONFIG_LV_MEM_CUSTOM=y``、 ``CONFIG_LV_MEMCPY_MEMSET_STD=y``、 ``CONFIG_LV_ATTRIBUTE_FAST_MEM_USE_IRAM=y``
    - **LVGL v9**： ``CONFIG_LV_OS_FREERTOS=y``、 ``CONFIG_LV_USE_CLIB_MALLOC=y``、 ``CONFIG_LV_USE_CLIB_STRING=y``、 ``CONFIG_LV_USE_CLIB_SPRINTF=y``、 ``CONFIG_LV_DEF_REFR_PERIOD=15``

  - 如果对帧率、旋转效率和防撕裂效果有更高的要求，建议使用 `esp_lvgl_adapter 组件 <https://docs.espressif.com/projects/esp-iot-solution/zh_CN/latest/display/tools/esp_lvgl_adapter.html>`__。

---------------

ESP32/ESP32-S2 是否有 I2S 驱动 I80 LCD 的参考代码？
----------------------------------------------------

  在 ESP32 和 ESP32-S2 上，esp_lcd 的 I80 驱动使用 I2S 外设的 LCD 模式。应用可通过 ESP-IDF v4.4 及后续版本提供的 ``esp_lcd_new_i80_bus()`` 创建总线。

  如需驱动 I80 LCD，请直接参考 :ref:`LCD 例程 <lcd-examples>` 中的 ``i80_controller`` 例程，以及 `ESP-IDF 编程指南 - I80 LCD <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/peripherals/lcd/i80_lcd.html>`__。

---------------

ESP 系列芯片推荐驱动的 LCD 分辨率上限是多少？相应的帧率是多少？
----------------------------------------------------------------------------------------------------------

  分辨率上限取决于接口类型和实际应用对帧率的要求，建议以能达到流畅帧率（通常 ≥ 30 FPS）的最大分辨率为实际上限，而不是追求硬件理论极限。各平台的典型分辨率与对应帧率（基于 esp_lvgl_adapter + LVGL v9 Benchmark）请查阅 `LCD 驱动芯片选型 <https://docs.espressif.com/projects/esp-techpedia/zh_CN/latest/esp-friends/advanced-development/lcd-application-note/overview.html#id5>`__。

  使用 ESP32-S3、ESP32-S31 或 ESP32-P4 的原生 RGB 接口时，每帧的垂直总行数 (``v_res + vsync_pulse_width + vsync_back_porch + vsync_front_porch``) 应配置为不超过 1024 行。

---------------

ESP32-S3R8 如何开启 PSRAM 120M Octal (DDR)？
----------------------------------------------------------------------------------------------------------

  - ESP-IDF 需要使用 **release/v5.1** 及以上分支版本。
  - 通过 menuconfig 开启配置项： ``IDF_EXPERIMENTAL_FEATURES``, ``SPIRAM_SPEED_120M``, ``SPIRAM_MODE_OCT``。
  - ESP32-S3-WROOM-1-N16R16V 模组目前不支持此功能，如果启用，可能会出现芯片在上电时卡死然后复位的问题。
  - **需注意**，该特性是一种仍在测试完善中的实验功能，并具有以下温度风险：

    - 在温度高于 65°C 的情况下，即使开启 ECC 功能也无法保证正常工作。
    - 温度变化也可能导致访问 PSRAM/flash 时程序崩溃，具体参考 `文档 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32s3/api-guides/flash_psram_config.html#flash-psram-combination>`__。

---------------

ESP32-S3 使用 RGB 屏幕必须要外接 PSRAM 吗？
---------------------------------------------------------------

  - 整屏帧缓冲通常超出内部 SRAM 容量。如果应用能在 ``on_bounce_empty`` 回调中及时填充像素，可启用 ``no_fb`` 并配置非零的 ``bounce_buffer_size_px``，无需分配整屏帧缓冲。
  - 不推荐使用 4 线 PSRAM，因为 4 线 PSRAM 的带宽较低，会导致 RGB LCD 的 PCLK 无法设置到需要的频率大小。
  - 推荐使用 8 线 PSRAM 并且需要配置时钟为 80 MHz 及以上。

---------------------

ESP32-S3 如何在保证 RGB 屏幕显示正常的情况下提高 PCLK 的设置上限？
----------------------------------------------------------------------------------------------------

  - 通常来说，PCLK 的设置上限受限于 PSRAM 的带宽，因此需要提高 PSRAM 的带宽：

    - 使用更高频率的 PSRAM 时钟，或者使用更宽的 PSRAM 总线（8 线）。
    - 减少其他外设对 PSRAM 带宽的占用，如 Wi-Fi、flash 等。
    - 降低 Data Cache Line Size 到 32 Byte（使用 RGB Bounce Buffer 模式时需要设置到 64 Byte）。

  - 开启 RGB 驱动的 Bounce Buffer 模式，并且 buffer 越大效果越好，使用方法请参考 `文档 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32s3/api-reference/peripherals/lcd/rgb_lcd.html>`__。需注意，由于该模式下是先通过 CPU 搬运 PSRAM 数据到 SRAM，再通过 GDMA 传输数据到 RGB 外设，因此需要同时开启 ``CONFIG_ESP32S3_DATA_CACHE_LINE_64B=y``，否则可能会导致屏幕出现漂移。
  - 经过少量测试，4 线 PSRAM 80 MHz 时的 PCLK 最高设置至 11 MHz，8 线 PSRAM 80 MHz 时的 PCLK 最高设置至 22 MHz，8 线 PSRAM 120 MHz 时的 PCLK 最高设置至 30 MHz。
  - 对于使用 LVGL 的应用，可以将执行 RGB 外设初始化的任务与执行 LVGL ``lv_timer_handler()`` 的任务分配在同一个核上，能够显著提升 PCLK 的设置上限。

---------------------

ESP 系列芯片的 LCD 应用支持哪些图片解码格式？
-----------------------------------------------------------------------------------------------------------------------------------------------------------

  - **软件 JPEG 解码**：ESP-IDF 例程使用 esp_jpeg 组件，可在支持的芯片上使用 ROM 解码器，参考 `esp-idf/examples/peripherals/lcd/tjpgd <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/lcd/tjpgd>`__。
  - **硬件 JPEG 解码**：ESP32-S31 和 ESP32-P4 集成了硬件 JPEG 编解码器 (``SOC_JPEG_CODEC_SUPPORTED``)，支持通过 `esp_driver_jpeg <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32p4/api-reference/peripherals/jpeg.html>`__ 组件进行硬件加速 JPEG 解码，速度显著快于软件解码。
  - **通过 esp_lvgl_adapter + esp_lv_decoder**：推荐使用 `esp_lvgl_adapter <https://docs.espressif.com/projects/esp-iot-solution/zh_CN/latest/display/tools/esp_lvgl_adapter.html>`__ 配合 `esp_lv_decoder <https://components.espressif.com/components/espressif/esp_lv_decoder>`__，支持以下格式：

    - 标准格式：JPG、PNG、QOI
    - 分片格式（针对嵌入式内存优化）：SJPG、SPNG、SQOI
    - 硬件加速（仅支持的芯片）：JPEG、PJPG

  - **基于 LVGL 内置库**：LVGL 本身也提供了 PNG、BMP、GIF 等格式的解码支持，具体见 `LVGL libs <https://lvgl.io/docs/open/libs>`__。
  - **EAF 动图格式**：乐鑫自定义动图格式，原生设计用于配合 `esp_emote_gfx <https://components.espressif.com/components/espressif2022/esp_emote_gfx>`__ 组件刷屏（分段解码），也已适配至 LVGL，参考 `EAF 动图格式示例 <https://github.com/espressif/esp-iot-solution/tree/master/examples/display/gui/lvgl_eaf_player>`__。

------------------------

.. _lcd-rgb-screen-drift:

为什么 ESP32-S3 驱动 RGB LCD 屏幕时出现偏移（显示画面整体漂移）？
-----------------------------------------------------------------------------------------------------------

  - **原因**

    - RGB 外设的 PCLK 设置过高，PSRAM 或 GDMA 的带宽无法满足。
    - PSRAM 和 flash 共用一组 SPI 接口，受写 flash 操作（如 Wi-Fi、OTA、低功耗蓝牙）影响，期间 PSRAM 被禁用。
    - 读取大量的 flash/PSRAM 数据，导致 PSRAM 带宽不足。

  - **配置方面**

    - 提高 PSRAM 和 flash 带宽，比如在硬件允许的条件下，采用更高的频率或更大的位宽。
    - 开启 ``CONFIG_COMPILER_OPTIMIZATION_PERF``。
    - 降低 Data Cache Line Size 到 32 Byte（使用 RGB Bounce Buffer 模式时需要设置到 64 Byte）。
    - 开启 ``CONFIG_SPIRAM_FETCH_INSTRUCTIONS`` 和 ``CONFIG_SPIRAM_RODATA``。
    - （不推荐）开启 ``CONFIG_LCD_RGB_RESTART_IN_VSYNC``，可以在屏幕漂移后自动恢复，但无法避免该问题并且降低帧率。

  - **应用方面**

    - 在保证屏幕正常工作的前提下，尽量减小 PCLK 的频率，降低 PSRAM 的带宽占用。
    - 如果需要使用 Wi-Fi、低功耗蓝牙和连续写 flash 的操作，请采用 XIP on PSRAM + RGB Bounce Buffer 的方法，其中，XIP on PSRAM 用于将代码段和只读段的数据加载到 PSRAM，开启后执行写 flash 操作不会禁用 PSRAM。RGB Bounce Buffer 用于将帧缓存的数据分块通过 CPU 从 PSRAM 搬运到 SRAM，然后再使用 GDMA 传输数据到 RGB 外设，相较于直接采用 PSRAM GDMA 的方式能够实现更高的传输带宽。设置步骤如下：

      - 确认 ESP-IDF 版本为较新 (> 2022.12.12) 的 release/v5.0 及以上，因为旧版本不支持 XIP on PSRAM 的功能（release/v4.4 可以通过打补丁的方式实现，但不推荐）。
      - 确认 PSRAM 配置里面是否能开启 ``CONFIG_SPIRAM_FETCH_INSTRUCTIONS`` 和 ``CONFIG_SPIRAM_RODATA`` 这两项。如果只读段数据过大（如大量图片），会导致 PSRAM 空间不够，此时可以采用文件系统或将图片制作成 bin 加载到指定分区。
      - 确认内存 (SRAM) 是否有余量，大概需要占用 [10 × screen_width × 4] 字节。
      - 设置 Data cache line size 为 64 Byte（可设置 Data cache size 为 32 KB 以节省内存）。
      - 设置 ``CONFIG_FREERTOS_HZ`` 为 1000。
      - 如以上均符合条件，那么就可以参考 `文档 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32s3/api-reference/peripherals/lcd/rgb_lcd.html>`__ 修改 RGB 驱动为 Bounce Buffer 模式。如果开启后仍存在漂移现象，可以尝试增大 buffer，但是会占用更多的 SRAM 内存。
      - 如操作 Wi-Fi 仍存在屏幕漂移问题，可以尝试关闭 PSRAM 里 ``CONFIG_SPIRAM_TRY_ALLOCATE_WIFI_LWIP`` 一项（会占用较大 SRAM）。
      - 设置后带来的影响包括：CPU 使用率升高、可能会造成中断看门狗复位、会造成较大内存开销。
      - 由于 Bounce Buffer 是在 GDMA 中断里通过 CPU 搬运 PSRAM 的数据到 SRAM，程序需要避免长时间执行关中断的操作（如调用 ``portENTER_CRITICAL()``），否则仍会造成屏幕漂移。

    - 短时操作 flash 导致漂移的情况，如 Wi-Fi 连接等操作前后，可以在操作前调用 ``esp_lcd_rgb_panel_set_pclk()`` 降低 PCLK（如 6 MHz），等待新时钟在下一次 VSYNC 生效后再操作 flash，然后在操作结束后提高 PCLK 至原始水平，期间可能会造成短暂的闪白屏现象。
    - 如果无法避免，可以开启 ``CONFIG_LCD_RGB_RESTART_IN_VSYNC`` 或调用 ``esp_lcd_rgb_panel_restart()`` 接口重置 RGB 时序，防止永久性漂移。
    - 关于如何在 Arduino 中避免 RGB 屏幕漂移问题，请参考 `链接 <https://github.com/esp-arduino-libs/ESP32_Display_Panel/blob/master/docs/envs/use_with_arduino_cn.md#%E5%9C%A8-arduino-ide-%E4%B8%AD%E4%BD%BF%E7%94%A8-esp32-s3-%E9%A9%B1%E5%8A%A8-rgb-lcd-%E6%97%B6%E5%87%BA%E7%8E%B0%E7%94%BB%E9%9D%A2%E6%BC%82%E7%A7%BB%E9%97%AE%E9%A2%98%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88>`__。

---------------------------

为什么驱动 SPI/8080 LCD 屏幕显示 LVGL 时出现纵向错位？
-------------------------------------------------------------------------------

  如果采用 DMA 中断传输的方式，flush 完成回调需要在 DMA 传输结束后调用，而不是在 ``draw_bitmap()`` 后立即调用。

  - LVGL v8：在 DMA 传输完成中断中调用 ``lv_disp_flush_ready()``。
  - LVGL v9：在 DMA 传输完成中断中调用 ``lv_display_flush_ready()``。

---------------------------

使用 ESP32-C3 通过 SPI 接口驱动 LCD 液晶显示屏，是否可使用 RTC_CLK 作为 SPI 时钟，让 LCD 液晶显示屏能在 Deep-sleep 模式下正常显示静态图片？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Deep-sleep 模式：CPU 和大部分外设都会掉电，只有 RTC 存储器处于工作状态。具体请参考 `《ESP32-C3 技术规格书》 <https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_cn.pdf>`__ 中关于“低功耗管理”的说明。
  - ESP32-C3 的 SPI 只支持 APB_CLK 和 XTAL_CLK 两种时钟源，不支持使用 RTC_CLK。进入 Deep-sleep 后，SPI 传输停止。具体请参考 *《ESP32-C3 技术参考手册》* > *复位和时钟* [`PDF <https://www.espressif.com/sites/default/files/documentation/esp32-c3_technical_reference_manual_cn.pdf#resclk>`__]。
  - 对于 SPI 接口驱动的 LCD 屏幕，一般来说驱动 IC 内置 GRAM，保持供电、开启显示和所需背光后，无需 ESP 持续输出 SPI 时钟即可正常显示静态图片，只是期间画面无法更新。

-----------------------

使用 ILI9488 LCD 屏幕测试 `屏幕 <https://github.com/espressif/esp-iot-solution/tree/release/v2.0/examples/screen>`__ 例程，是否支持 9-bit 总线和 18-bit 色深？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ILI9488 驱动芯片可以支持 9-bit 总线和 18-bit 色深，但目前我们的驱动只支持 8-bit 总线和 16-bit 色深。

---------------------------

使用 ESP32-S3 驱动 RGB 屏幕时，为什么运行到 ``esp_lcd_new_rgb_panel()`` 或 ``esp_lcd_panel_init()`` 就会卡死或复位 (TG1WDT_SYS_RST)？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 请检查 ESP 芯片或模组中与 PSRAM 占用的管脚是否与 RGB 管脚有冲突，如有冲突请修改 RGB 管脚配置。
  - 如使用 ESP32-S3R8，请避免使用 GPIO35、GPIO36、GPIO37 管脚。

---------------------------

使用 ESP32-S3 驱动 RGB 屏幕时发现屏幕颜色出现异常反色，即黑色变白色，白色变黑色，如何处理？
---------------------------------------------------------------------------------------------------------------------------

  请检查屏幕驱动 IC 的初始化寄存器是否设置了 invert_color 功能，举例 ST7789，可通过配置 Inversion 寄存器来修正：

  - INVOFF (20h): Display Inversion Off
  - INVON (21h): Display Inversion On

---------------------------

使用 ESP32-S3 驱动 RGB 屏幕时发现屏幕颜色不正，出现缺色，如何处理？
----------------------------------------------------------------------------------------------------------------------------

  很可能是 RGB 配置有误，可以排查以下几个方面：

  - 依次显示纯红、纯绿、纯蓝。如果红蓝互换而绿色正常，检查 RGB/BGR 色序。
  - ST7789 的 MADCTL (``0x36``) 通过 bit 3 (``0x08``) 选择色序。将该位置 1 选择 BGR，清零选择 RGB，保留其他位。
  - 使用 RGB565 时，还需检查 LVGL 像素缓冲区的字节序是否与传输格式一致。
  - 如 RGB TTL 屏幕显示缺色，需要分别设置 R、G、B 显示，检查有波形的通道和 RGB 数据线设计是否符合。

---------------------------

LVGL 的 label 中正确输入了空格，比如“室内温度 25.5℃”，但在屏幕上没有显示空格，请问是什么原因，怎么排查？
---------------------------------------------------------------------------------------------------------------------------

  这属于 LVGL label 显示缺失，可以打开如下调试项，缺失字符会用方块填充，防止 map 缺失：

  ``Component config`` → ``LVGL configuration`` → ``Font usage`` → ``Enable drawing placeholders when glyph dsc is not found``

---------------------------

LVGL v8 连续加载存放在 flash 上的不同图片时速度太慢，比如在屏幕首页循环展示三张图片时该如何规避速度慢的问题？
---------------------------------------------------------------------------------------------------------------------------

  - 如果图片在下次使用前已被移出缓存，LVGL 会在下一轮重新打开它。
  - 若只轮播三张图片且内存充足，可将 ``LV_IMG_CACHE_DEF_SIZE`` 设为 3，并为缓存的解码数据预留内存。

---------------------------

LVGL v8 加载 flash 里的 PNG、JPEG 图片失败。屏幕上显示一片空白，什么原因？
---------------------------------------------------------------------------------------------------------------------------

  - 确认已启用对应格式的解码器。读取 PNG 文件时，LVGL v8.3 的 PNG 解码器会载入压缩文件，并将图像解码到每像素 4 字节的缓冲区。LodePNG 错误码 83 表示内存分配失败。
  - 估算 PNG 内存峰值时，应计入压缩文件、解码后的像素、解码工作区和已缓存的图片。JPEG 的内存需求取决于所用的 JPEG 解码器。

---------------------------

如何将 GIF 动图转成 C 语言代码来使用？
---------------------------------------------------------------------------------------------------------------------------

  将 GIF 转成 Map 选项，Color format 为 CF_RAW。

---------------------------

屏幕显示 GIF 动图时是否能设置为透明？
---------------------------------------------------------------------------------------------------------------------------

  可以，但是 GIF 只有 1 bit Alpha 描述值，所以只能全透或者不透明，没有半透明。

---------------------------

LVGL 界面上的图片格式选择哪种比较好？有没有对比说明？
---------------------------------------------------------------------------------------------------------------------------

  可以参考以下表格：

    .. list-table::
      :header-rows: 1

      * - 图片格式
        - 透明支持
        - 大小
        - 解码速度
      * - PNG
        - 完美支持
        - 适中
        - 适中
      * - BMP
        - 有限支持
        - 较大
        - 最快，无需解码
      * - JPG
        - 不支持
        - 较小
        - 快速

  在将图片用 `LVGL imageconverter <https://lvgl.io/tools/imageconverter>`__ 转成 MAP 时，如采用 ``CF_TRUE_COLOR`` 等格式（非 RAW 格式）转换，后续 LVGL 加载均不需要二次解码，但会占用比较大的代码段。

---------------------------

在使用 LVGL 的一些第三方库如 FreeType、Lottie 时，程序正常加载，但是屏幕显示一片空白，为什么？
---------------------------------------------------------------------------------------------------------------------------

  先考虑任务堆栈设置是否有误：

  - **FreeType**：使用 esp_lvgl_adapter 时，首先确认堆栈配置：LVGL v8 需将 ``CONFIG_ESP_MAIN_TASK_STACK_SIZE`` 设置为 32768（字体初始化在调用线程执行）；LVGL v9 需将 ``CONFIG_LV_DRAW_THREAD_STACK_SIZE`` 设置为 32768（字体渲染在绘图线程执行）。此外，可通过以下两个 Kconfig 优化选项降低资源占用：

    - ``ESP_LVGL_ADAPTER_FREETYPE_SMALL_RENDER_POOL``：将 FreeType render pool 从 16 KB 降至 4 KB，可同时减少 LVGL v9 绘图线程的栈需求。
    - ``ESP_LVGL_ADAPTER_FREETYPE_MINIMAL_BUILD``：裁剪 FreeType 编译模块，仅保留 TTF/OTF 常用路径所需内容（去除 Type1/CID/BDF/PCF 等 legacy 驱动及压缩流辅助），可显著降低 flash 占用；若项目需要上述被裁剪的格式，请勿开启。

    参考示例：`lvgl_freetype_font <https://github.com/espressif/esp-iot-solution/tree/master/examples/display/gui/lvgl_freetype_font>`__。

  - **Lottie**：一般需要分配 30 KB 以上的任务堆栈，参考 `lottie 移植 <https://docs.lvgl.io/9.1/libs/rlottie.html>`__。

---------------------------

ESP32-S3 驱动 SPI 屏幕，内部 RAM 不够给整屏 buffer 分配空间，有什么好的办法？
---------------------------------------------------------------------------------------------------------------------------

  在 PSRAM 帧缓冲区中渲染。分块刷新时，先将像素复制到内部 SRAM 的小块 DMA 缓冲区，再通过 SPI DMA 发送到屏幕。

  ESP32-S3 也支持 SPI DMA 从 PSRAM 直传。在支持该功能的 ESP-IDF 版本（如 v5.5.5）中，可在 SPI Master 事务中设置 ``SPI_TRANS_DMA_USE_PSRAM``，或在 ``esp_lcd_panel_io_spi_config_t`` 中启用 ``flags.psram_dma_direct``。要省去拷贝，缓冲区地址和传输长度须满足驱动的对齐要求。传输速率应控制在与 MSPI 共享的 PSRAM 可用带宽内。详见 `使用 PSRAM 的传输事务 <https://docs.espressif.com/projects/esp-idf/zh_CN/stable/esp32s3/api-reference/peripherals/spi_master.html#psram>`__。

  使用 LVGL 时，可通过 ``ESP_LV_ADAPTER_DISPLAY_SPI_WITH_PSRAM_DEFAULT_CONFIG`` 配置 SPI 屏幕。对于提供撕裂效应信号的屏幕，同步刷新配置见 `esp_lvgl_adapter 0.7.9 使用指南 <https://components.espressif.com/components/espressif/esp_lvgl_adapter/versions/0.7.9/readme>`__。

---------------------------

SPI 屏幕上的图片在硬件旋转 90 度或 270 度后会出现斜撕裂的现象，如何处理？
---------------------------------------------------------------------------------------------------------------------------

  建议在普通模式下使能 LVGL ``sw_rotate`` 标志位，使用 LVGL 的软件旋转功能进行处理。但要注意 ``sw_rotate`` 与 ``full_refresh``、 ``direct_mode`` 有冲突，请不要同时使用。例如在 ``full_refresh`` 下调用 ``sw_rotate`` 将直接返回，不会产生任何作用。

  .. note::

    ``sw_rotate``、 ``full_refresh``、 ``direct_mode`` 均为 **LVGL v8** 的 API。LVGL v9 的旋转方式有所不同，请参考 `LVGL v9 旋转说明 <https://lvgl.io/docs/open/9.1/API/display/>`__。

---------------------------

ESP32-S2 USB 摄像头和 I80 LCD 同时使用会导致 LCD 显示缺图像或者异常，如何解决？
---------------------------------------------------------------------------------------------------------------------------

  需要参考 `此段代码 <https://github.com/espressif/esp-iot-solution/blob/aefbcb52210e2fbaac7e8a8efcc68645ecd21e7a/components/bus/i2s_lcd_esp32s2_driver.c#L130>`__ 来增加 I2S 启动延迟时间。

---------------------------

通过非 LVGL 任务操作 LVGL 控件时出现异常 crash，如何解决？
---------------------------------------------------------------------------------------------------------------------------

  在其他任务中操作 LVGL 控件时，应与 LVGL 任务使用同一把锁。使用 esp_lvgl_adapter 时，可按下例加锁和解锁。

  .. code-block:: c

    if (esp_lv_adapter_lock(-1) == ESP_OK) {
        /* LVGL API 调用 */
        esp_lv_adapter_unlock();
    }

---------------------------

ESP32-S3 是否支持 RGB888？
---------------------------------------------------------------------------------------------------------------------------

  ESP32-S3 最多支持 16 根并行 RGB 数据线。对于 8 位串行 RGB888 屏，可在 ESP-IDF v6.x 的 ``esp_lcd_rgb_panel_config_t`` 中设置以下字段。使用 ESP-IDF v5.5 时，色深字段应写为 ``.bits_per_pixel = 24``。

  .. code-block:: c

    .data_width = 8,
    .in_color_format = LCD_COLOR_FMT_RGB888,

---------------------------

在操作 LVGL 的 tabview 时，想要禁止其左右滑动功能，该怎么实现？
---------------------------------------------------------------------------------------------------------------------------

  通过添加 ``lv_obj_clear_flag(lv_tabview_get_content(tabview), LV_OBJ_FLAG_SCROLLABLE);`` 这行代码即可。

---------------------------

LVGL 是否支持多 indev 输入？
---------------------------------------------------------------------------------------------------------------------------

  支持，所有 indev 按照链表管理，支持多个同类型和不同类型的输入设备。使用例程可以参考组件 `espressif/esp_lvgl_adapter <https://components.espressif.com/components/espressif/esp_lvgl_adapter>`__，目前组件支持的输入设备类型有 touch、button、knob。

---------------------------

LVGL 是否支持多点触控？
---------------------------------------------------------------------------------------------------------------------------

  LVGL 本身对多点触控的支持因版本而异：

  - **LVGL v8**：不支持原生多点触控，每个 indev 只能上报一个触点。
  - **LVGL v9**：支持多指针输入 (multi-pointer)，可为同一显示注册多个触摸 indev，各触点独立控制不同控件。

  使用 `esp_lvgl_adapter <https://docs.espressif.com/projects/esp-iot-solution/zh_CN/latest/display/tools/esp_lvgl_adapter.html>`__ 时，可在注册触摸设备时启用多点模式（仅 LVGL v9）：

  .. code-block:: c

    esp_lv_adapter_touch_config_t touch_cfg = ESP_LV_ADAPTER_TOUCH_DEFAULT_CONFIG(disp, touch_handle);
    touch_cfg.multi_touch.mode = ESP_LV_ADAPTER_TOUCH_MODE_MULTI_CONTROL;
    touch_cfg.multi_touch.pointers = 2;  /* 需 >= 2，且不超过 CONFIG_ESP_LCD_TOUCH_MAX_POINTS */
    lv_indev_t *touch = esp_lv_adapter_register_touch(&touch_cfg);

---------------------------

LVGL 统计的 CPU 占用率过高，有没有什么影响？
---------------------------------------------------------------------------------------------------------------------------

  LVGL v8 统计约 500 ms 内 timer handler 的忙碌时间。LVGL v9.4 根据 ``LV_SYSMON_GET_IDLE()`` 返回的空闲比例计算占用率。可以用 FreeRTOS 的 `vTaskGetRunTimeStats <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/system/freertos_idf.html#_CPPv420vTaskGetRunTimeStatsPc>`__ 查看各任务的 CPU 运行时间。

---------------------------

使能 RGB 屏驱动后，ESP32-S3 能否进入 Light-sleep 模式？
---------------------------------------------------------------------------------------------------------------------------

  **直接使用 esp_lcd RGB 驱动**：初始化 RGB 接口时，如果使能了 ``CONFIG_PM_ENABLE``，驱动会自动持有 ``ESP_PM_NO_LIGHT_SLEEP`` 锁，阻止系统自动进入 Light-sleep。如需释放该锁，必须先调用 ``esp_lcd_panel_del()`` 删除 RGB 面板，睡眠唤醒后再重新初始化。

  **使用** `esp_lvgl_adapter 组件 <https://docs.espressif.com/projects/esp-iot-solution/zh_CN/latest/display/tools/esp_lvgl_adapter.html>`__：该组件提供两种 Light-sleep 使用方式，LVGL 界面状态（控件树）在睡眠期间均可保留，无需重建 UI。

  **手动睡眠**：由应用代码控制完整的睡眠/唤醒流程：

    #. 进入睡眠前调用 ``esp_lv_adapter_sleep_prepare()`` 暂停适配器并等待当前帧刷新完成。
    #. 调用 ``esp_lcd_panel_del()`` 释放显示硬件资源。
    #. 调用 ``esp_light_sleep_start()`` 进入 Light-sleep。
    #. 唤醒后重新初始化 LCD 硬件，再调用 ``esp_lv_adapter_sleep_recover()`` 重新绑定面板并恢复适配器运行。

  **自动睡眠 (auto_sleep)**：在初始化时配置空闲超时，适配器在 LVGL 空闲超过指定时间后进入所配置的模式：

  .. code-block:: c

    esp_lv_adapter_config_t cfg = ESP_LV_ADAPTER_DEFAULT_CONFIG();
    cfg.auto_sleep.enable = true;
    cfg.auto_sleep.idle_timeout_ms = 5000;  /* 空闲 5 s 后自动睡眠 */

    /* PAUSE 暂停 LVGL 并释放适配器自身的锁。RGB 面板驱动持有的锁
       仍会阻止系统自动进入 Light-sleep。 */
    cfg.auto_sleep.mode = ESP_LV_ADAPTER_AUTO_SLEEP_MODE_PAUSE;
    cfg.auto_sleep.callbacks.on_enter_sleep = panel_sleep_cb;
    cfg.auto_sleep.callbacks.on_exit_sleep  = panel_wake_cb;

    /* User 模式：on_enter_sleep 回调负责完整的 sleep_prepare → LCD deinit →
       light_sleep_start → LCD init → sleep_recover 流程 */
    /* cfg.auto_sleep.mode = ESP_LV_ADAPTER_AUTO_SLEEP_MODE_USER; */

    ESP_ERROR_CHECK(esp_lv_adapter_init(&cfg));

  Pause 模式下，已注册的触摸/按键/旋钮输入会自动通知适配器唤醒；自定义唤醒源可调用 ``esp_lv_adapter_request_wake()`` 或 ``esp_lv_adapter_request_wake_from_isr()``。

---------------------------

我们是否支持驱动液晶段码屏？
-------------------------------------------------------------------------------

  我们的芯片无法通过 GPIO 直接连接液晶段码屏进行驱动，因为驱动段码屏需要高低电平循环，要求工作电压为 2.7 V 至 5.0 V 的交流电压，典型值为 3.0 V、3.3 V、4.5 V 和 5.0 V，而我们的芯片不支持调整电压范围。

---------------------------

使用 ESP32-P4 驱动 RGB LCD 时，屏幕出现颜色异常，如何排查？
-------------------------------------------------------------------------------

  ESP32-P4 拥有多路 VDDPST 电源域，每路 VDDPST 控制对应区域 GPIO 的最大输出电平（具体 GPIO 与 VDDPST 的对应关系请参考 `ESP32-P4 技术规格书 <https://www.espressif.com/sites/default/files/documentation/esp32-p4_datasheet_cn.pdf>`__）。若对应 VDDPST 供电不足或未正确配置，部分 GPIO 最大输出电平可能为 1.8 V，导致 RGB 接口信号电平不足，进而引发屏幕颜色异常。请检查 RGB 接口所用 GPIO 的 VDDPST 是否已配置为正确电压（通常为 3.3 V）。

  前文的 30 MHz PCLK 是 ESP32-S3 搭配 120 MHz 8 线 PSRAM 的测试结果。实际可用的 PCLK 取决于芯片和可用内存带宽。

---------------------------

ESP32-P4 是否支持输出 HDMI 信号？
-------------------------------------------------------------------------------

  ESP32-P4 不支持直接输出 HDMI 信号，但可以通过 MIPI-DSI 转 HDMI 的芯片来实现 HDMI 信号输出。乐鑫支持的 MIPI-DSI 转 HDMI 芯片包括 `LT8912B <https://github.com/espressif/esp-bsp/tree/master/components/lcd/esp_lcd_lt8912b>`__，相关使用方法可参考 `示例代码 <https://github.com/espressif/esp-iot-solution/tree/master/examples/display/lcd/hdmi_video_renderer>`__。另见 `LT9611 示例 <https://github.com/espressif/esp-idf/tree/v6.1.1/examples/peripherals/lcd/dsi_hdmi_bridge>`__。

---------------------------

在 LVGL 应用中，RGB 或者 MIPI-DSI 接口屏幕如何旋转 90 度/270 度？如何避免撕裂现象？如何进一步提高帧率？
----------------------------------------------------------------------------------------------------------

  - 推荐使用 `esp_lvgl_adapter 组件 <https://docs.espressif.com/projects/esp-iot-solution/zh_CN/latest/display/tools/esp_lvgl_adapter.html>`__。该组件提供了高效率旋转、防撕裂、帧率提升等特性，并且支持 LVGL v8 和 v9 版本。
  - 参考示例代码 `esp_lvgl_adapter 示例 <https://github.com/espressif/esp-iot-solution/tree/master/examples/display/gui/lvgl_common_demo>`__。

--------------

.. _esp32-p4-mipi-mipi-dsi-lp-hp:

ESP32-P4 在未连接 MIPI 外设的情况下，能否产生 MIPI-DSI 信号（LP 和 HS）？
--------------------------------------------------------------------------------------------------------

  主机可以发送 LP（低功耗）和 HS（高速）信号。未连接接收端时，主机请求帧应答可能导致视频传输停滞。在 ESP-IDF v6.1.1 中，测量输出波形时可设置 ``esp_lcd_dpi_panel_config_t`` 的 ``flags.disable_frame_ack`` 来关闭帧应答请求。

--------------

EAF 格式的 GIF 动画在 ESP32-S3/ESP32-P4 上播放较慢，如何优化？
-------------------------------------------------------------------

  - 可将 EAF 编码格式改为 JPEG（在转换工具中设置），体积会增大但解码更快；
  - 对于较大分辨率屏幕（如 466 × 466），LVGL 渲染负担较重；
  - 相比 EAF + LVGL，直接使用 `esp_emote_gfx <https://components.espressif.com/components/espressif2022/esp_emote_gfx>`__ 组件刷屏（分段解码）效率更高，EAF 本来就是为 esp_emote_gfx 设计的，只是额外适配到了 LVGL；
  - 对于视频播放，可尝试使用 JPEG 帧编码的 AVI 文件，并在相同分辨率下比较播放效果。

---------------------------

ESP32-P4 驱动 MIPI-DSI LCD 无图像显示，且无其他报错日志，如何排查？
-------------------------------------------------------------------

  首先检查 D-PHY 的 2.5 V 供电、屏幕复位和初始化时序，以及时钟线对和所有已启用数据线对的连接。可使用 DSI 测试图检查链路。

  如果驱动报告帧缓冲欠载 (underrun)，请根据像素时钟和帧缓冲色深检查可用 PSRAM 带宽。ESP-IDF 例程使用 ``CONFIG_SPIRAM_SPEED_200M=y``。

---------------------------

ESP32-P4 驱动 MIPI-DSI LCD 出现画面扭曲或错位，如何处理？
-------------------------------------------------------------------

  该问题一般由 ``lane_bit_rate_mbps`` 与实际 ``pixel_clock`` 不匹配，或 ``lane_bit_rate_mbps`` 与屏幕要求的速率不匹配引起。可根据分辨率、刷新率、色深和 lane 数量重新计算 ``lane_bit_rate_mbps`` （预留约 20% 余量），具体计算方法请参考 `MIPI DSI LCD 详解 <https://docs.espressif.com/projects/esp-iot-solution/zh_CN/latest/display/lcd/mipi_dsi_lcd.html>`__。注意 ESP32-P4 上 ``lane_bit_rate_mbps`` 最大不超过 1500，建议最小不低于 480。

---------------------------

ESP32-P4 驱动 MIPI-DSI LCD 出现屏幕闪蓝屏，并提示 "can't fetch data from external memory fast enough, underrun happens"，如何处理？
-----------------------------------------------------------------------------------------------------------------------------------

  该问题由 PSRAM 带宽不足导致。可尝试以下方法：

  - 降低 ``lane_bit_rate_mbps`` 和 ``dpi_clock_freq_mhz`` （像素时钟频率）。
  - 若使用 RGB888 色彩格式，考虑改为 RGB565 以降低带宽需求。
  - 开启以下配置项以改善 PSRAM 带宽：

    - ``CONFIG_SPIRAM_XIP_FROM_PSRAM=y``
    - ``CONFIG_CACHE_L2_CACHE_256KB=y``
    - ``CONFIG_CACHE_L2_CACHE_LINE_128B=y``
    - ``CONFIG_COMPILER_OPTIMIZATION_PERF=y``
