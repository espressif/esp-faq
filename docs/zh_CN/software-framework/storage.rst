储存
====

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

ESP32 Flash 空间与使用要求？
----------------------------

  外部 Flash 可以同时映射到 CPU 指令和只读数据空间。外部 Flash 最大可支持 16 MB。

  - 当映射到 CPU 指令空间时，一次最多可映射 11 MB + 248 KB。如果一次映射超过 3 MB + 248 KB， 则 Cache 性能可能由于 CPU 的推测性读取而降低。
  - 当映射到只读数据空间时，一次最多可以映射 4 MB。支持 8-bit、16-bit 和 32-bit 读取。

--------------

使用 ESP32 模组，如何查看模组的 PSRAM 的大小？
----------------------------------------------

  需要先在 make menuconfig 中配置开启 PSRAM 功能。PSRAM 的大小可通过 bootloader 的 log 信息或调用 esp\_spiram\_get\_size() 来查看。

--------------

ESP32 外接 PSRAM 后，如何更改 PSRAM 的 clock 来源？
---------------------------------------------------

 在 menuconfig 中修改。具体位置：menuconfig -> Component config -> ESP32-specific -> SPI RAM config。

--------------

ESP8266 是否可以搭配 TF 卡使用？
--------------------------------

  不建议这么使用。 

  - 虽然硬件上是可以连接的（通过 spi 与 TF 卡通信），但是因为 ESP8266 的资源有限，根据不同的应用场景，很可能会出现内存不足等情况。所以不建议 ESP8266 搭配 TF 卡使用。 
  - 如果您只需要单 Wi-Fi 模组，并且要连接 TF 卡，建议使用 `ESP32-S2 <https://www.espressif.com/sites/default/files/documentation/esp32-s2_datasheet_cn.pdf>`_ 芯片。

--------------

若每分钟保存或者更新数据到 flash 中，ESP32 设备的 NVS 能否满足该需求？
----------------------------------------------------------------------

  根据 `NVS 说明 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/storage/nvs_flash.html>`_，NVS 库在其操作中主要使用两个实体：页面和条目。逻辑页面对应 flash 的一个物理扇区。假设 flash 扇区大小为 4096 字节，每个页面可容纳 126 个条目(每个条目大小为 32 字节)，页面的其余部分用于页头部（32字节）和条目状态位图（32字节）。每个扇区的典型 flash 寿命为 100k 个擦除周期。假设期待设备的运行时间为 10 年，每分钟写入 flash 的数据大小为 4 字节，并且不使用 flash 加密：计算 flash 写操作的次数 60×24×365×10=5256000，在 NVS 中，会导致不超过 42k 个擦除周期(5256000/126)， 42k < 100k，因此，即使在没有多扇区影响的情况下也可以支持。在实际使用中，分配给 NVS 的大小一般为多个扇区，NVS 会在多扇区之间分配擦除周期，那么每个扇区的擦除周期的次数必然小于 42k。

  因此，NVS 可以满足该擦写需求。

--------------

ESP8266 的模组，有哪些扇区可以自主使用？
----------------------------------------

  - SDK rel3.0 之前的版本，除 bootloader 与 app bin 外还会在设置的 flash 大小的尾部会保留扇区如下：1 个存放系统信息，1 个存储 ota 信息，1 个存放 RF 校准信息。
  - SDK rel3.0 及其以后的版本使用 partition\_table 来管理 flash，除改文件自身与 bootloader 外，其余 bin 文件均在 partition\_table 标注。

--------------

NVS 是否具有磨损均衡?
---------------------

  nvs 使用的不是 esp-idf 中的 wear\_levelling 组件，而是在其内部实现的一种擦写平衡机制，使用中 flash 磨损是出于均衡状态。

--------------

NVS 扇区是否会因写入时意外断电而损坏？
--------------------------------------

  NVS 设计之初就具有抵抗意外断电的能力，因此不会损坏。

--------------

ESP32 是否可以在外挂的 SPIFLASH 中挂载文件系统分区?
---------------------------------------------------

  在 esp-idf v4.0 以及之后的版本添加了该功能。需要注意：但是挂载了两个分区时，不能多个任务同时向一个分区写入文件。

--------------

意外的断电导致 FATFS 文件系统损坏如何改善？
-------------------------------------------

  因为 FATFS 设计不支持 write transactions，因此在擦写时意外断电会导致分区错误，并且无法通过简单修改 FATFS 来修复这个问题。目前建议：可以通过创建两个相同的 FATFS 分区进行双备份来从应用层避免该问题，也可以选择使用具有更高安全性的文件系统，如：`LittleFS <https://github.com/joltwallet/esp_littlefs>`_ 和 `SafeFAT <https://www.hcc-embedded.com/safefat>`_ （收费）。

--------------

如何制作并烧录一个 FATFS 文件系统的镜像？
-----------------------------------------

  esp-idf 中未提供相关工具，需要借助第三方工具，完整示例过程如下：

  - step1：使用 **`mkfatfs <https://github.com/jkearins/ESP32_mkfatfs>`__** 工具从一个指定文件夹创建镜像，从 file\_image 文件夹创建大小为 1048576 Byte ，名为 fat\_img.bin 的镜像：
  
  .. code-block:: text

    ./mkfatfs -c file_image -s 1048576 ./fat_img.bin

  - step2：烧录镜像到 0x110000 地址：

  .. code-block:: text

    esptool.py -p /dev/ttyUSB1 -b 460800 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_size detect --flash_freq 80m 0x110000 ~/Desktop/fat_img.bin``；

  - step3：在程序中挂载：

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

  说明：这里烧录的地址一定要是分区表里 fatfs 挂载时对应分区的地址。创建的镜像需要与分区表中设置的大小一致。menuconfig 中的 ``Component config -> Wear Levelling -> Wear Levelling library sector size`` 需要设置为 512，否则挂载失败。

--------------

ESP32 是否可以使用 LittleFs 文件系统？
--------------------------------------

  目前 esp-idf 未包含 LittleFs，存在第三方移植组件 `esp\_littlefs <https://github.com/joltwallet/esp_littlefs>`_，可直接在 esp-idf 中使用。匹配 littlefs 文件系统镜像的工具 `mklittlefs <https://github.com/earlephilhower/mklittlefs>`_。

