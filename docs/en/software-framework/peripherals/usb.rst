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
  - However, ESP32-S2/S3 supports USB2.0 Full-speed mode.

---------------

Does the ESP-IDF SDK USB interface support HID and MSC modes?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP32S2/S3 can be used as MSC Host to support reading from or writing to storage devices such as USB flash disks. For details, please refer to `esp-idf <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/usb/host/msc>`__.
  - ESP32S2/S3 can be used as MSC Device to simulate storage of USB flash disks. For details, please refer to `esp-iot-solution <https://github.com/espressif/esp-iot-solution/tree/usb/add_usb_solutions/examples/usb>`__.
  - ESP32S2/S3 does not support HID Host currently.
  - ESP32S2/S3 can be used as HID Device. For details, please refer to `esp-iot-solution <https://github.com/espressif/esp-iot-solution/tree/usb/add_usb_solutions/examples/usb>`__.

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

  Yes, but you cannot define the descriptor by yourself.

---------------

What are the USB features of ESP32-S2 and ESP32-S3? 
--------------------------------------------------------------------------------------------------------------------------------

  ESP32-S3 and ESP32-S2 support USB 2.0 OTG, and both support Host and Device functions. On top of that, ESP32-S3 also supports USB-Serial-JTAG peripheral, which can be used to download and debug firmware.
 
---------------

Are there any references to the library and demo of ESP32-S2 USB Host? 
--------------------------------------------------------------------------------------------------------------------------

  Please refer to `USB Host <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s2/api-reference/peripherals/usb_host.html>`_ in ESP-IDF.

---------------

The USB protocol supported by ESP32-S2 is OTG 1.1, with the maximum speed of 12 Mbps. Can it communicate with USB 2.0 devices?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  In the full speed mode, USB 2.0 devices are compatible with USB 1.1 devices, so they can communicate with each other.
  
---------------

Does ESP32-S2 support USB camera?
------------------------------------------------------------------------

  Yes. For demo code, please refer to example `uvc_stream <https://github.com/espressif/esp-iot-solution/tree/usb/add_usb_solutions/components/usb/uvc_stream>`_.

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

  You need to compile under ESP-IDF v4.4 or later versions. After pulling the latest branch and `updating the IDF tool <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/get-started/index.html>`_, you can compile normally and download it using USB. Please refer to `usb-serial-jtag-console <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/api-guides/usb-serial-jtag-console.html>`_ for the usage.

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

-------------

Does ESP32-S3 support USB CDC for printing program log and downloading firmware?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Yes, ESP32-S3 supports printing program log and downloading firmware using USB CDC when the following configuration option is enabled:

  ``Component config`` > ``ESP System Settings`` > ``Channel for console output`` > ``USB CDC``

-------------------

Does ESP32-S3 support devices with USB Device being Class 0?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes, please refer to the example `esp-idf/components/tinyusb/additions/src/usb_descriptors.c <https://github.com/espressif/esp-idf/blob/v5.0-dev/components/tinyusb/additions/src/usb_descriptors.c>`_. When class code == 00H, the class category is specified by the interface.

-----------

Can the ESP32-S3's USB OTG interface be used in both USB Host and USB Device modes?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The ESP32-S3's USB OTG interface can not be used both as USB Host and USB Device at the same time. However, it is possible to switch between USB Host and USB Device modes by software. 
  
----------------

When testing the `esp-idf/examples/peripherals/usb/device/tusb_serial_device <https://github.com/espressif/esp-idf/tree/release/v5.0/examples/peripherals/usb/device/tusb_serial_device>`_ example to send data using TinyUSB, do I have to use the `tinyusb_cdcacm_write_flush() <https://github.com/espressif/esp-idf/blob/203c3e6e1cdb1861cecaed4834fb09b0e097b10d/examples/peripherals/usb/device/tusb_serial_device/main/tusb_serial_device_main.c#L34>`_ function?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  To prevent sending FIFO overflows, you can use the 'tinyusb_cdcacm_write_flush()' function to flush. However, a large number of cycles of flushing may fail. So, it is recommended to set it according to the actual application.

---------------

Can ESP32-S3 use an external USB hub chip with two of its USB ports connecting to a USB 4G module and a dongle at the same time?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The ESP32-S3 USB does not support connection to an external USB hub chip currently because there is no driver support.
