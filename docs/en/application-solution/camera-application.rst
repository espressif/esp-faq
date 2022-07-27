Camera application
==================

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

What type of camera does the ESP32 series chip support?
-------------------------------------------------------------------------------

   - Please refer to `Camera models supported by ESP32 series <https://github.com/espressif/esp32-camera#supported-sensor>`_.

--------------

Where is the factory firmware of ESP-EYE?
-------------------------------------------------------------------------------

  - Please refer to `ESP-EYE's factory firmware <https://github.com/espressif/esp-who/tree/master/default_bin>`_.

--------------

Does ESP32 support the camera with a 12-bit DVP interface?
--------------------------------------------------------------------

  No, the driver currently only supports an 8-bit DVP interface.

--------------------

Does ESP32 support acquiring JPEG images using a camera without JEPG encoding?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - If the camera itself does not support JPEG encoding, you can refer to the `esp-iot-solution/examples/camera/pic_server <https://github.com/espressif/esp-iot-solution/tree/ master/examples/camera/pic_server>`_ example provided by us to achieve software JPEG encoding on the ESP32 devices. This method encodes YUV422 or RGB565 data by software to obtain JPEG images. 

