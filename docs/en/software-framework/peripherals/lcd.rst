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

  - ESP's LCD drivers are located in `components/esp_lcd <https://github.com/espressif/esp-idf/tree/master/components/esp_lcd>`__ within **ESP-IDF**. **esp_lcd** can drive screens with multiple interfaces supported by ESP series chips, including **I2C**, **SPI(QSPI)**, **8080**, and **RGB**. The interface types supported by each chip series are as follows:

    .. list-table::
        :header-rows: 1

        * - SoCs 
          - I2C
          - SPI (QSPI)
          - I80
          - RGB

        * - ESP32
          - Yes
          - Yes
          - Yes
          - No      
  
        * - ESP32-S2
          - Yes
          - Yes
          - Yes
          - No

        * - ESP32-S3
          - Yes
          - Yes
          - Yes
          - Yes

        * - ESP32-C3
          - Yes
          - Yes
          - No
          - No

        * - ESP32-C6
          - Yes
          - Yes
          - No
          - No

  - The LCD examples can be found in **ESP-IDF** at `examples/peripherals/lcd <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/lcd>`__ and in **esp-iot-solution** at `examples/display/lcd <https://github.com/espressif/esp-iot-solution/tree/master/examples/display/lcd>`__.
  - It's recommended to develop applications based on ESP-IDF **release/v5.1** or higher versions, as lower versions do not support some important new features, especially for the RGB interface.
  - **Do not use** the screen `driver <https://github.com/espressif/esp-iot-solution/tree/master/components/display/screen>`__ and `examples <https://github.com/espressif/esp-iot-solution/tree/master/examples/screen>`__ in esp-iot-solution.

---------------

Which adapted ICs can be used by the LCD screen of ESP32 series chips?
-------------------------------------------------------------------------------------------------

  Currently, the adapted ICs for the `esp_lcd`-based LCD driver include:

  - `ESP-IDF <https://github.com/espressif/esp-idf/blob/master/components/esp_lcd/include/esp_lcd_panel_vendor.h>`__：st7789, nt35510, ssd1306.
  - `ESP Registry <https://components.espressif.com/components?q=esp_lcd>`__：gc9a01, ili9341, ili9488, ra8875, sh1107, st7796, st7701, gc9503, gc9b71, spd2010, ... (continuously updated)

  **Please note that even if driver ICs are same, different screens vary in register configuration parameters. In addition, screen manufacturers generally provide matched configuration parameters (code). Thus, it is recommended to use the above two methods to obtain code of similar driver ICs, and to update the code based on the parameters of your own screen.**

  Currently, the adapted ICs of `esp_lcd_touch` based touch driver include:

  - `ESP Registry <https://components.espressif.com/components?q=esp_lcd>`__: FT5x06, GT1151, GT911, STMPE610, TT21100, XPT2046, CST816, ... (continuously updated).

--------------

Do ESP series development boards with screens support GUI development using the Arduino IDE?
-----------------------------------------------------------------------------------------------------------------

  - Currently, the official LCD driver library for Arduino development, `ESP32_Display_Panel <https://github.com/esp-arduino-libs/ESP32_Display_Panel>`__, has been released. It can be downloaded directly in the Arduino IDE. For supported development boards, please refer to the `documentation <https://github.com/esp-arduino-libs/ESP32_Display_Panel#espressif-development-boards>`__.
  - Several points to note:

    - ESP32_Display_Panel relies on `arduino-esp32 <https://github.com/espressif/arduino-esp32>`__.
    - The RGB interface of ESP32-S3 exhibits the :ref:`screen drift issue <lcd-rgb-screen-drift>`, an issue that can be solved by features available in ESP-IDF release/v5.1 and later versions. However, arduino-esp32 (v2.x.x) is based on ESP-IDF version v4.4.x and thus unable to resolve this issue. Fortunately, the upcoming arduino-esp32 (v3.x.x) will use ESP-IDF v5.1.
    - Given that Arduino cannot adjust various parameter configurations, such as compile optimization levels, through menuconfig like ESP-IDF, it is recommended to develop a GUI based on ESP-IDF to achieve optimal performance.

--------------

How can I improve the display frame rate of LCD screens?
----------------------------------------------------------

  - The actual display frame rate of LCD screens is determined by the "interface frame rate" and "rendering frame rate". Generally, the "interface frame rate" is much bigger than the "rendering frame rate". So this question actually is "how can I improve the rendering frame rate of the LCD".

  - Taking ESP32-S3R8 as an example, the following ESP configuration items can improve the frame rate (ESP-IDF release/v5.1):

    - ``CONFIG_FREERTOS_HZ=1000``
    - ``CONFIG_ESP_DEFAULT_CPU_FREQ_MHZ_240=y``
    - ``CONFIG_ESPTOOLPY_FLASHMODE_QIO=y``
    - ``CONFIG_ESPTOOLPY_FLASHFREQ_120M=y`` [should be consistent with PSRAM]
    - ``CONFIG_SPIRAM_MODE_OCT=y``
    - ``CONFIG_IDF_EXPERIMENTAL_FEATURES=y`` and ``CONFIG_SPIRAM_SPEED_120M=y`` [should be consistent with FLASH]
    - ``CONFIG_SPIRAM_FETCH_INSTRUCTIONS=y``
    - ``CONFIG_SPIRAM_RODATA=y``
    - ``CONFIG_ESP32S3_DATA_CACHE_LINE_64B=y``
    - ``CONFIG_COMPILER_OPTIMIZATION_PERF=y``

  - The following LVGL configuration items can improve the frame rate (LVGL v8.3):

    - ``#define LV_MEM_CUSTOM 1`` or ``CONFIG_LV_MEM_CUSTOM=y``
    - ``#define LV_MEMCPY_MEMSET_STD 1`` or ``CONFIG_LV_MEMCPY_MEMSET_STD=y``
    - ``#define LV_ATTRIBUTE_FAST_MEM IRAM_ATTR`` or ``CONFIG_LV_ATTRIBUTE_FAST_MEM=y``

  - For LCD and LVGL performance, please refer to `documentation <https://github.com/espressif/esp-bsp/blob/master/components/esp_lvgl_port/docs/performance.md#lcd--lvgl-performance>`__.

---------------

Is there any example code for I2S driving LCD with ESP32?
-------------------------------------------------------------------------------------

  - The interface type of the screen driven by I2S in ESP32/ESP32-S2 is i80(8080)
  - For the application examples, please refer to :ref:`LCD examples <lcd-examples>`.

---------------

What is the maximum resolution supported by ESP LCD? What is the corresponding frame rate?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - For the RGB peripheral interface of ESP32-S3, due to its hardware limitations, it theoretically supports a maximum resolution of 4096 x 1024 (maximum 4096 in the horizontal direction and 1024 in the vertical direction). As for other peripheral interfaces on ESP series chips, there isn't a specific "maximum" hardware limitation on the supported resolution.
  - Because chip storage, computing performance, and peripheral interface bandwidth are limited, and different types of LCDs usually have specific resolution ranges, it is recommended to use the following resolutions for ESP32-C3 and ESP32-S3 chips:

    .. list-table::
        :header-rows: 1

        * - SoCs
          - SPI
          - QSPI
          - I80
          - RGB

        * - ESP32-C3
          - 240 x 240
          - Not_recommended
          - Not_supported
          - Not_supported

        * - ESP32-S3
          - 320 x 240
          - 400 x 400
          - 480 x 320
          - 480 x 480, 800 x 480  

  - For the RGB interface of ESP32-S3, the maximum tested resolution is 800 x 480 currently, and the interface frame rate is limited to 59 (PCLK is 30 MHz). The corresponding average LVGL frame rate is 23. The upper limit of the average LVGL frame rate is 26, corresponding to an interface frame rate of 41 (PCLK is 21 MHz).

----------------

How can I enable PSRAM 120M Octal (DDR) on ESP32-S3R8?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP-IDF v5.1 or later versions are required.
  - Enable the configuration options through menuconfig: IDF_EXPERIMENTAL_FEATURES, SPIRAM_SPEED_120M, SPIRAM_MODE_OCT.
  - **Please note** it is an experimental feature still in testing and may come with the following temperature risks:

    - The chip may not work properly even with ECC enabled when the temperature is above 65°C.
    - Temperature changes may also cause program crashes when accessing PSRAM/flash. For more details, please refer to `SPI Flash and External SPI RAM Configuration <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-guides/flash_psram_config.html#all-supported-modes-and-speeds>`__.

----------------

What models of display touch panels are supported for testing the `LVGL <https://github.com/espressif/esp-iot-solution/tree/master/examples/hmi/lvgl_example>`__ example on ESP32-S3?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The driver and examples in esp-iot-solution are not recommended. For details, please refer to :ref:`lcd-examples`.

---------------

Does ESP32-S3 require an external PSRAM to use the RGB screen?
------------------------------------------------------------------------------------------------------

- In general, yes. RGB screens require the ESP to provide at least one full-screen-sized frame buffer. However, the resolution of RGB screens is usually large, and ESP32-S3's SRAM might not meet this requirement.
- It's not recommended to use a Quad PSRAM due to its relatively low bandwidth, as this could make the PCLK of the RGB LCD cannot be set to the required frequency.
- It's recommended to use an Octal PSRAM and set the clock to 80 MHz or above.

---------------------

How can I increase the upper limit of PCLK settings on ESP32-S3 while ensuring normal RGB screen display?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

- Typically, the upper limit of PCLK settings is constrained by the bandwidth of the PSRAM. Therefore, you need to enhance the PSRAM bandwidth:

  - Use a higher frequency PSRAM clock or a wider PSRAM bus (Octal).
  - Reduce the PSRAM bandwidth occupied by other peripherals like Wi-Fi, flash, etc.
  - Decrease the Data Cache Line Size to 32 Bytes (set to 64 Bytes when using RGB Bounce Buffer mode).

- Enable the Bounce Buffer mode for RGB display, and a larger buffer size provides better performance. For usage, please refer to `documentation <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/lcd.html#bounce-buffer-with-single-psram-frame-buffer>`__. Note that in this mode, PSRAM data is first moved to SRAM by the CPU and then transferred to the RGB peripheral via GDMA. Therefore, you need to enable `CONFIG_ESP32S3_DATA_CACHE_LINE_64B=y` simultaneously, or it may lead to screen drifting.
- Based on limited testing, for Quad PSRAM at 80 MHz, the highest PCLK setting is around 11 MHz; for Octal PSRAM at 80 MHz, the highest PCLK setting is around 22 MHz; for Octal PSRAM at 120 MHz, the highest PCLK setting is around 30 MHz.

--------------------

Which image decoding formats are supported by the ESP32-S3 series of chips?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Currently, ESP-IDF only supports the JPEG decoding format. For an application example, please refer to `esp-idf/examples/peripherals/lcd/tjpgd <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/lcd/tjpgd>`_.
  - If you develop based on LVGL, PNG, BMP, SJPG and GIF decoding formats are supported. For details, please refer to `LVGL libs <https://docs.lvgl.io/master/libs/index.html>`_.

--------------------------

.. _lcd-rgb-screen-drift:

Why do I get drift (overall drift of the display) when ESP32-S3 is driving an RGB LCD screen?
-----------------------------------------------------------------------------------------------------------

  - **Reasons**

    - PCLK is set to a too big number, and the PSRAM bandwidth is not applicable.
    - PSRAM is disabled due to the write operation of flash (like Wi-Fi, BLE, OTA).

  - **Solutions**

    - Improve bandwidths of PSRAM and flash. You can set flash to QIO 120 M and set PSRAM to Octal 120 M.
    - Enable ``CONFIG_COMPILER_OPTIMIZATION_PERF``.
    - Reduce the Data Cache Line Size to 32 Bytes (set to 64 Bytes when using the RGB ``Bounce Buffer`` mode).
    - Enable ``CONFIG_SPIRAM_FETCH_INSTRUCTIONS`` and ``CONFIG_SPIRAM_RODATA``.
    - (Not Recommended) Enable ``CONFIG_LCD_RGB_RESTART_IN_VSYNC`` to automatically recover after screen drifting, but this cannot completely avoid the issue and may reduce the frame rate.

  - **Applications**

    - While ensuring the screen display is normal, try to reduce the frequency of PCLK and decrease the bandwidth utilization of PSRAM.
    - If you need to use Wi-Fi, BLE and continuous write operation to flash, please use ``XIP on PSRAM + RGB Bounce buffer`` method, and the settings are as follows:

      - Make sure the ESP-IDF version is release/v5.0 or newer (released after 2022.12.12), as older versions do not support the ``XIP on PSRAM`` function. (release/v4.4 supports this function through patching, but it is not recommended)
      - Verify that whether ``CONFIG_SPIRAM_FETCH_INSTRUCTIONS`` and ``CONFIG_SPIRAM_RODATA`` can be enabled in the PSRAM configuration (too large rodata segment will cause insufficient space in the PSRAM).
      - Check if there is any memory (SRAM) left, and it takes about [10 * screen_width * 4] bytes.
      - Set ``Data cache line size`` to 64 Bytes (you can set ``Data cache size`` to 32 KB to save memory).
      - Set ``CONFIG_FREERTOS_HZ`` to 1000。
      - If all the above conditions are met, then you can refer to `Documentation <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/lcd.html#bounce-buffer-with-single-psram-frame-buffer>`__ to modify the RGB driver to ``Bounce buffer`` mode.
      - If you still have the drift problem when dealing with Wi-Fi, you can try to turn off ``CONFIG_SPIRAM_TRY_ALLOCATE_WIFI_LWIP`` in PSRAM, which takes up much SRAM space.
      - The effects of this setting include higher CPU usage, possible interrupt watchdog reset, and higher memory overhead.
      - Since the Bounce Buffer transfers data from PSRAM to SRAM through the CPU in GDMA interrupts, the program should avoid performing operations that disable interrupts for an extended period (such as calling ``portENTER_CRITICAL()``), as it can still result in screen drifting.

    - For the drift caused by short-term operations of flash, such as before and after Wi-Fi connection, you can call ``esp_lcd_rgb_panel_set_pclk()`` before the operation to reduce the PCLK (such as 6 MHz) and delay about 20 ms (the time for RGB to complete one frame), and then increase PCLK to the original level after the operation. This operation may cause the screen to flash blank in a short-term.
    - Enable ``flags.refresh_on_demand`` in ``esp_lcd_rgb_panel_config_t``, and manually refresh the screen by calling the ``esp_lcd_rgb_panel_refresh()`` interface. In addition, you need to reduce the refreshing frequency as much as possible while ensuring that the screen does not flash blank.
    - If unavoidable, you can enable ``CONFIG_LCD_RGB_RESTART_IN_VSYNC`` or use the ``esp_lcd_rgb_panel_restart()`` to reset the RGB timing to prevent permanent drifting.

-----------------------------

Why is there vertical dislocation when I drive SPI/8080 LCD screen to display LVGL?
---------------------------------------------------------------------------------------------

  If you use DMA interrupt to transfer data, ``lv_disp_flush_ready()`` of LVGL should be called after DMA transfer instead of immediately after calling ``draw_bitmap()``.

---------------------------

When I use ESP32-C3 to drive the LCD display through the SPI interface, is it possible to use RTC_CLK as the SPI clock, so that the LCD display can normally display static pictures in Deep-sleep mode?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Deep-sleep mode: CPU and most peripherals are powered down, and only the RTC memory is active. For details, please refer to "Low Power Management" in `ESP32-C3 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf>`__.
  - The SPI of ESP32-C3 only supports two clock sources, APB_CLK and XTAL_CLK, and does not support RTC_CLK. Therefore, the LCD screen cannot display static pictures in Deep-sleep mode. For details, please refer to *ESP32-C3 Technical Reference Manual* > *Reset and Clock* [`PDF <https://www.espressif.com/sites/default/files/documentation/esp32-c3_technical_reference_manual_en.pdf#resclk>`__].
  - For the LCD screen driven by the SPI interface, the driver IC generally has built-in GRAM. Thus, the static pictures can be displayed normally without the ESP continuously outputting the SPI clock, but the pictures cannot be updated during this period.

-----------------------

Are 9-bit bus and 18-bit color depth supported if I use the ILI9488 LCD screen to test the `screen <https://github.com/espressif/esp-iot-solution/tree/master/examples/screen>`__ example?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The ILI9488 driver chip can support 9-bit bus and 18-bit color depth. However, Espressif's driver can only support 8-bit bus and 16-bit color depth for now.

---------------------------

When using ESP32-S3 to drive an RGB screen, why does it halt or reset (TG1WDT_SYS_RST) when running ``esp_lcd_new_rgb_panel()`` or ``esp_lcd_panel_init()``?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Please check if the pins occupied by PSRAM in ESP chips or modules conflict with the RGB pins. If there is a conflict, modify the RGB pin configuration.
  - If using ESP32-S3R8, avoid using GPIO35, GPIO36, and GPIO37 pins.
