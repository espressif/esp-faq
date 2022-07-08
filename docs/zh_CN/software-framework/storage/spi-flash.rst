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
--------------------------------------

  外部 flash 可以同时映射到 CPU 指令和只读数据空间。外部 flash 最大可支持 16 MB。

  - 当映射到 CPU 指令空间时，一次最多可映射 11 MB + 248 KB。如果一次映射超过 3 MB + 248 KB， 则 Cache 性能可能由于 CPU 的推测性读取而降低。
  - 当映射到只读数据空间时，一次最多可以映射 4 MB。支持 8-bit、16-bit 和 32-bit 读取。

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

  - 这是由于 flash 型号不同导致的，部分型号的 flash 进行擦除时没有空块跳过的机制，所以耗时较长。
