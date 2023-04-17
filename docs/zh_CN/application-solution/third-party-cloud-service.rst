第三方云服务
===============

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

OTA 升级有没有相关示例参考？
-------------------------------

  请参考如下链接：

  - `ESP8266 OTA <https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/system/ota>`_
  - `ESP32 系列 OTA <https://github.com/espressif/esp-idf/tree/master/examples/system/ota>`_

--------------

ESP32 如何对接天猫精灵，是否有相应的资料？
------------------------------------------

  ESP32 对接天猫精灵可以使用 esp-aliyun SDK，可以参阅 `ESP 设备对接阿里云指南 <https://github.com/espressif/esp-aliyun>`_。

--------------

esp-aliyun 与 esp-ali-smartliving 的区别 ？
-------------------------------------------

  - esp-aliyun 对接的是 “物联网平台”。
  - esp-ali-smartliving 对接 “生活物联网平台”。
  - 阿里云将两个平台在云端互通，使用功能上相似度较高，并可相互替代。
  - 两者区别可以参见 `生活物联网平台与物联网平台的区别 <https://help.aliyun.com/document_detail/124922.html?spm=5176.10695662.1996646101.searchclickresult.6a782cfeLpWe7Z>`_。

--------------

使用乐鑫的产品连接乐鑫云平台，遇到问题如何提问与反馈？
--------------------------------------------------------------

  - 如果您使用的乐鑫云平台是 ESP RainMaker，建议您直接将问题反馈至 `Github <https://github.com/espressif/esp-rainmaker/issues>`_。
  - 如果是其他云平台，您可以将使用的云平台信息以及您的问题汇总，发送到 sales@espressif.com。

--------------

ESP32 与 ESP8266 可以连接 Alexa 或者 Google home 吗？
---------------------------------------------------------

  - Alexa 可以参考 `aws_iot <https://github.com/espressif/ESP8266_RTOS_SDK/tree/release/v3.3/examples/protocols/aws_iot>`_，做一些 Alexa 配置即可。
  - Google home 当前没有示例，可以参考 ESP32 参考示例 `esp-google-iot <https://github.com/espressif/esp-google-iot>`_。

--------------

ESP32 + 以太网 + MQTT 方式接入阿里云，应该怎么做？
-------------------------------------------------------------------------------------------------------------
  
  - 使用 `esp-aliyun <https://github.com/espressif/esp-aliyun>`_，将 Wi-Fi 初始化代码替换为 Ethernet 初始化即可。可以参考 ESP_IDF 下的 `Ethernet 示例 <https://github.com/espressif/esp-idf/tree/master/examples/ethernet>`_。

