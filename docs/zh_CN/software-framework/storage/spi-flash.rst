SPI Flash
=========

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
---------------------------------------

  外部 flash 可以同时映射到 CPU 指令和只读数据空间。ESP32 外部 flash 最大可支持 16 MB。

  - 当映射到 CPU 指令空间时，一次最多可映射 11 MB + 248 KB。如果一次映射超过 3 MB + 248 KB， 则 Cache 性能可能由于 CPU 的推测性读取而降低。
  - 当映射到只读数据空间时，一次最多可以映射 4 MB。支持 8-bit、16-bit 和 32-bit 读取。
  - 需要在编写代码时指定 flash 分区表，即将 flash 划分为不同的分区，如 app 分区、data 分区、OTA 分区等，并指定每个分区的大小和偏移地址
  - 在使用 flash 时，需要注意 flash 的使用寿命问题。由于 flash 的擦写次数有限，需要合理规划和管理 flash 的使用，例如使用 wear leveling 等技术来延长 flash 的寿命。
  - 在使用 flash 时，需要注意 flash 写操作会占用 CPU 时间，可能会影响系统的响应速度，因此需要尽量减少 flash 写操作的频率。

--------------

ESP8266 的模组，有哪些扇区可以自主使用？
------------------------------------------------

  - SDK rel3.0 之前的版本，除 bootloader 与 app bin 外还会在设置的 flash 大小的尾部会保留扇区如下：1 个存放系统信息，1 个存储 OTA 信息，1 个存放 RF 校准信息。
  - SDK rel3.0 及其以后的版本使用 partition_table 来管理 flash，除该文件自身与 bootloader 外，其余 bin 文件均在 partition_table 标注。

--------------

ESP8266 如何读取 flash 数据？
-------------------------------------------------------------------------

  - 可使用 ESP8266-RTOS-SDK 下的脚本工具读 flash ，读 flash 方式如下：

    - 安装 python 环境以及工具依赖的包文件；
    - 进入 ESP8266_RTOS_SDK/components/esptool_py/esptool 路径下；
    - 执行 ``python esptool.py --chip esp8266 --port /dev/ttyUSB0 --baud 115200 read_flash 0x0 0x400000 esp8266.bin``。该命令中 "esp8266.bin" 为自定义名称，读取到的 flash 数据将会生成名为 "esp8266.bin" 的文件，命令中 "/dev/ttyUSB0" 为 linux 环境中的串口号，其他环境以及系统中会有不同。

----------------

不同的 ESP32 模组为何出现 flash 擦除时间不一致？
----------------------------------------------------------------------------------------------------------------------------------------------

  - 不同的 ESP32 模组可能具有不同的 flash 芯片或 flash 控制器，这些硬件组件可能会对擦除时间产生影响，部分型号的 flash 进行擦除时没有空块跳过的机制，所以耗时较长。具体而言，不同的 flash 芯片可能具有不同的擦除时间，例如 SPI flash 和 QSPI flash 具有不同的擦除时间，即使是同一类型的 flash 芯片也可能存在不同的擦除时间，这取决于其封装和生产批次等因素。此外，不同的 flash 控制器的设计和性能也可能对擦除时间产生影响。因此，不同的 ESP32 模组可能会使用不同的 flash 芯片或 flash 控制器，从而导致擦除时间的不一致。

------------------

使用 ESP32-S3-WROOM-2-32R8V 模组，设置 flash SPI mode 为 QIO 模式，固件运行时打印如下错误是什么原因？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    E (47) qio_mode: Failed to set QIE bit, not enabling QIO mode

  ESP32-S3-WROOM-2-32R8V 模组使用的是 32 MB Octal SPI flash 和 8 MB Octal SPI RAM。请在配置选项中开启 Octal SPI flash 和 Octal PSRAM 的设置：
  
  - ``(Top)`` > ``Serial flasher config`` > ``[*] Enable Octal Flash`` > ``Flash SPI mode (OPI)``
  - ``(Top)`` > ``Component config`` > ``ESP PSRAM`` > ``Support for external, SPI-connected RAM`` > ``SPI RAM config`` > ``Mode (QUAD/OCT) of SPI RAM chip in use``

----------------

如何判断 ESP-IDF 是否已经支持某款 flash？ 
----------------------------------------------------------------------------------------------------------------------------------------------

  - 可以参考 `Optional features for flash <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/spi_flash/spi_flash_optional_feature.html#optional-features-for-flash>`__ 来进一步了解 ESP-IDF 支持的 flash 信息，需要注意的是，此文档仅说明 ESP-IDF 代码已支持这些 flash 的特性，并不是乐鑫认证的稳定 flash 列表。
  - 如需要 flash 选型的进一步支持，可以联系 `乐鑫商务 <https://www.espressif.com/zh-hans/contact-us/sales-questions>`_。

  
-----------------

基于 ESP32-S3 芯片外接 SPI flash，支持单次写入的数据量是多大？
-------------------------------------------------------------------------------------------------------------------------

  - ESP32-S3 硬件限制外接 SPI flash 只允许单次写入最大 64 字节数据。
