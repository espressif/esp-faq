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
------------------------------------------------------------------------------------------------------------------------------------------

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

  The default value is 120 s, defined by the ``MQTT_KEEPALIVE_TICK`` macro in ``mqtt_config.h``. This value can be modified via the ``session.keepalive`` parameter in ``esp_mqtt_client_config_t``.

----------------

Does MQTT support automatic reconnection?
------------------------------------------------

  - Yes. The automatic reconnection of MQTT is controlled by the member variable ``disable_auto_reconnect`` in `esp_mqtt_client_config_t <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/protocols/mqtt.html?highlight=esp_mqtt_client_config_t#_CPPv424esp_mqtt_client_config_t>`_. The default value of this variable is ``false``, which means automatic reconnection is enabled.
  - You can also modify the reconnection timeout by changing the ``network.reconnect_timeout_ms`` parameter in ``esp_mqtt_client_config_t``.

-----------------

What are the supported MQTT versions of ESP-IDF?
-----------------------------------------------------------------------------------------------------------

  ESP-IDF currently supports MQTT 3.1 and MQTT 3.1.1, and MQTT 5.0.

----------------

When a Wi-Fi connection is disconnected in ESP-IDF, will the memory previously requested by MQTT upper layer protocol be automatically released?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - No, but you do not need to care about this memory. What you need to care about is the application layer that ESP encapsulates.
  - For MQTT application layer components, you get an MQTT handle when initializing MQTT. You only need to care about the memory in this handle. When not using MQTT, you can call ``stop`` or ``destroy`` to release the corresponding MQTT memory. When Wi-Fi is disconnected and connected, you do not need to release the MQTT memory or reapply for the handle, because there is an automatic reconnection mechanism in the MQTT component.

----------------

For ESP32-C3 MQTT, can I not set corrresponding ``client_id`` but configure it as an empty string by default?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Yes. You can achieve this by setting the ``credentials.set_null_client_id`` parameter of ``esp_mqtt_client_config_t`` to ``true`` in the application code.

----------------

When ``MQTT_EVENT_PUBLISHED`` is triggered after an ESP-IDF MQTT client has published data with QoS of 1 or 2, does it mean that a proper ack has been received from the other side to prove that the publish has completed? Or does it just mean that the data was successfully sent to the server once?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The ``MQTT_EVENT_PUBLISHED`` event triggered means that the broker has acknowledged receipt of the messages published by the client, proving that the publish has completed successfully.

----------------

How does an ESP MQTT client manually release MQTT resources after disconnection?
-----------------------------------------------------------------------------------------------------------

  Calling the `esp_mqtt_client_destroy <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/protocols/mqtt.html#_CPPv423esp_mqtt_client_destroy24esp_mqtt_client_handle_t>`__ API will do the trick.

----------------

How should I configure the MQTT keepalive time when ESP32 Wi-Fi and Bluetooth LE coexist? Is there any appropriate configuration time?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - When using Wi-Fi and Bluetooth LE concurrently in ESP32, it is recommended to configure the MQTT keepalive time properly. Since both Wi-Fi and Bluetooth LE require system resources, setting the keepalive time too short may cause high system load, affecting system stability and performance.
  - Generally, it is advisable to set the MQTT keepalive time based on actual needs to ensure the device stays online while minimizing system resource consumption. In the case of Wi-Fi and Bluetooth LE coexistence, it is recommended to set the MQTT keepalive time to a longer duration, such as 30 seconds or 60 seconds, to reduce communication between the device and the MQTT broker, thereby reducing system load.
  - It is important to note that setting the keepalive time too long may cause a delay in detecting the device offline when it disconnects, which may affect real-time performance and reliability. Therefore, the MQTT keepalive time should be set based on actual needs and system performance.

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

  Yes. The ESP MQTT client controls whether to enable automatic reconnection by the ``network.disable_auto_reconnect`` parameter in the ``esp_mqtt_client_config_t`` structure. By default, this parameter is set to ``false``, indicating that MQTT will automatically attempt to reconnect.

----------------

How to check if the ESP32 is disconnected from the MQTT server?
-----------------------------------------------------------------------------------------------------------

  You can use the MQTT ``PING`` mechanism for detection. Specifically, in the ``esp_mqtt_client_config_t`` structure, set ``session.disable_keepalive`` to ``false`` (default value, which means the keepalive mechanism is enabled), and configure the ``session.keepalive`` parameter to 120 s (default value). In this way, the MQTT client will periodically send ``PING`` messages to check the connection status with the server.

----------------

How can I identify the specific error and troubleshoot the issue when encountering a connection failure to the MQTT server?
----------------------------------------------------------------------------------------------------------------------------------------------

  When MQTT connection fails, you can parse the data in the ``esp_mqtt_error_codes_t`` structure within the MQTT event ``MQTT_EVENT_ERROR``. For more details, please refer to the ``MQTT_EVENT_ERROR`` event in the example.

----------------

How to adjust the sending time of MQTT's will message?
-----------------------------------------------------------------------------------------------------------

  The delay in sending will messages can be reduced by shortening the MQTT heartbeat time.

----------------

While sending data, the MQTT client encounters a timeout. How to determine which network layer the problem occurred in?
---------------------------------------------------------------------------------------------------------------------------

  Issues can be identified by packet capture analysis to determine whether they occur at the transport layer, network layer, or data link layer. The specific failure point could be that the server did not return an ACK, the server returned an ACK but Wi-Fi did not receive it, or the data packet was not successfully sent.

----------------

Why does the MQTT client still report a write timeout when the network condition is good?
-----------------------------------------------------------------------------------------------------------

  This may be due to the underlying LWIP buffer being full, resulting in an inability to write. This is usually because the packets in the buffer have not received an ACK from the other end. Specific reasons may include the server not sending an ACK, the server sending an ACK but Wi-Fi not receiving it, or the data packet not being successfully sent out.

----------------

Why does memory usage drop sharply when using MQTT communication?
-----------------------------------------------------------------------------------------------------------

  The outbox in MQTT will occupy memory. For messages with QoS greater than 0, the related memory will only be released after the ACK from the MQTT layer is sent by the peer. You can track the allocation and release of memory by configuring CONFIG_HEAP_USE_HOOKS.

----------------

How to set the session expiry interval for MQTT?
-----------------------------------------------------------------------------------------------------------

  This feature is only available for MQTT5 protocol, which can be set through ``session_expiry_interval`` in ``esp_mqtt5_disconnect_property_config_t``.

----------------

Is the reconnection operation effective after MQTT disconnects? Does it need optimization?
-----------------------------------------------------------------------------------------------------------

  MQTT will automatically reconnect by default, so the application layer does not need to manually disconnect and then reconnect.

----------------

What is the cause of the "mqtt_client: No PING_RESP, disconnected" error?
-----------------------------------------------------------------------------------------------------------

  This error usually occurs because the MQTT heartbeat response from the peer was not received within the specified time. It is recommended to use packet capture and log comparison to analyze whether the issue is related to the server or WiFi packet transmission.

----------------

Why does the TCP receive window decrease by 2 bytes each time when MQTT connection only has heartbeat packets?
---------------------------------------------------------------------------------------------------------------------

  This may be because the data is stuck in the underlying receive buffer, causing the receive window to decrease gradually. To avoid this situation, ensure that the application calls the ``read`` function correctly to handle the MQTT ping response.

----------------

ESP32 acting as an AP connects to two ESP Stations, both of which have established MQTT connections. Can the AP monitor the MQTT messages?
---------------------------------------------------------------------------------------------------------------------------------------------------------

  No, ESP32 acting as an AP is only responsible for routing and forwarding. Since the destination address of the packets sent by the Stations is not the AP itself, the AP only forwards the packet upon receipt and does not listen to or process the messages.

----------------

Why does the MQTT connection fail with error ``MQTT_CONNECTION_REFUSE_NOT_AUTHORIZED``?
-----------------------------------------------------------------------------------------------------------

  This error typically indicates that the username or password is incorrect. Please check and ensure that you provide the correct ``username`` and ``password``.

----------------

How to ensure that MQTT devices can still receive messages published during offline periods after going offline?
--------------------------------------------------------------------------------------------------------------------

  Configure the MQTT connection parameters as follows:

  - Set ``session.disable_clean_session`` to ``true`` in ``esp_mqtt_client_config_t`` to ensure that the device can still receive QoS 1 or QoS 2 messages after reconnecting.
  - When publishing messages using ``esp_mqtt_client_publish``, set ``retain`` to ``true`` so the server retains the message. This allows the device to retrieve the message again after waking up.

----------------

Will the MQTT broker send a Last Will message if the client disconnects unexpectedly?
-------------------------------------------------------------------------------------------------------------------------------------------------------------

  If the client disconnects without sending an MQTT DISCONNECT message and the keepalive interval is short, the broker may assume the client is offline and trigger the Last Will message. It is recommended to explicitly call the disconnect API and set an appropriate keepalive interval.

----------------

During MQTT5 operation, frequent Wi-Fi network switching causes repeated re-subscriptions. As a result, ``MQTT5 publish check fail`` messages flood the log and the connection cannot recover. What is the reason, and how can this be resolved?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  MQTT5 provides a flow control mechanism that allows the server to limit the client’s message publishing rate. The number of messages that a client can send simultaneously is determined by the server. When the PUBLISH messages sent by the client have not yet received PUBACK confirmation from the server, and the total number reaches the limit set by the server, the client must wait for the server to acknowledge one packet before it can send another. If the device is restricted by flow control, it must wait for the PUBACK acknowledgment before continuing to publish; otherwise, message sending will fail.
