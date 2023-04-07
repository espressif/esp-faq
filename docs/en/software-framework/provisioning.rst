Provisioning
============

:link_to_translation:`zh_CN:[中文]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

-----------------------

Can I add any broadcast data I want to Android ESP-Touch (e.g., add a device ID so that ESP32 can receive this ID)?
-------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP-Touch is a communication protocol used to establish a Wi-Fi connection between a mobile phone and ESP8266/ESP32. It uses a special broadcast method to transmit Wi-Fi SSID and password. Typically, the data broadcasted by ESP-Touch should be in a fixed format and cannot include customized data.
  - If you want ESP32 to receive customized data such as device ID, you can consider using other communication protocols such as MQTT or HTTP. With these protocols, you can define data formats as you wish and communicate between an Android App and ESP32.
  - If you still want to broadcast customized data, you can use BluFi, which is the networking protocol based on Bluetooth LE. Please refer to the following references for BluFi:

    - Android APP：https://github.com/EspressifApp/EspBlufiForAndroid.
    - iOS APP：https://github.com/EspressifApp/EspBlufiForiOS.
