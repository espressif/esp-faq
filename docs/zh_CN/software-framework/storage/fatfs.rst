FAT 文件系统
=============

:link_to_translation:`en:[English]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

--------------

意外的断电导致 FatFs 文件系统损坏如何改善？
--------------------------------------------------------

  因为 FatFs 设计不支持 write transactions，因此意外断电可能会导致分区错误，并且无法通过简单修改 FatFs 来修复这个问题。目前建议：可以通过创建两个相同的 FatFs 分区进行双备份来从应用层避免该问题，也可以选择使用具有更高安全性的文件系统，如：`LittleFS <https://github.com/joltwallet/esp_littlefs>`_ 和 `SafeFAT <https://www.hcc-embedded.com/safefat>`_ （收费）。

--------------

如何制作并烧录一个 FatFs 文件系统的镜像？
------------------------------------------------------

  ESP-IDF 中未提供相关工具，需要借助第三方工具，完整示例过程如下：

  - 第一步：使用 `mkfatfs <https://github.com/jkearins/ESP32_mkfatfs>`_ 工具从一个指定文件夹创建镜像，例如从 file_image 文件夹创建大小为 1048576 Byte、名为 fat_img.bin 的镜像：
  
  .. code-block:: text

    ./mkfatfs -c file_image -s 1048576 ./fat_img.bin

  - 第二步：烧录镜像，例如烧录到 0x110000 地址：

  .. code-block:: text

    esptool.py -p /dev/ttyUSB1 -b 460800 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_size detect --flash_freq 80m 0x110000 ~/Desktop/fat_img.bin；

  - 第三步：在程序中挂载：

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
    这里烧录的地址一定要是分区表里 FatFs 对应分区的地址，创建的镜像需要与分区表中设置的大小一致。menuconfig 中的 ``Component config`` > ``Wear Levelling`` > ``Wear Levelling library sector size`` 需要设置为 512，否则将导致挂载失败。

--------------

FATFS 与 SPIFFS 这两种文件系统有何差异，我们怎么选择?
----------------------------------------------------------------

  请参考 `文件系统 <https://github.com/espressif/esp-iot-solution/blob/master/docs/zh_CN/storage/file_system.rst>`_。

--------------

FatFs 支持的最大容量是多少?
----------------------------------------------------------------

  FAT32 文件系统最大支持 2 TB 的容量，但是由于部分操作系统的限制（例如 Windows），目前 FatFs 普遍最大只在 32 GB 的存储设备上使用。大于 32 GB 的存储设备，一般默认会使用 exFAT 等文件系统。

--------------

使用 FAT 文件系统时，文件名稍微长一点的文件无法打开，该如何处理？
--------------------------------------------------------------------------------------------------------------------------------------------------

  可以在 ``menuconfig`` -> ``Component config`` -> ``FAT Filesystem support`` -> ``Long filename support 中进行修改，选择 ``Long filename buffer in heap`` 或 ``Long filename buffer on stack`` 配置项。然后可以在 ``Component config`` -> ``FAT Filesystem support`` -> ``Max long filename length`` 中修改最大的文件名长度。

----------------------------------------------------------------------

使用 `ext_flash_fatfs <https://github.com/espressif/esp-idf/tree/master/examples/storage/ext_flash_fatfs>`_ 示例测试，分区表中将 fatffs 分区设置小于 512 KB 时，会报 ``vfs_fat_spiflash:f_mks failed(14),config:Failed to mount FATFS(ESP_FAIL)`` 错误，如何解决？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  FAT 分区的最小扇区数是 128，所以文件系统的最小尺寸是 128*4+4*4=528 KB，额外的 4 个扇区需要用于磨损均衡信息，所以至少需要保证 fatffs 分区 size 不小于 528 KB。
