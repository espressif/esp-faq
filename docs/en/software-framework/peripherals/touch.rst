Touch Sensor
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

When using ESP32 to develop Touch Sensor applications, where can I find references?
------------------------------------------------------------------------------------------------------------

  Please refer to `Software and Hardware Designs <https://github.com/espressif/esp-iot-solution/tree/release/v1.1/examples/touch_pad_evb>`_.

--------------

When there is water on ESP32-S2 Touch Sensor, does it block or recognize the Touch event with its waterproof function?
------------------------------------------------------------------------------------------------------------------------------------------------------

  When there is a small amount of water droplets, the waterproof function of the ESP32-S2 Touch Sensor can work normally. In the event of a large area of standing water (i.e. the Touch contact area is completely covered), the Touch will temporarily lock and will not resume operation until the water is cleared.

--------------

While the waterproof feature of ESP32-S2 Touch Sensor shielding the Touchpad with water flow, does other pads with no water still usable?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

  Yes, the specific shielding channel can be selected via software.

--------------

Are there any recommendations for materials that can be used to test Touch Sensor, can trigger Touch Sensor stably and is close to the parameters of human touches?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  For experiments with high consistency requirements, it is doable to replace human hands with cell phone pencils.

--------------

Can the pins of Touch Sensor be remapped?
---------------------------------------------------------------------

  No, because Touch Sensor is realized via software programming.

--------------

Do I need to reset a check threshold for Touch Sensor after covering it with a acrylic plate?
-----------------------------------------------------------------------------------------------------------------------------

  Yes.

--------------

Is it possible for Touch Sensor to detect whether there is a acrylic plate on the top, so that it can switch to the pre-defined threshold value automatically when there is a acrylic plate added or removed?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  For now, it cannot adapt to the impacts brought by physical changes.

---------------

What reference drivers does the ESP32 touch screen have?
------------------------------------------------------------------------------------------

  - Code: please refer to `touch_panel_code <https://github.com/espressif/esp-iot-solution/tree/master/components/display/touch_panel>`_.
  - Documentation: please refer to `touch_panel_doc <https://docs.espressif.com/projects/espressif-esp-iot-solution/en/latest/input_device/touch_panel.html>`_.
