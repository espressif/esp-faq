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
-------------------------------------------------------------------------------------------

  The external flash can be mapped into CPU instruction space and RO data space simultaneously. ESP32 can support up to 16 MB of external flash.

  - When it is mapped into CPU instruction space, up to 11 MB + 248 KB of data can be mapped at a time. If more than 3 MB + 248 KB is mapped at a time, the cache performance may be degraded due to speculative CPU reads.
  - When it is mapped into RO data space, up to 4 MB of data can be mapped at a time, and 8-bit, 16-bit and 32-bit reads are supported.
  - You should specify flash partition table when programming. Specifically, you should divide flash into different partitions, such as app partition, data partition, and OTA partition, and you should specify the size and offset address of each partition.
  - When using flash, you need to pay attention to its service life. As flash can sustain only a limited number of erase operations, you need to plan and manage the usage of flash. For example, you can use wear leveling to extend the service life of flash.
  - It should be noted that writing operations to flash occupy CPU resources, which may influence the system response time. As a result, the writing operation to flash should be avoided as much as possible.

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

  - Different ESP32 modules may have different flash chips or flash controllers, which may affect the erase time. Some models of flash do not have a mechanism to skip empty blocks during erasing, so it takes longer time. Specifically, different flash chips may have different erase time, for example, the erase time of SPI flash and QSPI flash is different. Even the same type of flash chip may have different erase time as they are produced and packaged in different batches. In addition, the design and performance of the flash controller may also affect the erase time. Therefore, erase time varies in ESP32 modules with different flash chips and flash controllers.

------------

When the flash SPI mode is set to QIO mode on the ESP32-S3-WROOM-2-32R8V module, the running firmware prints the following error. Why?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    E (47) qio_mode: Failed to set QIE bit, not enabling QIO mode

  The ESP32-S3-WROOM-2-32R8V module uses the 32 MB Octal flash and the 8 MB Octal PSRAM. Please enable the settings in the configuration options: 

  - ``(Top)`` > ``Serial flasher config`` > ``[*] Enable Octal Flash`` > ``Flash SPI mode (OPI)``
  - ``(Top)`` > ``Component config`` > ``ESP PSRAM`` > ``Support for external, SPI-connected RAM`` > ``SPI RAM config`` > ``Mode (QUAD/OCT) of SPI RAM chip in use``
  
----------------

How can I confirm whether ESP-IDF supports a certain flash?
---------------------------------------------------------------------------------------------------------------------------------------------

  - You can refer to `Optional features for flash <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/spi_flash/spi_flash_optional_feature.html#optional-features-for-flash>`__ for further understanding of the flash information supported by ESP-IDF. Please note that this document only indicates that the ESP-IDF code supports these flash features, and it is not a list of stable flash certified by Espressif.
  - For further support on flash selection, please contact `Espressif <https://www.espressif.com/en/contact-us/sales-questions>`_.
   

-------------

For the SPI flash connected to ESP32-S3, what is the maximum amount of data that can be written in a single operation?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Due to hardware limitations, ESP32-S3 allows a maximum of 64 bytes of data per operation.
