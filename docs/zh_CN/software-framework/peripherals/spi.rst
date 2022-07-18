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
----------------------------------------------------

  ESP-WROOM-02D 有空闲 SPI 外设，可外接 SPI flash，用以存储数据。

--------------

ESP-WROOM-S2 作为从机，STM32 作为 MCU ，可以使⽤ SPI 接⼝下载吗？
-------------------------------------------------------------------------

  不可以，默认下载功能仅支持串口 UART0，固件启动后可应用中使能其他外设，在应用中⾃⾏设计⽀持 OTA 功能。

--------------

ESP32 中 SPI/HSPI/VSPI 三者有什么区别呢？
-------------------------------------------------------------

  - ESP32 有 4 组 SPI，其中 SPI0 和 SPI1 用来连接储存程序的 flash，默认被占用，剩下的两组 SPI2 和 SPI3 为可供客户自由使用的通用 SPI。
  - HSPI 代表上述 SPI2，VSPI 代表上述 SPI3，这两组 SPI 均为通用 SPI。

--------------

ESP32 使用 SPI DMA 时最大的数据传输量是 4092 字节，是因为硬件限制吗？
----------------------------------------------------------------------------------------------------------------------------------------------

  是的，这属于硬件限制。单个节点只能存 4092 字节，但 DMA 可以通过链表来发送更多的数据。

-----------------

ESP32-S2 的 SPI 同时访问三个 SPI 从机设备，是否需要做信号量同步才能访问？
------------------------------------------------------------------------------------------------------------------------------

  - 同一个 SPI 外设作为主机，一次只能与一个从机进行通信，由 CS 决定与哪个从机进行通信。如果是给 SPI 驱动挂 3 个 从机设备，并与它们分别通信的话是可以的，推荐这种用法。
  - 可使用 ``spi_device_transmit()`` 接口，这个接口是一个阻塞接口，在一次传输完成后返回。多个任务逐次调用这个接口，用不同的 handle 进行通信即可。
  
---------------------

使用 ESP32 开发板基于 ESP-IDF release/v4.3 版本的 SDK 进行开发测试，软件编译报错如下，是什么原因？
------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    spi_flash:Detected size(8192K) smaller than the size in the binary image header(16384K).Probe failed. 

  - 原因是配置的 flash 大小比实际使用的 flash 大小要大，为避免误用更大的地址空间而对实际使用的 flash 大小进行检测。

----------------

SPI 从机支持最大速度是多少？
-------------------------------------------------------------------------------
  :CHIP\: ESP32 :

  ESP32 作为 SPI 从机时钟最高只支持到 10 M。

-------------------------

使用 ESP32 作为 SPI 主机设备，在非 DMA 模式下最大可一次性传输多少字节的数据？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 使用 ESP32 作为 SPI 主机设备，在非 DMA 模式下最大可一次性传输 64 字节的数据。
  - 但当传输超过 32 比特时，需要设置 SPI 发送数据的缓冲区，可参考 `SPI Master Driver <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.4/esp32/api-reference/peripherals/spi_master.html?highlight=spi#spi-master-driver>`_ 说明。
  - 使用 ESP32 作为 SPI 主机设备在非 DMA 模式下传输超过 32 比特的 SPI 数据，可参考例程 `esp-idf/examples/peripherals/spi_slave/sender <https://github.com/espressif/esp-idf/tree/release/v4.4/examples/peripherals/spi_master/lcd>`_。
  
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

      E (453) psrm: psrm ID read error: 0x00ffff
      E (454) cpu start: Failed to init external RAM!

  ESP32-S3R8V 芯片集成了 8 线的 8 MB PSRAM，请在 menuconfig 中将 PSRAM 模式设置为 **Octal** 模式。如下：

    ``menuconfig → Component config → ESP32S3 Specific → Support for external, SPI connected RAM → SPI RAM config → Mode (QUAD/OCT) of SPI RAM chip in use (Octal Mode PSRAM)`` 

--------------------

使用 ESP32-C3 通过 SPI 接口驱动 LCD 液晶显示屏，是否可使用 RTC_CLK 作为 SPI 时钟，让 LCD 液晶显示屏能在 Deep-sleep 模式下正常显示静态图片？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Deep-sleep 模式：CPU 和大部分外设都会掉电，只有 RTC 存储器处于工作状态。请阅读`《ESP32-C3 技术规格书》 <https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_cn.pdf>`_ 关于“低功耗管理”的说明。
  - ESP32-C3 的 SPI 只支持 APB_CLK 和 XTAL_CLK 两种时钟源，不支持使用 RTC_CLK。因此在 Deep-sleep 模式下，LCD 液晶屏无法显示静态图片。请阅读 `《ESP32-C3 技术参考手册》 <https://www.espressif.com/sites/default/files/documentation/esp32-c3_technical_reference_manual_cn.pdf>`_  关于“外设时钟”说明。
  
-----------------------

ESP8266 RTOS SDK 是否支持 SPI 全双工？
--------------------------------------------------------------------------------------------------

  :CHIP\: ESP8266:

  不支持。因为 ESP8266 不支持 DMA，因此为了提高传输性能利用了全部 FIFO，所以只能半双工，具体的详情请参考 `SPI readme <https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/peripherals/spi#spi-demo-user-guide>`_。

---------------

ESP32 能支持三线 SPI 的 9 位时钟模式（即用第 1 位表示后 8 位是命令还是数据的模式）吗？
-----------------------------------------------------------------------------------------------------------

  支持，可以参考使用 `SPI Transactions <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/peripherals/spi_master.html#spi-transactions>`_ 里提到的命令或地址阶段，定义其中一个阶段大小为 1 位，然后给这个位赋值 0 或者 1 来区分后续 8 位是数据还是命令，这样即可实现三线 SPI 的 9 位时钟模式。

---------------

将 ESP32-S2 的 GPIO35 管脚设置为 SPI 屏的 SDA 数据线后，期望的结果是空闲时 SDA 线应为低电平，写数据时应为高电平。但此时为什么一上电空闲时此管脚为高电平，写数据是低电平？如何实现我期望的结果？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  请修改 `spi_device_interface_config_t 结构体里的 mode 成员变量  <https://github.com/espressif/esp-idf/blob/master/components/driver/include/driver/spi_master.h#L58>`_。

---------------

ESP32 使用 `gpio_install_isr_service() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/gpio.html#_CPPv424gpio_install_isr_servicei>`_ 初始化新的 GPIO 中断服务时返回 `ESP_ERR_NOT_FOUND`，可能是什么原因？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  这个错误通常代表 ESP32 的可用中断源不够用，此时应该同时有多个外设在同时占用中断源，可尝试减少其他组件的中断源使用个数来初始化新的 GPIO 中断。