共存
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

Wi-Fi 和 ESP-BLE-MESH 共存时，支持哪些模式？
--------------------------------------------

  目前，只有 Wi-Fi STA 模式支持共存。

--------------

Wi-Fi 和 ESP-BLE-MESH 共存时，为什么 Wi-Fi 吞吐量很低？
-------------------------------------------------------

  未搭载 PSRAM 的 ESP32-DevKitC 开发板，Wi-Fi 和 ESP-BLE-MESH 共存可以正常运行，但是吞吐率较低。当 Wi-Fi 和 ESP-BLE-MESH 共存时，搭载 PSRAM 的 ESP32-DevKitC 速率可以稳定在 1 Mbps 以上。

  应使能 menuconfig 中的一些配置来支持 PSRAM:

  - ``ESP32-specific --> Support for external,SPI-connected RAM --> Try to allocate memories of Wi-Fi and LWIP...``
  - ``Bluetooth --> Bluedriod Enable --> BT/BLE will first malloc the memory from the PSRAM``
  - ``Bluetooth --> Bluedriod Enable --> Use dynamic memory allocation in BT/BLE stack.``
  - ``Bluetooth --> Blutooth controller --> BLE full scan feature supported.``
  - ``Wi-Fi --> Software controls Wi-Fi/Bluetooth coexistence --> Wi-Fi``

--------------

ESP32 支持 16MB 的 External Flash 和 8MB 的 External PSRAM 共存吗？
----------------------------------------------------------------------------------

  - ESP32 可以支持 16MB 的 External Flash 和 8MB 的 External PSRAM 共存使用。

--------------

ESP32 Wi-Fi Mesh 和 BLE Mesh 可以同时支持吗？
------------------------------------------------------------

  - 不支持，补充一点：ESP32 Wi-Fi Mesh 和 BLE 可以同时支持，或者 ESP32 Wi-Fi STA 模式和 BLE Mesh 可以同时支持。

--------------

ESP32 蓝牙和 WI-FI 能否同时使用？
----------------------------------------

  - ESP32 的 Wi-Fi 和蓝牙可共存，但需要分时控制，可在 menuconfig 中使能 Wi-Fi 和蓝牙共存设置。如下：
  - ``menuconfig -> Component config -> Wi-Fi -> Software controls WiFi/Bluetooth coexistence （Enable）``
