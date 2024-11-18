GPIO & RTC GPIO
===============

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

ESP32 管脚配置需要注意什么？
--------------------------------------

  ESP32 系列模组分为 ESP32-WROOM 系列和 ESP32-WROVER 系列，GPIO 使用配置注意事项如下。

  WROOM-32/32D/32U/32E/32UE 系列共有 26 个管脚可供客户使用，注意事项如下：

  - WROOM-32/32D/32U 系列的 GPIO6-GPIO11 被内置 flash 占用，不可用做它用；
  - WROOM-32E/32UE 系列的 GPIO6 ～ GPIO11 被内置 flash 占用，且不再拉出至模组管脚；
  - GPIO34、35、36 和 39 为输入管脚，不具备输出能力；
  - ESP32 内置 GPIO 矩阵，部分外设接口可以配置到任意空闲管脚上。即硬件设计时，不需要严格将某些功能固定在某些管脚上；
  - WROOM-32/32D/32U 不推荐用于新设计，推荐使用 WROOM-32E/32UE 系列；
  - 在带有 QSPI PSRAM 的 WROOM-32E/32UE 系列中，GPIO16 用于连接至嵌入式 PSRAM，不可用于其他功能。

  详细信息可以参考 `《ESP32 技术规格书》 <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf>`_ 中表格 6-2 GPIO_Matrix 的内容。

  WROVER\ :sup:`*`/WROVER-I\ :sup:`*`/WROVER-B/WROVER-IB/WROVER-E/WROVER-IE 共有 24 个管脚可供客户使用，注意事项如下：

  - WROVER\ :sup:`*`/WROVER-I\ :sup:`*`/WROVER-B/WROVER-IB 系列的 GPIO6-GPIO11 被内置 flash 占用，不可用做它用；
  - WROVER-E/WROVER-IE 系列的 GPIO6-GPIO11 被内置 flash 占用，且不再拉出至模组管脚；
  - GPIO34、35、36 和 39 为输入管脚，不具备输出能力；
  - WROVER 系列模组中，GPIO12 由于在模组内部被上拉，不建议用做触摸传感功能；
  - ESP32 内置 GPIO 矩阵，部分外设接口可以配置到任意空闲管脚上。即硬件设计时，不需要严格将某些功能固定在某些管脚上；
  - WROVER\ :sup:`*`/WROVER-I\ :sup:`*`/WROVER-B/WROVER-IB 不推荐用于新设计，推荐使用 WROVER-E/WROVER-IE 系列。

  详细信息可以参考 `《ESP32 技术规格书》 <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf>`_ 中表格 6-2 GPIO_Matrix 的内容。

  ESP32 有 3 组 UART，但下载只可使用 UART0，且管脚固定。

  \ :sup:`*` 表示该产品处于生命周期终止状态。

----------------------------

ESP8266 部分 GPIO 出现高电平的原因是什么？
---------------------------------------------------------

  - 根据硬件设计，部分 GPIO 存在默认上下拉状态，所以在系统初始化时，该管脚的电平状态不受程序控制，所以会出现程序在引导过程中部分 GPIO 电平不正确。
  - 如果需要使用这些 GPIO ，硬件上建议外接器件与默认上下拉电平一致，软件可以在引导加载程序过程中调整电平状态，软件方法也会存在短暂电平异常。

--------------

ESP32 是否可以关闭线程调度使用一个单独的 CPU 以实现 GPIO 实时控制？
--------------------------------------------------------------------------

  - 目前 SDK 没有相关的配置选择供 CPU1 单独运行，两个核心只支持 SMP，不支持 AMP。
  - 解决输出波形被打断的问题有以下解决方案:

    - 使用硬件的信号输出，选择相关数字协议实现 SPI、I2C、I2S 等，特殊用法 SPI 取信号输出线产生波形。
    - 硬件 RMT 是否可以产生想要的波形，并达到足够的长度。
    - 硬件中断中产生相应波形，需要将所有回调放入 IRAM 中。
    - 可以利用芯片中的协处理器，它可以当作无操作系统的单片机。

--------------

ESP32 GPIO 电平翻转速度是多少？
--------------------------------------

  GPIO 电平翻转大约耗时 300 ns。

--------------

ESP32 当⼀些 RTC 外设的电源打开时（SARADC1、SARADC2、AMP、HALL 传感器），GPIO36 和 GPIO39 的数字输⼊会被拉低约 80 ns，如何解决？
--------------------------------------------------------------------------------------------------------------------------------------------------------

  - 对于需要精确计时和检测数字输入状态的应用，可通过软件避开以上问题：
    - 控制以上传感器的电源域打开时，忽略来⾃ GPIO36 和 GPIO39 的输⼊。
    - 通过软件实现数字输入的去抖动：在读取 GPIO36 和 GPIO39 输入状态时，可以在软件层面实现去抖动，对输入状态进行多次采样和滤波，从而减少电压短暂下降所导致的错误判断。

--------------

ESP32 如果多个 GPIO 管脚配置了沿中断，则硬件可能⽆法正确触发中断。如何解决？
------------------------------------------------------------------------------------------------

  - 请在 `《ESP32 系列芯片勘误表》 <https://www.espressif.com/sites/default/files/documentation/esp32_errata_cn.pdf>`_ 中查找该问题及答案。

--------------

使用 ESP-WROOM-02D 模组，GPIO0、GPIO15、GPIO1 和 GPIO3 是否可作为普通 GPIO 使用?
----------------------------------------------------------------------------------------------------------------------------------

  - Strapping 管脚（GPIO0 和 GPIO15）和下载管脚（GPIO1 和 GPIO3）可以作为普通 GPIO 使用。
  - 使用 Strapping 管脚作为普通 GPIO 使用时，在 flash 下载模式时需要注意 Strapping 管脚电平的要求。

---------------

ESP32-C3 系列芯片将 GPIO19 配置成输入下拉时，读取该 IO 口状态依旧显示高电平，但配置 ESP32-C3 的其他管脚或者其他芯片的管脚为输入下拉时，均正常显示为低电平？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP32-C3 的 GPIO19 为 USB D+ 管脚，USB 管脚的上拉电阻由管脚上拉和 USB 上拉共同控制，当其中一种上拉方式为 1 时，对应的上拉电阻就会使能。
  - GPIO19 是默认 USB 上拉使能的，因此配置了管脚为输入下拉后依旧是上拉使能，管脚显示高电平。
  - v4.4.3 及以上版本 GPIO 驱动已经修复该问题，如果您在使用较低版本的 ESP-IDF，请直接将 ``USB_SERIAL_JTAG_DP_PULLUP`` 寄存器写为 0 进行配置。

-----------------------

使用 ESP-IDF release/v4.2 版本的 SDK，ESP32 如何设置单个 GPIO 同时作为输入/输出模式？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  可使用 `esp_err_t gpio_set_direction(gpio_num_t gpio_num, gpio_mode_t mode) <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.2/esp32/api-reference/peripherals/gpio.html#_CPPv418gpio_set_direction10gpio_num_t11gpio_mode_t>`_ API 来设置。

-----------------------

ESP-IDF 里是否能设置 GPIO 的驱动强度？
------------------------------------------------------------

  可以。请使用 `API gpio_set_drive_capability <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/peripherals/gpio.html#_CPPv425gpio_set_drive_capability10gpio_num_t16gpio_drive_cap_t>`_ 来设置 GPIO 驱动强度。

---------------

ESP32 使用 `gpio_install_isr_service() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/gpio.html#_CPPv424gpio_install_isr_servicei>`_ 初始化新的 GPIO 中断服务时返回 `ESP_ERR_NOT_FOUND`，可能是什么原因？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  这个错误通常代表 ESP32 的可用中断源不够用，此时应该同时有多个外设在同时占用中断源，可尝试减少其他组件的中断源使用个数来初始化新的 GPIO 中断。

---------------

如何获取 ESP32 RTC_GPIO 的输入电平状态？
------------------------------------------------------------------------------------------------

  - 可读取 RTC GPIO 对应的寄存器地址的宏来获取 RTC_GPIO 的输入电平状态，可参考 `“esp-idf\components\soc\esp32\include\soc\rtc_io_reg.h” <https://github.com/espressif/esp-idf/blob/8a08cfe7d162bb9c07568b0635193bf922377123/components/soc/esp32/include/soc/rtc_io_reg.h#L91>`_ 。
  - 对应的代码参考如下：

  .. code-block:: c

    uint8_t level = (uint8_t)((REG_GET_FIELD(RTC_GPIO_IN_REG, RTC_GPIO_IN_NEXT) & BIT(gpio_num)) ? 1 : 0);

----------

如何在 Light-sleep 模式下使用 GPIO 按键？
----------------------------------------------------------------

  可以启用按键的唤醒功能，注意，非 RTC GPIO 无法同时启用 GPIO 边沿触发和电平触发。可以使用 `Button <https://components.espressif.com/components/espressif/button>`_ 组件现有的功能来实现。

----------

ESP32-C6 的 GPIO20 初始状态默认为 SDIO 管脚，如何改为普通 GPIO 模式？
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  可使用如下代码将 ESP32-C6 GPIO20 的初始 SDIO 状态改为普通 GPIO 模式：

    .. code:: c

      gpio_hal_iomux_func_sel(GPIO_PIN_MUX_REG[20], PIN_FUNC_GPIO);

----------

ESP32-P4 的不同 GPIO 是否可以设置不同的电平？例如，将 HP 电源域的 GPIO 设置为 3.3 V，同时将 LP 电源域的 GPIO 设置为 1.8 V？
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  不可以混合设置。所有 GPIO 引脚的电平必须统一，要么全部是 1.8 V，要么全部是 3.3 V。例如，如果 VDDPST_4 输入 1.8 V 电压，则该电源域下的所有 GPIO 电平均为 1.8 V。