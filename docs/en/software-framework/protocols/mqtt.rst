MQTT
====

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

How to configure the server address so as to make it an autonomic cloud platform by using MQTT?
-----------------------------------------------------------------------------------------------------------------------------------------

  Please refer to `MQTT Examples <https://github.com/espressif/esp-idf/tree/master/examples/protocols/mqtt>`_.

--------------

I'm using ESP8266 release/v3.3 version of SDK to test the example/protocols/esp-mqtt/tcp example. Then during Wi-Fi configuration, the connection fails after configuring SSID, password and connecting to the default server. The log is as follows, what is the reason?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    W (4211) MQTT_CLIENT: Connection refused, not authorized
    I (4217) MQTT_CLIENT: Error MQTT Connected
    I (4222) MQTT_CLIENT: Reconnect after 10000 ms
    I (4228) MQTT_EXAMPLE: MQTT_EVENT_DISCONNECTED
    I (19361) MQTT_CLIENT: Sending MQTT CONNECT message, type: 1, id: 0000

  When such error occurs,  it indicates that the server rejected the connection because the client's wrong MQTT username and password caused the server-side authentication to fail. Please check if you are using the correct MQTT username and password.

-----------------

What is the default keepalive value of the MQTT component in ESP-IDF?
---------------------------------------------------------------------------------------

  The default value is 120 s, which is defined by ``MQTT_KEEPALIVE_TICK`` in file ``mqtt_config.h``.
  
----------------

Does MQTT support automatic reconnection?
------------------------------------------------

  - The automatic reconnection of MQTT is controlled by the ``disable_auto_reconnect`` variable of struct `esp_mqtt_client_config_t <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/protocols/mqtt.html#_CPPv424esp_mqtt_client_config_t>`_. The default value of ``disable_auto_reconnect`` is ``false``, which means that automatic reconnection is enabled.
  - The reconnection timeout value can be set using ``reconnect_timeout_ms``.

-----------------

What are the supported MQTT versions of ESP-IDF?
-----------------------------------------------------------------------------------------------------------

  ESP-IDF currently supports the MQTT versions MQTT 3.1 and MQTT 3.1.1.

----------------

When a Wi-Fi connection is disconnected in ESP-IDF, will the memory previously requested by MQTT upper layer protocol be automatically released?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - No, but you do not need to care about this memory. What you need to care about is the application layer that ESP encapsulates.
  - For MQTT application layer components, you get an MQTT handle when initializing MQTT. You only need to care about the memory in this handle. When not using MQTT, you can call ``stop`` or ``destroy`` to release the corresponding MQTT memory. When Wi-Fi is disconnected and connected, you do not need to release the MQTT memory or reapply for the handle, because there is an automatic reconnection mechanism in the MQTT component.

----------------

For ESP32-C3 MQTT, is ``client_id`` configured as an empty string by default when not set? 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - No, the application code will configure the ``client_id`` as ESP32_XXX by default if it is not set. So, the code does not support null ``client_id`` for now.
  - We have plans to add the function to configure ``client_id`` as an empty string by default, so stay tuned.

----------------

When ``MQTT_EVENT_PUBLISHED`` is triggered after an ESP-IDF MQTT client has published data with QoS of 1 or 2, does it mean that a proper ack has been received from the other side to prove that the publish has completed? Or does it just mean that the data was successfully sent to the server once?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The ``MQTT_EVENT_PUBLISHED`` event triggered means that the broker has acknowledged receipt of the messages published by the client, proving that the publish has completed successfully.

----------------

How does an ESP MQTT client manually release MQTT resources after disconnection?
-----------------------------------------------------------------------------------------------------------

  Calling the ``esp_mqtt_client_destroy`` API will do the trick.

----------------

How should I configure the MQTT keepalive time when ESP32 Wi-Fi and Bluetooth LE coexist? Is there any appropriate configuration time?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

  No special consideration is needed for this case, as long as it is not too small, e.g. 30 s, 60 s, etc.

----------------

When will the disconnect event message be triggered for ESP-MQTT clients?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The disconnect message only occurs in the follow cases:

  - A TCP connection error occurs while the MQTT connection is being established.
  - An MQTT connection error occurs while the MQTT connection is being established.
  - You actively call the ``disconnect`` function.
  - An exception is received or sent.
  - The MQTT ``PING RESPONSE`` is not received within the specified time.
  - The MQTT ``PING`` request failed to be sent.
  - Reconnection.

----------------

Does the ESP32 MQTT client automatically try to reconnect after disconnecting from the server?
-----------------------------------------------------------------------------------------------------------

  The ``esp_mqtt_client_config_t`` structure in the ESP-MQTT client has the ``disable_auto_reconnect`` parameter, which can be configured as ``true`` or ``false`` to determine to reconnect or not. By default, it will reconnect.

----------------

How to check if the ESP32 is disconnected from the MQTT server?
-----------------------------------------------------------------------------------------------------------

  To detect if the ESP32 has been disconnected from the server, you can use MQTT's ``PING`` mechanism by configuring the keepalive parameters ``disable_keepalive`` and ``keepalive`` in the ``esp_mqtt_client_config_t`` structure in ESP-MQTT. For example, if you configure ``disable_keepalive`` to false (default setting) and ``keepalive`` to 120 s (default setting), the MQTT client will periodically send ``PING`` to check if the connection to the server is working.
