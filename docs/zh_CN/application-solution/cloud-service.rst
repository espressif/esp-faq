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

  ESP32 对接天猫精灵可以使用 esp-aliyun SDK，相关文档可以 `参阅 <https://github.com/espressif/esp-aliyun>`_。

--------------

esp-aliyun 与 esp-ali-smartliving 的区别 ？
-------------------------------------------

  - esp-aliyun 对接的是 “物联网平台”
  - esp-ali-smartliving 对接 “生活物联网平台”
  - 阿里以将两个平台在云端互通，所使用上功能相似度较高,并可相互替代。
  - 两者区别可以参见 `生活物联网平台与物联网平台的区别 <https://help.aliyun.com/document_detail/124922.html?spm=5176.10695662.1996646101.searchclickresult.6a782cfeLpWe7Z>`_。

--------------

使用乐鑫的产品连接乐鑫云平台，遇到问题如何提问与反馈？
--------------------------------------------------------------

  - 如果您使用的乐鑫云平台是 rainmaker ，建议您直接将问题在 Github 上反馈，会有专业人员尽快为您解答。
  - 如果是其他云平台，您可以将使用的云平台信息，以及您的问题汇总起来，发送到 sales@espressif.com 。

--------------

ESPESP8266 可以连接 Alex 或者 Google home 吗？
----------------------------------------------------

  - Alex 可以参考 `aws_iot <https://github.com/espressif/ESP8266_RTOS_SDK/tree/release/v3.3/examples/protocols/aws_iot>`_, 做一些 Alex 配置即可。
  - Google home 当前没有示例，可以参考 ESP32 参考示例 `esp-google-iot <https://github.com/espressif/esp-google-iot>`_。

-----------------------

ESP Azure 库支持 Azure IoT Central 吗？有没有 Demo？
-------------------------------------------------------------------------------------------------------------

  - ESP Azure 已经支持 Azure IoT Central。但是 master 上还没有相关示例。
  - ESP Azure preview/pnp_example 分支上的 PnP 示例会上报些真实的传感器数据，可以参考其中 Azure IoT Central 对这些数据的管理。

-----------------------

ESP32 + 以太网 + MQTT 方式接入阿里云，应该怎么做？
-------------------------------------------------------------------------------------------------------------
  
  - 使用 `esp-aliyun <https://github.com/espressif/esp-aliyun>`_，将 Wi-Fi 初始化代码替换为 Ethernet 初始化即可。可以参考 `ESP_IDF 下的 Ethernet 示例 <https://github.com/espressif/esp-idf/tree/master/examples/ethernet>`_。
