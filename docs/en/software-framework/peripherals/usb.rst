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
----------------------------------------------------

  - No, ESP32 does not support USB function.
  - However, ESP32-S2/S3 supports USB2.0 Full-speed mode.

---------------

Does the ESP-IDF SDK USB interface support HID and MSC modes?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP32S2/S3 can be used as MSC Host to support reading from or writing to storage devices such as USB flash disks. For details, please refer to `esp-idf <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/usb/host/msc>`__.
  - ESP32S2/S3 can be used as MSC Device to simulate storage of USB flash disks. For details, please refer to `esp-iot-solution <https://github.com/espressif/esp-iot-solution/tree/master/examples/usb/device/usb_msc_wireless_disk>`__.
  - ESP32S2/S3 can be used as HID Host. For details, please refer to `ESP-IDF Host HID <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/usb/host/hid>`__.
  - ESP32S2/S3 can be used as HID Device. For details, please refer to `ESP-IDF Device HID <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/usb/device/tusb_hid>`__.

-------------------------

What is the stable current output for ESP32-S2's USB interface?
-------------------------------------------------------------------------------------------------------------------

  The current output capability of the VBUS power line is determined by the power supply, not by the ESP32-S2 chip.  If the chip is self-powered, please refer to `Self-Powered Device <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/usb_device.html#self-powered-device>`__.

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

  ESP32-S3 and ESP32-S2 support USB 2.0 OTG (supporting full-speed mode), and both support Host and Device functions. On top of that, ESP32-S3 also supports USB-Serial-JTAG peripheral, which can be used to download and debug firmware.

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

  Yes. For the demo code of ESP32-S2/ESP32-S3 USB Host UVC, please refer to `usb_stream <https://github.com/espressif/esp-iot-solution/tree/master/components/usb/usb_stream>`__.

Does ESP32-S3 support USB cameras with microphones and speakers?
----------------------------------------------------------------------------

  Yes. For the demo code of ESP32-S2/ESP32-S3 USB Host UVC, please refer to `usb_stream <https://github.com/espressif/esp-iot-solution/tree/master/components/usb/usb_stream>`__.

---------------

Is there any reference for the example of using ESP32S2 as a USB flash drive (MSC DEVICE)?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Please refer to `usb_msc_wireless_disk demo <https://github.com/espressif/esp-iot-solution/tree/master/examples/usb/device/usb_msc_wireless_disk>`_. The average read and write speed currently tested is: read 540 KB/s, write 350 KB/s.

---------------

As ESP32-C3 already has USB function, can I download firmware directly via USB without using the cp2102 chip?
-------------------------------------------------------------------------------------------------------------------------------

  Yes, ESP32-C3 can download firmware via USB, The USB serial port number should be displayed as COMx on Windows devices and ttyACMx on Linux devices.

---------------

Does ESP32-C3 support USB Host?
------------------------------------------------------

  No, it only supports USB-Serial-JTAG function and can only be used as the USB device.

---------------

The ESP32-C3 chip can use USB to download firmware, but it is not supported under ESP-IDF v4.3. How to use USB to download firmware?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  You need to compile under ESP-IDF v4.4 or later versions. After pulling the latest branch and `updating the IDF tool <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/get-started/index.html>`_, you can compile normally and download it using USB. Please refer to `usb-serial-jtag-console <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/api-guides/usb-serial-jtag-console.html>`_ for the usage.

---------------

Does the ESP32-S2 support USB HID?
-----------------------------------------------------------------------

  Yes. For the example of USB HID Device, please refer to `ESP-IDF Device HID <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/usb/device/tusb_hid>`__. For the example of USB HID Host, please refer to `ESP-IDF Host HID example <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/usb/host/hid>`__.

---------------

Why is this error log printed when I am testing the `USB Camera + Wi-Fi Transfer <https://github.com/espressif/esp-iot-solution/tree/master/examples/usb/host/usb_camera_mic_spk>`_ example?
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

  - The ESP32-S3's USB OTG interface can not be used as USB Host and USB Device at the same time. However, it is possible to switch between the USB Host mode and the USB Device mode by software.
  - If you need the standard negotiation function of USB OTG, please note that currently ESP32-S3 only supports this function on the hardware, and does not support it in software protocol.

----------------

When testing the `esp-idf/examples/peripherals/usb/device/tusb_serial_device <https://github.com/espressif/esp-idf/tree/release/v5.0/examples/peripherals/usb/device/tusb_serial_device>`_ example to send data using TinyUSB, do I have to use the `tinyusb_cdcacm_write_flush() <https://github.com/espressif/esp-idf/blob/203c3e6e1cdb1861cecaed4834fb09b0e097b10d/examples/peripherals/usb/device/tusb_serial_device/main/tusb_serial_device_main.c#L34>`_ function?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  To prevent sending FIFO overflows, you can use the 'tinyusb_cdcacm_write_flush()' function to flush. However, a large number of cycles of flushing may fail. So, it is recommended to set it according to the actual application.

---------------

Can ESP32-S3 use an external USB hub chip with two of its USB ports connecting to a USB 4G module and a dongle at the same time?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Supported. The driver is under development.

---------------------

When ESP32-S2/ESP32-S3 serves as the UVC Host and connects some models of UVC cameras, why is there an error `HID_PIPI_EVENT_ERROR_OVERFLOW` in the log?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  This is because MPS of the Alt interface endpoint of the selected camera is too large (ESP32-S2/ESP32-S3 supports up to 512 bytes). Please confirm whether the camera has an interface of less than or equal to 512 bytes under USB1.1.

---------------------

Does ESP32-S2/ESP32-S3 have a USB 4G Internet access solution?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Yes, please refer to `USB CDC 4G Module Example <https://github.com/espressif/esp-iot-solution/tree/master/examples/usb/host/usb_cdc_4g_module>`_.

---------------------

Is there any USB CDC Host example for ESP32-S2/ESP32-S3?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Yes, please refer to `ESP-IDF USB CDC Host example <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/usb/host/cdc>`__ or `esp-iot-solution USB CDC Host example <https://github.com/leeebo/esp-iot-solution/tree/master/components/usb/iot_usbh_cdc>`__.

---------------------

When burning firmware through the ESP32-C3/ESP32-S3 USB Serial/JTAG Controller function, I found that the PC sometimes cannot recognize the USB serial port, or automatically disconnects from the USB serial port repeatedly after recognizing it. What is the reason?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  At present, the startup logic of the ESP32/ESP32-S2/ESP32-S3/ESP32-C3 chip is: if it cannot start normally (due to empty flash, no correct data/firmware in flash, the power-on sequence problem of flash, etc.), the internal timer will trigger the chip to restart every few seconds. The chip cannot connect stably until the program starts normally or enters the download mode. The ESP32-S3/ESP32-C3 USB-Serial-JTAG peripheral will be re-initialized when the chip restarts, so the corresponding result is that the chip tries to connect to and disconnects from the PC every few seconds. We provide the following two solutions:

  - You need to boot the chip to enter the download mode manually before the first download or after flash is erased, so that the chip can be connected stably.
  - You can also burn the firmware that can run stably through UART in advance to solve this issue. If there is firmware that can run stably in the chip, the USB serial port of the chip can be connected stably in subsequent programming.

  If there is no strap pin test point reserved for booting manually, you may need to try several times in the initial USB download.

---------------------

Why does ESP32-S2/ESP32-S3 not reach the maximum USB full speed, 12 Mbps?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  We will explain this issue with the TinyUSB protocol stack as an example. As this USB mode does not use DMA, but directly uses CPU polling, some time slices are wasted in each transfer. As a result, the TinyUSB protocol stack is only expected to reach 6.4 Mbps (it can reach 9.628 Mbps theoretically if the batch transfer is adopted).

---------------------

How can I confirm if ESP32-S2/ESP32-S3 USB supports a certain USB camera or not?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ESP32-S2/ESP32-S3 USB only supports USB cameras that correspond to wMaxPacketSize Video Streaming endpoints which include 512 bytes at the maximum. You can use `USB Stream Example <https://github.com/espressif/esp-iot-solution/tree/master/examples/usb/host/usb_camera_mic_spk>__` to test. An error log will be printed if the camera is not supported.

---------------------

What is the maximum resolution of USB cameras that ESP32-S2/ESP32-S3 support?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - If we do not consider local JPEG decoding, the bottleneck is the throughput rate of USB. The USB camera generally adopts synchronous transmission. ESP USB has a limitation of FIFO size, which can reach 500 KB/s at the maximum currently. Thus, if you want to achieve 15 frames, the size of each frame can only be 33 KB. The maximum resolution that can be achieved by 33 KB depends on the compression rate, and generally it can reach 480 * 320.
  - If you take local JPEG decoding into consideration, you also need to consider whether this resolution can reach 15 frames per second.

---------------------

Can the ESP32-S2/ESP32-S3 USB recognize the USB plugging and unplugging action when it is used as a USB CDC Device?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes, the USB device uses the tinyusb protocol stack, including mount and umount callback functions to response the USB plugging and unplugging events.
  - Please note that if the device is a self-powered USB device and you need to detect the plug and unplug action without power off, please reserve the VBUS detection pin. Refer to the `Self-Powered USB Device Solution <https://docs.espressif.com/projects/esp-iot-solution/en/latest/usb/usb_overview/usb_device_self_power.html>`_.

---------------------

After enabling the RNDIS and CDC functions on the ESP32-S3 USB, I found that the PC can recognize the COM port. However, the automatic programming function of the COM port is invalid. Is it expected?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes. The USB auto-programming function is implemented through the USB-Seial-JTAG peripheral, and the USB RNDIS function is implemented through the USB-OTG peripheral. However, only one of the two peripherals can work at a moment.
  - If the USB-OTG peripheral is used in the application, the automatic programming function implemented by the USB-Seial-JTAG peripheral will not be available. But you can manually enter the download mode for USB burning.

-------------

Does the ESP32-S2/ESP32-S3 support the USB CDC NCM protocol?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Currently, ESP32-S2/ESP32-S3 only supports the USB CDC ECM protocol, but does not support the USB CDC NCM protocol.

After I initialize the USB pins of ESP32-C3/ESP32-S3 to GPIO or other peripheral pins, why cannot I burn firmware through USB?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The USB pin of the ESP32-C3/ESP32-S3 can be initialized to GPIO or other peripheral pins. However, please note that after the initialization, the original USB download function will be disconnected, and the download mode cannot be entered automatically through USB. But you can manually pull down the Boot pin (GPIO9 in ESP32-C3 and GPIO0 in ESP32-S3) to make ESP32-C3/ESP32-S3 enter the download mode. Then you can download firmware through USB.

What should I pay attention to if I want to use the USB interface of ESP32-C3/ESP32-S3 as the unique download interface of firmware?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - DO NOT use USB pins of ESP32-C3 (GPIO18 and GPIO19) / ESP32-S3 (GPIO19 and GPIO20) as other peripheral functions.
  - If the USB pins have to be reused as other functions in the application, the BOOT pin (GPIO9 in ESP32-C3, GPIO0 in ESP32-S3) must be wired to manually enter the chip into the download mode.

---------------

When I attempted to download and print log via the USB interface using the command ``idf.py -p com35 flash monitor`` on Windows, I encountered the following error. What's the reason for it?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  - The error is as follows:

  .. code-block:: text

     Connecting...
     Failed to get PID of a device on com35, using standard reset sequence.

  - On Windows, the COM port must be configured in the upper case, not the lower case ``com``.

--------------------

How can I apply for USB VID/PID for ESP32-S series products?
---------------------------------------------------------------------------------------------------------------------------

  - If your software is based on the TinyUSB protocol stack, you can use the default TinyUSB PID. Otherwise, you need to apply for a USB VID/PID for each ESP32-S series product. For detailed instructions, please refer to `"usb-pids" <https://docs.espressif.com/projects/esp-iot-solution/en/latest/usb/usb_overview/usb_vid_pid.html>`__.

--------------

Is it possible to fix the COM port when downloading firmware using the USB-Serial-JTAG interface on Windows?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Please open the Windows CMD as the administrator and execute the following command to add a registry entry. In this way, you can prevent incremental numbering based on the Serial number. Then you need to restart the computer to enable the modification.

  .. code-block:: text

    REG ADD HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\usbflags\303A10010101 /V IgnoreHWSerNum /t REG_BINARY /d 01

  - For more information, please refer to `Preventing Windows from incrementing COM numbers based on USB device serial numbers <https://docs.espressif.com/projects/esp-iot-solution/en/latest/usb/usb_overview/usb_device_const_COM.html>`_.

---------------------

Can a USB drive be used for OTA upgrades?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Yes, it can be done using the component `esp_msc_ota <https://components.espressif.com/components/espressif/esp_msc_ota>`_.

------------

Does the ESP32 series chip support USB 2.0 High-Speed mode (480 Mbps)?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Currently, only ESP32-P4 supports USB 2.0 High-Speed mode.

------------

How to improve the transmission rate of ESP32-S3 USB?
---------------------------------------------------------------------------------------------------

  - To enhance the transmission performance of USB, you can use USB bulk transfer mode, as well as increase the amount of data transferred per packet.

-------------

Does the USB interface of ESP32-S3 support USB charging function?
---------------------------------------------------------------------------------------------------------------------------------------

No, ESP32-S3 does not support the USB PD (USB-PowerDelivery) protocol currently.

------------

A USB disk application is implemented based on the ESP32-S3 USB interface. Can the ESP32-S3 USB disk always appear as the Z: drive when plugged into a PC?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The drive letter is automatically assigned by the operating system and cannot be fixed by the software on ESP32-S3.
  - Drive Letter Assignment: The operating system will assign an unused drive letter to the USB disk based on the existing drive letters in the current system. In Windows systems, common drive letters are English letters from A to Z. Generally, A and B are traditionally reserved for floppy disk drives, C is usually the system disk, and the remaining letters are sequentially assigned to other storage devices (including hard disk partitions, optical drives, and external USB drives, etc.).

------------

How does a USB UAC device synchronize with the host's audio?
--------------------------------------------------------------------

Since the USB bus is not a clock bus, the interval between each transmission is not fixed. Therefore, UAC devices may experience audio-visual desynchronization and noise, etc. It is recommended to synchronize with the host using the feedback endpoint, allowing the host to send more or less data through the feedback endpoint to achieve audio synchronization.

The `usb_device_uac <https://components.espressif.com/components/espressif/usb_device_uac/versions/0.1.1>`_ component now supports the Feed Back endpoint. You can refer to the example code of this component to implement audio synchronization for the USB UAC device.

------------

Does ESP32-P4 support USB?
---------------------------------

Yes. ESP32-P4 has USB HS PHY, USB FS PHY, and a USB-Serial-JTAG interface.
