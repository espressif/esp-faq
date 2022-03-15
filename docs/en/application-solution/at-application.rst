AT
==

:link_to_translation:`zh_CN:[中文]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

This document lists some frequently asked questions on ESP-AT. For more FAQ, please go to `ESP-AT User Guide <https://docs.espressif.com/projects/esp-at/en/latest/faq.html>`_.

--------------

How to download redirected resources via ESP8266 AT firmware?
----------------------------------------------------------------------

- ESP8266 AT HTTP command does not support redirection. After getting the status code 301 (permanent redirection) or 302 (temporary redirection) returned by the server, it will not automatically redirect to the new URL address.
- You can use wireshark or postman to get the actual URL, and then access it through HTTP commands.

  - Please note that ESP8266-IDF-AT_V2.1.0.0 cannot support HTTP command by default, you need to compile AT firmware based on esp-at, please refer to `ESP8266 platform <https://docs.espressif.com/projects/esp-at/en/latest/Compile_and_Develop/How_to_clone_project_and_compile_it.html#esp8266-platform>`_. HTTP needs to be enabled in menuconfig: ``menuconfig`` -> ``Component config`` -> ``AT`` -> ``[*] AT http command support``. 

  - The maximum length of the parameter ``URL`` in ``AT+HTTPCLIENT`` is 256. When the length of the actual URL obtained exceeds 256, it will return ``ERROR``. You can use TCP related commands to send the a constructed HTTP request message to obtain the resource.

----------------

Using ESP8266 v2.1.0.0 version AT firmware, how to disable the default power save mode?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The default power save mode can be disable via the `AT+SLEEP=0 <https://docs.espressif.com/projects/esp-at/en/release-v2.1.0.0_esp8266/AT_Command_Set/Basic_AT_Commands.html?highlight=sleep#at-sleepsets-the -sleep-mode>`_.

--------------------

Received the following log after sending an AT command. What is the reason?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    busy p...
    OK

  - Please check whether there are redundant spaces or line breaks in your AT commands, e.g., extra CR and LF. You can also take data from the communication line to see what could be wrong.
  - For more information, please refer to `AT Command Types <https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/index.html#id5>`_.

---------------

What is the maximum value of the parameter `length` of AT+BLEGATTSNTFY and AT+BLEGATTSIND?
----------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32:

  - The maximum value of `length` is MTU - 3, and the MTU can support up to 517 bytes, so the maximum value of `length` is 514 bytes.

----------------

How to enable full calibration mode for ESP8266 NONOS AT firmware?
---------------------------------------------------------------------------------------------------------------------------------

  - The NONOS AT firmware uses partial calibration by default, and full calibration can be enabled in the following way:
  
    modify file ``esp_init_data_default_v08.bin``, byte[114] = 3 (for partial calibration, byte[114] = 1, while for full calibration, byte[114] = 3).

---------------

What is the maximum rate of ESP32 AT BLE UART transparent transmission? 
-----------------------------------------------------------------------------

  - In an open office environment, when the serial port baud rate is 2000000: the average transmission rate of ESPAT BT is 0.56 Mb, and the average transmission rate of ESPAT BLE is 0.101 Mb.
  - In shielding box environment, the data will also be provided after the test finished in the future.
  
---------------

How to get the AT firmware of the ESP32-MINI-1 (ESP32-U4WDH inside) module?
--------------------------------------------------------------------------------------------------------------------------------

  - Please refer to `How_to_download_the_latest_temporary_version_of_AT_from_github <https://docs.espressif.com/projects/esp-at/en/latest/Compile_and_Develop/How_to_download_the_latest_temporary_version_of_AT_from_github.html>`_.

-----------------------------------------------------------------------------------------------------

How to set ADV broadcast parameters after it exceeds 32 bytes?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32 :

  - The AT+BLEADVDATA <https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/BLE_AT_Commands.html#esp32-only-at-bleadvdata-set-bluetooth-le-advertising-data>_ command supports up to 32 bytes of ADV broadcast parameters. If you need to set a bigger parameter, please use command AT+BLESCANRSPDATA <https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/BLE_AT_Commands.html#esp32-only-at-blescanrspdata-set-bluetooth-le-scan-response>.

--------------------------------------------------------------------------

Does AT support Wi-Fi roaming function?
---------------------------------------------------------------------------------------------
  :CHIP\: ESP32|ESP32-S2|ESP32-C3 

  - Not supported.

----------------

When using ESP-AT to send TCP data, sometimes the data is messy/partially lost. What should I do?
--------------------------------------------------------------------------------------------------------------------

  - It is recommended to add hardware flow control or software flow control:

    - `Hardware flow control <https://docs.espressif.com/projects/esp-at/en/latest/Get_Started/Hardware_connection.html#id1>`_: CTS and RTS signals
    - `Software flow control <https://docs.espressif.com/projects/esp-idf/en/release-v4.1/api-reference/peripherals/uart.html>`_

  - If necessary, you can add some logic to handle errors in the code. For example, when your device accidentally entered the transparent transmission mode, or there is error transmission in the transparent transmission mode, send +++ in time to exit the transparent transmission, and resend the AT+CIPSEND command.

---------------------------

When ESP32 performs BLE OTA, it connects to phone via BLE and connects to MCU via UART, then performs OTA to MCU. But the data transmission between ESP32 and MCU is low even after increasing MCU via phone. Where should I check for such issue?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The reason may be that ESP32 and the mobile phone did not set the MTU successfully, or the UART limitation of ESP32 and MCU communication. Therefore, it is recommended to check/improve from the following points:

    - Connection between ESP32 and mobile phone

      1. Only the BLE client supports setting the GATT MTU length, and the BLE connection needs to be established before the MTU length is set. The final actual MTU length needs to be negotiated. If it returns OK, it only means the negotiation process is triggered. Therefore, the length you set before may not be valid. It is recommended to use the query command AT+BLECFGMTU? to check the actual MTU length after setting.
      2. Use BLE SPP, the BLE transparent transmission mode, to increase the transmission rate.
      
    - Connection between ESP32 and MCU: increase the baud rate of UART appropriately to increase the transmission rate.

----------------------

When using ESP32-C3 as a Server with AT firmware version v2.2.0.0, what is the maximum number of connections allowed by the AT+CIPSERVERMAXCONN command?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The maximum number of connections allowed to be established by the `AT+CIPSERVERMAXCONN <https://docs.espressif.com/projects/esp-at/en/release-v2.2.0.0_esp32c3/AT_Command_Set/TCP-IP_AT_Commands.html?highlight=CIPSERVERMAXCONN#at-cipservermaxconn-query-set-the-maximum-connections-allowed-by-a-server>`_ command is 5 by default.
  - You can configure the "menuconfig -> Component config -> AT -> Socket Maximum Connection" parameter to allow more connections.
  - If you need to support more than 10 connections, you also need to increase the "menuconfig -> Component config -> LWIP -> Max number of open sockets" (default is 10) configuration.
  - However, the maximum number of connections allowed during actual operation depends on the remaining available memory of the chip. When no more connections can be established, it is recommended to use the `AT+SYSRAM <https://docs.espressif.com/projects/esp-at/en/release-v2.2.0.0_esp32c3/AT_Command_Set/Basic_AT_Commands.html?highlight=sysram#at-sysram-query-current-remaining-heap-size-and-minimum-heap-size>`_ command to query the current remaining available memory.

------------------

When using the release/v2.1.0.0 version of the AT firmware, what is the maximum number of BLE devices that ESP32 supports to save binding and paring information for?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Up to 15 BLE devices.
  
-----------------------------------------------------------------------------------------------------

The maximum length of AT+BLEADVDATA broadcast data is 31. How to realize a bigger data length support?
---------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32:

 - You can put the data in BLE scan response by using the `AT+BLESCANRSPDATA <https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/BLE_AT_Commands.html#esp32-only-at-blescanrspdata-set-bluetooth-le-scan-response>_` command.

-----------------------------------------------------------------------------------------------------

What authentication methods does WPA2 Enteprise support?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP8266 | ESP32 | ESP32-C3:

  - Only EAP-TLS/EAP-PEAP/EAP-TTLS are supported. For details, please refer to the `AT+CWJEAP <https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#esp32-only-at-cwjeap-connect-to-a-wpa2-enterprise-ap>_` command introduction.

---------------

Are there any AT+HTTPCPOST usage examples?
--------------------------------------------------------------------------------------------------

  :CHIP\: ESP8266:

  - While compiling firmware manually under the master version of ESP-AT, it is required to change the "at process task stack size" to over 4096 in menuconfig, the specific operation steps are as follows:
  
    - ./build.py menuconfig----->AT----->(5120). The stack size of the AT process task in AT library, which will be used to process AT command.
  - [*] AT http command support:
    .. code:: text
 
      AT+CWMODE=1     //set as station mode
      OK
      AT+CWJAP="iot","123456789"
      WIFI CONNECTED
      WIFI GOT IP
      AT+HTTPCPOST="http://61.172.47.198:8082/hello/test",172
      OK
      >AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
      AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
      AAAAAAAAAAAAAAAAAAAAA
      SEND OK 

---------------

Are there any examples of using AT+CIPRECVDATA to receive cache data from the server?
--------------------------------------------------------------------------------------------------

  :CHIP\: ESP8266:

    .. code:: text

      AT+CWMODE=1     //set as station mode
      OK
      AT+CWJAP="iot","123456789"
      WIFI CONNECTED
      WIFI GOT IP
      AT+CIPSTART="TCP","192.168.3.129",8080
      CONNECT
      OK
      AT+CIPRECVMODE=1
      OK
      //The server send 16bytes data to client
      AT+CIPRECVLEN?    //Inquire server cached data
      +CIPRECVLEN:16    //Ensure the quire length isn't zero, otherwise the data received will return ERROR.
      AT+CIPRECVDATA=1080
      +CIPRECVDATA:16,http://en.usr.cn
      OK

---------------

I use ESP32 AT firmware to send BLE scan command, but the scan response packet is not received. What is the reason?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The AT commands used are as follows:

  .. code:: text

    AT+BLEINIT=1
    AT+BLESCANPARAM=0,0,0,100,50
    AT+BLESCAN=1

  There is a broadcast packet, but there is no scan response packet; the log of the command reply is shown in the figure:

  .. figure:: ../_static/application-solution/at-application/AT_BLESCAN_Return_LOG.png
    :align: center
  
---------------

Is there a limit to the maximum length of the broadcast packet sent by the "AT+BLEADVDATA" command?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The maximum length of broadcast packet by "AT+BLEADVDATA" is 31 bytes.
  
--------------------------------

What is the maximum value of the ``length`` parameter in the AT+BLEGATTCWR command?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    - The maximum value of ``length`` in the `AT+BLEGATTCWR <https://docs.espressif.com/projects/esp-at/en/release-v2.2.0.0_esp32/AT_Command_Set/BLE_AT_Commands.html?highlight=BLEGATTCWR#esp32-only-at-blegattcwr-gattc-writes-characteristics>`_ command is corresponds to the ``val_max_len`` parameter setting under the `example.csv <https://github.com/espressif/esp-at/blob/release/v2.2.0.0_esp32/components/customized_partitions/raw_data/ble_data/example.csv>`_ file, and it is recommended not to exceed 512. Please refer to the description in `README <https://github.com/espressif/esp-at/blob/release/v2.2.0.0_esp32/tools/README.md>`_.
    
--------------------

When using the v2.2.0.0 version of AT firmware to connect ESP32 to AP, it will automatically connect to the AP again after being reset and powered on. How to cancel this setting?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - This can be realized by using the AT+SYSSTORE=0 command. After calling this command, the related configuration information of affected commands will not be saved to flash. That is to say, before connecting AP using the AT+CWJAP command, you can call `AT+SYSSTORE=0 <https://docs.espressif.com/projects/esp-at/en/release-v2.2.0.0_esp32/AT_Command_Set/Basic_AT_Commands.html#at-sysstore-query-set-parameter-store-mode>`_ first to make old AP information not be stored to flash.
  
----------------

Does ESP32-AT supports PPP?
----------------------------------------------------------------------

  - Not supported, please reffer `pppos_client <https://github.com/espressif/esp-idf/tree/master/examples/protocols/pppos_client/>`_ demos for your own implementation.

----------------

How to enable Wi-Fi Debug for AT?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  :CHIP\: ESP8266 | ESP32 | ESP32-C3 | ESP32-S2:

  - Enable log level: ``. /build.py menuconfig -> Component Config -> Log output -> Default log verbosity`` set to Verbose.
  - Enable Wi-Fi debug: ``. /build.py menuconfig-> Component config -> Wi-Fi -> Enable WiFi debug log -> Wi-Fi debug log level (Wi-Fi Debug log Verbose)``.

---------------

Where should I pay attention to when updating certificates using the AT+SYSFLASH command?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The certificate length must be 4-byte aligned.
  - The certificate bin needs to be generated via tools/AtPKI.py, please refer to the example in `esp-at/tools/READ.md <https://github.com/espressif/esp-at/blob/master/tools/README.md>`__. For instance:
  
    python AtPKI.py generate_bin -b mqtt_cert_v2.bin cert mqtt_client.crt

---------------

What's the default type of content-type in AT+HTTPCPOST command ?
--------------------------------------------------------------------------------------------------

  :CHIP\: ESP8266 | ESP32 | ESP32-S2 | ESP32-C3:

  - The default type is application/x-www-form-urlencoded.

---------------

Is there a length limit on data sent with the AT+HTTPCLIENT command?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - yes, the total length of data set with this command can not exceed 256 bytes. This is due to the data is stored in command parameters. If you are going to send data with bigger length, it is recommended to configure via the `AT+HTTPCPOST <https://docs.espressif.com/projects/esp-at/zh_CN/latest/AT_Command_Set/HTTP_AT_Commands.html#at-httpcpost-post- http>`_ command, or use the TCP command to emulate Http to send data.

---------------

What TLS versions are supported by AT?
--------------------------------------------------------------------------------------------------------------------------------

  - TLS 1.0, TLS 1.1, TLS 1.2 are supported, the exact version numbers can be found in ``menuconfig-->Component config-->mbedTLS``.

---------------

How do I store the BLE name in Flash?
--------------------------------------------------------------------------------------------------------------------------------

  - The following command can be called.

   ::

    AT+SYSTORE=1            //Enable set to flash 
    AT+BLEINIT=2            //Set to BLE server mode
    AT+BLENAME?             //Query the default BLE name?
    AT+BLENAME="ESP-123"    //set new BLE nmae  
    AT+RST                  //reboot module    
    AT+BLEINIT=2            //Set to BLE server mode
    AT+BLENAME?             //Check if the BLE name is set successfully

------------------------

How to enable the notify and indicate functions with BLE client ?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The characteristics of BLE are not only read and write, but also notify and indicate, both of which are ways for the server to send data to the client. However, in order to send data successfully, the client needs to register notification in advance, i.e. write the value of CCCD.
  - If you want to enable notify, you need to write 0x01; if you want to enable indicate, you need to write 0x02 (write the 0x2902 descriptor); if you want to enable both notify and indicate, you need to write 0X03.
  - For example, in ESP-AT default service, notify can be enabled via 0xC305 and indicate can be enabled via 0xC306, so we write the 0x2902 descriptor under each characteristics:

   ::

    AT+BLEGATTCWR=0,3,6,1,2>     //Enables setting to flash
    // write 0x01         
    OK           
    // server+WRITE:0,1,6,1,2,<0x01>,<0x00> 
    AT+BLEGATTCWR=0,3,7,1,2>      
    // write 0x02
    OK
    // server+WRITE:0,1,6,1,2,<0x02>,<0x00>
    Writing ccc is a prerequisite for the server to be able to send notify and indicate

--------------

When an ESP32 serves as a slave, how to define MQTT data in json format on MCU side, e.g., and how to escape the strings?
--------------------------------------------------------------------------------------------------------------------------------------------------------

  - The original command: AT+MQTTPUB=0, "topic","{\"timestamp\":\"20201121085253\"}",1,0. When the MCU side sends the command, some characters need to be escaped, especially the "\" character, for example:

    .. code:: text

      sendData(TX_TASK_TAG, "AT+MQTTPUB=0,\"topic\",\"{\\\\"timestamp\\\":\\\\"20201121085253\\\\\"}\",1,0\r")     //MCU side definition

-------------------

For ESP8266-NONOS version of AT firmware, which AT serial port is used by default?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - For ESP8266-NONOS (V2.0 previous versions), the AT serial port used by default is UART0.