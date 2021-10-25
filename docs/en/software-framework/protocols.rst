Protocols
=========

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

Does ESP8266 OpenSSL support Hostname validation?
-----------------------------------------------------------------------

  Yes. ESP8266 OpenSSL is based on mbedTLS encapsulation, which supports ``Hostname validation``. ESP-TLS can be used to switch between mbedTLS and wolfSSL.

--------------

Does ESP32 support PCI-E protocol?
-----------------------------------------------------

  No, it doesn't.

--------------

How to optimize communication latency for ESP32？
-----------------------------------------------------------------------

  - It is recommended to turn off the sleep function for Wi-Fi by calling the API ``esp_wifi_set_ps(WIFI_PS_NONE)``.
  - You can also disable the ``AMPDU`` function in menuconfig.

--------------

Does ESP8285 support CCS (Cisco Compatible eXtensions)?
-----------------------------------------------------------------------------

  No, it doesn't.

--------------

Does ESP8266 support HTTP hosting?
------------------------------------------------------

  Yes, it does. ESP8266 can run as a server in both SoftAP and Station modes.

  - When running as a server in SoftAP mode, clients can directly access the ESP8266 host or server at 192.168.4.1 (default) IP address.
  - When the server is accessed via a router, the IP address should be the one allocated to the ESP8266 by the router.
  - When using SDK to write native code, please refer to relevant examples.
  - When using AT commands, start a server using ``AT+CIPSERVER`` command.

--------------

Does ESP32 support LoRa (Long Range Radio) communication?
--------------------------------------------------------------------------------

  No, the ESP32 itself does not have the LoRa protocol stack and the corresponding RF parts. However, to realize communication between Wi-Fi and LoRa devices, you can connect an external chip integrated with LoRa protocol to ESP32. In this way, ESP32 can be used as the master control MCU to connect the LoRa chip.

--------------

How soon can the associated resources be released after the TCP connection is closed?
----------------------------------------------------------------------------------------------------------------

 - The associated resources can be released in 20 seconds or can be specified by the sent linger/send_timeout parameter.

--------------

How to configure the server address so as to make it an autonomic cloud platform by using MQTT?
-----------------------------------------------------------------------------------------------------------------------------------------

  Please refer to `MQTT Examples <https://github.com/espressif/esp-idf/tree/master/examples/protocols/mqtt>`_.

--------------

With ESP32, are there any return instructions if I skip to a function using the ``jump`` instruction in ULP？
-----------------------------------------------------------------------------------------------------------------------------------------------

  Please see `here <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/ulp_instruction_set.html#add-add-to-register>`_ for ULP CPU instructions list and corresponding specifications. Normally, a general register is used for return instructions to store backup PC addresses for later jumping backs. Since there are only four general registers in ULP for now, please make proper use of them.

--------------

After the SNTP calibration for ESP8266 RTOS SDK v3.2, errors gradually increase. How to resolve such issue？
------------------------------------------------------------------------------------------------------------------------------------------------

  This is because the ESP8266 uses software timer, which brings large errors itself. You can improve it with the following solutions:

  - For branch v3.2, you can resynchronize time (300 s is recommended) from the server regularly by creating a task.
  - For branch release-v3.3, the code of system timer has been refactored and is tested with low errors. On the other hand, you can still synchronize time from the server regularly.
  - The master branch has inherited the refactored code from branch release-v3.3. In addition, you can configure the SNTP synchronization interval in menuconfig: ``Component config > LWIP > SNTP -> Request interval to update time (ms)``.

-----------------

Does ESP8266 support loop-back for device-end UDP broadcasts?
-----------------------------------------------------------------------------------------------------

  - Yes, it does.
  - Please enable the LOOPBACK option from LWIP in menuconfig: ``menuconfig -> Component config -> Enable per-interface loopback (type "Y" to enable)``.

--------------

What is the default packet length for TCP/IP?
-----------------------------------------------------------------

  In default configurations, the single packet TCP is 1460 bytes and UDP is 1472 bytes.

--------------

When using UTC and GMT methods in SNTP protocol, why can't I get the time of the target time zone？
---------------------------------------------------------------------------------------------------------------------------------------

  - The "TZ = UTC-8" refers to POSIX time, in which "UTC" is the abbreviation of any time zone and the number is the number of hours that the time zone is behind UTC.
  - "UTC-8" indicates a certain time zone, "UTC" for short, which is -8 hours later than the actual UTC. Therefore, "UTC+8" is 8 hours later than the actual UTC, and also 16 hours later than Beijing.

--------------

Is there any special firmware or SDK in ESP32 that can only provide AP/STA (TCP/IP bypass) without using its internal TCP/IP so as to give developers more permissions?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The software solution ESP-Dongle can fit your requirements. Please contact `Business Team <https://www.espressif.com/en/contact-us/sales-questions>`_ to sign NDA and then get related solutions.

--------------

Can I add any broadcast data I want to Android ESP-Touch (e.g., add a device ID so that ESP32 can receive this ID)?
------------------------------------------------------------------------------------------------------------------------------------------------------

  - No, the data content sent under the current ESP-Touch protocol is fixed and cannot be customized.
  - If you expect to send customized data, it is recommended to use Blufi, which is the networking protocol based on Bluetooth LE. Please refer to the following references for Blufi:

    - Android APP：https://github.com/EspressifApp/EspBlufiForAndroid.
    - iOS APP：https://github.com/EspressifApp/EspBlufiForiOS.

----------------

When testing RTOS-SDK mqtt/ssl_mutual_auth with ESP8266, the server connection failed. Why?
-------------------------------------------------------------------------------------------------------------------------------

  - The failure of SSL connection may due to insufficient memory of ESP8266.
  - Please use the Master version of ESP8266-RTOS-SDK to test this example, since it supports dynamic memory allocation in menuconfig so as to reduce the usage of memory peak. The specific action is:

    - menuconfig -> Component config -> mbadTLS -> (type “Y” to enable) Using dynamic TX /RX buffer -> (type “Y” to enable) Free SSL peer certificate after its usage -> (type “Y” to enable) Free certificate, key and DHM data after its usage.

----------------

After calling ``esp_netif_t* wifiAP = esp_netif_create_default_wifi_ap()`` for ESP32-S2 chips, a following call of ``esp_netif_destroy(wifiAP)`` to deinit caused a 12-byte of memory leakage. What is the reason?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - It is necessary to call ``esp_wifi_clear_default_wifi_driver_and_handlers(wifiAP)`` before ``esp_netif_destroy(wifiAP)``. This is the correct deinit process. Following this process, there will be no memory leakage.

----------------

When ESP32 & ESP8266 are used as TCP Servers, how can the ports be used again immediately after they are released?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - After closing the TCP socket, it often enters the TIME-WAIT state. At this time, the socket with the same source address of the same port as before will fail. The socket option SO_REUSEADDR is needed. Its function is to allow the device binding to be in TIME-WAIT state, the port and source address are the same as the previous TCP socket.
  - So the TCP server program can set the SO_REUSEADDR socket option before calling bind() and then bind the same port.

------------------

After downloading the tcp_client example for an ESP32 module, I connected the module to the router via Wi-Fi and performed a Ping test on the computer. Then the it shows high latency sometimes, what is the reason?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - When Wi-Fi is connected, Power Save mode will be turned on by default, which may cause high Ping delay. To solve this issue, you can turn off Power Save mode to reduce the delay by calling ``esp_wifi_set_ps (WIFI_PS_NONE)`` after ``esp_wifi_start()``.

----------------------

I'm using ESP8266 release/v3.3 version of SDK to test the example/protocols/esp-mqtt/tcp example. Then during Wi-Fi configuration, the connection fails after configuring SSID, password and connecting to the default server. The log is as follows, what is the reason?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    W (4211) MQTT_CLIENT: Connection refused, not authorized
    I (4217) MQTT_CLIENT: Error MQTT Connected
    I (4222) MQTT_CLIENT: Reconnect after 10000 ms
    I (4228) MQTT_EXAMPLE: MQTT_EVENT_DISCONNECTED
    I (19361) MQTT_CLIENT: Sending MQTT CONNECT message, type: 1, id: 0000

  - When such error occurs, it is usually because the connected server is unavailable. Please use another available server for testing.

-----------------

Using esp-idf release/v3.3 version of the SDK, is there an example for setting static IP for Ethernet?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - It can be set through the "tcpip_adapter_set_ip_info()" API , please refer to `API description <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v3.3/api-reference/network/tcpip_adapter.html?highlight=tcpip_adapter_set_ip_info#_CPPv425tcpip_adapter_set_ip_info18tcpip_adapter_if_tPK23tcpip_adapter_ip_info_t>`_.
  - Please refer to the example as follows:

    .. code-block:: text

      /* Stop dhcp client */
      tcpip_adapter_dhcpc_stop(TCPIP_ADAPTER_IF_STA);
      /* static ip settings */
      tcpip_adapter_ip_info_t sta_ip;
      sta_ip.ip.addr = ipaddr_addr("192.168.1.102");
      sta_ip.gw.addr = ipaddr_addr("192.168.1.1");
      sta_ip.netmask.addr = ipaddr_addr("255.255.255.0");
      tcpip_adapter_set_ip_info(TCPIP_ADAPTER_IF_STA, &sta_ip);
        
--------------

Does ESP32 have an LTE connection demo?
---------------------------------------------------------------------------------------

  - Yes, please refer to the example/protocols/pppos_client demo in ESP-IDF v4.2 and later versions.

--------------

Will memory leak occur when ESP32 TCP repeatedly closes and rebuilds socket (IDF 3.3)?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - In ESP-IDF v3.3, every time a socket is created, a lock will be assigned, given that this internal socket array has not been assigned any lock before. This lock will not be reclaimed after the socket is released. Thus, next time the same socket array is allocated, the previous lock will be used again. That is to say, every time a new socket array is allocated and released, there will be one lock memory used. After all socket arrays being allocated, there will be no memory leak any more.
  
----------------

How to optimize memory when ESP32 uses mbedtls?
------------------------------------------------------------------------------------------------

  - You can enable dynamic buffer in menuconfig, the specific operation is ``menuconfig -> Component config -> mbedTLS -> Using dynamic TX/RX buffer (key "Y" to enable)``.
  - At the same time, you can enable the sub-options ``Free SSL peer certificate after its usage`` and ``Free certificate, key and DHM data after its usage`` in the ``Using dynamic TX/RX buffer`` in the previous step.

--------------

What is the default keep-alive value of the MQTT component in ESP-IDF?
---------------------------------------------------------------------------------------

  - The default value is 120 s, which is defined by ``MQTT_KEEPALIVE_TICK`` in file ``mqtt_config.h``.
  
----------------

Are there any limits on the maximum number of TCP client connection after the ESP32 additionally opens the TCP server?
----------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes. The number of simultaneously connected socket fd number for ESP32 is limited by LWIP_MAX_SOCKETS, which is 10 by default.

--------------

Does MQTT support automatic reconnection?
------------------------------------------------

  - The automatic reconnection of MQTT is controlled by the ``disable_auto_reconnect`` variable of struct `esp_mqtt_client_config_t <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/protocols/mqtt.html#_CPPv424esp_mqtt_client_config_t>`_. The default value of ``disable_auto_reconnect`` is ``false``, which means that automatic reconnection is enabled.
  - The reconnection timeout value can be set using ``reconnect_timeout_ms``.
