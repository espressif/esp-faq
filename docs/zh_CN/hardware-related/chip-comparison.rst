芯片功能对比
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

ESP32 单核与双核的区别？（从编程开发⽅式、性能表现、功耗表现等⽅⾯列举⼀下）
-----------------------------------------------------------------------------------------------------

  ESP32 单核与双核主要差异是多了⼀个独⽴核⼼，可以把⼀些实时性⾼的操作放在独⽴的⼀个核⼼上。

  - 编程⽅式⼀致，单核芯片需要配置 FreeRTOS 运⾏在单核上。配置路径：``make menuconfig`` > ``Component config`` > ``FreeRTOS`` > ``[*] Run FreeRTOS only on first core``；
  - 性能表现仅在⾼负载运算时有差异，若⽆⼤量计算差异使⽤上⽆明显差异（例如 AI 算法，⾼实时性中断）；
  - 功耗⽅⾯仅在 modem-sleep 的时候会有细微差别，详情可参考 `ESP32 技术参考手册 <https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_cn.pdf>`_。

--------------

ESP32 ECO V3 芯⽚在软硬件使⽤上和之前版本的芯片有什么区别呢？
------------------------------------------------------------------------

  - 软件上使⽤⽆区别，是可以兼容之前的固件的，硬件上修复了⼀些 bug。
  - 具体的设计变化可以参考⽂档 `ESP32 ECO V3 使用指南 <https://www.espressif.com/sites/default/files/documentation/ESP32_ECO_V3_User_Guide__CN.pdf>`_。

--------------

ESP32 的 GPIO34 ~ GPIO39 管脚是否只能设置为输入模式？
-----------------------------------------------------

  - ESP32 的 GPIO34 ~ GPIO39 只能设置为输入模式，没有软件上拉或下拉功能，不能设置为输出模式。
  - 详情可参见 `外设说明 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/peripherals/gpio.html?highlight=gpio34#gpio-rtc-gpio>`_。

--------------

ESP32 有适配 Linux 平台驱动吗？
-------------------------------

  有适配，请参考 `esp-hosted <https://github.com/espressif/esp-hosted>`_ 示例。

  .. note:: 该示例适配 802.3 协议，并不是 802.11 协议。

--------------

模组屏蔽盖上的二维码扫描数据如何解读？
--------------------------------------------

  - 若二维码扫描后读取数据为 0920118CAAB5D2B7B4，那么其中 09 为工厂代码，20 为 20** 生产年份（本示例中为 2020 年），11 为本年第几周生产，后 12 位 8CAAB5D2B7B4 为设备 mac 地址。

--------------

ESP32 的 VDD3P3_RTC 是否支持单独电池供电？
------------------------------------------------------

  - ESP32 内部 RTC 域不可以独立工作，需要主 CPU 参与配置，单独使用纽扣电池供电时依然无法抵御突然掉电的情况。
  - 如果需要系统掉电时时钟信息保存，可以添加外部 RTC 时钟芯片。

--------------

ESP32-PICO-D4 和 ESP32-PICO-V3 以及 ESP32-PICO-V3-02 有什么区别？
-----------------------------------------------------------------------

  - ESP32-PICO-V3 和 ESP32-PICO-V3-02 使用的是 ESP32 的 ECO V3 版本芯片，ESP32-PICO-D4 是 ESP32 的 V1 版本芯片。
  - 三者芯片封装相同，除 flash 与 psram 外，GPIO 大部分相同，ECO V3 存在部分管脚功能调整，具体细则请参考 datasheet。

---------------

ESP 模块支持 Thread 吗？
--------------------------------------------------------------------------------------------------------------------------------
  :CHIP\: ESP32 | ESP32-C3 | ESP32-S3:

  - 不支持 。
  - 目前支持 Thread 协议的是 ESP32-H2 芯片。

---------------

ESP 模组支持 WAPI (Wireless LAN Authentication and Privacy Infrastructure) 功能吗？
--------------------------------------------------------------------------------------------------------------------------------

  - 支持。

---------------

ESP8266 是否支持 32 MHz 晶振频率？
--------------------------------------------------------------------------------------------------------------------------------

  - 不支持，ESP8266 支持 26 MHz 和 40 MHz 晶振频率，推荐用 26 MHz。
  
---------------

ESP32 是否支持 zephyr？
-----------------------------------------------------------------------------------------------------------------------------------------

  - 对于 ESP 模块，目前仅对部分模块做了适配，后续会一直持续更新，详情请参考 `zephyr Doc <https://docs.zephyrproject.org/latest/boards/riscv/index.html>`_。
