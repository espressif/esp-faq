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

为什么有部分模组使用 QOUT/QIO 下载固件，程序无法正常运行？ （DIO/DOUT 正常）
----------------------------------------------------------------------------

  - 首先需要确认模组内 flash 支持哪些模式，以及模组设计的走线是否满足模式需要；
  - 其次检测 Flash 状态寄存器的 QE 位，该 bit 位控制 Flash 是否使能四线模式。
  - 我司模组除部分集成 flash 芯片外模组均支持四线模式，但由于采用 flash 厂家不同，部分厂商 flash 默认 QE 关闭。
  - 当 ROM 引导二级 bootloader 时，如果使用配置的参数 QIO 方式读取，会因 QE 关闭而二次读取失败。
  - 建议模组使用 DIO 模式烧录，在 make menuconfig 中配置 QIO 模式，该配置会在二级 bootloader 中配置 QE 位使能，进而引导 APP bin 使用四线模式。


---------------

如何获取产测工具?
--------------------------------------------------------------------------------------------------

  :CHIP\: ESP32 | ESP8266:

  - `产测工具下载链接 <download.espressif.com/fac_tool_release/Qrelease/the_latest_release/ESP_PRODUCTION_TEST_TOOL_NORMAL.zip>`_。
