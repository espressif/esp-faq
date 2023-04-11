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

Where are the LCD drivers and reference examples for ESP32 series chips?
--------------------------------------------------------------------------------------------------------------------------------------

   - You can find ESP's LCD driver in `components/esp_lcd <https://github.com/espressif/esp-idf/tree/master/components/esp_lcd>`__ in **ESP-IDF**. However, this document is only available in * *release/v4.4 and newer** versions. **esp_lcd** can drive LCD screens with four interfaces (**I2C**, **SPI**, **8080**, and **RGB**) supported by ESP series chips. For the LCD interfaces supported by ESP32 series chips, see `ESP32 series chip screen interface <https://docs.espressif.com/projects/espressif-esp-iot-solution/en/latest/display/screen.html#esp32>`__.
   - For the application examples of the LCD driver of each interface, please refer to `examples/peripherals/lcd <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/lcd>`__ in ESP-IDF. Currently, these examples are only available in **release/v5.0** and newer versions. As the API names of esp_lcd in **release/v4.4** are basically same as those of higher versions, you can also refer to the above examples (please note the API implementations are a little different).
   - **NOT RECOMMENDED** Use the LCD driver and examples in esp-iot-solution.
   - ESP-IDF **release/v5.0** is recommended for RGB LCD applications as some features are not supported in release/v4.4.

---------------

Which adapted ICs can be used by the LCD screen of ESP32 series chips?
-------------------------------------------------------------------------------------------------

  Currently, the adapted ICs for the `esp_lcd`-based LCD driver include:

  - `esp_lcd <https://github.com/espressif/esp-idf/blob/7f4bcc36959b1c483897d643036f847eb08d270e/components/esp_lcd/include/esp_lcd_panel_vendor.h>`__ : st7789, nt35510, ssd1306
  - `Package Manager <https://components.espressif.com/>`__ : gc9a01, ili9341, ili9488, ra8875, sh1107 (continuously updated)

  **Please note that even if driver ICs are same, different screens vary in register configuration parameters. In addition, screen manufacturers generally provide matched configuration parameters (code). Thus, it is recommended to use the above two methods to obtain code of similar driver ICs, and to update the code based on the parameters of your own screen.**

  Currently, the adapted ICs of `esp_lcd_touch` based touch driver include:

  - `Package Manager <https://components.espressif.com/>`__: FT5x06, GT1151, GT911, STMPE610, TT21100, XPT2046 (continuously updated).

--------------

How can I improve the display frame rate of LCD screens?
----------------------------------------------------------

   - The actual display frame rate of LCD screens is determined by the "interface frame rate" and "rendering frame rate". Generally, the "interface frame rate" is much bigger than the "rendering frame rate". So this question actually is "how can I improve the rendering frame rate of the LCD".

   - The following ESP configuration items can improve the frame rate (ESP-IDF release/v5.0):

     - CONFIG_FREERTOS_HZ=1000
     - CONFIG_ESP_DEFAULT_CPU_FREQ_MHZ_240=y
     - CONFIG_ESPTOOLPY_FLASHMODE_QIO=y
     - CONFIG_ESPTOOLPY_FLASHFREQ_120M=y [needs to be consistent with PSRAM]
     - CONFIG_SPIRAM_MODE_OCT=y
     - CONFIG_SPIRAM_SPEED_120M=y [Need to be consistent with FLASH]
     - CONFIG_SPIRAM_FETCH_INSTRUCTIONS=y
     - CONFIG_SPIRAM_RODATA=y
     - CONFIG_ESP32S3_DATA_CACHE_LINE_64B=y
     - CONFIG_COMPILER_OPTIMIZATION_PERF=y

   - The following LVGL configuration items can improve the frame rate (LVGL v8.3):

     - #define LV_MEM_CUSTOM 1
     - #define LV_MEMCPY_MEMSET_STD 1
     - #define LV_ATTRIBUTE_FAST_MEM IRAM_ATTR

---------------

Is there any example code for I2S driving LCD with ESP32?
-------------------------------------------------------------------------------------

  - The interface type of the screen driven by I2S in ESP32/ESP32-S2 is i80(8080)
  - For the application examples, please refer to :ref:`LCD examples <lcd-examples>`.

---------------

What is the maximum resolution supported by ESP32 LCD? What is the corresponding frame rate?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Over the RGB interface, the ESP32 LCD can support up to 800 × 480 of resolution. The upper limit of the interface frame rate is 59 (PCLK 30 MHz), and the average frame rate of LVGL is about 23. The average upper limit of the frame rate of LVGL is 26, and the corresponding interface frame rate is 41 (PCLK 21 MHz).

----------------

What models of display touch panels are supported for testing the `LVGL <https://github.com/espressif/esp-iot-solution/tree/master/examples/hmi/lvgl_example>`_ example on ESP32-S3?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The driver and examples in esp-iot-solution are not recommended. For details, please refer to :ref:`lcd-examples`.

---------------

Does ESP32-S3 require an external PSRAM to use the RGB screen?
------------------------------------------------------------------------------------------------------

  Yes, and it must be an Octal PSRAM at least and the clock must be set to 80 MHz or above. Otherwise, the PCLK of RGB LCD cannot be set to a higher PCLK frequency and the frame rate will be too low.

--------------------

Which image decoding formats are supported by the ESP32-S3 series of chips?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Currently, ESP-IDF only supports the JPEG decoding format. For an application example, please refer to `esp-idf/examples/peripherals/lcd/tjpgd <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/lcd/tjpgd>`_.
  - If you develop based on LVGL, PNG, BMP, SJPG and GIF decoding formats are supported. For details, please refer to `LVGL libs <https://docs.lvgl.io/master/libs/index.html>`_.

--------------------------

Why do I get drift (overall drift of the display) when driving an RGB LCD screen?
-------------------------------------------------------------------------------------------------------

  - **Reasons**

    - PCLK is set to a too big number, and the PSRAM bandwidth is not applicable.
    - PSRAM is disabled due to the write operation of flash.

  - **Solutions**

    - Improve bandwidths of PSRAM and flash. You can set flash to QIO 120 M and set PSRAM to Octal 120 M.
    - Enable `CONFIG_COMPILER_OPTIMIZATION_PERF`.
    - Reduce data_cache_line_size to 32 bytes.
    - Enable `CONFIG_SPIRAM_FETCH_INSTRUCTIONS` and `CONFIG_SPIRAM_RODATA`.
    - Enable `CONFIG_LCD_RGB_RESTART_IN_VSYNC`. But this operation may cause the screen to flash blurred and drop the frame rate, so we generally do not recommend this way. However, you can try it if you have interests.

  - **Applications**

    - If you need to use Wi-Fi and continuous write operation to flash, please use `XIP PSRAM + RGB Bounce buffer` method, and the settings are as follows:
      - Make sure the ESP-IDF version is (> 2022.12.12) release/v5.0 and above (released after 2022.12.12), as older versions do not support the `XIP PSRAM` function.
      - Verify that whether `SPIRAM_FETCH_INSTRUCTIONS` and `SPIRAM_RODATA` can be enabled in the PSRAM configuration (too large rodata segment will cause insufficient space in the PSRAM).
      - Check if there is any memory (SRAM) left, and it takes about [10 * screen_width * 4] bytes.
      - Set `Data cache line size` to 64 Bytes (you can set `Data cache size` to 32 KB to save memory).
      - If all the above conditions are met, then you can refer to `Documentation <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/lcd.html#bounce-buffer-with-single-psram-frame-buffer>`_ to modify the RGB driver to `Bounce buffer` mode.
      - If you still have the drift problem when dealing with Wi-Fi, you can try to turn off CONFIG_SPIRAM_TRY_ALLOCATE_WIFI_LWIP in PSRAM, which takes up much SRAM space.
      - The effects of this setting include higher CPU usage, possible interrupt watchdog reset, and higher memory overhead.
    - For the drift caused by short-term operations of flash, such as before and after Wi-Fi connection, you can call `esp_lcd_rgb_panel_set_pclk()` before the operation to reduce the PCLK (such as 6 MHz) and delay about 20 ms (the time for RGB to complete one frame), and then increase PCLK to the original level after the operation. This operation may cause the screen to flash blank in a short-term.
    - Enable `flags.refresh_on_demand` in `esp_lcd_rgb_panel_config_t`, and manually refresh the screen by calling the `esp_lcd_rgb_panel_refresh()` interface. In addition, you need to reduce the refreshing frequency as much as possible while ensuring that the screen does not flash blank.
    - If unavoidable, you can call the `esp_lcd_rgb_panel_restart()` interface to reset the RGB timing to prevent permanent drift.

-----------------------------

Why is there vertical dislocation when I drive SPI/8080 LCD screen to display LVGL?
---------------------------------------------------------------------------------------------

  If you use DMA interrupt to transfer data, ``lv_disp_flush_ready`` of LVGL should be called after DMA transfer instead of immediately after calling ``draw_bitmap``. 

---------------------------

When I use ESP32-C3 to drive the LCD display through the SPI interface, is it possible to use RTC_CLK as the SPI clock, so that the LCD display can normally display static pictures in Deep-sleep mode?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

   - Deep-sleep mode: CPU and most peripherals are powered down, and only the RTC memory is active. For details, please refer to "Low Power Management" in `ESP32-C3 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf>`__.
   - The SPI of ESP32-C3 only supports two clock sources, APB_CLK and XTAL_CLK, and does not support RTC_CLK. Therefore, the LCD screen cannot display static pictures in Deep-sleep mode. For details, please refer to *ESP32-C3 Technical Reference Manual* > *Reset and Clock* [`PDF <https://www.espressif.com/sites/default/files/documentation/esp32-c3_technical_reference_manual_en.pdf#resclk>`__].
   - For the LCD screen driven by the SPI interface, the driver IC generally has built-in GRAM. Thus, the static pictures can be displayed normally without the ESP continuously outputting the SPI clock, but the pictures cannot be updated during this period.

-----------------------

Are 9-bit bus and 18-bit color depth supported if I use the ILI9488 LCD screen to test the `screen <https://github.com/espressif/esp-iot-solution/tree/master/examples/screen>`__ example?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

   The ILI9488 driver chip can support 9-bit bus and 18-bit color depth. However, Espressif's driver can only support 8-bit bus and 16-bit color depth for now. You can modify the driver according to the ILI9488 datasheet to support 9-bit bus and 18-bit color depth.
