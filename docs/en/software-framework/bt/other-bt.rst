Other Bluetooth
=================

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

How can I send Bluetooth HCI commands directly to ESP32-WROOM-32D module through the serial port?
--------------------------------------------------------------------------------------------------------

  - Please refer to `controller_hci_uart_esp32 <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/hci/controller_hci_uart_esp32>`_.
  - When ESP32 is used as a controller, and the other device serves as a host, HCI commands can be sent to ESP32 via UART.
