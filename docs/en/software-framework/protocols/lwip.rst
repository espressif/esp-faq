lwIP
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

How soon can the associated resources be released after the TCP connection is closed?
-----------------------------------------------------------------------------------------------------------------

  The associated resources can be released in 2 MSL, i.e. 120 seconds, or after the sent ``linger/send_timeout`` parameter is timeout.

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
  - Please enable the LOOPBACK option from lwIP in menuconfig: ``menuconfig`` > ``Component config`` > ``LWIP`` > ``Enable per-interface loopback`` (type "Y" to enable).
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

When ESP32 & ESP8266 are used as TCP servers, how can the ports be used again immediately after they are released?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - On both ESP32 and ESP8266, TCP ports are not immediately released after being closed. They remain in a TIME_WAIT state for a certain period of time. During this period, binding a socket with the same port and source address as before will fail. This is to ensure that you can receive the FIN signal sent by the server and can close the connection successfully. In this state, the port cannot be immediately reused. To address this issue, the socket option "SO_REUSEADDR" should be used, which allows the device to bind a TCP socket with the same port and source address in the TIME-WAIT state.

  - Therefore, a TCP server program can set the "SO_REUSEADDR" socket option before calling bind() to bind the same port.
  - Alternatively, the setsockopt() function can be used to set the SO_REUSEADDR option. Here is an example:

    .. code-block:: c
    
      int reuse = 1;
      if (setsockopt(socket, SOL_SOCKET, SO_REUSEADDR, &reuse, sizeof(reuse)) < 0) {
        ESP_LOGE(TAG, "setsockopt(SO_REUSEADDR) failed");
        return ESP_FAIL;
      }

    In the above code, "socket" means a socket that has already been created, and "reuse" is an integer variable with a value of 1, indicating that the SO_REUSEADDR option is enabled. If the setsockopt() function returns a negative value, it means that the setting has failed. 
    Enabling the SO_REUSEADDR option allows the port to be immediately reused after being closed. However, there are some potential risks. If another connection uses the same port while it is still in the TIME_WAIT state, it may cause packet confusion. Thus, it's better to make choice based on actual situations.

------------------

After downloading the tcp_client example for an ESP32 module, I connected the module to the router via Wi-Fi and performed a Ping test on the computer. Then the it shows high latency sometimes, what is the reason?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  When Wi-Fi is connected, Power Save mode will be turned on by default, which may cause high Ping delay. To solve this issue, you can turn off Power Save mode to reduce the delay by calling `esp_wifi_set_ps(WIFI_PS_NONE) <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv415esp_wifi_set_ps14wifi_ps_type_t>`_ after ``esp_wifi_start()``.

----------------------

How can I set static IP when using ESP-IDF?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  For details, please refer to `static_ip example <https://github.com/espressif/esp-idf/tree/master/examples/protocols/static_ip>`__.
        
--------------

Does ESP32 have an LTE connection demo?
---------------------------------------------------------------------------------------

  - Yes. For ESP-IDF v4.2 and later versions, please refer to the `example/protocols/pppos_client demo <https://github.com/espressif/esp-idf/tree/v4.4.4/examples/protocols/pppos_client>`__.
  - For ESP-IDF v5.0 and later versions, please refer to `examples <https://github.com/espressif/esp-protocols/tree/master/components/esp_modem/examples/pppos_client>`__ in the `esp-protocols` repo.

--------------

Will memory leak occur when ESP32 TCP repeatedly closes and rebuilds socket (IDF 3.3)?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  In ESP-IDF v3.3, every time a socket is created, a lock will be assigned, given that this internal socket array has not been assigned any lock before. This lock will not be reclaimed after the socket is released. Thus, next time the same socket array is allocated, the previous lock will be used again. That is to say, every time a new socket array is allocated and released, there will be one lock memory used. After all socket arrays being allocated, there will be no memory leak any more.
  
----------------

Are there any limits on the maximum number of TCP client connection after the ESP32 additionally opens the TCP server?
----------------------------------------------------------------------------------------------------------------------------------------------------------------

  Yes. The number of simultaneously connected socket fd number for ESP32 is limited by ``LWIP_MAX_SOCKETS``, which is 10 by default.

--------------

What is the default MTU of lwIP for an ESP32?
----------------------------------------------------------------------------------------------

  The default MTU of lwIP is 1500. This is a fixed value and it is not recommended to change it.
  
---------------

How to increase the DNS request time for ESP32?
------------------------------------------------------------------------------------

  You can manually modify the ``#define DNS_MAX_RETRIES 4`` in esp-idf/components/lwip/lwip/src/include/lwip/opt.h. For example, you can change the value of ``#define DNS_MAX_RETRIES`` to 10. In this way, the maximum time that DNS waits for a response from the server is 46 s (1+1+2+3+4+5+6+7+8+9).

---------------

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

  Yes, please refer to `esp_modem <https://github.com/espressif/esp-protocols/tree/master/components/esp_modem/examples/>`__ example.

----------------

Every time ESP32 attempts to read 4 KB of data with ``read`` and ``recv`` APIs in the socket, it can not always read the 4 KB of data. Why?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Both ``read`` and ``recv`` APIs are used to read the data in the underlying buffer. For example, if there are 100 bytes of data in the underlying buffer, and the ``len`` size passed in by ``read`` and ``recv`` is only 50, then the API will return after it reads 50 bytes. If ``len`` exceeds the length of the data received in the underlying buffer, say 200, the API will return after it reads 100 bytes and will not wait until it receives 200 bytes. So, an attempt to read 4 KB of data will not necessarily return 4 KB of data, but only the data available in the underlying buffer at the time of reading.
  - If you need to read 4 KB of data every time, it is recommended to use application code on top of the socket layer to design the corresponding logic, which reads data recursively until it reaches 4 KB.

----------------

What is the version of lwIP currently used in ESP-IDF?
--------------------------------------------------------------------------------------------------------------------------------

  lwIP v2.1.3 is used currently.

----------------

In DHCP mode, will ESP32 renew the IP or apply for a new IP when the lease expires?
--------------------------------------------------------------------------------------------------------------------------------

  There are two lease periods, T1 (1/2 time of the lease) and T2 (7/8 time of the lease) in DHCP mode. When both lease expires, ESP32 usually renews the same IP. Only when both of them fail to renew will ESP32 apply for a new IP.

----------------

Why does ESP-IDF report an error when ``SO_SNDBUF`` option of ``setsockopt`` are used to get or set the size of the send buffer?
-------------------------------------------------------------------------------------------------------------------------------------

  By default, lwIP does not support ``SO_SNDBUF``. To set the send buffer size, go to ``menuconfig`` -> ``Component config`` -> ``LWIP`` -> ``TCP`` -> ``Default send buffer size``. To get or set the receive buffer size, you need to enable the ``CONFIG_LWIP_SO_RCVBUF`` option in menuconfig before you can use the ``SO_RCVBUF`` option of ``setsockopt`` to get or set the receive buffer size.

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

Is it possible to operate the same socket in multiple threads in ESP-IDF?
-----------------------------------------------------------------------------------------------------------

  In ESP-IDF, it is possible for multiple threads to share one single socket for communication. Each thread can use the same socket to send and receive data, but it is important to ensure thread synchronization when accessing the socket to avoid race conditions and deadlocks. Typically, a mutex can be used to control access to the socket, ensuring that each thread's access to the socket is mutually exclusive to avoid data corruption caused by concurrent access to the socket. However, operating on the same socket from multiple threads is risky, and it is not recommended.

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

What is the difference between socket blocking and non-blocking in ESP-IDF?
-----------------------------------------------------------------------------------------------------------

  - For reads, the difference is whether the read interface returns immediately when no data arrives at the bottom. A blocking read will wait until data has arrived or until an exception occurs, while a non-blocking read will return immediately with or without data.
  - For writes, the difference is whether the write interface returns immediately when the underlying buffer is full. For blocking write, if the underlying buffer is not writable (the underlying buffer is full or the peer has not acknowledged the previously sent data), the write operation will keep blocking until it is writable or an exception occurs. For non-blocking write, it will write as much as it can without waiting for the underlying buffer to be writable or the length of the write to be returned.
  - The non-blocking interface call does not block the current process, while the blocking interface does.

----------------

Can ESP32 use the IP of the previous successful connection for communication after connecting to the router, and in case of failure, re-enter the authentication process and use DHCP to obtain a new IP?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes, if you enable ``Component config`` -> ``LWIP ->DHCP: Restore last IP obtained from DHCP server`` option in menuconfig.
  - Note that you cannot use a static IP instead, because static IP settings do not have conflict detection. It may lead to IP conflict.

----------------

How do I achieve connect_timeout when programming with sockets?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -  If you set the socket to the non-blocking mode, the connect() function will also be non-blocking. Then you can set the timeout by the select() function to determine whether the socket is connected successfully or not. For details, please refer to `"connect_timeout settings of sockets" <https://blog.csdn.net/wy5761/article/details/17695349>`_.

----------------

When ESP32 uses SNTP to synchronize the current time, I found that there is a random delay. After further analysis, I found that it is caused by ``SNTP_STARTUP_DELAY`` in the IDF lwip component, the default value of which is 1. Is there any way to avoid the random delay without modifying the IDF component?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - There is no way to avoid the random delay without modifying the IDF component. You need to manually add the code ``#define SNTP_STARTUP_DELAY 0`` to lwipopts.h in the lwip component. This code reduces the time that SNTP takes to send a request, so it can reduce the total time for ESP devices connecting to the cloud after they are powered up as a result.
  - The reason for enabling this random delay option by default is that it is mandated by the SNTP RFC protocol. A random delay can reduce the number of simultaneous accessing devices, so this can prevent the SNTP server from being overloaded.

----------------

Do IPv4 and IPv6 support setting a static IP?
-----------------------------------------------------------------------------------------------------------------------------------------

  - If it is a local static IP, IPv4 supports manual configuration, but the local IP for IPv6 is automatically generated according to protocol rules and does not require manual configuration.
  - If it is a global static IP, both IPv6 and IPv4 support manual configuration.

------------------------

After connecting an Android phone to ESP SoftAP, the phone will prompt "No Internet access, do you want to continue using it?" If I choose "Do not use", the phone can still access external web pages through cellular data. However, I cannot access external web pages through an Apple phone with the same operation. What is the reason for this? How to solve it?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Reason: The DHCP ACK returned by the ESP DHCP Server includes the option3 (router) field. Therefore, after the mobile phone parses this option, it will set the default route to 192.168.4.1, causing the Apple mobile phone to access external web pages through ESP Wi-Fi instead of cellular data.
  - Solution: You can comment out the `dhcpserver.c code snippet <https://github.com/espressif/esp-idf/blob/master/components/lwip/apps/dhcpserver/dhcpserver.c#L434-L441>`__.

----------------------------

TCP or UDP transmission fails with the error code 12(ENOMEM). How to solve it?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  12 indicates insufficient memory. First, print the remaining internal memory. If the memory is sufficient, the error is caused by a full Wi-Fi TX buffer. In this case, please send data on the application layer more slowly or increase the Wi-Fi TX buffer in sdkconfig.

----------------------------

What usually causes the `transport_base: Poll timeout or error, errno=Connection already in progress` error? How to determine if a poll timeout is due to network issues or code logic problems?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  This error is usually caused by an unstable network connection or a full underlying buffer. A poll timeout indicates that no ACK was received from the peer, or the peer did not respond while waiting for the write operation to complete. Packet capture analysis can be used to determine whether the ACK from the peer was not received or the peer did not respond. If it's a network issue, you can optimize the network environment or add a retry mechanism; if it's a code logic issue, you need to check whether the use of `poll` and `select` in the code is correct, ensuring that the timeout period and retry strategy are appropriately configured.
