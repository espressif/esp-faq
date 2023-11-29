Third-Party Cloud Service
=============================

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

Are there any examples for OTA upgrading?
----------------------------------------------------

  Please refer to the following links:

  - For ESP8266, please refer to `ESP8266 OTA <https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/system/ota>`_.
  - For ESP32 series, please refer to `ESP32 series OTA <https://github.com/espressif/esp-idf/tree/master/examples/system/ota>`_.

--------------

How to integrate ESP32 with Tmall Genie? Any reference materials?
--------------------------------------------------------------------------------

  You can integrate ESP32 with Tmall Genie using the ``esp-aliyun`` SDK with reference to `Guide for Integrating ESP Devices with Alibaba Cloud <https://github.com/espressif/esp-aliyun>`_.

--------------

What is the difference between ``esp-aliyun`` and ``esp-ali-smartliving``?
----------------------------------------------------------------------------

  - ``esp-aliyun`` is used for integration with "Internet of Things Platform".
  - ``esp-ali-smartliving`` is used for integration with "Smart Living IoT Platform".
  - Alibaba Cloud ensures the two platforms are interconnected in the cloud. They are functionally similar and can be used interchangeably.
  - For the differences between the two, please refer to `The differences between the Smart Living IoT Platform and the IoT Platform <https://help.aliyun.com/document_detail/124922.html?spm=5176.10695662.1996646101.searchclickresult.6a782cfeLpWe7Z>`_.

--------------

How to ask questions and provide feedback when encountering issues in connecting Espressif products to the Espressif cloud platform?
------------------------------------------------------------------------------------------------------------------------------------------------

  - For ESP RainMaker, the cloud platform developed by Espressif, submit feedback to `GitHub <https://github.com/espressif/esp-rainmaker/issues>`_.
  - For other cloud platforms, please send the information about the specific platform along with your issues to sales@espressif.com.

--------------

Can ESP32 and ESP8266 connect to Alexa or Google Home?
---------------------------------------------------------

  - Yes. For how to connect to Alexa, refer to the `aws_iot <https://github.com/espressif/ESP8266_RTOS_SDK/tree/release/v3.3/examples/protocols/aws_iot>`_ example and make some configuration.
  - There are currently no examples for Google Home, but you can refer to the ESP32 application example in `esp-google-iot <https://github.com/espressif/esp-google-iot>`_.

--------------

What should I do to connect ESP32 to Alibaba Cloud via Ethernet and MQTT?
--------------------------------------------------------------------------------------------------------------------------------

  Use `esp-aliyun <https://github.com/espressif/esp-aliyun>`_ but replace the Wi-Fi initialization code with Ethernet initialization. You can refer to the Ethernet examples under `ESP-IDF <https://github.com/espressif/esp-idf/tree/master/examples/ethernet>`_.
