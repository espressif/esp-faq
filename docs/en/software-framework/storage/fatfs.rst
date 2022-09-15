FAT Filesystem
==============

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

How to improve the damage to FatFs file system caused by accidental power loss?
-----------------------------------------------------------------------------------------------------

  Since FatFs is designed to not support write transactions, the accidental power loss during the erase process will cause error to partitions, which cannot be restored by simply modifying FatFs. For now, it is recommended to resolve this problem in application level by creating two identical FatFs partitions to do backups, or you can also choose a more secure file system instead, such as `LittleFS <https://github.com/joltwallet/esp_littlefs>`_ and `SafeFAT <https://www.hcc-embedded.com/safefat>`_ (charged).

--------------

How to make and flash the image of a FatFs file system?
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
    The address to be flashed in step 2 must be the corresponding partition address in the partition table where FatFs is mounted, and the image created must be the same size as the one set in the partition table. Please remember to go to menuconfig and set ``Component config -> Wear Levelling -> Wear Levelling library sector size`` to 512, or the mounting would fail.

--------------

What are the differences between the two file systems, FatFs and SPIFFS, and how do we choose?
---------------------------------------------------------------------------------------------------------------------------------

  Please refer to `File System <https://github.com/espressif/esp-iot-solution/blob/master/docs/en/storage/file_system.rst>`.

--------------

What is the maximum size supported by FatFs?
--------------------------------------------------------------------------

  Due to the limitations of the Windows system, FatFs is currently generally only available on storage devices up to 32 GB. Storage devices larger than 32 GB use other file systems, such as exFAT.
