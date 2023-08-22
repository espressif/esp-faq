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

  - The error is caused by DNS request timeout.
  - You can enable DNS log with the debug level or capture wireless packets for further analysis.
  - To enable the debug level DNS log, you can add ``#define DNS_DEBUG LWIP_DBG_ON`` code to the ``esp-idf/components/lwip/lwip/src/include/lwip/opt.h`` file, and then enable the ``Component config`` > ``LWIP`` > ``Enable LWIP Debug`` configuration.
