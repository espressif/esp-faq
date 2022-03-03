Third party cloud service
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


Are there any demo references for OTA upgrading?
---------------------------------------------------

  - For ESP8266, please refer to `ESP8266 OTA <https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/system/ota>`_.
  - For ESP32 and ESP32-S2, please refer to `ESP32 and ESP32-S2 OTA <https://github.com/espressif/esp-idf/tree/master/examples/system/ota>`_.

--------------

Does ESP Azure library support Azure IoT Central? Is there a demo?
------------------------------------------------------------------------------------------------------

  - ESP Azure already supports Azure IoT Central. But there is no relevant example on the master.
  - The PnP example on the ESP Azure's preview/pnp_example branch will report some actual data  from sensors, you can refer to the operation of Azure IoT Central for the data management.

--------------

What should I do to connect ESP32 to Alibaba Cloud via ESP32 + Ethernet + MQTT?
--------------------------------------------------------------------------------------------------------------------------------
  
  - Use `esp-aliyun <https://github.com/espressif/esp-aliyun>`_ but replace the Wi-Fi initialization code with Ethernet initialization. You can refer to the Ethernet example under `ESP_IDF <https://github.com/espressif/esp-idf/tree/master/examples/ethernet>`_.

----------------------------------------------------------------------------------------------------------------------------------------------------------------

what do Alexa LED states indicate?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - You can refer to `Alexa LEDs <https://developer.amazon.com/en-US/docs/alexa/alexa-voice-service/ux-design-attention.html#LEDs>`_.
