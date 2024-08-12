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

  请参考 `ESP-IoT-Solution 编程指南 - LCD 开发指南 <https://docs.espressif.com/projects/esp-iot-solution/zh_CN/latest/display/lcd/lcd_development_guide.html#id2>`__。

---------------

ESP 系列芯片 LCD 屏幕适配情况是怎样的？
-------------------------------------------------------------------

  请参考 `ESP-IoT-Solution 编程指南 - LCD 开发指南 <https://docs.espressif.com/projects/esp-iot-solution/zh_CN/latest/display/lcd/lcd_development_guide.html#id2>`__。

--------------

ESP32-P4 驱动 MIPI-DSI LCD 的一些说明
-------------------------------------------------------------------

  - 最高支持 2-lane，每路最高支持 1.5 Gbps 的速率（共 3 Gbps），并且支持 ``RGB565``、``RGB666``、``RGB888`` 颜色格式。
  - 部分 MIPI-DSI LCD 默认通过硬件 (IM[0:3]) 配置为 4-lane，如 ``ILI9881``、``JD9365``，但是可以通过修改 LCD 的初始化命令来配置为 2-lane（如 ILI9881 的 ``B6h-B7h`` 命令），因此需要查看 LCD 驱动 IC 的数据手册来判断是否能够支持。
  - MIPI-DSI 驱动默认开启了通信应答机制，如果 ESP 与 LCD 之前出现通信异常，ESP 可能会卡死并触发看门狗，此时请检查硬件连接是否正确，或者使用逻辑分析仪检查通信是否正常。

--------------

ESP 系列芯片的带屏开发板是否支持使用 Arduino IDE 开发 GUI？
-----------------------------------------------------------------------------------------------------------------

  - 目前官方已推出用于 Arduino 开发的 LCD 驱动库 `ESP32_Display_Panel <https://github.com/esp-arduino-libs/ESP32_Display_Panel>`__，可以直接在 Arduino IDE 上下载，支持的开发板请参考 `文档 <https://github.com/esp-arduino-libs/ESP32_Display_Panel/blob/master/README_CN.md#%E4%B9%90%E9%91%AB%E5%BC%80%E5%8F%91%E6%9D%BF>`__。
  - 需要注意以下几点：

    - ESP32_Display_Panel 依赖于 `arduino-esp32 <https://github.com/espressif/arduino-esp32>`__。
    - 由于 ESP32-S3 的 RGB 接口存在 :ref:`屏幕漂移 <lcd-rgb-screen-drift>` 问题，需要使用 ESP-IDF release/v5.1 及以上版本的特性来解决，而 arduino-esp32 v2.x.x 版本中使用的 ESP-IDF 版本为 v4.4.x，因此该版本无法解决此问题，需要使用 arduino-esp32 v3.x.x 版本，详细说明请参考 `文档 <https://github.com/esp-arduino-libs/ESP32_Display_Panel/blob/master/README_CN.md#%E4%BD%BF%E7%94%A8-esp32-s3-%E9%A9%B1%E5%8A%A8-rgb-lcd-%E6%97%B6%E5%87%BA%E7%8E%B0%E7%94%BB%E9%9D%A2%E6%BC%82%E7%A7%BB%E9%97%AE%E9%A2%98%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88>`_。
    - 由于使用 Arduino 无法像 ESP-IDF 一样通过 menuconfig 来调整各种参数配置，如编译优化等级等，所以为了实现最佳的性能，推荐基于 ESP-IDF 开发 GUI。

--------------

如何提高 LCD 的显示帧率？
-----------------------------------------------------

  - 关于帧率的详细介绍请参考 `ESP-IoT-Solution 编程指南 - LCD 概述 <https://docs.espressif.com/projects/esp-iot-solution/zh_CN/latest/display/lcd/lcd_guide.html#id9>`__。一般来说，受限于 ESP 的计算性能，“接口帧率”往往远大于“渲染帧率”，因此该问题可以表述为“如何提高 LCD 的渲染帧率”。针对这个问题，可以从以下三个方面进行考虑：

    - 提高 ESP 的性能。在使用 ESP-IDF 开发时可以通过 menuconfig 来配置 ESP，而默认并没有配置到最佳性能，这里以 ``ESP32-S3`` 为例，我们可以提高 CPU 频率到最高 ``240 MHz``，提高 FreeRTOS tick 的频率到 1000，增大 flash 或 PSRAM 的带宽。除此之外，还有增大 data cache line size，设置编译优化等级为 ``-O2`` 等等。
    - 提高 LVGL 的性能。LVGL 本身也是可以通过 menuconfig 或者 *lv_conf.h* 文件进行配置的，例如设置 LVGL 使用 ESP-IDF 中的 ``malloc`` 和 ``memcpy`` 等内存操作函数，开启 ``fast memory`` 编译选项等。
    - 优化应用设计。一方面可以通过调整任务的优先级或指定 CPU 核使得 LVGL 和其他任务充分利用 CPU 资源，尤其是对具有双核的 ESP；另一方面也可以优化 GUI 的设计，比如尽量避免使用复杂的动画以及具有透明度的图层混叠效果。

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

  - 详细 LCD 及 LVGL 性能说明，请参考 `文档 <https://github.com/espressif/esp-bsp/blob/master/components/esp_lvgl_port/docs/performance.md>`__。

---------------

ESP32 是否有 I2S 驱动 LCD 的参考代码？
----------------------------------------------------

  - ESP32/ESP32-S2 使用 I2S 驱动的屏幕接口类型为 i80(8080)
  - 关于例程，请参考 :ref:`LCD 例程 <lcd-examples>`。

---------------

ESP 系列芯片最大可以支持多少分辨率的 LCD？相应的帧率是多少？
----------------------------------------------------------------------------------------------------------

  - 对于 ESP32-S3 和 ESP32-P4 的 RGB 外设接口，由于受其硬件限制，理论上最大支持 ``4096 x 1024`` 分辨率（水平最大为 ``4096``，垂直最大为 ``1024``）；对于 ESP 系列芯片的其他外设接口，可以支持多大的分辨率并没有一个“最大”的硬件限制，
  - 由于芯片的存储大小、计算性能和外设接口的传输带宽有限，而且不同接口类型的 LCD 通常具有特定范围内的分辨率，因此针对 ESP32-C3 和 ESP32-S3 这两款芯片推荐使用 LCD 的分辨率如下：

    .. list-table::
        :header-rows: 1

        * - SoCs
          - SPI
          - QSPI
          - I80
          - RGB
          - MIPI-DSI

        * - ESP32-C3
          - 240 x 240
          - 不推荐
          - 不支持
          - 不支持
          - 不支持

        * - ESP32-S3
          - 320 x 240
          - 400 x 400
          - 480 x 320
          - 480 x 480，800 x 480
          - 不支持

        * - ESP32-P4
          - 320 x 240
          - 400 x 400
          - 480 x 320
          - 480 x 480，800 x 480
          - 1024 x 600，1280 x 720

  - 针对 ESP32-S3 的 RGB 接口，目前基于 LVGL (v8) 应用场景测试过的最大分辨率为 800 x 480，接口帧率上限为 59 (PCLK 30 MHz), 对应 LVGL 平均帧率为 23; LVGL 平均帧率上限为 26, 对应接口帧率为 41 (PCLK 21 MHz)。
  - 针对 ESP32-P4 的 MIPI-DSI 接口，目前基于 LVGL (v8) 应用场景测试过的最大分辨率为 1080 x 1920，接口帧率上限为 31 (DPI_CLK 80 MHz，2-lane bit rate 2.8 Gbps), 对应 LVGL 平均帧率为 4;

---------------

ESP32-S3R8 如何开启 PSRAM 120M Octal (DDR)？
----------------------------------------------------------------------------------------------------------

  - ESP-IDF 需要使用 **release/v5.1** 及以上分支版本。
  - 通过 menuconfig 开启配置项： ``IDF_EXPERIMENTAL_FEATURES``, ``SPIRAM_SPEED_120M``, ``SPIRAM_MODE_OCT``。
  - ``ESP32-S3-WROOM-1-N16R16V`` 模组目前不支持此功能，如果启用，可能会出现芯片在上电时卡死然后复位的问题。
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

  - 开启 RGB 驱动的 Bounce Buffer 模式，并且 buffer 越大效果越好，使用方法请参考 `文档 <https://docs.espressif.com/projects/esp-idf/en/v5.1.4/esp32s3/api-reference/peripherals/lcd.html#bounce-buffer-with-single-psram-frame-buffer>`__。需注意，由于该模式下是先通过 CPU 搬运 PSRAM 数据到 SRAM，再通过 GDMA 传输数据到 RGB 外设，因此需要同时开启 ``CONFIG_ESP32S3_DATA_CACHE_LINE_64B=y``，否则可能会导致屏幕出现漂移。
  - 经过少量测试，4 线 PSRAM 80 MHz 时的 PCLK 最高设置至 11 MHz，8 线 PSRAM 80 MHz 时的 PCLK 最高设置至 22 MHz，8 线 PSRAM 120 MHz 时的 PCLK 最高设置至 30 MHz。
  - 对于使用 LVGL 的应用，可以将执行 RGB 外设初始化的任务与执行 LVGL ``lv_timer_handler()`` 的任务分配在同一个核上，能够显著提升 PCLK 的设置上限。

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

    - RGB 外设的 PCLK 设置过高，PSRAM 或 GDMA 的带宽无法满足。
    - PSRAM 和 flash 共用一组 SPI 接口，受写 flash 操作（如 Wi-Fi、OTA、低功耗蓝牙）影响，期间 PSRAM 被禁用。
    - 读取大量的 flash/PSRAM 数据，导致 PSRAM 带宽不足。

  - **配置方面**

    - 提高 PSRAM 和 flash 带宽，比如在硬件允许的条件下，采用更高的频率或更大的位宽。
    - 开启 ``CONFIG_COMPILER_OPTIMIZATION_PERF``。
    - 降低 Data Cache Line Size 到 32 Byte（使用 RGB ``Bounce Buffer`` 模式时需要设置到 64 Byte）。
    - 开启 ``CONFIG_SPIRAM_FETCH_INSTRUCTIONS`` 和 ``CONFIG_SPIRAM_RODATA``。
    - （不推荐）开启 ``CONFIG_LCD_RGB_RESTART_IN_VSYNC``，可以在屏幕漂移后自动恢复，但无法避免该问题并且降低帧率。

  - **应用方面**

    - 在保证屏幕正常工作的前提下，尽量减小 PCLK 的频率，降低 PSRAM 的带宽占用。
    - 如果需要使用 Wi-Fi、低功耗蓝牙和连续写 flash 的操作，请采用 ``XIP on PSRAM + RGB Bounce buffer`` 的方法，其中， ``XIP on PSRAM`` 用于将代码段和只读段的数据加载到 PSRAM，开启后执行写 flash 操作不会禁用 PSRAM。 ``RGB Bounce buffer`` 用于将帧缓存的数据分块通过 CPU 从 PSRAM 搬运到 SRAM，然后再使用 GDMA 传输数据到 RGB 外设，相较于直接采用 PSRAM GDMA 的方式能够实现更高的传输带宽。设置步骤如下：

      - 确认 ESP-IDF 版本为较新（> 2022.12.12）的 release/v5.0 及以上，因为旧版本不支持 ``XIP on PSRAM`` 的功能（release/v4.4 可以通过打补丁的方式实现，但不推荐）。
      - 确认 PSRAM 配置里面是否能开启 ``CONFIG_SPIRAM_FETCH_INSTRUCTIONS`` 和 ``CONFIG_SPIRAM_RODATA`` 这两项。如果只读段数据过大（如大量图片），会导致 PSRAM 空间不够，此时可以采用文件系统或将图片制作成 bin 加载到指定分区。
      - 确认内存（SRAM）是否有余量，大概需要占用 [10 * screen_width * 4] 字节。
      - 设置 ``Data cache line size`` 为 64 Byte（可设置 ``Data cache size`` 为 32 KB 以节省内存）。
      - 设置 ``CONFIG_FREERTOS_HZ`` 为 1000。
      - 如以上均符合条件，那么就可以参考 `文档 <https://docs.espressif.com/projects/esp-idf/en/v5.1.4/esp32s3/api-reference/peripherals/lcd.html#bounce-buffer-with-single-psram-frame-buffer>`__ 修改 RGB 驱动为 ``Bounce buffer`` 模式。 如果开启后仍存在漂移现象，可以尝试增大 buffer，但是会占用更多的 SRAM 内存。
      - 如操作 Wi-Fi 仍存在屏幕漂移问题，可以尝试关闭 PSRAM 里 ``CONFIG_SPIRAM_TRY_ALLOCATE_WIFI_LWIP`` 一项（会占用较大 SRAM）。
      - 设置后带来的影响包括：CPU 使用率升高、可能会造成中断看门狗复位、会造成较大内存开销。
      - 由于 Boucne Buffer 是在 GDMA 中断里通过 CPU 搬运 PSRAM 的数据到 SRAM，程序需要避免长时间执行关中断的操作（如调用 ``portENTER_CRITICAL()``），否则仍会造成屏幕漂移。

    - 短时操作 flash 导致漂移的情况，如 wifi 连接等操作前后，可以在操作前调用 ``esp_lcd_rgb_panel_set_pclk()`` 降低 PCLK（如 6 MHz）并延时大约 20 ms（RGB 刷完一帧的时间），然后在操作结束后提高 PCLK 至原始水平，期间可能会造成短暂的闪白屏现象。
    - 如果无法避免，可以开启 ``CONFIG_LCD_RGB_RESTART_IN_VSYNC`` 或调用 ``esp_lcd_rgb_panel_restart()`` 接口重置 RGB 时序，防止永久性漂移。
    - 关于如何在 Arduino 中避免 RGB 屏幕漂移问题，请参考 `链接 <https://github.com/esp-arduino-libs/ESP32_Display_Panel?tab=readme-ov-file#how-to-fix-screen-drift-issue-when-driving-rgb-lcd-with-esp32-s3>`__。

---------------------------

为什么驱动 SPI/8080 LCD 屏幕显示 LVGL 时出现纵向错位？
-------------------------------------------------------------------------------

  如果采用 DMA 中断传输的方式，LVGL 的 ``lv_disp_flush_ready()`` 需要在 DMA 传输结束后调用，而不是 ``draw_bitmap()`` 后立即调用。

---------------------------

使用 ESP32-C3 通过 SPI 接口驱动 LCD 液晶显示屏，是否可使用 RTC_CLK 作为 SPI 时钟，让 LCD 液晶显示屏能在 Deep-sleep 模式下正常显示静态图片？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Deep-sleep 模式：CPU 和大部分外设都会掉电，只有 RTC 存储器处于工作状态。具体请参考 `《ESP32-C3 技术规格书》 <https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_cn.pdf>`__ 中关于“低功耗管理”的说明。
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

  - 检查是否为 RGB/BGR 设置错误：如将屏幕配置为红色 (0xC0, 0x0, 0x0)，但屏幕实际显示黑色。
  - 检查 RGB 和 BGR 的寄存器是否设置：如 ST7789，可通过 MADCTL (36h) 寄存器修正（当 MADCTL (36h) = 1 时，为 BGR，当 MADCTL (36h) = 0 时，为 RGB）。
  - 检查是否为 LVGL SWAP16 设置错误：如将屏幕配置为红色 (0xC0, 0x0, 0x0)，但屏幕实际显示蓝色，此时可 menuconfig → Component config → LVGL configuration → Color settings
  - 如 RGB TTL 屏幕显示缺色，需要分别设置 R、G、B 显示，检查有波形的通道和 RGB 数据线设计是否符合。

---------------------------

LVGL 的 label 中正确输入了空格，比如“室内温度 25.5℃”，但在屏幕上没有显示空格，请问是什么原因，怎么排查？
---------------------------------------------------------------------------------------------------------------------------

  这属于 LVGL label 显示缺失，可以打开如下调试项，缺失字符会用方块填充，防止 map 缺失：

    - ``Component config`` → ``LVGL configuration`` → ``Font usage`` → ``Enable drawing placeholders when glyph dsc is not found``

---------------------------

LVGL 连续加载存放在 flash 上的不同图片时速度太慢，比如在屏幕首页循环展示三张图片时该如何规避速度慢的问题？
---------------------------------------------------------------------------------------------------------------------------

  - 速度慢的原因是没有打开对应的图片缓存机制，每次使用时都需要通过解析器进行解析。
  - 直接通过 ``#define LV_IMG_CACHE_DEF_SIZE 1`` 宏打开对应的图片缓存机制即可，这里的 1 代表图片缓存的数量。请注意，此操作会消耗更多内存。

---------------------------

LVGL 加载 flash 里的 PNG、JPEG 图片失败。屏幕上显示一片空白，什么原因？
---------------------------------------------------------------------------------------------------------------------------

  - 首先需要查看下剩余内存的情况，LVGL 加载图片需要进行 loadpng_get_raw_size 和 loadpng_convert 两个步骤，如内存不够会直接返回错误码 83。
  - 也可以提前估计下内存需求：``loadpng_get_raw_size`` 需要和图片大小一致的内存，``loadpng_convert`` 需要图片长度*宽度*3 字节的内存，如果还开启了图片缓存机制导致 ``image_cache`` 过大，会同步导致内存紧张。

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

  在将图片用 imageconverter 转成 MAP 时，如采用 CF_TRUE_COLOR 等格式（非 RAW 格式）转换，后续 LVGL 加载均不需要二次解码，但会占用比较大的代码段。

---------------------------

在使用 LVGL 的一些第三方库如 FreeType、Lottie 时，程序正常加载，但是屏幕显示一片空白，为什么？
---------------------------------------------------------------------------------------------------------------------------

  先考虑任务堆栈设置是否有误，一般需要分配 30 KB 以上的任务堆栈。也可以参考以下 demo：

  - `freetype demo <https://github.com/espressif/esp-iot-solution/tree/master/examples/hmi/lvgl_freetype>`__
  - `lottie 移植 <https://docs.lvgl.io/master/libs/rlottie.html>`__

---------------------------

ESP32-S3 驱动 SPI 屏幕，内部 RAM 不够给整屏 buffer 分配空间，有什么好的办法？
---------------------------------------------------------------------------------------------------------------------------

  可使用 PSRAM 做 framebuffer，然后用较小的 SRAM buffer 来将数据分多次搬运到 framebuffer（SPI DMA 无法直接搬运 PSRAM 数据），完成搬运后直接用 framebuffer 进行渲染即可。相比小 buffer 直接渲染然后发送数据，可防撕裂，加快渲染速度。具体实现可参考 `esp_lvgl_port <https://components.espressif.com/components/espressif/esp_lvgl_port/versions/1.4.0?language=en>`__。

---------------------------

SPI 屏幕上的图片在硬件旋转 90 度或 270 度后会出现斜撕裂的现象，如何处理？
---------------------------------------------------------------------------------------------------------------------------

  建议在普通模式下使能 LVGL sw_rotate 标志位，使用 LVGL 的 sw_rotate 功能来进行软件旋转。但要注意 sw_rotate 功能和 full_refresh、direct_mode 有冲突，请不要一起使用。比如在 full_refresh 下调用 sw_rotate 将会直接 return，不会产生任何作用。

---------------------------

ESP32-S2 USB 摄像头和 I80 LCD 同时使用会导致 LCD 显示缺图像或者异常，如何解决？
---------------------------------------------------------------------------------------------------------------------------

  需要参考 `此段代码 <https://github.com/espressif/esp-iot-solution/blob/aefbcb52210e2fbaac7e8a8efcc68645ecd21e7a/components/bus/i2s_lcd_esp32s2_driver.c#L130>`__ 来增加 I2S 启动延迟时间。

---------------------------

通过非 LVGL 任务操作 LVGL 控件时出现异常 crash，如何解决？
---------------------------------------------------------------------------------------------------------------------------

  操作 LVGL 控件时使用 ``bsp_display_lock()`` 和 ``bsp_display_unlock()`` 来保护操作变量，进而保证线程安全。

---------------------------

ESP32-S3 是否支持 RGB888？
---------------------------------------------------------------------------------------------------------------------------

  不支持并行 RGB888，只能支持 RGB565。可以设置串行 RGB888 输出，如下：

  .. code-block:: c

    esp_lcd_rgb_panel_config_t panel_conf = {
    ...
    .data_width = 8,
    .bits_per_pixel = 24,
    ...
    }

---------------------------

在操作 LVGL 的 tabview 时，想要禁止其左右滑动功能，该怎么实现？
---------------------------------------------------------------------------------------------------------------------------

  通过添加 ``lv_obj_clear_flag(lv_tabview_get_content(tabview), LV_OBJ_FLAG_SCROLLABLE);`` 这行代码即可。

---------------------------

LVGL 是否支持多 indev 输入？
---------------------------------------------------------------------------------------------------------------------------

  支持，所有 indev 按照链表管理，支持多个同类型和不同类型的输入设备。使用例程可以参考组件 `espressif/esp_lvgl_port <https://components.espressif.com/components/espressif/esp_lvgl_port>`__，目前组件支持输入有 touch、button、knob、hid_host。

---------------------------

LVGL 统计的 CPU 占用率过高，有没有什么影响？
---------------------------------------------------------------------------------------------------------------------------

  LVGL 统计的 CPU 占用率计算的是 500 ms 内 LVGL 渲染任务的时长，并不能代表 CPU 真实的占用率。可以用 FreeRTOS 的 `vTaskGetRunTimeStats <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/system/freertos_idf.html#_CPPv420vTaskGetRunTimeStatsPc>`__ 来统计真实占用率。

---------------------------

使能 RGB 屏驱动后，ESP32-S3 能否进入 Light-sleep 模式？
---------------------------------------------------------------------------------------------------------------------------

  不能。在初始化 RGB 接口时，如果使能了 ``CONFIG_PM_ENABLE``，会自动锁住 ``ESP_PM_NO_LIGHT_SLEEP``，导致无法进入 Light-sleep 模式。此时如果想进入 Light-sleep 模式，需要先执行 ``lcd_rgb_panel_destory`` 来禁用 RGB 屏驱动。

---------------------------

我们是否支持驱动液晶段码屏？
-------------------------------------------------------------------------------

  我们的芯片无法通过 GPIO 直接连接液晶段码屏进行驱动，因为驱动段码屏需要高低电平循环，要求工作电压为 2.7 V 至 5.0 V 的交流电压，典型值为 3.0 V、3.3 V、4.5 V 和 5.0 V，而我们的芯片不支持调整电压范围。
