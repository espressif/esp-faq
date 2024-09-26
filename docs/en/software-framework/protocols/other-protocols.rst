Other Protocols
===============

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

How to optimize communication latency for ESP32?
------------------------------------------------------------------------

  - It is recommended to turn off the sleep function for Wi-Fi by calling the API ``esp_wifi_set_ps(WIFI_PS_NONE)``.
  - You can also disable the ``AMPDU`` function in menuconfig.

--------------

Does ESP8285 support CCS (Cisco Compatible eXtensions)?
----------------------------------------------------------------------------

  No, it doesn't.

--------------

Does ESP32 support LoRa (Long Range Radio) communication?
--------------------------------------------------------------------------------

  No, the ESP32 itself does not have the LoRa protocol stack and the corresponding RF parts. However, to realize communication between Wi-Fi and LoRa devices, you can connect an external chip integrated with LoRa protocol to ESP32. In this way, ESP32 can be used as the master control MCU to connect the LoRa chip.

--------------

After calling ``esp_netif_t* wifiAP = esp_netif_create_default_wifi_ap()`` for ESP32-S2 chips, a following call of ``esp_netif_destroy(wifiAP)`` to deinit caused a 12-byte of memory leakage. What is the reason?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - It is necessary to call ``esp_wifi_clear_default_wifi_driver_and_handlers(wifiAP)`` before ``esp_netif_destroy(wifiAP)``. This is the correct deinit process. Following this process, there will be no memory leakage.
  - Alternatively, call ``esp_netif_destroy_default_wifi(wifiAP)``, which is supported by ESP-IDF v4.4 and later versions.

----------------

How to implement the certificate auto-download function?
----------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32:

  Please refer to `aws certificate automatic download function <https://docs.aws.amazon.com/iot/latest/developerguide/auto-register-device-cert.html>`_ .

-----------------------------

How to get more debug information based on errno in ESP-IDF?
--------------------------------------------------------------------------------------------------------------------------------

  - The errno list in ESP-IDF v3.x exists directly in the IDF. Click `errno.h <https://github.com/espressif/esp-idf/blob/release/v3.3/components/newlib/include/sys/errno.h>`_ to check it.
  - The ``errno.h`` for ESP-IDF v4.x is located under the compiler toolchain. For example, for esp-2020r3, the path of ``errno.h`` is ``/root/.espressif/tools/xtensa-esp32-elf/esp-2020r3-8.4.0/xtensa-esp32-elf/xtensa-esp32-elf/include/sys/errno.h``.

----------------

Does the ESP8266_RTOS_SDK support the TR-069 protocol?
-----------------------------------------------------------------------------------------------------------

  No.The ESP8266_RTOS_SDK itself does not provide native support for the TR-069 protocol, but you can implement TR-069 protocol stack according to your requirements and integrate it into the ESP8266_RTOS_SDK. You can also use third-party TR-069 protocol stacks for integration. In summary, ESP8266_RTOS_SDK can support the TR-069 protocol, but requires yourself to integrate and implement.

----------------

Does the ESP32 support SAVI?
-----------------------------------------------------------------------------------------------------------

  No, SAVI (Source Address Validation Improvements) is to establish a binding relationship based on IPv6 source address, source MAC address and access device port on the access device (AP or switch) by listening to control packets (such as ND, DHCPv6), i.e. CPS (Control Packet Snooping), and then perform source address validation on IP packets passing through the specified port. Only when the source address of the message matches with the binding table entry can it be forwarded to ensure the authenticity of the source address of data messages on the network. This is generally a policy protocol for switches or enterprise-class AP routers. Currently ESP32 supports IPv6 link-local address and global address for communication.

--------------------------------

When Ethernet and Wi-Fi coexist, does Ethernet take precedence over Wi-Fi in data transfer?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  :CHIP\: ESP32 :

  - Call `esp_netif_get_route_prio first <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/network/esp_netif.html#_CPPv424esp_netif_get_route_prioP11esp_netif_t>`_ to check the priority of Ethernet and Wi-Fi. If Wi-Fi takes priority over Ethernet, you can prioritize them by modifying ``route_prio`` in the structure ``esp_netif_t``.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

When using SNTP, I encountered the error “ assert failed: sntp setoperatingmode IDF/components/lwip/lwip/src/apps/sntp/sntp.c:724 (Operating mode must not be set while SNTP client is running)？". How can I solve this issue?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - You can solve it by adding the following code snippet to the sntp_init() interface:

  .. code-block:: c

      if(sntp_enabled()){
      sntp_stop(); 
      } 

----------------

Have the ESP modules been IPv6 certified?
-----------------------------------------------------------------------------------------------------------

 - Currently not.

----------------

Does the ESP module support the IPP protocol for printers?
-----------------------------------------------------------------------------------------------------------

 Currently not supported.

----------------

When ESP32 connects to an open hotspot that requires login authentication (such as CMCC), how to handle this situation?
---------------------------------------------------------------------------------------------------------------------------

  This type of hotspot typically uses the ``Captive Portal`` mechanism. When ESP32 connects to such a hotspot, the device will be redirected to a login page where the user needs to enter the mobile number and verification code for authentication. Currently, there is no ready-made solution to automate this authentication process. An alternative approach is to add the device to the whitelist on the router's management page, thus avoiding the need for authentication each time it connects.

----------------

What is the time interval for switching NTP servers when using the NTP function? Is there an interface to change the time of NTP switching?
-------------------------------------------------------------------------------------------------------------------------------------------

  After the first NTP server fails, the interval time starts to increase from 15 seconds and eventually stabilizes at about two and a half minutes. Currently, there is no interface to modify the switch time of the NTP server.

----------------

Why is the sign of the timezone in SNTP opposite to the actual situation? For example, the timezone in India is GMT+5:30, but in the code, it has to be written as GMT-5:30?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  This is the design of the standard time API. The plus or minus sign indicates the direction of the time zone offset relative to GMT, using the GMT offset to represent the local time zone.
