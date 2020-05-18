# 系统

## Win 10 系统识别设备

- `Q:`
  - Win 10 系统下识别不到设备？

- `A:`
  - 请确认设备名称的标准格式是否正确，应为 /dev/ttyS*。

## ESP8266 看⻔狗

- `Q:`
  - ESP8266 的看⻔狗是什么作⽤？

- `A:`
  - 为了提供系统稳定性，以应对多冲突的操作环境，ESP8266 集成了 2 级看⻔狗机制，包括软件看⻔狗和硬件看⻔狗。默认 2 个看⻔狗都是打开的。

## ESP8266 看⻔狗时间和现象

- `Q:`
  - ESP8266 看⻔狗的超时间隔是多久？出发超时事件会有什么现象？

- `A:`
  - 硬件看⻔狗中断时间为 0.8*2048ms，即 1638.4s，中断后处理时间为 0.8*8192ms，即 6553.6ms。其中中断处理后时间为硬件看⻔狗中断发⽣后，需要进⾏喂狗操作的时间，如果超过该时间，即会触发硬件看⻔狗复位。因此，在仅有硬件看⻔狗的情况下，⼀个程序段如果运⾏时间超过 6553.6ms，即有可能触发硬件看⻔狗复位，若超过 8192ms 则⼀定会触发复位。
  - 软件看⻔狗建⽴在 MAC timer 以及系统调度之上，中断时间为 1600ms，中断后处理时间 1600ms。因此，在有软件+硬件看⻔狗的情况下，⼀个程序段如果运⾏时间超过 1600ms，即有可能会触发软件看⻔狗复位，若超过 3200ms 则⼀定会触发复位。

## 关闭看门狗

- `Q:`
  - 如果我的应⽤不需要看⻔狗，如何关闭看⻔狗？

- `A:`
  - 当前 SDK 仅⽀持关闭软件看⻔狗， ⽀持同时喂软硬件看⻔狗。可以通过如下⽅式防⽌执⾏时间过⻓的⽤户程序导致看⻔狗复位：
    - 如果⼀个程序段运⾏时间在触发软件看⻔狗和触发硬件看⻔狗复位之间，则可通过 system_soft_wdt_stop() 的⽅式关闭软件看⻔狗，在程序段执⾏完毕后⽤ system_soft_wdt_restart() 重新打开软件看⻔狗。
    - 可以通过在程序段中添加 system_soft_wdt_feed() 来进⾏喂软硬件狗操作，防⽌软硬件看⻔狗复位。

## 看门狗延迟

- `Q:`
  - 如果我要在程序⾥引⼊ 10 秒的延迟，怎么做最好？

- `A:`
  - 看⻔狗不⽀持⽆限循环。如果客户使⽤循环做延迟或者进⼊⼀个事件太⻓时间，就会触发硬件看⻔狗重启。推荐使⽤ callback 和 timer 的 API 做延迟。
  - 如果要轮询事件，推荐使⽤中断和 timer 的 API 来做。⼤多数事件都是关联到 callback 上的，所以⼤多数情况下，轮询都是可以避免的。

## ESP8266 timer 数量

- `Q:`
  - ESP8266 总共有⼏个 timer？

- `A:`
  - ESP8266 有 2 个 timer。 ⼀个硬件的 timer， ⼀个软件的 timer。
  - API os_timer 是 DSR 处理器，不能产⽣中断，但是可以产⽣任务。任务会按照普通等级排队。
  - 硬件 timer 能产⽣中断和任务，中断能触发任务，任务按照普通等级排队。

## ESP8266 使⽤ timer 中断

- `Q:`
  - ESP8266 使⽤ timer 中断是否有特定条件？

- `A:`
  - 请参考 SDK 的 API 参考：[《ESP8266 Non-OS SDK API 参考》](https://www.espressif.com/zh-hans/support/documents/technical-documents)和[《ESP8266 RTOS SDK API 参考》](https://www.espressif.com/zh-hans/support/documents/technical-documents)。⼀般情况，使⽤ Non-OS SDK 时，硬件中断回调⾥⾯不要有声明为 ICACHE_FLASH_ATTR 的功能。同时中断回调⾥不要占⽤ CPU 太⻓时间。

## ESP8266_Non-OS_SDK 中 `ICACHE_FLASH_ATTR` 宏

- `Q:`
  - 为什么 ESP8266_Non-OS_SDK 中有的函数前⾯添加了 `ICACHE_FLASH_ATTR` 宏？

- `A:`
  - **对于 ESP8266_Non-OS_SDK：**
  添加了了 `ICACHE_FLASH_ATTR` 宏的函数，将存放在 IROM 中，CPU 仅在调⽤到它们的时候，将它们读到 cache 中运⾏；没有添加 `ICACHE_FLASH_ATTR` 宏的函数，将在⼀开始上电运⾏时，就加载到 IRAM 中运⾏；由于空间有限，我们⽆法将所有代码都⼀次性加载到 IRAM 中运⾏，因此在⼤部分函数前添加 `ICACHE_FLASH_ATTR` 宏，放在 IROM 中。
  请注意，不要在中断处理理函数中调⽤带有 `ICACHE_FLASH_ATTR` 宏的函数，否则可能与 Flash 读写操作冲突。
  - **对于 ESP8266_RTOS_SDK：**
  函数默认存放在 IROM 中， ⽆需再添加“ICACHE_FLASH_ATTR”宏。中断处理函数也可以定义在 IROM 中。如果开发者需要将⼀些频繁调⽤的函数定义在 IRAM 中，在函数前添加 `IRAM_ATTR` 宏即可。

## Non-OS SDK IRAM_ATTR 错误

- `Q:`
  - 为什么编译 Non-OS SDK 时会发⽣ IRAM_ATTR 错误？

- `A:`
  - 如果需要在 IRAM 中执⾏功能，就不需要加 `ICACHE_FLASH_ATTR` 的宏，那么该功能就是放在 IRAM 中执⾏。

## `irom0_0_seg` 错误

- `Q:`
  - 为什么编译的时候会发⽣ `irom0_0_seg` 错误？

- `A:`
  - 它表示代码量量太⼤，IROM 区域存放不下了。
    我们可以在 SDK_v0.9.5 (及之后) 的软件版本中，尝试如下步骤，解决这个问题:
    1. 使⽤默认设置，编译⽣成 eagle.flash.bin 和 eagle.irom0text.bin。
        - 如果 size of eagle.flash.bin + size of eagle.irom0text.bin >= 236KBytes：很抱歉，您的代码量量太⼤了了，只能换⼤些的 Flash。
        - 如果 size of eagle.flash.bin + size of eagle.irom0text.bin < 236KBytes：请继续步骤 2。
    2. 在路径 SDK/ld 下修改⽂件“eagle.app.v6.new.512.app1.ld”。
        irom0_0_seg : org = 0x40201010, len = 0x2B000
        根据步骤 1 中编译的 `eagle.irom0text.bin` ⼤⼩，改写上述 len 的值。
        示例：如果 `eagle.irom0text.bin` ⼤⼩为 179 KB，则可修改配置如下：
        irom0_0_seg : org = 0x40201010, len = 0x2D000
    3. 重新编译 user1.bin 选择 boot_v1.2+。
        补充说明：
        代码中，
        - 函数前未加 ICACHE_FLASH_ATTR 的，编译到 IRAM 中，最⼤ 32 KB；
        - 函数前加了了 ICACHE_FLASH_ATTR 的，编译到 IROM 中；
        因为 RAM 的空间有限，因此做了了这两个部分的区分:
        - IRAM 中的代码，会在上电初始就完整加载到 RAM 中；
        - IROM 中的代码是⽤到的时候才从 Flash 加载到 cache 中执⾏。

## ESP8266 main

- `Q:`
  - ESP8266 有 main 吗？

- `A:`
  - ESP8266 没有 main，程序⼊⼝为 user_init。

## 操作指针

- `Q:`
  - 操作指针有什么需要注意的？

- `A:`
  - 内存必须 4 字节对⻬读取，指针做转换时请确保为 4 字节对⻬，否则转换失败，不能正常使⽤。例如，请勿直接指针转换 float temp = *((float*)data)； ⽽是使⽤ os_memcpy (memcpy) 实现。

## NONOS SDK IRAM_ATTR 错误

- `Q:`
  - 为什么编译 NONOS SDK 时会发⽣ IRAM_ATTR 错误？

- `A:`
  - 如果需要在 IRAM 中执⾏功能，就不需要加 `ICACHE_FLASH_ATTR` 的宏，那么该功能就是放在 IRAM 中执⾏。

## irom0_0_seg 错误

- `Q:`
  - 为什么编译的时候会发⽣ `irom0_0_seg` 错误？

- `A:`
  - 它表示代码量量太⼤，IROM 区域存放不下了。
    我们可以在 SDK_v0.9.5 (及之后) 的软件版本中，尝试如下步骤，解决这个问题: 
    1. 使⽤默认设置，编译⽣成 eagle.flash.bin 和 eagle.irom0text.bin。
        - 如果 size of eagle.flash.bin + size of eagle.irom0text.bin >= 236KBytes：很抱歉，您的代码量量太⼤了了，只能换⼤些的 Flash。
        - 如果 size of eagle.flash.bin + size of eagle.irom0text.bin < 236KBytes：请继续步骤 2。
    2. 在路径 SDK/ld 下修改⽂件“eagle.app.v6.new.512.app1.ld”。
        irom0_0_seg : org = 0x40201010, len = 0x2B000 
        根据步骤 1 中编译的 `eagle.irom0text.bin` ⼤⼩，改写上述 len 的值。
        示例：如果 `eagle.irom0text.bin` ⼤⼩为 179 KB，则可修改配置如下：
        irom0_0_seg : org = 0x40201010, len = 0x2D000 
    3. 重新编译 user1.bin 选择 boot_v1.2+。
        补充说明：
        代码中，
        - 函数前未加 ICACHE_FLASH_ATTR 的，编译到 IRAM 中，最⼤ 32 KB；
        - 函数前加了了 ICACHE_FLASH_ATTR 的，编译到 IROM 中；
        因为 RAM 的空间有限，因此做了了这两个部分的区分:
        - IRAM 中的代码，会在上电初始就完整加载到 RAM 中；
        - IROM 中的代码是⽤到的时候才从 Flash 加载到 cache 中执⾏。

## ESP8266 MAIN

- `Q:`
  - ESP8266 有 main 吗？

- `A:`
  - ESP8266 没有 main，程序⼊⼝为 user_init。

## RTOS SDK 和 Non-OS SDK 区别

- `Q:`
  - RTOS SDK 和 Non-OS SDK 有何区别？

- `A:`
  - 主要差异点如下：
  **Non-OS SDK**
  Non-OS SDK 主要使⽤定时器和回调函数的⽅式实现各个功能事件的嵌套，达到特定条件下触发特定功能函数的⽬的。Non-OS SDK 使⽤ espconn 接⼝实现⽹络操作， ⽤户需要按照 espconn 接⼝的使⽤规则进⾏软件开发。
  **RTOS SDK** 
    1. RTOS 版本 SDK 使⽤ freeRTOS 系统，引⼊ OS 多任务处理的机制，⽤户可以使⽤ freeRTOS 的标准接⼝实现资源管理、循环操作、任务内延时、任务间信息传递和同步等⾯向任务流程的设计⽅式。具体接⼝使⽤⽅法参考 freeRTOS 官⽅⽹站的使⽤说明或者 USING THE FREERTOS REAL TIME KERNEL - A Practical Guide 这本书中的介绍。
    2. RTOS 版本 SDK 的⽹络操作接⼝是标准 lwIP API，同时提供了 BSD Socket API 接⼝的封装实现，⽤户可以直接按照 socket API 的使⽤⽅式来开发软件应⽤，也可以直接编译运⾏其他平台的标准 Socket 应⽤，有效降低平台切换的学习成本。
    3. RTOS 版本 SDK 引⼊了 cJSON 库，使⽤该库函数可以更加⽅便的实现对 JSON 数据包的解析。
    4. RTOS 版本兼容 Non-OS SDK 中的 Wi-Fi 接⼝、SmartConfig 接⼝、Sniffer 相关接⼝、系统接⼝、定时器接⼝、FOTA 接⼝和外围驱动接⼝，不⽀持 AT 实现。

## user_init 调用

- `Q:`
  - 哪些接⼝需要在 user_init 中调⽤，否则容易出现问题，或者不⽣效？

- `A:`
    1. wifi_set_ip_info、wifi_set_macaddr 仅在 user_init 中调⽤⽣效，其他地⽅调⽤不⽣效。
    2. system_timer_reinit 建议在 user_init 中调⽤，否则调⽤后，需要重新 arm 所有 timer。
    3. wifi_station_set_config 如果在 user_init 中调⽤，底层会⾃动连接对应路由，不需要再调⽤ wifi_station_connect 来进⾏连接。否则，需要调⽤ wifi_station_connect进⾏连接。
    4. wifi_station_set_auto_connect 设置上电启动时是否⾃动连接已记录的路由；例如，关闭⾃动连接功能，如果在 user_init 中调⽤，则当前这次上电就不会⾃动连接路由，如果在其他位置调⽤，则下次上电启动不会⾃动连接路由。

## ESP8266 触发看⻔狗复位

- `Q:`
  - 为什么 ESP8266 进⼊启动模式（2，7）并触发看⻔狗复位？

- `A:`
  - 请确保 ESP8266 启动时，strapping 管脚处于所需的电平。如果外部连接的外设使 strapping 管脚进⼊到错误的电平，ESP8266 可能进⼊错误的操作模式。在⽆有效程序的情况下，看⻔狗计时器将复位芯⽚。
  因此在设计实践中，建议仅将 strapping 管脚⽤于连接⾼阻态外部器件的输⼊，这样便不会在上电时强制 strapping 管脚为⾼/低电平。

## ESP8266 `ets_main.c` 打印

- `Q:`
  - 为什么 ESP8266 启动时打印 `ets_main.c`，并且⽆法正常运⾏？

- `A:`
  - ESP8266 启动时打印 `ets_main.c`，表示没有可运⾏的程序区，⽆法运⾏；遇到这种问题时，请检查烧录时的 bin ⽂件和烧录地址是否正确。