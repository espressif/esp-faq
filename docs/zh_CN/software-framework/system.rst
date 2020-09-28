系统
====

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

如果我的应⽤不需要看⻔狗，如何关闭看⻔狗？
------------------------------------------

  当前 SDK 仅⽀持关闭软件看⻔狗，⽀持同时喂软硬件看⻔狗。可以通过如下⽅式防⽌执⾏时间过⻓的⽤户程序导致看⻔狗复位：
  - 如果⼀个程序段运⾏时间在触发软件看⻔狗和触发硬件看⻔狗复位之间，则可通过 system\_soft\_wdt\_stop() 的⽅式关闭软件看⻔狗，在程序段执⾏完毕后⽤ system\_soft\_wdt\_restart() 重新打开软件看⻔狗。
  - 可以通过在程序段中添加 system\_soft\_wdt\_feed() 来进⾏喂软硬件狗操作，防⽌软硬件看⻔狗复位。
  - 硬件看⻔狗中断时间为 0.8\ *2048 ms，即 1638.4 s，中断后处理时间为 0.8*\ 8192 ms，即 6553.6 ms。其中中断处理后时间为硬件看⻔狗中断发⽣后，需要进⾏喂狗操作的时间，如果超过该时间，即会触发硬件看⻔狗复位。因此，在仅有硬件看⻔狗的情况下，⼀个程序段如果运⾏时间超过 6553.6 ms，即有可能触发硬件看⻔狗复位，若超过 8192 ms 则⼀定会触发复位。
  - 软件看⻔狗建⽴在 MAC timer 以及系统调度之上，中断时间为 1600 ms，中断后处理时间 1600 ms。因此，在有软件+硬件看⻔狗的情况下，⼀个程序段如果运⾏时间超过 1600 ms，即有可能会触发软件看⻔狗复位，若超过 3200 ms 则⼀定会触发复位。

--------------

RTOS SDK 和 Non-OS SDK 有何区别？
---------------------------------

  主要差异点如下：

  **Non-OS SDK**

  - Non-OS SDK 主要使⽤定时器和回调函数的⽅式实现各个功能事件的嵌套，达到特定条件下触发特定功能函数的⽬的。Non-OS SDK 使⽤ espconn 接⼝实现⽹络操作， ⽤户需要按照 espconn 接⼝的使⽤规则进⾏软件开发。

  **RTOS SDK**

  - RTOS 版本 SDK 使⽤ freeRTOS 系统，引⼊ OS 多任务处理的机制，⽤户可以使⽤ freeRTOS 的标准接⼝实现资源管理、循环操作、任务内延时、任务间信息传递和同步等⾯向任务流程的设计⽅式。具体接⼝使⽤⽅法参考 freeRTOS 官⽅⽹站的使⽤说明或者 USING THE FREERTOS REAL TIME KERNEL - A Practical Guide 这本书中的介绍。
  - RTOS 版本 SDK 的⽹络操作接⼝是标准 lwIP API，同时提供了 BSD Socket API 接⼝的封装实现，⽤户可以直接按照 socket API 的使⽤⽅式来开发软件应⽤，也可以直接编译运⾏其他平台的标准 Socket 应⽤，有效降低平台切换的学习成本。
  - RTOS 版本 SDK 引⼊了 cJSON 库，使⽤该库函数可以更加⽅便的实现对 JSON 数据包的解析。
  - RTOS 版本兼容 Non-OS SDK 中的 Wi-Fi 接⼝、SmartConfig 接⼝、Sniffer 相关接⼝、系统接⼝、定时器接⼝、FOTA 接⼝和外围驱动接⼝，不⽀持 AT 实现。

--------------

ESP8266 启动时 LOG 输出 ets\_main.c 有哪些原因？
------------------------------------------------

  ESP8266 启动时打印 ``ets_main.c``\ ，表示没有可运⾏的程序区，⽆法运⾏；遇到这种问题时，请检查烧录时的 bin ⽂件和烧录地址是否正确。

--------------

ESP8266 编译 Non-OS SDK 时 IRAM\_ATTR 错误是什么原因？
------------------------------------------------------

  如果需要在 IRAM 中执⾏功能，就不需要加 ``ICACHE_FLASH_ATTR`` 的宏，那么该功能就是放在 IRAM 中执⾏。

--------------

ESP8266 main 函数在哪里？
-------------------------

  ESP8266 用户 SDK 部分没有 main 函数。main 函数处于 一级 bootloader 并且固化在芯片 ROM 中， 用于引导二级 bootloader。二级 bootloader 入口函数为 ets\_main，启动后会加载用户应用中的 user\_init，引导至用户程序。

--------------

ESP8266 partition-tables 特殊注意点？
-------------------------------------

  ESP8266 partition-tables 相对 ESP32 对于 ota 分区有一定的特殊要求，这是由于 ESP8266 cache 特性导致。详情参考 `ESP8266 partition-tables 偏移与空间 <https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/api-guides/partition-tables.html#offset-size>`_。

--------------

应⽤层与底层的 bin ⽂件可以分开编译吗?
--------------------------------------

  不⽀持分开编译。

--------------

ESP32 模组 flash 使用 80 Mhz 有什么注意事项吗 ？
------------------------------------------------------------

  乐鑫模组发售前已经过稳定性测试，测试可以支持 80 MHz 频率。根据稳定性测试数据，80 MHz 的频率不会影响使用寿命和稳定性。

--------------

ESP32 系统软件复位 API？
------------------------

  软件复位 API：``esp_restart()``。

--------------

使用 esp-idf 按汇编操作寄存器，是否涉及到调用不可编辑的库文件？
---------------------------------------------------------------

  如果单纯使用读写寄存器指令或者汇编指令，不存在调用库文件的问题。如果调用 esp-idf 预制的函数，则可能会遇到调用 lib 函数的情况。不推荐在 ESP32 中使用汇编操作，如果部分场景想要提高速度，可以读写寄存器来完成部分操作。

--------------

使用 ESP-IDF 测试程序，如何设置可在单核模组上下载程序？
-------------------------------------------------------------------

  程序编译时，使用 make menuconfig 指令进入配置界面，进行如下配置，可在单核模组上下载程序；在配置界面中，按键 Y 为启动，N 为关闭。

  Component config --> FreeRTOS --> Run FreeRTOS only on first core（启动此选项）

--------------

使用 esp-idf，如何使能 ESP32 的双核模式？
-----------------------------------------

  esp-idf 一般情况下默认配置的是双核模式，您可以在 menuconfig 中进行单双核的修改：menuconfig -> Component config -> FreeRTOS -> Run。

  FreeRTOS only on first core 使能即为单核，未使能默认双核。

--------------

使用 ESP32-D0WD 芯片是否可以存储用户程序？
------------------------------------------

  不可以，用户程序必须使用外挂 Flash 进行存储，片上 ROM 不能存储用户程序。ROM 内存放的程序为芯片一级 bootloader，为了保护出厂程序不被破坏，该区域为只读存储。

--------------

ESP32 进入低功耗模式时， PSRAM 中的数据会丢失吗？
-------------------------------------------------

  - Modem-sleep/Light-sleep 模式时，PSRAM 中的数据不会丢失。
  - Deep-sleep 模式时，CPU 和大部分外设都会掉电，PSRAM 的数据会丢失。

--------------

请问 ESP32 CPU 系统时间是否由系统滴答时钟生成？精度如何？
---------------------------------------------------------

  CPU 系统时间是由 esp\_timer 内部的 64 位硬件定时器 CONFIG\_ESP\_TIMER\_IMPL 产生的，是微秒级的时间分辨率。参见 `说明 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/system/esp_timer.html?highlight=esp_timer_get_time#high-resolution-timer>`_。

--------------

ESP32 的 flash 和 psram 的时钟频率如何修改？
--------------------------------------------

  在 menuconfig 中修改。 
  - flash 时钟频率：menuconfig -> Serial flasher config -> Flash SPI speed。 
  - PSRAM 时钟频率：Component config -> ESP32-specific -> SPI RAM config -> Set RAM clock speed。

--------------

使用 ESP32-SOLO-1 模组，esp-idf 如何设置可在单核模组上运行？
------------------------------------------------------------

  使用 menuconfig 指令进入配置界面，Component config  -->  FreeRTOS  -->  Run FreeRTOS only on first core（启动此选项）可在单核模组上运行下载。

--------------

esp-idf 是否可以配置 time\_t 为 64 bit ? （现在是 32 bit）
----------------------------------------------------------

  当前暂时不支持，预计在 release/v4.2 或更高版本种支持。如果配置支持 time\_t 64 bit 自定义工具链，可以使能 make menuconfig 中 SDK tool configuration -> SDK\_TOOLCHAIN\_SUPPORTS\_TIME\_WIDE\_64\_BITS 。

--------------

固件如何区分主芯片是 ESP8285 还是 ESP8266？
-------------------------------------------

  通常使用外部工具 `esptool <https://github.com/espressif/esptool>`_ 来读取芯片类型。可以在固件中根据 python 代码示例，读取芯片对应寄存器位，并进计算判断得出。

.. code-block:: python

  def get_efuses(self): 
  # Return the 128 bits of ESP8266 efuse as a single Python integer 
  return (self.read_reg(0x3ff0005c) << 96 | self.read_reg(0x3ff00058) << 64 | self.read_reg(0x3ff00054) << 32 | self.read_reg(0x3ff00050))

  def get_chip_description(self):
    efuses = self.get_efuses()
    is_8285 = (efuses & ((1 << 4) | 1 << 80)) != 0  # One or the other efuse bit is set for ESP8285
    return "ESP8285" if is_8285 else "ESP8266EX"

--------------

ESP32 能否以动态库的方式加载库文件运行?
---------------------------------------

  ESP32 不支持动态库的方式加载库文件，只支持靜态库。

------------------

ESP32 有几种系统复位方式？
--------------------------------

  - 有“芯片上电复位”、“RWDT 系统复位”、“欠压复位” 3 种系统复位方式。
  - 具体说明参见 `《ESP32 技术规格书》<https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_cn.pdf>`__ 4.1.2 复位源章节。

--------------

ESP8266-NONOS-V3.0 版本的 SDK，报错如下，是什么原因？
-----------------------------------------------------------------

  .. code-block:: text

    E:M 536 
    E:M 1528 

  - 导致出现 E:M 开头的 LOG 是由于剩余内存不足。

--------------
  
ESP32 是否可以完整使用 8MB PSRAM 内存？
-----------------------------------------------------------------

  - ESP32 可完整使用 8MB PSRAM 内存。
  - 由于 cache 最大映射空间为 4MB，所以仅支持 4MB psram 映射使用，剩余空间可以使用 API 操作使用。
  - 参考示例 [himem](https://github.com/espressif/esp-idf/tree/master/examples/system/himem)。

--------------

ESP8266 AT 连接 AP 后，系统默认进入 modem-sleep，但电流未明显下降有哪些原因？
----------------------------------------------------------------------------------------

  - AT 固件连接 AP 后，ESP8266 会进入自动 modem-sleep 模式，功耗大约会在 15mA ~ 70mA 之间波动。
  - 如果功耗并没有在 15mA ~ 70mA 之间波动，在示波器中未呈现波形的电流，有以下建议：
    - 擦除设备 flash 后，重新烧录 AT 固件。
    - 抓取网络包分析，是否在当前的网络环境中，是否有频繁发送广播包的设备，可换一个网络环境的路由器（AP）进行测试。

--------------

IDF 版本更新后，更新说明在哪里？
----------------------------------------------------------------------------------------

  可以在 Github release note 查看相关说明。链接为: https://github.com/espressif/esp-idf/releases

--------------

ESP8266 是否有详细的寄存器⼿册？
---------------------------------------

  请参考 《8266 TRM appendix》部分，链接：https://www.espressif.com/sites/default/files/documentation/esp8266-technical_reference_cn.pdf

--------------

ESP8266 如何在设备软重启的情况下保留数据？
---------------------------------------------

  - 如果写入或者修改的次数不频繁， 可以使用 Flash 来存储数据，该区域相对于内存较大，并且容易调整。
  - 若数据较小，可以使用 RTC Memory 内存来存储相关数据。示例： Rel 2.1 的分支中 esp_system.h 中的接口 （详细阅读使用说明）system_rtc_mem_read。
  - 如果以上两者都无法满足需求，也可以选择外挂的 RTC 内存，可以使用 I2C 与 SPI 进行交互。
  - 通常在写入频率不高的情况下建议写入 Flash ， 因为该方法在硬断电时数据仍然正常。

--------------

ESP8266 有哪些定时器可用？
-----------------------------

  - ESP8266 有一个硬件定时器，可以产生中断，在 NONOS SDK 与 RTOS SDK 调用 API 略有不同。
  - 软件定时器：
    - NONOS 中 API os_timer 是 DSR 处理，不能产⽣中断，但是可以产⽣任务，任务会按照普通等级排队。
    - RTOS 中可以使用 freertos 中的软件定时器，使用方式更加灵活。

--------------

ESP8266 的看⻔狗是什么作⽤？
-----------------------------

  - 为了提供系统稳定性，以应对多冲突的操作环境，ESP8266 集成了 2 级看⻔狗机制，包括软件看⻔狗和硬件看⻔狗。
  - 默认 2 个看⻔狗都是打开的，HW WDT 始终在运行，并且如果未重置 HW WDT 计时器，则会在大约 6 秒钟后重置 MCU。
  - SW WDT 大约在 1.5 秒左右将 MCU 复位。您可以启用/禁用 SW WDT，但不能启用/禁用 HW WDT。因为必须重置 SW WDT 后才能同时重置 HW WDT。
  - 可通过修改 `make menuconfig` -> `Component config` -> `Common ESP-related` 里的 `Invoke panic handler on Task Watchdog timeout` 等来配置看门狗。 

--------------

ESP8266 user_init 内有那些注意事项？
----------------------------------------

  - wifi_set_ip_info、wifi_set_macaddr 仅在 user_init 中调⽤⽣效，其他地⽅调⽤不⽣效。
  - system_timer_reinit 建议在 user_init 中调⽤，否则调⽤后，需要重新 arm 所有 timer。
  - wifi_station_set_config 如果在 user_init 中调⽤，底层会⾃动连接对应路由，不需要再调⽤ wifi_station_connect 来进⾏连接。否则，需要调⽤ wifi_station_connect进⾏连接。
  - wifi_station_set_auto_connect 设置上电启动时是否⾃动连接已记录的路由；例如，关闭⾃动连接功能，如果在 user_init 中调⽤，则当前这次上电就不会⾃动连接路由，如果在其他位置调⽤，则下次上电启动不会⾃动连接路由。
