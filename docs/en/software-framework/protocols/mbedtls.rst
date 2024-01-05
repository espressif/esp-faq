Mbed TLS
========

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
------------------------------------------------------------------------

  Yes. ESP8266 OpenSSL is based on Mbed TLS encapsulation, which supports ``hostname validation``. ESP-TLS can be used to switch between Mbed TLS and wolfSSL.

--------------

How to optimize memory when ESP32 uses Mbed TLS?
------------------------------------------------------------------------------------------------

  - You can enable dynamic buffer in menuconfig, the specific operation is ``menuconfig`` > ``Component config`` > ``mbedTLS`` > ``Using dynamic TX/RX buffer (key "Y" to enable)``.
  - At the same time, you can enable the sub-options ``Free SSL peer certificate after its usage`` and ``Free certificate, key and DHM data after its usage`` in the ``Using dynamic TX/RX buffer`` in the previous step.
  - However, ESP-IDF v5.0 and later no longer have sub-optioin ``Free SSL peer certificate after its usage``, and Mbed TLS enables ``MBEDTLS_SSL_KEEP_PEER_CERTIFICATE`` by default. If you want to save memory, you can close it by ``menuconfig`` > ``Component config`` > ``mbedTLS`` > ``mbedTLS v3.x related`` > ``Keep peer certificate after handshake completion (key "N" to disable）``.

----------

When I connected an ESP32 module with the HTTPS Server, I got the following log. What is the reason?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   
    .. code-block:: c
      
      free heap size: 181784 bytes
      I (4285) esp_https_server: Starting server
      E (4285) esp_https_server: Could not allocate memory
      I (4295) example: Error starting server!
      I (4295) SSDP Server: SSDP server started
      free heap size: 178636 bytes

  - The error is caused by low memory. The log shows that you use the `esp_get_free_heap_size() <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v5.0/esp32/api-reference/system/misc_system_api.html?highlight=get_free_heap_size#_CPPv422esp_get_free_heap_sizev>`_ API to get the remaining memory. However, the remaining memory includes the chip's internal RAM as well as external PSRAM.
  - By default, mbedTLS uses internal RAM memory, and you can use the `esp_get_free_internal_heap_size() <https://docs.espressif.com/projects/esp-idf/en/release-v5.0/esp32/api-reference/system/misc_system_api.html#_CPPv431esp_get_free_internal_heap_sizev>`_ API to obtain the remaining internal memory.
  - If the module has an external PSRAM, you can modify the configuration from ``menuconfig`` > ``Component config`` > ``mbedTLS`` > ``Memory allocation strategy`` > ``Internal memory`` to ``menuconfig`` > ``Component config`` > ``mbedTLS`` > ``Memory allocation strategy`` > ``External SPIRAM`` for testing.

-------------

When resolving a hostname on ESP32, I encountered the following error. What could be the reason?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    getaddrinfo() returns 202, addrinfo=0x0
    
  - The error is caused by DNS request timeout.
  - You can enable DNS log with the debug level or capture wireless packets for further analysis.
  - To enable the debug level DNS log, you can add ``#define DNS_DEBUG LWIP_DBG_ON`` code to the ``esp-idf/components/lwip/lwip/src/include/lwip/opt.h`` file, and then enable the ``Component config`` > ``LWIP`` > ``Enable LWIP Debug`` configuration.

-------------

Why does the following mbedtls software error occur when I develop applications based on the esp-idf SDK?
----------------------------------------------------------------------------------------------------------------------------------

    .. code-block:: c

      E: esp-tls-mbedtls: mbedtls_ssl_handshake returned -0x4290 
      E: esp-tls: Failed to open new connection
      E: transport_base: Failed to open a new connection
      E: HTTP_CLIENT: Connection failed, sock < 0
      E: HTTP_CLIENT: Failed to open HTTP connection: ESP_ERR_HTTP_CONNECT

  - The mbedtls error code is 0x4290, which is generally 0x4280 + 0x10. 0x4280 represents the error stage MBEDTLS_ERR_RSA_PUBLIC_FAILED, and 0x10 indicates that the cause of this error stage is MBEDTLS_ERR_MPI_ALLOC_FAILED, which means that this error stage is caused by a failure in memory allocation.
  - For the meanings for mbedtls error codes, refer to `Mbed TLS error codes <https://gist.github.com/erikcorry/b25bdcacf3e0086f8a2afb688420678e>`__.

-------------

The following error occurred when I ran the `esp-idf/examples/protocols/https_mbedtls <https://github.com/espressif/esp-idf/blob/482a8fb2d78e3b58eb21b26da8a5bedf90623213/examples/protocols/https_mbedtls/main/https_mbedtls_example_main.c#L125>`_ example on ESP32 to connect to a TLS v1.3 server in the ESP-IDF v5.1.2 SDK. What could be the reason?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    .. code-block:: c

      E(53769) example: mbedtls_ssl_handshake returned -0x6c00
      I(53779) mbedtls: ssl_tls.c:355 Reallocating in_buf to 4429
      I(53779) mbedtls: ssl_tls.c:355 Reallocating in_buf to 16717
      E(53769) example: Last error was: -0x6c00 - SSL - Internal error (eg, unexpected failure in lower-level module)
   
  - TLS v1.3 is not yet supported on ESP-IDF v5.1.2. If you need to connect to a TLS v1.3 server, please test with the ESP-IDF v5.2-beta1 or later SDK. See: `esp_tls: add initial support for TLS 1.3 connection <https://github.com/espressif/esp-idf/commit/7fd1378fbb0b81231a83f91f8227f8fb083635a5>`_.
