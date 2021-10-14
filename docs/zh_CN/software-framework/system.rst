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

  当前 SDK 仅⽀持关闭软件看⻔狗，⽀持同时喂软硬件看⻔狗。可以通过如下⽅式防⽌执⾏时间过⻓的⽤户程序导致看⻔狗复位

  - 如果⼀个程序段运⾏时间在触发软件看⻔狗和触发硬件看⻔狗复位之间，则可通过 system_soft_wdt_stop() 的⽅式关闭软件看⻔狗，在程序段执⾏完毕后⽤ system_soft_wdt_restart() 重新打开软件看⻔狗。
  - 可以通过在程序段中添加 system_soft_wdt_feed() 来进⾏喂软硬件狗操作，防⽌软硬件看⻔狗复位。
  - 硬件看⻔狗中断时间为 0.8 *2048 ms，即 1638.4 s，中断后处理时间为 0.8* 8192 ms，即 6553.6 ms。
  - 其中中断处理后时间为硬件看⻔狗中断发⽣后，需要进⾏喂狗操作的时间，如果超过该时间，即会触发硬件看⻔狗复位。
  - 因此，在仅有硬件看⻔狗的情况下，⼀个程序段如果运⾏时间超过 6553.6 ms，即有可能触发硬件看⻔狗复位，若超过 8192 ms 则⼀定会触发复位。
  - 软件看⻔狗建⽴在 MAC timer 以及系统调度之上，中断时间为 1600 ms，中断后处理时间 1600 ms。
  - 因此，在有软件+硬件看⻔狗的情况下，⼀个程序段如果运⾏时间超过 1600 ms，即有可能会触发软件看⻔狗复位，若超过 3200 ms 则⼀定会触发复位。

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

ESP8266 启动时 LOG 输出 ets_main.c 有哪些原因？
------------------------------------------------

  ESP8266 启动时打印 ``ets_main.c`` ，表示没有可运⾏的程序区，⽆法运⾏；遇到这种问题时，请检查烧录时的 bin ⽂件和烧录地址是否正确。

--------------

ESP8266 编译 Non-OS SDK 时 IRAM_ATTR 错误是什么原因？
------------------------------------------------------

  如果需要在 IRAM 中执⾏功能，就不需要加 ``ICACHE_FLASH_ATTR`` 的宏，那么该功能就是放在 IRAM 中执⾏。

--------------

ESP8266 main 函数在哪里？
-------------------------

  ESP8266 用户 SDK 部分没有 main 函数。main 函数处于 一级 bootloader 并且固化在芯片 ROM 中， 用于引导二级 bootloader。二级 bootloader 入口函数为 ets_main，启动后会加载用户应用中的 user_init，引导至用户程序。

--------------

ESP8266 partition-tables 特殊注意点？
------------------------------------------

  ESP8266 partition-tables 相对 ESP32 对于 ota 分区有一定的特殊要求，这是由于 ESP8266 cache 特性导致。详情参考 `ESP8266 partition-tables 偏移与空间 <https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/api-guides/partition-tables.html#offset-size>`_。

--------------

应用层与底层的 bin 文件可以分开编译码？
-----------------------------------------

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

  - 如果单纯使用读写寄存器指令或者汇编指令，不存在调用库文件的问题。如果调用 esp-idf 预制的函数，则可能会遇到调用 lib 函数的情况。
  - 不推荐在 ESP32 中使用汇编操作，如果部分场景想要提高速度，可以读写寄存器来完成部分操作。

--------------

使用 ESP-IDF 测试程序，如何设置可在单核模组上下载程序？
-------------------------------------------------------------------

  程序编译时，使用 make menuconfig 指令进入配置界面，进行如下配置，可在单核模组上下载程序；在配置界面中，按键 Y 为启动，N 为关闭。

  - ``Component config --> FreeRTOS --> Run FreeRTOS only on first core``

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

  CPU 系统时间是由 esp_timer 内部的 64 位硬件定时器 CONFIG_ESP_TIMER_IMPL 产生的，是微秒级的时间分辨率。
  参见 `说明 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/system/esp_timer.html?highlight=esp_timer_get_time#high-resolution-timer>`_。

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

esp-idf 是否可以配置 time_t 为 64 bit ？ （现在是 32 bit）
--------------------------------------------------------------

  当前暂时不支持，预计在 release/v4.2 或更高版本种支持。如果配置支持 time_t 64 bit 自定义工具链，可以使能 make menuconfig 中 SDK tool configuration -> SDK_TOOLCHAIN_SUPPORTS_TIME_WIDE_64_BITS 。

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

ESP32 能否以动态库的方式加载库文件运行？
--------------------------------------------

  ESP32 不支持动态库的方式加载库文件，只支持靜态库。

------------------

ESP32 如何减小系统对 IRAM 内存的占用？
--------------------------------------------------------------------

  - 请将 mencuofnig -> Component config -> LWIP -> Enable LWIP IRAM optimization (键"N" 禁用) 配置选项禁用。
  - 请更改 menuconfig -> Compiler option -> Optimization Level -> Optimize for size (-Os) 中的配置选项。
  - 请将 menuconfig -> Component config -> wifi 中的配置选项中的 WiFi IRAM speed optimization (N) 和 WiFi RX IRAM speed optimization (N) 配置选项禁用。

----------------------

ESP32 芯片低电压复位阈值是多少？

- 欠压复位电压阈值范围在 2.43V ~ 2.80 V 之间，可在 menuconfig -> Component config -> ESP32-specific -> Brownout voltage level 中进行设置。

----------------

ESP32 light sleep 例程为何会自动唤醒？
----------------------------------------------------------------------------------------------------

  light sleep 例程下，默认使用了两种唤醒方式，如下：
  .. code-block:: c

    esp_sleep_enable_timer_wakeup(2000000);     // 2 秒自动唤醒
    esp_sleep_enable_gpio_wakeup();             // GPIO 唤醒

  GPIO 唤醒默认是 GPIO0 低有效唤醒，GPIO0 拉低则为唤醒状态，GPIO0 释放则自动进入 light sleep 模式。
  若需要长时间保存 light sleep 模式，可以将 2 秒自动唤醒屏蔽，仅开启 GPIO 唤醒。

---------------------

ESP32 deep_sleep例程测试，为何当 const int wakeup_time_sec = 3600时，程序 crash 出现死循环？
----------------------------------------------------------------------------------------------

  - 程序 crash 原因是 int 类型参数 `wakeup_time_sec` 在 wakeup_time_sec * 1000000 在运算时溢出。

  .. code-block:: c

    const uint64_t wakeup_time_sec = 3600;
    printf("Enabling timer wakeup, %lldn",wakeuo_time_sec);

------------------

ESP32 有几种系统复位方式？
--------------------------------

  - 有“芯片上电复位”、“RWDT 系统复位”、“欠压复位” 3 种系统复位方式。
  - 具体说明参见 `ESP32 技术规格书 <https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_cn.pdf>`__ 4.1.2 复位源章节。

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

ESP32 是否可以永久更改 MAC 地址？
-----------------------------------------

  - 芯片自带的 MAC 地址无法修改。efuse 中支持用户写入自己的 MAC 地址。
  - 在固件中调用 api 可以获取定制 MAC 地址，并且可以设置到系统中替代默认地址。
  - 配置参考：`mac-address <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/system.html#mac-address>`_。
  - 另外，Espressif 提供在芯片出厂之前，烧录用户提供的 MAC 地址服务。如有需要，可发送邮件至 sales@espressif.com

--------------

ESP8266 进行 ota 升级时如何校验 all.bin 为非法文件？
---------------------------------------------------------

  **问题背景：**

  - all.bin: 由 bootloader.bin，partition.bin 和 app.bin 合并生成。
  - ota.bin: 用于 ota 升级的目标 bin文件。
  
  使用 `simple_ota_example <https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/system/ota/simple_ota_example>`_ 进行 OTA 升级时，误从服务器上下载 all.bin,写入 ota 分区之后，设备会出现反复重启的现象。
  
  **原因分析：**

  代码中未对 all.bin 进行校验，导致将非法的 bin 文件写入 ota 分区。

  **解决方案：**

  通过打开 sha256 校验判断 all.bin 为非法 bin 文件，配置路径如下：Component config > App update > [*] Check APP binary data hash after downloading.

--------------

IDF 版本更新后，更新说明在哪里？
----------------------------------------------------------------------------------------

  可以在 Github release note 查看相关说明。链接为: https://github.com/espressif/esp-idf/releases

--------------

ESP8266 是否有详细的寄存器⼿册？
---------------------------------------

  请参考 《8266 TRM appendix》部分，链接：https://www.espressif.com/sites/default/files/documentation/esp8266-technical_reference_cn.pdf

---------------

ESP32 开启 Secure Boot 后 无法正常启动 ,出现如下报错，是什么原因？
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

  可能是因为开启 Secure Boot 后 Bootloader 会变大，烧录固件时 Bin 文件产生了覆盖。
  可以查询 Secure Boot 后 Bootloader 的大小，比如可以尝试把分区表的偏移量增大为 0xF000 。

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

-----------------

ESP32 同时开启 "Enable debug tracing of PM using GPIOs" 和 "Allow .bss segment placed in external memory" 后为何会导致系统不停重启？
---------------------------------------------------------------------------------------------------------------------------------------------

  - "Enable debug tracing of PM using GPIOs" 配置选项是在 GDB 调试时需要打开的，不可与 "Allow .bss segment placed in external memory" 配置选项同时使用。
  - 因为 “Enable debug tracing of PM using GPIOs" 默认使用的是 GPIO16 与 GPIO17 ，与 PSRAM 接口（默认也是 GPIO16 和 GPIO17） 冲突。


ESP32 IDF v3.3 版本 bootloader 运行 v3.1 版本 APP bin , 程序为何会触发 RTCWDT_RTC_RESET ？
--------------------------------------------------------------------------------------------------------

  - 在 v3.3 的 bootloader 中会开启 WDT 看门狗，且在应用程序(app) 运行时关闭 WDT 看门狗。
  - 但 v3.1 的 bootloader 没有开启 WDT 看门狗，所以应用程序(app) 没有 WDT 看门狗的机制，进而导致 v3.3 的 bootloader 引导 v3.1 的应用程序(app) 会触发 WDT 看门狗复位。
  - 可以通过在 menuconfig 中不使能 BOOTLOADER_WDT_ENABLE ，关闭 v3.3 版本 bootloader 中 WDT 看门狗开启。

-------------------

ESP32 芯片出厂是否有唯一的 chip_id ？
-------------------------------------------------

  - ESP32 芯片未未烧录唯一 chip_id，但设备默认烧录有全球唯一 MAC 地址，可以读取 MAC 地址替代 chip_id。

--------------

ESP8266 rst curse 如何查看？
------------------------------------

  - 请参考 `ESP8266 异常重启原因 <https://www.espressif.com/sites/default/files/documentation/esp8266_reset_causes_and_common_fatal_exception_causes_cn.pdf/>`_。

-----------------

ESP32 编译生成的 bin 文件大小如何优化？
--------------------------------------------------

  - 可配置 GCC 编译优化，操作步骤：idf.py menuconfig---->Compiler options---->Optimization level (Optimize for size(-Os))。
  - 可对代码进行优化，提高代码复用率，调整 log 等级，减少不必要的 log 打印。


-----------------

ESP32 是否有系统重新启动的 API ？
------------------------------------------------------------------------------

  - 系统重新启动的 API 可使用 esp_restart()，相关说明可 `参见 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/system/ota.html?highlight=esp_restart#id5>`__ 。

--------------

ESP32 异常 log `invalid header: 0xffffffff`
--------------------------------------------------------

  - ESP32 芯片打印该异常 log 通常有如下几种情况：
  - 芯片上下电时序不正确，芯片部分区域未完全复位。
  - Flash 中的固件出现异常，例如未烧录完整固件。
  - Flash 器件损坏，无法读取正确数据。
  - 芯片自身 cache 被关闭或者损坏，无法读取固件数据。

--------------

ESP8266 deep sleep 定时唤醒机制是什么？
----------------------------------------

  - 在 Deep-sleep 状态下，将 GPIO16 (XPD_DCDC) 连接至 EXT_RSTB ,计时到达睡眠时间后，GPIO16 输出低电平给 EXT_RSTB 管脚，芯片被复位唤醒。

ESP32 使用 heap_caps_get_free_size 获取 RAM 约 300 KB，为何与手册 520K 存在差异？
------------------------------------------------------------------------------------------------------

  - 是因为内存在系统启动时预分配给各个功能模块使用，系统启动后剩余内存约 300 KB。
  - 如果剩余内存不足，可以选用带 PSRAM 模组，将内存分配在 PSRAM 中。

--------------
  
ESP32 & ESP8266 如何通过局域网的 APP 进行 OTA 升级？
--------------------------------------------------------------

  - 局域网内 APP 设备可以配置开启 http 服务，将提供的固件下载链接通过其他方法（udp，coap，mqtt 等）发送至设备。
  - 设备通过传统 URL OTA 方法即可完成 OTA 更新，示例已在 SDK 中提供。

-----------------

ESP32 如何修改 LOG 输出至串口 UART1 ?
-------------------------------------------------------------------------------------------------

  - 更换 LOG 输出串口为 UART1 可通过配置 menuconfig -> Component Config ->Common ESP-related -> Channel for console output -> Custom UART -> UART peripheral to use for console output(0-1) -> UART1

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

  - 0x7f00 此报错是由于 内存不足 导致，建议使用 http 方式 OTA 。

-----------------

ESP32 配置 menuconfig --> Component config 中有 NVS 选项，为何配置项目为空？
-----------------------------------------------------------------------------------------

  - menuconfig --> Component config 中的 NVS 选项是配置 NVS 加密功能的，该功能的前提是开启 Flash 加密。
  - menuconfig --> security feaures --> enable flash encryption on boot 配置选项后，便可以看到 NVS 的配置选项。

--------------

ESP32 上电或 Deep-sleep 醒来后，会随机发⽣⼀次看⻔狗复位?
---------------------------------------------------------------------

  - 芯⽚上电的看⻔狗复位⽆法使⽤软件绕过，但复位后 ESP32 正常启动。
  - Deep-sleep 醒来后的看⻔狗复位在 ESP-IDF V1.0 及更⾼版本中⾃动绕过。
  - Deep-sleep 醒来后，CPU 可以⽴即执⾏ RTC fast memory 中的⼀段程序。RTC fast memory 中的这段程序通过清除 cache MMU 的⾮法访问标志从⽽绕过 Deep-sleep 醒来后的看⻔狗复位，具体为：

    - 将 DPORT_PRO_CACHE_CTRL1_REG 寄存器的 PRO_CACHE_MMU_IA_CLR ⽐特置 1。
    - 将该⽐特清零。

--------------

ESP32 CPU 使⽤ cache 访问外部 SRAM 时，如果这些操作需要 CPU 同时处理，可能会发⽣读写错误?
----------------------------------------------------------------------------------------------------

  - 这个问题⽆法使⽤软件⾃动绕过。
  - 对于版本 0 ESP32，CPU 使⽤ cache 访问外部 SRAM 时，只能够进⾏单向操作，即只能够单纯的进⾏写 SRAM 操作，或者单纯的进⾏读 SRAM 操作，不能交替操作。
  - 使⽤ MEMW 指令：在读操作之后，加上 ``__asm__("MEMW")`` 指令，然后在 CPU 流⽔线被清空前再发起写操作。

--------------

ESP32 CPU 访问外设时，如果连续不间断地通过 DPORT 写同⼀个地址，为何会出现数据丢失的现象？
----------------------------------------------------------------------------------------------------

  - 此问题在 ESP-IDF V1.0 及更⾼版本中⾃动绕过。
  - 当连续写同⼀个地址（即类似 FIFO 的地址）时，使⽤ AHB 地址⽽不是 DPORT 地址。（对于其他类型的寄存器写⼊，使⽤ DPORT 地址可能写性能更好。）

  +-----------------------+------------+-----------------+
  | 寄存器名称            | DPORT 地址 | AHB（安全）地址 |
  +=======================+============+=================+
  | UART_FIFO_REG         | 0x3FF40000 | 0x60000000      |
  +-----------------------+------------+-----------------+
  | UART1_FIFO_REG        | 0x3FF50000 | 0x60010000      |
  +-----------------------+------------+-----------------+
  | UART2_FIFO_REG        | 0x3FF6E000 | 0x6002E000      |
  +-----------------------+------------+-----------------+
  | I2S0_FIFO_RD_REG      | 0x3FF4F004 | 0x6000F004      |
  +-----------------------+------------+-----------------+
  | I2S1_FIFO_RD_REG      | 0x3FF6D004 | 0x6002D004      |
  +-----------------------+------------+-----------------+
  | GPIO_OUT_REG          | 0x3FF44004 | 0x60004004      |
  +-----------------------+------------+-----------------+
  | GPIO_OUT_W1TC_REG     | 0x3FF4400c | 0x6000400c      |
  +-----------------------+------------+-----------------+
  | GPIO_OUT1_REG         | 0x3FF44010 | 0x60004010      |
  +-----------------------+------------+-----------------+
  | GPIO_OUT1_W1TS_REG    | 0x3FF44014 | 0x60004014      |
  +-----------------------+------------+-----------------+
  | GPIO_OUT1_W1TC_REG    | 0x3FF44018 | 0x60004018      |
  +-----------------------+------------+-----------------+
  | GPIO_ENABLE_REG       | 0x3FF44020 | 0x60004020      |
  +-----------------------+------------+-----------------+
  | GPIO_ENABLE_W1TS_REG  | 0x3FF44024 | 0x60004024      |
  +-----------------------+------------+-----------------+
  | GPIO_ENABLE_W1TC_REG  | 0x3FF44028 | 0x60004028      |
  +-----------------------+------------+-----------------+
  | GPIO_ENABLE1_REG      | 0x3FF4402c | 0x6000402c      |
  +-----------------------+------------+-----------------+
  | GPIO_ENABLE1_W1TS_REG | 0x3FF44030 | 0x60004030      |
  +-----------------------+------------+-----------------+

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

  - ESP-IDF V2.1 及更⾼版本的 GPIO 驱动⾃动绕过此问题。
  - GPIO 和 RTC_GPIO 都使⽤ RTC_GPIO 寄存器。

--------------

ESP32 由于 flash 启动的速度慢于芯⽚读取 flash 的速度，芯⽚上电或 Deep-sleep 醒来后，会随机发⽣⼀次看⻔狗复位，如何解决？
---------------------------------------------------------------------------------------------------------------------------------------------

  - 更换更快的 flash，要求 flash 上电到可读的时间⼩于 800 μs。这种⽅法可以绕过芯⽚上电和 Deep-sleep 醒来时的看⻔狗复位。
  - Deep-sleep 醒来后的看⻔狗复位问题在 ESP-IDF V2.0 及更⾼版本中⾃动绕过（延迟时间可以根据需要配置）。具体⽅式是从 Deep-sleep 醒来后⾸先读取 RTC fast memory 中的指令，等待⼀段时间，然后再读取 flash。

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

ESP32 双核情况下，⼀个 CPU 的总线在读 A 地址空间，⽽另⼀个 CPU 的总线在读 B 地址空间，读 B 地址空间的 CPU可能会发⽣错误如何解决？
---------------------------------------------------------------------------------------------------------------------------------------------

  - ⼀个 CPU 在读 A 地址空间时，通过加锁和中断的⽅式来避免另⼀个 CPU 发起对 B 地址空间的读操作。
  - ⼀个 CPU 在读 A 地址空间之前，加⼀个此 CPU 读 B 地址空间（⾮ FIFO 地址空间，如 0x3FF40078）操作，并且要保证读 B 地址空间操作和读 A 地址空间操作是原⼦的。

--------------

ESP32 CPU 通过读取 INTERRUPT_REG 寄存器来复位 CAN 控制器的中断信号。如果在同⼀个 APB 时钟周期内 CAN 控制器刚好产⽣发送中断信号，则发送中断信号丢失，如何解决？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
  数据等待发送完成期间（即发送请求已发起），每⼀次读取 INTERRUPT_REG 后，⽤户都应检查 ``STATUS_TRANSMIT_BUFFER`` 位。如果 ``STATUS_TRANSMIT_BUFFER`` 置位⽽
  ``CAN_TRANSMIT_INT_ST`` 没有置位，则说明发送中断信号丢失。

--------------

ESP32 ECO V3 芯⽚，当程序同时满⾜下列条件时，会出现 live lock（活锁）现象，导致 CPU ⼀直处于访存状态，不能继续执⾏指令，请问如何解决？
-----------------------------------------------------------------------------------------------------------------------------------------------

  .. code::text

    1. 双核系统；
    2. 四条访问外存的指令/数据总线 (IBUS/DBUS) 中，有 3 条总线同时发起对同⼀个 cache 组的访问请求，并且三个
       cache 请求均缺失。

  发⽣ live lock 时，软件主动或被动识别并解锁 cache line 竞争，之后两个核按队列节拍分时完成各⾃的 cache 操作，解锁 live lock。详细过程如下：

    - 当两个核执⾏的指令均不在代码临界区中时出现 live lock，系统各类型中断会主动解除 cache line 竞争，解锁 live lock；
    - 当两个核执⾏的指令位于代码临界区中时出现 live lock，在临界区中，系统会屏蔽 3 级及以下中断。因此软件预先为两个核各设置⼀个⾼优先级（4 级或 5 级）中断，将它们绑定到同⼀个定时器，并选择合适的定时器超时⻔限。由于 live lock 产⽣的定时器超时中断会迫使两个核均进⼊⾼优先级中断处理程序，从⽽释放两个核的 IBUS 以达到解锁 live lock ⽬的。解锁过程通过 3 个阶段完成：

      a. 第 1 阶段两个核均进⾏等待以清空 CPU write buffer；
      b. 第 2 阶段⼀个核 (Core 0) 等待，另⼀个核 (Core 1) 执⾏；
      c. 第 3 阶段 Core 1 等待，Core 0 执⾏。

--------------

ESP32 CPU 访问 ``0x3FF0_0000 ~ 0x3FF1_EFFF`` 与 ``0x3FF4_0000 ~ 0x3FF7_FFFF`` 两段地址空间存在限制，如何解决？
-----------------------------------------------------------------------------------------------------------------------

  - 落在这两段地址空间的 CPU 访问均需要在对应的操作前加⼊ “MEMW” 指令。即在 C/C++ 中，软件访问这两段地址内的寄存器时需要加上 “volatile” 属性。

------------------

ESP32 如何关闭程序 LOG 输出？
--------------------------------------------------------------------

  - 关闭 bootloader 日志：menuconfig -> bootloader config --> bootloader log verbosity 选定为 No output 。
  - 关闭程序日志：menuconfig -> Component config --> log output --> Default log verbosity 选定为 No output 。
  - 关闭 UART0 输出日志：menuconfig -> Component Config ->Common ESP-related -> Channel for console output -> None 。
