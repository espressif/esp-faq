芯片功能对比
============

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

--------------

ESP32 单核与双核的区别？
------------------------

    单核与双核的区别有哪些？从编程开发⽅式、性能表现、功耗表现等⽅⾯列举⼀下。

|  ESP32 单核与双核主要差异是多了⼀个独⽴核⼼，可以把⼀些实时性⾼的操作放在独⽴的⼀个核⼼上。
|  编程⽅式⼀致，单核芯片需要配置 freertos 运⾏在单核上。示例：``make menuconfig-->Component config → FreeRTOS -> [*] Run FreeRTOS only on first core``
|  性能表现仅在⾼负载运算时有差异，若⽆⼤量计算差异使⽤上⽆明显差异（例如 AI 算法， ⾼实时性中断 ）。
|  功耗⽅⾯仅在 modem-sleep 的时候会有细微差别，详情可参考芯⽚⼿册。

--------------

ESP32 E03 版本芯⽚在使⽤上和之前芯⽚软件使⽤上有什么区别呢？
------------------------------------------------------------

 软件上使⽤⽆区别，是可以兼容之前的固件的，硬件上修复了⼀些bug，具体的可以参考`此⽂档 <https://www.espressif.com/sites/default/files/documentation/ESP32_ECO_V3_User_Guide__CN.pdf>`__\ 。

--------------

ESP32 的 GPIO34 ~ GPIO39 管脚是否只能设置为输入模式？
-----------------------------------------------------

 ESP32 的 GPIO34 ~ GPIO39
只能设置为输入模式，没有软件上拉或下拉功能，不能设置为输出模式，参见\ `说明 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/peripherals/gpio.html?highlight=gpio34#gpio-rtc-gpio>`__\ 。

--------------

ESP32 有适配 Linux 平台驱动吗？
-------------------------------

-  有适配，请参考
   `esp-hosted <https://github.com/espressif/esp-hosted>`__ 示例。
-  注意： 示例适配 802.3 协议，并不是 802.11 协议。

--------------

模组上的二维码如何解读 ？
-------------------------

-  例如：0920118CAAB5D2B7B4
-  09 工厂代码， 20 为 20\*\* 生产年份（本示例为 2020 年），11
   为本年第几周生产，8CAAB5D2B7B4 为设备 mac 地址。

--------------

ESP32 的 VDD3P3\_RTC 是否支持系统掉电时使用电池供电 ？
------------------------------------------------------

-  ESP32 内部 RTC 域不可以独立工作，需要主 CPU
   参与配置，当单独使用纽扣电池供电，依然无法抵御突然掉电的情况。
-  如果需要系统掉电时时钟信息保存，可以添加外部 RTC 时钟芯片。

