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

When Wi-Fi coexists with ESP-BLE-MESH, what mode does it support?
------------------------------------------------------------------------

  For now, only Wi-Fi STA mode supports coexistence.
 
--------------

When Wi-Fi coexists with ESP-BLE-MESH, the Wi-Fi throughput is low, why?
-----------------------------------------------------------------------------------------

  For ESP32-DevKitC boards without PSRAM, Wi-Fi can coexist with ESP-BLE-MESH but with a relatively low throughput. For ESP32-DevKitC boards with PSRAM, the transmit rate can stabilize at over 1 Mbps.

  To support PSRAM, the following configurations in menuconfig should be enabled accordingly:

  - ``ESP32-specific --> Support for external,SPI-connected RAM --> Try to allocate memories of Wi-Fi and LWIP...``
  - ``Bluetooth --> Bluedriod Enable --> BT/BLE will first malloc the memory from the PSRAM``
  - ``Bluetooth --> Bluedriod Enable --> Use dynamic memory allocation in BT/BLE stack.``
  - ``Bluetooth --> Blutooth controller --> BLE full scan feature supported.``
  - ``Wi-Fi --> Software controls Wi-Fi/Bluetooth coexistence --> Wi-Fi``

--------------

Does ESP32 support coexistence between 16 MB External Flash and 8 MB External PSRAM?
-------------------------------------------------------------------------------------------------

  Yes, ESP32 supports coexistence between 16 MB External Flash and 8 MB External PSRAM.

--------------

Does ESP32 support coexistence between ESP-WIFI-MESH and Bluetooth® LE Mesh?
---------------------------------------------------------------------------------------

  No.

  However, the ESP32 supports coexistence between ESP-WIFI-MESH and Bluetooth LE, or Wi-Fi STA and Bluetooth LE Mesh.

--------------

Does ESP32 support coexistence between Bluetooth® and Wi-Fi?
---------------------------------------------------------------------

  Yes, but time-sharing control is required for ESP32's coexistence between Wi-Fi and Bluetooth. Please go to menuconfig to enable the Wi-Fi/Bluetooth coexistence, shown as follows:
  
  ``menuconfig -> Component config -> Wi-Fi -> Software controls WiFi/Bluetooth coexistence (Enable)``

--------------

When Bluetooth® LE and A2DP coexist, audio data reception is lost and lagged while entering Bluetooth LE scanning. How to resolve such issue?
--------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Reduce the duty cycle of Bluetooth LE scanning
  - Use RingBuf to cache audio data

--------------

Does ESP32 support coexistence between the network port (LAN8720) and Wi-Fi (Wifi-AP)?
-------------------------------------------------------------------------------------------------------

  Yes, this can be achieved by writing the detection events of both connections as one.

---------------

Can BLE adverting (Connectable) and iBeacon sending (advertising) be coexisted?
--------------------------------------------------------------------------------------------------

  :release/v4.0 and above| CHIP: ESP32:

  - Not supported yet on hardware level, but can be realized on application layer by polling and sending broadcast packets at regular intervals.
