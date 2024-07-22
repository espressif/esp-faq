PSRAM
=====

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

使用 ESP32 模组，如何查看模组的 PSRAM 的大小？
--------------------------------------------------------

  对于使用 ESP32 模组的情况，可以使用 ESP-IDF 中的 `esp_spiram_get_size() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/migration-guides/release-5.x/5.0/system.html?highlight=esp_spiram_get_size#psram>`_ 函数来获取模组的 PSRAM 大小。该函数会返回 PSRAM 的总大小（单位为字节），可以用于进行内存分配和管理等操作。

  以下是获取 PSRAM 大小的示例代码：

  .. code-block:: c

    size_t psram_size = esp_spiram_get_size();
    printf("PSRAM size: %d bytes\n", psram_size);

  注意，该函数需要在使用 PSRAM 之前调用，以确保正确获取 PSRAM 的大小。另外，需要先在 ``make menuconfig`` 中配置开启 PSRAM 功能，以便正确启用和配置 PSRAM。
  此外，PSRAM 的大小可通过 bootloader 的 log 信息来查看。

--------------

ESP32 外接 PSRAM 后，如何更改 PSRAM 的 clock 来源？
----------------------------------------------------------

  在 menuconfig 中修改。具体位置：menuconfig -> Component config -> ESP32-specific -> SPI RAM config。

--------------

ESP32 模组挂载 8 MB PSRAM, 为何实际映射的只有 4 MB？
---------------------------------------------------------------------

  - 使用 ESP32 芯片建议搭配使用官方 ESP-PSRAM 芯片。
  - 片外 RAM 最大可映射 4 MB (0x3F80_0000 ~ 0x3FBF_FFFF) 到数据地址空间，可参考 `ESP32 技术规格书 <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf>`_ 中 3.1.4 节存储器映射的说明。
  - 对于 8 MB PSRAM，可参考例程 `himem <https://github.com/espressif/esp-idf/tree/master/examples/system/himem>`_ 访问其余的 4 MB 空间。

-----------------

使用 ESP32 开发板，上面用了官方 PSRAM 芯片 PSRAM64H，当更换了另一个型号的 PSRAM 芯片后，运行 ESP-IDF 的例程并开启 PSRAM 配置，却无法正常识别，是什么原因？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 更换 PSRAM 芯片的型号，需要在 ``menuconfig`` > ``Component config`` > ``ESP32-specific`` > ``Support for external, SPI-connected RAM`` > ``SPI RAM config`` > ``Type of SPI RAM chip in use`` 中修改相应配置选项。
  - 若更换的 PSRAM 芯片型号在 menuconfig 中没有相应的配置选项，则需要自行加入 PSRAM 芯片的驱动。

-----------------------

使用 ESP32-WROOM-32E 模组下载 hello-world 例程，打印如下报错，是什么原因？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: c

    E (225) psram: PSRAM ID read error: 0xffffffff
    E (225) spiram: SPI RAM enabled but initialization failed. Bailing out. 

  报错原因是：软件上开启了 PSRAM (``Component config`` > ``ESP32-specific`` > ``Support for external, SPI-connected RAM``) 的设置，但硬件上没有检测到可用的 PSRAM。

--------------

ESP32 支持 16 MB 的 External Flash 和 8 MB 的 External PSRAM 共存吗？
----------------------------------------------------------------------------------

  ESP32 可以支持 16 MB 的 External Flash 和 8 MB 的 External PSRAM 共存使用。

--------------

基于 ESP32-S3-WROOM-N4R2 开启 ``BT/BLE will first malloc the memory form the PARAM`` 配置选项后，软件运行报错如下日志，但关闭 Bluetooth LE 5.0 配置后，运行正常。是什么原因？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: c

    E(36997)BLE_INIT:Mallocfailed
    E(37307)BLE_INIT:Mallocfailed
    E(38307)BLE_INIT:Mallocfailed
    E(39307)BLE_INIT:Mallocfailed
    E(40307)BLE_INIT:Mallocfailed

  - 当前报错是因为 Malloc 内存不足，当应用内存小于 ``idf.py menuconfig > ``Component config`` > ``ESP PSRAM`` > ``Support for external, SPI-connected RAM`` > ``SPI RAM config`` > ``(16384) Maximum malloc() zise , in bytes , to always put in internal memory`` 配置时，会默认使用芯片内部内存。可以将此配置调小，或者将 ``idf.py menuconfig`` > ``Component config`` > ``ESP PSRAM`` > ``Support for external, SPI-connected RAM`` > ``SPI RAM config`` > ``SPI RAM access method`` 配置改为 ``Make RAM allocatable using heap_caps_malloc(...... MALLOC_CAP_SPIRAM)`` 的配置。 

-------------

ESP32-C6 支持外挂 PSRAM 芯片吗？
-------------------------------------------------------------------------------------------------------------------

  - ESP32-C6 不支持外挂 PSRAM，但 ESP32-C61 支持外挂 PSRAM 芯片。

---------

使用 ESP32-PICO-V3-02 芯片在 ESP-IDF v5.1.2 上进行开发时，PSRAM speed 仅支持 40 MHz 吗？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - PSRAM speed 还支持 80 MHz。将 ``idf.py menuconfig`` > ``Serial flasher config`` > ``Flash SPI speed`` 设置为 80 MHz 之后，PSRAM speed 即可支持 80 MHz。
  - 通常，我们更推荐使用 80 MHz flash speed + 80 MHz PSRAM speed 的软件设置。

-------------

当使用 `xTaskCreateWithCaps() <https://docs.espressif.com/projects/esp-idf/zh_CN/v5.2.1/esp32/api-reference/system/freertos_additions.html#_CPPv419xTaskCreateWithCaps14TaskFunction_tPCKc22configSTACK_DEPTH_TYPEPCv11UBaseType_tP12TaskHandle_t11UBaseType_t>`_ API 分配外部 PSRAM 时，软件编译报错如下，是什么原因？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: c

    assert failed: xTaskCreateStaticPinnedToCore freertos_tasks_c_additions.h:314 (xPortcheckValidStackMem(puxStackBuffer))

当使用 ``xTaskCreateWithCaps()`` 分配 PSRAM 时，menuconfig 中需要启用 ``Component config`` > ``ESP PSRAM`` > ``Support for external, SPI-connected RAM`` 配置，然后将 ``SPI RAM config`` > ``SPI RAM access method`` 设置为 ``(X) Make RAM allocatable using malloc() as well`` 模式，最后需要启用 ``[*] Allow external memory as an argument to xTaskCreateStatic`` 配置选项。
