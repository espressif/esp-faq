coexistence
===========

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

When Wi-Fi coexists with Bluetooth, what mode does it support?
------------------------------------------------------------------------

  For supported coexistence scenarios, please refer to `coexistence documentation <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/coexist.html>`_.

--------------

When Wi-Fi coexists with ESP-BLE-MESH, the Wi-Fi throughput is low, why?
------------------------------------------------------------------------------------------

  For ESP32-DevKitC boards without PSRAM, Wi-Fi can coexist with ESP-BLE-MESH but with a relatively low throughput. For ESP32-DevKitC boards with PSRAM, the transmit rate can stabilize at over 1 Mbps.

  To support PSRAM, the following configurations in menuconfig should be enabled accordingly:

  - ``ESP32-specific --> Support for external,SPI-connected RAM --> Try to allocate memories of Wi-Fi and LWIP...``
  - ``Bluetooth --> Bluedriod Enable --> BT/BLE will first malloc the memory from the PSRAM``
  - ``Bluetooth --> Bluedriod Enable --> Use dynamic memory allocation in BT/BLE stack.``
  - ``Bluetooth --> Blutooth controller --> BLE full scan feature supported.``
  - ``Wi-Fi --> Software controls Wi-Fi/Bluetooth coexistence --> Wi-Fi``

--------------

Does ESP32 support coexistence between ESP-WIFI-MESH and Bluetooth® LE Mesh?
---------------------------------------------------------------------------------------

  No.

  However, the ESP32 supports coexistence between ESP-WIFI-MESH and Bluetooth LE, or Wi-Fi STA and Bluetooth LE Mesh.

--------------

Does ESP32 support coexistence between Bluetooth® and Wi-Fi?
---------------------------------------------------------------------

  Yes, but time-sharing control is required for ESP32's coexistence between Wi-Fi and Bluetooth. Please go to menuconfig to enable the Wi-Fi/Bluetooth coexistence, shown as follows:

  :IDF\: release/v5.0:

  ``menuconfig -> Component config -> Wi-Fi -> Software controls WiFi/Bluetooth coexistence (Enable)``

  :IDF\: release/v5.1 and later versions:

  ``menuconfig -> Component config -> Wireless Coexistence -> Software controls WiFi/Bluetooth coexistence (Enable)``

--------------

When Wi-Fi, Bluetooth® LE, and A2DP sink coexist, audio data reception is lost and lagged while entering Bluetooth LE scanning. How to resolve such issue?
--------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Use RingBuf to cache audio data
  - Pause music and add a tone, such as "scanning for devices".

--------------

Can BLE advertising (Connectable) and iBeacon sending (advertising) coexist?
--------------------------------------------------------------------------------------------------

  :IDF\: release/v4.0 and later versions | CHIP: ESP32:

  - Not supported yet on hardware level, but can be realized on application layer by polling and sending broadcast packets at regular intervals.

  :IDF\: release/v4.3 and later versions | CHIP\: ESP32-C3|ESP32-S3:

  - Yes.

--------------

How do ESP32 Bluetooth® and Bluetooth® LE dual-mode coexist and how can I use this coexistence mode?
---------------------------------------------------------------------------------------------------------------------------------------

  The ESP32 Bluetooth and Bluetooth LE dual-mode does not require complex configurations. For developers, it is simple as calling Bluetooth LE API for Bluetooth LE, and calling Classic Bluetooth API for Classic Bluetooth.

  For Classic Bluetooth and Bluetooth LE coexistence, please refer to `a2dp_gatts_coex example <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/coex/a2dp_gatts_coex>`_.

--------------

How do ESP32 Bluetooth® and Wi-Fi coexist?
----------------------------------------------------

  In the ``menuconfig``, there is a special option called ``Software controls WiFi/Bluetooth coexistence``, which is used to control the coexistence of Bluetooth and Wi-Fi for ESP32 using software, thus balancing the coexistence requirement for controlling the RF module by both the Wi-Fi and Bluetooth modules.

  - Please note that if ``Software controls WiFi/Bluetooth coexistence`` is enabled, the Bluetooth LE scan interval shall not exceed ``0x100 slots`` (about 160 ms). If the Bluetooth LE and Wi-Fi coexistence is required, this option can be enabled or disabled. However, if this option is not enabled, please note that the Bluetooth LE scan window should be larger than 150 ms, and the Bluetooth LE scan interval should be less than 500 ms.
  - If the Classic Bluetooth and Wi-Fi coexistence is required, it is recommended to enable this option.

---------------

How can I resolve the frequently occurred ELxXX error (such as ELx200) when Wi-Fi and Ble co-exit？
-----------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32:

  - It has been fixed in commit 386a8e37f19fecc9ef62e72441e6e1272fa985b9. Please switch to the corresponding commit to test.
