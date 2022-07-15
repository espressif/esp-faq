安全数字输入输出 (SDIO)
=============================

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

SDIO 最⾼速度能⽀持到多少？
-------------------------------------

  SDIO 时钟能到 50 MHz，理论最⾼速度是 200 Mbps。

--------------

ESP8266 的 SDIO 是否⽀持 SD 卡？
--------------------------------------------

  ESP8266 是 SDIO 从机，不⽀持 SD 卡。

--------------

ESP32 SD 卡支持的最大容量是多少？
-------------------------------------------------

  - SD3.01 规范中 SDXC 的卡最大支持 2 TB (2048 GB) 容量。
  - ESP32 的 SDMMC 主机符合 SD3.01 协议，通过该外设可以访问最多 2 TB 的区域；使用 SDSPI 驱动通过 SPI 总线访问卡时，硬件也支持访问 2 TB 的区域。
  - 在软件层面上，卡能使用的空间还受文件系统的影响。

--------------

ESP32 SD 卡是否可以与 flash & PSRAM 共同使用？
---------------------------------------------------------------

  - 可以共同使用。 
  - ESP32 flash & PSRAM 与 SD 卡使用的不是同一组 SDIO。

--------------

使用 ESP-WROOM-S2 模组，是否支持 SDIO 作从机？
----------------------------------------------------------------------------

  ESP-WROOM-S2 支持 SDIO 作从机。

-----------------

ESP32-S2 取消了 SDIO 接口，是否还支持外接 TF 卡？
----------------------------------------------------------------

  ESP32-S2 可使用 SPI2/SPI3 的接口外接 TF 卡，此时使用 TF 卡的 SPI 模式。

----------------

ESP32-S2 支持 eMMC 吗？
--------------------------------------------------------------------------------------------------

  :CHIP\: ESP32-S2:

  不支持。

----------------

ESP32-S2 是否支持 SDIO 作从机？
----------------------------------------------------------------------------------------

  ESP32-S2 没有 SDIO 接口，不支持 SDIO 作从机。

----------------

ESP32 如何开启和关闭 SDIO 从机接收数据的中断？
--------------------------------------------------------------------------------------------------------------

  SDIO 从机数据接收与挂载的 buffer 状态有关，接收完之后需要调用 `sdio_slave_recv_load_buf <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/peripherals/sdio_slave.html#_CPPv424sdio_slave_recv_load_buf23sdio_slave_buf_handle_t>`_ 释放 buffer，否则 SDIO 主机将无法继续向 SDIO 从机发送数据。