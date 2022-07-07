USB
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

Does ESP32 support USB function?
---------------------------------------------------

  - No, ESP32 does not support USB function.
  - However, ESP32-S2 supports USB1.1.

---------------

Does the ESP-IDF SDK USB interface support HID and MSC modes?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Our SDK will provide examples of HID and MSC classes in the future. And specific device classes need to be implemented by yourselves referring to `esp-iot-solution <https://github.com/espressif/esp-iot-solution/tree/usb/add_usb_solutions/examples/usb>`__.

-------------------------

What is the stable current output for ESP32-S2's USB interface? 
-------------------------------------------------------------------------------------------------------------------

  The current output capability of the VBUS power line is determined by the power supply, not by the ESP32-S2 chip.

-------------------------

Does ESP32-S3's USB peripheral supports USB Host?
------------------------------------------------------

  Yes, regarding this function, ESP32-S3 is the same as ESP32-S2.

-------------------------

Does ESP32-C3 USB support USB serial port function and USB JTAG function? 
---------------------------------------------------------------------------------------------------------------------

  Yes.

---------------

What are the USB features of ESP32-S2 and ESP32-S3? 
--------------------------------------------------------------------------------------------------------------------------------

  ESP32-S3 and ESP32-S2 support USB 1.1 OTG, and both support Host and Device functions. On top of that, ESP32-S3 also supports USB-Serial-JTAG peripheral, which can be used to download and debug firmware.
 
---------------

Are there any references to the library and demo of ESP32-S2 USB Host? 
--------------------------------------------------------------------------------------------------------------------------

  This part is already under internal development. If you want to do some functional verification first, please refer to the `USB example <https://github.com/espressif/esp-iot-solution/tree/usb/add_usb_solutions/examples/usb>`_ in esp-iot-solution.

---------------

The USB protocol supported by ESP32-S2 is OTG 1.1, with the maximum speed of 12 Mbps. Can it communicate with USB 2.0 devices?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Most USB 2.0 devices can backward compatible with USB 1.1, so they can communicate with USB 1.1 (in full speed mode).
  
---------------

Does ESP32-S2 support USB camera?
------------------------------------------------------------------------

  Yes, but currently ESP32S2 only supports USB 1.1. So please choose the camera which is compatible with USB 1.1. For demo code, please refer to example `uvc_stream <https://github.com/espressif/esp-iot-solution/tree/usb/add_usb_solutions/components/usb/uvc_stream>`_.

---------------

Is there any reference for the example of using ESP32S2 as a USB flash drive (MSC DEVICE)?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Please refer to `usb_msc_wireless_disk demo <https://github.com/espressif/esp-iot-solution/tree/usb/add_usb_solutions/examples/usb/device/usb_msc_wireless_disk>`_. The average read and write speed currently tested is: read 540 KB/s, write 350 KB/s.
  
---------------

As ESP32-C3 already has USB function, can I download firmware directly via USB without using the cp2102 chip?
-------------------------------------------------------------------------------------------------------------------------------

  Yes, ESP32-C3 can download firmware via USB, The USB serial port number should be displayed as COMx on Windows devices and ttyACMx on Linux devices.
  
---------------

Does ESP32-C3 support USB Host?
------------------------------------------------------

  No, it only supports USB-Serial-JTAG function.

---------------
  
The ESP32-C3 chip can use USB to download firmware, but it is not supported under ESP-IDF v4.3. How to use USB to download firmware?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  You need to compile under ESP-IDF v4.4 or later versions. After pulling the latest branch and `updating the IDF tool <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/get-started/index.html#step-3-set-up-the-tools>`_, you can compile normally and download it using USB. Please refer to `usb-serial-jtag-console <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/api-guides/usb-serial-jtag-console.html>`_ for the usage.

---------------

Does the ESP32-S2 support USB HID?
-----------------------------------------------------------------------

  Supported.

---------------

Why is this error log printed when I am testing the `USB Camera + Wi-Fi Transfer <https://github.com/espressif/esp-iot-solution/tree/usb/add_usb_solutions/examples/usb/host/usb_camera_wifi_transfer>`_ example?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

   E (1437) UVC STREAM: Configuration descriptor larger than control transfer max length

  This error log is reported because the length of the descriptor sent by the USB Camera is larger than the default length (256). You can modify the following configuration to 2048 for testing:

  ``Component config`` > ``UVC Stream`` > ``(2048) Max control transfer data size (Bytes)``