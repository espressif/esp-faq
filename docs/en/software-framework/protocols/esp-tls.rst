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
--------------------------------------------------------------------------------------------------------------------------------

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
  - ESP-IDF v5.0 and later no longer support SSL 3.0, TLS 1.0 and TLS 1.1, but only support TLS 1.2 and TLS 1.3.

--------------------------

Why does the "mbedtls_ssl_handshake returned -0x7200" error occur during the SSL handshake?
----------------------------------------------------------------------------------------------------

  - The 0x7200 error is caused by the following reasons:

    - MBEDTLS_SSL_IN_CONTENT_LEN is too small, generally less than the maximum 16 K
    - Insufficient memory
    - The server refuses the ESP connection and the sent SSL record is incomplete. You need to capture the packet and check it. For details, please refer to `Espressif Systems Wireshark User Guide <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/wireshark-user-guide.html#espressif-wireshark-user-guide>`__.

----------------

When accessing the MQTTS Broker using IP, the error ``MBEDTLS_ERR_X509_CERT_VERIFY_FAILED`` occurs, but communication can be successfully carried out under the same conditions in testing tools like MQTTX. What could be the reason?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The issue might be due to a mismatch in the CN field. This can be bypassed by setting the member variable `skip_cert_common_name_check <https://github.com/espressif/esp-mqtt/blob/e6afdb4025fe018ae0add44e3c45249ea1974774/include/mqtt_client.h#L260>`__ to True to skip the CN check.

----------------

How much memory is required for a stable TLS handshake on ESP32? How to solve the problem of insufficient memory during a TLS handshake?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  A TLS handshake typically requires 40-50 KB of free heap memory for temporary allocation during the handshake process. If memory fragmentation is excessive or available memory is insufficient, the handshake may fail. When memory is insufficient, it needs to be optimized. Please refer to `Minimizing RAM Usage <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/performance/ram-usage.html>`__. Additionally, if the module includes external PSRAM, ensure it is properly configured and utilized.

----------------

What do the error codes ``0x6900`` and ``0x7600`` represent during a TLS handshake?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ``0x6900 (MBEDTLS_ERR_SSL_WANT_READ)``: This usually indicates that the operation would be blocked because there is temporarily no data in the TCP receive buffer. It is not necessarily an error but rather a signal that more data needs to be received.
  - ``0x7600 (MBEDTLS_ERR_SSL_PRIVATE_KEY_REQUIRED)``: This indicates that the required private key or pre-shared key has not been set. For two-way authentication, please ensure that the client has configured the correct private key.

----------------

When implementing HTTPS on ESP32, how to resolve the issue that the server certificate chain is different from what is obtained by the PC browser?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Try enabling more detailed mbedtls debug information on ESP32 to obtain the certificate chain sent by the server during the TLS handshake process, and compare it with the certificate chain obtained from the browser.

----------------

How to resolve the issue of certificate parsing failure when using ESP32?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  First, you should check whether the certificate format complies with the X509 standard, and ensure that there are no issues with the certificate chain. In addition, enabling the log function of mbedtls can help diagnose the problem.
