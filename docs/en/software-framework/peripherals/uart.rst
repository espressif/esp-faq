Universal Asynchronous Receiver/Transmitter (UART)
==================================================

:link_to_translation:`zh_CN:[中文]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

--------------

When using ESP8266 RTOS SDK v2.1 and previous versions, how to set log to UART1?
-----------------------------------------------------------------------------------------------------------------

  After initializing UART1, you can switch log to UART1 via API:

  .. code-block:: c

    UART_SetPrintPort(UART1);

-----------------

When using ESP8266 RTOS SDK v3.0 and later versions, how to set log to UART1?
----------------------------------------------------------------------------------------------------------

  Go to ``menuconfig`` -> ``Component config`` -> ``ESP8266-specific`` -> ``UART for console output`` -> ``custom`` -> ``UART peripheral to use for console output`` -> ``UART0`` and change the option to "UART1".

--------------

How to enable UART Flow Control in ESP32 IDF?
---------------------------------------------------------------------------

  - To enable hardware flow control, please refer to `uart-flow-control <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/uart.html?highlight=uart%20flow%20control#multiple-steps>`_.
  - To enable software flow control, please refer to `software-flow-control <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/uart.html?highlight=uart%20flow%20control#software-flow-control>`_.

--------------

When using UART0 as a serial communication port for ESP32, what should I pay attention to?
---------------------------------------------------------------------------------------------------------------------

  - Generally, it is not recommended to use UART0 as a normal serial communication port, because it is the default LOG output port.
  - If the UART number in ESP32 is not enough for you or it is not convenient to change your hardware designs anymore, and UART0 is therefore going to be used as a normal communication port, please pay attention to the following suggestions:

  **Software**: You need to protect the serial communication port from being affected by printing. The UART0 mainly has three print settings in the default program:

    - The first instance is the Level 1 bootloader (ROM firmware) printout. When powered on, the MTDO pin can be set to a low level to block the ROM firmware printout.
    - The second part is the secondary bootloader log output. You can set ``menuconfig`` -> ``Bootloader config`` -> ``Bootloader log verbosity`` to ``No output`` to block the bootloader log output.
    - Third, app log output. You can set ``menuconfig`` -> ``Component config`` -> ``Log output`` -> ``Default log verbosity`` as ``Not output`` to block app log output.

  **Hardware**:

    - Pay attention to other devices on UART0 when downloading programs since they could affect downloading. It is recommended to reserve a 0 Ω resistance between ESP32 and other devices so that if there is something wrong while downloading, you can still disconnect this resistance.

-----------------

Is it possible to use GPIO34 ～ GPIO39 from ESP32 as the RX signal pin for UART and TWAI®?
-----------------------------------------------------------------------------------------------------------------------------

  Yes, GPIO34 ～ GPIO39 are for receive only and can be used as the RX signal pins for UART and TWAI®.

---------------

How to dynamically change the serial baud rate and make it take effect immediately with ESP32?
------------------------------------------------------------------------------------------------------------------------------

  You can use the ``uart_set_baudrate()`` API to dynamically change the UART baud rate. See `API Description <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/uart.html?highlight=uart_set_baud#_CPPv417uart_set_baudrate11uart_port_t8uint32_t>`_.

--------------

Does the ESP32 chip support USRAT (Universal Synchronous Asynchronous Receiver Transmitter)?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  It's not support. ESP32 only supports UART and cannot provide the synchronous clock.

----------------------------

Does the serial port verification of the ESP32 chip support MARK and SPACE verification?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  No.

----------------------------

What is the size of the hardware FIFO in ESP8266's serial port?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Both UART0 and UART1 of ESP8266 have a 128-byte hardware FIFO and a 128-byte RW FIFO, which operate at the same address. Please refer to Section 11.2. Hardware Resources in `ESP8266 Technical Reference Manual <https://www.espressif.com/sites/default/files/documentation/esp8266-technical_reference_en.pdf>`_.

---------------------------

What is the serial port baud rate range of ESP8266?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  300 ~ 115200*40 bps. Please refer to Section 11.3.1. Baud Rate in `ESP8266 Technical Reference Manual <https://www.espressif.com/sites/default/files/documentation/esp8266-technical_reference_en.pdf>`_.

-----------------------------------------------------------------------------------------------------

How to modify the output port of UART0?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32 | ESP32 | ESP32-C3:

  This can be set in menuconfig: ``idf.py menuconfig`` —> ``Component config`` —> ``Common ESP-related`` -> ``Channel for console output(custom UART)``.

------------------

When using ESP8266, I want to use UART0 exclusively for downloading, and then use UART1 to communicate with other chips. Can GPIO4 and GPIO5 be configured as UART1 serial ports?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Since the RXD of UART1 is occupied, UART1 cannot be used to communicate with other chips, but the TXD pin of UART1 can be used to output logs.
  - ESP8266 can only communicate with other chips by swapping CTS and RTS pins of UART0. It will be invalid to configure GPIO4 and GPIO5.
  - ESP8266 can communicate with other chips by calling the ``uart_enable_swap()`` function, swapping the CTS and RTS pins of UART0 for MTCK (IO13) and MTDO (IO15) pins. After the pin swap, ESP8266 can use GPIO13 (RXD) and GPIO15 (TXD) to communicate with other chips via UART.

---------------------

Can ESP32's UART0 be used for inputting from the computer console while it is being used for outputting logs?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Yes. Outputting logs only requires using the TXD0 pin, while receiving input from the computer console only requires using the RXD0 pin. You can use the `esp-idf/examples/system/console/basic <https://github.com/espressif/esp-idf/tree/master/examples/system/console/basic>`_ example for testing.

--------------

How to realize UART signal inversion?
--------------------------------------------------------------------------------------------------------------------------------

  You can use the `uart_set_line_inverse <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/uart.html#_CPPv421uart_set_line_inverse11uart_port_t8uint32_t>`_ interface to set it. The inverse pin parameter can be obtained from the `uart_signal_inv_t <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/uart.html#_CPPv417uart_signal_inv_t>`_ variable.

--------------

Does the ESP module UART support LIN mode?
--------------------------------------------------------------------------------------------------------------------------------

  LIN mode is not supported at the hardware level. You may conduct simulation on the software side to realize this feature, and there is currently no reference material available from the official source.

------------

Does ESP32 support the UART IRDA working mode?
---------------------------------------------------------------------------------------------------------------------

  ESP32 supports the UART IRDA working mode at the hardware level, but there is no corresponding driver implementation in software yet.

------------

In situations where serial port resources are limited, is GPIO-based UART simulation supported?
---------------------------------------------------------------------------------------------------------------------
  
  You can test this using the `soft_uart <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/dedicated_gpio/soft_uart>`_ example.

---------------

Can UART and LP UART be used simultaneously when ESP32-C6 is not in DeepSleep mode?
--------------------------------------------------------------------------------------------------------------------------------------------------------------

  Yes, UART and LP UART can be used simultaneously. You can enable the LP Core to use LP UART. Please refer to this use case: `esp-idf/examples/system/ulp/lp_core/lp_uart <https://github.com/espressif/esp-idf/tree/release/v5.3/examples/system/ulp/lp_core/lp_uart>`_.
