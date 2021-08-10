调试分析
========

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

使用 ESP32 ，在快速掉电再上电后，出现产品起不来的现象，是什么原因？
-------------------------------------------------------------------

  场景描述：电源为 220 V 转 5 V，5 V 转 3.3 V，220 V 掉电再上电出现故障。报错 log 如下: 

  .. code-block:: text

    brownout detector was triggered.
    rst:0xc(SW_CPU_RESET),boot:0x13(SPI_FAST_FLASH_BOOT) configsip:0,SPI

  - 打印此 log 是因为在快速掉电过程中，电压降到了触发硬件看门狗的电压阈值。
  - 由于上电时序不对，导致没有进入 bootloader ，可以将 chip_PU 强制拉低解除故障。
  - ESP32 上电、复位时序说明，详见 `《ESP32技术规格书》 <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf>`_。

--------------

Wi-Fi 设备的串口名称？
----------------------

  - Windows 系统中串口设备名称格式是：COM*
  - Windows 10 ⼦统系 linux 中串口设备名称的标准格式是：/dev/ttyS*
  - Linux 系统中串口设备名称格式是：/dev/ttyUSB*
  - macOS 系统中串口设备名称格式是: /dev/cu.usbserial-*

--------------

ESP32 如何关闭默认通过 UART0 发送的调试信息？
---------------------------------------------

  - 一级 Bootloader log 信息可以通过 GPIO15 接地来使能屏蔽。
  - 二级 Bootloader log 信息可以通过 make menuconfig 中 ``Bootloader config`` 进⾏相关配置。
  - IDF 中 log 信息可以通过 make menuconfig 中 ``Component config/Log output`` 进⾏相关配置。

--------------

ESP32 如何修改默认上电校准⽅式？
------------------------------------

  - 上电时 RF 初始化默认采⽤部分校准的⽅案：打开 menuconfig 中 ``CONFIG_ESP32_PHY_CALIBRATION_AND_DATA_STORAGE`` 选项。
  - 不关注上电启动时间，可修改使⽤上电全校准⽅案：关闭 menuconfig 中 ``CONFIG_ESP32_PHY_CALIBRATION_AND_DATA_STORAGE`` 选项。
  - 建议默认使用 **部分校准** 的方案，这样既可以保证上电启动的时间，也可以在业务逻辑中增加擦除 NVS 中 RF 校准信息的操作，以触发全校准的操作。

--------------

ESP8266 如何修改默认上电校准⽅式？
--------------------------------------

  上电时 RF 初始化默认采⽤部分校准的⽅案： esp_init_data_default.bin 中第 115 字节为 ``0x01``，RF 初始化时间较短。不关注上电启动时间，可修改使⽤上电全校准⽅案。

  **使⽤ NONOS SDK 及 RTOS SDK 3.0 以前的版本：**

  - 在 user_pre_init 或 user_rf_pre_init 函数中调⽤ system_phy_set_powerup_option(3)；
  - 修改 phy_init_data.bin 中第 115 字节为 ``0x03``。 

  **使⽤ RTOS SDK 3.0 及以后版本：**

  - 在 menuconfig 中关闭 CONFIG_ESP_PHY_CALIBRATION_AND_DATA_STORAGE；
  - 如果在 menuconfig 中开启了 CONFIG_ESP_PHY_INIT_DATA_IN_PARTITION，修改 phy_init_data.bin 中第 115 字节为 ``0x03``； 如果没有开启 CONFIG_ESP_PHY_INIT_DATA_IN_PARTITION，修改 phy_init_data.h 中第 115 字节为 ``0x03``。
  
  **继续使⽤上电部分校准⽅案，若需在业务逻辑中增加触发全校准操作的功能：**

  - 使⽤ NONOS SDK 及 RTOS SDK 3.0 以前的版本：擦除 RF 参数区中的内容，触发全校准操作。
  - 使⽤ RTOS SDK 3.0 及以后版本：擦除 NVS 分区中的内容，触发全校准操作。

--------------

ESP32 boot 启动模式不正常如何排查？
-----------------------------------

  - ESP32-WROVER 模组使用 1.8 V flash 与 PSRAM 启动状态默认为 ``0x33`` ,下载模式 ``0x23`` 。
  - 其余模组使用 3.3 V flash 与 PSRAM 模组默认为 ``0x13`` , 下载模式 ``0x03`` 。
  - 详情请参考 ESP32 系列芯片技术规格书中 Strapping 管脚部分。示例 ``0x13`` 对应如下： 

  +--------+--------+-------+-------+-------+--------+-------+
  | 管脚   | GPIO12 | GPIO0 | GPIO2 | GPIO4 | GPIO15 | GPIO5 |
  +========+========+=======+=======+=======+========+=======+
  | 电平   |    0   |   1   |   0   |   0   |    1   |   1   |
  +--------+--------+-------+-------+-------+--------+-------+

--------------

使用 ESP32 JLINK 调试，发现会报 ERROR：No Symbols For Freertos ，如何解决呢？
-----------------------------------------------------------------------------

  该错误 log 不影响调试使用，解决措施可以参考 `此论坛 <https://community.st.com/s/question/0D50X0000BVp8RtSQJ/thread-awareness-debugging-in-freertos-stm32cubeide-110-has-a-bug-for-using-rtos-freertos-on-stlinkopenocd>`_。

--------------

如何监测任务栈的剩余空间？
--------------------------

  调用函数 ``vTaskList()`` 可以用于定期打印任务栈的剩余空间。

--------------

ESP32-S2 是否可以使用 JTAG 进行下载调试？
-----------------------------------------

  可以，详情请参考 `ESP32-S2 JATG 调试 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32s2/api-guides/jtag-debugging/>`_。

--------------

如何在不更改 menuconfig 输出级别的情况下调整 log 输出？
-------------------------------------------------------

  可以通过函数 ``esp_log_level_set()`` 修改 log 的输出级别。

--------------

为什么 ESP8266 进⼊启动模式（2，7）并触发看⻔狗复位？
-----------------------------------------------------

  - 请确保 ESP8266 启动时，strapping 管脚处于所需的电平。如果外部连接的外设使 strapping 管脚进⼊到错误的电平，ESP8266 可能进⼊错误的操作模式。在⽆有效程序的情况下，看⻔狗计时器将复位芯⽚。
  - 因此在设计实践中，建议仅将 strapping 管脚⽤于连接⾼阻态外部器件的输⼊，这样便不会在上电时强制 strapping 管脚为⾼/低电平。参考链接：`ESP8266 Boot Mode Selection <https://github.com/espressif/esptool/wiki/ESP8266-Boot-Mode-Selection>`_。

--------------

ESP-WROVER-KIT 开发板 openocd 错误 Error: Can't find board/esp32-wrover-kit-3.3v.cfg？
-----------------------------------------------------------------------------------------------------

  - openocd 版本为 20190313 和 20190708，请使用 ``openocd -f board/esp32-wrover.cfg`` 指令打开。
  - openocd 版本为 20191114 和 20200420（2020 以上版本）， 请使用 ``openocd -f board/esp32-wrover-kit-3.3v.cfg`` 指令打开。

--------------

ESP32 如何获取与解析 coredump？
-----------------------------------

  - 从完整的固件中提取出 64 K 大小的 coredump，需要先从分区表中确认 coredump 的偏移量，当前假设为 ``0x3F0000``。

  .. code-block:: text

    python esp-idf/components/esptool_py/esptool/esptool.py -p /dev/ttyUSB* read_flash 0x3f0000 0x10000  coredump.bin

  - 使用 coredump 读取脚本将二进制的 coredump 文件转变成可读的信息。假设第一步获得的 coredump 文件为 coredump.bin，与固件对于的 elf 文件 hello_world.elf。

  .. code-block:: text

    python esp-idf/components/espcoredump/espcoredump.py info_corefile -t raw -c coredump.bin hello_world.elf

--------------

ESP32&ESP8266&ESP32S2 如何做射频性能测试？
-----------------------------------------------

  - 参见：`ESP 射频测试指南 <https://www.espressif.com/sites/default/files/tools/ESP_RF_Test_CN.zip>`_。
  
--------------

Win 10 系统下识别不到设备有哪些原因？
----------------------------------------

  - 是否是在 Win10 Linux 虚拟子系统下识别设备。
  - 如果只是在 Win 10 下识别不到设备，应该到设备管理器查看是否有对应设备，如 COM x，若没有识别到任何设备，请查看设备接线以及驱动是否正常。
  - 如果是在 Linux 虚拟子系统下识别不到设备，在完成设备接线以及驱动是否正常的检查后，以 VMWare 为例应该到虚拟机设置窗口里的 “USB 控制器” 里勾选 “显示所有 USB 输入设备”。

--------------

ESP32 出现 Error:Core 1 paniced (Cache disabled but cache memory region accessed) 是什么原因？
----------------------------------------------------------------------------------------------------

  问题原因：

  - 在 cache 被禁用期间（例如在使用 spi_flash API 读取/写入/擦除/映射 SPI Flash 的时候），发生了中断并且中断程序访问了 Flash 的资源。
  - 通常发生在处理程序调用了在 Flash 中的程序，引用了 Flash 中的常量。值得注意的是，当在中断程序里面使用 double 类型变量时，由于 double 型变量操作的实现是软件实现的， 该部分实现也是被链接在了 Flash 中（例如强制类型转换操作）。

  解决措施：
  
  - 给在中断中访问的函数加上 IRAM_ATTR 修饰符
  - 给在中断中访问的常量加上 DRAM_ATTR 修饰符
  - 不在中断处理程序中使用 double 类型

--------------

如何读取模组 flash 型号信息？
----------------------------------

  - 乐鑫模组或芯片可通过 python 脚本 `esptool <https://github.com/espressif/esptool>`_ 读取。

  .. code-block:: text

    esptool.py --port /dev/ttyUSB* flash_id

--------------

调试 IDF 里的 Ethernet demo，出现如下异常 log？
------------------------------------------------------

  .. code-block:: text

    emac: Timed out waiting for PHY register 0x2 to have value 0x0243(mask 0xffff). Current value:

  可以参考开发板的如下配置，详见板子原理图:

    - CONFIG_PHY_USE_POWER_PIN=y
    - CONFIG_PHY_POWER_PIN=5
