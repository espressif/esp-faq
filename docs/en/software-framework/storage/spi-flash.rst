SPI Flash
=========

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

What is the requirement for the storage and usage of ESP32 flash?
------------------------------------------------------------------------------------------

  The external flash can be mapped into CPU instruction space and RO data space simultaneously. ESP32 can support up to 16 MB of external flash.

  - When it is mapped into CPU instruction space, up to 11 MB + 248 KB of data can be mapped at a time. If more than 3 MB + 248 KB is mapped at a time, the cache performance may be degraded due to speculative CPU reads.
  - When it is mapped into RO data space, up to 4 MB of data can be mapped at a time, and 8-bit, 16-bit and 32-bit reads are supported.

--------------

What kind of sectors are reserved for customized use in ESP8266 modules?
---------------------------------------------------------------------------------------

  - For previous versions of SDK rel3.0, besides for bootloader and app bin, the following sectors are reserved at the end of the configured flash: 1 for system information, 1 for OTA information and 1 for RF calibration information.
  - For SDK rel3.0 and later versions, we use partition_table to manage flash. Except for partition_table and bootloader, other bin files are all marked in partition_table.

--------------

How to read flash data for ESP8266?
-------------------------------------------------------------------------

  - You can use the script tool under ESP8266-RTOS-SDK to read flash data. The whole process is shown as follows:

    - Install python environment and the required packages;
    - Go to ESP8266_RTOS_SDK/components/esptool_py/esptool;
    - Run ``python esptool.py --chip esp8266 --port /dev/ttyUSB0 --baud 115200 read_flash 0x0 0x400000 esp8266.bin``. In this command, "esp8266.bin" is a self-defined file, where all flash data read will be stored; "/dev/ttyUSB0" is the serial port number in linux environment, which can be different in other environments and systems.

----------------

Why do different ESP32 modules have inconsistent flash erase times?
--------------------------------------------------------------------------------------------------------

  - This is due to the difference in flash models. Some flash models do not have an empty block skip mechanism when erasing, so it takes longer time.

------------

When the flash SPI mode is set to QIO mode on the ESP32-S3-WROOM-2-32R8V module, the running firmware prints the following error. Why?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    E (47) qio_mode: Failed to set QIE bit, not enabling QIO mode

  The ESP32-S3-WROOM-2-32R8V module uses the 32 MB Octal flash and the 8 MB Octal PSRAM. Please enable the settings in the configuration options: 

  - ``(Top)`` > ``Serial flasher config`` > ``[*] Enable Octal Flash`` > ``Flash SPI mode (OPI)``
  - ``(Top)`` > ``Component config`` > ``ESP PSRAM`` > ``Support for external, SPI-connected RAM`` > ``SPI RAM config`` > ``Mode (QUAD/OCT) of SPI RAM chip in use``
  
