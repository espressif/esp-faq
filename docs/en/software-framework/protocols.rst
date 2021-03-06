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

Does ESP8266 OpenSSL support Hostname validation?
-----------------------------------------------------------------------

  Yes. ESP8266 OpenSSL is based on mbedTLS encapsulation, which supports ``Hostname validation``. ESP-TLS can be used to switch between mbedTLS and wolfSSL.

--------------

Does ESP32 support PCI-E protocol?
-----------------------------------------------------

  No, it doesn't.

--------------

How to optimize communication latency for ESP32？
-----------------------------------------------------------------------

  - It is recommended to turn off the sleep function for Wi-Fi by calling the API ``esp_wifi_set_ps(WIFI_PS_NONE)``.
  - You can also disable the ``AMPDU`` function in menuconfig.

--------------

Does ESP8285 support CCS (Cisco Compatible eXtensions)?
-----------------------------------------------------------------------------

  No, it doesn't.

--------------

Does ESP8266 support HTTP hosting?
------------------------------------------------------

  Yes, it does. ESP8266 can run as a server in both SoftAP and Station modes.

  - When running as a server in SoftAP mode, clients can directly access the ESP8266 host or server at 192.168.4.1 (default) IP address.
  - When the server is accessed via a router, the IP address should be the one allocated to the ESP8266 by the router.
  - When using SDK to write native code, please refer to relevant examples.
  - When using AT commands, start a server using ``AT+CIPSERVER`` command.

--------------

Does ESP32 support LoRa (Long Range Radio) communication?
--------------------------------------------------------------------------------

  No, the ESP32 itself does not have the LoRa protocol stack and the corresponding RF parts. However, to realize communication between Wi-Fi and LoRa devices, you can connect an external chip integrated with LoRa protocol to ESP32. In this way, ESP32 can be used as the master control MCU to connect the LoRa chip.

--------------

How soon can the associated resources be released after the TCP connection is closed?
----------------------------------------------------------------------------------------------------------------

  The associated resources can be released in 20 seconds or can be specified by the sent linger/send_timeout parameter.

--------------

How to configure the server address so as to make it an autonomic cloud platform by using MQTT?
-----------------------------------------------------------------------------------------------------------------------------------------

  Please refer to `MQTT Examples <https://github.com/espressif/esp-idf/tree/master/examples/protocols/mqtt>`_.

--------------

With ESP32, are there any return instructions if I skip to a function using the ``jump`` instruction in ULP？
-----------------------------------------------------------------------------------------------------------------------------------------------

  Please see `here <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/ulp_instruction_set.html#add-add-to-register>`_ for ULP CPU instructions list and corresponding specifications. Normally, a general register is used for return instructions to store backup PC addresses for later jumping backs. Since there are only four general registers in ULP for now, please make proper use of them.

--------------

After the SNTP calibration for ESP8266 RTOS SDK v3.2, errors gradually increase. How to resolve such issue？
------------------------------------------------------------------------------------------------------------------------------------------------

  This is because the ESP8266 uses software timer, which brings large errors itself. You can improve it with the following solutions:

  - For branch v3.2, you can resynchronize time (300 s is recommended) from the server regularly by creating a task.
  - For branch release-v3.3, the code of system timer has been refactored and is tested with low errors. On the other hand, you can still synchronize time from the server regularly.
  - The master branch has inherited the refactored code from branch release-v3.3. In addition, you can configure the SNTP synchronization interval in menuconfig: ``Component config > LWIP > SNTP -> Request interval to update time (ms)``.

-----------------

Does ESP8266 support loop-back for device-end UDP broadcasts?
-----------------------------------------------------------------------------------------------------

  - Yes, it does.
  - Please enable the LOOPBACK option from LWIP in menuconfig: ``menuconfig -> Component config -> Enable per-interface loopback (type "Y" to enable)``.

--------------

What is the default packet length for TCP/IP?
-----------------------------------------------------------------

  In default configurations, the single packet TCP is 1460 bytes and UDP is 1472 bytes.

--------------

When using UTC and GMT methods in SNTP protocol, why can't I get the time of the target time zone？
---------------------------------------------------------------------------------------------------------------------------------------

  - The "TZ = UTC-8" refers to POSIX time, in which "UTC" is the abbreviation of any time zone and the number is the number of hours that the time zone is behind UTC.
  - "UTC-8" indicates a certain time zone, "UTC" for short, which is -8 hours later than the actual UTC. Therefore, "UTC+8" is 8 hours later than the actual UTC, and also 16 hours later than Beijing.

--------------

Is there any special firmware or SDK in ESP32 that can only provide AP/STA (TCP/IP bypass) without using its internal TCP/IP so as to give developers more permissions?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The software solution ESP-Dongle can fit your requirements. Please contact `Business Team <https://www.espressif.com/en/contact-us/sales-questions>`_ to sign NDA and then get related solutions.

--------------

Can I add any broadcast data I want to Android ESP-Touch (e.g., add a device ID so that ESP32 can receive this ID)?
------------------------------------------------------------------------------------------------------------------------------------------------------

  - No, the data content sent under the current ESP-Touch protocol is fixed and cannot be customized.
  - If you expect to send customized data, it is recommended to use Blufi, which is the networking protocol based on Bluetooth LE. Please refer to the following references for Blufi:

    - Android APP：https://github.com/EspressifApp/EspBlufiForAndroid.
    - iOS APP：https://github.com/EspressifApp/EspBlufiForiOS.

----------------

When testing RTOS-SDK mqtt/ssl_mutual_auth with ESP8266, the server connection failed. Why?
-------------------------------------------------------------------------------------------------------------------------------

  - The failure of SSL connection may due to insufficient memory of ESP8266.
  - Please use the Master version of ESP8266-RTOS-SDK to test this example, since it supports dynamic memory allocation in menuconfig so as to reduce the usage of memory peak. The specific action is:

    - menuconfig -> Component config -> mbadTLS -> (type “Y” to enable) Using dynamic TX /RX buffer -> (type “Y” to enable) Free SSL peer certificate after its usage -> (type “Y” to enable) Free certificate, key and DHM data after its usage.
