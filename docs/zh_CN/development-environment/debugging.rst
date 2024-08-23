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

ESP 设备的串口名称是什么？
-----------------------------------------

  串口名称通常是由操作系统指定的，不同的操作系统和设备可能会有不同的串口名称。常见如下：

  - Windows 系统中串口设备名称格式是 COM*
  - Linux 系统中：
    - UART 接口设备名称格式是 /dev/ttyUSB*
    - USB 接口设备名称是 /dev/ttyACM*
  - macOS 系统中串口设备名称格式是 /dev/cu.usbserial-*

--------------

ESP32 如何关闭默认通过 UART0 发送的调试信息？
---------------------------------------------

  - 一级 Bootloader 日志信息可以通过 GPIO15 接地来屏蔽。
  - 二级 Bootloader 日志信息可以在 menuconfig 里的 ``Bootloader config`` 中进⾏相关配置。
  - ESP-IDF 中的日志信息可以在 menuconfig 里的 ``Component config`` > ``Log output`` 中进⾏相关配置。

--------------

ESP32 如何修改默认上电 RF 校准⽅式？
------------------------------------

  - 上电时 RF 初始化默认采⽤部分校准的⽅案：打开 menuconfig 中 ``CONFIG_ESP32_PHY_CALIBRATION_AND_DATA_STORAGE`` 选项。
  - 不关注上电启动时间，可修改使⽤上电全校准⽅案：关闭 menuconfig 中 ``CONFIG_ESP32_PHY_CALIBRATION_AND_DATA_STORAGE`` 选项。
  - 建议默认使用 **部分校准** 的方案，这样既可以保证上电启动的时间，也可以在业务逻辑中增加擦除 NVS 中 RF 校准信息的操作，以触发全校准的操作。

  请参考 `RF 校准文档 <https://docs.espressif.com/projects/esp-idf/en/v4.4.4/esp32/api-guides/RF_calibration.html>`__ 获取更多信息。

--------------

ESP8266 如何修改默认上电校准⽅式？
--------------------------------------

  上电时 RF 初始化默认采⽤部分校准的⽅案。该方案中 esp_init_data_default.bin 的第 115 字节为 ``0x01``，RF 初始化时间较短。如不关注上电启动时间，可修改使⽤上电全校准⽅案。

  **使⽤ NONOS SDK 及 RTOS SDK 3.0 以前的版本：**

  - 在 user_pre_init 或 user_rf_pre_init 函数中调⽤ system_phy_set_powerup_option(3)。
  - 修改 phy_init_data.bin 中第 115 字节为 ``0x03``。

  **使⽤ RTOS SDK 3.0 及以后版本：**

  - 在 menuconfig 中关闭 CONFIG_ESP_PHY_CALIBRATION_AND_DATA_STORAGE。
  - 如果在 menuconfig 中开启了 CONFIG_ESP_PHY_INIT_DATA_IN_PARTITION，修改 phy_init_data.bin 中第 115 字节为 ``0x03``；如果没有开启 CONFIG_ESP_PHY_INIT_DATA_IN_PARTITION，修改 phy_init_data.h 中第 115 字节为 ``0x03``。

  **继续使⽤上电部分校准⽅案，若需在业务逻辑中增加触发全校准操作的功能：**

  - 使⽤ NONOS SDK 及 RTOS SDK 3.0 以前的版本：擦除 RF 参数区中的内容，触发全校准操作。
  - 使⽤ RTOS SDK 3.0 及以后版本：擦除 NVS 分区中的内容，触发全校准操作。

--------------

ESP32 Boot 启动模式不正常如何排查？
-----------------------------------

  - ESP32-WROVER\ :sup:`*` 模组使用 1.8 V flash 与 PSRAM，启动状态默认为 ``0x33``，下载模式 ``0x23``。
  - 其余模组使用 3.3 V flash 与 PSRAM，启动状态默认为 ``0x13``，下载模式 ``0x03``。
  - 详情请参考 `ESP32 系列芯片技术规格书 <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf>`_ 中的 Strapping 管脚部分。示例 ``0x13`` 对应如下：

    +--------+--------+-------+-------+-------+--------+-------+
    | 管脚   | GPIO12 | GPIO0 | GPIO2 | GPIO4 | GPIO15 | GPIO5 |
    +========+========+=======+=======+=======+========+=======+
    | 电平   |    0   |   1   |   0   |   0   |    1   |   1   |
    +--------+--------+-------+-------+-------+--------+-------+

  您也可以直接参考 `Boot 模式选择文档 <https://docs.espressif.com/projects/esptool/en/latest/esp32/advanced-topics/boot-mode-selection.html>`__。

  \ :sup:`*` 表示该产品处于生命周期终止状态。

--------------

使用 ESP32 JLINK 调试，发现会报 ERROR：No Symbols For Freertos，如何解决呢？
-----------------------------------------------------------------------------

  该错误日志不影响调试使用，解决措施可以参考 `ST 论坛 <https://community.st.com/s/question/0D50X0000BVp8RtSQJ/thread-awareness-debugging-in-freertos-stm32cubeide-110-has-a-bug-for-using-rtos-freertos-on-stlinkopenocd>`_。

--------------

如何监测任务栈的剩余空间？
--------------------------

  调用函数 ``vTaskList()`` 可以用于定期打印任务栈的剩余空间。详细的操作可以参考 `CSDN 文档 <https://blog.csdn.net/espressif/article/details/104719907>`_。

--------------

ESP32-S2 是否可以使用 JTAG 进行下载调试？
-----------------------------------------

  可以，详情请参考 `ESP32-S2 JTAG 调试 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32s2/api-guides/jtag-debugging/>`_。

--------------

如何在不更改 menuconfig 输出级别的情况下调整日志输出？
-------------------------------------------------------

  要修改日志输出而不改变 menuconfig 的输出级别，您可以使用 ``esp_log_level_set()`` 函数。此函数允许您为特定模块或子系统设置日志级别，而不是更改全局日志级别。

  例如，要将 network 模块的日志级别设置为 ``ESP_LOG_DEBUG``，可以使用以下代码：

  .. code-block:: c

    esp_log_level_set("network", ESP_LOG_DEBUG);

  有关此功能的更多信息，请参阅 `Logging library <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/system/log.html>`_。

--------------

为什么 ESP8266 进⼊启动模式 (2,7) 并触发看⻔狗复位？
-----------------------------------------------------

  - 请确保 ESP8266 启动时，Strapping 管脚处于所需的电平。如果外部连接的外设使 Strapping 管脚进⼊到错误的电平，ESP8266 可能进⼊错误的操作模式。在⽆有效程序的情况下，看⻔狗计时器将复位芯⽚。
  - 因此在设计实践中，建议仅将 Strapping 管脚⽤于连接高阻态外部器件的输⼊，这样便不会在上电时强制 Strapping 管脚为高/低电平。详情请参考 `ESP8266 Boot Mode Selection <https://github.com/espressif/esptool/wiki/ESP8266-Boot-Mode-Selection>`_。

--------------

ESP-WROVER-KIT 开发板 OpenOCD 错误 Error: Can't find board/esp32-wrover-kit-3.3v.cfg，如何解决？
-----------------------------------------------------------------------------------------------------

  - OpenOCD 版本为 20190313 和 20190708，请使用 ``openocd -f board/esp32-wrover.cfg`` 指令打开。
  - OpenOCD 版本为 20191114 和 20200420（2020 以上版本），请使用 ``openocd -f board/esp32-wrover-kit-3.3v.cfg`` 指令打开。

--------------

ESP32 SPI boot 时会一直发生 RTC_WDT 复位是什么原因?
------------------------------------------------------------------------------------------------------

  - 原因：flash 对 VDD_SDIO 上电到第一次访问之间有时间间隔要求。例如，GD 的 1.8 V Flash 要求从供电到第一次访问的时间间隔为 5 ms，而 ESP32 的时间间隔则为 1 ms 左右（XTAL 频率为 40 MHz），此时，访问 flash 会出错，接着会触发定时器看门狗或 RTC 看门狗重置，具体的重置类型取决于谁先被触发。RTC 看门狗重置的门限是 128 KB cycle，定时器看门狗重置的门限是 26 MB cycle。以 40 MHz 的 XTAL 时钟频率为例，当 RTC 慢速时钟的频率大于 192 KHz 时，会先触发 RTC 看门狗重置，反之则触发定时器看门狗重置。定时器看门狗重置时，VDD_SDIO 会持续供电，此时访问 flash 不会出现问题，芯片可以正常工作。而 RTC 看门狗重置时会停止 VDD_SDIO 供电，此时访问 flash 则会因为不满足 flash 上电到第一次访问的时间间隔而导致持续复位。
  - 解决办法：当发生 RTC 看门狗重置时，VDD_SDIO 的供电停止，可以通过 VDD_SDIO 加上一个电容来保证这段时间 VDD_SDIO 的电压不会掉到 flash 能够容忍的电压以下。

--------------

ESP32 如何获取与解析 coredump？
-----------------------------------

  - 从完整的固件中提取出 64 KB 大小的 coredump，需要先从分区表中确认 coredump 的偏移量。假设当前偏移量为 ``0x3F0000``，运行如下命令读取固件：

    .. code-block:: text

      python esp-idf/components/esptool_py/esptool/esptool.py -p /dev/ttyUSB* read_flash 0x3f0000 0x10000  coredump.bin

  - 使用 coredump 读取脚本将二进制的 coredump 文件转变成可读的信息。假设第一步获得的 coredump 文件为 coredump.bin，此固件对应的 elf 文件为 hello_world.elf，运行如下命令转换文件：

    .. code-block:: text

      python esp-idf/components/espcoredump/espcoredump.py info_corefile -t raw -c coredump.bin hello_world.elf

  也可以参考 `Core Dump 文档 <https://docs.espressif.com/projects/esp-idf/en/v4.4.4/esp32/api-guides/core_dump.html>`__ 了解更多信息。

--------------

ESP32、ESP8266、ESP32S2 如何做射频性能测试？
-----------------------------------------------------------------

  请参见 `ESP 射频测试指南 <https://www.espressif.com/sites/default/files/tools/ESP_RF_Test_CN.zip>`_ 中 ``help`` 文件夹下的文档说明。

--------------

Win 10 系统下识别不到 ESP 设备有哪些原因？
----------------------------------------------------------------------------------------
  - 请检查是否开启了任何安全防护软件。
  - 请检查是否是在 Win10 Linux 虚拟子系统下识别设备。
  - 如果只是在 Win10 下识别不到设备，应前往设备管理器，查看是否有对应设备，如 COM x。若没有识别到任何设备，请查看设备接线以及驱动是否正常。
  - 如果是在 Linux 虚拟子系统下识别不到设备，在完成设备接线以及驱动检查后，以 VMWare 为例，前往虚拟机设置窗口里的 “USB 控制器”，勾选 “显示所有 USB 输入设备”。

--------------

ESP32 出现 Error:Core 1 paniced (Cache disabled but cache memory region accessed) 是什么原因？
----------------------------------------------------------------------------------------------------

  问题原因：

  - 在 cache 被禁用期间（例如在使用 spi_flash API 读取/写入/擦除/映射 SPI flash 的时候），发生了中断并且中断程序访问了 flash 的资源。
  - 通常发生在处理程序调用了在 flash 中的程序，引用了 flash 中的常量时。值得注意的是，当在中断程序里面使用 double 类型变量时，由于 double 型变量操作的实现属于软件实现，该部分实现也被链接在了 flash 中（例如强制类型转换操作）。

  解决措施：

  - 给在中断中访问的函数加上 IRAM_ATTR 修饰符。
  - 给在中断中访问的常量加上 DRAM_ATTR 修饰符。
  - 不在中断处理程序中使用 double 类型。

  您也可以参考 `严重错误文档 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/fatal-errors.html#cache-err-msg>`__ 来获取更多信息。

--------------

如何读取模组 Flash 型号信息？
----------------------------------

  - 乐鑫模组或芯片可通过 python 脚本 `esptool <https://github.com/espressif/esptool>`_ 读取。
  - Windows 环境：

    .. code-block:: text

      esptool.py -p COM* flash_id

  - Linux 环境：

    .. code-block:: text

      esptool.py -p /dev/ttyUSB* flash_id


--------------

调试 ESP-IDF 里的 `Ethernet 示例 <https://github.com/espressif/esp-idf/tree/master/examples/ethernet>`__，出现如下异常日志如何解决？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    emac: Timed out waiting for PHY register 0x2 to have value 0x0243(mask 0xffff). Current value:

  可以参考开发板的如下配置，详见开发板原理图:

    - CONFIG_PHY_USE_POWER_PIN=y
    - CONFIG_PHY_POWER_PIN=5

---------------

使用 ESP32 时出现 “Brownout detector was triggered” 报错，原因是什么，如何解决？
--------------------------------------------------------------------------------------------------------------------------

  - ESP32 内置有掉电探测器，当其探测到芯片电压低于一定的预设阈值时，将重置芯片以防出现意外情况。
  - 该报错信息可能会在不同场景内出现，但根本原因都在于芯片的供电电压暂时或永久性地低于掉电阈值。可通过替换稳定的电源、USB 电缆，或在模组内增加电容来解决。
  - 对于使用电池供电的产品，可以检查一下上电时序，或者更换能提供大电流的电池，或者尝试增加电源的电容。
  - 除此之外，也可以通过配置重置掉电阈值，或禁用掉电探测功能。详细信息请参考 `config-esp32-brownout-det <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/kconfig.html#brownout-detector>`_。
  - 关于 ESP32 上电、复位时序说明，详见 `《ESP32 技术规格书》 <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf>`_。

---------------

ESP32 导入头文件 protocol_examples_common.h 后，为什么编译时提示找不到该文件?
--------------------------------------------------------------------------------------------------------------

  - 在工程下的 CMakeLists.txt 中添加语句 “set(EXTRA_COMPONENT_DIRS $ENV{IDF_PATH}/examples/common_components/protocol_examples_common)” 即可。
  - 您也可以参考 `构建系统文档 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/build-system.html>`__ 来获取更多信息。

--------------

使用 ESP8266 NonOS v3.0 版本的 SDK，如下报错是什么原因？
------------------------------------------------------------------------

  .. code-block:: text

    E:M 536    E:M 1528

  以 E:M 开头的报错表示内存不足。

--------------

使用 flash_download_tool 给 ESP8266 模组烧录固件时，出现如下错误如何解决？
---------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    ESP8266 Chip efuse check error esp_check_mac_and_efuse

  - 原因：

    - 出现 ``efuse check error`` 说明芯片内部的 eFuse 参数区域遭到意外修改。eFuse 中通常存储着一些重要信息，比如芯片的配置以及 MAC 地址。如果 eFuse 损坏，将导致芯片不可用。
    - eFuse 损坏通常由过压或者静电导致。

  - 建议：

    - 检测电源部分上下电过程中的波动情况。
    - ESP32-C3/ESP32-C2 芯片的 eFuse 功能有所加强，后续可以考虑替换相关产品。

--------------

从 ESP-IDF v4.4 版本更新到 v5.0 以及以上版本，会报 `esp_log.h:265:27: error: format '%d' expects argument of type 'int', but argument 6 has type 'uint32_t' {aka 'long unsigned int'} [-Werror=format=]265 | #define LOG_COLOR(COLOR)  "\033[0;" COLOR "m"` 错误，如何解决？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 这是乐鑫工具链更新导致的错误，具体原因和解决方法可参考 `迁移指南：从 4.4 迁移到 5.0 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/migration-guides/release-5.x/5.0/gcc.html#xtensa-int32-t-uint32-t>`__。
  - 如想有意忽视这个错误（不推荐），也可以在编译报错文件对应的 cmake 里添加 ``target_compile_options(${COMPONENT_LIB} PRIVATE -Wno-pointer-sign -Wno-format)``。

------------

ESP32 系列产品是否支持在 `边界扫描 <https://www.jtag.com/boundary-scan/>`_ 环境中使用 JTAG 功能？从哪里可以下载 BSDL 文件？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  由于硬件限制，目前 ESP32 系列产品都不支持边界扫描功能，因此不支持在边界扫描环境中使用 JTAG，也没有 BSDL 文件。
