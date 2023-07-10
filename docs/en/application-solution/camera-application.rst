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

What type of camera does the ESP32 series chips support?
--------------------------------------------------------------------------------

   - Please refer to `Camera models supported by ESP32 series <https://github.com/espressif/esp32-camera/blob/master/README.md>`_.

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

--------------

Can the 2-megapixel OV2640 camera on the ESP-EYE be changed to only output 0.3-megapixel images?
-----------------------------------------------------------------------------------------------------------------------------

  Yes, you can specify the output resolution of the camera by configuring the value of `frame_size <https://github.com/espressif/esp32-camera/blob/master/driver/include/sensor.h#L110>`_ during initialization.

--------------

Does ESP32 support a global shutter camera?
----------------------------------------------------------------------------------------

  Yes. Currently, the camera models supported by ESP32 are SC031GS and SC132GS, while other cameras need additional driver support.

--------------

What is the frame rate when ESP32 transfers 1080P video via RTSP using the DVP camera?
-----------------------------------------------------------------------------------------------------------------

  We haven't conducted the test for 1080P yet. Currently, 720P can reach 20 FPS.

--------------

ESP32-S3 only supports MJPEG encoding, but H264/H265 format encoding is needed when implementing rtsp/rtmp streaming. Is there any encoding that supports H264/H265 format?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Currently, encoding in H264/H265 format is not supported.

--------------

Does ESP32/ESP32-S3 have a camera that supports wide-angle?
-----------------------------------------------------------------------------------------------

  Yes, you can refer to the two cameras modules: BF3005 and OV5640.

--------------

It takes 5 seconds for ESP32-S2 to display the camera image from power-on. Can it be improved?
----------------------------------------------------------------------------------------------------------------------------------------

  Yes, please refer to the following:

  - Try to remove some delay functions in ``esp_camera_init()``.
  - Change the clock frequency of sccb in ``menuconfig`` -> ``component config`` -> ``camera configuration`` to 400000.

--------------

Can ESP32 directly provide 24 MHz frequency to GC0308 camera?
---------------------------------------------------------------------------------------------

  I'm afraid not. The XCLK provided by ESP32 to GC0308 has been tested, with a maximum stable test value of 20 MHz.

--------------

Does ESP32/ESP32-S3 support MMS streaming protocol?
---------------------------------------------------------------------------------------------

  No, ESP32 and ESP32-S3 do not support the Microsoft Media Server (MMS) streaming protocol directly. The streaming media protocols supported by ESP32 and ESP32-S3 are RTSP and SIP. If you need to use ESP32 or ESP32-S3 for scenarios that require MMS protocol support, you can consider using middleware or converters that support the MMS protocol.

--------------

When debugging the GC2145 camera with ESP32-S3, the maximum supported resolution seems to be 1024x768. If it is adjusted to a larger resolution, such as 1280x720, it will print `cam_hal: EV-EOF-OVF` error. How to solve this issue?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  In this case, it is necessary to reduce the PCLK of GC2145. For specific methods, try to configure a smaller XCLK and debug the PLL clock coefficient of the camera.

--------------

Does ESP32-S3 support GB28181 protocol?
------------------------------------------------------------------------------------

  Not yet supported.

--------------

Is there any reference for ESP32/ESP32-S2/ESP32-S3 to recognize the QR code through the camera?
------------------------------------------------------------------------------------------------------------------------------------------------

  Yes, please refer to the `code recognition <https://github.com/espressif/esp-who/tree/master/examples/code_recognition>`_ in ESP-WHO.

--------------

When adding the SD-card interface and camera interface for OV5640 sensor, we found that some pins of different ESP32 drivers conflicted with each other. Please suggest pins for the camera interface and SD-card interface.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  `ESP-WROVER-KIT development board <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/esp32/get-started-wrover-kit-v3.html>`__ includes the camera and SD card circuits, so you can refer to pins configuration of `ESP-WROVER-KIT V3 Getting Started Guide <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/esp32/get-started-wrover-kit-v3.html>`__.

--------------

Can a driver for a specific camera model be added if the currently supported camera sensors do not meet my requirements?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Yes. Please confirm your requirements and select the camera sensor model with our engineers through `technical support <https://www.espressif.com/en/contact-us/technical-inquiries>`__. We can then provide the corresponding driver for your camera sensor.

--------------

How to add a custom resolution?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Suppose you need a resolution of 640x240. You can add the custom resolution in two ways:

  - Configure the sensor to work at the typical resolution of 640x480 and only use the upper half of the data (640x240).
  - Add the identifier FRAMESIZE_640*240 in `esp32-camera/driver/include/sensor.h <https://github.com/espressif/esp32-camera/blob/master/driver/include/sensor.h#L92>`__, and define the length and width of that resolution in `esp32-camera/driver/sensor.c <https://github.com/espressif/esp32-camera/blob/master/driver/sensor.c#L31>`__` as {640, 240, ASPECT_RATIO_16X9}. This method requires support for custom resolutions in the sensor's driver to work properly.

--------------

How to modify the register configuration of a camera sensor?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Suppose you want to change the register configuration of the OV5640 sensor. This can be achieved in two ways:

  - Directly configure the relevant registers using write_reg() in the reset() function of `esp32-camera/sensors/ov5640.c`.
  - Configure the relevant registers using set_reg() at the application level:

  .. code-block:: c  

    //Initialize the camera
    esp_err_t ret = esp_camera_init(&camera_config);
    sensor_t *s = esp_camera_sensor_get();
    s->set_reg(s, 0xFFFA, 0xFF, 0xA1);
  
--------------

What triggers "cam_hal: EV-VSYNC-OVF" in esp32-camera?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  This issue occurs when the frame synchronization signal triggered by the sensor is too fast. You can troubleshoot it following the steps below:

  - Run the `esp-iot-solution/examples/camera/pic_server <https://github.com/espressif/esp-iot-solution/tree/master/examples/camera/pic_server>`__ example. If the example runs correctly, it indicates that the issue is not hardware-related.
  - Check the XCLK and resolution specified during sensor initialization. A smaller resolution or a larger XCLK can cause the frame synchronization signal triggered by the sensor to be too fast. Note that the XCLK used by the sensor should match the specified resolution.
