Wi-Fi
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

Do ESP32 and ESP8266 support Chinese SSID for Wi-Fi?
--------------------------------------------------------

  Yes, but the CODEC format of router or smart phone should be the same.

  For example, if both router and device use UTF-8 format, then the device can be successfully connected to the router with Chinese SSID.

--------------

Do Espressif's products support boundary scans?
-------------------------------------------------

  No, they don't.

--------------

What is the definition for Wi-Fi channel? Can I select any channel of my choice?
------------------------------------------------------------------------------------

  A channel refers to a specific frequency channel within the allowable range of frequencies allocated for use by Wi-Fi systems. Different countries and regions use different channel numbers. Please refer to `ESP8266 Wi-Fi Channel Selection Guidelines <https://www.espressif.com/sites/default/files/documentation/esp8266_wi-fi_channel_selection_guidelines_en.pdf>`_.

--------------

What is the default network segment for ESP8266 SoftAP?
-------------------------------------------------------------

  Why do I have problem connecting to router with IP 192.168.4.X in SoftAP + Station mode?

  - The network segment used by ESP8266 SoftAP is 192.168.4.\*, and its default IP address is 192.168.4.1. When connecting to router 192.168.4.X, errors may occur because the ESP8266 cannot distinguish if it should connect to the internal SoftAP or the external router.