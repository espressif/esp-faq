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

--------------

Does ESP8266 support HTTP hosting?
-------------------------------------

  Yes, it does. ESP8266 can run as a server in both SoftAP and Station modes.

  - When running as a server in SoftAP mode, clients can directly access the ESP8266 host or server at 192.168.4.1 (default) IP address.
  - When the server is accessed via a router, the IP address should be the one allocated to the ESP8266 by the router.
  - When using SDK to write native code, please refer to relevant examples.
  - When using AT commands, start a server using AT+CIPSERVER command.

--------------

How soon can the associated resources be released after the TCP connection is closed?
---------------------------------------------------------------------------------------

  The associated resources can be released in 20 seconds or can be specified by the sent linger/send_timeout parameter.

