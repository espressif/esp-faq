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
-----------------------------------------------------------------------------------------------------------

  - 目前的 ESP-Touch 协议下发送的数据内容都是固定的，不支持自定义数据。
  - 如果需要发送自定义数据的话，建议使用 BluFi，这是基于 Bluetooth LE 的配网协议。请参见：

    - Android APP：https://github.com/EspressifApp/EspBlufiForAndroid。
    - iOS APP：https://github.com/EspressifApp/EspBlufiForiOS。