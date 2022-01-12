Storage
=======

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

When using ESP32 modules, how to check the size of their PSRAM?
-------------------------------------------------------------------------------

  First of all, you need to enable the PSRAM function in ``make menuconfig``. Then, you can check its size via the log information of bootloader or by calling esp_spiram_get_size().

--------------

When ESP32 connected to a PSRAM externally, how to change its clock source?
----------------------------------------------------------------------------------------------

  In menuconfig: menuconfig -> Component config -> ESP32-specific -> SPI RAM config.

--------------

Is it possible to use ESP8266 together with TF card?
-----------------------------------------------------------------------

  It is not recommended to use ESP8266 together with TF card.

  - Although ESP8266 can be connected to TF card in hardware level (communicate through SPI), the chip may run out of memory in different application scenarios due to its limited resources. Thus, it is not recommended to use ESP8266 with TF card.
  - If all you need is a Wi-Fi-only module that can be connected to a TF card, it is recommended to use the `ESP32-S2 <https://www.espressif.com/sites/default/files/documentation/esp32-s2_datasheet_en.pdf>`_ chip instead.

--------------

If data needs to be stored or updated to flash every minute, can ESP32 NVS meet this requirement?
-------------------------------------------------------------------------------------------------------------------------

  According to `NVS Specifications <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/storage/nvs_flash.html>`_, NVS uses two main entities in its operation: pages and entries. Logical page corresponds to one physical sector of flash memory. For now, we assume that flash sector is 4096 bytes and each page can contain 126 entries (32 bytes for one entry), with the left spaces for page header (32 bytes) and entry state bitmap (32 bytes). Typical flash lifetime is 100 k erase cycles. Assuming that the device is expected to run for 10 years, and the data size written to flash is 4 bytes per minute with flash encryption disabled, then the number of flash write operation can be calculated as: 60×24×365×10=5256000. In this way, no more than 42 k of erase cycles (5256000/126) will be caused in NVS, which does not exceed 100 k. Therefore, such operation is supported even without the effects of multiple sectors. In actual use, usually there will be multiple sectors given to NVS, and the NVS can distribute erase cycles to different sectors, making the number of erase cycles in each sector necessarily less than 42 k.

  Therefore, the NVS of ESP32 can meet such requirement.


--------------

What kind of sectors are reserved for customized use in ESP8266 modules?
---------------------------------------------------------------------------------------

  - For previous versions of SDK rel3.0, besides for bootloader and app bin, the following sectors are reserved at the end of the configured flash: 1 for system information, 1 for OTA information and 1 for RF calibration information.
  - For SDK rel3.0 and later versions, we use partition_table to manage flash. Except for partition_table and bootloader, other bin files are all marked in partition_table.

--------------

Does NVS have wear levelling function?
-------------------------------------------------

   NVS does not use the wear_levelling component in ESP-IDF, but uses an erase levelling mechanism implemented internally. The flash in use is in a wear-levelling state.

--------------

Can NVS sectors be corrupted by accidental power loss during writing?
--------------------------------------------------------------------------------------

  No, NVS is designed to resist accidental power loss, so it will not be damaged.

--------------

Can ESP32 mount a file system partition in the external SPI flash？
---------------------------------------------------------------------------------------------

  Yes, this function has been added in ESP-IDF v4.0 and later versions. Please note that when two partitions are mounted to ESP32, it is not permitted for multiple tasks to write files into the same partition at the same time.

--------------

How to improve the damage to FATFS file system caused by accidental power loss?
-----------------------------------------------------------------------------------------------------

  Since FATFS is designed to not support write transactions, the accidental power loss during the erase process will cause error to partitions, which cannot be restored by simply modifying FATFS. For now, it is recommended to resolve this problem in application level by creating two identical FATFS partitions to do backups, or you can also choose a more secure file system instead, such as `LittleFS <https://github.com/joltwallet/esp_littlefs>`_ and `SafeFAT <https://www.hcc-embedded.com/safefat>`_ (charged).

--------------

How to make and flash the image of a FATFS file system?
-------------------------------------------------------------------------

  Here we will use a third-party tool, since there is no such tool provided in ESP-IDF now. The entire process shows as below:

  - Step 1: use the `mkfatfs <https://github.com/jkearins/ESP32_mkfatfs>`_ tool to create image in a specified folder. Here we create a 1048576-byte image named fat_img.bin in the file_image folder.
  
  .. code-block:: text

    ./mkfatfs -c file_image -s 1048576 ./fat_img.bin

  - Step 2: flash the image to address 0x110000:

  .. code-block:: text

    esptool.py -p /dev/ttyUSB1 -b 460800 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_size detect --flash_freq 80m 0x110000 ~/Desktop/fat_img.bin；

  - Step 3: mount the image in program:

  .. code-block:: c

    static void initialize_filesystem() { 
      static wl_handle_t
      wl_handle = WL_INVALID_HANDLE;
      const esp_vfs_fat_mount_config_t
      mount_config = { .max_files = 10, };
      ESP_LOGI(TAG, "Mounting FATfilesystem");
      esp_err_t err = esp_vfs_fat_spiflash_mount("/spiflash", "storage", &mount_config, &wl_handle);
      if (err != ESP_OK) {
          ESP_LOGE(TAG, "Failed to mount FATFS (%s)", esp_err_to_name(err));
          return;
      }
    } 


.. Note::
    The address to be flashed in step 2 must be the corresponding partition address in the partition table where FATFS is mounted, and the image created must be the same size as the one set in the partition table. Please remember to go to menuconfig and set ``Component config -> Wear Levelling -> Wear Levelling library sector size`` to 512, or the mounting would fail.

--------------

Can ESP32 use LittleFS file system?
-----------------------------------------------------

  Currently, LittleFS is not included in ESP-IDF, but there is a third-party porting component `esp_littlefs <https://github.com/joltwallet/esp_littlefs>`_ that can be used directly in ESP-IDF. You can use the `mklittlefs <https://github.com/earlephilhower/mklittlefs>`_ tool for the image of LittleFS file system.

----------------

How to check the memory usage (e.g., DRAM, IRAM, rodata) of ESP32 chips?
------------------------------------------------------------------------------------------------------------------

  You can check the usage of related memories for ESP32 chips by inputting the instruction `size-components` under corresponding directories in terminal, e.g., `make size-components` or `idf.py size-components`.

-----------------

How to read flash data for ESP8266?
-------------------------------------------------------------------------

  - You can use the script tool under ESP8266-RTOS-SDK to read flash data. The whole process is shown as follows:

    - Install python environment and the required packages;
    - Go to ESP8266_RTOS_SDK/components/esptool_py/esptool;
    - Run ``python esptool.py --chip esp8266 --port /dev/ttyUSB0 --baud 115200 read_flash 0x0 0x400000 esp8266.bin``. In this command, "esp8266.bin" is a self-defined file, where all flash data read will be stored; "/dev/ttyUSB0" is the serial port number in linux environment, which can be different in other environments and systems.

----------------

When a 8 MB PSRAM mounted on ESP32, why only 4 MB of it is actually mapped?
-----------------------------------------------------------------------------------------------------------------------

  - Up to 4 MB (0x3F80_0000 ~ 0x3FBF_FFFF) of external RAM can be mapped into data address space, please refer to the specifications of Section 3.1.4 Memory Map in `ESP32 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_.
  - You can access the other 4 MB following example `himem <https://github.com/espressif/esp-idf/tree/master/examples/system/himem>`_.

--------------------

I'm using an ESP32 development board with the official PSRAM chip PSRAM64H embedded. But after replacing another type of PSRAM chip to PSRAM64H, it failed to recognize when I ran an ESP-IDF example and enabled the PSRAM configuration. What is the reason?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - If you need to change the PSRAM chip, please update configuration options in  "menuconfig -> Component config -> ESP32-specific -> Support for external, SPI-connected RAM -> SPI RAM config -> Type of SPI RAM chip in use".
  - If you cannot find the corresponding type options of the new PSRAM chip you are about to use, please add the chip driver manually.
  - It is recommended to use Espressif's official ESP-PSRAM chip for ESP32 series.
  
---------------------

What is the available size of RTC RAM in ESP8266 for users?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The available RTC RAM in ESP8266 for users is '0x200'. Please see descriptions in `esp8266.ld <https://github.com/espressif/ESP8266_RTOS_SDK/blob/release/v3.4/components/esp8266/ld/esp8266.ld>`_.

----------------

How to deal with the file with long filename when using the FAT filesystem？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - You can change the configuration in ``menuconfig -> Component config -> FAT Filesystem support -> Long filename support`` by selecting the `Long filename buffer in heap` or `Long filename buffer on stack` option. Then you can modify the maximum length for a file name in ``Component config -> FAT Filesystem support -> Max long filename length``.

---------------

How to enable exFAT?
--------------------------------------------------------------------------------------------------

  :CHIP\: ESP32:

  - please modify #define FF_FS_EXFAT  0 as #define FF_FS_EXFAT  1 , please reffer to `ffconf.h <https://github.com/espressif/esp-idf/blob/178b122c145c19e94ac896197a3a4a9d379cd618/components/fatfs/src/ffconf.h#L255 />`_ for details.

----------------

Will the configured Wi-Fi SSID and PASSWORD disappear after the ESP series development board is powered on again and need to be reconfigured?
---------------------------------------------------------------------------------------------------------------------------------------------------------------

   - It will be stored in NVS by default and will not disappear due to power failure. You can also set it through ``esp_wifi_set_storage()``, which can be divided into two situations:

     - If you want to save the Wi-Fi SSID and PSAAWORD when powered off, you can store the Wi-Fi information in flash by calling ``esp_wifi_set_storage(WIFI_STORAGE_FLASH)``.
     - If you want to achieve the operation of not saving the Wi-Fi SSID and PASSWORD when powered off, you can call ``esp_wifi_set_storage(WIFI_STORAGE_RAM)`` to store the Wi-Fi information in RAM.
