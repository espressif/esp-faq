协议
====

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


ESP8266 OpenSSL 是否⽀持验证主机名？
--------------------------------------------------------

  ⽀持，目前 ESP8266 OpenSSL 是基于 Mbed TLS 封装的接口，Mbed TLS 支持 验证主机名。使用 ESP-TLS 可以根据配置切换 mbedTLS 与 wolfSSL。

--------------

ESP32 如何优化通信延时？
-----------------------------------

  - 建议关闭 Wi-Fi 休眠功能，调用 API ``esp_wifi_set_ps(WIFI_PS_NONE)``。
  - 建议在 menucongfig 关掉 ``AMPDU`` 功能。

--------------

ESP8285 是否⽀持 CCS (Cisco Compatible eXtensions)？
-----------------------------------------------------------------

  ESP8285 不支持 CCS (Cisco Compatible eXtensions)。

--------------

ESP8266 ⽀持 HTTP 服务端吗？  
----------------------------------------

  ⽀持。ESP8266 在 SoftAP 和 Station 模式下都可以作服务端。

  - 在 SoftAP 模式下，ESP8266 的服务端 IP 地址是 192.168.4.1。
  - 如果 Station 模式，服务端的 IP 地址为路由器分配给 ESP8266 的 IP。
  - 如果基于 SDK 进行⼆次开发，可参考相关应用示例。
  - 如果使⽤ AT 指令，需使⽤ ``AT+CIPSERVER`` 开启服务端。

--------------

ESP32 是否支持 LoRa (Long Range Radio) 通信？
------------------------------------------------------------

  ESP32 自身并不支持 LoRa 通信，芯片没有集成 LoRa 协议栈与对应的射频部分。ESP32 可以外接集成 LoRa 协议的芯⽚，作为主控 MCU 连接 LoRa 芯片，可以实现 Wi-Fi 与 LoRa 设备的通信。

--------------

TCP 链接关闭后占用的相关资源何时释放？
------------------------------------------------

  TCP 链接关闭后占用的相关资源会在 20 s 或者发送的 ``linger/send_timeout`` 超时之后释放。

--------------

如何使用 MQTT 配置服务器地址为自主云平台？
------------------------------------------------------

  可以参考 `MQTT 例程 <https://github.com/espressif/esp-idf/tree/master/examples/protocols/mqtt>`_。

--------------

ESP8266 RTOS SDK v3.2 SNTP 校准后误差会逐渐变大，如何解决？
-------------------------------------------------------------------------------

  原因是 ESP8266 系统定时器有误差，采用软件定时器，自身存在误差较大。可通过以下几种方法改善：

  - 分支 v3.2 可以通过创建 task 定时重新从服务器同步时间（推荐 300 s）。
  - 分支 release-v3.3 的系统时钟代码有进行重构，目前测试误差较小，并且也可以定时同步服务器时间。
  - 分支 master 继承了 release-v3.3 上的代码重构，除此之外，可通过 menuconfig 配置 SNTP 同步间隔，路径如下：``Component config`` > ``LWIP`` > ``SNTP`` > ``Request interval to update time (ms)``。

-----------------

ESP8266 是否支持设备端自发自收？
---------------------------------------------------------------------------------

  - ESP8266 设备端支持自发自收。
  - 需要在 menuconfig 配置选项中把 LWIP 的 LOOPBACK 选项打开：``menuconfig`` > ``Component config`` > ``LWIP`` > ``Enable per-interface loopback`` (键 "Y" 使能)。
  - 设备端往环回地址 127.0.0.1 发送数据，设备端可以在环回地址读取到自己发送的数据。

--------------

TCP/IP 默认配置的数据包长度是多少？
-------------------------------------------------

  请参考 ``menuconfig`` > ``Component config`` > ``LWIP`` > ``TCP`` > ``Maximum Segment Size (MSS)`` 配置的值。

--------------

SNTP 协议中使用 UTC 与 GMT 的方法为何获取不到目标时区的时间？
----------------------------------------------------------------------------

  - "TZ = UTC-8" 被解释为 POSIX 时区。在 POSIX 时区格式中，这 3 个字母是时区的缩写（任意），数字是时区落后于 UTC 的小时数。 
  - "UTC-8" 表示时区，缩写为 "UTC"，比实际 UTC 晚 -8 小时，即 UTC + 8 小时。故 UTC+8 是比 UTC 落后 8 小时，就出现了 UTC+8 比正确的北京时间相差 16 小时的情况。

--------------

ESP32 是否有特殊的固件或者 SDK，可以不使用芯片内部的 TCP/IP 协议仅提供 AP/STA (TCP/IP bypass)，以给开发者更多的权限？
---------------------------------------------------------------------------------------------------------------------------------------------------

  ESP-Dongle 的软件方案符合您的上述需求，请联系 `商务 <https://www.espressif.com/zh-hans/contact-us/sales-questions>`_ 签署 NDA 后获取相关方案。

--------------

安卓 ESP-Touch 可以添加自己想要广播的数据吗（如添加设备 ID，希望 ESP32 能接收到这个 ID）？
-----------------------------------------------------------------------------------------------------------

  - 目前的 ESP-Touch 协议下发送的数据内容都是固定的，不支持自定义数据。
  - 如果需要发送自定义数据的话，建议使用 BluFi，这是基于 Bluetooth LE 的配网协议。请参见：

    - Android APP：https://github.com/EspressifApp/EspBlufiForAndroid。
    - iOS APP：https://github.com/EspressifApp/EspBlufiForiOS。

----------------

ESP8266 测试 RTOS SDK ``mqtt/ssl_mutual_auth`` 为何连接服务器失败？
-------------------------------------------------------------------------------------

  - 出现 SSL 无法连接可能是由于 ESP8266 内存不足导致。
  - 请使用 ESP8266-RTOS-SDK master 版本来测试此例程，master 版本支持在 menuconfig 配置端动态分配内存，可以减少峰值内存的开销，通过 menuconfig -> ``Component  config`` -> ``mbedTLS`` ->（键 “Y” 使能） ``Using  dynamic TX /RX buffer`` ->（键 “Y” 使能） ``Free SSL peer certificate after its usage`` ->（键 “Y” 使能） ``Free certificate, key and DHM data after its usage``。

----------------

ESP32-S2 在调用 ``esp_netif_t* wifiAP  = esp_netif_create_default_wifi_ap()`` 后通过 ``esp_netif_destroy(wifiAP)`` 注销会产生 12 字节的内存泄露，什么原因？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 需要在 ``esp_netif_destroy(wifiAP)`` 前额外调用 ``esp_wifi_clear_default_wifi_driver_and_handlers(wifiAP)``，这样才是正确的注销流程，此时可发现内存泄露的情况已消失。
  - 也可以直接调用 ``esp_netif_destroy_default_wifi(wifiAP)``，该接口在 ESP-IDF v4.4 版本以上支持。

--------------

ESP32 & ESP8266 做 TCP server 时端口释放后如何立即被再次使用？
--------------------------------------------------------------------------------------------

  - 关闭 TCP 套接字后，往往会进入 ``TIME-WAIT`` 状态，此时绑定与之前相同端口相同源地址的套接字会失败，需要借助套接字选项 ``SO_REUSEADDR``，它的作用是允许设备绑定处于 ``TIME-WAIT`` 状态，端口和源地址与之前相同的 TCP 套接字。
  - 故 TCP server 程序可以在调用 bind() 之前设置 ``SO_REUSEADDR`` 套接字选项后来绑定同样的端口。

------------------

使用 ESP32 模组下载 tcp_client 例程，通过 Wi-Fi 连接路由器，在电脑端进行 Ping 测试，偶尔出现高延时，是什么原因？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Wi-Fi 默认开启 Power Save 模式，关闭 Power Save 可降低由于 Power Save 引起的 Ping 高延时，在 esp_wifi_start() 之后调用 esp_wifi_set_ps(WIFI_PS_NONE) 来关闭 Power Save 模式。

--------------

使用 ESP8266 release/v3.3 版本的 SDK 测试 examples/protocols/esp-mqtt/tcp 例程，配置 Wi-Fi 账号、密码，连接默认配置的服务器，出现连接失败，log 如下，是什么原因？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    W (4211) MQTT_CLIENT: Connection refused, not authorized
    I (4217) MQTT_CLIENT: Error MQTT Connected
    I (4222) MQTT_CLIENT: Reconnect after 10000 ms
    I (4228) MQTT_EXAMPLE: MQTT_EVENT_DISCONNECTED
    I (19361) MQTT_CLIENT: Sending MQTT CONNECT message, type: 1, id: 0000

  当出现如上报错，表示服务器拒绝了连接，原因是客户端错误的 MQTT 用户名和密码导致服务端认证没有通过。建议您确认是否使用了正确的 MQTT 用户名和密码。

----------------

使用 ESP-IDF release/v3.3 版本的 SDK ，请问以太网有设置静态 IP 的例程吗？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 可通过 ``tcpip_adapter_set_ip_info()`` API 来设置，请参见 `API 说明 <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v3.3/api-reference/network/tcpip_adapter.html?highlight=tcpip_adapter_set_ip_info#_CPPv425tcpip_adapter_set_ip_info18tcpip_adapter_if_tPK23tcpip_adapter_ip_info_t>`_。
  - 例程参考如下：

  .. code-block:: text

      /* Stop dhcp client */
      tcpip_adapter_dhcpc_stop(TCPIP_ADAPTER_IF_STA);
      /* static ip settings */
      tcpip_adapter_ip_info_t sta_ip;
      sta_ip.ip.addr = ipaddr_addr("192.168.1.102");
      sta_ip.gw.addr = ipaddr_addr("192.168.1.1");
      sta_ip.netmask.addr = ipaddr_addr("255.255.255.0");
      tcpip_adapter_set_ip_info(TCPIP_ADAPTER_IF_STA, &sta_ip);

----------------

ESP32 有没有 LTE 连接示例？
-----------------------------------------------------------------------------

  可以参考 ESP-IDF v4.2 及以上版本里的 examples/protocols/pppos_client 示例。

----------------

ESP32 TCP 反复关闭并重建 socket 时会出现内存泄漏的情况 (ESP-IDF v3.3)，原因是什么？
-----------------------------------------------------------------------------------------------------------------------------------------

  IDF v3.3 版本，每次创建 socket 时，如果内部该 socket 数组没有分配过锁，就会给该 socket 分配锁，并且该锁在 socket 释放后并不会回收，下次分配该 socket 数组时就使用之前分配的。所以每次分配新的 socket 数组后释放，就会多一个锁的内存消耗。当每个 socket 数组都分配一遍后，就不会存在内存泄漏。

----------------

ESP32 使用 Mbed TLS 时如何优化内存？
-----------------------------------------------------------------------------

  - 可以在 menuconfig 里开启动态 buffer， 具体操作为 ``menuconfig -> Component config -> mbedTLS -> Using dynamic TX/RX buffer（键 "Y" 使能）``。
  - 同时可以使能上一步的 ``Using dynamic TX/RX buffer`` 里的子选项 ``Free SSL peer certificate after its usage`` 和 ``Free certificate, key and DHM data after its usage``。

--------------

ESP-IDF 中 MQTT 组件 keepalive 的默认值是多少？
----------------------------------------------------

  默认值为 120 s，在 ``mqtt_config.h`` 中通过 ``MQTT_KEEPALIVE_TICK`` 定义。

----------------

ESP32 额外开启 TCP server 后对 TCP client 的最大连接数是否有限制？
-----------------------------------------------------------------------------------------------------------------------------------------------------------

  有限制，ESP32 同时存在的 socket fd 数量受限于 ``LWIP_MAX_SOCKETS``，默认为 10。

--------------

MQTT 支持自动重连吗？
----------------------------------------

  - MQTT 的自动重连由 `esp_mqtt_client_config_t <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/protocols/mqtt.html?highlight=esp_mqtt_client_config_t#_CPPv424esp_mqtt_client_config_t>`_ 中的成员变量　``disable_auto_reconnect`` 控制，该变量值默认为 ``false``，表示使能自动重连。
  - 可以使用 ``reconnect_timeout_ms`` 设置重连超时时间。
  
---------------

使用 ESP32，LWIP 的 MTU 默认是多大？
-----------------------------------------------------------------------------------

  LWIP 的 MTU 默认是 1500（固定值），不建议自行修改。

---------------

ESP32 如何增大 DNS 请求时间？
-----------------------------------------------------------------------------------

  可以手动修改位于 esp-idf/components/lwip/lwip/src/include/lwip/opt.h 里的 ``#define DNS_MAX_RETRIES 4``，例如将 ``#define DNS_MAX_RETRIES`` 的值改成 10，这样 DNS 在一个服务器上会尝试 10 次域名请求，每次请求的超时时间(s)是 1，1，2，3，4，5，6，7，8，9，总时间是 46 s。

---------------

如何使用 ``esp_http_client`` 发送块 (chunked) 数据？
-----------------------------------------------------------------------------------

  - 可以通过 `HTTP Stream <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/protocols/esp_http_client.html#http-stream>`_ 的方式，将 ``esp_http_client_open()`` 的 ``write_len``　参数设置为 -1，代码中会自动将 ``Transfer-Encoding`` 设置为 ``chunked``，参考 `esp_http_client.c <https://github.com/espressif/esp-idf/blob/master/components/esp_http_client/esp_http_client.c>`_ 中的 ``http_client_prepare_first_line()``。
  - 可使用如下代码：

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

如何实现证书自动下载功能 ?
---------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32:

  具体操作详情参考 `aws 下面证书自动下载功能 <https://docs.aws.amazon.com/zh_cn/iot/latest/developerguide/auto-register-device-cert.html>`_ 。

-----------------------------

连续多次创建并关闭 TCP SOCKET 后出现报错 "Unable to create TCP socket: errno 23"，怎么解决？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  :CHIP\: ESP8266 | ESP32 | ESP32-S2 | ESP32-C3 | ESP32-S3 :

  - 原因："errno 23" 代表的是 open many open files in system，由于关闭 socket 需要 2 MSL 的时间，所以调用 close 接口并不会立即关闭，导致 socket 持续累加，超过了 socket 最大支持连接数（menuconfig 中默认是 10 个，最大支持 16 个）报错。
  - 解决措施：通过 setsockopt 接口设置 SO_LINGER 来调整 TCP 关闭时间，代码实现参考：

::

    linger link ;
    link.on_off = 1 ;
    link.linger = 0 ;
    setsockopt(m_sockConnect, SOL_SOCKET, SO_LINGER, (const char*)&link, sizeof(linger));

----------------

ESP8266 收到 "tcp out of order" 的报文会怎么处理？
-------------------------------------------------------------------------------------

  - 如果使能 ``CONFIG_LWIP_TCP_QUEUE_OOSEQ(Component config -> LWIP -> TCP -> Queue incoming out-of-order segments)``，会存储 "out of order" 的报文，代价是消耗内存。
  - 如果该配置是未使能，收到 "out of order" 的报文，会丢弃数据并让对端重传。比如现在有 1、2、3、4 四包数据，ESP8266 先收到 1 然后收到 4。该配置使能时，ESP8266 会把 4 这个数据存下来，等收到 2、3 后，把这四包数据上报应用层；该配置未使能时，ESP8266 会直接丢弃 4，并让对端发送包 2，对端就会从 2 开始发送，即该情况下会增加重传。

----------------

ES32 支持 PPP 功能吗？
----------------------------------------------------------------------------------------------------------------

  支持，请参考 `usb_cdc_4g_module <https://github.com/espressif/esp-iot-solution/tree/usb/add_usb_solutions/examples/usb/host/usb_cdc_4g_module/>`_ 示例。

----------------

ESP32 作为 HTTP 客户端，可以设置 cookie 的方式吗？
----------------------------------------------------------------------------------------------------------------

  ESP32 本身没有直接设置 cookie 的 API，但可以通过 `esp_http_client_set_header <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/protocols/esp_http_client.html#_CPPv426esp_http_client_set_header24esp_http_client_handle_tPKcPKc>`_ 向 HTTP 头里添加 cookie 等头数据的方式来设置 cookie。

----------------

ESP32 使用套接字中的 ``read`` 和 ``recv`` API 读取 4 KB 数据时，发现并不是每次都能读到 4 KB 的数据。这种情况如何解释？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ``read`` 和 ``recv`` API 都是用来读底层缓冲区中的数据，比如底层缓冲区中有 100 字节数据，``read`` 和 ``recv`` 传入的 ``len`` 大小只有 50 字节，那么 API 读到 50 字节的数据时就会返回；如果传入的 ``len`` 超过底层缓冲区中接收到的数据的长度，比如 200 字节，此时 API 读到 100 字节就会返回，并不会等到接收到 200 字节才返回。所以传入 4 KB 的长度的数据并不一定会返回 4KB 长度的数据，只会返回读取时底层缓冲区中有的数据。
  - 如果需要每次都读取到 4 KB 的数据，建议在套接字层之上使用应用代码设计对应的逻辑，让应用代码循环读取数据直到满足 4 KB 的大小。

----------------

ESP-IDF 里目前使用的 lwIP 版本是什么？
--------------------------------------------------------------------------------------------------------------------------------

  lwIP 版本目前是 2.1.2。

----------------

ESP32 作为 HTTP 服务器时，如何设置可同时连接的客户端个数上限？如果客户端连接个数超出上限，会出现怎样的情况？
--------------------------------------------------------------------------------------------------------------------------------

  - 通过配置 ``httpd_config_t`` 结构体里的 ``max_open_sockets`` 即可设置同时连接的客户端最大个数。
  - 如果存在客户端连接个数超出上限的情况，可以把 ``httpd_config_t`` 结构体里的 ``lru_purge_enable`` 参数设置为 true。这个参数设置为 true 的作用是如果没有可用的套接字（这个套接字由 ``max_open_sockets`` 决定)，就会清除最少使用的那个套接字从而接受最新的套接字。

----------------

ESP HTTPS 在使用时能跳过服务器证书校验吗？
--------------------------------------------------------------------------------------------------------------------------------

  - 可以，请在 menuconfig 里使能以下选项：

    - ``Menu path: (Top)`` -> ``Component config`` -> ``ESP-TLS`` -> ``Allow potentially insecure options``
    - ``Menu path: (Top)`` -> ``Component config`` -> ``ESP-TLS`` -> ``Allow potentially insecure options`` -> ``Skip server certificate verification by default``

  - 同时要确保 ``esp_http_client_config_t`` 结构体里不设置 ``cert_pem`` 成员变量。如果设置了 ``cert_pem``，就仍会用这个设置的 CA 证书校验服务器证书。
  - 如果要同时测试 HTTP OTA，还需要在 menuconfig 里使能 ``Menu path: (Top)`` -> ``Component config`` -> ``ESP HTTPS OTA`` -> ``Allow HTTP for OTA`` 选项。

----------------

ESP32 是否支持在连上路由后使用上一次成功连接路由器时的 IP 进行通信，如果失败再重新开始认证流程，通过 DHCP 来获取新的 IP？
--------------------------------------------------------------------------------------------------------------------------------

  - 支持，可以在 menuconfig 里使能 ``Component config`` > ``LWIP ->DHCP: Restore last IP obtained from DHCP server`` 选项。
  - 需要注意的是，此时不能用静态 IP 来代替，因为静态 IP 设置没有冲突检测，可能会导致 IP 冲突。

----------------

ESP32 是否有至少在 HTTP/2 上实现 gRPC 客户端的示例？
--------------------------------------------------------------------------------------------------------------------------------

  目前还没有。

----------------

在 ESP-IDF 中，如何通过 HTTP 下载文件里的某一特定段（即在头部添加 ``Range:bytes`` 信息）？
--------------------------------------------------------------------------------------------------------------------------------

  可以参考 `esp http client 示例 <https://github.com/espressif/esp-idf/tree/v4.4.1/examples/protocols/esp_http_client>`_ 里的 ``http_partial_download`` 函数。

----------------

在 DHCP 模式下，ESP32 申请到 IP 后，如果租期到期，会续约此 IP 还是重新申请 IP？
--------------------------------------------------------------------------------------------------------------------------------

  DHCP 模式下有两个租期，T1（租约的 1/2 时间）和 T2（租约的 7/8 时间），通常这两个租期期满后会续租同一 IP，只有当上述两个租期时间点都续租失败，才会重新申请 IP。

----------------

如何将 ESP-TLS 中的 ``esp_tls_conn_read`` API 设置成非阻塞模式？或者有其他方式来实现非阻塞？
--------------------------------------------------------------------------------------------------------------------------------

  - 可以将 ``esp_tls.h`` 里 ``esp_tls_cfg_t`` 结构体里的 ``non_block`` 设置为 true 来实现非阻塞。
  - 也可以调用 ``esp_transport_connect_async`` 来实现非阻塞。


----------------

ESP-IDF 里使用 ``setsockopt`` 的 ``SO_SNDBUF`` 选项获取或者设置发送缓冲区大小会报错，为什么？
--------------------------------------------------------------------------------------------------------------------------------

  lwIP 默认不支持 ``SO_SNDBUF`` 选项，如果需要配置发送缓冲区大小可以在 menuconfig -> ``Component config`` -> ``LWIP`` -> ``TCP`` -> ``Default send buffer size`` 设置。如果需要获取或者设置接收缓冲区大小，此时需要在 menuconfig 里使能 ``CONFIG_LWIP_SO_RCVBUF`` 选项后才支持使用 ``setsockopt`` 的 ``SO_SNDBUF`` 选项获取或者设置接收缓冲区大小。

----------------

ESP-IDF 里如何根据错误码来获取更多的调试信息？
--------------------------------------------------------------------------------------------------------------------------------

  - ESP-IDF 3.x 版本下的错误码 (errno) 列表直接存在于 IDF 中，点击 `errno.h <https://github.com/espressif/esp-idf/blob/release/v3.3/components/newlib/include/sys/errno.h>`_ 可以进行查询。
  - ESP-IDF 4.x 版本的 ``errno.h`` 位于编译器工具链下，比如，对于 esp-2020r3 而言，errno.h 的路径为 ``/root/.espressif/tools/xtensa-esp32-elf/esp-2020r3-8.4.0/xtensa-esp32-elf/xtensa-esp32-elf/include/sys/errno.h``。

----------------

ESP-IDF 支持的 MQTT 版本有哪些？
-----------------------------------------------------------------------------------------------------------

  ESP-IDF 目前支持的 MQTT 版本为 MQTT 3.1 和 MQTT 3.1.1.

----------------

ESP-IDF 支持的 TLS 版本有哪些？
-----------------------------------------------------------------------------------------------------------

  - ESP-IDF 里推荐的 TLS 协议为 Mbed TLS 协议。
  - ESP-IDF 目前支持的 TLS 版本为 TLS1.0、TLS1.1 和 TLS1.2。

----------------

ESP8266_RTOS_SDK 是否支持 TR-069 协议？
-----------------------------------------------------------------------------------------------------------

  不支持。

----------------

ESP32 支持 SAVI 吗？
-----------------------------------------------------------------------------------------------------------

  不支持，SAVI (Source Address Validation Improvements) 是通过监听控制类报文（如 ND、DHCPv6），即 CPS (Control Packet Snooping)，在接入设备上（AP 或交换机）为终端建立基于 IPv6 源地址、源 MAC 地址及接入设备端口的绑定关系，进而对通过指定端口的 IP 报文进行源地址校验。只有报文源地址与绑定表项匹配时才可以转发，保证网络上数据报文源地址真实性。这种一般针对于交换机或者企业级 AP 路由器的，是策略协议。目前 ESP32 支持 IPv6 链路本地地址、全球地址通信。

----------------

使用 ESP-IDF 测试发现 TCP & UDP 的网络数据延时较大，请问 TCP & UDP 协议的缓冲数据机制是什么？
-----------------------------------------------------------------------------------------------------------

  - 对于 TCP，套接字选项里有 ``TCP_NODELAY`` 选项，可以使能该选项来禁用默认使能的 Nagle 算法，这样就不会出现本地缓存一定数据后再一起发送的情况。
  - 对于 UDP，UDP 的数据交互采取直接发送的形式，如果有延迟，也是 Wi-Fi 网络环境的延迟，和 UDP 本身无关。
  - 如果是网络环境较差导致 TCP 重传，重传的间隔设置过大会导致延迟高，可以尝试缩短 RTO 的值（通过修改 menuconfig 里的 ``component config`` -> ``lwip`` -> ``tcp`` -> ``Default TCP rto time`` 和 ``TCP timer interval`` 选项）。

----------------

ESP32 做双网卡（比如 ETH+STA）时，默认路由如何选择？
---------------------------------------------------------------------------------------------------------

  以下总结了双网卡时默认路由如何选择，以 ETH 和 STA 为例：

  - 假设 ETH 和 STA 在同一个局域网：

    - 当设备访问局域网地址时，数据走最后 up 的 netif。
    - 当设备访问非局域网内地址时，数据走 ``route_prio`` 值大的 netif。

  - 假设 ETH 和 STA 不在一个局域网，ETH 属于 192.168.3.x 网段，STA 属于 192.168.2.x 网段：

    - 当设备访问 192.168.3.5 时，就会走 ETH netif。
    - 当设备访问 192.168.2.5 时，就会走 STA netif。
    - 当设备访问 10.10.10.10 时，就会走默认路由（``route_prio`` 值大的 netif）。netif 起来后，会根据 ``route_prio`` 值大小设置默认路由，默认路由往往是 ``route_prio`` 值大的 netif。当设备访问的地址不在路由表里时，数据就会走默认路由。

----------------

ESP-IDF 里 TCP 如何开启 keepalive？
-----------------------------------------------------------------------------------------------------------

  可以参考 `esp_tls.c <https://github.com/espressif/esp-idf/blob/v4.4.1/components/esp-tls/esp_tls.c#L207>`_ 里的使能 TCP keepalive 相关代码。

----------------

ESP-IDF 里 Wi-Fi 连接断开的时候，之前 MQTT 上层协议申请的内存会自动释放吗？
-----------------------------------------------------------------------------------------------------------

  - 不会自动释放，但对于用户而言不需要关心这部分内存。用户要关心的是 ESP 给用户封装的应用层。
  - 对于 MQTT 应用层组件，用户初始化 MQTT 的时候会获得一个 MQTT 句柄，用户只需关心这个句柄里的内存，在不用 MQTT 的时候调用 ``stop`` 或者 ``destory`` 释放对应 MQTT 内存即可。对于 Wi-Fi 断开与连接，用户也不需要通过 ``stop`` 或者 ``destory`` 释放这个 MQTT 句柄然后再重新申请 MQTT 句柄。因为 MQTT 组件里有自动重连机制。

----------------

ESP32-C3 MQTT 是否能不设置对应的 ``client_id`` 而将 ``client_id`` 默认配置为空字符串？
-----------------------------------------------------------------------------------------------------------

  - 目前不能，应用代码里如果不设置 ``client_id`` 的话，内部代码会默认设置 ``client_id`` 为 ESP32_XXX，所以代码里暂不支持 ``client_id`` 为空。
  - 目前我们有计划添加将 ``client_id`` 默认配置为空字符串的功能，敬请期待。

----------------

使用 ESP-IDF MQTT 客户端发布 QoS 为 1 或者 2 的数据后，当 ``MQTT_EVENT_PUBLISHED`` 触发时是否意味着已经收到了对端合适的 ack 来证明这次发布已完成？还是仅仅只能说明成功发送了一次数据给服务器？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ``MQTT_EVENT_PUBLISHED`` 事件触发代表代理已确认收到客户端的发布的 QoS 为 1 或者 2 的消息，证明这次发布已经顺利完成。
  
----------------

ESP MQTT 客户端断开连接后，如何手动释放 MQTT 资源？
-----------------------------------------------------------------------------------------------------------

  手动调用 ``esp_mqtt_client_destroy`` API 即可。

----------------

ESP-IDF 里可以在多线程里操作同一个套接字吗？
-----------------------------------------------------------------------------------------------------------

  多线程操作同一个套接字有风险，因此不建议该做法。

----------------

ESP DHCP 服务器模式下，ESP 设备分配到其他设备 IP 的时间是多少？
-----------------------------------------------------------------------------------------------------------

  默认为 120 s，具体见 ``DHCPS_LEASE_TIME_DEF`` 参数，不建议修改为太小的值。

----------------

ESP-IDF DHCP 里三个租约相关时间是指什么？具体对应代码里的什么参数？
-----------------------------------------------------------------------------------------------------------

  DHCP 有租约时间 (Address Lease Time)、租约续期时 (Lease Renewal Time) 和租约重新设定的时间 (Lease Rebinding Time)，分别对应 lwIP 代码 ``offered_t0_lease``、``offered_t1_renew`` 和 ``offered_t2_rebind``。

----------------

ESP-IDF lwIP 里每次发送数据的最大长度是多少？
-----------------------------------------------------------------------------------------------------------

  如果使用套接字接口 ``send``，支持最大长度有 ``SSIZE_MAX`` 参数决定。如果使用 ``tcp_write`` 函数，最大发送的长度受限于 ``snd_buf`` （发送缓存区长度）。 ``send`` 接口是 lwIP 基于顺序 API 封装的套接字接口，是比 ``tcp_write`` 还要上层的接口，更适合于用户层开发调用。这两个 API 调用资源占用几乎没有差别。

----------------

使用 ESP-IDF 出现 lwIP 层相关问题需要更多的调试日志时，如何使能对应的调试日志打印（如 lwIP 下的 DHCP 和 IP 等）？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 可以在 menuconfig 里使能 lwIP 相关调试日志选项，具体的选项为：menuconfig -> ``Component config`` -> ``LWIP`` -> ``Enable LWIP Debug``。其中有子选项 ``Enable IP debug messages``、``Enable DHCP debug messages`` 等，可以按实际需要进行勾选来开启对应的调试日志。
  - 如在上述 menuconfig 里没有找到想要的调试日志模块，如 UDP 模块，请首先检查 ``esp-idf/components/lwip/port/esp32/include/lwipopts.h`` 中是否有 ``#define UDP_DEBUG``，如果有，可以手动将 ``#define UDP_DEBUG  LWIP_DBG_OFF`` 修改为 ``#define UDP_DEBUG  LWIP_DBG_ON``。如果没有，可以参照 `esp-idf/components/lwip/lwip/src/include/lwip/opt.h <https://github.com/espressif/esp-lwip/blob/76303df2386902e0d7873be4217f1d9d1b50f982/src/include/lwip/opt.h#L3489>`_ 文件下的 ``#define UDP_DEBUG  LWIP_DBG_OFF``，在 ``esp-idf/components/lwip/port/esp32/include/lwipopts.h`` 里加一行 ``#define UDP_DEBUG  LWIP_DBG_ON``。

----------------

ESP32 Wi-Fi 和低功耗蓝牙共存时，MQTT keepalive 时间该如何配置？有没有什么合适的配置时间？
-----------------------------------------------------------------------------------------------------------

  无需特殊考虑这种情况，只要不是太小即可，如可以配置为 30 s、60 s 等。

----------------

ESP MQTT 客户端的 disconnect 事件消息什么时候才会触发？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  disconnect 消息只有在以下情况出现：

  - MQTT 建立连接时，TCP 连接错误
  - MQTT 建立连接时，MQTT 连接错误
  - 自行主动调用了 ``disconnect`` 函数
  - 接收或发送数据异常
  - 规定时间内没收到对端 MQTT ``PING RESPONSE``
  - 发送 MQTT PING 请求失败
  - 重新连接

----------------

ESP32 MQTT 客户端与服务器断开后会自动尝试重新连接吗?
-----------------------------------------------------------------------------------------------------------

  ESP MQTT 客户端里的 ``esp_mqtt_client_config_t`` 结构体配置里有 ``disable_auto_reconnect`` 参数，可以通过配置这个参数为 ``true`` 或者 ``false`` 来决定是否需要 MQTT 自动重连，MQTT 默认会自动进行重连。

----------------

如何检测 ESP32 是否已经与 MQTT 服务器断开?
-----------------------------------------------------------------------------------------------------------

  检测 ESP32 是否已经与服务器断开可以使用 MQTT 的 ``PING`` 机制。也就是配置 ESP-MQTT 中 ``esp_mqtt_client_config_t`` 结构体里的 ``keepalive`` 参数 ``disable_keepalive`` 和 ``keepalive``，比如将 ``disable_keepalive`` 配置为 ``false`` （默认参数也是 ``false``，即默认开启 keepalive 机制），然后配置 ``keepalive`` 参数为 120 s 来设置保活时间，默认为 120 s。这样 MQTT 客户端会定期发送 ``PING`` 来检测和 MQTT 服务器的连接是否正常。

----------------

ESP-IDF 中套接字阻塞和非阻塞的区别是什么?
-----------------------------------------------------------------------------------------------------------

  - 对于读而言，阻塞和非阻塞的区别在于底层没有数据到达时读接口是否立刻返回。阻塞的读会一直等到读取到数据或者异常，非阻塞的读会立刻返回，无论有无数据。
  - 对于写而言，阻塞和非阻塞的区别在于底层缓冲区满了后写接口是否立刻返回。阻塞的写，如果底层不可写（底层缓冲区满了或者对端没有 ack 之前发送的数据），这时候的写操作会一直阻塞，直到可写或者异常才会退出；非阻塞的写是可以写多少就写多少，无需等待底层是否可写，返回写入的长度。
  - 非阻塞接口调用后不会阻塞当前进程继续执行，阻塞接口调用后会阻塞当前进程执行。