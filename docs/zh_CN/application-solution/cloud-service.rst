云服务
======

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

OTA 升级有没有相关 demo 参考？
------------------------------

  请参考如下链接：

  - `ESP8266 OTA <https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/system/ota>`_
  - `ESP32 及 ESP32-S2 OTA <https://github.com/espressif/esp-idf/tree/master/examples/system/ota>`_

--------------

ESP8266 NONOS SDK OTA 为何云端需要 “user1.bin” 和 “user2.bin” 两个 bin 文件？
-----------------------------------------------------------------------------

 ESP8266 Cache 偏移仅支持 1MB 的单位偏移。

  - 当分区设置为 512+512 模式时，user1.bin 与 user2.bin 指令地址并不相同，不可以相互替换；所以，同一版本需要云端放置两个不同版本的固件用于设备升级。
  - 当分区设置为 1024+1024 模式时，分区大小满足 Cache 偏移，不受该限制。

--------------

ESP RainMaker 方案中数据是通过乐鑫云中转数据吗？设备直接连接到 AWS, Google 或者 Homekit 吗？
--------------------------------------------------------------------------------------------

  - 在 ESP RainMaker 方案中，设备直接连接到 AWS IOT，ESP RainMaker 服务托管在 AWS 上。
  - 对于 Alexa 和 Google Voice Assistant 而言，采用云对云的集成方案。以 Alexa 为例，数据流如下：Alexa device (Echo speaker) -> Alexa Cloud -> RainMaker Cloud -> Device。
  - HomeKit 是完全独立的， 当前没有集成到 ESP RainMaker。

--------------

ESP32 如何对接天猫精灵，是否有相应的资料？
------------------------------------------

  ESP32 对接天猫精灵可以使用 esp-aliyun SDK，相关文档可以\ `参阅 <https://github.com/espressif/esp-aliyun>`__\ 。

--------------

esp-aliyun 与 esp-ali-smartliving 的区别 ？
-------------------------------------------

  - esp-aliyun 对接的是 “物联网平台”
  - esp-ali-smartliving 对接 “生活物联网平台”
  - 阿里以将两个平台在云端互通，所使用上功能相似度较高,并可相互替代。
  - 两者区别可以参见 `生活物联网平台与物联网平台的区别 <https://help.aliyun.com/document_detail/124922.html?spm=5176.10695662.1996646101.searchclickresult.6a782cfeLpWe7Z>`__
