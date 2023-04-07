配置
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

----------------

安卓 ESP-Touch 可以添加自己想要广播的数据吗（如添加设备 ID，希望 ESP32 能接收到这个 ID）？
------------------------------------------------------------------------------------------------------------

  - ESP-Touch 是一个用于在手机和 ESP8266/ESP32 之间建立 Wi-Fi 连接的通信协议，它使用一种特殊的广播方式来传输 Wi-Fi SSID 和密码信息。通常情况下，ESP-Touch 广播的数据是固定格式的，不能直接添加自定义数据。
  - 如果您希望 ESP32 能够接收到设备 ID 等自定义数据，您可以考虑使用其他通信协议，例如 MQTT、HTTP 等。使用这些协议，您可以自由地定义数据格式，并在 Android 应用程序和 ESP32 之间进行通信。
  - 如果您仍然希望广播自定义数据，建议使用 BluFi，这是基于 Bluetooth LE 的配网协议。请参见：

    - Android APP：https://github.com/EspressifApp/EspBlufiForAndroid。
    - iOS APP：https://github.com/EspressifApp/EspBlufiForiOS。
