生产测试
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

为什么部分模组使用 DIO/DOUT 时可以正常下载固件，但使用 QOUT/QIO 时程序无法正常运行？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 首先需要确认模组内 flash 支持哪些模式，以及模组设计的走线是否满足模式需要。
  - 其次检测 flash 状态寄存器的 QE 位，该 bit 位控制 flash 是否使能四线模式。
  - 不同的乐鑫芯片/模组采用 flash 厂家不同，部分厂商 flash 默认 QE 关闭。需要通过实际测试判断是否支持四线模式。
  - 当 ROM 引导二级引导加载程序时，如果配置的参数使用 QIO 方式读取，会因 QE 关闭而二次读取失败。
  - 建议模组使用 DIO 模式烧录，在 menuconfig 中配置 QIO 模式，该配置会在二级引导加载程序中配置 QE 位使能，进而引导 app bin 使用四线模式。

---------------

如何获取产测工具?
--------------------------------------------------------------------------------------------------

  :CHIP\: ESP32 | ESP8266:

  - 请点击 `产测工具 <https://download.espressif.com/fac_tool_release/Qrelease/the_latest_release/ESP_PRODUCTION_TEST_TOOL_NORMAL.zip>`_ 进行下载。

--------------

ESP32 使用 ``esptool.py burn_custom_mac`` 命令写入用户自定义 MAC 地址，为什么通过 ``esptool.py read_mac`` 读到的还是出厂默认的 MAC 地址？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ``esptool.py read_mac`` 命令默认只能读到出厂写在 eFuse BLOCK0 的 MAC 地址，而使用 ``esptool.py burn_custom_mac`` 命令写入的用户自定义的 MAC 地址是写到 eFuse BLOCK3 中，可以使用 ``espefuse.py get_custom_mac`` 命令来查询写入 eFuse BLOCK3 中的 MAC 地址。
  - 更多信息可以参考 `esptool 文档 <https://docs.espressif.com/projects/esptool/en/latest/esp32/>`__。

---------------

ESP32-WROVER-E (16 MB flash）模组使用 Flash 下载工具下载多个单独的 bin 文件成功，但下载合并的固件 (12 MB) 失败，是什么原因？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  由于合并后的固件绝大部分都是 "0xFF"，压缩率比较高，同样长度的压缩数据解压后的数据量比较大，导致烧录时间久出现烧录超时（默认 7 秒）报错。可以关闭 Flash 下载工具里的 ``configure`` > ``esp32`` > ``spi_download`` 文件里的压缩配置选项来下载合并的固件，如下：

  .. code-block:: c

    compress = False
    no_compress = True
