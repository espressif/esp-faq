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
----------------------------------------------------------------------------------------------------------------

  The associated resources can be released in 20 seconds or can be specified by the sent ``linger/send_timeout`` parameter.

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

  - After closing the TCP socket, it often enters the ``TIME-WAIT`` state. At this time, the socket with the same source address of the same port as before will fail. The socket option ``SO_REUSEADDR`` is needed. Its function is to allow the device binding to be in ``TIME-WAIT`` state, the port and source address are the same as the previous TCP socket.
  - So the TCP server program can set the ``SO_REUSEADDR`` socket option before calling bind() and then bind the same port.

------------------

After downloading the tcp_client example for an ESP32 module, I connected the module to the router via Wi-Fi and performed a Ping test on the computer. Then the it shows high latency sometimes, what is the reason?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  When Wi-Fi is connected, Power Save mode will be turned on by default, which may cause high Ping delay. To solve this issue, you can turn off Power Save mode to reduce the delay by calling ``esp_wifi_set_ps (WIFI_PS_NONE)`` after ``esp_wifi_start()``.

----------------------

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

  Yes, please refer to `usb_cdc_4g_module <https://github.com/espressif/esp-iot-solution/tree/usb/add_usb_solutions/examples/usb/host/usb_cdc_4g_ module/>`_ example.

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

  By default, lwIP does not support ``SO_SNDBUF``. To set the send buffer size, go to ``menuconfig`` -> ``Component config`` -> ``LWIP`` -> ``TCP`` -> ``Default send buffer size``. To get or set the receive buffer size, you need to enable the ``CONFIG_LWIP_SO_RCVBUF`` option in menuconfig before you can use the ``SO_SNDBUF`` option of ``setsockopt`` to get or set the receive buffer size.

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
