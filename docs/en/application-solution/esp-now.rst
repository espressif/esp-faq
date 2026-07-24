ESP-NOW
=======

:link_to_translation:`zh_CN:[中文]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

-----------------

What is the one-to-one bit rate for ESP32 in ESP-NOW mode?
---------------------------------------------------------------------

  Test result:

  - Test board: `ESP32-DevKitC V4 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/esp32/get-started-devkitc.html>`__.
  - Wi-Fi mode: station.
  - PHY rate is 1 Mbps by default.
  - Around 214 Kbps in an open environment.
  - Around 555 Kbps in a shielding box.
  - If you require a higher rate, configure the TX rate. For details, see :ref:`How do I set the rate at which ESP-NOW data is sent? <esp-now-set-tx-rate>`.

--------------

What is ESP-NOW? What are its advantages and application scenarios?
--------------------------------------------------------------------------

  - `ESP-NOW <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_now.html>`_ is a connectionless communication protocol defined by Espressif.
  - In ESP-NOW, application data is encapsulated in action frames from different vendors and then transmitted from one Wi-Fi device to another without a connection.
  - ESP-NOW is ideal for smart lights, remote control devices, sensors, and other applications.

--------------

Can Wi-Fi be used with ESP-NOW at the same time?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes, but it should be noted that the channel of ESP-NOW must be the same as that of the connected AP.

--------------------

.. _esp-now-set-tx-rate:

How do I set the rate at which ESP-NOW data is sent?
--------------------------------------------------------------------------------------------------------------------------------------------

  It is recommended to use `esp_now_set_peer_rate_config() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_now.html#config-esp-now-rate>`__ to configure the TX rate per peer. This API supports all rates, including Wi-Fi 6 HE rates. Call it after ``esp_wifi_start()``, ``esp_now_init()``, and after adding the peer with ``esp_now_add_peer()``.

  .. note::

     - Before ESP-IDF v5.2: use the legacy API ``esp_wifi_config_espnow_rate()`` (for example ``esp_wifi_config_espnow_rate(WIFI_IF_STA, WIFI_PHY_RATE_MCS0_LGI)``; non-HE rates only).
     - ESP-IDF v5.2 to v5.x: ``esp_now_set_peer_rate_config()`` is available. Both APIs can be used (the legacy API is marked as deprecated). Migration is optional.
     - ESP-IDF v6.0 and later: ``esp_wifi_config_espnow_rate()`` has been removed. You must use ``esp_now_set_peer_rate_config()``.

-----------------

ESP-NOW allows pairing with a maximum of 20 devices. Is there a way to control more devices?
---------------------------------------------------------------------------------------------------------------------------------------------------------

  You can use broadcast packets and provide the destination addresses in the payload. The number of addresses would then not be affected by the limited number. You only need to configure the correct broadcast address.

-----------------

.. _esp-now-max-control-devices:

What is the maximum number of devices that can be controlled by ESP-NOW?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The following limits apply to the ESP-IDF protocol layer (``esp_now``) and depend on the communication method:

  - If unicast packets are used, up to 20 devices can be paired and controlled at the same time (``ESP_NOW_MAX_TOTAL_PEER_NUM``).
  - If ESP-NOW encrypted mode is used, the maximum number of encrypted devices depends on the ESP-IDF version:

    - Before ESP-IDF v5.1: fixed at 6 and not configurable.
    - ESP-IDF v5.1 and later: configurable; default 7, maximum 17 (for ESP32-C2: default 2, maximum 4). Change it with ``CONFIG_ESP_WIFI_ESPNOW_MAX_ENCRYPT_NUM`` in the Wi-Fi menuconfig.

  - If broadcast packets are used, theoretically there is no limitation on the number of devices that can be controlled. You only need to configure the correct broadcast address and take care of interference when there are too many devices.

  If you use the `esp-now component <https://github.com/espressif/esp-now>`__ (application-level wrapper): control uses a broadcast + group + bindlist model. Control commands are sent as broadcast, so the number of controlled devices is not limited by the protocol-layer limit of 20 peers (the practical limit still depends on factors such as broadcast interference). The component uses application-layer encryption and is also not limited by the protocol-layer encrypted-peer limit (6/17).

-----------------

Do I need to connect a router for communication between ESP-NOW devices?
---------------------------------------------------------------------------------------------------------

  ESP-NOW interacts directly from device to device and does not require a router to forward data.

-----------------

What is the maximum data length of a single ESP-NOW packet? Can it be modified?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The following limits apply to the ESP-IDF protocol layer (``esp_now``). ESP-NOW currently has two versions with different maximum payload lengths per packet:

    - v1.0: up to 250 bytes (``ESP_NOW_MAX_DATA_LEN``). This is limited because the Length field of one vendor-specific element in IEEE 802.11 is only 1 byte (0xff = 255), so the payload in a single element is at most 250 bytes.
    - v2.0: up to 1470 bytes (``ESP_NOW_MAX_DATA_LEN_V2``), by concatenating multiple vendor-specific elements in an action frame.

  - Maximum lengths supported by ESP-IDF versions:

    - Before v5.4: only v1.0 is supported; maximum 250 bytes per packet.
    - v5.4 and later: v2.0 is supported; maximum 1470 bytes per packet (early v5.4 and v5.4.1 used 1490 bytes; corrected to 1470 bytes from v5.4.2). v1.0 (250 bytes) remains supported for backward compatibility.

  - These limits are determined by the protocol version and cannot be changed arbitrarily by the user. To bypass this encapsulation, you can send with API ``esp_wifi_80211_tx()`` and receive in sniffer mode, which also works only on the Wi-Fi stack without the TCP/IP stack.
  - If you use the `esp-now component <https://github.com/espressif/esp-now>`__ (application-level wrapper):

    - The usable payload per frame is ``ESPNOW_PAYLOAD_LEN``, which is the protocol-layer maximum minus the component header (20 bytes, ``sizeof(espnow_data_t)``): 1450 bytes on IDF versions that support v2.0 (1470 bytes on early v5.4 and v5.4.1), and 230 bytes before v5.4.
    - With application-layer encryption enabled, TAG(4) + IV(8) take another 12 bytes. The usable size is ``ESPNOW_SEC_PACKET_MAX_SIZE`` (that is, ``ESPNOW_PAYLOAD_LEN`` − 12; for example, 1438 bytes on v5.5).
    - The component also supports fragmentation for large transfers such as OTA and log upload.

--------------

What is the difference between ESP-NOW v1.0 and v2.0? Can they be mixed?
----------------------------------------------------------------------------------------------------------

  - The main difference is the maximum payload length per packet: 250 bytes for v1.0 (``ESP_NOW_MAX_DATA_LEN``) and 1470 bytes for v2.0 (``ESP_NOW_MAX_DATA_LEN_V2``). Call ``esp_now_get_version()`` to query the ESP-NOW version on the current device.
  - Compatibility:

    - A v2.0 device can receive packets from both v2.0 and v1.0 devices.
    - A v1.0 device can receive packets from v1.0 devices. It can also receive v2.0 packets whose length does not exceed 250 bytes (``ESP_NOW_MAX_IE_DATA_LEN``). If the packet is longer than 250 bytes, only the first 250 bytes are kept or the entire packet is dropped.

  - Therefore, in a network that mixes v1.0 and v2.0 devices, keep the packet length within 250 bytes on the sender to ensure interoperability. For more information, see the `ESP-NOW documentation <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_now.html>`__.

--------------

What should I pay attention to when using ESP-NOW applications?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The device cannot switch channels after connecting to Wi-Fi. It can only transmit and receive data on the current Wi-Fi channel.
  - By default, the device can receive ESP-NOW data normally (the wake window of ``esp_now_set_wake_window()`` defaults to the maximum value, so the RF stays on). Only when you configure a smaller wake window so that the device sleeps periodically will data sent outside that window be missed; synchronize the TX and RX windows at the application layer. The wake-window setting takes effect when the device is connected to an AP. When it is not connected to an AP, you must also enable ``CONFIG_ESP_WIFI_STA_DISCONNECTED_PM_ENABLE`` (see the power-consumption FAQ below).

---------------

How can I reduce power consumption when using ESP-NOW?
--------------------------------------------------------------------------------------------------------------------------

  - You can use the following methods to reduce power consumption:

    - If you use an ESP-IDF version earlier than v5.0, when not connected to an AP, you can configure the wake window and interval with `esp_now_set_wake_window() <https://docs.espressif.com/projects/esp-idf/en/release-v4.4/esp32/api-reference/network/esp_now.html#_CPPv423esp_now_set_wake_window8uint16_t>`__ and `esp_wifi_set_connectionless_wake_interval() <https://docs.espressif.com/projects/esp-idf/en/v4.4.4/esp32/api-reference/network/esp_wifi.html#_CPPv441esp_wifi_set_connectionless_wake_interval8uint16_t>`__ to save power.
    - If you use ESP-IDF v5.0 or later, the function names and meanings have changed. Whether or not the device is connected to an AP, you can use `esp_now_set_wake_window() <https://docs.espressif.com/projects/esp-idf/en/release-v5.0/esp32/api-reference/network/esp_now.html#_CPPv423esp_now_set_wake_window8uint16_t>`__ and `esp_wifi_connectionless_module_set_wake_interval() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv448esp_wifi_connectionless_module_set_wake_interval8uint16_t>`__ to set the wake window and interval.

  - Note that window synchronization between the sender and the receiver must be considered in the application-layer design. The chip wakes up at every interval and stays awake for the configured window duration. In this case, you also need to set ``CONFIG_ESP_WIFI_STA_DISCONNECTED_PM_ENABLE=y`` in ``sdkconfig.defaults``.

-----------------

In addition to wireless communication through ESP-NOW, is there any other better way to realize one-to-one and one-to-many communication?
-------------------------------------------------------------------------------------------------------------------------------------------

  One-to-one and one-to-many communication can also be realized by using SoftAP + Station. The master device applies Wi-Fi SoftAP mode to establish connections with multiple slave devices (Wi-Fi Station) at the same time.

-----------------

Do ESP-NOW applications support sending packets over each Wi-Fi channel?
-----------------------------------------------------------------------------------------------------------------------------------------

  Yes, please refer to `ESP-NOW documentation <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_now.html>`__.

-----------------

Are there any special procedures required if I intend to use ESP-NOW for commercial purposes? Could you provide technical documentation on ESP-NOW? To evaluate the quality of wireless communication, I would like to know relevant information about parameters including CSMA/CA, modulation method, and bit rate.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The application for ESP-NOW does not require any special procedures.
  - For technical documentation, please refer to `ESP-NOW User Guide <https://www.espressif.com/sites/default/files/documentation/esp-now_user_guide_en.pdf>`__. You can use examples in `ESP-NOW SDK <https://github.com/espressif/esp-now>`__ for testing.
  - The default bit rate of ESP-NOW is 1 Mbps.

---------------

Why does testing the `esp-idf/examples/wifi/espnow <https://github.com/espressif/esp-idf/tree/master/examples/wifi/espnow>`__ example on ESP32 support connecting to only 7 encrypted devices at most?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - This behavior depends on the ESP-IDF version:

    - ESP-IDF v5.1 and later: for ESP32, the default number of encrypted devices is 7 and the maximum is 17. You can change it with ``CONFIG_ESP_WIFI_ESPNOW_MAX_ENCRYPT_NUM`` in the Wi-Fi menuconfig.
    - Before ESP-IDF v5.1: fixed at 6 and not configurable.

  - See also :ref:`What is the maximum number of devices that can be controlled by ESP-NOW? <esp-now-max-control-devices>` above, and the `Add Paired Device <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_now.html#add-paired-device>`__ documentation.

---------------

How do I obtain the corresponding RSSI when transferring data using ESP-NOW?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The following describes how to obtain RSSI at the ESP-IDF protocol layer (``esp_now``). The method depends on the ESP-IDF version (the signature of the receive callback ``esp_now_recv_cb_t`` changed in v5.1):

    - Before ESP-IDF v5.1: the callback only provides ``mac_addr`` / ``data`` / ``data_len`` and does not include ``rx_ctrl``, so RSSI cannot be read from the callback. On older versions, you can only capture same-channel 802.11 frames in promiscuous (sniffer) mode, read ``rx_ctrl.rssi``, and correlate them with ESP-NOW packets by source MAC. Upgrading to v5.1 or later is recommended so that RSSI can be read directly from the callback.
    - ESP-IDF v5.1 and later: the first callback argument is ``esp_now_recv_info_t``. Read RSSI from the ``rssi`` field of its ``rx_ctrl`` member (type `wifi_pkt_rx_ctrl_t <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv418wifi_pkt_rx_ctrl_t>`__).

  - If you use the `esp-now component <https://github.com/espressif/esp-now>`__, you do not need to handle the version difference yourself: the component data receive callback (``handler_for_data_t`` registered via ``espnow_set_config_for_data_type()``) provides ``wifi_pkt_rx_ctrl_t *rx_ctrl`` directly. Read ``rx_ctrl->rssi``.

-------------

How do I use RSSI in ESP-NOW to achieve selective range control?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  You can achieve it by modifying the ``.forward_ttl`` and ``.forward_rssi`` fields of `g_initiator_frame in espnow_ctrl.c <https://github.com/espressif/esp-now/blob/master/src/control/src/espnow_ctrl.c>`__. For parameter descriptions, see ``espnow_frame_head_t`` in `esp-now/src/espnow/include/espnow.h <https://github.com/espressif/esp-now/blob/master/src/espnow/include/espnow.h>`__.
