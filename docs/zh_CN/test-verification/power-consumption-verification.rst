功耗测试指南
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

ESP32 从 Deep-sleep 中唤醒时为何表现为重启的状态？
-----------------------------------------------------------------------

  进入 Deep-sleep 后，数字内核会断电，CPU 内容丢失，唤醒后需要重新引导固件并加载至内存。在 Deep-sleep 时 RTC 内存保持供电，可以将需要保留的应用信息保存其中，在唤醒后进行加载保留信息。


--------------

ESP32 的休眠⽅式有哪⼏种？有什么区别？
----------------------------------------------

  有 Modem-sleep、Light-sleep 和 Deep-sleep 三种休眠⽅式。

  - Modem-sleep 模式：CPU 正常工作，可以对时钟进行配置。设备作为 station 连接上 AP 之后⾃动开启，进⼊休眠状态后关闭射频模块，休眠期间保持和 AP 的连接。如果与 AP 断开连接，ESP32 将无法在 Wi-Fi Modem-sleep 模式下正常运行。ESP32 进入 Modem-sleep 模式后，还可以选择降低 CPU 时钟频率，进⼀步降低电流。
  - Light-sleep 模式：CPU 暂停工作，数字内核时钟受限。与 Modem-sleep 模式的不同之处在于，进⼊休眠状态后，不仅 RF 模块关闭，CPU 和部分系统时钟也将暂停。退出休眠状态后，CPU 继续运⾏。
  - Deep-sleep 模式：数字内核断电，CPU 内容丢失。进⼊休眠状态后，关闭除 RTC 模块外的所有其他模块；退出休眠状态后，整个系统重新运⾏（类似于系统重启）。休眠期间，AP 连接断开。

  对应的休眠功耗可参考 `ESP32 规格书 <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf>`__ 中的 *表 8：不同功耗模式下的功耗*。

--------------

ESP32 Deep-sleep 可以通过任意 RTC_GPIO 唤醒吗？
------------------------------------------------

  可以，RTC_GPIO 管脚配置可以参考 `《ESP32 技术规格书》 <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf>`_ 中的 *管脚定义* > *管脚描述* 章节。

--------------

ESP8266 的 CHIP_PU 管脚为低电平时，芯片的功耗是多少？
---------------------------------------------------------------------------

  - CHIP_PU 管脚即模组 EN 管脚，管脚设为低电平时，芯片的功耗约为 0.5 μA。
  - 在 `《ESP8266 技术规格书》 <https://www.espressif.com/sites/default/files/documentation/0a-esp8266ex_datasheet_cn.pdf>`_ > *功能描述* > *低功耗管理*> *表 3-4.不同功耗模式下的功耗* 中，功耗模式为 **关闭** 的一栏即代表 CHIP_PU 管脚拉低的状态。

--------------

ESP32 进入 Light-sleep 时，仅配置 GPIO 唤醒而不配置定时器唤醒时，底电流为什么会升高？
-----------------------------------------------------------------------------------------------------------------------------------------------------

  - 默认情况下，调用函数 `esp_light_sleep_start <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/system/sleep_modes.html#_CPPv421esp_light_sleep_startv>`_ 后不会断电 flash，这是为了防止当设备刚进入休眠又立刻被唤醒时，如果 flash 尚未完全断电又重新上电可能会导致的错误。
  - 有关此问题的详细信息，以及如何优化这种场景下的电流功耗，请参考《ESP-IDF 编程指南》中的 `Power-down of Flash <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/system/sleep_modes.html#flash>`_ 小节。

-----------------

在 ESP32 的 Deep-sleep 模式下，使用内部 150 KHz 的 RTC 时钟或使用外部 32 KHz，哪个功耗更大？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 若 RTC 时钟源选择的是外部无源 32 kHz 晶振，则功耗没有区别。
  - 若硬件上外接了外部有源 32 kHz 晶振，无论选择何者作为 RTC 时钟源，功耗都会上升 50~100 μA。

-----------------

如果通过降低 CPU 主频的方法减少功耗，为了保证射频模块的正常运行对 CPU 主频有什么要求？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  CPU 主频至少需要 80 Mhz 才能保证射频模块的正常工作。

-----------

使用 ESP32-S3 模组基于 `esp-idf/examples/system/light_sleep <https://github.com/espressif/esp-idf/tree/v5.1.1/examples/system/light_sleep>`__ 例程测试，如果单独使用 GPIO 唤醒源不使能 timer 唤醒时，功耗是 3 mA，与 datasheet 差别过大，可能是什么原因？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 当使用 RTC GPIO 唤醒源时，请在进入 light-sleep 模式前增加如下代码进行测试，**但是用户一定要保证仅使用 GPIO 的时候不会在刚睡下去就马上唤醒，因为在没配置 timer 的情况下，flash 上下电时间过短会导致 flash 上电时挂掉**

  .. code:: c

    esp_sleep_pd_config(ESP_PD_DOMAIN_VDDSDIO,ESP_PD_OPTION_OFF);
