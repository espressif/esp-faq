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
