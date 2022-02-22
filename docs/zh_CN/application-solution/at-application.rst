AT
==

:link_to_translation:`en:[English]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

本文提供了有关 ESP-AT 的常见问题，更多问题请见 `ESP-AT 用户指南 <https://docs.espressif.com/projects/esp-at/zh_CN/latest/faq.html>`_.

--------------

如何使用 ESP8266 AT 固件下载重定向的资源？
-----------------------------------------------------

  - ESP8266 AT HTTP 指令不支持重定向，在获取到服务器返回的状态码 301（永久性重定向）或者 302（临时性重定向）后不会自动跳转到新的 URL 地址。
  - 可以使用 wireshark 或者 postman 获取到实际访问的 URL，然后通过 HTTP 指令访问。

  - 需要注意的是，当前 ESP8266-IDF-AT_V2.1.0.0 默认不支持 HTTP 指令，若想要使用 HTTP 的指令，需要基于 esp-at 编译，参考 `ESP8266 platform <https://docs.espressif.com/projects/esp-at/en/latest/Compile_and_Develop/How_to_clone_project_and_compile_it.html#esp8266-platform>`_。编译时需要在 menuconfig 中使能 HTTP：``menuconfig`` -> ``Component config`` -> ``AT`` -> ``[*] AT http command support``。

  - ``AT+HTTPCLIENT`` 的参数 ``URL`` 的最大长度为 256，当获取到的实际访问的 URL 长度超过 256 时，会返回 ``ERROR``，可以使用 TCP 的相关指令发送构造的 HTTP 请求报文获取该资源。

--------------

ESP8266 v2.1.0.0 版本 AT 固件，如何关闭默认的 power save 模式？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 使用 `AT+SLEEP=0 <https://docs.espressif.com/projects/esp-at/en/release-v2.1.0.0_esp8266/AT_Command_Set/Basic_AT_Commands.html?highlight=sleep#at-sleepsets-the-sleep-mode>`_ 指令即可关闭 AT 固件默认的 power save 模式。
  
----------------

发送 AT 命令，返回如下日志，是什么原因？
--------------------------------------------------------------------------------

  .. code-block:: text

    busy p...
    OK

  - 检查发送的 AT 命令是否存在多余的字节，例如多了换行和回车（CR 和 LF），更进一步，您也可以抓下通信线上的数据。

  - 更多消息请参考：`ESP-AT 消息报告 <https://docs.espressif.com/projects/esp-at/zh_CN/latest/AT_Command_Set/index.html#id5>`_。

---------------

AT+BLEGATTSNTFY 和 AT+BLEGATTSIND 的 length 最大可以支持到多少？
----------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32:

  - length 的最大值为 MTU - 3，MTU 最大可以支持到 517 字节，因此 length 的最大值为 514 字节。
  
---------------

ESP8266 NONOS AT 固件如何使能全校准模式？
--------------------------------------------------------------------------------------------------------------------------------

  - NONOS AT 固件默认使用部分校准，可通过如下方式使用全校准：
  
    修改文件 esp_init_data_default_v08.bin，byte[114] = 3 (部分校准 byte[114]  =  1，全校准 byte[114]  =  3)

---------------

ESP32 AT BLE UART 透传的最大传输率是？
-----------------------------------------------------------------------

  - 办公室开放环境下，串口波特率为 2000000 时：ESPAT BT 平均传输速率为 0.56 Mb，ESPAT BLE 平均传输速率为 0.101 Mb。
  - 屏蔽箱数据后续会继续补充测试。

---------------

如何获取到模组 ESP32-MINI-1(内置芯片 ESP32-U4WDH) 的 AT 固件？
--------------------------------------------------------------------------------------------------------------------------------

  - 请参考 `如何从 GitHub 下载最新临时版本 AT 固件 <https://docs.espressif.com/projects/esp-at/zh_CN/latest/Compile_and_Develop/How_to_download_the_latest_temporary_version_of_AT_from_github.html>`_。
  
-----------------------------------------------------------------------------------------------------

ADV 广播参数超过 32 字节之后应该如何设置?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32 :

   - `AT+BLEADVDATA <https://docs.espressif.com/projects/esp-at/zh_CN/latest/AT_Command_Set/BLE_AT_Commands.html#esp32-only-at-bleadvdata-set-bluetooth-le-advertising-data>`_  指令支持 adv 广播参数最大为 32 字节，如果需要设置更长的广播参数，请调用 `AT+BLESCANRSPDATA <https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/BLE_AT_Commands.html#esp32-only-at-blescanrspdata-set-bluetooth-le-scan-response>`_  指令来设置。
   
--------------------------------------------------------------------------

AT 支持 Wi-Fi 漫游功能吗?
--------------------------------------------------------------------------------------------
  :CHIP\: ESP32|ESP32-S2|ESP32-C3:

  - 不支持。

--------------------------------------------------------------------------

使用 ESP-AT 发送 TCP 数据时，有时数据会混乱/部分丢失，应该如何处理？
--------------------------------------------------------------------------------------------------------------

  - 建议添加硬件流控或软件流控：

    - `硬件流控 <https://docs.espressif.com/projects/esp-at/zh_CN/latest/Get_Started/Hardware_connection.html#id1>`_：CTS 和 RTS 信号
    - `软件流控 <https://docs.espressif.com/projects/esp-idf/en/release-v4.1/api-reference/peripherals/uart.html>`_

  - 必要时可以在代码中添加一些处理错误的逻辑，例如不小心进入透传模式，或透传模式数据传输错误时，及时发送 +++ 退出透传，重新发送 AT+CIPSEND 指令等。

---------------------------

ESP32 进行 BLE OTA 时，使用 BLE 连接手机、UART 连接 MCU ，对 MCU 进行 OTA。手机设置 MTU 增大后，ESP32 与 MCU 端数据传输仍然很慢。可以从哪方面排查？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 可能由于 ESP32 和手机端设置 MTU 时没有成功，或者 ESP32 和 MCU 端通信时 UART 限制。所以建议从以下几点进行排查/改进：

    - ESP32 与手机端的连接

      1. 仅 BLE client 支持设置 GATT MTU 长度，并且需要先建立 BLE 连接，才能设置 MTU 长度。最终实际的 MTU 长度需经过协商，设置指令返回 OK 仅表示尝试协商 MTU，因此，设置长度不一定有效，建议设置后，使用查询指令 AT+BLECFGMTU? 查询实际的 MTU 长度。
      2. 使用 BLE SPP，即 BLE 透传模式，可增大传输速率。
      
    - ESP32 与 MCU 端的连接：适当调大 UART 的波特率，可增大传输速率。

-------------------------

使用 ESP32-C3 作为 Server 且 AT 固件版本为 v2.2.0.0 时，AT+CIPSERVERMAXCONN 指令允许建立的最大连接数是多少？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - `AT+CIPSERVERMAXCONN <https://docs.espressif.com/projects/esp-at/en/release-v2.2.0.0_esp32c3/AT_Command_Set/TCP-IP_AT_Commands.html?highlight=CIPSERVERMAXCONN#at-cipservermaxconn-query-set-the-maximum-connections-allowed-by-a-server>`_ 指令默认设置的允许建立的最大连接数是 5 。
  - 可增大 “menuconfig -> Component config -> AT -> Socket Maximum Connection” 参数设置，以支持更大的连接数。
  - 若需要支持 10 个以上的连接数，还需要增大 “menuconfig -> Component config -> LWIP -> Max number of open sockets”（默认是 10）配置。
  - 但实际运行时允许的最大连接数取决于芯片的剩余可用内存。当无法建立更多连接时建议使用 `AT+SYSRAM <https://docs.espressif.com/projects/esp-at/en/release-v2.2.0.0_esp32c3/AT_Command_Set/Basic_AT_Commands.html?highlight=sysram#at-sysram-query-current-remaining-heap-size-and-minimum-heap-size>`_ 命令来查询当前剩余可用内存。
  
--------------------

使用 release/v2.1.0.0 版本的 AT 固件，ESP32 最多支持保存多少个 BLE 设备的绑定配对信息？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP32 最多支持保存 15 个 BLE 设备的绑定配对信息。

-----------------------------------------------------------------------------------------------------

AT+BLEADVDATA 广播数据支持的最大长度为 31，如何支持更大的数据长度?
---------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32:

 - 可以将数据放到 BLE scan response 中，指令为 `AT+BLESCANRSPDATA <https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/BLE_AT_Commands.html#esp32-only-at-blescanrspdata-set-bluetooth-le-scan-response>`_。

-----------------------------------------------------------------------------------------------------

WPA2 Enteprise 支持哪些认证方式呢 ?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP8266 | ESP32 | ESP32-C3:

  - 仅支持 EAP-TLS/EAP-PEAP/EAP-TTLS 三种，详情参考 `AT+CWJEAP <https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#esp32-only-at-cwjeap-connect-to-a-wpa2-enterprise-ap>`_ 指令介绍。

---------------

AT+HTTPCPOST 有哪些使用示例?
--------------------------------------------------------------------------------------------------

  :CHIP\: ESP8266:

  - 在 ESP-AT master 版本下面手动编译固件，需要将 at process task stack size 大小改到 4096 以上， 具体的操作步骤如下：
 
    - ./build.py menuconfig----->AT----->(5120)。表示 AT 仓库中任务运行的栈大小，将用于运行 AT 指令。
    - [*] AT http 指令支持：

    .. code:: text
 
      AT+CWMODE=1     //设置为 station 模式
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

是否有 AT+CIPRECVDATA 接收服务器端缓存数据示例?
--------------------------------------------------------------------------------------------------

  :CHIP\: ESP8266:
    .. code:: text

      AT+CWMODE=1     //设置为 station 模式
      OK
      AT+CWJAP="iot","123456789"
      WIFI CONNECTED
      WIFI GOT IP
      AT+CIPSTART="TCP","192.168.3.129",8080
      CONNECT
      OK
      AT+CIPRECVMODE=1
      OK
      //服务器端发送数据给客户端 16字节
      AT+CIPRECVLEN?    //查询服务器端缓存数据
      +CIPRECVLEN:16    //确保查询长度不为 0，否则获取数据会返回 ERROR
      AT+CIPRECVDATA=1080
      +CIPRECVDATA:16,http://en.usr.cn
      OK

-----------------------------

使用 ESP32 的 AT 固件，发送 BLE 扫描命令，没有收到扫描应答包，是什么原因？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 使用的 AT 指令如下：

.. code:: text

    AT+BLEINIT=1
    AT+BLESCANPARAM=0,0,0,100,50
    AT+BLESCAN=1
  
  有广播包，但没有扫描应答包; 命令回复的日志如图所示：
  
  .. figure:: ../_static/application-solution/at-application/AT_BLESCAN_Return_LOG.png
    :align: center

  - 若想要获得扫描应答包，那么需要设置的扫描方式是 "active scan"，即 "AT+BLESCANPARAM=1,0,0,100,50"
  - 且对端设备需要设置 "scan rsp data" ，才能获得扫描应答包；
  - 可参考`《ESP32 AT 指令集与使用示例》 <https://www.espressif.com/sites/default/files/documentation/esp32_at_instruction_set_and_examples_cn.pdf>`_ 。

------------------

使用 AT+BLEADVDATA 指令发广播包最大长度有限制吗？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - AT+BLEADVDATA 广播包最大长度为 31 字节。
  
--------------------

使用 ESP32 的 v2.2.0.0 版本的 AT 固件，AT+BLEGATTCWR 指令的 "length" 参数最大可以设置多大？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - `AT+BLEGATTCWR <https://docs.espressif.com/projects/esp-at/zh_CN/release-v2.2.0.0_esp32/AT_Command_Set/BLE_AT_Commands.html?highlight=BLEGATTCWR#esp32-only-at-blegattcwr-gattc-writes-characteristics>`_ 指令的 "length" 参数的最大设置对应 `example <https://github.com/espressif/esp-at/blob/release/v2.2.0.0_esp32/components/customized_partitions/raw_data/ble_data/example.csv>`_ 文件的下的 "val_max_len" 参数设置，建议不要超过 512。请参见 `README <https://github.com/espressif/esp-at/blob/release/v2.2.0.0_esp32/tools/README.md>`_ 下的 "val_max_len" 参数说明。

----------------

ESP32 使用 v2.2.0.0 版本的 AT 固件连接上 AP，重新复位上电后会自动连接 AP，如何取消这个设置？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 建议使用 AT+SYSSTORE=0 指令。调用该指令后，相关受影响的指令对应的配置信息不会保存到 flash。比如，在使用 AT+CWJAP 命令连接 AP 前，先使用 `AT+SYSSTORE=0 <https://docs.espressif.com/projects/esp-at/zh_CN/release-v2.2.0.0_esp32/AT_Command_Set/Basic_AT_Commands.html#at-sysstore-query-set-parameter-store-mode>`_ 命令设置不保存历史 AP 信息到 flash。

----------------

ESP32-AT 支持 PPP 吗?
----------------------------------------------------------------------

  - 不支持，可参考 `pppos_client <https://github.com/espressif/esp-idf/tree/master/examples/protocols/pppos_client/>`_ 示例自行实现。

----------------

AT 如何使能 Wi-Fi Debug ?
----------------------------------------------------------------------
  :CHIP\: ESP8266 | ESP32 | ESP32-C3 | ESP32-S2:

  - 使能 log 等级：``./build.py menuconfig -> Component Config -> Log output -> Default log verbosity`` 设置到 Verbose。
  - 使能 Wi-Fi debug：``./build.py menuconfig-> Component config -> Wi-Fi -> Enable WiFi debug log -> Wi-Fi debug log level(Wi-Fi Debug log Verbose)``。

---------------

使用 AT+SYSFLASH 指令更新证书应注意什么？
--------------------------------------------------------------------------------------------------------------------------------

  - 证书长度必须 4 字节对齐。
  - 证书 bin 需要通过 tools/AtPKI.py 生成，参考 `esp-at/tools/README.md <https://github.com/espressif/esp-at/blob/master/tools/README.md>`__ 中生成方法。例如：
  
    python AtPKI.py generate_bin -b mqtt_cert_v2.bin cert mqtt_client.crt

---------------

AT+HTTPCPOST 指令中 content-type 默认类型是什么？
--------------------------------------------------------------------------------------------------

  :CHIP\: ESP8266 | ESP32 | ESP32-S2 | ESP32-C3:

  - 默认类型是 application/x-www-form-urlencoded。

---------------

AT+HTTPCLIENT 发送数据到服务器有长度限制吗？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 有限制，AT 命令总长度不能超过 256 字节。数据是在指令参数中，导致 HTTP POST 请求数据长度会有限制，如果发送的数据比较长，建议通过 `AT+HTTPCPOST <https://docs.espressif.com/projects/esp-at/zh_CN/latest/AT_Command_Set/HTTP_AT_Commands.html#at-httpcpost-post-http>`_ 指令去设置，或者用 TCP 指令模拟 HTTP 发送数据。

---------------

AT 支持 哪些 TLS 版本 ？
--------------------------------------------------------------------------------------------------------------------------------

  - 支持 TLS1.0、TLS 1.1、TLS1.2，具体支持的版本号可以在 ``menuconfig-->Component config-->mbedTLS`` 中查看。
