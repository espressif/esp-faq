SPI 控制器
============

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

ESP-WROOM-02D 模块是否可以外接 SPI flash？
-----------------------------------------------------

  ESP-WROOM-02D 模组是一款基于 ESP8266 芯片的 Wi-Fi 模组，支持使用 SPI 接口与外部 SPI flash 设备进行通信。具体来说，ESP-WROOM-02D 模组提供了 4 个 SPI 接口引脚（GPIO12、GPIO13、GPIO14 和 GPIO15），其中 GPIO12~GPIO14 可以用作 SPI 主机接口的 MISO、 MOSI、和 SCLK 引脚，而 GPIO15 则可以用作 SPI 从机接口的 CS 引脚。

  要使用 ESP-WROOM-02D 模组连接外部 SPI flash 设备，需要将 SPI flash 设备的 MOSI、MISO、SCK 和 CS 引脚分别连接到 ESP-WROOM-02D 模组的 GPIO12~GPIO14 和 GPIO15 引脚上。同时，还需要在 ESP8266 的固件中正确配置和初始化 SPI 接口，以便能够正确地与外部 SPI flash 设备进行通信。

  需要注意的是，外接 SPI flash 设备的型号和容量等参数需要根据具体的应用场景和需求进行选择，同时需要特别关注 SPI flash 设备的时序特性和可靠性，以保证数据传输的正确性和稳定性。此外，还需要考虑 SPI flash 设备和 ESP-WROOM-02D 模组之间的物理距离和噪声环境等因素对通信质量的影响，尽可能采取合适的措施来提高系统的可靠性和性能。

--------------

ESP-WROOM-S2 作为从机，STM32 作为 MCU ，可以使⽤ SPI 接⼝下载吗？
-------------------------------------------------------------------------

  不可以，默认下载功能仅支持串口 UART0，固件启动后可应用中使能其他外设，在应用中⾃⾏设计⽀持 OTA 功能。

--------------

ESP32 中 SPI0/SPI1/HSPI/VSPI 三者有什么区别呢？
-------------------------------------------------------------

  - ESP32 有 4 组 SPI，SPI0 和 SPI1 是两个外设，统称为 MSPI。其中 MSPI CS0 连接储存程序的 flash， MSPI CS1 连接 PSRAM，SPI0 和 SPI1 共用一组 GPIO 接口，默认被占用；剩下的两组 SPI2 和 SPI3 为可供客户自由使用的通用 SPI。
  - HSPI 代表上述 SPI2，VSPI 代表上述 SPI3，这两组 SPI 均为通用 SPI，并且都支持 QSPI。

--------------

ESP 系列芯片使用 SPI DMA 时最大的数据传输量是 4095 字节，是因为硬件限制吗？
----------------------------------------------------------------------------------------------------------------------------------------------

  - 是的，这属于硬件限制，DMA 链表中单个节点只能挂载 4095 字节的数据。
  - 但是 SPI DMA 单次发送可以通过若干节点来挂载更多的数据，此时最大的数据传输字节数受限于硬件寄存器 ``SPI_LL_DATA_MAX_BIT_LEN``（不同系列芯片的数值不同，可在 ESP-IDF 中搜索到），即 ``max_transfer_sz <= (SPI_LL_DATA_MAX_BIT_LEN / 8)``。

-----------------

ESP 系列芯片的 SPI 同时访问三个 SPI 从机设备，是否需要做信号量同步才能访问？
------------------------------------------------------------------------------------------------------------------------------

  - 同一个 SPI 外设作为主机，一次只能与一个从机进行通信，由 CS 决定与哪个从机进行通信。如果是给 SPI 驱动挂 3 个 从机设备，并与它们分别通信的话是可以的，推荐这种用法。
  - 推荐只在一个任务中操作共用同一个 SPI 的设备，否则是线程不安全的，需要通过信号量同步进行通信，具体问题见 `SPI 主机驱动程序 - 主机驱动特性 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/peripherals/spi_master.html#id2>`_。

---------------------

使用 ESP32 开发板基于 ESP-IDF release/v4.3 版本的 SDK 进行开发测试，软件编译报错如下，是什么原因？
------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    spi_flash:Detected size(8192K) smaller than the size in the binary image header(16384K).Probe failed.

  原因是配置的 flash 大小比实际使用的 flash 大小要大，为避免误用更大的地址空间而对实际使用的 flash 大小进行检测。

----------------

SPI 从机支持最大速度是多少？
-------------------------------------------------------------------------------
  :CHIP\: ESP32:

  ESP32 作为 SPI 从机时钟最高只支持到 10 M。

-------------------------

使用 ESP 系列芯片作为 SPI 主机设备，在非 DMA 模式下最大可一次性传输多少字节的数据？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 受 SPI 硬件 FIFO 的限制，在非 DMA 模式下最大可一次性传输 64 字节，可参考 `SPI 主机驱动程序 - 传输事务持续时间 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/peripherals/spi_master.html#id18>`__。
  - 当传输不超过 32 比特时，可以使用 SPI Master 驱动内部的 4 字节数组作为发送数据的缓冲区，可参考 `SPI 主机驱动程序 - 传输数据小于 32 位的传输事务 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/peripherals/spi_master.html#id13>`_ 说明。
  - 当传输超过 32 比特时，需要自行创建 SPI 发送数据的缓冲区，可参考 `SPI 主机驱动程序 - SPI 传输事务 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/peripherals/spi_master.html#id3>`_ 说明。

---------------------------

使用 ESP32-S3-WROOM-1 (ESP32-S3R2) 模组基于 ESP-IDF v4.4 版本的 hello-world 例程开启 PSRAM 的设置后，打印如下报错，是什么原因？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

      E (232) spiram: Virtual address not enough for PSRAM!

  ESP32-S3R2 芯片集成了 4 线的 2 MB PSRAM，请在 menuconfig 中将 PSRAM 模式设置为 **Quad** 模式。如下：

  ``menuconfig → Component config → ESP32S3 Specific → Support for external, SPI connected RAM → SPI RAM config → Mode (QUAD/OCT) of SPI RAM chip in use (Quad Mode PSRAM)``

-------------------------

使用 ESP32-S3-WROOM-2 (ESP32-S3R8V) 模组基于 ESP-IDF v4.4 版本的 hello-world 例程开启 PSRAM 的设置后，打印如下报错，是什么原因？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

      E (453) psram: psram ID read error: 0x00ffff
      E (454) cpu start: Failed to init external RAM!

  ESP32-S3R8V 芯片集成了 8 线的 8 MB PSRAM，请在 menuconfig 中将 PSRAM 模式设置为 **Octal** 模式。如下：

    ``menuconfig → Component config → ESP32S3 Specific → Support for external, SPI connected RAM → SPI RAM config → Mode (QUAD/OCT) of SPI RAM chip in use (Octal Mode PSRAM)``

--------------------

ESP8266 RTOS SDK 是否支持 SPI 全双工？
--------------------------------------------------------------------------------------------------

  :CHIP\: ESP8266:

  不支持。因为 ESP8266 不支持 DMA，因此为了提高传输性能利用了全部 FIFO，所以只能半双工，具体的详情请参考 `SPI readme <https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/peripherals/spi>`_。

---------------

ESP 系列芯片能支持三线 SPI 的 9 位时钟模式（即用第 1 位表示后 8 位是命令还是数据的模式）吗？
-----------------------------------------------------------------------------------------------------------

  - 目前 ESP32, ESP32-S, ESP32-C 系列的芯片都不支持非字节对齐的数据传输，即只支持 8 位对齐的数据传输，该问题的具体说明见 `Github issue <https://github.com/espressif/esp-idf/issues/8487>`_ 和 `文档 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/peripherals/spi_master.html#uint8-t>`__。
  - 后续新版本的 ESP 芯片可能会支持非字节对齐的数据传输，但目前还没有具体的时间表。

---------------

将 ESP 系列芯片的某一管脚设置为 SDA 数据线后，期望的结果是空闲时 SDA 线应为低电平，写数据时应为高电平。但此时为什么一上电空闲时此管脚为高电平，写数据是低电平？如何实现我期望的结果？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - SPI 中 MOSI (SDA) 和 SCK 信号线的空闲电平是由 SPI 模式控制的。
  - 可以通过修改 `spi_device_interface_config_t 结构体里的 mode 成员变量  <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/peripherals/spi_master.html#_CPPv4N29spi_device_interface_config_t4modeE>`_ 来实现。

----------------

ESP32-C6 使用 SPI DMA 模式时，单个 DMA Buffer 最大支持多少字节？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP32-C6 使用 SPI DMA 模式时，单个 DMA Buffer 最大支持 4092 字节。

---------------

ESP32 作为 SPI 主机，是否支持 30 MHz 时钟？
------------------------------------------------------------------------------------------------------------------------------

  - 不支持。ESP32 作为 SPI 主机时，当使用 SPI IO_MUX 管脚，最高可支持 80 MHz CLK，支持 80 MHz 进行整数分频。
  - 当使用 GPIO 矩阵管脚，最高可支持 40 MHz CLK；如果使用 GPIO 矩阵管脚的全双工传输模式，仅支持高达 26 MHz CLK。详细说明参见 `SPI 主机驱动程序 <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v5.2/esp32/api-reference/peripherals/spi_master.html#spi>`_ 软件使用说明。
