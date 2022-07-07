ESP-TLS
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

--------------

When testing RTOS SDK ``mqtt/ssl_mutual_auth`` with ESP8266, the server connection failed. Why?
-------------------------------------------------------------------------------------------------------------------------------

  - The failure of SSL connection may due to insufficient memory of ESP8266.
  - Please use the master version of ESP8266-RTOS-SDK to test this example, since it supports dynamic memory allocation in menuconfig so as to reduce the usage of memory peak. The specific action is: menuconfig -> ``Component config`` -> ``mbedTLS`` -> (type “Y” to enable) ``Using dynamic TX /RX buffer`` -> (type “Y” to enable) ``Free SSL peer certificate after its usage`` -> (type “Y” to enable) ``Free certificate, key and DHM data after its usage``.

----------------

Can ESP HTTPS skip the server certificate check?
--------------------------------------------------------------------------------------------------------------------------------

  - Yes, if you enable the following options in menuconfig.

    - ``Menu path: (Top)`` -> ``Component config`` -> ``ESP-TLS`` -> ``Allow potentially insecure options``
    - ``Menu path: (Top)`` -> ``Component config`` -> ``ESP-TLS`` -> ``Allow potentially insecure options`` -> ``Skip server certificate verification by default``

  - Besides, make sure that the ``cert_pem`` member variable is not set in the ``esp_http_client_config_t`` structure. Otherwise, the server certificate will still be verified with this CA certificate.
  - If you want to test HTTP OTA at the same time, you need to enable the ``Menu path: (Top)`` -> ``Component config`` -> ``ESP HTTPS OTA`` -> ``Allow HTTP for OTA`` option in menuconfig.

----------------

How to set the ``esp_tls_conn_read`` API in ESP-TLS to non-blocking mode? Or is there any other way to implement non-blocking?
--------------------------------------------------------------------------------------------------------------------------------

  - You can set ``non_block`` to true in the ``esp_tls_cfg_t`` structure in ``esp_tls.h`` to achieve non-blocking.
  - Alternatively, you can call ``esp_transport_connect_async`` to achieve non-blocking.

----------------

What are the TLS versions supported by ESP-IDF?
-----------------------------------------------------------------------------------------------------------

  - The recommended TLS protocol in ESP-IDF is the Mbed TLS protocol.
  - The TLS versions currently supported by ESP-IDF are TLS1.0, TLS1.1 and TLS1.2.
