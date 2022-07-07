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

ESP32 是否有 I2S 驱动 LCD 的参考代码？
----------------------------------------------------

  I2S LCD 驱动：`esp-iot-solution i2s_devices <https://github.com/espressif/esp-iot-solution/blob/master/components/bus/i2s_lcd_esp32_driver.c>`_。

---------------

ESP32 LCD 最大可以支持多大的分辨率？相应的帧率是多少？
----------------------------------------------------------------------------------------------------------

  ESP32 LCD 在 8080 16 位并口的接口下，分辨率最大能够支持 800 × 480，相应的帧率约为 30 帧。请参考 `显示屏 <https://docs.espressif.com/projects/espressif-esp-iot-solution/zh_CN/latest/display/screen.html>`_。

---------------

使用 ESP32-S3 测试 `LVGL <https://github.com/espressif/esp-iot-solution/tree/master/examples/hmi/lvgl_example>`_ 例程，请问目前已经适配了哪些型号的触摸屏？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 目前已适配的触摸屏的型号参见 `触摸屏驱动 <https://docs.espressif.com/projects/espressif-esp-iot-solution/zh_CN/latest/input_device/touch_panel.html#id1>`_ 说明。