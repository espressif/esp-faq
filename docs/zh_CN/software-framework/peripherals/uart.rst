UART 控制器
=============

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

使用 ESP8266 RTOS v2.1 以及之前版本 SDK，如何将日志配置到 UART1？
-------------------------------------------------------------------------------

  在配置 UART1 初始化后，可以通过 API 切换日志输出到 UART1。

  .. code-block:: c

    UART_SetPrintPort(UART1);

-----------------

使用 ESP8266 RTOS v3.0 以及之后的 SDK，如何将日志配置到 UART1 ？
------------------------------------------------------------------------------------

  可通过 ``menuconfig`` -> ``Component config`` -> ``ESP8266-specific`` -> ``UART for console output`` -> ``custom`` -> ``UART peripheral to use for console output`` -> ``UART0`` 修改为 UART1 接口。

--------------

ESP32 IDF 中如何使能 UART 流控？
----------------------------------------------

  - 使能硬件流控，请参考 `uart-flow-control <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/peripherals/uart.html#id5>`_。
  - 使能软件流控，请参考 `software-flow-control <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/peripherals/uart.html#id11>`_。

--------------

ESP32 使用 UART0 作为通信串口，有哪些需要注意的地方？
---------------------------------------------------------

  - 通常情况下不建议将 UART0 作为普通的通信串口，因为 UART0 为设备默认日志输出串口。
  - 若 ESP32 的 UART 不够用，或者硬件设计已经不方便更改的情况下，如果您要使用 UART0 作为普通的通信串口，请参考以下建议：

  **软件方面**：防止打印影响串口通信，默认程序中 UART0 主要有三处打印设置。

    - 第一处是一级引导程序（ROM 固件） 打印，上电时可将 MTDO 管脚设为低电平屏蔽 ROM 固件打印。
    - 第二处是二级引导加载程序日志信息输出，您可以将 ``menuconfig`` -> ``Bootloader config`` -> ``Bootloader log verbosity`` 设置为 ``No output`` 来屏蔽引导加载程序日志输出。
    - 第三处是应用日志输出，您可以将 ``menuconfig`` -> ``Component config`` -> ``Log output`` -> ``Default log verbosity`` 设置为 ``No output`` 来屏蔽应用日志输出。

  **硬件方面**：

    - 在下载程序的时候，注意防止 UART0 上有其它设备，如果有其它设备可能会影响程序的下载。建议在 ESP32 和其它设备之间预留一个 0 Ω 电阻，如果下载有问题可以断开这个 0 Ω 电阻。

-----------------

ESP32 的 GPIO34 ～ GPIO39 是否可作为 UART 的 RX 及 TWAI® 的 RX 信号管脚？
--------------------------------------------------------------------------------------------------------

  GPIO34 ～ GPIO39 仅作为接收，可作为 UART 的 RX 及 TWAI 的 RX 信号管脚。

---------------

使用 ESP32 如何动态修改串口波特率并立即生效？
---------------------------------------------------------------

  可以使用 ``uart_set_baudrate()`` API 来动态修改 UART 波特率。参见 `API 说明 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/peripherals/uart.html?highlight=uart_set_baud#_CPPv417uart_set_baudrate11uart_port_t8uint32_t>`_。

-------------------------------

请问 ESP32 芯片支持 USRAT（Universal Synchronous Asynchronous Receiver Transmitter） 吗？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

  不支持，ESP32 仅支持 UART，无法提供同步时钟。

-------------------------

ESP32 芯片的串口校验支持 ＭARK 和 SPACE 校验吗？
--------------------------------------------------------------------------------------------------------------------------------------------

  ESP32 芯片不支持。

-----------------------

ESP8266 串口的硬件 FIFO 是多大？
----------------------------------------------------------------------------------------------------------------

  ESP8266 的 UART0 和 UART1 各有⼀个⻓度为 128 字节的硬件 FIFO 和读写 FIFO，且都在同⼀个地址操作。参见 `《ESP8266 技术参考手册》 <https://www.espressif.com/sites/default/files/documentation/esp8266-technical_reference_cn.pdf>`_ 中“11.2. 硬件资源”章节说明。

---------------------------

ESP8266 的串⼝波特率范围是多大？
---------------------------------------------------------------------------------------------------------------------------

  ESP8266 的串⼝波特率范围为 300 ~ 115200*40 bps。参见 `《ESP8266 技术参考手册》 <https://www.espressif.com/sites/default/files/documentation/esp8266-technical_reference_cn.pdf>`_ 中的“ 11.3.1. 波特率”章节说明。

-----------------------------------------------------------------------------------------------------

如何修改 UART0 的输出口?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32 | ESP32 | ESP32-C3:

  可以在 menuconfig 中进行设置，``idf.py menuconfig`` —> ``Component config`` —> ``Common ESP-related`` -> ``Channel for console output(custom UART)``。

-----------------

使用 ESP8266，想把 UART0 专门用作下载，再使用 UART1 与其他芯片通信。GPIO4 和 GPIO5 能配置成 UART1 串口吗？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 由于 UART1 的 RXＤ 被占用了，所以 UART1 不能与其他芯片进行通讯，但 UART1 的 TXD 管脚可用作输出日志。
  - ESP8266 与其他芯片通信只能通过 UART0 的 CTS 和 RTS 管脚交换来实现，配置成 GPIO4 和 GPIO5 是无效的。
  - ESP8266 与其他芯片通信可通过调用 ``uart_enable_swap()`` 函数，通过 UART0 的 CTS 和 RTS 引脚进行交换，交换为 MTCK (IO13)、MTDO (IO15) 管脚。管脚交换后 ESP8266 可通过 GPIO13（RXD）和 GPIO15（TXD）来与其他芯片进行 UART 通信。

--------------

ESP32 的 UART0 是否可以在输出日志的同时又用作接收电脑控制台的输入？
--------------------------------------------------------------------------------------------------------------------------------

  可以。UART0 输出日志只需要使用 TXD0 管脚，接收电脑控制台的输入只需要使用 RXD0 管脚。可基于 `esp-idf/examples/system/console/basic <https://github.com/espressif/esp-idf/tree/master/examples/system/console/basic>`_ 例程来测试。

--------------

如何实现 UART 信号反转呢？
--------------------------------------------------------------------------------------------------------------------------------

  可以使用 `uart_set_line_inverse <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/uart.html#_CPPv421uart_set_line_inverse11uart_port_t8uint32_t>`_ 接口来设置。反转引脚参数可以从 `uart_signal_inv_t <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/uart.html#_CPPv417uart_signal_inv_t>`_ 变量中获取。

--------------

ESP 模组 UART 支持 LIN 模式吗?
--------------------------------------------------------------------------------------------------------------------------------

  硬件上不支持，需要软件上进行模拟，官方暂时没有参考资料。

------------

ESP32 是否支持 UART IRDA 工作模式？
---------------------------------------------------------------------------------------------------------------------

  ESP32 硬件上可以支持 UART IRDA 工作模式，但软件上还没有对应的驱动实现。

------------

在串口资源有限的情况下，是否支持基于 GPIO 的 UART 模拟？
---------------------------------------------------------------------------------------------------------------------
  
  可基于 `soft_uart <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/dedicated_gpio/soft_uart>`_ 例程来测试。

---------------

在 ESP32-C6 未进入 DeepSleep 模式的情况下，是否可以同时使用 UART 和 LP UART？
--------------------------------------------------------------------------------------------------------------------------------------------------------------

  可以同时使用。只需使能 LP Core，即可使用 LP UART。例程请参考：`esp-idf/examples/system/ulp/lp_core/lp_uart <https://github.com/espressif/esp-idf/tree/release/v5.3/examples/system/ulp/lp_core/lp_uart>`_。
