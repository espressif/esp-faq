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
----------------------------------------------------------------------

  - 相关协议应用请参考 `ESP32 串口协议 <https://github.com/espressif/esptool>`_，对应文档说明请参考 `串口协议 <https://docs.espressif.com/projects/esptool/en/latest/esp32/advanced-topics/serial-protocol.html#serial-protocol>`_。
  - 示例实现代码请参考 `esp-serial-flasher <https://github.com/espressif/esp-serial-flasher>`_。

--------------

如何使用 USB 转串口工具对 ESP32 系列的模组下载固件？
--------------------------------------------------------------------------------

  USB 转串口对 ESP32 系列的模组下载固件的接线方式如下：

  +------------+-------+-------+-------+-------+-------+-------+
  | 乐鑫模组   | 3V3   | GND   | TXD   | RXD   | IO0   | EN    |
  +============+=======+=======+=======+=======+=======+=======+
  | 串口工具   | 3V3   | GND   | RXD   | TXD   | DTR   | RTS   |
  +------------+-------+-------+-------+-------+-------+-------+

  .. note:: ESP8266 模组需要额外将 IO15 接地。

--------------

macOS 与 Linux 如何烧录固件？
-----------------------------------------------------------------

  - 苹果系统 (macOS) 可以通过 brew 安装或 git 下载 `esptool <https://github.com/espressif/esptool>`_ 工具烧录固件。
  - Linux 系统（如 Ubuntu）可以通过 apt-get 安装或 git 下载 `esptool <https://github.com/espressif/esptool>`_ 工具烧录固件。

--------------

ESP32 是否支持使用 JTAG 管脚直接烧写程序？
-------------------------------------------------------------------------

  ESP32 支持使用 `JTAG 管脚 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/jtag-debugging/configure-other-jtag.html#id1>`_ 直接烧写程序，请参考 `上传待调试的应用程序 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/jtag-debugging/index.html#jtag-upload-app-debug>`_。

--------------

ESP_Flash_Downloader_Tool 是否支持自定义编程控制？
---------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP_Flash_Downloader_Tool GUI 工具不开源，且不支持嵌入执行脚本。
  - ESP_Flash_Downloader_Tool 底层组件 `esptool <https://github.com/espressif/esptool>`_ 开源，支持完成烧录加密等所有功能，建议基于该组件二次开发。

---------------

ESP32 能否通过 OTA 开启 Secure Boot 功能？
------------------------------------------------------------------------------------------------

  - 不推荐通过 OTA 开启 Secure Boot 功能，因为这样存在操作风险，并且需要多次 OTA 固件。
  - Secure Boot 功能存在于 Bootloader 中，需要首先更新 Bootloader 才可以启用该功能。

    1. 首先，检测目前设备的分区表是否可以存放开启 Secure Boot 后的 Bootloader。
    2. 然后，更新一个支持写入 Bootloader 分区的中间固件。默认配置中无法擦写 Bootloader 分区，需要 `make menuconfig` 单独开启。
    3. 随后，将中间固件签名后 OTA 到目标设备，运行中间固件。中间固件先进行 OTA Bootloader，再 OTA 被签名的新固件。
    4. 如果在 OTA Bootloader 时出现中途断电或者断网失败重启，设备将无法启动，需要重新烧录。

--------------

基于 ESP-IDF v4.1 编译固件烧录到 ESP32-S2 设备的过程中遇到如下错误，该如何解决？
-------------------------------------------------------------------------------------------------------------------------------------------------

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

  如果当前使用的是 ESP32-S2 芯片而不是 ESP32-S2 Beta 芯片，需要将 ESP-IDF 升级到 v4.2 或以上。

  **补充说明:**

  - ESP-IDF v4.1 只支持 ESP32-S2 Beta，该芯片和 ESP32-S2 是不同的芯片，无法兼容。
  - ESP-IDF v4.1 自带的 esptool 的版本是 v2.9-dev，也只支持 ESP32-S2 Beta。
  - ESP-IDF v4.2 支持 ESP32-S2 芯片，该版本自带的 esptool 的版本是 v3.0-dev，支持 ESP32-S2。

--------------

如何使用 flash_download_tool 下载基于 ESP-IDF 编译的固件？
--------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 初次编译 ESP-IDF 工程请参考 `get-started-guide <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/get-started/index.html>`_。
  - 以 hello-world 例程为例，运行 ``idf.py build``（支持 ESP-IDF v4.0 及以后版本，v4.0 之前版本请使用 ``make``）。编译工程后，会生成如下的 bin 文件的烧录指令提示：

  .. code:: shell

    #Project build complete. To flash, run this command:
    ../../../components/esptool_py/esptool/esptool.py -p (PORT) -b 921600 write_flash --flash_mode dio --flash_size detect --flash_freq 40m 0x10000 build/hello-world.bin  build 0x1000 build/bootloader/bootloader.bin 0x8000 build/partition_table/partition-table.bin
    or run 'idf.py -p PORT flash'

  可以按照该指令提示的 bin 文件及烧录地址使用 flash_download_tool 进行烧录。

--------------

ESP 芯片烧录通讯协议是什么？
------------------------------------------------------------------------------

  - ESP 烧录协议规范：`Serial Protocol <https://docs.espressif.com/projects/esptool/en/latest/esp32/advanced-topics/serial-protocol.html>`__。
  - 串口协议 Python 实现：`esptool <https://github.com/espressif/esptool>`_。
  - 串口协议 C 语言实现：`esp-serial-flasher <https://github.com/espressif/esp-serial-flasher>`_。

--------------

如何对 ESP32-C3 进行固件离线烧录？
------------------------------------------------------------------------------------------

  - 目前没有任何工具支持 ESP32-C3 固件离线烧录。但官方发布的 `Flash 下载工具 <https://www.espressif.com/zh-hans/support/download/other-tools>`_ 可以直接烧录二进制固件，且支持量产烧录模式，最多支持 8 个 ESP32-C3 设备同时下载固件。
  - 另外，官方也提供了用于量产生产的 `治具 <https://www.espressif.com/zh-hans/products/equipment/production-testing-equipment/overview>`_，最多支持 4 个 ESP32-C3 模组同时下载固件。

--------------

ESP32 如何设置 Flash SPI 模式为 QIO 模式？
---------------------------------------------------------------------------------------------

  可前往 menuconfig，通过 ``Serial flasher config`` > ``Flash SPI mode`` 配置端进行设置，对应 API 为 `esp_image_spi_mode_t() <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.4/esp32/api-reference/system/app_image_format.html?highlight=esp_image_spi_mode_t#_CPPv420esp_image_spi_mode_t>`_。

----------------------

使用 ESP8266 开发板下载程序后，上电启动串口打印如下日志，是什么原因？
-------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    ets Jan  8 2013,rst cause:1, boot mode:(7,7)
    waiting for host

  打印 `waiting for host` 说明 Boot 模式是 SDIO 模式，表明 GPIO15 (MTDO) 被拉高，请参见 `ESP8266 Boot 模式说明 <https://github.com/esp8266/esp8266-wiki/wiki/Boot-Process>`_。

----------------

乐鑫模组烧录工具有哪些？
-----------------------------------------------------------

  - 请前往 `Flash 下载工具 <https://www.espressif.com/zh-hans/support/download/other-tools>`_ 下载乐鑫烧录工具。免安装 GUI 工具，仅适用于 ``Windows`` 环境。
  - 乐鑫烧录工具 `esptool <https://github.com/espressif/esptool>`_ 基于 `python` 编写，开放源代码，并且支持用户二次开发。

--------------------------------------------------------------------------------------------------------------------------------------------------------

`Flash 下载工具 <https://www.espressif.com/zh-hans/support/download/other-tools>`_ 的工厂模式和开发者模式有什么区别？
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 工厂模式支持多通道下载，开发者模式仅支持单通道。
  - 工厂模式下 bin 文件的路径是相对路径，开发者模式下的路径是绝对路径。

----------------------

ESP32-C3 芯片可以使用 USB 进行固件下载，但在 ESP-IDF v4.3 下使用并不支持，如何使用 USB 进行固件下载？
--------------------------------------------------------------------------------------------------------------------------------------------------------------

  需要在 ESP-IDF v4.4 以上版本下进行编译。拉取最新分支并 `更新 IDF 工具 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/get-started/index.html>`_ 后可以正常编译并使用 USB 进行下载。使用过程请参考 `usb-serial-jtag-console <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/api-guides/usb-serial-jtag-console.html>`_。

---------------

一拖四治具工厂模式烧写失败是什么原因？
---------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32 | ESP8266  :

  - 乐鑫产品启动时会通过一些发包来完成校准操作，此操作需要 3.3 V 电压并保证有 500 mA 的峰值电流。所以，在一拖多的情况下，通过连接电脑 USB 的方式来烧录时，会出现由于电脑 USB 供电不足而引起无法烧录或者烧录中断的情况，建议使用 hub 进行烧录并给 hub 供电。

------------

使用 ESP32-WROVER-B 模组通过 `Flash 下载工具 <https://www.espressif.com/zh-hans/support/download/other-tools>`_ 下载 AT 固件，当完成写 flash 后，结果显示 ERROR。但使用 ESP32-WEOVER-E 的模组下载相同的 AT 固件结果却显示正常，是什么原因？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP32-WROVER-B 模组引出了 SPI flash 的管脚，但 ESP32-WROVER-E 模组没有引出 SPI flash 的管脚，请先检查 ESP32-WROVER-B 模组的 SPI flash 引脚是否被外部其他应用电路复用。
  - ESP32-WROVER-B 的 SPI flash 的 CMD 引脚接 GND 会导致 flash 无法启动，报错将打印如下日志：

  .. code:: shell

    rst:0x10 (RTCWDT_RTC_RESET),boot:0x1b (SPI_FAST_FLASH_BOOT)
    flash read err, 1000
    ets_main.c 371
    ets Jun  8 2016 00:22:57

---------------

为什么使用 `flash 下载工具 <https://www.espressif.com/zh-hans/support/download/other-tools>`_ 无法对已开启 flash 加密但未禁用下载模式的设备重新烧录固件？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32 | ESP32-S2:

  - flash 下载工具的默认配置开启了 eFuse 校验，若希望对已经开启 flash 加密的设备重烧固件，需要修改如下配置：

    - 修改 `esp32 > security.conf` 文件里的默认配置，将 `flash_force_write_enable = False` 改为 `flash_force_write_enable = True`。
    - 修改 `esp32 > spi_download.conf` 文件里的默认配置，将 `no_stub = False` 改为 `no_stub = True`。
  
  - 注意：对已开启 flash 加密的设备重烧固件，要求重烧的固件使用相同的 flash 加密密钥。若 flash 加密密钥不匹配，将无法正常运行新固件。

--------------

基于 `esptool 串口协议 <https://github.com/espressif/esptool>`_ 通过 UART 接口对 ESP32 进行刷新固件，是否可以新增一个 app 分区？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - flash 实际的分区情况主要取决于 partition_table.bin 的数据。若可以更新 partition_table.bin，则可以重新划分 bootloader.bin、app.bin 等其他数据的存储空间，从而新增一个 app 分区。

-------------

使用 ESP8266 通过 `Flash 下载工具 <https://www.espressif.com/zh-hans/support/download/other-tools>`_ 下载程序固件后无程序运行日志输出，串口打印如下，是什么原因？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: shell

    ets Jan  8
    2013,rst cause:1, boot mode:(3,7)
    ets_main.c

  - 请先检查硬件接线是否正确。参见 `Boot mode 接线说明 <https://docs.espressif.com/projects/esptool/en/latest/esp8266/advanced-topics/boot-mode-selection.html>`_。
  - 请检查 bootloader.bin 的下载偏移地址是否正确，ESP8266 的 bootloader.bin 下载的偏移地址为 0x0，若此偏移地址错误将会导致 flash 无法启动。

----------------

Windows 7 系统 USB 驱动无法识别是什么原因？
--------------------------------------------------------------------------------------------------------------------------------------------

  - Windows 7 系统需要手动下载并安装 `USB Serial JTAG 驱动 <https://dl.espressif.com/dl/idf-driver/idf-driver-esp32-usb-jtag-2021-07-15.zip>`_。

----------------

使用 ESP32-WROVER-E 模组下载程序后，上电打印日志如下，是什么原因？
---------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: shell

      rst：0x10 （RTCWDT_RTC_RESET），boot:0x37（SPI_FLASH_BOOT）
    【2020-12-11 15:51:42 049】invalrd header：0xffffffff
      invalrd header：0xffffffff
      invalrd header：0xffffffff

  - 出现如上报错日志一般情况为 GPIO12 拉高导致，ESP32-WROVER-E 模组 GPIO12 不能拉高，建议将 GPIO12 拉低测试一下。可参见 `ESP32 boot log 指南 <https://docs.espressif.com/projects/esptool/en/latest/esp32/advanced-topics/boot-mode-selection.html#select-bootloader-mode>`_。

----------------

使用 `Flash 下载工具 <https://www.espressif.com/zh-hans/support/download/other-tools>`_ 通过 USB 烧录 ESP32-C3 时，反复出现 8-download data fail，如何解决？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 请先完全擦除芯片，再进行烧录
  - V3.9.4 及以上版本已修复该问题

--------------

ESP32 使用 ESP-IDF v3.0 版本的 bootloader.bin 无法正常启动 ESP-IDF v5.0 版本的 app.bin，是什么原因？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 当使用 ESP-IDF v3.0 版本的 bootloader.bin 启动 ESP-IDF v5.0 版本的 app.bin 时，需要在 ESP-IDF v5.0 上开启 ``idf.py menuconfig`` > ``Build type`` > ``[*] App compatible with bootloader and partition table before ESP-IDF v3.1`` 配置选项。

------------

ESP32-C3 是否支持通过 OTA 来关闭 ROM 代码日志？
----------------------------------------------------------------------------------------------------------------------------------------------------------------

  支持。通过在软件上开启 `Boot ROM Behavior → Permanently change Boot ROM output → (X) Permanently disable logging` 配置来关闭 ROM 代码日志，然后 OTA 新的固件即可。

--------------

芯片在进行 OTA 固件升级 (`esp_ota_write() <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/system/ota.html#_CPPv413esp_ota_write16esp_ota_handle_tPKv6size_t>`_ ) 时，是否会影响到其他任务的运行？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  在 OTA 升级过程中，写入 flash 时会关闭 cache，这会影响外设中断和部分 SPI 任务。因此，在此期间不建议执行其他任务。
