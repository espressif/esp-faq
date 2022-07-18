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
-------------------------------------------------------

  需要先在 ``make menuconfig`` 中配置开启 PSRAM 功能。PSRAM 的大小可通过 bootloader 的 log 信息或调用 esp_spiram_get_size() 来查看。

--------------

ESP32 外接 PSRAM 后，如何更改 PSRAM 的 clock 来源？
----------------------------------------------------------

  在 menuconfig 中修改。具体位置：menuconfig -> Component config -> ESP32-specific -> SPI RAM config。

--------------

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

-----------------------

使用 ESP32-WROOM-32E 模组下载 hello-world 例程，打印如下报错，是什么原因？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: c

    E (225) psram: PSRAM ID read error: 0xffffffff
    E (225) spiram: SPI RAM enabled but initialization failed. Bailing out. 

  报错原因是：软件上开启了 PSRAM (``Component config`` > ``ESP32-specific`` > ``Support for external, SPI-connected RAM``) 的设置，但硬件上没有 PSRAM 的支持。