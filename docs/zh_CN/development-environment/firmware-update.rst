固件更新
========

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

Host MCU 如何通过串口对 ESP32 进行烧录升级？
--------------------------------------------

  - 相关协议说明请参考：`ESP32 串口协议 <https://github.com/espressif/esptool/wiki/Serial-Protocol>`__
  - 示例实现代码参考：`esp-serial-flasher <https://github.com/espressif/esp-serial-flasher>`__

--------------

如何使用 USB 转串口工具对乐鑫模组进行自动烧录？
-----------------------------------------------

  USB 转串口对乐鑫模组进行自动烧录接线方式如下：

  +------------+-------+-------+-------+-------+-------+-------+
  | 乐鑫模组   | 3V3   | GND   | TXD   | RXD   | IO0   | EN    |
  +============+=======+=======+=======+=======+=======+=======+
  | 串口工具   | 3V3   | GND   | RXD   | TXD   | DTR   | RTS   |
  +------------+-------+-------+-------+-------+-------+-------+

  注：ESP8266 模组需要额外将 IO15 接地。

--------------

MacOS 与 Linux 如何烧录固件？
-----------------------------

  - 苹果系统（Mac OS）可以通过 brew 安装或 git 下载 `esptool <https://github.com/espressif/esptool>`__ 工具烧录固件。
  - Linux系统（如 ubuntu）可以通过 apt-get 安装或 git 下载 `esptool <https://github.com/espressif/esptool>`__ 工具烧录固件。

--------------

ESP32 是否支持使用 JTAG 管脚直接烧写程序？
------------------------------------------

  - ESP32 支持使用 JTAG 管脚直接烧写程序，参考文档 `JATG调试 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/jtag-debugging/index.html#jtag-upload-app-debug>`_。

--------------

ESP_Flash_Downloader_Tool 是否可以自定义编程控制？
---------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP_Flash_Downloader_Tool GUI 工具不开源，且不支持嵌入执行脚本。
  - ESP_Flash_Downloader_Tool 底层组件 ESPtool 工具开源，可以完成烧录加密等等所有功能，建议基于该组件二次开发。

---------------

ESP32 能否通过 OTA 开启 Security Boot 功能？
------------------------------------------------------------------------------------------------

  - 不推荐这样开启，因为这样操作存在风险，并且需要多次 OTA 固件。
  - 因为 Security Boot 功能存在于 Bootloader 中，所以需要更新 Bootloader 才可以开启该功能。

    - 首先检测目前设备的分区表是否可以存放开启 Security Boot 后的 Bootloader。
    - 然后更新一个支持写入 Bootloader 分区的中间固件，默认配置中无法擦写 Bootloader 分区，需要 `make menuconfig` 单独开启。
    - 再将中间固件签名后 OTA 到目标设备，运行中间固件，中间固件先进行 OTA Bootloader, 再 OTA 被签名的新固件。
    - 如果在 OTA Bootloader 时出现中途断电或者断网失败重启，设备将无法启动，需要重新烧录。

--------------

ESP32S2 固件烧录时出现错误 “A fatal error occurred: Invalid head of packet (0x50)” 如何解决？
--------------------------------------------------------------------------------------------------
  **问题背景：**

  基于 ESP-IDF v4.1 编译固件烧录到 ESP32-S2 设备的过程中遇到如下错误：

  .. code-block:: shell

    esptool.py v2.9-dev
    Serial port /dev/ttyUSB0
    Connecting....
    Chip is ESP32S2 Beta
    Features: Engineering Sample
    Crystal is 40MHz
    MAC: 7c:df:a1:01:b7:64
    Uploading stub...
    Running stub...

    A fatal error occurred: Invalid head of packet (0x50)
    esptool.py failed with exit code 2

  **解决方法：**

    如果当前使用的是 ESP32-S2 芯片而不是 ESP32-S2 Beta 芯片，需要将 ESP-IDF 升级到 v4.2 或 以上。

  **补充说明:**

  - ESP-IDF v4.1 只支持 ESP32-S2 Beta，该芯片和 ESP32-S2 是不同的芯片，无法兼容。
    ESP-IDF v4.1 自带的 esptool 的版本是 v2.9-dev，也只支持 ESP32-S2 Beta。

  - ESP-IDF v4.2 支持 ESP32-S2 芯片，该版本自带的 esptool 的版本是 v3.0-dev，支持 ESP32S2。

--------------

如何使用 flash_download_tool 下载基于 esp-idf 编译的固件？
-----------------------------------------------------------

  - 以 hello-world 例程为例，初次编译 esp-idf 工程请参考 `get-started-guide <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/get-started/index.html>`_。
  - 执行 idf.py build(esp-idf v4.0 及以后版本，v4.0 之前请使用 make) 编译工程后，会生成如下的指令提示：

    .. code-block:: 

      Project build complete. To flash, run this command:
      ../../../components/esptool_py/esptool/esptool.py -p (PORT) -b 921600 write_flash --flash_mode dio --flash_size detect --flash_freq 40m 0x10000 build/hello-world.bin  build 0x1000 build/bootloader/bootloader.bin 0x8000 build/partition_table/partition-table.bin
      or run 'idf.py -p PORT flash'

  可以按照该指令提示的 bin 文件及烧录地址使用 flash_download_tool 进行烧录。

--------------

如何查找官方AT固件的源码？
------------------------------

  - 参考 `esp-at <https://github.com/espressif/esp-at>`_。
