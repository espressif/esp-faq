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
----------------------------------------------------------------------

  在进入深度睡眠 (Deep-sleep) 后数字内核会断电，CPU 内容丢失，唤醒后需要重新引导固件并加载至内存。在深度睡眠时 RTC 内存保持供电，可以将需要保留的应用信息保存其中，在唤醒后进行加载保留信息。


--------------

休眠⽅式有哪⼏种？有什么区别？
------------------------------

  有 Modem-sleep、Light-sleep 和 Deep-sleep 三种休眠⽅式。

  - Modem-sleep 模式：CPU 可以正常工作，可以对时钟进行配置。设备作为 station 连接上 AP 之后⾃动开启，进⼊休眠状态后关闭射频模块，休眠期间保持和 AP 的连接。如果与 AP 断开连接，ESP32 将无法正常运行在这种 Wi-Fi Modem-sleep 模式下。ESP32 进入 Modem-sleep 模式后，还可以选择降低 CPU 时钟频率，进⼀步降低电流。
  - Light-sleep 模式：CPU 暂停工作，数字内核时钟受限。与 Modem-sleep 模式的不同之处在于进⼊休眠状态后，不仅关闭 RF 模块，还暂停 CPU 和部分系统时钟。退出休眠状态后，CPU 继续运⾏。
  - Deep-sleep 模式：数字内核断电，CPU 内容丢失。进⼊休眠状态后，关闭除 RTC 模块外的所有其他模块；退出休眠状态后，整个系统重新运⾏（类似于系统重启）。休眠期间不保持到 AP 的连接。

--------------

ESP32 Deep-sleep 可以通过任意 RTC_GPIO 唤醒吗？
------------------------------------------------

  是的，RTC_GPIO 管脚配置可以参考 `《ESP32 技术规格书》 <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf>`_ > *管脚定义* > *管脚描述*。

--------------

ESP8266 的 CHIP_PU 管脚为低电平时，芯片的功耗是多少？
---------------------------------------------------------------------------

  - CHIP_PU 管脚即模组 EN 管脚，管脚设为低电平时，芯片的功耗约为 0.5 μA。
  - 在 `《ESP8266 技术规格书》 <https://www.espressif.com/sites/default/files/documentation/0a-esp8266ex_datasheet_cn.pdf>`_ 不同功耗模式下的功耗一表中，功耗模式为关闭，即代表的是 CHIP_PU 管脚拉低，芯片处于关闭状态。

--------------

ESP32 进入 Light-sleep 时，如果仅配置 GPIO 唤醒而不配置定时器唤醒，底电流为什么会升高？
-----------------------------------------------------------------------------------------------------------------------------------------------------

  - 默认情况下，调用函数 `esp_light_sleep_start <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/sleep_modes.html#_CPPv421esp_light_sleep_startv>`_ 和 `esp_deep_sleep_start <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/sleep_modes.html#_CPPv420esp_deep_sleep_startv>`_ 不会断电 flash，这是为了防止设备刚进入休眠就立刻被唤醒，而如果 flash 还没断电完又重新上电可能会出错。
  - 而在配置了定时器唤醒的情况下，系统会对 flash 进行掉电，所以底电流会相对较低。 
  - 在不配置定时器的情况下，对于一些功耗敏感型的应用，可以在 menuconfig 中通过以下的操作来进行 flash 的掉电：关闭 ``Power down flash in light sleep when there is no SPIRAM`` 这个选项，同时打开 ``Flash leakage current workaround in light sleep`` 这个选项。
