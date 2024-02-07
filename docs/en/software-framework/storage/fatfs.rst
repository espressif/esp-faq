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
------------------------------------------------------------------------------------------------------

  Since FatFs is designed to not support write transactions, the accidental power loss may cause error to partitions, which cannot be restored by simply modifying FatFs. For now, it is recommended to resolve this problem in application level by creating two identical FatFs partitions to do backups, or you can also choose a more secure file system instead, such as `LittleFS <https://github.com/joltwallet/esp_littlefs>`_ and `SafeFAT <https://www.hcc-embedded.com/safefat>`_ (charged).

--------------

How to make and flash the image of a FatFs file system?
-------------------------------------------------------------------------

  Here we will use a third-party tool, since there is no such tool provided in ESP-IDF now. The entire process shows as below:

  - Step 1: Use the `mkfatfs <https://github.com/jkearins/ESP32_mkfatfs>`_ tool to create an image from a specified folder, for example, create an image named fat_img.bin with a size of 1048576 Bytes from the file_image folder:
  
  .. code-block:: text

    ./mkfatfs -c file_image -s 1048576 ./fat_img.bin

  - Step 2: Flash the image, for example, flash it to 0x110000:

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
    The address to be flashed in step 2 must be the corresponding partition address in the partition table, and the created image must be the same size as the one set in the partition table. Please remember to go to menuconfig and set ``Component config`` > ``Wear Levelling`` > ``Wear Levelling library sector size`` to 512, otherwise it will cause a mounting failure.

--------------

What are the differences between the two file systems, FatFs and SPIFFS, and how do we choose?
---------------------------------------------------------------------------------------------------------------------------------

  Please refer to `File System <https://github.com/espressif/esp-iot-solution/blob/master/docs/en/storage/file_system.rst>`.

--------------

What is the maximum size supported by FatFs?
--------------------------------------------------------------------------

  The FAT32 file system supports a maximum capacity of 2 TB. However, due to the limitations of some operating systems (such as Windows), FatFs is generally only used on storage devices up to 32 GB. For storage devices larger than 32 GB, file systems like exFAT are typically used by default.

---------------

I cannot open the files with long names when I use the FAT file system. How can I fix this issue?
------------------------------------------------------------------------------------------------------

  - You can modify this in ``menuconfig`` > ``Component config`` > ``FAT Filesystem support`` > ``Long filename support``, and choose either the ``Long filename buffer in heap`` or ``Long filename buffer on stack``. Then, you can change the maximum filename length in ``Component config`` > ``FAT Filesystem support`` > ``Max long filename length``.

-----------------------------------------------------------------------

When I used the `ext_flash_fatfs <https://github.com/espressif/esp-idf/tree/master/examples/storage/ext_flash_fatfs>`_ example to test, I encountered an error ``vfs_fat_spiflash :f_mks failed(14),config:Failed to mount FATFS(ESP_FAIL)`` if I set the fatffs partition to less than 512 KB. How can I solve it?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  A FAT partition has 128 sectors at the minimum, so the minimum size of the file system should be 128*4+4*4=528 KB. The extra four sectors are used for wear leveling information. As a result, the size of the fatffs partition must not be less than 528 KB.
