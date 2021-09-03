外设
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

SDIO 最⾼速度能⽀持到多少？
---------------------------

  SDIO 时钟能到 50 MHz, 理论最⾼速度是 200 Mbps。

--------------

使⽤ ESP32 做触摸相关应⽤时，哪⾥有相关资料可参考？
---------------------------------------------------

  请参考推荐的 `软硬件设计 <https://github.com/espressif/esp-iot-solution/tree/master/examples/touch_pad_evb>`_。

--------------

ESP-WROOM-02D 模块是否可以外接 SPI Flash ？
-------------------------------------------

  ESP-WROOM-02D 有空闲 SPI 外设，可外接 SPI Flash，用以存储数据。

--------------

ESP-WROOM-S2 作为从机，STM32 作为 MCU ，可以使⽤ SPI 接⼝下载吗？
-----------------------------------------------------------------

  不可以，默认下载功能仅支持串口 UART0，固件启动后可应用中使能其他外设，在应用中⾃⾏设计⽀持 OTA 功能。

--------------

ESP8266 的 SDIO 是否⽀持 SD 卡？
--------------------------------

  ESP8266 是 SDIO Slave，不⽀持 SD 卡。

--------------

ESP8266 是否支持 I2C slave 模式？
---------------------------------

  不支持，如果要使用此功能，推荐使用 ESP32-S2 或者 ESP32 芯片。ESP32 参考示例：`i2C\_self\_test <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/i2c/i2c_self_test>`_。

--------------

ESP32 管脚配置需要注意什么？
----------------------------

  ESP32 系列模组分为 ESP32-WROOM 系列和 ESP32-Wrover 系列，GPIO 使用配置注意事项如下。

  WROOM-32/32D/32U 系列共有 26 个 pin 脚可供客户使用, 注意事项如下：

  - GPIO6～GPIO11 被内置 flash 占用，不可用做它用； 
  - GPIO34，35，36 和 39 为 input only pin 脚，不具备 output 能力 
  - ESP32 内置 GPIO 矩阵，部分外设接口可以配置到任意空闲 pin 脚上，即硬件设计时，不需要严格将某些功能固定在某些 pin 脚上。

  详细信息可以参考 `ESP32 datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf>`_ 中表格 9 的内容。

  WROVER／WROVER-I／WROVER-B／WROVER-IB 共有 24 个 pin 脚可供客户使用，注意事项如下： 

  - GPIO6～GPIO11 被内置 flash 占用，不可用做它用； 
  - GPIO34，35，36 和 39 为 input only pin 脚，不具备 output 能力；
  - WROVER 系列模组中，GPIO12 由于在模组内部被上拉，不建议用做触摸传感功能；
  - ESP32 内置 GPIO 矩阵，部分外设接口可以配置到任意空闲 pin 脚上，即硬件设计时，不需要严格将某些功能固定在某些 pin 脚上。

  详细信息可以参考 `ESP32 datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf>`_ 中表格 9 的内容。 

  ESP32 有 3 组 UART，但下载只可使用 UART0，且 pin 脚固定

--------------

ESP32 是否支持 A2DP 发送音频？
------------------------------

  ESP32 支持 A2DP 发送音频，可参考例程 `esp-idf/examples/bluetooth/bluedroid/classic\_bt/a2dp\_source <https://github.com/espressif/esp-idf/tree/d85d3d969ff4b42e2616fd40973d637ff337fae6/examples/bluetooth/bluedroid/classic_bt/a2dp_source#esp-idf-a2dp-source-demo>`_。

--------------

ESP8266 I2C 是软件模拟的吗？
----------------------------

  ESP8266 I2C 是使用 gpio 软件模拟。

--------------

使用 ESP8266-NONOS-V3.0 版本的 SDK，如下报错是什么原因？
---------------------------------------------------------------

.. code-block:: text

  E:M 536    E:M 1528

  - 导致 E:M 开头的 LOG  是内存不足的原因。

--------------

ESP8266 PWM 频率范围是多少呢？
------------------------------

  ESP8266 PWM 是软件模拟的，受定时器限制 CLK 最大为 1M。推荐频率为 1K，也可以通过降低占空比分辨率的方式提高频率。

--------------

ESP32 GPIO 管脚输出 PWM 存在限制吗？
--------------------------------------------------------------------

  ESP32 PWM 可通过 IO Matrix 切换至任意 GPIO 输出。但是由于 GPIO34 ~ GPIO39 仅为输入模式，故不支持做 PWM 输出。

--------------

ESP32S2 Touch Sensor 的防水功能是在有水时屏蔽 Touch 还是有水时仍然能识别 Touch 事件？
---------------------------------------------------------------------------------------------------------------------------------------

-  当水对触摸传感器的影响较小时(水珠)，传感器会主动适应；当水对触摸传感器的影响较大时(水流)，传感器可通过软件配置来选择锁定某些传感器通道的状态来避免水的影响

--------------

ESP32S2 Touch Sensor 的防水流功能在屏蔽有水流的 Touchpad 时，是否能够保持未沾水的 Pad 仍能使用？
-----------------------------------------------------------------------------------------------------------------------------------------

-  可以，可通过软件选择具体屏蔽的通道

--------------

是否有推荐的可以用于 Touch Sensor 测试、稳定触发 Touch Sensor 并且参数与人手触摸时参数接近的材料？
----------------------------------------------------------------------------------------------------------------------------------------------------------

-  对一致性要求较高的实验可使用手机电容笔来替代人手进行测试

--------------

Touch Sensor 的 Pin 能否重映射？
----------------------------------------------------------------

-  不能

--------------

在覆盖亚克力板后，Touch Sensor 检测阈值是否需要重新设置？
-----------------------------------------------------------------------------------------------

-  需要重新设置一个阈值

--------------

Touch Sensor 能否检测是否有亚克力板覆盖，以便在添加或移除亚克力板时，自动切换预设定的检测阈值？
------------------------------------------------------------------------------------------------------------------------------

-  暂时不能自动适应覆盖层物理参数变化所带来的影响

--------------

ESP32 SD 卡支持的最大容量是多少？
-------------------------------------------------

  - SD3.01 规范中 SDXC 的卡最大支持 2TB（2048GB）容量。
  - ESP32 的 SDMMC host 符合 SD3.01 协议，通过该外设可以访问最多 2TB 的区域；使用 SDSPI 驱动通过 SPI 总线访问卡时，硬件也支持访问 2TB 的区域。
  - 在软件层面上，卡能使用的空间还受文件系统的影响。

--------------

ESP32 是否支持 USB 功能？
--------------------------------------

  - ESP32 不支持 USB 功能。
  - ESP32-S2 支持 USB1.1 。

--------------

ESP8266 使⽤ hw timer 中断有哪些注意事项？
------------------------------------------

  - 可以参考相关 API 文档  `ESP8266 技术参考手册 <https://www.espressif.com/sites/default/files/documentation/esp8266-technical_reference_cn.pdf>`__。
  - 如果使用 NONOS SDK 可以阅读  `ESP8266 Non-OS SDK API 参考 <https://www.espressif.com/sites/default/files/documentation/2c-esp8266_non_os_sdk_api_reference_cn.pdf>`__。
  - 通常情况下，硬件中断需要尽快执行结束，并且将回调函数放入 IRAM 中，避免 Cache 影响。
    - RTOS SDK 需要函数去添加 IRAM_ATTR
    - NonOS SDK 不能在函数前添加 ICACHE_FLASH_ATTR

--------------

ESP32 脉冲宽度调制（PWM）信号是否可以分配任意一个 I/O 上？
------------------------------------------------------------

  - 除了只有输⼊功能的 I/O（例如：GPIO34-GPIO39） 之外，理论上 PWM 可以输出到任何管脚。
  - 实际使用中仍会受到模组与芯片限制，模组未引出管脚或 Flash 占用等情况影响。

--------------

ESP32 是否有 I2S 驱动 LCD 的参考代码？
----------------------------------------------

  - I2S LCD driver：`esp-iot-solution i2s_devices <https://github.com/espressif/esp-iot-solution/tree/master/components/i2s_devices>`__。

--------------

ESP8266 RTOS_2.1 以及之前版本 SDK，如何将 LOG 配置到 UART1 ？
---------------------------------------------------------------------

  - 在配置 UART1 初始化后，可以通过 API 切换 LOG 输出到 UART1。

  .. code-block:: c

    UART_SetPrintPort(UART1);

--------------

ESP32 IDF 中如何使能 UART 流控？
----------------------------------------------

  - `硬件流控使能 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/peripherals/uart.html?highlight=uart%20flow%20control#multiple-steps>`__。
  - `软件流控使能 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/peripherals/uart.html?highlight=uart%20flow%20control#software-flow-control>`__。

--------------

ESP8266 NonOS SDK PWM 的变化缓慢，又哪些原因？
------------------------------------------------

  - 如果使用 SDK example/IOT_demo 中的渐变 API，如 light_set_aim 或 light_set_aim_r 这些 API，需要渐变的过程。
  - 若需要 PWM Duty 设置后⽴即⽣效，则可以调⽤接⼝ pwm_set_duty，需要注意调⽤ pwm_set_duty 后要调⽤ pwm_start 此次设置才能⽣效。

--------------

ESP8266 部分 GPIO 出现高电平 ？
------------------------------------------------

  - 根据硬件设计，部分 GPIO 存在默认上下拉状态，所以在系统初始化时，该管脚的电平状态不受程序控制，所以会出现程序在引导过程中部分 GPIO 电平不正确。
  - 如果需要使用这些 GPIO ，硬件上建议外接器件与默认上下拉电平一致，软件可以在 bootloader 过程中调整电平状态，软件方法也会存在短暂电平异常。

--------------

ESP8266 ADC 的精度如何？
------------------------------------------------

  - ESP8266 ADC 为 10 bit, 理论精度为 2^10=1024。
  - ESP8266 连接路由器后，单 STA 模式会进⼊ modem-sleep，导致芯⽚内部参考值变化，因此 ADC 测量得数据变化。
  - 如果想要测量精确，可以再关闭 wifi 后，使用 `system_adc_fast_read` 函数读取。

--------------

ESP8266 如何获取 ADC 寄存器 bitmap 信息？
------------------------------------------------

  - 由于 ESP8266 ADC 是和内部 RF 电路⾼度集成的，所以 bitmap 和寄存器信息没有公开，如有特殊需求请联系 sales@espressif.com。

--------------

ESP32 ADC 有⼏个通道？采样率和有效位数是多少？
------------------------------------------------

  - ESP32 的 ADC 共有 18 个通道。
  - 在停⽌ Wi-Fi 的情况下，采样率能达到每秒 100000 次。
  - 在 Wi-Fi 正常⼯作的情况下，能达到每秒 1000 次。
  - ADC 内部有效位数为 12 位。

--------------

ESP32 是否可以关闭线程调度使用一个单独的 CPU 以实现实时 GPIO？
-----------------------------------------------------------------

  - 目前 SDK 没有相关的配置选择供 CPU1 单独运行，两个核心只支持 SMP，不支持 AMP。
  - 解决输出波形被打断的问题有以下解决方案:
    - 使用硬件的信号输出，选择相关数字协议实现 SPI， I2C, I2S 等, 特殊用法 SPI 取信号输出线产生波形。
    - 硬件 RMT 是否可以产生想要的波形， 并达到足够的长度 。
    - 硬件中断中产生相应波形，需要将所有回调放入 IRAM 中。
    - 可以利用芯片中的协处理器，它可以当作无操作系统的单片机，但目前只支持汇编语言。

--------------

ESP32 Touch 应用有哪些参考资料？
-------------------------------------------

  - ESP32 touch 应用可以参考 `Touch 软硬件设计 <https://github.com/espressif/esp-iot-solution/tree/master/examples/touch_pad_evb>`__ 。


--------------

ESP32 SD 卡是否可以与 Flash & Psram 共同使用？
-------------------------------------------------

  - 可以共同使用。 
  - ESP32 Flash & PSRAM 与 SD 卡使用的不是同一组 SDIO。

--------------

ESP32 使用 UART0 作为通信串口，有哪些？
-------------------------------------------------

  - 通常情况下不建议将 UART0 作为普通的通信串口，因为 UART0 为设备默认 LOG 输出串口。
  - 若 ESP32 的 UART 不够用，或者硬件设计已经不方便更改的情况下，如果您要使用 UART0 作为普通的通信串口，请参考以下建议：
    
    软件方面：防止打印影响串口通信，默认程序中 UART0 主要有三处打印设置：
    - 第一处是上电 ROM 打印，上电时可将 MTDO pin 设为低电平屏蔽上电 ROM 打印。
    - 第二处是 bootloader log 信息输出，您可以将 menuconfig -> Bootloader config -> Bootloader log verbosity 设置为 No output 来屏蔽 bootloader log 输出。
    - 第三处是 app log 信息输出，您可以将 menuconfig -> Component config -> Log output -> Default log verbosity 设置为 No output 来屏蔽 log 输出。
    
    硬件方面：
    - 在下载程序的时候，注意防止 UART0 上有其它设备，如果有其它设备可能会影响程序的下载。建议在 ESP32 和其它设备之间预留一个 0 Ω 电阻，如果下载有问题可以断开这个 0 Ω 电阻。

-----------

悬空 ADC 引脚，打印出 VDD3P3 的值为 65535，那么 VDD3P3 的电压就是 65535/1024 ≈ 63V 这个电压值不符，是什么原因？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

- ADC 功能管脚不可以悬空，悬空 ADC 管脚测得的值不是正确的值。
