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

--------------

How to test and optimize the throughput of ESP32 AT?
----------------------------------------------------

  - Many factors are affecting the AT throughput test. It is recommended to use the iperf example in esp-idf for testing. While testing, please use the passthrough mode, adjust the data length to 1460 bytes, and send data continuously.
  - If the test rate does not meet your requirements, you can increase it by modifying the menuconfig iperf parameter in esp-idf and compiling your esp-at project.

--------------

How long does it take for the ESP32 AT to connect to Wi-Fi?
------------------------------------------------------------

  How long does it take for ESP32 AT (firmware release/v2.0.0.0) to connect to Wi-Fi after firmware initialization, or module startup? 

  In an office scenario, the connection time is 11 s. However, in actual practice, Wi-Fi connection time depends on the router performance, network environment, module antenna performance, etc.

--------------

Why does AT prompt "busy"?
-------------------------------------------

  - The “busy” prompt indicates that the previous command is being executed, and the system cannot respond to the current input. The processing mechanism of the AT commands is serial, i.e. one command at a time. 
  - Any input through serial ports is considered to be a command input, so the system will also prompt “busy” or “ERROR” when there is any extra invisible character input.

  For example:

  - If you enter AT+GMR (line break CR LF) + (space) through serial ports, the system will execute AT+GMR (line break CR LF) immediately, because the it is already considered to be a complete AT command. The space following the AT+GMR command will be treated as a second command. 
  - If AT+GMR has not been processed by the time of receiving the space, the system will prompt “busy”. 
  - However, if AT+GMR has been processed, the system will prompt “ERROR”, since the space is an incorrect command.

--------------

Is it possible to change the TCP send window size in AT firmware?
-----------------------------------------------------------------

  - Currently, it cannot be changed by commands, but you can compile the esp-at code to generate a new firmware.
  - You can reconfigure the menuconfig parameter: Component config -> LWIP -> TCP -> Default send buffer size.

--------------

Where can I get all the resources related to ESP32 AT?
--------------------------------------------------------

  - ESP32 AT bin files: https://www.espressif.com/en/support/download/at.
  - Documentation: `ESP-AT User Guide <https://docs.espressif.com/projects/esp-at/en/latest/index.html>`_.
  - You can develop more AT commands based on the Espressif's official `esp-at <https://github.com/espressif/esp-at>`_ project.

--------------

Why is there a "no module named yaml" error when I am compiling the ESP32 AT?
------------------------------------------------------------------------------

  Please install the yaml module by using ``python -m pip install pyyaml``.

--------------

Does the default AT firmware for ESP32 modules support Bluetooth functionality?
-------------------------------------------------------------------------------

  - For the ESP32-WROOM series of modules, the default AT firmware does not support Classic Bluetooth AT commands, but you can enable this functionality in menuconfig (Component config -> AT -> [*] AT bt command support) and compile your firmware based on the esp-at project.
  - For the ESP32-WROVER series of modules, the default AT firmware support Classic Bluetooth AT commands.

--------------

Does the ESP8266 AT support PSK authentication in SSL connections? 
------------------------------------------------------------------

  Supported in IDF-based AT, but not in ESP8266_NONOS_SDK-based AT. 

  - `AT firmware <https://www.espressif.com/en/support/download/at>`_.
  - ESP8266_NONOS_SDK-based AT: `ESP8266 AT Instruction Set <https://www.espressif.com/sites/default/files/documentation/4a-esp8266_at_instruction_set_en.pdf>`_.
  - IDF-based AT: `RTOS AT Command Set <https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/index.html>`_.

--------------

Can the serial port baudrate be modified in AT Commands? (Default: 115200)
--------------------------------------------------------------------------

  Yes, you can use either of the two ways below to modify it: 

  - Use the command ``AT+UART_CUR`` or ``AT+UART_DEF``. See `AT Instructions <https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/index.html>`_ for more information.
  - Re-compile the AT firmware: `establish the compiling environment <https://docs.espressif.com/projects/esp-at/en/latest/Compile_and_Develop/How_to_clone_project_and_compile_it.html>`_ and `change the UART baudrate <https://docs.espressif.com/projects/esp-at/en/latest/Compile_and_Develop/How_to_set_AT_port_pin.html>`_.

--------------

How does ESP8266 establish an SSL connection using AT commands?
------------------------------------------------------------------

  - Please refer to the following commands to establish an SSL connection between ESP8266 and a server:

  .. code:: text

    AT+CWMODE=1                                  // set Wi-Fi mode to station
    AT+CWJAP="espressif_2.4G","espressif"        // connect to AP, enter ssid and password   
    AT+CIPMUX=0                                  // enable the single connection mode    
    AT+CIPSTART="SSL","www.baidu.com",443        // establish an SSL connection

--------------

How do I specify the TLS protocol version for ESP32 AT?
-------------------------------------------------------

  When compiling the esp-at project, you can disable the unwanted versions in the menuconfig -> Component config -> mbedTLS.

--------------

What interfaces of ESP chips can be used to transmit AT commands?
------------------------------------------------------------------

  ESP8266, ESP32, ESP32-S2 can transmit AT commands through SDIO, SPI, and UART. You can configure it in menuconfig -> Component config -> AT when compiling the esp-at project.

--------------

How does the ESP32 AT communicate through the UART0 port?
---------------------------------------------------------

  The default AT firmware communicates through the UART1 port. If you want to communicate through UART0, please download and compile the esp-at project.

  - Refer to `How to clone and compile a project <https://docs.espressif.com/projects/esp-at/en/latest/Compile_and_Develop/How_to_clone_project_and_compile_it.html#esp32-esp32-s2-and-esp32-c3-series>`_ to set up the compiling environment;
  - Modify the module's UART pins in your `factory_param_data.csv <https://github.com/espressif/esp-at/blob/master/components/customized_partitions/raw_data/factory_param/factory_param_data.csv>`_, i.e. change uart_tx_pin to GPIO1，and uart_tx_pin to GPIO3;
  - Configure your esp-at project: make menuconfig > Component config > Common ESP-related > UART for console output(Custom) > Uart peripheral to use for console output(0-1)(UART1) > (1)UART TX on GPIO# (NEW) > (3)UART TX on GPIO# (NEW).

--------------

How to wake up ESP8266 from Light-sleep mode using AT commands?
----------------------------------------------------------------

  Please refer to the command `AT+SLEEPWKCFG <https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-wkcfg>`_.

--------------

How to use AT commands to establish the Bluetooth LE passthrough between ESP32-SOLO-1C and a cell phone?
---------------------------------------------------------------------------------------------------------

  - Configure ESP32-SOLO-1C as the Bluetooth LE passthrough server. See `Bluetooth LE AT Examples <https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Examples/BLE_AT_Examples.html#exam-UARTBLE>`_ for detailed steps.
  - Download a Bluetooth LE test tool in your cell phone, such as nRF Connect (Android) and lightblue (iOS), then open SCAN to find the MAC address of the ESP device, and finally you can send commands.

--------------

My ESP8266 uses the compiled ESP-AT firmware and needs the OTA function. How much flash size is needed?
--------------------------------------------------------------------------------------------------------

  The ESP-AT firmware needs at least 2 MB (16 Mbit) of flash if OTA function is required, and at least 1 MB (8 Mbit) of flash if the OTA function is not required.

--------------

How to enable the MDNS function using AT commands?
--------------------------------------------------

  Use the ``AT+MDNS`` command to enable the MDNS function.

  .. code-block:: text

    AT+CWMODE=1                            // set the device to station mode
    AT+CWJAP="ssid","password"             // connect to an AP, enter ssid and password
    AT+MDNS=1,"esp"," *pos.* tcp.",3030    // enable MDNS
    AT+MDNS=0                              // disable MDNS

--------------

Does esp-at firmware support MQTT?
----------------------------------

  - ESP8266 firmware supports MQTT in v2.1.0.0-rc1 and later versions.
  - ESP32 firmware supports MQTT in v2.0.0.0 and later versions.
  - See `release notes <https://github.com/espressif/esp-at/releases>`_ for more details.

--------------

After MCU sends AT+CIPSEND, it receives the busy p... response. Does the MCU need to resend the data?
-------------------------------------------------------------------------------------------------------

  busy p.. means the previous command is being executed and the current input is invalid. It is recommended to wait for the response of the previous command before resending AT+CIPSEND.

--------------

Does ESP-WIFI-MESH support AT commands?
---------------------------------------------------

  Currently ESP-WIFI-MESH does not support AT commands.

--------------

How does ESP32 enable the BluFi functionality in AT?
----------------------------------------------------

  - The default AT firmware does not support the BluFi function, but you can enable it by compiling the esp-at code to generate a new firmware.
  - When compiling, enable the BluFi functionality in menuconfig: make menuconfig--->Component config--->AT--->[*]AT blufi command support.

--------------

How to get the default firmware version in modules or development boards?
-------------------------------------------------------------------------

  - The factory firmware varies from modules to modules, or boards to boards. You can ask your purchaser to consult Espressif's Business Support.
  - If the module is shipped with AT firmware, you can use the command AT+GMR to check the version information.

--------------

Are there any examples of using AT commands to connect to aliyun or Tencent Cloud?
----------------------------------------------------------------------------------

  - Download and flash `AT fimware <https://docs.espressif.com/projects/esp-at/en/latest/AT_Binary_Lists/index.html>`_.
  - Aliyun: `AT+MQTT aliyun <https://blog.csdn.net/espressif/article/details/107367189>`_.
  - Tencent Cloud: `AT+MQTT cloud <https://blog.csdn.net/espressif/article/details/104714464>`_.

--------------

Does AT firmware support SSL certificate authentication?
---------------------------------------------------------

  - Yes, please refer to `SSL certification commands <https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-SSLCCONF>`_ for more information.
  - For how to generate the SSL certificate bin, please refer to `esp-at/tools/README.md <https://github.com/espressif/esp-at/tree/release/v2.1.0.0_esp8266/tools>`_.
  - The flash address of the SSL certificate is determined by at_customize.csv.

--------------

Does AT support websocket commands?
------------------------------------

  - Not supported in the default firmware.
  - It can be implemented by custom commands. See `websocket <https://github.com/espressif/esp-idf/tree/master/examples/protocols/websocket>`_ and `How_to_add_user-defined_AT_commands <https://docs.espressif.com/projects/esp-at/en/latest/Compile_and_Develop/How_to_add_user-defined_AT_commands.html>`_ for more information.

--------------

Does the AT firmware shipped in modules support flow control?
----------------------------------------------------------------

  - Hardware flow control is supported, but software flow control not.

--------------

How to modify the number of TCP connections in AT? 
--------------------------------------------------

  - The ESP32 AT supports a maximum of 16 TCP connections, which can be configured in menuconfig as follows:
    
    - make menuconfig---> Component config---> AT--->  (16)AT socket maximum connection number
    - make menuconfig---> LWIP---> (16)Max number of open sockets

  - The ESP8266 AT supports a maximum of 5 TCP connections, which can be configured in menuconfig as follows:
    
    - make menuconfig---> Component config---> AT--->  (5)AT socket maximum connection number
    - make menuconfig---> LWIP---> (10)Max number of open sockets

--------------

How to view the error log of AT firmware?
------------------------------------------

  - For ESP32, the error log is output through the download port. By default, UART0 is GPIO1 and GPIO3.
  - For ESP8266, it is output from UART1 TX, which is GPIO2 by default.
  - See `AT Hardware Connection <https://docs.espressif.com/projects/esp-at/en/latest/Get_Started/Hardware_connection.html>`_ for more details.

--------------

How to OTA upgrade AT firmware?
---------------------------------

- You can use the following AT commands to do it:

  .. code-block:: text

    AT+CWMODE=1
    AT+CWJAP_DEF="ssid","password"
    AT+CIUPDATE

--------------

How does the ESP32 module use AT commands to implement encrypted Bluetooth pairing?
--------------------------------------------------------------------------------------

  - The commands to encrypt Bluetooth pairing are as follows:

  .. code-block:: text

    AT+RST                          // restart the module
    AT+GMR                          // check the module version information
    AT+BLEINIT=2                    // initialize the module as a server
    AT+BLEGATTSSRVCRE               // GATTS creates services
    AT+BLEGATTSSRVSTART             // GATTS start services
    AT+BLEADDR?                     // query the public address of the Bluetooth LE device
    AT+BLEADVPARAM=50,50,0,0,4      // set Bluetooth LE advertising parameters
    AT+BLEADVDATA="020120"          // set Bluetooth LE advertising data
    AT+BLESECPARAM=4,1,8,3,3        // set encrypted parameters         
    AT+BLEADVSTART                  // start the Bluetooth LE advertising
    AT+BLEENC=0,3                   // After connecting without a secret key, use this command to generate an encrypted connection request and an encryption key

---------------

What is the default Wi-Fi name of the AP after the ESP-AT firmware is downloaded to the ESP32?
------------------------------------------------------------------------------------------------

  - You can use the AT+CWJAP? command to query the default Wi-Fi name. By default, the MAC address is appended to Wi-Fi names.
  - AT supports custom Wi-Fi names, which can be set with the following AT commands:

  .. code-block:: text

     AT+CWMODE=1                            // set the current device to the softAP mode
     AT+CWSAP="SSID","PASSWORD",1,0,4,0     // set softAP parameters
     AT+CWSAP?                              // query the softAP parameters you just set

---------------

How to use the SPI interface for AT communication?
---------------------------------------------------

  - The AT firmware provided by Espressif uses UART for communication by default. If you need to use SPI for communication, please configure and compile your own esp-at project. See `Compile and develop <https://docs.espressif.com/projects/esp-at/en/latest/Compile_and_Develop/index.html>`_ for more information.

--------------

Does the command AT+CWLAP perform an active scan or passive scan in the old version of ESP8266 AT firmware (SDK v1.5.4)?
--------------------------------------------------------------------------------------------------------------------------

  - The AT firmware that is based on ESP8266_NonOS_SDK v2.2.0 is of version 1.6.2. It supports active scan (default) and passive scan. AT firmware before this version only supports active scan.

--------------

How to use AT commands to change the default IP address of the softAP?
-----------------------------------------------------------------------

  - Taking V2.0 and later versions of ESP-AT firmware as an example, the IP address of the softAP can be modified with the following commands:

  .. code-block:: text

    AT+CWMODE=2    // set the current device to softAP mode
    AT+CIFSR       // query the IP address of the current device's AP
    AT+CIPAP="192.168.1.1","192.168.1.1","255.255.255.0"  // set the current softAP's IP address
    AT+CIFSR                                              // check the newly set softAP's IP address
    
--------------

What is the default Bluetooth name for the ESP32 AT firmware?
-----------------------------------------------------------------

  - The default BLE_NAME for AT firmware is BLE_AT.
  - You can use the `AT+BLENAME?` command to query the default Bluetooth name.

--------------

How to set the keepalive parameter using the AT+CIPSTART command?
-----------------------------------------------------------------

  - Example: AT+CIPSTART="TCP","192.168.1.*",2500,60

--------------

The at_http_webserver example keeps restarting. How to fix it?
---------------------------------------------------------------

  This `issue <https://github.com/espressif/esp-at/commit/94f5781033b7dd44b9f5bf5882d4599fc5efea27>`_ has been fixed on the master branch. Please rebase the latest master branch. Or, you can update to ``CONFIG_SPI_FLASH_USE_LEGACY_IMPL=y`` in the sdksonfig configuration to fix the crash.

--------------

Is it possible to set the ESP32-WROOM-32 module to HID keyboard mode with AT commands?
-------------------------------------------------------------------------------------------

  Yes, please refer to `Bluetooth LE AT Commands <https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/BLE_AT_Commands.html#esp32-only-at-blehidinit-bluetooth-le-hid>`_.

--------------

How does ESP-AT perform the BQB certification?
-----------------------------------------------

  - Please refer to `Updates to multiple BQB Bluetooth certification options of ESP32 <https://mp.weixin.qq.com/s?__biz=MzA4Nzc5MjkwNw==&mid=2651783810&idx=1&sn=fb0e132af240606d8178347966721542&chksm=8bcfaee6bcb827f03992aa200a2eb2baef5114712a4001da0c8282502a9183f5379605412cea&mpshare=1&scene=1&srcid=0920VLpOLubCew48DrCRdjCT&sharer_sharetime=1583218643838&sharer_shareid=1a1137fefea7b87a843519e48151f9a4&rd2werd=1#wechat_redirect>`_ and `ESP module certificates <https://www.espressif.com/en/support/documents/certificates>`_.

----------------

I am new to ESP-AT firmware. Which AT firmware version shall I choose for ESP8266, NONOS or RTOS？
----------------------------------------------------------------------------------------------------

  -  It is recommended to use the RTOS version, which is being actively maintained now. NONOS is an older AT version.
  -  The two versions are quite different in terms of logic. Besides, RTOS supports more features and fixes the bugs that exist in NONOS version. RTOS version is now and will be our focus in the long run. We will fix bugs more timely and constantly add new features in this version.
  -  Please download RTOS `AT bin <https://docs.espressif.com/projects/esp-at/en/latest/AT_Binary_Lists/ESP8266_AT_binaries.html/>`_.

----------------

Is it possible to set the Bluetooth LE TX for ESP-AT?
-----------------------------------------------------

  - Yes, ESP32 shares an antenna for Wi-Fi and Bluetooth LE. See `AT+RFPOWER <https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-rfpower>`_ for more details.

----------------

For the AT+CIPTCPOPT command, if multiple clients are connected and disconnected from time to time when ESP32 is the server, should AT+CIPTCPOPT be configured each time?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - You do not need to configure it every time. This setting is for the connection itself, not for the client, that is, you configure link0-link4 and use the socket option of whichever link the client uses.

--------------

After I migrate from ESP8266 NONOS AT to RTOS AT (v2.0.0.0 and above), flash the firmware successfully, and start up AT, why no "ready" is returned?
----------------------------------------------------------------------------------------------------------------------------------------------------

  - AT communication pins of the ESP8266 RTOS version have been changed to GPIO13 and GPIO15.
  - See `Hardware connection <https://docs.espressif.com/projects/esp-at/en/latest/Get_Started/Hardware_connection.html#esp8266-series>`_ for more details.

--------------

How to download the AT firmware on Espressif's official website?
---------------------------------------------------------------------

  - Download the flash tool: `Flash Download Tools <https://www.espressif.com/en/support/download/other-tools>`_.
  - See `AT Downloading Guide <https://docs.espressif.com/projects/esp-at/en/latest/Get_Started/Downloading_guide.html>`_ for the download address.

--------------

Why is the error "flash read err,1000" printed on the serial port after powering up the newly purchased ESP32-WROVE-B module? How to use AT commands for this module?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The ESP32 WROVER module is shipped without AT firmware, so the error "flash read err" appears.
  - If you want to use the AT command function of ESP32-WROVER-B, please refer to the following links to get the firmware and flash it.
  
    - `Download firmware <https://docs.espressif.com/projects/esp-at/en/latest/AT_Binary_Lists/ESP32_AT_binaries.html#esp32-wrover-32-series>`_;
    - `Connect hardware <https://docs.espressif.com/projects/esp-at/en/latest/Get_Started/Hardware_connection.html#esp32-wrover-series>`_;
    - `Flash firmware <https://docs.espressif.com/projects/esp-at/en/latest/Get_Started/Downloading_guide.html#downloading-guide>`_.

----------------

How to combine all the bin files compiled by esp-at?
----------------------------------------------------

  - You can use the **combine** button of the `Flash Download Tools <https://www.espressif.com/en/support/download/other-tools>`_.

--------------

After ESP32 enters the passthrough mode using AT commands, can ESP32 give a message if the connected hotspot is disconnected?
-------------------------------------------------------------------------------------------------------------------------------

  - Yes, you can configure it with `AT+SYSMSG <https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-sysmsg>`_, i.e., set AT+SYSMSG=4. In this way, the serial port will report "WIFI DISCONNECT\r\n" when the connected hotspot is disconnected.
  - Note that this command is added after AT v2.1.0. It is not available for v2.1.0 and earlier versions.

----------------

Do AT commands support IPv6?
------------------------------

  - Currently AT does not support IPv6, but only IPv4.

-----------------

How does ESP8266 get the SNTP time of a half time zone using AT commands?
------------------------------------------------------------------------------------------

    V2.2.0.0 and later versions of the ESP8266 AT firmware support obtaining SNTP time of a half time zone. Below is an example:

  .. code-block:: text

    AT+GMR
    AT+CWMODE=1                     // set the device to station mode
    AT+CWJAP="SSID","password"      // connect to an AP, enter ssid and password
    AT+CIPSNTPCFG=1,530             // configure to obtain the SNTP time of the half time zone 5:30
    AT+CIPSNTPTIME?                 // query the SNTP time of the half time zone 

--------------

How to handle special characters in AT commands?
-----------------------------------------------------------------------------------------------

  - Please refer to `escape character syntax <https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/index.html#at-command-types>`_.

--------------

How to get the source code of AT firmware?
-------------------------------------------

  - ESP-AT firmware is partially open-source. See `esp-at <https://github.com/espressif/esp-at>`_ for the open-source repository.

--------------

Why does the ESP-AT firmware always return the following message after the I powered up the device and sent the first command?
------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    ERR CODE:0x010b0000
    busy p...

  - This message means that the previous command is being executed.
  - Normally only "busy p..." is displayed. The ERR CODE is displayed because the error code prompt is enabled.
  - If you receive this message after sending the first command on power-up, the possible reasons are: the command is followed by the unnecessary newline/space/other symbols; or two or more AT commands are sent in succession.

--------------

Does ESP8266 AT+MQTTPUB support the data in json format?
-------------------------------------------------------------

  - Yes, below is an example:

  .. code-block:: text

    AT+CWMODE=1                                                         // set the current device to station mode
    AT+CWJAP="ssid","passwd"                                            // connect to the specified AP
    AT+MQTTUSERCFG=0,1,"ESP32","espressif","1234567890",0,0,""          // set MQTT parameters
    AT+MQTTCONN=0,"192.168.10.234",1883,0                               // connect to the specified MQTT server
    AT+MQTTPUB=0,"topic","\"{\"timestamp\":\"20201121085253\"}\"",0,0   // publish a piece of json data to Topic

----------------

How does the ESP32 AT send data to the debug APP over Bluetooth LE?
-------------------------------------------------------------------

  - The following commands demonstrate how ESP32 AT sends data to the debug APP over Bluetooth LE:

  .. code-block:: text

    AT+RESTORE                   // initialize the device
    AT+BLEINIT=2                 // set ESP32 to SERVER mode 
    AT+BLEGATTSSRVCRE            // GATTS creates services
    AT+BLEGATTSSRVSTART          // GATTS starts services
    AT+BLEADDR?                  // query the MAC address of the Bluetooth LE device
    AT+BLEADVSTART               // start Bluetooth LE advertising and connect to the device using the APP
    AT+BLEGATTSCHAR?             // query the characteristics that are allowed to notify
    AT+BLEGATTSNTFY=0,1,6,6      // notify the 6-byte data using the sixth characteristic in the first service
                                 // then, ESP32 sends data to the APP through the serial port tool, such as "12345"

----------------

How does the ESP32 module use AT commands to implement encrypted Bluetooth pairing with the static secret key?
---------------------------------------------------------------------------------------------------------------

  - The commands are as follows:

  .. code-block:: text

    AT+RESTORE                    // initialize the module
    AT+BLEINIT=2                  // initialize the module as a server
    AT+BLEGATTSSRVCRE             // GATTS creates services
    AT+BLEGATTSSRVSTART           // GATTS start services
    AT+BLEADDR?                   // query the address of the Bluetooth LE device
    AT+BLESECPARAM=1,0,16,3,3     // set Bluetooth LE encryption parameters
    AT+BLESETKEY=123456           // set the static secret key for Bluetooth LE pairing
    AT+BLEADVSTART                // start Bluetooth LE advertising and connect to ESP32 using the APP
    AT+BLEENC=0,3                 // after the connection is established, use this command to generate an encrypted connection request, and enter the secret key

--------------

How to use the Ethernet function of the ESP32 AT?
--------------------------------------------------

  - In terms of hardware, you can use the ESP32-Ethernet-Kit development board to do the test.
  - Since GPIO19 and GPIO22 of ESP32-Ethernet-Kit are already occupied, you need to change the default UART pins to other free GPIOs, such as GPIO4 and GPIO2.
  - In addition, you need to enable the ``AT ethernet support`` function in menuconfig when compiling your esp-at project. By default, this function is not enabled in the AT.bin downloaded from Espressif's official website.

Why does the ESP32 loaded with the ESP-AT firmware V2.1.0.0 return ERROR after the AT+BLUFI=1 command is sent?
----------------------------------------------------------------------------------------------------------------------

  - The ESP-AT firmware V2.1.0.0 does not support BluFi provisioning. To use this feature, you need to compile the latest master (V2.2.0.0) version of esp-at code to generate the firmware. 
  - When compiling the project, go to menuconfig -> Component config -> AT -> AT blufi command support, enter "Y" to enable this feature.

  .. code-block:: text

    AT+RESTORE    // initialize the device
    AT+GMR        // check the firmware version 
    AT+BLUFI=1    // enable the BluFi feature
    AT+BLEADDR?   // query the device's address
    
----------------

Is it possible to set b/g/n modes for modules using ESP32 AT commands?
----------------------------------------------------------------------

  - This feature in supported since ESP32 AT v2.1.0.0.
  - `AT+CWSTAPROTO <https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-staproto>`_ is used to set and query the 802.11 b/g/n in station mode.
  - `AT+CWAPPROTO <https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-staproto>`_ is used to set and query the 802.11 b/g/n in softAP mode.

---------------

The ESP32 AT UART1 communication pins do not match the default pins in the datasheet?
-----------------------------------------------------------------------------------------

  - ESP32 supports the GPIO Matrix. When compiling esp-at, you can modify the UART1 pin configuration through the software in menuconfig, so the pins may not match with those in the datasheet.