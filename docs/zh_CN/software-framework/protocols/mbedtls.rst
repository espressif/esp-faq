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
--------------------------------------------------------

  ⽀持，目前 ESP8266 OpenSSL 是基于 Mbed TLS 封装的接口，Mbed TLS 支持 验证主机名。使用 ESP-TLS 可以根据配置切换 Mbed TLS 与 wolfSSL。

--------------

ESP32 使用 Mbed TLS 时如何优化内存？
-----------------------------------------------------------------------------

  - 可以在 menuconfig 里开启动态 buffer， 具体操作为 ``menuconfig -> Component config -> mbedTLS -> Using dynamic TX/RX buffer（键 "Y" 使能）``。
  - 同时可以使能上一步的 ``Using dynamic TX/RX buffer`` 里的子选项 ``Free SSL peer certificate after its usage`` 和 ``Free certificate, key and DHM data after its usage``。
