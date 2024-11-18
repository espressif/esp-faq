ESP-TLS
=======

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

ESP8266 测试 RTOS SDK ``mqtt/ssl_mutual_auth`` 为何连接服务器失败？
--------------------------------------------------------------------------------------

  - 出现 SSL 无法连接可能是由于 ESP8266 内存不足导致。
  - 请使用 ESP8266-RTOS-SDK master 版本来测试此例程，master 版本支持在 menuconfig 配置端动态分配内存，可以减少峰值内存的开销，通过 menuconfig -> ``Component  config`` -> ``mbedTLS`` ->（键 “Y” 使能） ``Using  dynamic TX /RX buffer`` ->（键 “Y” 使能） ``Free SSL peer certificate after its usage`` ->（键 “Y” 使能） ``Free certificate, key and DHM data after its usage``。

----------------

ESP HTTPS 在使用时能跳过服务器证书校验吗？
--------------------------------------------------------------------------------------------------------------------------------

  - 可以，请在 menuconfig 里使能以下选项：

    - ``Menu path: (Top)`` -> ``Component config`` -> ``ESP-TLS`` -> ``Allow potentially insecure options``
    - ``Menu path: (Top)`` -> ``Component config`` -> ``ESP-TLS`` -> ``Allow potentially insecure options`` -> ``Skip server certificate verification by default``

  - 同时要确保 ``esp_http_client_config_t`` 结构体里不设置 ``cert_pem`` 成员变量。如果设置了 ``cert_pem``，就仍会用这个设置的 CA 证书校验服务器证书。
  - 如果要同时测试 HTTP OTA，还需要在 menuconfig 里使能 ``Menu path: (Top)`` -> ``Component config`` -> ``ESP HTTPS OTA`` -> ``Allow HTTP for OTA`` 选项。

----------------

如何将 ESP-TLS 中的 ``esp_tls_conn_read`` API 设置成非阻塞模式？或者有其他方式来实现非阻塞？
--------------------------------------------------------------------------------------------------------------------------------

  - 可以将 ``esp_tls.h`` 里 ``esp_tls_cfg_t`` 结构体里的 ``non_block`` 设置为 true 来实现非阻塞。
  - 也可以调用 ``esp_transport_connect_async`` 来实现非阻塞。

----------------

ESP-IDF 支持的 TLS 版本有哪些？
-----------------------------------------------------------------------------------------------------------

  - ESP-IDF 里推荐的 TLS 协议为 Mbed TLS 协议。
  - ESP-IDF v5.0 及以上版本不再支持 SSL 3.0，TLS 1.0 和 TLS 1.1，当前支持的 TLS 版本为 TLS 1.2 和 TLS 1.3。

------------------------

如何分析 SSL 握手会报 "mbedtls_ssl_handshake returned -0x7200" 错误？
-----------------------------------------------------------------------------------------------------------------------------------------------------------

  - 0x7200 的错误可能有以下几点：

    - MBEDTLS_SSL_IN_CONTENT_LEN 过小，一般小于最大 16 K
    - 内存不够
    - 服务器拒绝 ESP 连接，发送的 SSL record 不完整，需要抓包看下, 详情请参考 `乐鑫 Wireshark 使用指南 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/wireshark-user-guide.html#wireshark>`__。

----------------

使用 IP 访问 MQTTS Broker 时出现 ``MBEDTLS_ERR_X509_CERT_VERIFY_FAILED`` 错误，但是用同样的条件在 MQTTX 等测试工具中就能成功进行通信，可能是什么原因？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  可能是 CN 字段不匹配，可以通过配置成员变量 `skip_cert_common_name_check <https://github.com/espressif/esp-mqtt/blob/e6afdb4025fe018ae0add44e3c45249ea1974774/include/mqtt_client.h#L260>`__ 为 True 来跳过 CN 检查。

----------------

ESP32 进行稳定的 TLS 握手需要多少内存？TLS 握手时出现内存不足的问题，如何解决？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  TLS 握手通常需要 40～50 KB 的空闲堆内存，用于在握手过程中进行临时分配。如果内存碎片过多或可用内存不足，可能会导致握手失败。内存不足时需要优化内存，可以参考 `内存优化 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/performance/ram-usage.html>`__ 。此外，如果模组带有外部 PSRAM，请确保正确配置以使用该内存。

----------------

TLS 握手时出现错误码 ``0x6900`` 和 ``0x7600``，这些错误分别代表什么？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ``0x6900 (MBEDTLS_ERR_SSL_WANT_READ)``：通常表示操作会被阻塞，因为 TCP 接收缓冲区中暂时没有数据。这不一定是错误，而是表示需要等待更多的数据到达。
  - ``0x7600 (MBEDTLS_ERR_SSL_PRIVATE_KEY_REQUIRED)``：表示未设置所需的私钥或预共享密钥。在双向认证的情况下，请确保客户端已经设置了正确的私钥。

----------------

在 ESP32 上实现 HTTPS 时，如果服务器证书链与 PC 浏览器获取的不同，应如何解决？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  可以尝试在 ESP32 上启用更详细的 mbedtls 调试信息，以获取 TLS 握手过程中服务器发送的证书链，并与浏览器获取的证书链进行对比分析。

----------------

在使用 ESP32 时，遇到证书解析失败的问题，应该如何解决？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  首先应该检查证书格式是否符合 X509 标准，确保证书链没有问题。此外，打开 mbedtls 的日志功能可以帮助诊断问题所在。