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


Does ESP8266 OpenSSL support hostname validation?
-----------------------------------------------------------------------

  Yes. ESP8266 OpenSSL is based on Mbed TLS encapsulation, which supports ``hostname validation``. ESP-TLS can be used to switch between Mbed TLS and wolfSSL.

--------------

How to optimize communication latency for ESP32?
-----------------------------------------------------------------------

  - It is recommended to turn off the sleep function for Wi-Fi by calling the API ``esp_wifi_set_ps(WIFI_PS_NONE)``.
  - You can also disable the ``AMPDU`` function in menuconfig.

--------------

Does ESP8285 support CCS (Cisco Compatible eXtensions)?
----------------------------------------------------------------------------

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

  The associated resources can be released in 20 seconds or can be specified by the sent ``linger/send_timeout`` parameter.

--------------

How to configure the server address so as to make it an autonomic cloud platform by using MQTT?
-----------------------------------------------------------------------------------------------------------------------------------------

  Please refer to `MQTT Examples <https://github.com/espressif/esp-idf/tree/master/examples/protocols/mqtt>`_.

--------------

After the SNTP calibration for ESP8266 RTOS SDK v3.2, errors gradually increase. How to resolve such issue?
------------------------------------------------------------------------------------------------------------------------------------------------

  This is because the ESP8266 uses software timer, which brings large errors itself. You can improve it with the following solutions:

  - For branch v3.2, you can resynchronize time (300 s is recommended) from the server regularly by creating a task.
  - For branch release-v3.3, the code of system timer has been refactored and is tested with low errors. On the other hand, you can still synchronize time from the server regularly.
  - The master branch has inherited the refactored code from branch release-v3.3. In addition, you can configure the SNTP synchronization interval in menuconfig: ``Component config`` > ``LWIP`` > ``SNTP`` > ``Request interval to update time (ms)``.

-----------------

Does ESP8266 support loop-back for the device end?
-----------------------------------------------------------------------------------------------------

  - Yes, it does.
  - Please enable the LOOPBACK option from LWIP in menuconfig: ``menuconfig`` > ``Component config`` > ``LWIP`` > ``Enable per-interface loopback`` (type "Y" to enable).
  - The device end sends data to the loopback address 127.0.0.1, and can read it from the address.

--------------

What is the default packet length for TCP/IP?
-----------------------------------------------------------------

  Please go to ``menuconfig`` > ``Component config`` > ``LWIP`` > ``TCP`` > ``Maximum Segment Size (MSS)`` for the length.
  
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
  - If you expect to send customized data, it is recommended to use BluFi, which is the networking protocol based on Bluetooth LE. Please refer to the following references for BluFi:

    - Android APP：https://github.com/EspressifApp/EspBlufiForAndroid.
    - iOS APP：https://github.com/EspressifApp/EspBlufiForiOS.

----------------

When testing RTOS SDK ``mqtt/ssl_mutual_auth`` with ESP8266, the server connection failed. Why?
-------------------------------------------------------------------------------------------------------------------------------

  - The failure of SSL connection may due to insufficient memory of ESP8266.
  - Please use the master version of ESP8266-RTOS-SDK to test this example, since it supports dynamic memory allocation in menuconfig so as to reduce the usage of memory peak. The specific action is: menuconfig -> ``Component config`` -> ``mbedTLS`` -> (type “Y” to enable) ``Using dynamic TX /RX buffer`` -> (type “Y” to enable) ``Free SSL peer certificate after its usage`` -> (type “Y” to enable) ``Free certificate, key and DHM data after its usage``.

----------------

After calling ``esp_netif_t* wifiAP = esp_netif_create_default_wifi_ap()`` for ESP32-S2 chips, a following call of ``esp_netif_destroy(wifiAP)`` to deinit caused a 12-byte of memory leakage. What is the reason?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - It is necessary to call ``esp_wifi_clear_default_wifi_driver_and_handlers(wifiAP)`` before ``esp_netif_destroy(wifiAP)``. This is the correct deinit process. Following this process, there will be no memory leakage.
  - Alternatively, call ``esp_netif_destroy_default_wifi(wifiAP)``, which is supported by ESP-IDF v4.4 and later versions.

----------------

When ESP32 & ESP8266 are used as TCP servers, how can the ports be used again immediately after they are released?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - After closing the TCP socket, it often enters the ``TIME-WAIT`` state. At this time, the socket with the same source address of the same port as before will fail. The socket option ``SO_REUSEADDR`` is needed. Its function is to allow the device binding to be in ``TIME-WAIT`` state, the port and source address are the same as the previous TCP socket.
  - So the TCP server program can set the ``SO_REUSEADDR`` socket option before calling bind() and then bind the same port.

------------------

After downloading the tcp_client example for an ESP32 module, I connected the module to the router via Wi-Fi and performed a Ping test on the computer. Then the it shows high latency sometimes, what is the reason?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  When Wi-Fi is connected, Power Save mode will be turned on by default, which may cause high Ping delay. To solve this issue, you can turn off Power Save mode to reduce the delay by calling ``esp_wifi_set_ps (WIFI_PS_NONE)`` after ``esp_wifi_start()``.

----------------------

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

Using esp-idf release/v3.3 version of the SDK, is there an example for setting static IP for Ethernet?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - It can be set through the ``tcpip_adapter_set_ip_info()`` API , please refer to `API description <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v3.3/api-reference/network/tcpip_adapter.html?highlight=tcpip_adapter_set_ip_info#_CPPv425tcpip_adapter_set_ip_info18tcpip_adapter_if_tPK23tcpip_adapter_ip_info_t>`_.
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

  Yes, please refer to the example/protocols/pppos_client demo in ESP-IDF v4.2 and later versions.

--------------

Will memory leak occur when ESP32 TCP repeatedly closes and rebuilds socket (IDF 3.3)?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  In ESP-IDF v3.3, every time a socket is created, a lock will be assigned, given that this internal socket array has not been assigned any lock before. This lock will not be reclaimed after the socket is released. Thus, next time the same socket array is allocated, the previous lock will be used again. That is to say, every time a new socket array is allocated and released, there will be one lock memory used. After all socket arrays being allocated, there will be no memory leak any more.
  
----------------

How to optimize memory when ESP32 uses Mbed TLS?
------------------------------------------------------------------------------------------------

  - You can enable dynamic buffer in menuconfig, the specific operation is ``menuconfig -> Component config -> mbedTLS -> Using dynamic TX/RX buffer (key "Y" to enable)``.
  - At the same time, you can enable the sub-options ``Free SSL peer certificate after its usage`` and ``Free certificate, key and DHM data after its usage`` in the ``Using dynamic TX/RX buffer`` in the previous step.

--------------

What is the default keepalive value of the MQTT component in ESP-IDF?
---------------------------------------------------------------------------------------

  The default value is 120 s, which is defined by ``MQTT_KEEPALIVE_TICK`` in file ``mqtt_config.h``.
  
----------------

Are there any limits on the maximum number of TCP client connection after the ESP32 additionally opens the TCP server?
----------------------------------------------------------------------------------------------------------------------------------------------------------------

  Yes. The number of simultaneously connected socket fd number for ESP32 is limited by ``LWIP_MAX_SOCKETS``, which is 10 by default.

--------------

Does MQTT support automatic reconnection?
------------------------------------------------

  - The automatic reconnection of MQTT is controlled by the ``disable_auto_reconnect`` variable of struct `esp_mqtt_client_config_t <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/protocols/mqtt.html#_CPPv424esp_mqtt_client_config_t>`_. The default value of ``disable_auto_reconnect`` is ``false``, which means that automatic reconnection is enabled.
  - The reconnection timeout value can be set using ``reconnect_timeout_ms``.

-----------------

What is the default MTU of LWIP for an ESP32?
----------------------------------------------------------------------------------------------

  The default MTU of LWIP is 1500. This is a fixed value and it is not recommended to change it.
  
---------------

How to increase the DNS request time for ESP32?
------------------------------------------------------------------------------------

  You can manually modify the ``#define DNS_MAX_RETRIES 4`` in esp-idf/components/lwip/lwip/src/include/lwip/opt.h. For example, you can change the value of ``#define DNS_MAX_RETRIES`` to 10. In this way, the maximum time that DNS waits for a response from the server is 46 s (1+1+2+3+4+5+6+7+8+9).

---------------

How to use ``esp_http_client`` to send chunked data?
-----------------------------------------------------------------------------------

  - Please use `HTTP Stream <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/protocols/esp_http_client.html#http-stream>`_ by setting the  ``write_len`` parameter of ``esp_http_client_open()`` to -1. Then the "Transfer-Encoding" will be set to "chunked" automatically，please see ``http_client_prepare_first_line()`` in　`esp_http_client.c <https://github.com/espressif/esp-idf/blob/master/components/esp_http_client/esp_http_client.c>`_.
  - The code snippet is listed below for your reference：

    .. code-block:: c

      static void http_post_chunked_data()
      {
          esp_http_client_config_t config = {
          .url = "http://httpbin.org/post",
          .method = HTTP_METHOD_POST, // This is NOT required. write_len < 0 will force POST anyway
        };
        char buffer[MAX_HTTP_OUTPUT_BUFFER] = {0};
        esp_http_client_handle_t client = esp_http_client_init(&config);

        esp_err_t err = esp_http_client_open(client, -1); // write_len=-1 sets header "Transfer-Encoding: chunked" and method to POST
        if (err != ESP_OK) {
          ESP_LOGE(TAG, "Failed to open HTTP connection: %s", esp_err_to_name(err));
          return;
        }

        // Post some data
        esp_http_client_write(client, "5", 1); // length
        esp_http_client_write(client, "\r\n", 2);
        esp_http_client_write(client, "Hello", 5); // data
        esp_http_client_write(client, "\r\n", 2);
        esp_http_client_write(client, "7", 1); // length
        esp_http_client_write(client, "\r\n", 2);
        esp_http_client_write(client, " World!", 7);  // data
        esp_http_client_write(client, "\r\n", 2);
        esp_http_client_write(client, "0", 1);  // end
        esp_http_client_write(client, "\r\n", 2);
        esp_http_client_write(client, "\r\n", 2);


        // After the POST is complete, you can examine the response as required using:
        int content_length = esp_http_client_fetch_headers(client);
        ESP_LOGI(TAG, "content_length: %d, status_code: %d", content_length, esp_http_client_get_status_code(client));

        int read_len = esp_http_client_read(client, buffer, 1024);
        ESP_LOGI(TAG, "receive %d data from server: %s", read_len, buffer);
        esp_http_client_close(client);
        esp_http_client_cleanup(client);
      }

-----------------------------------------------------------------------------------------------------

How to implement the certificate auto-download function?
----------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32:

  Please refer to `aws certificate automatic download function <https://docs.aws.amazon.com/en/iot/latest/developerguide/auto-register-device-cert.html>`_ .

-----------------------------

After creating and closing TCP SOCKET several times, an error is reported as "Unable to create TCP socket: errno 23". How to resolve such issue?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  :CHIP\: ESP8266 | ESP32 | ESP32-S2 | ESP32-C3 | ESP32-S3 :

  - Reason: "errno 23 " means open many open files in system. Closing a socket takes 2 MSL of time, which means sockets will not be closed immediately after calling the close interface. Due to this reason, open sockets are accumulated and exceeds the maximum connection number (the default is 10 in menuconfig, the maximum connection is 16) thus triggering this error. 
  - Solution: Set SO_LINGER via the setsockopt interface to adjust the TCP close time.

::

    linger link ;
    link.on_off = 1 ;
    link.linger = 0 ;
    setsockopt(m_sockConnect, SOL_SOCKET, SO_LINGER, (const char*)&link, sizeof(linger));

-----------------------------

What happens when ESP8266 receives a "tcp out of order" message?
-------------------------------------------------------------------------------------

  - If ``CONFIG_LWIP_TCP_QUEUE_OOSEQ(Component config -> LWIP -> TCP -> Queue incoming out-of-order segments)`` is enabled, the out-of-order messages will be stored at the cost of memory consumption.
  - If this configuration is disabled, after receiving the "out of order" message, data will be discarded and a retransmission will be requested. For example, there are four data packets namely 1, 2, 3 and 4, ESP8266 receives 1 first, and then receives 4. If this configuration is enabled, ESP8266 will store the data of 4, wait until it receives 2, 3, and then report the four packets to the application layer; if this configuration is disabled, ESP8266 will discard the packet of 4 when it receives it, and let the other side send packet 2, and then the other side will send from 2. Under this condition, the retransmission is increased.

----------------

Does ES32 support PPP functionality?
----------------------------------------------------------------------------------------------------------------

  Yes, please refer to `usb_cdc_4g_module <https://github.com/espressif/esp-iot-solution/tree/usb/add_usb_solutions/examples/usb/host/usb_cdc_4g_ module/>`_ example.

----------------

Is there a way to set cookies when ESP32 operates as an HTTP client?
----------------------------------------------------------------------------------------------------------------

  ESP32 itself does not have an API for setting cookies directly, but you can use `esp_http_client_set_header <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/protocols/esp_http_client.html#_CPPv426esp_http_client_set_header24esp_http_client_handle_tPKcPKc>`_ to add cookies to the HTTP header.

----------------

Every time ESP32 attempts to read 4 KB of data with ``read`` and ``recv`` APIs in the socket, it can not always read the 4 KB of data. Why?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Both ``read`` and ``recv`` APIs are used to read the data in the underlying buffer. For example, if there are 100 bytes of data in the underlying buffer, and the ``len`` size passed in by ``read`` and ``recv`` is only 50, then the API will return after it reads 50 bytes. If ``len`` exceeds the length of the data received in the underlying buffer, say 200, the API will return after it reads 100 bytes and will not wait until it receives 200 bytes. So, an attempt to read 4 KB of data will not necessarily return 4 KB of data, but only the data available in the underlying buffer at the time of reading.
  - If you need to read 4 KB of data every time, it is recommended to use application code on top of the socket layer to design the corresponding logic, which reads data recursively until it reaches 4 KB.

----------------

What is the version of lwIP currently used in ESP-IDF?
--------------------------------------------------------------------------------------------------------------------------------

  The version is 2.1.2 currently.

----------------

How do I set the maximum number of clients that are allowed for connection when ESP32 serves as an HTTP server? What will happen if the number exceeds the limit?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The maximum number of client connections can be set by configuring ``max_open_sockets`` in the ``httpd_config_t`` structure.
  - If the number of clients exceeds the limit, you can set the ``lru_purge_enable`` parameter in the ``httpd_config_t`` structure to true. In doing so, if there is no socket available (which is determined by max_open_sockets), the least used socket will be cleared to accept the coming one.

----------------

Can ESP HTTPS skip the server certificate check?
--------------------------------------------------------------------------------------------------------------------------------

  - Yes, if you enable the following options in menuconfig.

    - ``Menu path: (Top)`` -> ``Component config`` -> ``ESP-TLS`` -> ``Allow potentially insecure options``
    - ``Menu path: (Top)`` -> ``Component config`` -> ``ESP-TLS`` -> ``Allow potentially insecure options`` -> ``Skip server certificate verification by default``

  - Besides, make sure that the ``cert_pem`` member variable is not set in the ``esp_http_client_config_t`` structure. Otherwise, the server certificate will still be verified with this CA certificate.
  - If you want to test HTTP OTA at the same time, you need to enable the ``Menu path: (Top)`` -> ``Component config`` -> ``ESP HTTPS OTA`` -> ``Allow HTTP for OTA`` option in menuconfig.

----------------

Can ESP32 use the IP of the previous successful connection for communication after connecting to the router, and in case of failure, re-enter the authentication process and use DHCP to obtain a new IP?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes, if you enable ``Component config`` -> ``LWIP ->DHCP: Restore last IP obtained from DHCP server`` option in menuconfig.
  - Note that you cannot use a static IP instead, because static IP settings do not have conflict detection. It may lead to IP conflict.

----------------

Does ESP32 have an example of implementing a gRPC client over HTTP/2 and above versions?
--------------------------------------------------------------------------------------------------------------------------------

  Not yet.

----------------

How to download a specific segment of a file over HTTP in ESP-IDF (i.e., add ``Range:bytes`` information to the header)?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Please refer to the ``http_partial_download`` function in the `esp http client example <https://github.com/espressif/esp-idf/tree/v4.4.1/examples/protocols/esp_http_client>`_.

----------------

In DHCP mode, will ESP32 renew the IP or apply for a new IP when the lease expires?
--------------------------------------------------------------------------------------------------------------------------------

  There are two lease periods, T1 (1/2 time of the lease) and T2 (7/8 time of the lease) in DHCP mode. When both lease expires, ESP32 usually renews the same IP. Only when both of them fail to renew will ESP32 apply for a new IP.

----------------

How to set the ``esp_tls_conn_read`` API in ESP-TLS to non-blocking mode? Or is there any other way to implement non-blocking?
--------------------------------------------------------------------------------------------------------------------------------

  - You can set ``non_block`` to true in the ``esp_tls_cfg_t`` structure in ``esp_tls.h`` to achieve non-blocking.
  - Alternatively, you can call ``esp_transport_connect_async`` to achieve non-blocking.


----------------

Why does ESP-IDF report an error when ``SO_SNDBUF`` option of ``setsockopt`` are used to get or set the size of the send buffer?
-------------------------------------------------------------------------------------------------------------------------------------

  By default, lwIP does not support ``SO_SNDBUF``. To set the send buffer size, go to ``menuconfig`` -> ``Component config`` -> ``LWIP`` -> ``TCP`` -> ``Default send buffer size``. To get or set the receive buffer size, you need to enable the ``CONFIG_LWIP_SO_RCVBUF`` option in menuconfig before you can use the ``SO_SNDBUF`` option of ``setsockopt`` to get or set the receive buffer size.

----------------

How to get more debug information based on errno in ESP-IDF?
--------------------------------------------------------------------------------------------------------------------------------

  - The errno list in ESP-IDF v3.x exists directly in the IDF. Click `errno.h <https://github.com/espressif/esp-idf/blob/release/v3.3/components/newlib/include/sys/errno.h>`_ to check it.
  - The ``errno.h`` for ESP-IDF v4.x is located under the compiler toolchain. For example, for esp-2020r3, the path of ``errno.h`` is ``/root/.espressif/tools/xtensa-esp32-elf/esp-2020r3-8.4.0/xtensa-esp32-elf/xtensa-esp32-elf/include/sys/errno.h``.

----------------

What are the supported MQTT versions of ESP-IDF?
-----------------------------------------------------------------------------------------------------------

  ESP-IDF currently supports the MQTT versions MQTT 3.1 and MQTT 3.1.1.

----------------

What are the TLS versions supported by ESP-IDF?
-----------------------------------------------------------------------------------------------------------

  - The recommended TLS protocol in ESP-IDF is the Mbed TLS protocol.
  - The TLS versions currently supported by ESP-IDF are TLS1.0, TLS1.1 and TLS1.2.

----------------

Does the ESP8266_RTOS_SDK support the TR-069 protocol?
-----------------------------------------------------------------------------------------------------------

  No.

----------------

Does the ESP32 support SAVI?
-----------------------------------------------------------------------------------------------------------

  No, SAVI (Source Address Validation Improvements) is to establish a binding relationship based on IPv6 source address, source MAC address and access device port on the access device (AP or switch) by listening to control packets (such as ND, DHCPv6), i.e. CPS (Control Packet Snooping), and then perform source address validation on IP packets passing through the specified port. Only when the source address of the message matches with the binding table entry can it be forwarded to ensure the authenticity of the source address of data messages on the network. This is generally a policy protocol for switches or enterprise-class AP routers. Currently ESP32 supports IPv6 link-local address and global address for communication.

----------------

I find that the network data latency of TCP & UDP is large when testing ESP-IDF. What is the buffering data mechanism of TCP & UDP protocols?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - For TCP, there is ``TCP_NODELAY`` option in socket option. You can enable this option to disable the Nagle algorithm which is enabled by default, so that the data will not be cached locally and then sent together.
  - For UDP, UDP data is sent directly. If there is any delay, it is because of the delay of the Wi-Fi network environment, not the UDP itself.
  - If TCP retransmission is caused by poor network environment, and the transmission interval is set too long, high latency will occur. You can try to shorten the RTO value (by modifying ``component config`` -> ``lwip`` -> ``tcp`` -> ``Default TCP rto time`` and ``TCP timer interval`` options in menuconfig).

----------------

How to choose the default route when ESP32 works as dual NICs (e.g. ETH+STA)?
-----------------------------------------------------------------------------------------------------------

  The following summarizes how the default route is selected for dual NICs, using ETH and STA as examples.

  - Supposing ETH and STA are in the same LAN:

    - When the device accesses the LAN address, the data will go to the last up netif.
    - When the device accesses the non-LAN address, the data will go to the netif with the larger ``route_prio`` value.
  
  - Supposing ETH and STA are not in a LAN, ETH belongs to 192.168.3.x segment, and STA belongs to 192.168.2.x segment:
  
    - When the device accesses 192.168.3.5, it will take the ETH netif.
    - When the device accesses 192.168.2.5, it will take the STA netif.
    - When the device accesses 10.10.10.10, it takes the default route (the netif with the larger ``route_prio`` value). When netif is up, it sets the default route based on the ``route_prio`` value size, and the default route is often the netif with the larger ``route_prio`` value. When the device accesses an address that is not inside the routing table, the data takes the default route.

----------------

How do I enable keepalive for TCP in ESP-IDF?
-----------------------------------------------------------------------------------------------------------

  You can refer to the code for enabling TCP keepalive in `esp_tls.c <https://github.com/espressif/esp-idf/blob/v4.4.1/components/esp-tls/esp_tls.c#L207>`_.

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

Is it possible to operate the same socket in multiple threads in ESP-IDF?
-----------------------------------------------------------------------------------------------------------

  It is risky to operate the same socket with multiple threads, and thus not recommended.

----------------

How much time do ESP devices allocate to other device's IPs in ESP DHCP server mode?
-----------------------------------------------------------------------------------------------------------

  The default is 120 s. Please refer to the ``DHCPS_LEASE_TIME_DEF`` parameter, which is not recommended to be set to a small value.

----------------

What are the three lease related times in ESP-IDF DHCP? What parameters in the code do they correspond to?
-----------------------------------------------------------------------------------------------------------

  They are Address Lease Time, Lease Renewal Time and Lease Rebinding Time, corresponding to the lwIP codes ``offered_t0_lease``, ``offered_t1_renew``, and ``offered_t2_rebind`` respectively.

----------------

What is the maximum length for each data transmission in the ESP-IDF lwIP?
-----------------------------------------------------------------------------------------------------------

  If you are using the socket interface ``send``, the maximum length supported is determined by the ``SSIZE_MAX`` parameter. If you use the ``tcp_write`` function, the maximum length is limited by ``snd_buf`` (send buffer length). ``send`` is a socket interface wrapped by lwIP based on the sequential API, which is a higher-level interface than ``tcp_write`` and is more suitable for user-level calls. There is basically no difference in resource usage between the two API calls.

----------------

If I need more debug logs for lwIP layer related issues with ESP-IDF, how can I enable the corresponding debug log to be printed (e.g. DHCP, IP)?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - To print lwIP-related debug log, open menuconfig, go to ``Component config`` -> ``LWIP``, and enable the option ``Enable LWIP Debug``. There are sub-options, including ``Enable IP debug messages`` and ``Enable DHCP debug messages``. You could enable them as needed.
  - If you don't find the desired debug log module in the above menuconfig, such as, UDP module, first check if there is ``#define UDP_DEBUG`` in ``esp-idf/components/lwip/port/esp32/include/lwipopts.h``. If yes, change ``#define UDP_DEBUG LWIP_DBG_OFF`` to ``#define UDP_DEBUG LWIP_DBG_ON`` manually. If no, add ``#define UDP_DEBUG LWIP_DBG_ON`` to ``esp-idf/components/lwip/port/esp32/include/lwipopts.h`` referring to ``#define UDP_DEBUG LWIP_DBG_OFF`` in `esp-idf/components/lwip/lwip/src/include/lwip/opt.h <https://github.com/espressif/esp-lwip/blob/ 76303df2386902e0d7873be4217f1d9d1b50f982/src/include/lwip/opt.h#L3489>`_ file.

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

----------------

What is the difference between socket blocking and non-blocking in ESP-IDF?
-----------------------------------------------------------------------------------------------------------

  - For reads, the difference is whether the read interface returns immediately when no data arrives at the bottom. A blocking read will wait until data has arrived or until an exception occurs, while a non-blocking read will return immediately with or without data.
  - For writes, the difference is whether the write interface returns immediately when the underlying buffer is full. For blocking write, if the underlying buffer is not writable (the underlying buffer is full or the peer has not acknowledged the previously sent data), the write operation will keep blocking until it is writable or an exception occurs. For non-blocking write, it will write as much as it can without waiting for the underlying buffer to be writable or the length of the write to be returned.
  - The non-blocking interface call does not block the current process, while the blocking interface does.