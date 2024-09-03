其他蓝牙
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

---------------

怎样通过串口给 ESP32-WROOM-32D 模块直接发送蓝牙 HCI 命令?
-----------------------------------------------------------------

  - 请参考例程 `controller_hci_uart_esp32 <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/hci/controller_hci_uart_esp32>`_。
  - ESP32 用作 controller，其他设备作为 host，可通过 UART 给 ESP32 发送 HCI 指令。
