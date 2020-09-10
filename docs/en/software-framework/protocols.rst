Protocols
=========

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

Does ESP8266 openSSL support Hostname validation?
----------------------------------------------------

  Yes. ESP8266 openSSL is based on mbedTLS encapsulation, which supports Hostname validation. Use esp-tls to switch between mbedTLS and wolfSSL.

--------------

Does ESP8285 support CCS (Cisco Compatible eXtensions)?
----------------------------------------------------------

  No, it doesn't.