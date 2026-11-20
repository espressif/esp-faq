LCD
============

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

.. _lcd-examples:

Where are the LCD drivers and reference examples for ESP series chips?
--------------------------------------------------------------------------------------------------------------------------------------

  - Please first understand the LCD development process through the `ESP-IoT-Solution Programming Guide - LCD Development Guide <https://docs.espressif.com/projects/esp-iot-solution/en/latest/display/lcd/lcd_development_guide.html#supported-interface-types>`__.
  - For basic LCD driver examples, please refer to `esp-idf/examples/peripherals/lcd <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/lcd>`__.
  - For advanced LCD driver examples, please refer to `esp-iot-solution/examples/display <https://github.com/espressif/esp-iot-solution/tree/master/examples/display>`__.

---------------

Which adapted ICs can be used by the LCD screen of ESP32 series chips?
-------------------------------------------------------------------------------------------------

  - For support of SPI, I80, RGB, MIPI-DSI, and other interfaces across ESP chip series, please refer to `LCD Development Guide - Supported Interface Types <https://docs.espressif.com/projects/esp-iot-solution/en/latest/display/lcd/lcd_development_guide.html#supported-interface-types>`__. Some chips (such as ESP32-C5, ESP32-H2, and ESP32-H4) do not have a native I80 peripheral, but can drive an LCD by simulating I80 timing through the Parlio interface in esp_lcd. In ESP-IDF v6.1.1, ESP32-C6 lacks the ``SOC_PARLIO_LCD_SUPPORTED`` capability required by this driver.
  - For the list of LCD driver IC components officially ported by Espressif based on esp_lcd (including I2C, SPI, QSPI, I80, MIPI-DSI, 3-wire SPI + RGB, and other interfaces), please refer to `LCD Development Guide - Driver and Examples <https://docs.espressif.com/projects/esp-iot-solution/en/latest/display/lcd/lcd_development_guide.html#driver-and-examples>`__.

--------------

Common issues in application development with the ESP series chips
-------------------------------------------------------------------

  For common issues about the LCD screen, please refer to the `LCD Application Development Notes <https://docs.espressif.com/projects/esp-techpedia/en/latest/esp-friends/advanced-development/lcd-application-note/index.html>`__.

--------------

Notes for Driving MIPI-DSI LCD with ESP32-P4
-------------------------------------------------------------------

  - ESP32-P4 supports MIPI-DSI LCD with up to 2 lanes. Each supports a maximum rate of 1.5 Gbps, totaling 3 Gbps. It also supports color formats RGB565, RGB666, and RGB888.
  - Some MIPI-DSI LCDs, such as ILI9881C and JD9365, are configured as 4-lane by default through hardware. However, most ICs support switching to 2-lane by modifying initialization registers. The register addresses and operations vary by IC model; please consult the LCD driver IC datasheet or the panel vendor. ESP32-P4 only supports 1-lane and 2-lane configurations.
  - When configuring ``lane_bit_rate_mbps``: the maximum must not exceed 1500 Mbps; a minimum of 480 Mbps is recommended. The actual value can be calculated from resolution, refresh rate, color depth, and lane count, then determined with a 20% margin. For the calculation method, please refer to `MIPI DSI LCD Detailed Guide <https://docs.espressif.com/projects/esp-iot-solution/en/latest/display/lcd/mipi_dsi_lcd.html>`__.
  - The MIPI-DSI driver enables the communication response mechanism (frame ACK) by default. If there is a communication anomaly between the ESP and the LCD, the ESP may freeze and trigger the watchdog. At this point, please check whether the hardware connection is correct, whether the initialization command is correct, whether the reset timing is correct, or use a logic analyzer to troubleshoot communication issues.
  - Driving a MIPI-DSI screen requires a stable 2.5 V power supply for the MIPI DSI PHY (obtained via an LDO). Please refer to the LDO configuration section in the corresponding example code.

--------------

Do ESP series development boards with screens support GUI development using the Arduino IDE?
-----------------------------------------------------------------------------------------------------------------

  - The official LCD driver library for Arduino development, `ESP32_Display_Panel <https://github.com/esp-arduino-libs/ESP32_Display_Panel>`__, has been released. It can be directly downloaded on the Arduino IDE. For supported development boards, please refer to the `documentation <https://github.com/esp-arduino-libs/ESP32_Display_Panel/blob/master/README.md#supported-boards>`__.
  - Several points to note:

    - ESP32_Display_Panel relies on `arduino-esp32 <https://github.com/espressif/arduino-esp32>`__.
    - Due to the :ref:`screen drift <lcd-rgb-screen-drift>` issue with the RGB interface of ESP32-S3, it is necessary to use features from ESP-IDF release/v5.1 or later to solve the problem. However, the ESP-IDF version used in arduino-esp32 v2.x.x is v4.4.x, which cannot solve this problem. Therefore, you should use arduino-esp32 v3.x.x. For detailed instructions, please refer to `Document <https://github.com/esp-arduino-libs/ESP32_Display_Panel/blob/master/docs/envs/use_with_arduino.md#solution-for-screen-drift-issue-when-using-esp32-s3-to-drive-rgb-lcd-in-arduino-ide>`__.
    - Given that Arduino cannot adjust various parameter configurations, such as compile optimization levels, through menuconfig like ESP-IDF, it is recommended to develop a GUI based on ESP-IDF to achieve optimal performance.

--------------

How can I improve the display frame rate of LCD screens?
----------------------------------------------------------

  - For a detailed introduction to frame rates, please refer to the `ESP-IoT-Solution Programming Guide - LCD Overview <https://docs.espressif.com/projects/esp-iot-solution/en/latest/display/lcd/lcd_guide.html#frame-rate>`__. Generally speaking, due to the computational performance of the ESP, the "interface frame rate" is often much higher than the "rendering frame rate", so this issue can be described as "how to improve the rendering frame rate of the LCD". This issue can be considered from the following three aspects:

    - Improve the performance of ESP. When developing with ESP-IDF, ESP can be configured through menuconfig, but it is not configured to the best performance by default. Here, taking ESP32-S3 as an example, we can increase the CPU frequency to the highest 240 MHz, increase the frequency of FreeRTOS tick to 1000, and increase the bandwidth of flash or PSRAM. In addition, we can also increase the data cache line size, set the compilation optimization level to ``-O2``, and so on.
    - Improve the performance of LVGL. LVGL itself can also be configured through menuconfig or the *lv_conf.h* file, such as setting LVGL to use the ``malloc`` and ``memcpy`` memory operation functions in ESP-IDF, enabling the fast memory compilation option, etc.
    - Optimize application design. You can make full use of CPU resources by adjusting the priority of tasks or specifying CPU cores for LVGL and other tasks, especially for ESPs with dual cores. Besides, you can also optimize the design of the GUI, such as avoiding the use of complex animations and layers with transparency overlay effects as much as possible.

  - Taking ESP32-S3R8 as an example, the following ESP configuration items can improve the frame rate (ESP-IDF release/v5.1):

    - ``CONFIG_FREERTOS_HZ=1000``
    - ``CONFIG_ESP_DEFAULT_CPU_FREQ_MHZ_240=y``
    - ``CONFIG_ESPTOOLPY_FLASHMODE_QIO=y``
    - ``CONFIG_ESPTOOLPY_FLASHFREQ_120M=y`` [should be consistent with PSRAM]
    - ``CONFIG_SPIRAM_MODE_OCT=y``
    - ``CONFIG_IDF_EXPERIMENTAL_FEATURES=y`` and ``CONFIG_SPIRAM_SPEED_120M=y`` [should be consistent with flash]
    - ``CONFIG_SPIRAM_FETCH_INSTRUCTIONS=y``
    - ``CONFIG_SPIRAM_RODATA=y``
    - ``CONFIG_ESP32S3_DATA_CACHE_LINE_64B=y``
    - ``CONFIG_COMPILER_OPTIMIZATION_PERF=y``

  - On ESP32-P4, you can adjust the following configurations to increase the frame rate (applicable to ESP-IDF release/v5.4 and later; release/v6.0 is recommended):

    - ``CONFIG_CACHE_L2_CACHE_256KB=y``
    - ``CONFIG_CACHE_L2_CACHE_LINE_128B=y``
    - ``CONFIG_SPIRAM_XIP_FROM_PSRAM=y``
    - ``CONFIG_COMPILER_OPTIMIZATION_PERF=y``

  - The following LVGL configuration items can help improve the frame rate:

    - **LVGL v8**: ``CONFIG_LV_MEM_CUSTOM=y``, ``CONFIG_LV_MEMCPY_MEMSET_STD=y``, ``CONFIG_LV_ATTRIBUTE_FAST_MEM_USE_IRAM=y``
    - **LVGL v9**: ``CONFIG_LV_OS_FREERTOS=y``, ``CONFIG_LV_USE_CLIB_MALLOC=y``, ``CONFIG_LV_USE_CLIB_STRING=y``, ``CONFIG_LV_USE_CLIB_SPRINTF=y``, ``CONFIG_LV_DEF_REFR_PERIOD=15``

  - If higher frame rates, better rotation performance, and improved anti-tearing behavior are required, it is recommended to use the `esp_lvgl_adapter component <https://docs.espressif.com/projects/esp-iot-solution/en/latest/display/tools/esp_lvgl_adapter.html>`__.

---------------

Is there any example code for I2S driving I80 LCD with ESP32/ESP32-S2?
----------------------------------------------------------------------------------

  On ESP32 and ESP32-S2, the esp_lcd I80 driver uses the I2S peripheral in LCD mode. Applications can use ``esp_lcd_new_i80_bus()``, available in ESP-IDF v4.4 and later.

  To drive an I80 LCD, please refer directly to the ``i80_controller`` example in :ref:`LCD examples <lcd-examples>`, and `ESP-IDF Programming Guide - I80 LCD <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/lcd/i80_lcd.html>`__.

---------------

What is the recommended upper limit of LCD resolution for ESP series chips? What is the corresponding frame rate?
---------------------------------------------------------------------------------------------------------------------

  The resolution upper limit depends on the interface type and the application's frame-rate requirements. It is recommended to use the maximum resolution that can achieve a smooth frame rate (typically ≥ 30 FPS) as the practical upper limit, rather than pursuing the theoretical hardware limit. For typical resolutions and corresponding frame rates on each platform (based on esp_lvgl_adapter + LVGL v9 Benchmark), please refer to `Selection of LCD Driver Chip <https://docs.espressif.com/projects/esp-techpedia/en/latest/esp-friends/advanced-development/lcd-application-note/overview.html#selection-of-lcd-driver-chip>`__.

  When using the native RGB interface on ESP32-S3, ESP32-S31, or ESP32-P4, configure at most 1024 total lines per frame (``v_res + vsync_pulse_width + vsync_back_porch + vsync_front_porch``).

----------------

How can I enable PSRAM 120M Octal (DDR) on ESP32-S3R8?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP-IDF v5.1 or later versions are required.
  - Enable configuration items through menuconfig: ``IDF_EXPERIMENTAL_FEATURES``, ``SPIRAM_SPEED_120M``, ``SPIRAM_MODE_OCT``.
  - The ESP32-S3-WROOM-1-N16R16V module currently does not support this feature. If enabled, the chip may freeze upon power-up and then reset.
  - **Please note** it is an experimental feature still in testing and may come with the following temperature risks:

    - The chip may not work properly even with ECC enabled when the temperature is above 65°C.
    - Temperature changes may also cause program crashes when accessing PSRAM/flash. For more details, please refer to `SPI Flash and External SPI RAM Configuration <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-guides/flash_psram_config.html#all-supported-modes-and-speeds>`__.

----------------

Does ESP32-S3 require an external PSRAM to use the RGB screen?
------------------------------------------------------------------------------------------------------

  - A full-screen frame buffer often exceeds the available internal SRAM. If the application can supply pixels in time via ``on_bounce_empty``, it can use ``no_fb`` with a nonzero ``bounce_buffer_size_px`` to drive the panel without a full-screen buffer.
  - It's not recommended to use a Quad PSRAM due to its relatively low bandwidth, as this may prevent the RGB LCD PCLK from being set to the required frequency.
  - It's recommended to use an Octal PSRAM and set the clock to 80 MHz or above.

---------------------

How can I increase the upper limit of PCLK settings on ESP32-S3 while ensuring normal RGB screen display?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Typically, the upper limit of PCLK settings is constrained by the bandwidth of the PSRAM. Therefore, you need to enhance the PSRAM bandwidth:

    - Use a higher frequency PSRAM clock or a wider PSRAM bus (Octal).
    - Reduce the PSRAM bandwidth occupied by other peripherals like Wi-Fi, flash, etc.
    - Decrease the Data Cache Line Size to 32 Bytes (set to 64 Bytes when using RGB Bounce Buffer mode).

  - Enable the Bounce Buffer mode of the RGB driver. The larger the buffer, the better the effect. For usage, please refer to the `documentation <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/lcd/rgb_lcd.html>`__. Please note that in this mode, the CPU first moves PSRAM data to SRAM, and then the GDMA transfers data to the RGB peripheral. Therefore, it is necessary to enable ``CONFIG_ESP32S3_DATA_CACHE_LINE_64B=y``. Otherwise, it may cause the screen to drift.
  - Based on limited testing, for Quad PSRAM at 80 MHz, the highest PCLK setting is around 11 MHz; for Octal PSRAM at 80 MHz, the highest PCLK setting is around 22 MHz; for Octal PSRAM at 120 MHz, the highest PCLK setting is around 30 MHz.
  - For applications using LVGL, the task of RGB peripheral initialization can be assigned to the same core as the task of LVGL ``lv_timer_handler()``. This significantly increases the upper limit of PCLK settings.

--------------------

Which image decoding formats are supported by LCD applications on ESP series chips?
--------------------------------------------------------------------------------------------

  - **Software JPEG decoding**: The ESP-IDF example uses the esp_jpeg component, which can use the ROM decoder on supported targets. For an application example, please refer to `esp-idf/examples/peripherals/lcd/tjpgd <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/lcd/tjpgd>`__.
  - **Hardware JPEG decoding**: ESP32-S31 and ESP32-P4 integrate a hardware JPEG codec (``SOC_JPEG_CODEC_SUPPORTED``), and support hardware-accelerated JPEG decoding through the `esp_driver_jpeg <https://docs.espressif.com/projects/esp-idf/en/latest/esp32p4/api-reference/peripherals/jpeg.html>`__ component, which is significantly faster than software decoding.
  - **Via esp_lvgl_adapter + esp_lv_decoder**: It is recommended to use `esp_lvgl_adapter <https://docs.espressif.com/projects/esp-iot-solution/en/latest/display/tools/esp_lvgl_adapter.html>`__ together with `esp_lv_decoder <https://components.espressif.com/components/espressif/esp_lv_decoder>`__, which supports the following formats:

    - Standard formats: JPG, PNG, QOI
    - Sliced formats (optimized for embedded memory): SJPG, SPNG, SQOI
    - Hardware acceleration (supported chips only): JPEG, PJPG

  - **Based on LVGL built-in libraries**: LVGL itself also provides decoding support for PNG, BMP, GIF, and other formats. For details, please refer to `LVGL libs <https://lvgl.io/docs/open/libs>`__.
  - **EAF animation format**: An Espressif custom animation format, originally designed for screen refreshing with the `esp_emote_gfx <https://components.espressif.com/components/espressif2022/esp_emote_gfx>`__ component (segmented decoding), and also adapted to LVGL. Refer to the `LVGL EAF Player Example <https://github.com/espressif/esp-iot-solution/tree/master/examples/display/gui/lvgl_eaf_player>`__.

--------------------------

.. _lcd-rgb-screen-drift:

Why do I get drift (overall drift of the display) when ESP32-S3 is driving an RGB LCD screen?
-----------------------------------------------------------------------------------------------------------

  - **Reasons**

    - The PCLK setting of the RGB peripheral is too high, and the bandwidth of PSRAM or GDMA cannot be satisfied.
    - PSRAM and flash share a set of SPI interfaces. PSRAM is disabled during writes to flash (such as via Wi-Fi, OTA, Bluetooth LE).
    - Reading a large amount of flash/PSRAM data results in insufficient PSRAM bandwidth.

  - **Solutions**

    - Improve PSRAM and flash bandwidth. For example, use a higher frequency or larger bit width under the conditions allowed by the hardware.
    - Enable ``CONFIG_COMPILER_OPTIMIZATION_PERF``.
    - Reduce the Data Cache Line Size to 32 Bytes (set to 64 Bytes when using the RGB Bounce Buffer mode).
    - Enable ``CONFIG_SPIRAM_FETCH_INSTRUCTIONS`` and ``CONFIG_SPIRAM_RODATA``.
    - (Not Recommended) Enable ``CONFIG_LCD_RGB_RESTART_IN_VSYNC`` to automatically recover after screen drifting, but this cannot completely avoid the issue and may reduce the frame rate.

  - **Applications**

    - While ensuring the screen display is normal, try to reduce the frequency of PCLK and decrease the bandwidth utilization of PSRAM.
    - If you need to use Wi-Fi, Bluetooth LE, and continuous flash writing operations, please adopt the XIP on PSRAM + RGB Bounce Buffer method. Here, XIP on PSRAM is used to load the code segment and read-only segment data into PSRAM, and the flash writing operation will not disable PSRAM after it is turned on. RGB Bounce Buffer is used to block the frame buffer data and transfer it from PSRAM to SRAM through the CPU, and then use GDMA to transfer data to the RGB peripheral. Compared with directly using PSRAM GDMA, it can achieve higher transmission bandwidth. The setup steps are as follows:

      - Make sure the ESP-IDF version is release/v5.0 or newer (released after 2022.12.12), as older versions do not support the XIP on PSRAM function. (release/v4.4 supports this function through patching, but it is not recommended)
      - Confirm whether ``CONFIG_SPIRAM_FETCH_INSTRUCTIONS`` and ``CONFIG_SPIRAM_RODATA`` can be enabled in the PSRAM configuration. If the read-only data segment is too large (such as a large number of images), it may cause insufficient PSRAM space. At this time, you can use the file system or make the images into a bin to load into the designated partition.
      - Check if there is any memory (SRAM) left, and it takes about [10 × screen_width × 4] bytes.
      - Set Data cache line size to 64 Bytes (you can set Data cache size to 32 KB to save memory).
      - Set ``CONFIG_FREERTOS_HZ`` to 1000.
      - If all the above conditions are met, you can refer to the `documentation <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/lcd/rgb_lcd.html>`__ to modify the RGB driver to Bounce Buffer mode. If drift still occurs after enabling, you can try to increase the buffer, but this will consume more SRAM memory.
      - If you still have the drift problem when dealing with Wi-Fi, you can try to turn off ``CONFIG_SPIRAM_TRY_ALLOCATE_WIFI_LWIP`` in PSRAM, which takes up much SRAM space.
      - The effects of this setting include higher CPU usage, possible interrupt watchdog reset, and higher memory overhead.
      - Since the Bounce Buffer transfers data from PSRAM to SRAM through the CPU in GDMA interrupts, the program should avoid performing operations that disable interrupts for an extended period (such as calling ``portENTER_CRITICAL()``), as it can still result in screen drifting.

    - For the drift caused by short-term flash operations, such as before and after Wi-Fi connection, you can call ``esp_lcd_rgb_panel_set_pclk()`` before the operation to reduce PCLK (such as 6 MHz), wait for the new clock to take effect at the next VSYNC before performing the flash operation, and then restore PCLK to its original level afterward. This may briefly cause the screen to flash blank.
    - If unavoidable, you can enable ``CONFIG_LCD_RGB_RESTART_IN_VSYNC`` or use the ``esp_lcd_rgb_panel_restart()`` to reset the RGB timing to prevent permanent drifting.
    - For guidance on how to avoid RGB screen drift issues in Arduino, please refer to `the link <https://github.com/esp-arduino-libs/ESP32_Display_Panel/blob/master/docs/envs/use_with_arduino.md#solution-for-screen-drift-issue-when-using-esp32-s3-to-drive-rgb-lcd-in-arduino-ide>`__.

-----------------------------

Why is there vertical dislocation when I drive SPI/8080 LCD screen to display LVGL?
-------------------------------------------------------------------------------------------

  If you use DMA interrupt transfer, the flush-complete callback should be called after the DMA transfer finishes, not immediately after ``draw_bitmap()``.

  - LVGL v8: Call ``lv_disp_flush_ready()`` in the DMA transfer complete interrupt.
  - LVGL v9: Call ``lv_display_flush_ready()`` in the DMA transfer complete interrupt.

---------------------------

When I use ESP32-C3 to drive the LCD display through the SPI interface, is it possible to use RTC_CLK as the SPI clock, so that the LCD display can normally display static pictures in Deep-sleep mode?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Deep-sleep mode: The CPU and most peripherals are powered down, only the RTC memory is operational. For more details, please refer to the "Low Power Management" section in the `ESP32-C3 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf>`__.
  - The SPI of ESP32-C3 only supports two clock sources, APB_CLK and XTAL_CLK, and does not support RTC_CLK. SPI transfers stop during Deep-sleep. For details, please refer to *ESP32-C3 Technical Reference Manual* > *Reset and Clock* [`PDF <https://www.espressif.com/sites/default/files/documentation/esp32-c3_technical_reference_manual_en.pdf#resclk>`__].
  - For the LCD screen driven by the SPI interface, the driver IC generally has built-in GRAM. If the panel stays powered with the display and any required backlight on, static pictures can be displayed normally without the ESP continuously outputting the SPI clock, but the pictures cannot be updated during this period.

-----------------------

Are 9-bit bus and 18-bit color depth supported if I use the ILI9488 LCD screen to test the `screen <https://github.com/espressif/esp-iot-solution/tree/release/v2.0/examples/screen>`__ example?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The ILI9488 driver chip can support 9-bit bus and 18-bit color depth. However, Espressif's driver can only support 8-bit bus and 16-bit color depth for now.

---------------------------

When using ESP32-S3 to drive an RGB screen, why does it halt or reset (TG1WDT_SYS_RST) when running ``esp_lcd_new_rgb_panel()`` or ``esp_lcd_panel_init()``?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Please check if the pins occupied by PSRAM in ESP chips or modules conflict with the RGB pins. If there is a conflict, modify the RGB pin configuration.
  - If using ESP32-S3R8, avoid using GPIO35, GPIO36, and GPIO37 pins.

---------------------------

When using ESP32-S3 to drive an RGB screen, an abnormal color inversion is observed, i.e., black turns into white, and white turns into black. How to handle this?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Please check whether the initialization register of the screen driver IC has set the invert_color function. For example, in ST7789, this can be corrected by configuring the Inversion register:

  - INVOFF (20h): Display Inversion Off
  - INVON (21h): Display Inversion On

---------------------------

How to handle color inaccuracies, such as missing colors, when driving an RGB screen with ESP32-S3?
----------------------------------------------------------------------------------------------------------------------------

  It's likely that the RGB configuration is incorrect. This problem can be troubleshot in the following ways:

  - Display solid red, green, and blue in turn. If red and blue are exchanged but green is correct, check the RGB/BGR color order.
  - On ST7789, bit 3 (``0x08``) of MADCTL (``0x36``) selects the color order. Set this bit for BGR or clear it for RGB, preserving the other bits.
  - For RGB565, check that the byte order of the LVGL pixel buffer matches the transfer format.
  - If colors are missing on the RGB TTL screen display, it is necessary to set R, G, B displays separately, and check whether the channel with waveform and RGB data line design are compliant.

---------------------------

The spaces in the LVGL's label are correctly inputted, for example "Indoor temperature 25.5℃", but the spaces are not displayed on the screen. What could be the reason and how to troubleshoot this?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  This pertains to the missing display of the LVGL label. Enable the following debug items and missing characters will be filled with squares to prevent map loss:

  ``Component config`` → ``LVGL configuration`` → ``Font usage`` → ``Enable drawing placeholders when glyph dsc is not found``

---------------------------

When LVGL v8 continuously loads different images stored on flash, the speed is too slow. For example, how to avoid the slow speed issue when cycling through three images on the home screen?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - If an image is evicted from the cache before it is used again, LVGL must reopen it on the next cycle.
  - For a cycle of three images, set ``LV_IMG_CACHE_DEF_SIZE`` to 3 if memory permits. Allow enough memory for the cached decoder data.

---------------------------

LVGL v8 fails to load PNG, JPEG images from flash. What's the reason for a blank screen?
---------------------------------------------------------------------------------------------------------------------------

  - Check that the decoder for the image format is enabled. For PNG files, the LVGL v8.3 decoder loads the compressed file and decodes it to a 4-byte-per-pixel buffer. LodePNG error 83 indicates an allocation failure.
  - Allow for the compressed input, the decoded pixels, decoder workspace, and any cached images. For JPEG, check the memory requirements of the selected JPEG decoder.

---------------------------

How to convert a GIF animation into C language code?
---------------------------------------------------------------------------------------------------------------------------

  Convert the GIF to Map option, with the Color format set to CF_RAW.

---------------------------

Can the screen be set to transparent when displaying GIF animations?
---------------------------------------------------------------------------------------------------------------------------

  Yes. But GIF only has a 1 bit Alpha descriptor, so it can only be fully transparent or opaque, and there is no semi-transparency.

---------------------------

Which image format is better for the LVGL interface? Is there any reference?
---------------------------------------------------------------------------------------------------------------------------

  You can refer to the table below:

    .. list-table::
      :header-rows: 1

      * - Image format
        - Transparent support
        - Size
        - Decoding speed
      * - PNG
        - Perfectly supported
        - Moderate
        - Moderate
      * - BMP
        - Limited support
        - Large
        - Fastest, no decoding required
      * - JPG
        - Not supported
        - Small
        - Fast

  When converting images to MAP format via `LVGL imageconverter <https://lvgl.io/tools/imageconverter>`__, if using non-RAW formats such as ``CF_TRUE_COLOR`` for conversion, subsequent LVGL loading will not require re-decoding, but it will occupy a larger code segment.

---------------------------

When using some third-party libraries such as FreeType and Lottie with LVGL, why does the screen go blank despite the program loading normally?
-------------------------------------------------------------------------------------------------------------------------------------------------------

  First, consider whether the task stack settings are incorrect:

  - **FreeType**: When using esp_lvgl_adapter, first confirm the stack configuration: for LVGL v8, set ``CONFIG_ESP_MAIN_TASK_STACK_SIZE`` to 32768 (font initialization runs on the calling thread); for LVGL v9, set ``CONFIG_LV_DRAW_THREAD_STACK_SIZE`` to 32768 (font rendering runs on the draw thread). In addition, the following two Kconfig options can reduce resource usage:

    - ``ESP_LVGL_ADAPTER_FREETYPE_SMALL_RENDER_POOL``: Reduces the FreeType render pool from 16 KB to 4 KB, and can also reduce the LVGL v9 draw thread stack requirement.
    - ``ESP_LVGL_ADAPTER_FREETYPE_MINIMAL_BUILD``: Trims FreeType build modules and keeps only what is needed for common TTF/OTF paths (removes Type1/CID/BDF/PCF and other legacy drivers and compressed-stream helpers), which significantly reduces flash usage. Do not enable this if your project needs any of the trimmed formats.

    Reference example: `lvgl_freetype_font <https://github.com/espressif/esp-iot-solution/tree/master/examples/display/gui/lvgl_freetype_font>`__.

  - **Lottie**: Generally, more than 30 KB of task stack needs to be allocated. Refer to `lottie porting <https://docs.lvgl.io/9.1/libs/rlottie.html>`__.

---------------------------

What are some good solutions if the internal RAM of ESP32-S3, driving an SPI screen, is insufficient to allocate space for the entire screen buffer?
----------------------------------------------------------------------------------------------------------------------------------------------------

  Render into a framebuffer in PSRAM. To flush it in chunks, copy pixels into a small DMA-capable SRAM buffer and send each chunk to the display by SPI DMA.

  ESP32-S3 also supports direct SPI DMA from PSRAM. On ESP-IDF versions with this support (for example, v5.5.5), set ``SPI_TRANS_DMA_USE_PSRAM`` on SPI Master transactions or enable ``flags.psram_dma_direct`` in ``esp_lcd_panel_io_spi_config_t``. To avoid a copy, align the buffer address and transfer length as required by the driver. Keep the transfer rate within the PSRAM bandwidth shared with MSPI. See `Transactions with Data on PSRAM <https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/peripherals/spi_master.html#transactions-with-data-on-psram>`__.

  For LVGL, use ``ESP_LV_ADAPTER_DISPLAY_SPI_WITH_PSRAM_DEFAULT_CONFIG`` to configure the SPI display. For panels with a tearing effect signal, see the synchronized refresh options in the `esp_lvgl_adapter 0.7.9 guide <https://components.espressif.com/components/espressif/esp_lvgl_adapter/versions/0.7.9/readme>`__.

---------------------------

How to deal with diagonal tearing on the SPI screen after the hardware is rotated 90 or 270 degrees?
---------------------------------------------------------------------------------------------------------------------------

  It is recommended to enable the LVGL ``sw_rotate`` flag in normal mode and use LVGL software rotation. However, please note that ``sw_rotate`` conflicts with ``full_refresh`` and ``direct_mode``, so do not use them together. For example, calling ``sw_rotate`` under ``full_refresh`` will directly return without any effect.

  .. note::

    ``sw_rotate``, ``full_refresh``, and ``direct_mode`` are **LVGL v8** APIs. Rotation in LVGL v9 works differently; please refer to `LVGL v9 Rotation Notes <https://lvgl.io/docs/open/9.1/API/display/>`__.

---------------------------

Using the ESP32-S2 USB camera and I80 LCD simultaneously may result in the LCD display showing missing images or behaving abnormally. How can this be resolved?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Please refer to `this code <https://github.com/espressif/esp-iot-solution/blob/aefbcb52210e2fbaac7e8a8efcc68645ecd21e7a/components/bus/i2s_lcd_esp32s2_driver.c#L130>`__ to increase the startup delay time of I2S.

---------------------------

How to solve the unexpected crash when operating LVGL controls through non-LVGL tasks?
---------------------------------------------------------------------------------------------------------------------------

  When accessing LVGL widgets from another task, use the same lock as the LVGL task. If you use esp_lvgl_adapter, take and release its lock as shown below.

  .. code-block:: c

    if (esp_lv_adapter_lock(-1) == ESP_OK) {
        /* LVGL API calls */
        esp_lv_adapter_unlock();
    }

---------------------------

Does ESP32-S3 support RGB888?
---------------------------------------------------------------------------------------------------------------------------

  ESP32-S3 supports up to 16 parallel RGB data lines. For an 8-bit serial RGB888 panel, set the following fields in ``esp_lcd_rgb_panel_config_t`` on ESP-IDF v6.x. On ESP-IDF v5.5, use ``.bits_per_pixel = 24`` for the color depth.

  .. code-block:: c

    .data_width = 8,
    .in_color_format = LCD_COLOR_FMT_RGB888,

---------------------------

How can I disable the left and right swipe functionality when operating the LVGL tabview?
---------------------------------------------------------------------------------------------------------------------------

  Please add the following code: ``lv_obj_clear_flag(lv_tabview_get_content(tabview), LV_OBJ_FLAG_SCROLLABLE);``.

---------------------------

Does LVGL support multiple indev inputs?
---------------------------------------------------------------------------------------------------------------------------

  Yes. All input devices are managed in a linked list, supporting multiple input devices of the same and different types. For application examples, please refer to the component `espressif/esp_lvgl_adapter <https://components.espressif.com/components/espressif/esp_lvgl_adapter>`__. The component currently supports input device types such as touch, button, and knob.

---------------------------

Does LVGL support multi-touch?
---------------------------------------------------------------------------------------------------------------------------

  LVGL multi-touch support varies by version:

  - **LVGL v8**: Native multi-touch is not supported; each indev can report only one touch point.
  - **LVGL v9**: Multi-pointer input is supported. Multiple touch indevs can be registered for the same display, and each touch point can control different widgets independently.

  When using `esp_lvgl_adapter <https://docs.espressif.com/projects/esp-iot-solution/en/latest/display/tools/esp_lvgl_adapter.html>`__, you can enable multi-touch mode when registering a touch device (LVGL v9 only):

  .. code-block:: c

    esp_lv_adapter_touch_config_t touch_cfg = ESP_LV_ADAPTER_TOUCH_DEFAULT_CONFIG(disp, touch_handle);
    touch_cfg.multi_touch.mode = ESP_LV_ADAPTER_TOUCH_MODE_MULTI_CONTROL;
    touch_cfg.multi_touch.pointers = 2;  /* Must be >= 2, and not exceed CONFIG_ESP_LCD_TOUCH_MAX_POINTS */
    lv_indev_t *touch = esp_lv_adapter_register_touch(&touch_cfg);

---------------------------

Does a high CPU usage rate reported by LVGL have any impact?
---------------------------------------------------------------------------------------------------------------------------

  LVGL v8 measures time spent in its timer handler over roughly 500 ms. LVGL v9.4 derives CPU usage from ``LV_SYSMON_GET_IDLE()``. Use FreeRTOS's `vTaskGetRunTimeStats <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/freertos_idf.html#_CPPv420vTaskGetRunTimeStatsPc>`__ to inspect per-task CPU time.

---------------------------

Can ESP32-S3 enter Light-sleep mode after enabling the RGB screen driver?
---------------------------------------------------------------------------------------------------------------------------

  **Using the esp_lcd RGB driver directly**: When initializing the RGB interface, if ``CONFIG_PM_ENABLE`` is enabled, the driver automatically holds the ``ESP_PM_NO_LIGHT_SLEEP`` lock, preventing automatic Light-sleep. To release this lock, you must first call ``esp_lcd_panel_del()`` to delete the RGB panel, then reinitialize after waking from sleep.

  **Using the** `esp_lvgl_adapter component <https://docs.espressif.com/projects/esp-iot-solution/en/latest/display/tools/esp_lvgl_adapter.html>`__: This component provides two Light-sleep usage modes. The LVGL UI state (widget tree) is retained during sleep, so the UI does not need to be rebuilt.

  **Manual sleep**: The application controls the full sleep/wake flow:

    #. Before entering sleep, call ``esp_lv_adapter_sleep_prepare()`` to pause the adapter and wait for the current frame refresh to complete.
    #. Call ``esp_lcd_panel_del()`` to release display hardware resources.
    #. Call ``esp_light_sleep_start()`` to enter Light-sleep.
    #. After waking, reinitialize the LCD hardware, then call ``esp_lv_adapter_sleep_recover()`` to rebind the panel and resume the adapter.

  **Automatic sleep (auto_sleep)**: Configure an idle timeout at initialization. The adapter enters the configured sleep mode after LVGL has been idle longer than the specified time:

  .. code-block:: c

    esp_lv_adapter_config_t cfg = ESP_LV_ADAPTER_DEFAULT_CONFIG();
    cfg.auto_sleep.enable = true;
    cfg.auto_sleep.idle_timeout_ms = 5000;  /* Auto-sleep after 5 s of idle */

    /* PAUSE stops the LVGL worker and releases the adapter's own lock.
       An active RGB panel still holds its lock and prevents automatic Light-sleep. */
    cfg.auto_sleep.mode = ESP_LV_ADAPTER_AUTO_SLEEP_MODE_PAUSE;
    cfg.auto_sleep.callbacks.on_enter_sleep = panel_sleep_cb;
    cfg.auto_sleep.callbacks.on_exit_sleep  = panel_wake_cb;

    /* User mode: the on_enter_sleep callback owns the full
       sleep_prepare → LCD deinit → light_sleep_start → LCD init → sleep_recover flow */
    /* cfg.auto_sleep.mode = ESP_LV_ADAPTER_AUTO_SLEEP_MODE_USER; */

    ESP_ERROR_CHECK(esp_lv_adapter_init(&cfg));

  In Pause mode, registered touch/button/knob inputs automatically notify the adapter to wake; custom wake sources can call ``esp_lv_adapter_request_wake()`` or ``esp_lv_adapter_request_wake_from_isr()``.

---------------------------

Is it supported to drive segment LCD screens?
-------------------------------------------------------------------------------

  ESP chips can't directly drive the segment LCD screen through the GPIO pin, because this function requires cycling between high and low voltage levels, with an AC voltage from 2.7 V to 5.0 V and typical values of 3.0 V, 3.3 V, 4.5 V, and 5.0 V. However, the chips do not support voltage range adjustment.

---------------------------

When driving an RGB LCD with ESP32-P4, the screen shows abnormal colors. How to troubleshoot?
-------------------------------------------------------------------------------------------------------------

  ESP32-P4 has multiple VDDPST power domains. Each VDDPST controls the maximum output level of GPIOs in the corresponding region (for the GPIO-to-VDDPST mapping, please refer to the `ESP32-P4 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32-p4_datasheet_en.pdf>`__). If the corresponding VDDPST supply is insufficient or not configured correctly, some GPIOs may have a maximum output level of 1.8 V, causing insufficient RGB interface signal levels and abnormal screen colors. Please check that the VDDPST for the GPIOs used by the RGB interface is configured to the correct voltage (typically 3.3 V).

  The 30 MHz PCLK mentioned above was measured on ESP32-S3 with 120 MHz Octal PSRAM. The achievable PCLK depends on the chip and available memory bandwidth.

---------------------------

Does ESP32-P4 support HDMI signal output?
-------------------------------------------------------------------------------

  ESP32-P4 does not support direct HDMI signal output. However, HDMI signal output can be achieved through an MIPI-DSI to HDMI bridge chip. Espressif supports `LT8912B <https://github.com/espressif/esp-bsp/tree/master/components/lcd/esp_lcd_lt8912b>`__. For more information, refer to `example code <https://github.com/espressif/esp-iot-solution/tree/master/examples/display/lcd/hdmi_video_renderer>`__. See also the `LT9611 example <https://github.com/espressif/esp-idf/tree/v6.1.1/examples/peripherals/lcd/dsi_hdmi_bridge>`__.

---------------------------

In LVGL applications, how to rotate the RGB or MIPI-DSI interface screen by 90 degrees/270 degrees? How to avoid tearing? How to further improve the frame rate?
----------------------------------------------------------------------------------------------------------------------------------------------------------------

  - It is recommended to use the `esp_lvgl_adapter component <https://docs.espressif.com/projects/esp-iot-solution/en/latest/display/tools/esp_lvgl_adapter.html>`__. This component provides features such as high-efficiency rotation, tear prevention, frame rate enhancement, and supports LVGL v8 and v9 versions.
  - Refer to the example code `esp_lvgl_adapter example <https://github.com/espressif/esp-iot-solution/tree/master/examples/display/gui/lvgl_common_demo>`__.

--------------

.. _can-esp32-p4-generate-mipi-dsi-signals-lp-and-hp-when-no-mipi-peripheral-is-connected:

Can ESP32-P4 generate MIPI-DSI signals (LP and HS) when no MIPI peripheral is connected?
----------------------------------------------------------------------------------------

  The host can transmit LP (low-power) and HS (high-speed) signals. With no receiver, video transmission can stall when the host requests a frame acknowledgement. In ESP-IDF v6.1.1, set ``flags.disable_frame_ack`` in ``esp_lcd_dpi_panel_config_t`` to disable that request when probing the output.

--------------

GIF animations in EAF format play slowly on ESP32-S3/ESP32-P4. How to optimize?
------------------------------------------------------------------------------------

  - You can change the EAF encoding format to JPEG (set in the conversion tool), which will increase file size but decode faster;
  - For larger resolution screens (such as 466 × 466), LVGL rendering burden is heavy;
  - Compared with EAF + LVGL, using the `esp_emote_gfx <https://components.espressif.com/components/espressif2022/esp_emote_gfx>`__ component directly for screen refreshing (segmented decoding) is more efficient. EAF was originally designed for esp_emote_gfx, and is only additionally adapted to LVGL;
  - For video playback, try an AVI file with JPEG-encoded frames and compare playback at the same resolution.

---------------------------

ESP32-P4 drives a MIPI-DSI LCD with no image and no other error logs. How to troubleshoot?
----------------------------------------------------------------------------------------------------------------

  First check the 2.5 V D-PHY supply, panel reset and initialization sequence, and the wiring of the clock pair and all configured data lanes. Use a DSI test pattern to check the link.

  If the driver reports a framebuffer underrun, check the PSRAM bandwidth available at the configured pixel clock and framebuffer color depth. The ESP-IDF example uses ``CONFIG_SPIRAM_SPEED_200M=y``.

---------------------------

ESP32-P4 drives a MIPI-DSI LCD with twisted or misaligned images. How to handle this?
----------------------------------------------------------------------------------------------------------------

  This issue is generally caused by a mismatch between ``lane_bit_rate_mbps`` and the actual ``pixel_clock``, or between ``lane_bit_rate_mbps`` and the rate required by the panel. Recalculate ``lane_bit_rate_mbps`` based on resolution, refresh rate, color depth, and lane count (with about a 20% margin). For the calculation method, please refer to `MIPI DSI LCD Detailed Guide <https://docs.espressif.com/projects/esp-iot-solution/en/latest/display/lcd/mipi_dsi_lcd.html>`__. Note that on ESP32-P4, ``lane_bit_rate_mbps`` must not exceed 1500, and a minimum of 480 is recommended.

---------------------------

ESP32-P4 drives a MIPI-DSI LCD with a flashing blue screen and the message "can't fetch data from external memory fast enough, underrun happens". How to handle this?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  This issue is caused by insufficient PSRAM bandwidth. You can try the following:

  - Lower ``lane_bit_rate_mbps`` and ``dpi_clock_freq_mhz`` (pixel clock frequency).
  - If using the RGB888 color format, consider switching to RGB565 to reduce bandwidth demand.
  - Enable the following configuration items to improve PSRAM bandwidth:

    - ``CONFIG_SPIRAM_XIP_FROM_PSRAM=y``
    - ``CONFIG_CACHE_L2_CACHE_256KB=y``
    - ``CONFIG_CACHE_L2_CACHE_LINE_128B=y``
    - ``CONFIG_COMPILER_OPTIMIZATION_PERF=y``
