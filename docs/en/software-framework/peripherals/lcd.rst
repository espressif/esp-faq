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

  Please refer to the `ESP-IoT-Solution Programming Guide - LCD Development Guide <https://docs.espressif.com/projects/esp-iot-solution/en/latest/display/lcd/lcd_development_guide.html#lcd-development-guide>`__.

---------------

Which adapted ICs can be used by the LCD screen of ESP32 series chips?
-------------------------------------------------------------------------------------------------

  Please refer to the `ESP-IoT-Solution Programming Guide - LCD Development Guide <https://docs.espressif.com/projects/esp-iot-solution/en/latest/display/lcd/lcd_development_guide.html#id2>`__.

--------------

Notes for Driving MIPI-DSI LCD with ESP32-P4
-------------------------------------------------------------------

  - ESP32-P4 supports MIPI-DSI LCD with up to 2 lanes. Each supports a maximum rate of 1.5 Gbps, totaling 3 Gbps. It also supports color formats ``RGB565``, ``RGB666``, and ``RGB888``.
  - Some MIPI-DSI LCDs, such as ``ILI9881`` and ``JD9365``, are configured as 4-lane by default through hardware (IM[0:3]). However, they can be configured to 2-lane by modifying the LCD's initialization commands (e.g., the ``B6h-B7h`` command of ILI9881). Therefore, it is necessary to consult the datasheet of the LCD driver IC to confirm if it is supported.
  - The MIPI-DSI driver has the communication response mechanism enabled by default. If there is a communication anomaly between the ESP and the LCD, the ESP may freeze and trigger the watchdog. At this point, please check whether the hardware connection is correct, or use a logic analyzer to check if the communication works well.

--------------

Do ESP series development boards with screens support GUI development using the Arduino IDE?
-----------------------------------------------------------------------------------------------------------------

  - The official LCD driver library for Arduino development, `ESP32_Display_Panel <https://github.com/esp-arduino-libs/ESP32_Display_Panel>`__, has been released. It can be directly downloaded on the Arduino IDE. For supported development boards, please refer to the `documentation <https://github.com/esp-arduino-libs/ESP32_Display_Panel/blob/master/README.md#espressif-development-boards>`__.
  - Several points to note:

    - ESP32_Display_Panel relies on `arduino-esp32 <https://github.com/espressif/arduino-esp32>`__.
    - Due to the :ref:`screen drift <lcd-rgb-screen-drift>` issue with the RGB interface of ESP32-S3, it is necessary to use features from ESP-IDF release/v5.1 or later to solve the problem. However, the ESP-IDF version used in arduino-esp32 v2.x.x is v4.4.x, which cannot solve this problem. Therefore, you should use arduino-esp32 v3.x.x. For detailed instructions, please refer to `Document <https://github.com/esp-arduino-libs/ESP32_Display_Panel/blob/master/README.md#how-to-fix-screen-drift-issue-when-driving-rgb-lcd-with-esp32-s3>`_.
    - Given that Arduino cannot adjust various parameter configurations, such as compile optimization levels, through menuconfig like ESP-IDF, it is recommended to develop a GUI based on ESP-IDF to achieve optimal performance.

--------------

How can I improve the display frame rate of LCD screens?
----------------------------------------------------------

  - For a detailed introduction to frame rates, please refer to the `ESP-IoT-Solution Programming Guide - LCD Overview <https://docs.espressif.com/projects/esp-iot-solution/en/latest/display/lcd/lcd_guide.html#id9>`__. Generally speaking, due to the computational performance of the ESP, the "interface frame rate" is often much higher than the "rendering frame rate", so this issue can be described as "how to improve the rendering frame rate of the LCD". This issue can be considered from the following three aspects:

    - Improve the performance of ESP. When developing with ESP-IDF, ESP can be configured through menuconfig, but it is not configured to the best performance by default. Here, taking ``ESP32-S3`` as an example, we can increase the CPU frequency to the highest ``240 MHz``, increase the frequency of FreeRTOS tick to 1000, and increase the bandwidth of Flash or PSRAM. In addition, we can also increase the data cache line size, set the compilation optimization level to ``-O2``, and so on.
    - Improve the performance of LVGL. LVGL itself can also be configured through menuconfig or the *lv_conf.h* file, such as setting LVGL to use the ``malloc`` and ``memcpy`` memory operation functions in ESP-IDF, enabling the ``fast memory`` compilation option, etc.
    - Optimize application design. You can make full use of CPU resources by adjusting the priority of tasks or specifying CPU cores for LVGL and other tasks, especially for ESPs with dual cores. Besides, you can also optimize the design of the GUI, such as avoiding the use of complex animations and layers with transparency overlay effects as much as possible.

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

  - For detailed LCD and LVGL performance specifications, please refer to the `document <https://github.com/espressif/esp-bsp/blob/master/components/esp_lvgl_port/docs/performance.md>`__.

---------------

Is there any example code for I2S driving LCD with ESP32?
-------------------------------------------------------------------------------------

  - The interface type of the screen driven by I2S in ESP32/ESP32-S2 is i80(8080)
  - For the application examples, please refer to :ref:`LCD examples <lcd-examples>`.

---------------

What is the maximum resolution supported by ESP LCD? What is the corresponding frame rate?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - For the RGB peripheral interfaces of ESP32-S3 and ESP32-P4, due to their hardware limitations, they theoretically support a maximum resolution of ``4096 x 1024`` (with a maximum of ``4096`` horizontally and ``1024`` vertically); for the other peripheral interfaces of the ESP series chips, there is no "maximum" hardware limitation on how much resolution they can support.
  - Because chip storage, computing performance, and peripheral interface bandwidth are limited, and different types of LCDs usually have specific resolution ranges, it is recommended to use the following resolutions for ESP32-C3 and ESP32-S3 chips:

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
          - Not_recommended
          - Not_supported
          - Not_supported
          - Not supported

        * - ESP32-S3
          - 320 x 240
          - 400 x 400
          - 480 x 320
          - 480 x 480, 800 x 480  
          - Not supported

        * - ESP32-P4
          - 320 x 240
          - 400 x 400
          - 480 x 320
          - 480 x 480，800 x 480
          - 1024 x 600，1280 x 720

  - For the RGB interface of ESP32-S3, the maximum resolution tested in LVGL (v8) application scenarios is currently 800 x 480, with an interface frame rate limit of 59 (PCLK 30 MHz), corresponding to an average LVGL frame rate of 23; The maximum average LVGL frame rate is 26, corresponding to an interface frame rate of 41 (PCLK 21 MHz).
  - For the MIPI-DSI interface of ESP32-P4, the maximum resolution tested in LVGL (v8) application scenarios is currently 1080 x 1920, with an interface frame rate limit of 31 (DPI_CLK 80 MHz, 2-lane bit rate 2.8 Gbps), corresponding to an average LVGL frame rate of 4;

----------------

How can I enable PSRAM 120M Octal (DDR) on ESP32-S3R8?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP-IDF v5.1 or later versions are required.
  - Enable configuration items through menuconfig: ``IDF_EXPERIMENTAL_FEATURES``, ``SPIRAM_SPEED_120M``, ``SPIRAM_MODE_OCT``.
  - The ``ESP32-S3-WROOM-1-N16R16V`` module currently does not support this feature. If enabled, the chip may freeze upon power-up and then reset.
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

  - Enable the Bounce Buffer mode of the RGB driver. The larger the buffer, the better the effect. For usage, please refer to the `documentation <https://docs.espressif.com/projects/esp-idf/en/v5.1.4/esp32s3/api-reference/peripherals/lcd.html#bounce-buffer-with-single-psram-frame-buffer>`_. Please note that in this mode, the CPU first moves PSRAM data to SRAM, and then the GDMA transfers data to the RGB peripheral. Therefore, it is necessary to enable ``CONFIG_ESP32S3_DATA_CACHE_LINE_64B=y``. Otherwise, it may cause the screen to drift.
  - Based on limited testing, for Quad PSRAM at 80 MHz, the highest PCLK setting is around 11 MHz; for Octal PSRAM at 80 MHz, the highest PCLK setting is around 22 MHz; for Octal PSRAM at 120 MHz, the highest PCLK setting is around 30 MHz.
  - For applications using LVGL, the task of RGB peripheral initialization can be assigned to the same core as the task of LVGL ``lv_timer_handler()``. This significantly increases the upper limit of PCLK settings.

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

    - The PCLK setting of the RGB peripheral is too high, and the bandwidth of PSRAM or GDMA cannot be satisfied.
    - PSRAM and flash share a set of SPI interfaces. PSRAM is disabled during writes to flash (such as via Wi-Fi, OTA, Bluetooth LE).
    - Reading a large amount of flash/PSRAM data results in insufficient PSRAM bandwidth.

  - **Solutions**

    - Improve PSRAM and flash bandwidth. For example, use a higher frequency or larger bit width under the conditions allowed by the hardware.
    - Enable ``CONFIG_COMPILER_OPTIMIZATION_PERF``.
    - Reduce the Data Cache Line Size to 32 Bytes (set to 64 Bytes when using the RGB ``Bounce Buffer`` mode).
    - Enable ``CONFIG_SPIRAM_FETCH_INSTRUCTIONS`` and ``CONFIG_SPIRAM_RODATA``.
    - (Not Recommended) Enable ``CONFIG_LCD_RGB_RESTART_IN_VSYNC`` to automatically recover after screen drifting, but this cannot completely avoid the issue and may reduce the frame rate.

  - **Applications**

    - While ensuring the screen display is normal, try to reduce the frequency of PCLK and decrease the bandwidth utilization of PSRAM.
    - If you need to use Wi-Fi, Bluetooth LE, and continuous flash writing operations, please adopt the ``XIP on PSRAM + RGB Bounce buffer`` method. Here, ``XIP on PSRAM`` is used to load the code segment and read-only segment data into PSRAM, and the flash writing operation will not disable PSRAM after it is turned on. ``RGB Bounce buffer`` is used to block the frame buffer data and transfer it from PSRAM to SRAM through the CPU, and then use GDMA to transfer data to the RGB peripheral. Compared with directly using PSRAM GDMA, it can achieve higher transmission bandwidth. The setup steps are as follows:

      - Make sure the ESP-IDF version is release/v5.0 or newer (released after 2022.12.12), as older versions do not support the ``XIP on PSRAM`` function. (release/v4.4 supports this function through patching, but it is not recommended)
      - Confirm whether ``CONFIG_SPIRAM_FETCH_INSTRUCTIONS`` and ``CONFIG_SPIRAM_RODATA`` can be enabled in the PSRAM configuration. If the read-only data segment is too large (such as a large number of images), it may cause insufficient PSRAM space. At this time, you can use the file system or make the images into a bin to load into the designated partition.
      - Check if there is any memory (SRAM) left, and it takes about [10 * screen_width * 4] bytes.
      - Set ``Data cache line size`` to 64 Bytes (you can set ``Data cache size`` to 32 KB to save memory).
      - Set ``CONFIG_FREERTOS_HZ`` to 1000。
      - If all the above conditions are met, you can refer to the `documentation <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/lcd.html#bounce-buffer-with-single-psram-frame-buffer>`__ to modify the RGB driver to ``Bounce buffer`` mode. The ``Bounce buffer`` mode allocates a block of SRAM memory as an intermediate cache, then quickly transfers the frame buffer data in blocks to SRAM via the CPU, and then transfers the data to the RGB peripheral via GDMA, thus avoiding the issue of PSRAM being disabled. If drift still occurs after enabling, you can try to increase the buffer, but this will consume more SRAM memory.
      - If you still have the drift problem when dealing with Wi-Fi, you can try to turn off ``CONFIG_SPIRAM_TRY_ALLOCATE_WIFI_LWIP`` in PSRAM, which takes up much SRAM space.
      - The effects of this setting include higher CPU usage, possible interrupt watchdog reset, and higher memory overhead.
      - Since the Bounce Buffer transfers data from PSRAM to SRAM through the CPU in GDMA interrupts, the program should avoid performing operations that disable interrupts for an extended period (such as calling ``portENTER_CRITICAL()``), as it can still result in screen drifting.

    - For the drift caused by short-term operations of flash, such as before and after Wi-Fi connection, you can call ``esp_lcd_rgb_panel_set_pclk()`` before the operation to reduce the PCLK (such as 6 MHz) and delay about 20 ms (the time for RGB to complete one frame), and then increase PCLK to the original level after the operation. This operation may cause the screen to flash blank in a short-term.
    - If unavoidable, you can enable ``CONFIG_LCD_RGB_RESTART_IN_VSYNC`` or use the ``esp_lcd_rgb_panel_restart()`` to reset the RGB timing to prevent permanent drifting.

-----------------------------

Why is there vertical dislocation when I drive SPI/8080 LCD screen to display LVGL?
---------------------------------------------------------------------------------------------

  If you use DMA interrupt to transfer data, ``lv_disp_flush_ready()`` of LVGL should be called after DMA transfer instead of immediately after calling ``draw_bitmap()``.

---------------------------

When I use ESP32-C3 to drive the LCD display through the SPI interface, is it possible to use RTC_CLK as the SPI clock, so that the LCD display can normally display static pictures in Deep-sleep mode?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Deep-sleep mode: The CPU and most peripherals are powered down, only the RTC memory is operational. For more details, please refer to the "Low Power Management" section in the `ESP32-C3 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf>`__.
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

  - Check for RGB/BGR setting errors: For example, if the screen is set to red (0xC0, 0x0, 0x0), but the screen actually displays black.
  - Check whether the RGB and BGR registers are set: For example, in ST7789, it can be corrected through the MADCTL (36h) register (when MADCTL (36h) = 1, it is BGR; when MADCTL (36h) = 0, it is RGB).
  - Check for LVGL SWAP16 setting errors: If the screen is configured to red (0xC0, 0x0, 0x0), but the screen actually displays blue, please go to menuconfig → Component config → LVGL configuration → Color settings.
  - If there's missing colors in the RGB TTL screen display, it is necessary to set R, G, B displays separately, and check whether the channel with waveform and RGB data line design are compliant.

---------------------------

The spaces in the LVGL's label are correctly inputted, for example "Indoor temperature 25.5℃", but the spaces are not displayed on the screen. What could be the reason and how to troubleshoot this?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  This pertains to the missing display of the LVGL label. Enable the following debug items and missing characters will be filled with squares to prevent map loss:

    - ``Component config`` → ``LVGL configuration`` → ``Font usage`` → ``Enable drawing placeholders when glyph dsc is not found``

---------------------------

When LVGL continuously loads different images stored on flash, the speed is too slow. For example, how to avoid the slow speed issue when cycling through three images on the home screen?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The reason for the slow speed is that the corresponding image caching mechanism is not turned on, so each images need to be parsed by the parser each time it is used.
  - Enable the corresponding image caching mechanism via the ``#define LV_IMG_CACHE_DEF_SIZE 1`` macro, where 1 represents the number of cached images. Please note that this operation will consume more memory.

---------------------------

LVGL fails to load PNG, JPEG images from flash. What's the reason for a blank screen?
---------------------------------------------------------------------------------------------------------------------------

  - First, it is necessary to check the status of the remaining memory. LVGL needs to perform two steps to load images: loadpng_get_raw_size and loadpng_convert. If the memory is not enough, it will directly return error code 83.
  - The memory requirements should also be estimated in advance: ``loadpng_get_raw_size`` needs memory equivalent to the image size, ``loadpng_convert`` requires memory of image length * width * 3 bytes. Enabling the image caching mechanism will cause large ``image_cache``, which will simultaneously lead to memory strain.

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

  When converting images to MAP format via imageconverter, if using non-RAW formats such as CF_TRUE_COLOR for conversion, subsequent LVGL loading will not require re-decoding, but it will occupy a larger code segment.

---------------------------

When using some third-party libraries such as FreeType and Lottie with LVGL, why does the screen go blank despite the program loading normally?
-------------------------------------------------------------------------------------------------------------------------------------------------------------

  First, consider whether the task stack settings are incorrect. Generally, more than 30 KB of task stack needs to be allocated. Please refer to the following demos:

  - `freetype demo <https://github.com/espressif/esp-iot-solution/tree/master/examples/hmi/lvgl_freetype>`__
  - `lottie porting <https://docs.lvgl.io/master/libs/rlottie.html>`__

---------------------------

What are some good solutions if the internal RAM of ESP32-S3, driving an SPI screen, is insufficient to allocate space for the entire screen buffer?
----------------------------------------------------------------------------------------------------------------------------------------------------

  Use PSRAM as a framebuffer, and then use a small SRAM buffer to transfer data to the framebuffer in multiple batches (SPI DMA can't directly transfer PSRAM data). After completing the transfer, use the framebuffer to render directly. Compared to rendering directly with a small buffer and then sending data, this can prevent tearing and speed up rendering. For specific implementation, please refer to `esp_lvgl_port <https://components.espressif.com/components/espressif/esp_lvgl_port/versions/1.4.0?language=en>`__.

---------------------------

How to deal with diagonal tearing on the SPI screen after the hardware is rotated 90 or 270 degrees?
---------------------------------------------------------------------------------------------------------------------------

  It is recommended to enable the LVGL sw_rotate flag in normal mode to use LVGL's sw_rotate function for software rotation. However, please note that this function conflicts with full_refresh and direct_mode, so do not use them together. For example, calling sw_rotate under full_refresh will directly return without any effect.

---------------------------

Using the ESP32-S2 USB camera and I80 LCD simultaneously may result in the LCD display showing missing images or behaving abnormally. How can this be resolved?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Please refer to `this code <https://github.com/espressif/esp-iot-solution/blob/aefbcb52210e2fbaac7e8a8efcc68645ecd21e7a/components/bus/i2s_lcd_esp32s2_driver.c#L130>`__ to increase the startup delay time of I2S.

---------------------------

How to solve the unexpected crash when operating LVGL controls through non-LVGL tasks?
---------------------------------------------------------------------------------------------------------------------------

  When operating LVGL controls, use ``bsp_display_lock()`` and ``bsp_display_unlock()`` to protect operation variables, thereby ensuring thread safety.

---------------------------

Does ESP32-S3 support RGB888?
---------------------------------------------------------------------------------------------------------------------------

  Parallel RGB888 is not supported. Only RGB565 is supported. You can set up serial RGB888 output as follows:

  .. code-block:: c

    esp_lcd_rgb_panel_config_t panel_conf = {
    ...
    .data_width = 8,
    .bits_per_pixel = 24,
    ...
    }

---------------------------

How can I disable the left and right swipe functionality when operating the LVGL tabview?
---------------------------------------------------------------------------------------------------------------------------

  Please add the following code: ``lv_obj_clear_flag(lv_tabview_get_content(tabview), LV_OBJ_FLAG_SCROLLABLE);``.

---------------------------

Does LVGL support multiple indev inputs?
---------------------------------------------------------------------------------------------------------------------------

  Yes. All input devices are managed in a linked list, supporting multiple input devices of the same and different types. For application examples, please refer to the component `espressif/esp_lvgl_port <https://components.espressif.com/components/espressif/esp_lvgl_port>`__, the current component supports inputs such as touch, button, knob, and hid_host.

---------------------------

Does a high CPU usage rate reported by LVGL have any impact?
---------------------------------------------------------------------------------------------------------------------------

  The CPU usage calculated by LVGL statistics is the duration of the LVGL rendering task within 500 ms, and it does not represent the real CPU usage. Please use FreeRTOS's `vTaskGetRunTimeStats <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/freertos_idf.html#_CPPv420vTaskGetRunTimeStatsPc>`__ to calculate the real usage.

---------------------------

Can ESP32-S3 enter Light-sleep mode after enabling the RGB screen driver?
---------------------------------------------------------------------------------------------------------------------------

  No, it can't. When initializing the RGB interface, if ``CONFIG_PM_ENABLE`` is enabled, ``ESP_PM_NO_LIGHT_SLEEP`` will be automatically locked, preventing the system from entering Light-sleep mode. At this time, please execute ``lcd_rgb_panel_destory`` to disable the RGB screen driver before entering Light-sleep mode.

---------------------------

Is it supported to drive segment LCD screens?
-------------------------------------------------------------------------------

  ESP chips can't directly drive the segment LCD screen through the GPIO pin, because this fuction requires cycling between high and low voltage levels, with an AC voltage from 2.7 V to 5.0 V and typical values of 3.0 V, 3.3 V, 4.5 V, and 5.0 V. However, the chips do not support voltage range adjustment.
