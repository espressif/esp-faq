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
-------------------------------------------

  ESP-IDF 中主要有两种看门狗：任务看门狗和中断看门狗。您可以在配置菜单中关闭这两种看门狗。更多细节请参考 `Watchdogs <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/get-started/index.html>`_。

--------------

RTOS SDK 和 Non-OS SDK 有何区别？
---------------------------------

  主要差异点如下：

  **Non-OS SDK**

  - Non-OS SDK 主要使⽤定时器和回调函数的⽅式实现各个功能事件的嵌套，达到特定条件下触发特定功能函数的⽬的。Non-OS SDK 使⽤ espconn 接⼝实现⽹络操作，⽤户需要按照 espconn 接⼝的使⽤规则进⾏软件开发。

  **RTOS SDK**

  - RTOS 版本 SDK 使⽤ FreeRTOS 系统，引⼊ OS 多任务处理的机制，⽤户可以使⽤ FreeRTOS 的标准接⼝实现资源管理、循环操作、任务内延时、任务间信息传递和同步等⾯向任务流程的设计⽅式。具体接⼝使⽤⽅法参考 FreeRTOS 官⽅⽹站的使⽤说明或者 USING THE FREERTOS REAL TIME KERNEL - A Practical Guide 这本书中的介绍。
  - RTOS 版本 SDK 的⽹络操作接⼝是标准 lwIP API，同时提供了 BSD Socket API 接⼝的封装实现，⽤户可以直接按照 socket API 的使⽤⽅式来开发软件应⽤，也可以直接编译运⾏其他平台的标准 Socket 应⽤，有效降低平台切换的学习成本。
  - RTOS 版本 SDK 引⼊了 cJSON 库，使⽤该库函数可以更加⽅便的实现对 JSON 数据包的解析。
  - RTOS 版本兼容 Non-OS SDK 中的 Wi-Fi 接⼝、SmartConfig 接⼝、Sniffer 相关接⼝、系统接⼝、定时器接⼝、FOTA 接⼝和外围驱动接⼝，不⽀持 AT 实现。

--------------

ESP8266 启动时 LOG 输出 ets_main.c 有哪些原因？
------------------------------------------------

  ESP8266 启动时打印 ``ets_main.c``，表示没有可运⾏的程序区，⽆法运⾏；遇到这种问题时，请检查烧录时的 bin ⽂件和烧录地址是否正确。

--------------

ESP8266 编译 Non-OS SDK 时 IRAM_ATTR 错误是什么原因？
------------------------------------------------------

  如果需要在 IRAM 中执⾏功能，就不需要加 ``ICACHE_FLASH_ATTR`` 的宏，那么该功能就是放在 IRAM 中执⾏。

--------------

ESP8266 main 函数在哪里？
-------------------------

  ESP8266 用户 SDK 部分没有 main 函数。main 函数处于一级 bootloader 并且固化在芯片 ROM 中，用于引导二级 bootloader。二级 bootloader 入口函数为 ets_main，启动后会加载用户应用中的 user_init，引导至用户程序。

--------------

ESP8266 partition-tables 特殊注意点？
------------------------------------------

  ESP8266 partition-tables 相对 ESP32 对于 OTA 分区有一定的特殊要求，这是由于 ESP8266 cache 特性导致。详情参考 `ESP8266 partition-tables 偏移与空间 <https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/api-guides/partition-tables.html#offset-size>`_。

--------------

应用层与底层的 bin 文件可以分开编译吗？
-----------------------------------------

  不⽀持分开编译。

--------------

ESP32 模组 flash 使用 80 MHz 有什么注意事项吗？
------------------------------------------------------------

  乐鑫模组发售前已经过稳定性测试，测试可以支持 80 MHz 频率。根据稳定性测试数据，80 MHz 的频率不会影响使用寿命和稳定性。

--------------

使用 ESP-IDF 测试程序，如何设置可在单核模组上下载程序？
-------------------------------------------------------------------

  程序编译时，使用 ``make menuconfig`` 指令进入配置界面，进行如下配置，可在单核模组上下载程序；在配置界面中，按键 ``Y`` 为使能，``N`` 为关闭。

  ``Component config`` > ``FreeRTOS`` > ``Run FreeRTOS only on first core``

--------------

使用 ESP-IDF，如何使能 ESP32 的双核模式？
-----------------------------------------

  ESP-IDF 一般情况下默认配置的是双核模式，您可以在 menuconfig 中进行单双核的修改：``menuconfig`` > ``Component config`` > ``FreeRTOS`` > ``Run FreeRTOS only on first core`` 使能即为单核，未使能默认双核。

--------------

使用 ESP32-D0WD 芯片是否可以存储用户程序？
------------------------------------------

  不可以，用户程序必须使用外挂 flash 进行存储，片上 ROM 不能存储用户程序。ROM 内存放的程序为芯片一级 bootloader，为了保护出厂程序不被破坏，该区域为只读存储。

--------------

ESP32 进入低功耗模式时，PSRAM 中的数据会丢失吗？
-------------------------------------------------

  - Modem-sleep/Light-sleep 模式时，PSRAM 中的数据不会丢失。
  - Deep-sleep 模式时，CPU 和大部分外设都会掉电，PSRAM 的数据会丢失。

--------------

请问 ESP32 CPU 系统时间是否由系统滴答时钟生成？精度如何？
---------------------------------------------------------

  CPU 系统时间是由 esp_timer 内部的 64 位硬件定时器 CONFIG_ESP_TIMER_IMPL 产生的，是微秒级的时间分辨率。详情参见 `高精度时钟说明 <https://docs.espressif.com/projects/esp-idf/zh_CN/v4.4.2/esp32/api-reference/system/esp_timer.html#obtaining-current-time>`_。

--------------

ESP32 的 flash 和 PSRAM 的时钟频率如何修改？
--------------------------------------------

  在 menuconfig 中修改：

  - flash 时钟频率：``menuconfig`` > ``Serial flasher config`` > ``Flash SPI speed``。
  - PSRAM 时钟频率：``Component config`` > ``ESP32-specific`` > ``SPI RAM config`` > ``Set RAM clock speed``。

--------------

使用 ESP32-SOLO-1 模组，ESP-IDF 如何设置可在单核模组上运行？
------------------------------------------------------------

  使用 ``menuconfig`` 指令进入配置界面， ``Component config`` > ``FreeRTOS`` > ``Run FreeRTOS only on first core`` （启动此选项）可在单核模组上运行下载。

--------------

ESP-IDF 是否可以配置 time_t 为 64 bit ？（现在是 32 bit）
--------------------------------------------------------------

  ESP-IDF 从 v5.0 版本起开始使用有符号的 64 bit 来表示 time_t，详情参见 `Unix 时间 2038 年溢出问题 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/system/system_time.html#id5>`_。

--------------

固件如何区分主芯片是 ESP8285 还是 ESP8266？
-------------------------------------------

  通常使用外部工具 `esptool <https://github.com/espressif/esptool>`_ 来读取芯片类型。可以在固件中根据 Python 代码示例，读取芯片对应寄存器位，并进计算判断得出。

  .. code-block:: python

    def get_efuses(self):
    # Return the 128 bits of ESP8266 efuse as a single Python integer
    return (self.read_reg(0x3ff0005c) << 96 | self.read_reg(0x3ff00058) << 64 | self.read_reg(0x3ff00054) << 32 | self.read_reg(0x3ff00050))

    def get_chip_description(self):
      efuses = self.get_efuses()
      is_8285 = (efuses & ((1 << 4) | 1 << 80)) != 0  # One or the other efuse bit is set for ESP8285
      return "ESP8285" if is_8285 else "ESP8266EX"

--------------

ESP32 能否以动态库的方式加载库文件运行？
--------------------------------------------

  ESP32 不支持动态库的方式加载库文件，只支持静态库。

------------------

ESP32 如何减小系统对 IRAM 内存的占用？
--------------------------------------------------------------------

  - 请将 ``menuconfig`` > ``Component config`` > ``LWIP`` > ``Enable LWIP IRAM optimization`` (键 ``N`` 禁用) 配置选项禁用。
  - 请更改 ``menuconfig`` > ``Compiler option`` > ``Optimization Level`` > ``Optimize for size (-Os)`` 中的配置选项。
  - 请将 ``menuconfig`` > ``Component config`` > ``wifi`` 中的配置选项中的 ``WiFi IRAM speed optimization (N)`` 和 ``WiFi RX IRAM speed optimization (N)`` 配置选项禁用。
  - 更多细节请参考 `Minimizing RAM Usage <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/performance/ram-usage.html>`__。

----------------------

ESP32 芯片低电压复位阈值是多少？
------------------------------------------------------------

  欠压复位电压阈值范围在 2.43 V ~ 2.80 V 之间，可在 ``menuconfig`` > ``Component config`` > ``ESP32-specific`` > ``Brownout voltage level`` 中进行设置。

----------------

ESP32 light sleep 例程为何会自动唤醒？
----------------------------------------------------------------------------------------------------

  light sleep 例程下，默认使用了两种唤醒方式，如下：

  .. code-block:: c

    esp_sleep_enable_timer_wakeup(2000000);     // 2 秒自动唤醒
    esp_sleep_enable_gpio_wakeup();             // GPIO 唤醒

  GPIO 唤醒默认是 GPIO0 低有效唤醒，GPIO0 拉低则为唤醒状态，GPIO0 释放则自动进入 Light-sleep 模式。若需要长时间保存 Light-sleep 模式，可以将 2 秒自动唤醒屏蔽，仅开启 GPIO 唤醒。

---------------------

ESP32 deep_sleep 例程测试，为何当 const int wakeup_time_sec = 3600 时，程序 crash 出现死循环？
----------------------------------------------------------------------------------------------

  程序 crash 原因是 int 类型参数 `wakeup_time_sec` 在计算 ``wakeup_time_sec * 1000000`` 时溢出。

  .. code-block:: c

    const uint64_t wakeup_time_sec = 3600;
    printf("Enabling timer wakeup, %lldn",wakeuo_time_sec);

------------------

ESP32 有几种系统复位方式？
--------------------------------

  ESP32 有多种系统复位方式，包括以下几种：

  - 软件复位（Software Reset）：在应用程序中可以通过调用 esp_restart() 函数来进行软件复位。
  - 外部复位（External Reset）：通过外部硬件电路，例如按下 RESET 按键、供电电压不稳定等，触发 ESP32 的复位。
  - 硬件看门狗复位（Hardware Watchdog Reset）：当 ESP32 在运行时发生死锁或其他异常情况时，硬件看门狗模块会自动触发复位。
  - 欠压复位（Brownout Reset）：当系统电压不稳定或电源电压不足时，ESP32 内置的电源管理模块会自动触发复位。
  - 异常复位（Exception Reset）：当 ESP32 在运行时发生 CPU 异常，例如访问非法内存、运行非法指令等，会触发异常复位。
  - JTAG 复位（JTAG Reset）：当 ESP32 使用 JTAG 调试器进行调试时，可以通过 JTAG 复位信号进行复位操作。
  - 更多说明参见 `ESP32 技术参考手册 <https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_cn.pdf>`__ > 章节“复位源”。

--------------

ESP8266-NONOS-V3.0 版本的 SDK，报错如下，是什么原因？
-----------------------------------------------------------------

  .. code-block:: text

    E:M 536
    E:M 1528

  - 导致出现 E:M 开头的 LOG 是由于剩余内存不足。

--------------

ESP32 是否可以完整使用 8 MB PSRAM 内存？
-----------------------------------------------------------------

  - ESP32 可完整使用 8 MB PSRAM 内存。
  - 由于 cache 最大映射空间为 4 MB，所以仅支持 4 MB PSRAM 映射使用，剩余空间可以通过 API 操作使用。
  - 参考示例 `himem <https://github.com/espressif/esp-idf/tree/master/examples/system/himem>`_。

--------------

ESP8266 AT 连接 AP 后，系统默认进入 Modem-sleep，但电流未明显下降有哪些原因？
----------------------------------------------------------------------------------------

  - AT 固件连接 AP 后，ESP8266 会自动进入 Modem-sleep 模式，功耗大约会在 15 mA ~ 70 mA 之间波动。
  - 如果功耗并没有在 15 mA ~ 70 mA 之间波动，在示波器中未呈现波形的电流，有以下建议：
    - 擦除设备 flash 后，重新烧录 AT 固件。
    - 抓取网络包分析，是否在当前的网络环境中，是否有频繁发送广播包的设备，可换一个网络环境的路由器（AP）进行测试。

--------------

ESP32 是否可以永久更改 MAC 地址？
-----------------------------------------

  - 芯片自带的 MAC 地址无法修改。eFuse 中支持用户写入自己的 MAC 地址。
  - 在固件中调用 API 可以获取定制 MAC 地址，并且可以设置到系统中替代默认地址。
  - 配置参考：`mac-address <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v5.0/esp32/api-reference/system/misc_system_api.html#mac>`_。
  - 另外，Espressif 提供在芯片出厂之前，烧录用户提供的 MAC 地址服务。如有需要，可发送邮件至 sales@espressif.com。

--------------

ESP8266 进行 OTA 升级时如何校验 all.bin 为非法文件？
---------------------------------------------------------

  **问题背景：**

  - all.bin: 由 bootloader.bin，partition.bin 和 app.bin 合并生成。
  - ota.bin: 用于 OTA 升级的目标 bin 文件。

  使用 `simple_ota_example <https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/system/ota/simple_ota_example>`_ 进行 OTA 升级时，误从服务器上下载 all.bin，写入 OTA 分区之后，设备会出现反复重启的现象。

  **原因分析：**

  代码中未对 all.bin 进行校验，导致将非法的 bin 文件写入 OTA 分区。

  **解决方案：**

  通过打开 sha256 校验判断 all.bin 为非法 bin 文件，配置路径如下：``Component config`` > ``App update`` > ``[*] Check APP binary data hash after downloading``.

--------------

ESP-IDF 版本更新后，更新说明在哪里？
----------------------------------------------------------------------------------------

  可以在 `GitHub release note <https://github.com/espressif/esp-idf/releases>`_ 查看相关说明。

--------------

ESP8266 是否有详细的寄存器⼿册？
---------------------------------------

  请参考 `ESP8266 TRM <https://www.espressif.com/sites/default/files/documentation/esp8266-technical_reference_cn.pdf>`_ > 附录。

---------------

ESP32 开启 Secure Boot 后无法正常启动，出现如下报错，是什么原因？
-----------------------------------------------------------------------------------------------

  .. code-block:: text

    csum err:0x9a!=0x5f
    ets_main.c 371
    ets Jun  8 2016 00:22:57
    rst:0x10 (RTCWDT_RTC_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
    configsip: 0, SPIWP:0xee
    clk_drv:0x00,q_drv:0x00,d_drv:0x00,cs0_drv:0x00,hd_drv:0x00,wp_drv:0x00
    mode:DIO, clock div:2
    load:0x3fff0030,len:4
    load:0x3fff0034,len:9372
    load:0x40078000,len:19636

  可能是因为开启 Secure Boot 后 Bootloader 会变大，烧录固件时 bin 文件产生了覆盖。可以查询 Secure Boot 后 Bootloader 的大小，比如可以尝试把分区表的偏移量增大为 0xF000。

--------------

ESP8266 如何在设备软重启的情况下保留数据？
---------------------------------------------

  - 如果写入或者修改的次数不频繁，可以使用 flash 来存储数据，该区域相对于内存较大，并且容易调整。
  - 若数据较小，可以使用 RTC Memory 内存来存储相关数据。示例：Rel 2.1 的分支中 esp_system.h 中的接口（详细阅读使用说明）system_rtc_mem_read。
  - 如果以上两者都无法满足需求，也可以选择外挂的 RTC 内存，可以使用 I2C 与 SPI 进行交互。
  - 通常在写入频率不高的情况下建议写入 flash，因为该方法在硬断电时数据仍然正常。

--------------

ESP8266 有哪些定时器可用？
-----------------------------

  - ESP8266 有一个硬件定时器，可以产生中断，在 NONOS SDK 与 RTOS SDK 调用 API 略有不同。
  - 软件定时器：

    - NONOS 中 API os_timer 是 DSR 处理，不能产⽣中断，但是可以产⽣任务，任务会按照普通等级排队。
    - RTOS 中可以使用 FreeRTOS 中的软件定时器，使用方式更加灵活。

--------------

ESP8266 的看⻔狗是什么作⽤？
-----------------------------

  - 为了提供系统稳定性，以应对多冲突的操作环境，ESP8266 集成了 2 级看⻔狗机制，包括软件看⻔狗和硬件看⻔狗。
  - 默认 2 个看⻔狗都是打开的，HW WDT 始终在运行，并且如果未重置 HW WDT 计时器，则会在大约 6 秒钟后重置 MCU。
  - SW WDT 大约在 1.5 秒左右将 MCU 复位。您可以启用/禁用 SW WDT，但不能启用/禁用 HW WDT。因为必须重置 SW WDT 后才能同时重置 HW WDT。
  - 可通过修改 ``make menuconfig`` > ``Component config`` > ``Common ESP-related`` 里的 ``Invoke panic handler on Task Watchdog timeout`` 等来配置看门狗。

--------------

ESP8266 ``user_init`` 内有那些注意事项？
----------------------------------------

  - ``wifi_set_ip_info``、``wifi_set_macaddr`` 仅在 ``user_init`` 中调⽤⽣效，其他地⽅调⽤不⽣效。
  - ``system_timer_reinit`` 建议在 ``user_init`` 中调⽤，否则调⽤后，需要重新 arm 所有 timer。
  - ``wifi_station_set_config`` 如果在 ``user_init`` 中调⽤，底层会⾃动连接对应路由，不需要再调⽤ ``wifi_station_connect`` 来进⾏连接。否则，需要调⽤ ``wifi_station_connect`` 进⾏连接。
  - ``wifi_station_set_auto_connect`` 设置上电启动时是否⾃动连接已记录的路由；例如，关闭⾃动连接功能，如果在 ``user_init`` 中调⽤，则当前这次上电就不会⾃动连接路由，如果在其他位置调⽤，则下次上电启动不会⾃动连接路由。

-----------------

ESP32 同时开启 ``Enable debug tracing of PM using GPIO`` 和 ``Allow .bss segment placed in external memory`` 后为何会导致系统不停重启？
---------------------------------------------------------------------------------------------------------------------------------------------

  - ``Enable debug tracing of PM using GPIOs`` 配置选项是在 GDB 调试时需要打开的，不可与 ``Allow .bss segment placed in external memory`` 配置选项同时使用。
  - 因为 ``Enable debug tracing of PM using GPIOs`` 默认使用的是 GPIO16 与 GPIO17，与 PSRAM 接口（默认也是 GPIO16 和 GPIO17）冲突。

-----------------------

ESP32 IDF v3.3 版本 bootloader 运行 v3.1 版本 app bin，程序为何会触发 RTCWDT_RTC_RESET？
--------------------------------------------------------------------------------------------------------

  - 在 v3.3 的 bootloader 中会开启 WDT 看门狗，且在应用程序 (app) 运行时关闭 WDT 看门狗。
  - 但 v3.1 的 bootloader 没有开启 WDT 看门狗，所以应用程序 (app) 没有 WDT 看门狗的机制，进而导致 v3.3 的 bootloader 引导 v3.1 的应用程序 (app) 会触发 WDT 看门狗复位。
  - 可以通过在 ``menuconfig`` 中不使能 ``BOOTLOADER_WDT_ENABLE``，关闭 v3.3 版本 bootloader 中 WDT 看门狗开启。

-------------------

ESP32 芯片出厂是否有唯一的 chip_id？
-------------------------------------------------

  ESP32 芯片未未烧录唯一 chip_id，但设备默认烧录有全球唯一 MAC 地址，可以读取 MAC 地址替代 chip_id。

--------------

如何查看 ESP8266 重启原因？
--------------------------------------

  请参考 `ESP8266 异常重启原因 <https://www.espressif.com/sites/default/files/documentation/esp8266_reset_causes_and_common_fatal_exception_causes_cn.pdf>`_。

-----------------

ESP32 编译生成的 bin 文件大小如何优化？
--------------------------------------------------

  在 ESP32 编译生成的 bin 文件中，通常包括应用程序代码、分区表、ESP-IDF 固件和其他数据。为了优化 bin 文件的大小，可以采取以下几种方法：

  - 配置编译选项: 可配置 GCC 编译优化，操作步骤 ``idf.py menuconfig`` > ``Compiler options`` > ``Optimization level (Optimize for size(-Os))``。
  - 优化代码：可以对应用程序代码进行优化，例如采用更高效的算法和数据结构、精简代码逻辑和流程、提高代码复用率，调整 log 等级，减少不必要的 log 打印，减少代码文件大小。
  - 需要注意的是，在进行 bin 文件大小优化时，需要权衡优化效果和程序功能，避免优化过度导致程序异常或功能不完整。建议在进行 bin 文件大小优化时参考官方文档和示例，并遵循相关规定和标准。

  更多细节请参考 `Minimizing Binary Size <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/performance/size.html>`__。


-----------------

ESP32 是否有系统重新启动的 API？
------------------------------------------------------------------------------

  - 系统重新启动的 API 可使用 ``esp_restart()``，相关说明可 `参见 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/system/misc_system_api.html#_CPPv411esp_restartv>`__ 。

--------------

ESP32 异常 log ``invalid header: 0xffffffff``
--------------------------------------------------------

  ESP32 芯片打印该异常 log 通常有如下几种情况：

  - 芯片上下电时序不正确，芯片部分区域未完全复位。
  - flash 中的固件出现异常，例如未烧录完整固件。
  - flash 器件损坏，无法读取正确数据。
  - 芯片自身 cache 被关闭或者损坏，无法读取固件数据。

--------------

ESP8266 deep sleep 定时唤醒机制是什么？
----------------------------------------

  在 Deep-sleep 状态下，将 GPIO16 (XPD_DCDC) 连接至 EXT_RSTB，计时到达睡眠时间后，GPIO16 输出低电平给 EXT_RSTB 管脚，芯片被复位唤醒。

----------------------------------------

ESP32 使用 ``heap_caps_get_free_size`` 获取 RAM 约 300 KB，为何与手册 520 KB 存在差异？
------------------------------------------------------------------------------------------------------

  - 是因为内存在系统启动时预分配给各个功能模块使用，系统启动后剩余内存约 300 KB。
  - 如果剩余内存不足，可以选用带 PSRAM 模组，将内存分配在 PSRAM 中。

--------------

ESP32 & ESP8266 如何通过局域网的 app 进行 OTA 升级？
--------------------------------------------------------------

  - 局域网内 APP 设备可以配置开启 HTTP 服务，将提供的固件下载链接通过其他方法（UDP，CoAP，MQTT 等）发送至设备。
  - 设备通过传统 URL OTA 方法即可完成 OTA 更新，示例已在 SDK 中提供。

-----------------

ESP32 如何修改日志输出串口使用的 GPIO？
-------------------------------------------------------------------------------------------------

  - 配置 ``menuconfig`` > ``Component Config`` > ``ESP System Settings`` > ``Channel for console output`` > ``Custom UART``，选择自定义 UART 管脚。
  - 返回上一层，会看到出现 ``UART TX on GPIO#`` 和 ``UART RX on GPIO#`` 的选项，通过修改这两个选项可以更改日志输出串口使用的 GPIO。

-----------------

ESP8266 使用 MQTT ssl_mutual_auth 通讯，在 OTA 时出现如下报错：
----------------------------------------------------------------------------

  .. code::text

    W(50083) _http_event_handler：HTTP_EVENT_DISCONNECTED
    E(50089)esp_https_ota：Failed to open HTTP connection：28674
    E(50095)gateway_https_ota：Firmware upgrade failed
    E(50179)esp-tls-mbedtls: mbedtls_ssl_setup returned -0x7f00
    E(50181)esp-tls-mbedtls: mbedtls_ssl_handle failed
    E(50194)esp-tls：Failed to open a new connection

  - 0x7f00 此报错是由于内存不足导致，建议使用 HTTP 方式 OTA。

-----------------

ESP32 配置 ``menuconfig`` > ``Component config`` 中有 NVS 选项，为何配置项目为空？
-----------------------------------------------------------------------------------------

  - ``menuconfig`` > ``Component config`` 中的 NVS 选项是配置 NVS 加密功能的，该功能的前提是开启 flash 加密。
  - ``menuconfig`` > ``security feaures`` > ``enable flash encryption on boot`` 配置选项后，便可以看到 NVS 的配置选项。

--------------

ESP32 上电或 Deep-sleep 醒来后，会随机发⽣⼀次看⻔狗复位?
---------------------------------------------------------------------

  - 芯⽚上电的看⻔狗复位⽆法使⽤软件绕过，但复位后 ESP32 正常启动。
  - Deep-sleep 醒来后的看⻔狗复位在 ESP-IDF v1.0 及更⾼版本中⾃动绕过。
  - Deep-sleep 醒来后，CPU 可以⽴即执⾏ RTC fast memory 中的⼀段程序。RTC fast memory 中的这段程序通过清除 cache MMU 的⾮法访问标志从⽽绕过 Deep-sleep 醒来后的看⻔狗复位，具体为：

    - 将 ``DPORT_PRO_CACHE_CTRL1_REG`` 寄存器的 ``PRO_CACHE_MMU_IA_CLR`` ⽐特置 1。
    - 将该⽐特清零。

--------------

ESP32 CPU 使⽤ cache 访问外部 SRAM 时，如果这些操作需要 CPU 同时处理，可能会发⽣读写错误?
----------------------------------------------------------------------------------------------------

  - 这个问题⽆法使⽤软件⾃动绕过。
  - 对于版本 0 ESP32，CPU 使⽤ cache 访问外部 SRAM 时，只能够进⾏单向操作，即只能够单纯的进⾏写 SRAM 操作，或者单纯的进⾏读 SRAM 操作，不能交替操作。
  - 使⽤ MEMW 指令：在读操作之后，加上 ``__asm__("MEMW")`` 指令，然后在 CPU 流⽔线被清空前再发起写操作。

--------------

ESP32 CPU 频率从 240 MHz 直接切换到 80/160 MHz 会卡死，如何解决？
-----------------------------------------------------------------------------

  - 建议使⽤以下两种模式：

    (1) 2 MHz <-> 40 MHz <-> 80 MHz <-> 160 MHz
    (2) 2 MHz <->40 MHz <->240 MHz
  - 此问题已在芯⽚版本 1 中修复。

--------------

ESP32 同时有 GPIO 和 RTC_GPIO 功能的 pad 的上拉下拉电阻只能由 RTC_GPIO 的上拉下拉寄存器控制，如何解决？
------------------------------------------------------------------------------------------------------------------------

  - ESP-IDF v2.1 及更⾼版本的 GPIO 驱动⾃动绕过此问题。
  - GPIO 和 RTC_GPIO 都使⽤ RTC_GPIO 寄存器。

--------------

ESP32 由于 flash 启动的速度慢于芯⽚读取 flash 的速度，芯⽚上电或 Deep-sleep 醒来后，会随机发⽣⼀次看⻔狗复位，如何解决？
---------------------------------------------------------------------------------------------------------------------------------------------

  - 更换更快的 flash，要求 flash 上电到可读的时间⼩于 800 μs。这种⽅法可以绕过芯⽚上电和 Deep-sleep 醒来时的看⻔狗复位。
  - Deep-sleep 醒来后的看⻔狗复位问题在 ESP-IDF v2.0 及更⾼版本中⾃动绕过（延迟时间可以根据需要配置）。具体⽅式是从 Deep-sleep 醒来后⾸先读取 RTC fast memory 中的指令，等待⼀段时间，然后再读取 flash。

--------------

ESP32 CPU 在访问外部 SRAM 时会⼩概率发⽣读写错误, 如何解决？
-------------------------------------------------------------------------

  .. code::text

    store.x at0, as0, n
    load.y at1, as1, m
    其中 store.x 表示 x 位写操作，load.y 表示 y 位读操作，且 as0+n 和 as1+m 访问的外部 SRAM 的地址相同。

  - x>=y 时，在 store.x 和 load.y 之间插⼊ 4 个 nop 指令。
  - x<y 时，在 store.x 和 load.y 之间插⼊ memw 指令。

--------------

ESP32 双核情况下，⼀个 CPU 的总线在读 A 地址空间，⽽另⼀个 CPU 的总线在读 B 地址空间，读 B 地址空间的 CPU 可能会发⽣错误如何解决？
---------------------------------------------------------------------------------------------------------------------------------------------

  - ⼀个 CPU 在读 A 地址空间时，通过加锁和中断的⽅式来避免另⼀个 CPU 发起对 B 地址空间的读操作。
  - ⼀个 CPU 在读 A 地址空间之前，加⼀个此 CPU 读 B 地址空间（⾮ FIFO 地址空间，如 0x3FF40078）操作，并且要保证读 B 地址空间操作和读 A 地址空间操作是原⼦的。

--------------

ESP32 CPU 通过读取 ``INTERRUPT_REG`` 寄存器来复位 CAN 控制器的中断信号。如果在同⼀个 APB 时钟周期内 CAN 控制器刚好产⽣发送中断信号，则发送中断信号丢失，如何解决？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  数据等待发送完成期间（即发送请求已发起），每⼀次读取 ``INTERRUPT_REG`` 后，⽤户都应检查 ``STATUS_TRANSMIT_BUFFER`` 位。如果 ``STATUS_TRANSMIT_BUFFER`` 置位⽽ ``CAN_TRANSMIT_INT_ST`` 没有置位，则说明发送中断信号丢失。在 ESP32 中，可以通过读取 ``INTERRUPT_REG`` 寄存器来复位 CAN 控制器的中断信号。但是如果在同一个 APB 时钟周期内 CAN 控制器产生发送中断信号，该中断信号可能会丢失，因为 ESP32 在该时钟周期内读取该寄存器时可能已经被清除。为了解决这个问题，可以使用以下方法：

  - 添加延时：在读取 ``INTERRUPT_REG`` 寄存器之前，可以添加一定的延时，以确保 CAN 控制器的中断信号已经被清除。可以通过试验和调整来确定适当的延时时间。
  - 使用中断处理程序：可以使用中断处理程序来处理 CAN 控制器的中断信号，并避免在同一个 APB 时钟周期内读取 ``INTERRUPT_REG`` 寄存器。中断处理程序可以及时响应 CAN 控制器的中断信号，保证信号不会丢失。
  - 使用其他寄存器：可以使用其他寄存器来复位 CAN 控制器的中断信号，以避免在同一个 APB 时钟周期内读取 ``INTERRUPT_REG`` 寄存器。例如，可以使用 ``CANCTRL`` 寄存器或 ``ERRCNT`` 寄存器等。

  需要注意的是，在使用以上方法时，需要根据具体应用场景和需求来选择和实现。同时，也需要对软件和硬件进行充分的测试和验证，以确保系统的可靠性和稳定性。在 ESP32 中复位 CAN 控制器的中断信号时，需要注意避免中断信号丢失的问题，以保证系统的正常运行。

--------------

ESP32 v3.0 芯⽚，当程序同时满⾜下列条件时，会出现 live lock（活锁）现象，导致 CPU ⼀直处于访存状态，不能继续执⾏指令，请问如何解决？
-----------------------------------------------------------------------------------------------------------------------------------------------

  请参见 `ESP32 系列芯片勘误表 <https://www.espressif.com/sites/default/files/documentation/esp32_errata_cn.pdf>`__ > 3.15 小节。

--------------

ESP32 CPU 访问 ``0x3FF0_0000 ~ 0x3FF1_EFFF`` 与 ``0x3FF4_0000 ~ 0x3FF7_FFFF`` 两段地址空间存在限制，如何解决？
-----------------------------------------------------------------------------------------------------------------------

  请参见 `ESP32 系列芯片勘误表 <https://www.espressif.com/sites/default/files/documentation/esp32_errata_cn.pdf>`__ > 3.16 小节。

------------------

ESP32 如何关闭程序 LOG 输出？
--------------------------------------------------------------------

  - 关闭 bootloader 日志：``menuconfig`` > ``bootloader config`` > ``bootloader log verbosity`` 选定为 ``No output``。
  - 关闭程序日志：``menuconfig`` > ``Component config`` > ``log output`` > ``Default log verbosity`` 选定为 ``No output``。
  - 在 ESP-IDF release/v4.3 及之前的版本中关闭 UART0 输出日志：``menuconfig`` > ``Component Config`` > ``Common ESP-related`` > ``Channel for console output`` > ``None``。
  - 在 ESP-IDF release/v4.4 及之后的版本中关闭 UART0 输出日志：``Component config`` > ``ESP System Settings`` > ``Channel for console output`` > ``None``。

------------------

ESP8266 在 Deep-sleep 模式下，保存在 RTC Memory 里的数据是否可运行？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ESP8266 在 Deep-sleep 模式下只有 RTC 定时器继续工作，保存在 RTC Memory 里的数据在 Deep-sleep 模式下不会运行，只能保持数据不会丢失。但是，当 ESP8266 掉电后，保存在 RTC memory 里的数据无法保存。

------------------

ESP32 的 NVS 的 Key 的最大长度为多大？
----------------------------------------------------------------------------------------------

  - ESP32 的 NVS 的 Key 最大长度为 15 个字符，且无法更改 Key 的最大长度。可参见 `键值对 <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.3/esp32/api-reference/storage/nvs_flash.html#id4>`_ 说明。
  - 可使用 `nvs_set_str() <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.3/esp32/api-reference/storage/nvs_flash.html#_CPPv411nvs_set_str12nvs_handle_tPKcPKc>`_ 的 value 来存数据。

------------------

ESP-IDF release/v4.2 里的 cJSON 支持 uint64_t 的数据解析吗？
-------------------------------------------------------------------------------------

  不支持。cJSON 库解析长整形有限制，最长只有 Double 类型。

---------------

未启用 flash 加密的 ESP32 可以进行 GDB 调试，但启动 flash 加密后进行 GDB 调试时，设备一直重启，是什么原因？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  启用 flash 加密或安全启动 (secure boot) 后，将默认禁用 JTAG 调试功能，更多信息请参考 `JTAG 与闪存加密和安全引导 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/jtag-debugging/tips-and-quirks.html#jtag-debugging-security-features>`_。

---------------

ESP32 使用手机热点进行 OTA 固件下载时，关闭流量开关几秒后再次打开会出现程序一直卡死在 OTA 里的情况（使用路由器时插拔 WAN 口网线同理），是什么原因？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 这是协议的正常现象。如果使用 ``esp_https_ota`` 组件进行 OTA，可以设置网络超时时间 ``http_config->timeout_ms`` 为 10 ~ 30 秒（不建议太小），使能 ``http_config->keep_alive_enable`` 来检测链路是否异常。
  - 对于用户自行实现的 OTA 模块，按照上述思路，通过 ``select`` 机制添加读取超时或者使能 TCP Keep-alive 链路检测机制。

------------------

ESP32-C3 在 Deep-Sleep 模式下可以通过哪些 GPIO 进行唤醒？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ESP32-C3 仅有 VDD3P3_RTC 域中的管脚 (GPIO0 ~ GPIO5) 可用于将芯片从 Deep-sleep 唤醒。请阅读`《ESP32-C3 技术参考手册》 <https://www.espressif.com/sites/default/files/documentation/esp32-c3_technical_reference_manual_cn.pdf>`_ 中“5.9.1 GPIO 管脚供电” 章节的说明。

---------------------

使用 ESP-WROOM-02D 模组，电池供电，在低电量（模组勉强启动）的时候，频繁格式化读写 flash 有什么风险吗？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  在低电量情况下频繁进行格式化和读写 flash 存储器可能会有一些风险。它在低电量情况下可能无法正常工作或容易发生错误，如果在这种情况下频繁进行格式化和读写 flash 存储器，可能会导致以下风险：

  - 数据丢失或损坏：在低电量情况下，flash 存储器可能无法正常写入数据。如果频繁进行格式化和读写操作，可能会导致数据丢失或损坏。
  - 模组崩溃或损坏：低电量情况下频繁进行格式化和读写 flash 存储器会消耗模组的电量，可能会导致模组崩溃或损坏。

  因此，建议在低电量情况下尽量减少对 flash 存储器的访问和操作，避免频繁进行格式化和读写操作。如果需要进行格式化和读写操作，应确保模组有足够的电量，并在操作前先备份数据以防止数据丢失。此外，建议使用低功耗模式和优化代码以尽可能减少电量消耗。

---------------------

ESP32 如何查看线程使用过的最大栈大小？
-----------------------------------------------------------------------------------------------------------

  可以调用 `UBaseType_t uxTaskGetStackHighWaterMark( TaskHandle_t xTask ) <https://www.freertos.org/uxTaskGetStackHighWaterMark.html>`_ 函数来查看。该函数可以返回任务启动后的最⼩剩余堆栈空间。

-------------------

使用 ESP32 时打印 "SW_CPU_RESET" 日志是什么原因？
----------------------------------------------------------------------------------------------------------------------------------------------------------------

  在 ESP32 上，打印出 “SW_CPU_RESET” 日志通常是由于程序异常终止导致的。
  ESP32 内置了两个处理器内核，即主核和辅助核。在某些情况下，如果程序在主核上执行，并且出现了一些异常情况，例如访问非法地址或发生未处理的中断，可能会导致主核进入异常状态并重新启动。当这种情况发生时，ESP32 会在串行终端（UART）上打印 “SW_CPU_RESET” 日志。
  此外，使用 ESP-IDF 开发应用程序时，也可能会在应用程序中调用 ``esp_restart()`` 函数来重新启动 ESP32。在这种情况下，ESP32 也会在串行终端上打印 “SW_CPU_RESET” 日志。
  需要注意的是，出现 “SW_CPU_RESET” 日志并不一定意味着程序有问题或 ESP32 硬件有故障。它可能只是由于某些异常情况导致的正常现象。但是，如果程序频繁出现异常并重新启动，需要进行调试和排除问题。可以通过检查程序日志和硬件设备状态来确定问题的原因。

----------------

使用 ESP32 时，单独测试 NVS 发现占用内存很大，是什么原因？
-----------------------------------------------------------------------------------------------------------------------------------------------

  请检查分区表设置，建议将分区表中的 NVS 数据分区设置小一些来测试，NVS 数据分区设置越大占用内存越多。

-----------------------------------------------------------------------------------------------------

如何修改模块的系统时间?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32 | ESP32 | ESP32-C3:

  - 可以使用 c 语言 ``time()`` 接口来设置系统时间。

----------------------------------------------------------------------------------------

OTA 升级过程中 ``esp_ota_end`` 返回 ``ESP_ERR_OTA_VALIDATE_FAILED`` 报错，如何排查这类问题?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32:

  - 一般是由于下载的固件内容有误导致的，可以通过 `esptool <https://github.com/espressif/esptool>`_  中的  `read_flash <https://docs.espressif.com/projects/esptool/en/latest/esp32/esptool/basic-commands.html#read-flash-contents-read-flash>`_  指令 dump 出模组中的内容，然后再用 Beyond Compare 工具对这 2 个 bin 文件进行 16 进制对比，看 bin 文件哪里下载有误。

-------------

ESP8266-RTOS-SDK 如何将数据存储在 RTC memory 中？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 将数据存储在 RTC memory 中的定义方式如下：

  .. code:: text

      #define RTC_DATA_ATTR _SECTION_ATTR_IMPL(".rtc.data", __COUNTER__)

  - 可参见 `esp_attr.h <https://github.com/espressif/ESP8266_RTOS_SDK/blob/release/v3.4/components/esp8266/include/esp_attr.h>`__ 文件说明。

---------------

在 Deep-sleep 模式唤醒后，ESP8266 是从哪里启动的？
---------------------------------------------------------------------------------

  ESP8266 在 Deep-sleep 模式唤醒后，设备将从 user_init 启动。请参见 `esp_deep_sleep() <https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/api-reference/system/sleep_modes.html?highlight=deep#_CPPv414esp_deep_sleep8uint64_t>`__ 说明。

---------------

RTC 时钟什么时候会被重置？
---------------------------------------------------------------------------------

  除上电复位外的任何睡眠或者复位方式都不会重置 RTC 时钟。

-------------------

ESP32 使用 ``AT+GSLP`` 指令进入 Deep-sleep 模式后，是否可通过拉低 EN 进行唤醒？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 使用 ``AT+GSLP`` 指令进入 Deep-sleep 模式后，可以通过拉低 EN 唤醒，但不推荐此做法。
  - Deep-sleep 模式可通过 RTC_GPIO 来唤醒。请参见 `《ESP32 技术参考手册》 <https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_cn.pdf>`__。

----------------

当多个线程要使用 ESP32 的看门狗时，是否每个线程都要开启看门狗？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  当多个线程要使用看门狗时，每个线程都要开启看门狗。可参见 `任务看门狗说明 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/system/wdts.html?highlight=wdt#task-watchdog-timer>`_。

-----------------------------

使用 ESP8266-RTOS-SDK release/v3.3，如何进入 Light-sleep 模式？
------------------------------------------------------------------------------------------------------------------------------------

  - 先设置 Light-sleep 模式的唤醒模式，可参考 `ESP8266_RTOS_SDK/components/esp8266/include/esp_sleep.h <https://github.com/espressif/ESP8266_RTOS_SDK/blob/release/v3.3/components/esp8266/include/esp_sleep.h>`_。
  - 然后使用 `esp_light_sleep_start() <https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/api-reference/system/sleep_modes.html?highlight=esp_light_sleep_start%28%29#_CPPv421esp_light_sleep_startv>`_ API 进入 Light-sleep 模式。
  - 程序实现逻辑可以参考 `esp-idf/examples/system/light_sleep/main/light_sleep_example_main.c <https://github.com/espressif/esp-idf/blob/release/v4.2/examples/system/light_sleep/main/light_sleep_example_main.c>`_ 例程。
  - ESP8266-RTOS-SDK 关于 Sleep 模式的 API 说明请阅读 `Sleep modes API Reference <https://docs.espressif.com/projects/esp8266-rtos-sdk/en/release-v3.3/api-reference/system/sleep_modes.html#sleep-modes>`_。

-----------------------------

ESP8266 在 Deep-sleep 模式下如何唤醒？
-------------------------------------------------------------------------------------------------------------------------

  ESP8266 在 Deep-sleep 模式下只能通过 RTC Timer 进行唤醒，定时时长为用户通过函数 ``esp_deep_sleep()`` 设置的时间，且硬件上需要把 GPIO16 (XPD_DCDC) 通过 0 欧姆电阻连接到 EXT_RSTB，以支持 Deep-Sleep 模式唤醒。请参见 `相应 API 唤醒说明 <https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/api-reference/system/sleep_modes.html?highlight=deep#_CPPv414esp_deep_sleep8uint64_t>`_。

-----------------

使用 ESP32-WROVER\ :sup:`*` 模组，休眠时存在电池抖动或异常掉电上电导致死机无法唤醒的问题，是什么原因？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 应用场景：休眠的时候电流大概是 12 uA, 当拔电池或震动摇晃产品的时候会造成掉电，但是电容里还有电，ESP32 从 3.3 V 放电到 0 V 的过程中，再上电恢复 3.3 V 会导致 ESP32 无法唤醒。

  - 请检查芯片 VCC 与 EN 是否满足上电时序要求。
  - 在使用 ESP32-WROVER\ :sup:`*` 模组进行休眠时，如果存在电源电压不稳定或异常掉电的情况，可能会导致芯片的电源管理单元出现问题，导致无法正常唤醒。
  - 可以考虑添加复位芯片保证时序正常。
  - ESP32 上电、复位时序说明，详见 `《ESP32 技术规格书》 <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf>`_。

  \ :sup:`*` 表示该产品处于生命周期终止状态。

--------------

如何烧录自定义 Mac 地址？
---------------------------------------------

  可以先了解 ESP 模块 Mac 的机制，请参考 `Mac 地址介绍 <https://docs.espressif.com/projects/esp-idf/en/latest/api-reference/system/system.html?highlight=MAC%20address/>`_。目前烧录自定义 Mac 地址有 2 种方案：

  - 方案 1：直接烧到 eFuse blk3 中，可以保证不被修改；
  - 方案 2：存储到 flash 中。不推荐将 Mac 地址存放在默认 NVS 分区中，建议创建一块自定义的 NVS 分区用来存储自定义的 Mac 地址。关于自定义 Mac 地址的使用，可以参考 `base_mac_address <https://github.com/espressif/esp-idf/tree/master/examples/system/base_mac_address/>`_。

---------------

ESP32 在使用 esp_timer 时，出现网络通信或者蓝牙通信异常，是什么原因？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - esp_timer 是高精度的硬件定时器组件，后台一些组件也使用 esp_timer 完成一些系统任务。在使用 esp_timer 时，请不要在该定时器的回调函数中使用延时、阻塞类的 API，应尽可能地保证回调函数能够快速地被执行结束，以免影响系统其他组件的功能。
  - 如您需要的定时精度不是太高，请使用 FreeRTOS 中的定时器组件 `xTimer <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/system/freertos_idf.html#id33>`_。

--------------

使用 ESP32，请问 ULP 里面用 ``jump`` 跳转到一个函数，是否有返回的指令？
----------------------------------------------------------------------------------------

  目前 ULP CPU 指令列表以及说明参见 `这里 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/ulp_instruction_set.html>`_。返回指令通常使用一个通用寄存器备份 PC 地址，用于后续跳回，由于目前 ULP 只有 4 个通用寄存器，所以需要合理使用。

--------------

如何调整编译的警告级别？
-----------------------------------------------------------

  编译工程时，发现一些警告被视为错误，导致编译失败，如下：

  .. code:: text

    error: format '%d' expects argument of type 'int *', but argument 3 has type 'uint32_t *' {aka 'long unsigned int *'} [-Werror=format=]

  针对于上述错误，用户可以在组件级别（在组件 CMakeLists.txt 中）或项目级别（在项目 CMakeLists.txt 中）修改编译标志，这两种方式的效果大致相同。

  - 要修改特定组件的编译标志，请使用标准 CMake 函数 ``target_compile_options``。请参考 `组件编译控制 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/build-system.html#component-build-control>`_。组件级别的 ``target_compile_options`` 示例请见 `CMakeLists.txt#L3 <https://github.com/espressif/esp-idf/blob/4d14c2ef2d9d08cd1dcbb68a8bb0d76a666e2b4b/examples/bluetooth/bluedroid/ble/ble_ancs/main/CMakeLists.txt#L3>`_。
  - 要修改整个项目的编译标志，请使用标准 CMake 函数 ``add_compile_options`` 或 IDF 特定函数 ``idf_build_set_property`` 来设置 ``COMPILE_OPTIONS`` 属性。请参考 `覆盖默认的构建规范 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/build-system.html#id11>`_。

-----------------

基于 ESP-IDF SDK 编译固件时，会包含 ``IDF_PATH`` 的信息和存储编译时间，导致编译的 bin 不一样。如何删除这些信息？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 如果是 v5.0 及以上版本的 SDK，可以开启 ``CONFIG_APP_REPRODUCIBLE_BUILD`` 配置选项，开启后，使用 ESP-IDF 构建的应用程序不依赖于构建环境。应用程序的 .elf 文件和 .bin 文件都保持完全相同，即使以下变量发生变化：

    - 项目所在目录
    - ESP-IDF 所在目录（IDF_PATH）
    - 构建时间

    详情参见 `Reproducible Builds <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/reproducible-builds.html#reproducible-builds>`_ 说明。

  - 如果是 v5.0 以下版本的 SDK，可以关闭 ``CONFIG_APP_COMPILE_TIME_DATE=n`` 配置，来删除编译时间戳信息，并且开启 ``COMPILER_HIDE_PATHS_MACROS=y`` 配置来隐藏 IDF_PATH。

-------------------

使用 ESP32-S3-DevKitM-1 开发板下载官方 hello_world 例程后出现如下报错，是什么原因？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code:: text

    ESP-ROM:esp32s3-20210327
    Build:Mar 27 2021
    rst:0x7 (TG0WDT_SYS_RST),boot:0x8 (SPI_FAST_FLASH_BOOT)
    Saved PC:0x40043ac8
    Invalid chip id. Expected 9 read 4. Bootloader for wrong chip?
    ets_main.c 329


  - 当前报错可能与开发板上的芯片版本或 ESP-IDF SDK 的软件版本不是正式量产版本有关。芯片 (ROM) 引导加载程序预期芯片 ID 为 9，这是芯片的量产版本（不是测试版本）。然而，在二级引导加载程序标头中，它看到了芯片 ID 为 4，这是 beta 版本的芯片。可参考`这里 <https://github.com/espressif/esp-idf/issues/7960>`_ 的说明。
  - 可以通过 ``esptool.py chip_id`` 命令来查询芯片的实际版本。如果芯片版本是量产版本，那么该报错与所使用的 ESP-IDF SDK 版本有关。ESP32-S3 系列的产品请使用 ESP-IDF release/v4.4 及以上版本的软件环境。

--------------

请问 ESP32 芯片的内部 150 kHz 的 RTC 时钟精度是多大？
---------------------------------------------------------------------------------------------------------------------------

  ESP32 芯片内部 150 kHz 的 RTC 时钟精度为 ±5%。

-------------

ESP32-D0WDR2-V3 芯片支持的 ESP-IDF SDK 的版本有哪些？
---------------------------------------------------------------------------------------------------------

  支持 ESP-IDF 版本是：v4.4.1、v4.3.3、v4.2.3、v4.1.3。

---------------

基于 ESP32 芯片测试 OTA 应用，是否可以删除分区表里默认存在的 factory 分区，将 OTA_0 分区的地址设置为 0x10000?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  可以省略 factory 分区并将 OTA_0 分区的地址设置为 0x10000，需要注意任何 app 类型的分区的偏移地址必须要与 0x10000 (64K) 对齐。

为什么使用 ``espefuse.py burn_key`` 命令无法烧录 ESP32-C3 eFuse 的 BLOCK3？
---------------------------------------------------------------------------------------------------------

  - ``espefuse.py burn_key`` 命令只能向类型为 KEY_DATA 的 eFuse 块烧录数据，但是默认情况下 ESP32-C3 的 BLOCK3 为 USR_DATA 类型。
  - 可以通过 ``espefuse.py burn_block_data`` 命令向 USR_DATA 类型的 eFuse 块烧录数据。

-------------

基于 ESP-IDF SDK 运行固件后打印如下报错是什么原因？
------------------------------------------------------------------------------------------

  .. code:: text

    ***ERROR*** A stack overflow in task sys_evt has been detected.

  当前报错是由于 system_event 任务堆栈不足导致的，可尝试增大 ``Component config`` > ``ESP System Setting`` > ``Event loop task stack size`` 设置来进行测试。不过出现溢出是在 system_event 事件中处理了太多的逻辑，这种行为本身是不提倡的，可能会导致后序事件无法及时抛出来。我们建议是通过队列或者其他操作将这个事件抛给其他任务处理。

----------------------------

Wi-Fi OTA 时，指定 url 中有空格导致无法解析，如何解决？
--------------------------------------------------------------------------------------------------------------------------------------------------------

  可以将空格替换成 ``+`` 或者 ``%20`` 来解决。

----------------------------

如何查看 ESP-IDF 中 newlib 的版本号？
--------------------------------------------------------------------------------------------------------------------------------------------------------

  - 可使用以下两种方式可以获取版本号：

    - 1. 在 ESP-IDF 环境中运行 `xtensa-esp32-elf-gcc -dM -E -x c - <<< "#include <_newlib_version.h>" | grep NEWLIB_VERSION` 命令去获取 newlib 版本号，将打印类似以下内容： `#define _NEWLIB_VERSION "4.1.0"`。
    - 2. 在工具链版本中查找 newlib 版本，查找 ESP-IDF 使用的工具链版本。例如，对于 ESP-IDF v5.0，从 `xtensa-esp32-elf <https://docs.espressif.com/projects/esp-idf/en/v5.0/esp32/api-guides/tools/idf-tools.html#xtensa-esp32-elf>`_ 可以得知工具链版本为 esp2021-r1，转到 `该工具链版本 <https://github.com/espressif/crosstool-NG/releases/tag/esp-2022r1>`_ 的发行说明页面，从链接中可以获知 newlib 版本为 v4.1.0。

--------------

ESP32-P4 是否支持浮点运算？
-------------------------------------------------------------------------------------------

  - ESP32-P4 HP CPU 支持浮点运算；LP CPU 不支持浮点运算。

-----------

不同系列的 ESP32 芯片版本对应的 ESP-IDF SDK 版本是什么？
-------------------------------------------------------------------------------------------------------------------

  - 请参见 `ESP-IDF 版本与乐鑫芯片版本兼容性 <https://github.com/espressif/esp-idf/blob/master/COMPATIBILITY_CN.md>`_ 说明。

------------

如何查看 ESP-IDF 中定义的各种错误代码说明？
------------------------------------------------------------------------------------------------------------------------------------

  - 参见: `错误代码参考说明 <https://docs.espressif.com/projects/esp-idf/zh_CN/v5.0.3/esp32c3/api-reference/error-codes.html#error-codes-reference>`__。

------------

固件运行出现如下日志报错，通常是什么原因？
----------------------------------------------------------------------------------------------

  .. code:: text

    Guru Meditation Error: Core  1 panic'ed (Unhandled debug exception).
    Debug exception reason: Stack canary watchpoint triggered (zcr_task)

  - 上述日志报错通常是由于栈溢出导致的。可以尝试增大 zcr_task 任务的栈大小 。
  - 更多软件异常说明参见 `严重错误 <https://docs.espressif.com/projects/esp-idf/zh_CN/v5.2/esp32/api-guides/fatal-errors.html#id1>`__。

---------------------------------------------

ESP 芯片是否支持用 `esp-bootloader-plus <https://github.com/espressif/esp-bootloader-plus>`__ 压缩升级方案给其他 MCU 升级呢？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  不可以。对其他 MCU 进行压缩更新是用户需要考虑的事情。在 ESP32 的压缩更新中，其解压过程发生在引导启动程序阶段，而不是应用程序阶段，自然无法直接对其他 MCU 的数据进行解压。但是，可以先在 ESP32 上的应用程序中解压数据，再将解压后的数据发送到其他 MCU。用户可以自行实现这一过程，详情请参考 `xz_decompress_file <https://github.com/espressif/esp-iot-solution/tree/master/examples/utilities/xz_decompress_file>`__ 解压示例。

------------

基于 ESP32 进行软件开发，如何获取任务状态、任务优先级、任务剩余栈以及任务使用的核心等信息？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 可以基于 FreeRTOS 使用 `vTaskList() <https://docs.espressif.com/projects/esp-idf/zh_CN/v5.2.1/esp32s3/api-reference/system/freertos_idf.html#_CPPv49vTaskListPc>`_ 函数来获取任务的相关信息。

------------------

使用 ESP32 进行软件开发，如何获取任务的 CPU 使用率？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 可以基于 FreeRTOS 使用 `vTaskGetRunTimeStats() <https://docs.espressif.com/projects/esp-idf/en/v5.2.1/esp32s3/api-reference/system/freertos_idf.html#_CPPv420vTaskGetRunTimeStatsPc>`__ 获取系统任务的 CPU 使用率。

------------------

基于 ESP32 下载固件后无法正常启动，出现如下报错是什么原因？
-----------------------------------------------------------------------------------------------------------

  .. code:: text

   E(88)flash parts: partition 0 invalid magic number 0x5e9
   E(95)boot: Failed to verify partition table
   E(100)boot: load partition table error!

  - 上述日志报错通常是由于下载的 ``partition-table.bin`` 的地址与实际软件上的 ``Partition Table`` > ``Offset of partition table`` 设置不匹配导致的，即 ``partition-table.bin`` 的下载地址错误。
  - 工程编译完成后会生成 ``build`` 文件夹，在 ``build`` 文件夹下有一个 ``flash_project_args`` 文件，此文件将存储工程编译生成的 ``bin`` 文件和对应的下载地址信息。

---------------

是否支持将 ESP32 的 UART0 输出日志重定向到文件系统？
-----------------------------------------------------------------------------------------------------------------------------------------------------

  支持。可通过 `esp_log_set_vprintf <https://docs.espressif.com/projects/esp-idf/zh_CN/v5.2.2/esp32/api-reference/system/log.html?highlight=esp_log_set_%20vprintf#_CPPv419esp_log_set_vprintf14vprintf_like_t>`_ API，将 UART0 输出日志重定向到文件。

----------------

ESP32 的 BootLoader 配置为单核运行，可以通过 OTA 升级为双核运行吗？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
  - ESP32 不支持。因为 ESP32 的每个 CPU 都有独立的 cache, 而 cache 对应的 MMU 配置是在 BootLoader 中完成的。如果 BootLoader 配置为单核，但第二内核的 MMU 未被配置，则会导致取指出错。
  - ESP32-S3 和 ESP32-P4 支持。ESP32-S3 和 ESP32-P4 是两个内核共用同一套 cache，不存在上述问题，支持从单核升级为双核。

----------------

ESP32 系列芯片是否支持通过文件传输协议 (FTP) 进行 OTA 固件更新？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
  默认示例不支持基于 TLS 的 FTP，仅支持基础的套接字编程。但 ESP32 系列芯片支持基于 TLS 的 FTP，用户可以根据需要自行实现该功能。

----------------

使用 native_ota_example 示例进行 OTA 升级后，设备进入 ESP_OTA_IMG_UNDEFINED 事件，ota_state 值打印为 -1，但固件能正常使用，这是为什么？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
  这可能是由于 menuconfig 中未开启应用回滚功能。请确保在配置中启用应用回滚功能，以避免此问题。