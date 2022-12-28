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

请从编程开发⽅式、性能表现、功耗表现等⽅⾯列举⼀下 ESP32 单核与双核的区别？
-----------------------------------------------------------------------------------------------------

  ESP32 单核与双核的主要差异是双核多了⼀个独⽴核⼼，可以把⼀些实时性⾼的操作放在该独⽴核⼼上。

  - 单核与双核的编程⽅式⼀致，不过单核芯片需要配置 FreeRTOS 运⾏在单核上，双核芯片则无需此步骤。配置路径：``make menuconfig`` > ``Component config`` > ``FreeRTOS`` > ``[*] Run FreeRTOS only on first core``。
  - 性能表现仅在⾼负载运算时有差异（例如 AI 算法，⾼实时性中断），其余使⽤上⽆明显差异。
  - 功耗仅在 Modem-sleep 模式下会有细微差别，此时双核芯片的功耗略高于单核芯片。详情可参考 `《ESP32 技术参考手册》 <https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_cn.pdf>`_。

--------------

ESP32 芯片版本 v3.0 在软硬件使⽤上和之前版本的芯片有什么区别呢？
------------------------------------------------------------------------

  - 软件上使⽤⽆区别，是兼容之前的固件的，硬件上修复了⼀些 bug。
  - 具体的设计变化可以参考⽂档 `《ESP32 芯片版本 v3.0 使用指南》 <https://www.espressif.com/sites/default/files/documentation/esp32_chip_revision_v3_0_user_guide_cn.pdf>`_。

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

  - 若二维码扫描后读取数据为 0920118CAAB5D2B7B4，那么其中 09 为工厂代码，20 为 20** 生产年份（本示例中为 2020 年），11 为本年第几周生产，后 12 位 8CAAB5D2B7B4 为设备 MAC 地址。关于此信息的最新说明，请参考 `《模组包装信息》 <https://www.espressif.com/sites/default/files/documentation/espressif_module_packaging_information_cn.pdf>`_。

--------------

ESP32 的 VDD3P3_RTC 是否支持单独电池供电？
------------------------------------------------------

  - ESP32 内部 RTC 域不可以独立工作，需要主 CPU 参与配置，单独使用电池供电时依然无法抵御突然掉电的情况。
  - 如果需要系统掉电时时钟信息保存，可以添加外部 RTC 时钟芯片。

--------------

ESP32-PICO-D4 和 ESP32-PICO-V3 以及 ESP32-PICO-V3-02 有什么区别？
-----------------------------------------------------------------------

  - ESP32-PICO-V3 和 ESP32-PICO-V3-02 使用的是 ESP32 的 v3.0 版本芯片，ESP32-PICO-D4 使用的是 ESP32 的 v1.0 版本芯片。
  - 三者芯片封装面积相同，除 flash 与 PSRAM 外，GPIO 大部分相同。v3.0 存在部分管脚功能调整，具体细则请参考技术规格书。

---------------

ESP8266 是否支持 32 MHz 晶振频率？
--------------------------------------------------------------------------------------------------------------------------------

  - 不支持，ESP8266 支持 26 MHz 和 40 MHz 晶振频率，推荐用 26 MHz。
  
---------------

ESP 系列产品是否支持 Zephyr？
-----------------------------------------------------------------------------------------------------------------------------------------

  - ESP 系列产品对 Zephyr 的支持可以参考 `乐鑫对 Zephyr 的最新支持 <https://www.espressif.com/zh-hans/news/Zephyr_updates>`_，目前仅适配了部分功能模块，后续会进一步更新。如果您有相关的功能需求，可以先在 `zephyr github issue <https://github.com/zephyrproject-rtos/zephyr/issues/29394>`_ 上查询或者提问。
  - 也可以从 `Zephyr 官方文档 <https://docs.zephyrproject.org/latest/introduction/index.html>`_ 的 `XTENSA Boards <https://docs.zephyrproject.org/latest/boards/xtensa/index.html>`_ 和 `RISCV Boards <https://docs.zephyrproject.org/latest/boards/riscv/index.html>`_ 找到 ESP 产品的相关资料。
