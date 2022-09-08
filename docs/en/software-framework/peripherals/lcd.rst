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

  Please refer to I2S LCD driver: `esp-iot-solution i2s_devices <https://github.com/espressif/esp-iot-solution/blob/master/components/bus/i2s_lcd_esp32_driver.c>`__.

---------------

What is the maximum resolution supported by ESP32 LCD? What is the corresponding frame rate?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Over the 8080 16-bit parallel interface, the ESP32 LCD can support up to 800 × 480 of resolution, and the corresponding frame rate is about 30 frames. Please see `Screen <https://docs.espressif.com/projects/espressif-esp-iot-solution/en/latest/display/screen.html>`__.

----------------

What models of touch panels are supported for testing the `LVGL <https://github.com/espressif/esp-iot-solution/tree/master/examples/hmi/lvgl_example>`_ example on ESP32-S3?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - For the currently supported models of touch panels, please refer to `Touch Panel <https://docs.espressif.com/projects/espressif-esp-iot-solution/en/latest/input_device/touch_panel.html#touch-panel>`_.

---------------

Does ESP32-S3 require an external PSRAM to use the RGB screen?
------------------------------------------------------------------------------------------------------

  Yes, and it must be an 8-line PSRAM. Otherwise, the frame rate will be too low.

--------------------

Which image decoding formats are supported by the ESP32-S3 series of chips?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Currently, only the JPEG decoding format is supported. For an application example, please refer to `esp-idf/examples/peripherals/lcd/tjpgd <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/lcd/tjpgd>`_.
