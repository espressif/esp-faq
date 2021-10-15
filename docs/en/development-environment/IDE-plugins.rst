IDE plugins
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

How to add ESP32 development board on Arduino IDE?
-------------------------------------------------------------------

  - For installation instructions of arduino-esp32, please refer to `arduino-ide <https://github.com/espressif/arduino-esp32/blob/master/docs/arduino-ide/boards_manager.md>`_.
  - For instructions on how to add development boards on Arduino IDE, please refer to `arduino Cores <https://www.arduino.cc/en/Guide/Cores>`_.

----------------

When using the Arduino IDE development platform, how to read the MAC address of the Wi-Fi that comes with ESP32?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Please refer to the `"esp32-arduino development framework" <https://github.com/espressif/arduino-esp32>`_.
  - Use "WiFi.macAddress() " to obtain the MAC address of ESP32's Wi-Fi.
  - Please refer to example: `Serial.println(WiFi.macAddress()); <https://github.com/espressif/arduino-esp32/blob/a59eafbc9dfa3ce818c110f996eebf68d755be24/libraries/WiFi/examples/WiFiClientStaticIP/WiFiClientStaticIP.ino>`_.
  
