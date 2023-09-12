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
   - ESP-IDF **release/v5.1** is recommended for RGB LCD applications as some features are not supported in release/v4.4.

---------------

Which adapted ICs can be used by the LCD screen of ESP32 series chips?
-------------------------------------------------------------------------------------------------

  Currently, the adapted ICs for the `esp_lcd`-based LCD driver include:

  - `esp_lcd <https://github.com/espressif/esp-idf/blob/7f4bcc36959b1c483897d643036f847eb08d270e/components/esp_lcd/include/esp_lcd_panel_vendor.h>`__ : st7789, nt35510, ssd1306
  - `Package Manager <https://components.espressif.com/components?q=esp_lcd>`__ : gc9a01, ili9341, ili9488, ra8875, sh1107, st7796 (continuously updated)

  **Please note that even if driver ICs are same, different screens vary in register configuration parameters. In addition, screen manufacturers generally provide matched configuration parameters (code). Thus, it is recommended to use the above two methods to obtain code of similar driver ICs, and to update the code based on the parameters of your own screen.**

  Currently, the adapted ICs of `esp_lcd_touch` based touch driver include:

  - `Package Manager <https://components.espressif.com/components?q=esp_lcd>`__: FT5x06, GT1151, GT911, STMPE610, TT21100, XPT2046, CST816 (continuously updated).

--------------

Do ESP32 series development boards with screens support GUI development using the Arduino IDE?
-----------------------------------------------------------------------------------------------------------------

- Currently, an official LCD driver library `ESP32_Display_Panel <https://github.com/Lzw655/ESP32_Display_Panel>`_ has been released for Arduino development. It can be directly downloaded from the Arduino IDE. For details, please refer to `Supported Boards <https://github.com/Lzw655/ESP32_Display_Panel#supported-boards>`_.
- Please note that since Arduino does not support making configurations through menuconfig like ESP-IDF, such as adjusting the compilation optimization level, it's recommended to develop GUI using ESP-IDF to achieve the optimal performance.

--------------

How can I improve the display frame rate of LCD screens?
----------------------------------------------------------

   - The actual display frame rate of LCD screens is determined by the "interface frame rate" and "rendering frame rate". Generally, the "interface frame rate" is much bigger than the "rendering frame rate". So this question actually is "how can I improve the rendering frame rate of the LCD".

   - Taking ESP32-S3R8 as an example, the following ESP configuration items can improve the frame rate (ESP-IDF release/v5.1):

     - CONFIG_FREERTOS_HZ=1000
     - CONFIG_ESP_DEFAULT_CPU_FREQ_MHZ_240=y
     - CONFIG_ESPTOOLPY_FLASHMODE_QIO=y
     - CONFIG_ESPTOOLPY_FLASHFREQ_120M=y [needs to be consistent with PSRAM]
     - CONFIG_SPIRAM_MODE_OCT=y
     - CONFIG_IDF_EXPERIMENTAL_FEATURES=y && CONFIG_SPIRAM_SPEED_120M=y [Need to be consistent with FLASH]
     - CONFIG_SPIRAM_FETCH_INSTRUCTIONS=y
     - CONFIG_SPIRAM_RODATA=y
     - CONFIG_ESP32S3_DATA_CACHE_LINE_64B=y
     - CONFIG_COMPILER_OPTIMIZATION_PERF=y

   - The following LVGL configuration items can improve the frame rate (LVGL v8.3):

     - #define LV_MEM_CUSTOM 1
     - #define LV_MEMCPY_MEMSET_STD 1
     - #define LV_ATTRIBUTE_FAST_MEM IRAM_ATTR

  - For LCD and LVGL performance, please refer to `documentation <https://github.com/espressif/esp-bsp/blob/master/components/esp_lvgl_port/docs/performance.md#lcd--lvgl-performance>`__.

---------------

Is there any example code for I2S driving LCD with ESP32?
-------------------------------------------------------------------------------------

  - The interface type of the screen driven by I2S in ESP32/ESP32-S2 is i80(8080)
  - For the application examples, please refer to :ref:`LCD examples <lcd-examples>`.

---------------

What is the maximum resolution supported by ESP32 LCD? What is the corresponding frame rate?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - There is no "maximum" limit on how much resolution can be supported. Due to the limited data transmission bandwidth of the interface, the interface frame reduces as the LCD resolution increases. Thus, you need confirm the LCD resolution based on this.
  - Over the RGB interface, the maximum resolution of ESP32 LCD is 800 × 480; the maximum interface frame rate is 59 (PCLK 30 MHz); and the average frame rate of LVGL is about 23. The average upper limit of the frame rate of LVGL is 26, and the corresponding interface frame rate is 41 (PCLK 21 MHz).

----------------

How to enable PSRAM 120M Octal(DDR) on ESP32R8?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP-IDF v5.1 or later versions are required.
  - For details, please refer to `SPI Flash and External SPI RAM Configuration <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-guides/flash_psram_config.html#all-supported-modes-and-speeds>`__.
  - Note: This feature is an experimental and has the following temperature-related risks:

    - The chip may not work properly even with ECC enabled when the temperature is above 65°C.
    - Temperature changes may also cause program crashes when accessing PSRAM/flash. For more details, please refer to `SPI Flash and External SPI RAM Configuration <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-guides/flash_psram_config.html#all-supported-modes-and-speeds>`__.

----------------

What models of display touch panels are supported for testing the `LVGL <https://github.com/espressif/esp-iot-solution/tree/master/examples/hmi/lvgl_example>`_ example on ESP32-S3?
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
--------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------

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

Why do I get drift (overall drift of the display) when driving an RGB LCD screen?
-----------------------------------------------------------------------------------------------------------

  - **Reasons**

    - PCLK is set to a too big number, and the PSRAM bandwidth is not applicable.
    - PSRAM is disabled due to the write operation of flash (like Wi-Fi, BLE, OTA).

  - **Solutions**

    - Improve bandwidths of PSRAM and flash. You can set flash to QIO 120 M and set PSRAM to Octal 120 M.
    - Enable `CONFIG_COMPILER_OPTIMIZATION_PERF`.
    - Reduce the Data Cache Line Size to 32 Bytes (set it to 64 Bytes when using the RGB Bounce Buffer mode).
    - Enable `CONFIG_SPIRAM_FETCH_INSTRUCTIONS` and `CONFIG_SPIRAM_RODATA`.
    - Enable `CONFIG_LCD_RGB_RESTART_IN_VSYNC` to automatically recover after screen drifting, but this cannot completely avoid the issue and may reduce the frame rate.

  - **Applications**

    - While ensuring the screen display is normal, try to reduce the frequency of PCLK and decrease the bandwidth utilization of PSRAM.
    - If you need to use Wi-Fi, BLE and continuous write operation to flash, please use `XIP on PSRAM + RGB Bounce buffer` method, and the settings are as follows:

      - Make sure the ESP-IDF version is release/v5.0 or newer (released after 2022.12.12), as older versions do not support the `XIP on PSRAM` function. (release/v4.4 supports this function through patching, but it is not recommended)
      - Verify that whether `CONFIG_SPIRAM_FETCH_INSTRUCTIONS` and `CONFIG_SPIRAM_RODATA` can be enabled in the PSRAM configuration (too large rodata segment will cause insufficient space in the PSRAM).
      - Check if there is any memory (SRAM) left, and it takes about [10 * screen_width * 4] bytes.
      - Set `Data cache line size` to 64 Bytes (you can set `Data cache size` to 32 KB to save memory).
      - Set `CONFIG_FREERTOS_HZ` to 1000。
      - If all the above conditions are met, then you can refer to `Documentation <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/lcd.html#bounce-buffer-with-single-psram-frame-buffer>`__ to modify the RGB driver to `Bounce buffer` mode.
      - If you still have the drift problem when dealing with Wi-Fi, you can try to turn off `CONFIG_SPIRAM_TRY_ALLOCATE_WIFI_LWIP` in PSRAM, which takes up much SRAM space.
      - The effects of this setting include higher CPU usage, possible interrupt watchdog reset, and higher memory overhead.
      - Since the Bounce Buffer transfers data from PSRAM to SRAM through the CPU in GDMA interrupts, the program should avoid performing operations that disable interrupts for an extended period (such as calling `portENTER_CRITICAL()`), as it can still result in screen drifting.

    - For the drift caused by short-term operations of flash, such as before and after Wi-Fi connection, you can call `esp_lcd_rgb_panel_set_pclk()` before the operation to reduce the PCLK (such as 6 MHz) and delay about 20 ms (the time for RGB to complete one frame), and then increase PCLK to the original level after the operation. This operation may cause the screen to flash blank in a short-term.
    - Enable `flags.refresh_on_demand` in `esp_lcd_rgb_panel_config_t`, and manually refresh the screen by calling the `esp_lcd_rgb_panel_refresh()` interface. In addition, you need to reduce the refreshing frequency as much as possible while ensuring that the screen does not flash blank.
    - If unavoidable, you can enable `CONFIG_LCD_RGB_RESTART_IN_VSYNC` or use the `esp_lcd_rgb_panel_restart()` to reset the RGB timing to prevent permanent drifting.

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

---------------------------

When using ESP32-S3 to drive an RGB screen, why does it halt or reset (TG1WDT_SYS_RST) when running `esp_lcd_new_rgb_panel()` or `esp_lcd_panel_init()`?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Please check if the pins occupied by PSRAM in ESP chips or modules conflict with the RGB pins. If there is a conflict, modify the RGB pin configuration.
  - If using ESP32-S3R8, avoid using GPIO35, GPIO36, and GPIO37 pins.
