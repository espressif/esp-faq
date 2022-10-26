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

Is there any example code for I2S driving LCD with ESP32?
-------------------------------------------------------------------------------------

  - The interface type of the screen driven by I2S in ESP32/ESP32-S2 is i80(8080)
  - IDF master and release/4.4 both support the driver of the screen with the interface type of i80
  - Recommended examples:
     - master: `esp-idf/examples/peripherals/lcd/i80_controller <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/lcd/i80_controller>`__.
     - release/4.4: `esp-idf/examples/peripherals/lcd/lvgl <https://github.com/espressif/esp-idf/tree/release/v4.4/examples/peripherals/lcd/lvgl>`__.

---------------

What is the maximum resolution supported by ESP32 LCD? What is the corresponding frame rate?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Over the 8080 16-bit parallel interface, the ESP32 LCD can support up to 800 × 480 of resolution, and the corresponding frame rate is about 30 frames. Please see `Screen <https://docs.espressif.com/projects/espressif-esp-iot-solution/en/latest/display/screen.html>`__.

----------------

What models of display touch panels are supported for testing the `LVGL <https://github.com/espressif/esp-iot-solution/tree/master/examples/hmi/lvgl_example>`_ example on ESP32-S3?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - For the currently supported models of display driver IC, please refer to `Display Screen <https://docs.espressif.com/projects/espressif-esp-iot-solution/en/latest/display/screen.html#id3>`_.
  - For the currently supported models of touch driver IC, please refer to `Touch Panel <https://docs.espressif.com/projects/espressif-esp-iot-solution/en/latest/input_device/touch_panel.html#id1>`_.

---------------

Does ESP32-S3 require an external PSRAM to use the RGB screen?
------------------------------------------------------------------------------------------------------

  Yes, and it must be an Octal PSRAM at least and the clock must be set to 80 MHz or above. Otherwise, the PCLK of RGB LCD cannot be set to a higher frequency and the frame rate will be too low.

--------------------

Which image decoding formats are supported by the ESP32-S3 series of chips?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Currently, ESP-IDF only supports the JPEG decoding format. For an application example, please refer to `esp-idf/examples/peripherals/lcd/tjpgd <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/lcd/tjpgd>`_.
  - If you develop based on LVGL, PNG, BMP, SJPG and GIF decoding formats are supported. For details, please refer to `LVGL libs <https://docs.lvgl.io/master/libs/index.html>`_.

--------------------------

Why is there horizontal drift (overall image drift) when I drive the RGB LCD screen?
--------------------------------------------------------------------------------------------

  - Generally, this is caused by a too big PCLK and the PSRAM bandwidth does not suit it any more. You can set PCLK to a smaller value or increase the PSRAM bandwidth, which is 120 M Octal by default.
  - If `CONFIG_ESP32S3_DATA_CACHE_64KB=y` and `CONFIG_ESP32S3_DATA_CACHE_LINE_64B=y` are enabled, you can set them to default values to increase the upper limit of PCLK setting.

-----------------------------

Why is there vertical dislocation when I drive SPI/8080 LCD screen to display LVGL?
---------------------------------------------------------------------------------------------

  If you use DMA interrupt to transfer data, ``lv_disp_flush_ready`` of LVGL should be called after DMA transfer instead of immediately after calling ``draw_bitmap``. 