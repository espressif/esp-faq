Mbed TLS 
========

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
---------------------------------------------------------

  ⽀持，目前 ESP8266 OpenSSL 是基于 Mbed TLS 封装的接口，Mbed TLS 支持 验证主机名。使用 ESP-TLS 可以根据配置切换 Mbed TLS 与 wolfSSL。

--------------

ESP32 使用 Mbed TLS 时如何优化内存？
-----------------------------------------------------------------------------

  - 可以在 menuconfig 里开启动态 buffer， 具体操作为 ``menuconfig -> Component config -> mbedTLS -> Using dynamic TX/RX buffer（键 "Y" 使能）``。
  - 同时可以使能上一步的 ``Using dynamic TX/RX buffer`` 里的子选项 ``Free SSL peer certificate after its usage`` 和 ``Free certificate, key and DHM data after its usage``。
  - 如果使用的是 v5.0 及以上版本，``Free SSL peer certificate after its usage`` 配置功能将不存在，Mbed TLS 默认提供配置 ``MBEDTLS_SSL_KEEP_PEER_CERTIFICATE``。如果您需要节省内存，可关闭 ``MBEDTLS_SSL_KEEP_PEER_CERTIFICATE``， 具体操作为 ``menuconfig`` > ``Component config`` > ``mbedTLS`` > ``mbedTLS v3.x related`` > ``Keep peer certificate after handshake completion （键 "N" 关闭）``。

-------------

基于 ESP32 模组连接 HTTPS Server, 报错如下，是什么原因？
-----------------------------------------------------------------------------------------------------------

    .. code-block:: c
      
      free heap size: 181784 bytes
      I (4285) esp_https_server: Starting server
      E (4285) esp_https_server: Could not allocate memory
      I (4295) example: Error starting server!
      I (4295) SSDP Server: SSDP server started
      free heap size: 178636 bytes

  - 当前报错是由于内存不足导致。从日志信息来看，是使用了 `esp_get_free_heap_size() <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v5.0/esp32/api-reference/system/misc_system_api.html?highlight=get_free_heap_size#_CPPv422esp_get_free_heap_sizev>`_ API 打印了当前剩余内存，但此剩余内存包含了芯片内部 RAM 和外部 PSRAM 总容量的剩余内存。
  - mbedTLS 默认使用内部 RAM 内存，可使用 `esp_get_free_internal_heap_size() <https://docs.espressif.com/projects/esp-idf/en/release-v5.0/esp32/api-reference/system/misc_system_api.html#_CPPv431esp_get_free_internal_heap_sizev>`_ 获取内部剩余内存。
  - 如果模组带外部 PSRAM，可将 ``menuconfig`` > ``Component config`` > ``mbedTLS`` > ``Memory allocation strategy`` > ``Internal memory`` 配置改为 ``menuconfig`` > ``Component config`` > ``mbedTLS`` > ``Memory allocation strategy`` > ``External SPIRAM`` 进行测试。
