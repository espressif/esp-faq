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

ESP32 flash 空间与使用要求是什么？
--------------------------------------

  外部 flash 可以同时映射到 CPU 指令和只读数据空间。外部 flash 最大可支持 16 MB。

  - 当映射到 CPU 指令空间时，一次最多可映射 11 MB + 248 KB。如果一次映射超过 3 MB + 248 KB， 则 Cache 性能可能由于 CPU 的推测性读取而降低。
  - 当映射到只读数据空间时，一次最多可以映射 4 MB。支持 8-bit、16-bit 和 32-bit 读取。

--------------

使用 ESP32 模组，如何查看模组的 PSRAM 的大小？
-------------------------------------------------------

  需要先在 ``make menuconfig`` 中配置开启 PSRAM 功能。PSRAM 的大小可通过 bootloader 的 log 信息或调用 esp_spiram_get_size() 来查看。

--------------

ESP32 外接 PSRAM 后，如何更改 PSRAM 的 clock 来源？
----------------------------------------------------------

  在 menuconfig 中修改。具体位置：menuconfig -> Component config -> ESP32-specific -> SPI RAM config。

--------------

ESP8266 是否可以搭配 TF 卡使用？
----------------------------------------

  不建议这么使用。 

  - 虽然硬件上是可以连接的（通过 SPI 与 TF 卡通信），但是因为 ESP8266 的资源有限，根据不同的应用场景，很可能会出现内存不足等情况。所以不建议 ESP8266 搭配 TF 卡使用。 
  - 如果您只需要单 Wi-Fi 模组，并且要连接 TF 卡，建议使用 `ESP32-S2 <https://www.espressif.com/sites/default/files/documentation/esp32-s2_datasheet_cn.pdf>`_ 芯片。

--------------

若每分钟保存或者更新数据到 flash 中，ESP32 设备的 NVS 能否满足该需求？
----------------------------------------------------------------------------------

  根据 `NVS 说明 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/storage/nvs_flash.html>`_，NVS 库在其操作中主要使用两个实体：页面和条目。逻辑页面对应 flash 的一个物理扇区。假设 flash 扇区大小为 4096 字节，每个页面可容纳 126 个条目（每个条目大小为 32 字节），页面的其余部分用于页头部（32 字节）和条目状态位图（32 字节）。每个扇区的典型 flash 寿命为 100 k 个擦除周期。假设期待设备的运行时间为 10 年，每分钟写入 flash 的数据大小为 4 字节，并且不使用 flash 加密，计算 flash 写操作的次数为：60×24×365×10=5256000。这样，在 NVS 中会导致不超过 42 k 个擦除周期 (5256000/126)，而 42 k < 100 k，因此，即使在没有多扇区影响的情况下也可以支持。在实际使用中，分配给 NVS 的大小一般为多个扇区，NVS 会在多扇区之间分配擦除周期，那么每个扇区的擦除周期的次数必然小于 42 k。

  因此，NVS 可以满足该擦写需求。

--------------

ESP8266 的模组，有哪些扇区可以自主使用？
------------------------------------------------

  - SDK rel3.0 之前的版本，除 bootloader 与 app bin 外还会在设置的 flash 大小的尾部会保留扇区如下：1 个存放系统信息，1 个存储 OTA 信息，1 个存放 RF 校准信息。
  - SDK rel3.0 及其以后的版本使用 partition_table 来管理 flash，除该文件自身与 bootloader 外，其余 bin 文件均在 partition_table 标注。

--------------

NVS 是否具有磨损均衡？
----------------------------

  NVS 使用的不是 ESP-IDF 中的 wear_levelling 组件，而是在其内部实现的一种擦写平衡机制，使用中 flash 磨损是处于均衡状态。

--------------

NVS 扇区是否会因写入时意外断电而损坏？
------------------------------------------------

  NVS 设计之初就具有抵抗意外断电的能力，因此不会损坏。

--------------

ESP32 是否可以在外挂的 SPI flash 中挂载文件系统分区？
---------------------------------------------------------------

  在 ESP-IDF v4.0 以及之后的版本添加了该功能。需要注意的是，当挂载了两个分区时，不能多个任务同时向一个分区写入文件。

--------------

意外的断电导致 FATFS 文件系统损坏如何改善？
-------------------------------------------------------

  因为 FATFS 设计不支持 write transactions，因此在擦写时意外断电会导致分区错误，并且无法通过简单修改 FATFS 来修复这个问题。目前建议：可以通过创建两个相同的 FATFS 分区进行双备份来从应用层避免该问题，也可以选择使用具有更高安全性的文件系统，如：`LittleFS <https://github.com/joltwallet/esp_littlefs>`_ 和 `SafeFAT <https://www.hcc-embedded.com/safefat>`_ （收费）。

--------------

如何制作并烧录一个 FATFS 文件系统的镜像？
------------------------------------------------------

  ESP-IDF 中未提供相关工具，需要借助第三方工具，完整示例过程如下：

  - 第一步：使用 `mkfatfs <https://github.com/jkearins/ESP32_mkfatfs>`_ 工具从一个指定文件夹创建镜像，从 file_image 文件夹创建大小为 1048576 Byte、名为 fat_img.bin 的镜像：
  
  .. code-block:: text

    ./mkfatfs -c file_image -s 1048576 ./fat_img.bin

  - 第二步：烧录镜像到 0x110000 地址：

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
    这里烧录的地址一定要是分区表里 FATFS 挂载时对应分区的地址，创建的镜像需要与分区表中设置的大小一致。menuconfig 中的 ``Component config -> Wear Levelling -> Wear Levelling library sector size`` 需要设置为 512，否则将导致挂载失败。

--------------

ESP32 是否可以使用 LittleFS 文件系统？
--------------------------------------------------

  目前 ESP-IDF 未包含 LittleFS，存在第三方移植组件 `esp_littlefs <https://github.com/joltwallet/esp_littlefs>`_，可直接在 ESP-IDF 中使用。匹配 LittleFS 文件系统镜像的工具为 `mklittlefs <https://github.com/earlephilhower/mklittlefs>`_。

----------------

ESP32 如何查看芯片内存（例如：DRAM、IRAM、rodata）使用情况？
------------------------------------------------------------------------------------------------------------------

  可以在工程终端目录下输入 `size-components` 指令来查看相关内存使用情况，如 `make size-components` 或 `idf.py size-components`。

-----------------

ESP8266 如何读取 flash 数据？
-------------------------------------------------------------------------

  - 可使用 ESP8266-RTOS-SDK 下的脚本工具读 flash ，读 flash 方式如下：

    - 安装 python 环境以及工具依赖的包文件；
    - 进入 ESP8266_RTOS_SDK/components/esptool_py/esptool 路径下；
    - 执行 ``python esptool.py --chip esp8266 --port /dev/ttyUSB0 --baud 115200 read_flash 0x0 0x400000 esp8266.bin``。该命令中 "esp8266.bin" 为自定义名称，读取到的 flash 数据将会生成名为 "esp8266.bin" 的文件，命令中 "/dev/ttyUSB0" 为 linux 环境中的串口号，其他环境以及系统中会有不同。

----------------

ESP32 模组挂载 8 MB PSRAM, 为何实际映射的只有 4 MB？
---------------------------------------------------------------------

  - 使用 ESP32 芯片建议搭配使用官方 ESP-PSRAM 芯片。
  - 片外 RAM 最大可映射 4 MB (0x3F80_0000 ~ 0x3FBF_FFFF) 到数据地址空间，可参考 `ESP32 技术规格书 <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf>`_ 中 3.1.4 节存储器映射的说明。
  - 可参考例程 `himem <https://github.com/espressif/esp-idf/tree/master/examples/system/himem>`_ 访问其余的 4 MB 空间。

-----------------

使用 ESP32 开发板，上面用了官方 PSRAM 芯片 PSRAM64H，当更换了另一个型号的 PSRAM 芯片后，运行 ESP-IDF 的例程并开启 PSRAM 配置，却无法正常识别，是什么原因？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 更换 PSRAM 芯片的型号，需要在 menuconfig -> Component config -> ESP32-specific -> Support for external, SPI-connected RAM -> SPI RAM config -> Type of SPI RAM chip in use 中修改相应配置选项。
  - 若更换的 PSRAM 芯片型号在 menuconfig 中没有相应的配置选项，则需要自行加入 PSRAM 芯片的驱动。

----------------

ESP8266 用户可用的 RTC RAM 是多大？
----------------------------------------------------------------------------------------------

  - ESP8266 用户可用的 RTC RAM 为 0x200。可参见 `esp8266.ld <https://github.com/espressif/ESP8266_RTOS_SDK/blob/release/v3.4/components/esp8266/ld/esp8266.ld>`_ 文件说明。