Camera Application
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
--------------------------------------------------------

  - For camera models supported by the ESP32, ESP32-S2, and ESP32-S3 series, please refer to `ESP32 Camera Driver <https://github.com/espressif/esp32-camera/blob/master/README.md>`_.
  - For camera models supported by the ESP32-P4 series, please refer to `espressif-camera-sensors-component <https://github.com/espressif/esp-video-components/tree/master/esp_cam_sensor#espressif-camera-sensors-component>`_.

--------------

What are the output image formats of the camera?
-------------------------------------------------

  The image format is mainly determined by the camera. If a camera supports multiple image formats, such as RGB565, RGB888, YUV422, JPEG, and so on, the output format then needs to be selected by configuring the camera's register.

--------------

What parameters does the camera support for adjustment?
--------------------------------------------------------------

  The camera supports adjustment of the following parameters: built-in image mode parameters such as image data transfer speed (PCLK), camera output format, resolution, output image size, white balance, GAMMA correction.

--------------

What is the relationship between MCLK and PCLK in the camera? What is the difference between them?
-------------------------------------------------------------------------------------------------------

  - MCLK is the main clock of the camera system, controlling the synchronization and frequency of the system. Inside the camera chip, MCLK is used to control the timing of various modules, such as pre-processors, digital signal processors, pixel arrays, and data output interfaces. Usually, the frequency of MCLK is jointly determined by the system clock of the main control chip and the divider inside the camera. Common frequencies are 6 MHz, 12 MHz, 24 MHz, 48 MHz, etc.
  - PCLK is the clock signal used to control pixel output. When the camera outputs an image, each pixel output requires a timing signal, and PCLK is the signal used to control this timing. Specifically, the rising edge of PCLK indicates that the data of a pixel has been output, and the falling edge indicates that the data of the next pixel is about to be output, thus forming a sequence of pixel data.
  - MCLK is multiplied/divided (determined by camera configuration) inside the camera to get PCLK. Usually, the frequency of PCLK is half or an integer multiple of half of MCLK. For example, under 24 MHz MCLK, the frequency of PCLK can be 12 MHz, 6 MHz, etc.

--------------

Is a higher PCLK always better for the camera?
------------------------------------------------------

  - Theoretically, the higher the PCLK is, the faster the data transmission will be. However, in actual use, a higher PCLK also means a higher requirement on the processing speed of the chip.
  - The current ESP32 and ESP32-S2 chips realize parallel communication through the I2S interface. Too high a PCLK will cause parallel data to be out of sync, resulting in image jitter or even screen flicker.
  - ESP32-S3 uses an independent LCD-CAM interface, which can support a higher PCLK frequency.

   - For ESP32, the upper limit of PCLK is 8 MHz.
   - For ESP32-S2, the upper limit of PCLK is 32 MHz.
   - For ESP32-S3, the upper limit of PCLK is 40 MHz.

--------------

Do the ESP32 series chips support the MIPI interface?
-------------------------------------------------------

  - ESP32-P4 supports the MIPI interface.

--------------

Do the ESP32 series chips support the USB2.0 interface?
---------------------------------------------------------

  - ESP32-S2 and ESP32-S3 support USB2.0 full-speed interface (12 Mbps). In addition, ESP32-P4 also supports USB2.0 high-speed interface (480 Mbps).

--------------

Why is the transmission speed of YUV/RGB in the camera slower than JPEG?
-------------------------------------------------------------------------

  - Because the amount of YUV/RGB data is larger than that of JPEG.
  - For example: For a screen size of 320 × 240, the output of YUV422 is 153.6 K, while JPEG only needs about 10 K after compression.

--------------

In camera applications, what are the factors that may affect the frame rate?
-------------------------------------------------------------------------------

  In camera applications, the factors that affect the frame rate mainly include:

  - Resolution: As the resolution increases, more pixel data needs to be captured and transmitted per frame, resulting in a lower frame rate.
  - Image format: Common image formats include RGB565, RGB888, YUV422, JPEG, etc. Different image formats have differences in image quality and data compression, which will directly affect the frame rate.
  - Image processing: If each frame of the image needs to be processed, such as noise reduction, enhancement, compression, etc., it will take up more processing time and reduce the frame rate.
  - Transmission bandwidth: As the transmission bandwidth becomes smaller, fewer data needs to be transmitted per frame, resulting in a lower frame rate.
  - Processor performance: For the processor with lower performance, it is more difficult to handle the amount of data needed per frame, resulting in a lower frame rate.

  Therefore, in camera applications, it is necessary to balance these factors according to specific application scenarios to achieve the best frame rate and image quality.

--------------

How to troubleshoot when the camera fails to run?
--------------------------------------------------

  - Unable to recognize the camera model:

   - Check whether the pins correspond correctly, especially for XCLK, SIOC, and SIOD.
   - The clock frequency input by XCLK may be too low or the camera power supply is abnormal, causing the camera to fail to run normally.
   - There are too many devices mounted on SIOC and SIOD, causing the polled read to return the address ID of a device other than the camera. In this case, it is recommended to fix the camera ID to remove the polling step.

  - The camera model is recognized, but there is no image display:

   - Check whether there is a signal on the camera data pin, and whether MCLK is input normally.
   - Check whether the camera register parameters are configured correctly.

  - The camera image display is abnormal:

   - Check the code to see whether the output format is RGB, YUV, or JPEG, and whether it meets the format required by the receiving end.
   - Try to lower the PCLK frequency.

--------------

Does ESP32 support video stream transmission?
----------------------------------------------

  - The operation of video stream transmission is divided into binary transmission and video stream encoding and decoding.

   - Binary transmission: ESP32 itself supports binary transmission, so whether the video stream transmission is supported depends on the network bandwidth of the transmission. The current ESP32 TCP bandwidth is 20 MB/s, please refer to `Wi-Fi test data <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/wifi.html#disconnected-state-sleep>`_.
   - Video stream encoding and decoding is not yet supported on ESP32.

--------------

Where is the factory firmware of ESP-EYE?
------------------------------------------

  Please refer to `ESP-EYE's factory firmware <https://github.com/espressif/esp-who/tree/master/default_bin>`_.

--------------

Where are the examples related to the camera solution stored?
--------------------------------------------------------------

  - Please refer to `ESP-WHO <https://github.com/espressif/esp-who>`_.
  - Please refer to `esp-iot-solution <https://github.com/espressif/esp-iot-solution/tree/master/examples/camera>`_.
  - Please refer to `esp-dev-kits <https://github.com/espressif/esp-dev-kits>`_.
  - For common examples of the ESP32-P4 series, please visit `esp-video/examples <https://github.com/espressif/esp-video-components/tree/master/esp_video/examples>`_.
  - For examples of using ESP32-P4 together with an LCD screen, please visit `esp-iot-solution/examples/camera/video_lcd_display <https://github.com/espressif/esp-iot-solution/tree/master/examples/camera/video_lcd_display>`_.

--------------

Does ESP32 support a camera with a 12-bit DVP interface?
---------------------------------------------------------

  No, the current driver only supports an 8-bit DVP interface.

-----------------

Can ESP32 use a camera without JEPG encoding to obtain JPEG images?
--------------------------------------------------------------------

  If the camera itself does not support JPEG encoding, you can refer to our `esp-iot-solution/examples/camera/pic_server <https://github.com/espressif/esp-iot-solution/tree/master/examples/camera/pic_server>`_ example, to implement software JPEG encoding on the ESP32 device. This method encodes YUV422 or RGB565 data through software to obtain JPEG images.

--------------

Can the 2-megapixel OV2640 camera on ESP-EYE be changed to only output 300,000-pixel images?
---------------------------------------------------------------------------------------------

  Yes, you can specify the resolution size that the camera should output by configuring the `frame_size <https://github.com/espressif/esp32-camera/blob/master/driver/include/sensor.h#L110>`_ value during initialization.

--------------

Does ESP32 support a global shutter camera?
---------------------------------------------------

  Yes. Currently, the camera models supported by ESP32 are SC031GS and SC132GS, while other cameras need additional driver support.

--------------

What is the frame rate when ESP32 transfers 1080P video via RTSP using the DVP camera?
-------------------------------------------------------------------------------------------------

  We have not conducted the test for 1080P yet. Currently, 720P can reach 20 FPS.

--------------

ESP32-S3 only supports MJPEG encoding, but H264/H265 format encoding is needed when implementing rtsp/rtmp streaming. Is there any encoding that supports H264/H265 format?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Currently, ESP32-S3 does not support hardware-accelerated H.264/H.265 encoding. However, you can use software encoders, such as the FFmpeg library and the x264/x265 library, to convert MJPEG frames captured from the OV2640 into H.264/H.265 encoded frames. The conversion performance depends on the processor performance, which may affect the frame rate.

--------------

Does ESP32/ESP32-S3 support wide-angle cameras?
----------------------------------------------------

  Yes. You can refer to BF3005 and OV5640.

--------------

It takes five seconds for ESP32-S2 to display the camera image from power-on. Is there room for improvement?
---------------------------------------------------------------------------------------------------------------

  Yes, please refer to the following:

  - Try to remove some delay functions in ``esp_camera_init()``.
  - Change the sccb clock frequency in ``menuconfig`` > ``component config`` > ``camera configuration`` to 400000.

--------------

Can ESP32 directly support 24 MHz frequency to the GC0308 camera?
------------------------------------------------------------------------

  It might not be feasible. According to tests, the maximum stable test value of XCLK ESP32 supported for GC0308 is 20 MHz.

--------------

Does ESP32/ESP32-S3 support the MMS streaming protocol?
------------------------------------------------------------

  No, ESP32 and ESP32-S3 do not support the Microsoft Media Server (MMS) streaming protocol directly. MMS is a streaming media transmission protocol developed by Microsoft, mainly used for network streaming media playback in Windows Media Player. The streaming media protocols supported by ESP32 and ESP32-S3 are RTSP and SIP. If you need to use ESP32 or ESP32-S3 for scenarios that require MMS protocol support, you may consider using middleware or converters that support the MMS protocol.

--------------

When debugging the GC2145 camera with ESP32-S3, the maximum supported resolution seems to be 1024x768. If it is adjusted to a larger resolution, such as 1280x720, it will print cam_hal: EV-EOF-OVF error. How to solve this issue?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  In this case, it is necessary to reduce the PCLK of GC2145. For specific methods, try to configure a smaller XCLK and debug the PLL clock coefficient of the camera.

--------------

Does ESP32-S3 support the GB28181 protocol?
--------------------------------------------

  ESP32-S3 does not directly support the GB28181 protocol, but it can be implemented by combining ESP32-S3 with external circuits and software. Since GB28181 is a communication protocol between video surveillance devices, the network capabilities of ESP32-S3 and external circuits, such as video encoders, audio codecs, and sensors, can be used to implement the GB28181 function. At the same time, relevant software development is required to realize the parsing and data transmission of the GB28181 protocol.

--------------

Is there any reference for ESP32/ESP32-S2/ESP32-S3 to recognize the QR code through the camera?
-------------------------------------------------------------------------------------------------

  Yes, please refer to the `code recognition <https://github.com/espressif/esp-who/tree/master/examples/code_recognition>`_ in ESP-WHO.

--------------

When adding the SD-card interface and camera interface for OV5640 sensor, we found that some pins of different ESP32 drivers conflicted with each other. Please suggest pins for the camera interface and SD-card interface.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The `ESP-WROVER-KIT development board <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/esp32/get-started-wrover-kit-v3.html>`__ includes the camera and SD card circuits, so you can refer to pins configuration of `the ESP-WROVER-KIT V3 getting started guide <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/esp32/get-started-wrover-kit-v3.html>`__.

--------------

Can a driver for a specific camera model be added if the currently supported camera sensors do not meet my requirements?
-------------------------------------------------------------------------------------------------------------------------------------------

  Yes. Please confirm your requirements and select the camera sensor model with our engineers through `technical support <https://www.espressif.com/en/contact-us/technical-inquiries>`__. We can then provide the corresponding driver for your camera sensor.

--------------

How to add a custom resolution?
--------------------------------

  Suppose you need a resolution of 640x240, you can use the custom resolution in the following two ways:
  - Configure the sensor to work at the typical resolution of 640x480, and then only use the upper half of the data (640x240).
  - Add the identifier FRAMESIZE_640*240 in `esp32-camera/driver/include/sensor.h <https://github.com/espressif/esp32-camera/blob/master/driver/include/sensor.h#L92>`__, and define the length and width of that resolution in `esp32-camera/driver/sensor.c <https://github.com/espressif/esp32-camera/blob/master/driver/sensor.c#L31>`__ as {640, 240, ASPECT_RATIO_16X9}. This method requires support for custom resolutions in the sensor’s driver to work properly.


--------------

How to modify the register configuration of the camera sensor?
---------------------------------------------------------------

  Suppose you need to change the register configuration of the OV5640 sensor. This can be achieved in two ways:
  - Directly configure the relevant registers using write_reg() in the reset() function of esp32-camera/sensors/ov5640.c.
  - Configure the relevant registers at the application layer through the set_reg() function:

  .. code-block:: c

    // Initialize the camera
    esp_err_t ret = esp_camera_init(&camera_config);
    sensor_t *s = esp_camera_sensor_get();
    s->set_reg(s, 0xFFFA, 0xFF, 0xA1);

--------------

What is the reason for triggering "cam_hal: EV-VSYNC-OVF" in esp32-camera?
--------------------------------------------------------------------------

  This issue occurs when the frame synchronization signal triggered by the sensor is too fast. You can troubleshoot it following the steps below:
  - Run the `esp-iot-solution/examples/camera/pic_server <https://github.com/espressif/esp-iot-solution/tree/master/examples/camera/pic_server>`_ example. If this example runs normally, it indicates that the issue is not hardware-related.
  - Check the XCLK and resolution specified during sensor initialization. A smaller resolution or a larger XCLK can cause the frame synchronization signal triggered by the sensor to be too fast. Note that the XCLK used by the sensor should match the specified resolution.

-------------------

What could be the reason for the following warning log appearing in the Camera application based on ESP32-S3?
------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: c

    W (7232) cam_haL:FB-OVF
    W (7242) cam_haL:FB-OVF
    W (7492) cam_haL:FB-OVF
    W (7512) cam_haL:FB-OVF
    W (7762) cam_haL:FB-OVF
    W (7772) cam_haL:FB-OVF
    W (8022) cam_haL:FB-OVF
    W (8042) cam_haL:FB-OVF

  The above warning log indicates a frame buffer overflow, which is caused by too fast a frame rate. You can try to reduce the XCLK (Note that the XCLK of ESP32S3 is devided from the 80 MHz clock by default, so the size of XCLK must be divisible by 80 MHz).
  Specifically, if the sensor is operating in JPEG mode, you can try to increase the size of the jpeg recv buffer by increasing the value of the `Custom JPEG mode frame size (bytes)` option in menuconfig.

-------------------

What is the difference between the two capture modes of the ESP32-Camera?
------------------------------------------------------------------------------------------------------------------------------

  After initialization, the camera sensor pushes image data to the receiver on the ESP32.

  - When the configured receive mode is CAMERA_GRAB_WHEN_EMPTY, the background driver writes image data to the frame_buffer as long as there is an idle frame_buffer. When all the frame_buffers are exhausted, the new image data pushed by the camera sensor will be forcibly discarded due to the lack of available frame_buffer.
  - When the configured receive mode is CAMERA_GRAB_LATEST, the number of frame_buffers that the application layer can obtain is fb_count - 1. This is because the background driver occupies one frame_buffer and tries to refresh the latest data into this frame_buffer.

Note that the capturing does not occur when calling `esp_camera_fb_get`. The capturing is an ongoing process, and we can only control the frame_buffer used by the backend to obtain new data. Therefore, if you want to immediately obtain a new image, try executing the following code:

  .. code-block:: c

    // Returns a frame_buffer to the backend driver
    esp_err_t ret = esp_camera_fb_return(esp_camera_fb_get());
    // The background program automatically refreshes the new image data to frame_buffer, then the application layer can access the data in frame_buffer.
    fb = esp_camera_fb_get();

-------------

How to implement frame skipping with the `esp32-camera <https://github.com/espressif/esp32-camera>`_ SDK?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  You can call `esp_camera_fb_return(esp_camera_fb_get());` to discard the current frame, that is, to skip the frame that is being fetched.

-------------

Can ESP32-S3 connect to two cameras and display split screen?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ESP32-S3 can connect to two cameras with SPI interfaces (with a relatively small resolution, 240*320). However, if using the DVP interface, multiple cameras cannot be used simultaneously. In such cases, the ESP32-P4 is a more suitable option.

-------------

Does ESP32-S3 support a 10-bit DVP camera?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  In general, a 10-bit DVP camera can be used by capturing only the upper 8 bits, which is sufficient to produce a normal image.

-------------

How to scale image data?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - For JPEG images, use the `esp_new_jpeg <https://components.espressif.com/components/espressif/esp_new_jpeg/>`_ component to directly scale down the decoded data during the decoding process.
  - For RGB or YUV data, use the `PPA <https://docs.espressif.com/projects/esp-idf/en/latest/esp32p4/api-reference/peripherals/ppa.html>`_ peripheral (only supported on P series chips), or use the software-based image processing component `esp_image_effects <https://components.espressif.com/components/espressif/esp_image_effects>`_ for scaling.
