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

SP32 是否支持 USB 功能？
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
