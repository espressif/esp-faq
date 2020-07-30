# 系统

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## 如果我的应⽤不需要看⻔狗，如何关闭看⻔狗？

- 当前 SDK 仅⽀持关闭软件看⻔狗， ⽀持同时喂软硬件看⻔狗。可以通过如下⽅式防⽌执⾏时间过⻓的⽤户程序导致看⻔狗复位：
  - 如果⼀个程序段运⾏时间在触发软件看⻔狗和触发硬件看⻔狗复位之间，则可通过 system_soft_wdt_stop() 的⽅式关闭软件看⻔狗，在程序段执⾏完毕后⽤ system_soft_wdt_restart() 重新打开软件看⻔狗。
  - 可以通过在程序段中添加 system_soft_wdt_feed() 来进⾏喂软硬件狗操作，防⽌软硬件看⻔狗复位。
- 硬件看⻔狗中断时间为 0.8*2048ms，即 1638.4s，中断后处理时间为 0.8*8192ms，即 6553.6ms。其中中断处理后时间为硬件看⻔狗中断发⽣后，需要进⾏喂狗操作的时间，如果超过该时间，即会触发硬件看⻔狗复位。因此，在仅有硬件看⻔狗的情况下，⼀个程序段如果运⾏时间超过 6553.6ms，即有可能触发硬件看⻔狗复位，若超过 8192ms 则⼀定会触发复位。
- 软件看⻔狗建⽴在 MAC timer 以及系统调度之上，中断时间为 1600ms，中断后处理时间 1600ms。因此，在有软件+硬件看⻔狗的情况下，⼀个程序段如果运⾏时间超过 1600ms，即有可能会触发软件看⻔狗复位，若超过 3200ms 则⼀定会触发复位。

---

## RTOS SDK 和 Non-OS SDK 有何区别？

- 主要差异点如下：
- **Non-OS SDK**
  - Non-OS SDK 主要使⽤定时器和回调函数的⽅式实现各个功能事件的嵌套，达到特定条件下触发特定功能函数的⽬的。Non-OS SDK 使⽤ espconn 接⼝实现⽹络操作， ⽤户需要按照 espconn 接⼝的使⽤规则进⾏软件开发。
- **RTOS SDK** 
  - RTOS 版本 SDK 使⽤ freeRTOS 系统，引⼊ OS 多任务处理的机制，⽤户可以使⽤ freeRTOS 的标准接⼝实现资源管理、循环操作、任务内延时、任务间信息传递和同步等⾯向任务流程的设计⽅式。具体接⼝使⽤⽅法参考 freeRTOS 官⽅⽹站的使⽤说明或者 USING THE FREERTOS REAL TIME KERNEL - A Practical Guide 这本书中的介绍。
  - RTOS 版本 SDK 的⽹络操作接⼝是标准 lwIP API，同时提供了 BSD Socket API 接⼝的封装实现，⽤户可以直接按照 socket API 的使⽤⽅式来开发软件应⽤，也可以直接编译运⾏其他平台的标准 Socket 应⽤，有效降低平台切换的学习成本。
  - RTOS 版本 SDK 引⼊了 cJSON 库，使⽤该库函数可以更加⽅便的实现对 JSON 数据包的解析。
  - RTOS 版本兼容 Non-OS SDK 中的 Wi-Fi 接⼝、SmartConfig 接⼝、Sniffer 相关接⼝、系统接⼝、定时器接⼝、FOTA 接⼝和外围驱动接⼝，不⽀持 AT 实现。

---

## ESP8266 启动时 LOG 输出 ets_main.c 有哪些原因？

- ESP8266 启动时打印 `ets_main.c`，表示没有可运⾏的程序区，⽆法运⾏；遇到这种问题时，请检查烧录时的 bin ⽂件和烧录地址是否正确。

---

## ESP8266 编译 Non-OS SDK 时 IRAM_ATTR 错误是什么原因？

- 如果需要在 IRAM 中执⾏功能，就不需要加 `ICACHE_FLASH_ATTR` 的宏，那么该功能就是放在 IRAM 中执⾏。

---

## ESP8266 main 函数在哪里？

- ESP8266 用户 SDK 部分没有 main 函数。
- main 函数处于 一级 bootloader 并且固化在芯片 ROM 中， 用于引导二级 bootloader。
- 二级 bootloader 入口函数为 ets_main，启动后会加载用户应用中的 user_init，引导至用户程序。

---

## ESP8266 partition-tables 特殊注意点？

- ESP8266 partition-tables 相对 ESP32 对于 ota 分区有一定的特殊要求，这是由于 ESP8266 cache 特性导致。
- 详情参考[ESP8266 partition-tables 偏移与空间](https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/api-guides/partition-tables.html#offset-size)

---

## 应⽤层与底层的 bin ⽂件可以分开编译吗?

- 不⽀持分开编译。

---  

## ESP32 模组 flash 使用 80Mhz 有什么注意事项吗 ？

- 乐鑫模组发售前已经过稳定性测试，测试可以支持 80 MHz 频率。
- 根据稳定性测试数据，80 MHz 的频率不会影响使用寿命和稳定性。

---

## ESP32 系统软件复位 API？

&emsp;&emsp;软件复位 API:`esp_restart()`。

---

## 使用 esp-idf 按汇编操作寄存器，是否涉及到调用不可编辑的库文件？

- 如果单纯使用读写寄存器指令或者汇编指令，不存在调用库文件的问题。
- 如果调用 esp-idf 预制的函数，则可能会遇到调用 lib 函数的情况。
- 不推荐在 ESP32 中使用汇编操作，如果部分场景想要提高速度，可以读写寄存器来完成部分操作。

---

## 使用 ESP-IDF 测试程序，如何设置可在单核模组上下载程序？

程序编译时，使用 make menuconfig 指令进入配置界面，进行如下配置，可在单核模组上下载程序；在配置界面中，按键 Y 为启动，N 为关闭。

  Component config  -->  FreeRTOS  -->  Run FreeRTOS only on first core（启动此选项）
  
---

## 使用 esp-idf ,如何使能 ESP32 的双核模式？

esp-idf 一般情况下默认配置的是双核模式，您可以在 menuconfig 中进行单双核的修改。
  - menuconfig -> Component config -> FreeRTOS -> Run FreeRTOS only on first core 使能即为单核，未使能默认双核。

---

## 使用 ESP32-D0WD 芯片是否可以存储用户程序？

- 不可以，用户程序必须使用外挂 Flash 进行存储，片上 ROM 不能存储用户程序。
- ROM 内存放的程序为芯片一级 bootloader ，为了保护出厂程序不被破坏，该区域为只读存储。

---

## ESP32 进入低功耗模式时， PSRAM 中的数据会丢失吗？

- Modem-sleep/Light-sleep 模式时，PSRAM 中的数据不会丢失。
- Deep-sleep 模式时，CPU 和大部分外设都会掉电，PSRAM 的数据会丢失。

---

## 请问 ESP32 CPU 系统时间是否由系统滴答时钟生成？精度如何？

CPU 系统时间是由 esp_timer 内部的 64 位硬件定时器 CONFIG_ESP_TIMER_IMPL 产生的，是微秒级的时间分辨率。参见[说明](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/system/esp_timer.html?highlight=esp_timer_get_time#high-resolution-timer)。

---

##  ESP32 的 flash 和 psram 的时钟频率如何修改？

在 menuconfig 中修改。
  - flash 时钟频率：menuconfig -> Serial flasher config -> Flash SPI speed。
  - PSRAM 时钟频率：Component config -> ESP32-specific -> SPI RAM config -> Set RAM clock speed
