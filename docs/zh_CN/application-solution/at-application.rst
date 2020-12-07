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

--------------

ESP32 AT 吞吐量如何测试及优化？
-------------------------------

  AT 吞吐量测试的影响因素较多，建议使⽤ esp-idf 中的 iperf 示例进行测试（用 AT 测试时，请使用透传方式，并将数据量调整为 1460 字节连续发送）。

  若测试速率不满⾜需求，可⾃行编译 esp-at ，修改 esp-idf 中 menuconfig iperf 参数，提⾼速率。

--------------

ESP32 AT Wi-Fi 连接耗时多少 ？
------------------------------

  ESP32 AT release/v2.0 固件初始化（模块启动）到 Wi-Fi 连接的整个时间⼤概是多久？

  在办公室场景下，ESP32 AT release/v2.0.0 版本连接耗时实测为 11 s。但在实际使用中，Wi-Fi 连接时间取决于路由器性能，⽹络环境，模块天线性能等多个条件。

--------------

AT 提示 busy 是什么原因？
-------------------------

  提示 "busy" 表示正在处理前⼀条指令，⽆法响应当前输⼊。因为，AT 指令的处理是线性的，只有处理完前⼀条指令后，才能接收下⼀条指令。

  当有多余的不可⻅字符输⼊时，系统也会提示 "busy" 或 "ERROR"。因为，任何串⼝的输⼊，均被认为是指令输⼊。 - 例如： - 串⼝输⼊ AT + GMR (换⾏符 CR LF) (空格符)，由于 AT + GMR (换⾏符 CR LF) 已经是⼀条完整的 AT 指令了，系统会执⾏该指令。 - 如果系统尚未完成 AT+GMR 操作，就收到了后⾯的空格符，将被认为是新的指令输⼊，系统提示 "busy"。 - 如果系统已经完成了 AT+GMR 操作，再收到后⾯的空格符，空格符将被认为是⼀条错误的指令，系统提示"ERROR"。

--------------

ESP32 AT 相关资源从哪里获得？
-----------------------------

- ESP32 AT bin 文件：https://www.espressif.com/zh-hans/support/download/at
- ESP32 AT 文档：`AT 指令集 <https://github.com/espressif/esp-at/blob/master/docs/ESP_AT_Commands_Set.md>`__
- 此外，客户也可以基于乐鑫官方的 esp-at 工程开发更多的 AT 指令，ESP32 AT 工程可以在 GitHub 下载：https://github.com/espressif/esp32-at

--------------


ESP32-AT 编译过程中，出现 no module named yaml 的错误，应如何解决？
-------------------------------------------------------------------

  请安装 yaml 模块: ``python -m pip install pyyaml``

--------------

ESP32 模组默认 AT 固件是否支持 BT 功能？
----------------------------------------

- ESP32-WROOM 系列模组 AT 固件默认不带 classic BT AT 指令，如需要 BT 指令，需要自行基于 `esp-at <https://github.com/espressif/esp-at/>`__ 工程编译 AT 固件，可通过 menuconfig 菜单设置，Component config -> AT -> [\*] AT bt command support。
- ESP32-WROVER 系列模组 AT 固件默认带 classic BT AT 指令。

--------------

ESP8266 通过 AT 进行 SSL 连接时是否支持 PSK 认证？
--------------------------------------------------

  ESP8266_Nonos_SDK 版本的 AT 是不支持的，但 IDF 版本 的 AT 是支持的。 

- AT `固件下载地址 <https://www.espressif.com/zh-hans/support/download/at>`_
- ESP8266_Nonos_SDK 版本的 `AT 指令集 <https://www.espressif.com/sites/default/files/documentation/4a-esp8266_at_instruction_set_cn.pdf>`__
- IDF 版本 的 `AT 指令集 <https://github.com/espressif/esp-at/blob/master/docs/en/get-started/ESP_AT_Commands_Set.md>`__

--------------

AT 命令中串口波特率是否可以修改？（默认：115200）
-------------------------------------------------

  AT 命令串口的波特率是可以修改的。 

- 第一种方法，您可以通过串口命令 ``AT+UART_CUR`` 或者 ``AT+UART_DEF``\ 进行修改, 详情请参考 `AT 指令集 <https://github.com/espressif/esp-at/blob/master/docs/en/get-started/ESP_AT_Commands_Set.md>`__。
- 第二种方法，您可以重新编译 AT 固件，编译介绍：`使用 esp-at 工程编译固件 <https://github.com/espressif/esp-at/blob/master/docs/en/get-started/ESP_AT_Get_Started.md>`_ ，以及波特率修改介绍 `修改 UART 的波特率 <https://github.com/espressif/esp-at/blob/master/docs/zh_CN/get-started/How_To_Set_AT_Port_Pin.md>`_。

--------------

ESP8266 如何通过 AT 指令建立 SSL 链接？
---------------------------------------

  ESP8266 建立 SLL 连接服务器示例，请使用如下指令：

.. code-block:: text

  AT+CWMODE=1                        // 设置 wifi 模式  为 station
  AT+CWJAP="espressif_2.4G","espressif"        // 连接 AP ，账号、密码   
  AT+CIPMUX=0                                  // 设置 单连接    
  AT+CIPSTART="SSL","www.baidu.com",443        // 建立 SSL 连接``

--------------

ESP32 AT 如何指定 TLS 协议版本？
--------------------------------

  编译 esp-at 工程时，可以在 menuconfig 的 Component config/mbedTLS 目录下，可以将不需要的版本关闭使能。

--------------

乐鑫芯片可以通过那些接口来传输 AT 指令？
----------------------------------------

  ESP8266，ESP32，ESP32-S2 可通过 SDIO, SPI UART 来传输 AT 指令。在 esp-at 工程中通过 menuconfig -> Component config -> AT 中进行配置。

--------------

ESP32 AT 如何从 UART0 口通信？
------------------------------

  默认 AT 固件是通过 UART1 口通信的，如果要从 UART0 通信， 需要下载并编译 `esp-at <https://github.com/espressif/esp-at>`__ code。

1. 参考\ `入门指南 <https://github.com/espressif/esp-at/blob/master/docs/en/get-started/ESP_AT_Get_Started.md#platform-esp32>`__ 搭建好环境；
2. 修改 `factory_param_data.csv <https://github.com/espressif/esp-at/blob/master/components/customized_partitions/raw_data/factory_param/factory_param_data.csv>`_ 表中对应模组的 UART 管脚，将 uart_tx_pin 修改为 GPIO1，uart_tx_pin 修改为 GPIO3；
3. menuconfig 配置：make menuconfig > Component config > Common ESP-related > UART for console output(Custom) >Uart peripheral to use for console output(0-1)(UART1) > (1)UART TX on GPIO# (NEW) > (3)UART TX on GPIO# (NEW)。

--------------

使用 ESP8266，如何用 AT 指令唤醒 light-sleep 模式？
----------------------------------------------------

  请参考AT 指令唤醒 `light-sleep <https://docs.espressif.com/projects/esp-at/en/release-v2.1.0.0_esp8266/AT_Command_Set/Basic_AT_Commands.html?highlight=wake#at-sleepwkcfgconfig-the-light-sleep-wakeup-source-and-awake-gpio>`_。

--------------

ESP32-SOLO-1C 如何使用 AT 与手机进行 BLE 透传？
-----------------------------------------------

1. 设备端需要按照 BLE server 透传模式去设置，具体 BLE 透传模式流程参考\ `《ESP32 AT 指令集与使用示例》 <https://www.espressif.com/sites/default/files/documentation/esp32_at_instruction_set_and_examples_cn.pdf>`__。
2. 手机端需要下载 BLE 调试助手，例如 nRF Connect APP（安卓）和 lightblue（IOS），然后打开 SCAN 去寻找设备端的 MAC 地址，最后就可以发送命令了。

--------------

ESP8266 使用 ESP-AT 编译后的固件，需要 OTA 功能，芯片 Flash 要求多大？
----------------------------------------------------------------------

  新版本 ESP-AT 固件，如果需要 OTA 功能，至少需要 2MB（16M bit）的 Flash，如果不需要 OTA 功能，至少需要 1MB（8M bit） 的 Flash 。

--------------

如何使用 AT 命令启用 MDNS 功能？
--------------------------------

  可以使用 ``AT+MDNS`` 指令来开启 MDNS 功能。

.. code-block:: text

  AT+CWMODE=1                            //将设备端设为 station 模式
  AT+CWJAP="ssid","password"             //设备要连接的 AP 账户 、密码
  AT+MDNS=1,"esp","\ *pos.*\ tcp.",3030  //启用 MDNS
  AT+MDNS=0                              //关闭 MDNS  

--------------

esp-at 固件是否支持 MQTT？
--------------------------

- ESP8266 芯片在 v2.1.0.0-rc1 版本后支持 MQTT。
- ESP32 系列芯片在 v2.0.0.0 版本后支持 MQTT。
- 详情可参考`release notes <https://github.com/espressif/esp-at/releases>`_。

--------------

AT 固件中 TCP 发送窗口大小是否可以修改？
----------------------------------------

  TCP 发送窗口当前无法通过命令修改，需要编译 `esp-at <https://github.com/espressif/esp-at>`__ 代码生成固件。可以重新配置 menuconfig 参数，Component config -> LWIP / TCP -> Default send buffer size。

--------------

MCU 发送 AT+CIPSEND 后，收到 busy p.. 响应，MCU 需要重新发送数据吗？
--------------------------------------------------------------------

  busy p.. 代表上一条命令正在执行, 当前输入无效。建议等 AT 上一条命令响应后， MCU 再重新发送新命令。

--------------

Wi-Fi-Mesh 是否支持 AT 指令？
-----------------------------

  Wi-Fi-Mesh 当前不支持 AT 指令。

--------------

ESP32 如何在 AT 中开启 blufi 功能？
-----------------------------------

  默认的 AT 固件不支持 blufi 功能，如果要使用 blufi 功能，需要编译 `esp-at <https://github.com/espressif/esp-at>`__ 代码生成固件。编译时需要在 menuconfig 中开启 blufi 的功能：make menuconfig--->Component config--->AT--->[\*]AT blufi command support。

--------------

如何获取模组或开发板中默认的固件版本信息？
------------------------------------------

  - 不同型号的模组或者开发板出厂固件不同，可以与采购对接商务咨询。
  - 如果模组出厂确认为 AT 固件，可以使用指令 AT+GMR 查看版本信息。

--------------

AT 命令连接阿里云以及腾讯云示例？
---------------------------------

  - 下载 `AT 固件 <https://docs.espressif.com/projects/esp-at/en/latest/AT_Binary_Lists/index.html>`__ 并完成烧录；
  - `阿里云应用参考示例 <https://blog.csdn.net/espressif/article/details/107367189>`_；
  - `腾讯云应用参考示例 <https://blog.csdn.net/espressif/article/details/104714464>`_。

--------------

AT 固件支持 SSL 证书认证吗？
---------------------------------

- 支持，具体请参考 `SSL 认证指令 <https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-SSLCCONF>`__。
- SSL 证书获取，可以参考 `esp-at/tools/README.md <https://github.com/espressif/esp-at/tree/release/v2.1.0.0_esp8266/tools>`__ 生成证书 bin 。
- SSL 证书的烧录地址是根据 at_customize.csv 决定的 。

--------------

AT 是否支持 websocket 指令？
---------------------------------

  - 默认指令不支持。
  - 可通过自定义指令实现，代码参考 [websocket](https://github.com/espressif/esp-idf/tree/master/examples/protocols/websocket)。

--------------

模组出厂 AT 固件是否支持流控？
-------------------------------------

  - 支持该模组支持硬件流控，但是不支持软件流控。

--------------

AT 如何修改 TCP 连接数？
-------------------------------

- ESP32 AT 最大支持 16 个 TCP 连接，可以在 menuconfig 中进行配置， 配置方法如下：
  - make menuconfig---> Component config---> AT--->  (16)AT socket maximum connection number
  - make menuconfig---> LWIP---> (16)Max number of open sockets

- ESP8266 AT 最大支持 5 个 TCP 连接，可以在 menuconfig 中进行配置， 配置方法如下：
  - make menuconfig---> Component config---> AT--->  (5)AT socket maximum connection number
  - make menuconfig---> LWIP---> (10)Max number of open sockets

--------------

AT 固件如何查看 error log ？
-------------------------------

  - ESP32 在 download port 查看 error log, 默认 UART0 为 GPIO1 GPIO3。
  - ESP8266 在 GPIO2 查看 error log , GPIO2 是 UART1 TX。 
  - 详情可以参阅 `AT 文档 <https://docs.espressif.com/projects/esp-at/en/latest/Get_Started/Hardware_connection.html>`__。

--------------

AT 固件如果 OTA 升级指？
---------------------------------

- AT 固件可以通过指令触发 OTA 升级。

.. code-block:: text

  AT+CWMODE=1
  AT+CWJAP_DEF="ssid","passwrod"
  AT+CIUPDATE

--------------

ESP32模组如何使用 AT 指令实现蓝牙加密配对？
----------------------------------------------

  - 蓝牙 AT 加密指令参考示例：

  .. code-block:: text

    AT+RST                          // 重启模块
    AT+GMR                          // 查询模组版本信息
    AT+BLEINIT=2                    // 将模组初始化为 server
    AT+BLEGATTSSRVCRE               // GATTS 创建服务
    AT+BLEGATTSSRVSTART             // GATTS 开启服务
    AT+BLEADDR?                     // 查询 BLE 设备的public address。
    AT+BLEADVPARAM=50,50,0,0,4      // 设置⼴播参数
    AT+BLEADVDATA="020120"          // 设置 BLE ⼴播数据
    AT+BLESECPARAM=4,1,8,3,3        // 设置加密参数         
    AT+BLEADVSTART                  // 开始 BLE 广播
    AT+BLEENC=0,3                   //无秘钥连接后，进行这一步，即可产生加密连接请求，并产生加密密钥。

---------------

ESP32 模组下载 ESP-AT 固件，默认 AP 的 Wi-Fi 名称是什么？
---------------------------------------------------------------

  - 可使用 AT+CWJAP? 指令查询默认的 Wi-Fi 名称，默认会拼接设备 MAC 地址。
  - AT 支持自定义 Wi-Fi 名称，可通过如下 AT 命令进行设置：

  .. code-block:: text

     AT+CWMODE=1                            //设置当前设备为SoftAP 模式
     AT+CWSAP="SSID","PASSWORD",1,0,4,0     //设置 SoftAP 参数
     AT+CWSAP？                             // 查询设置后的 SoftAP 信息

---------------

如何使用 SPI 接口进行 AT 通信？
---------------------------------------

  - 乐鑫提供的 AT 固件默认使用 UART 进行通信，用户如果需要使用 SPI 进行通信，可以基于 `esp-at <https://github.com/espressif/esp-at>`__ 配置编译。
  - 更多 AT 相关文档：`AT README.md <https://github.com/espressif/esp-at/blob/master/README.md>`__ 。

--------------

ESP8266 旧版本（SDK v1.5.4）的 AT 固件 AT+CWLAP 是主动扫描还是被动扫描？
-------------------------------------------------------------------------

  - 基于 ESP8266_NonOS_SDK v2.2.0 的 AT 固件，对应 AT 版本为 1.6.2 ，支持主动扫描 + 被动扫描，默认为主动扫描，之前的 AT 版本仅支持主动扫描。

--------------

AT 指令如何修改 SoftAP 默认的 IP 地址？
--------------------------------------------------

  - 以 ESP-AT V2.0 版本的以上的固件为例，SoftAP 的 IP 地址修改方式如下：

  .. code-block:: text

    AT+CWMODE=2    #设置当前设备为 SoftAP 模式
    AT+CIFSR       #查询当前设备的 AP 的 IP 地址
    AT+CIPAP="192.168.1.1","192.168.1.1","255.255.255.0"  #设置当前 SoftAP 的 IP 地址
    AT+CIFSR                                              #查看修改后的 SOftAP 的 IP 地址

--------------

ESP32 ESP-AT 固件默的蓝牙名称是什么？
---------------------------------------------

  - AT 固件的 BLE_NAME 默认为 BLE_AT 。
  - 可使用 `AT+BLENAME?` 指令查询默认的蓝牙名称。

--------------

如何使用 AT+CIPSTART 指令设置 keepalive 参数？
--------------------------------------------------

  - 使用示例：AT+CIPSTART="TCP","192.168.1.*",2500,60

--------------

ESP32-AT 是否支持 websocket 指令？
--------------------------------------------------

  - 固件目前不支持，但可以参考 `websocket <https://github.com/espressif/esp-idf/tree/master/examples/protocols/websocket>`__  示例自行实现相关指令。

  - 请参考文档: `How_to_add_user-defined_AT_commands <https://docs.espressif.com/projects/esp-at/en/latest/Compile_and_Develop/How_to_add_user-defined_AT_commands.html>`__ 。

--------------

at_http_webserver 例程无限重启如何解决？
-------------------------------------------

  master 分支已经修复了 `这个问题 <https://github.com/espressif/esp-at/commit/94f5781033b7dd44b9f5bf5882d4599fc5efea27>`__，请更新到最新的 master 分支，或者在 sdkconfig 配置项中更改为 ``CONFIG_SPI_FLASH_USE_LEGACY_IMPL=y`` 即可解决 crash 的问题

--------------

可以通过 AT 指令将 esp32-wroom-32 模块设置为 HID 键盘模式吗？
-------------------------------------------------------------

  可以的，官方指令集文档里面有指令说明，下面这个链接是简单的演示链接：
  https://pan.baidu.com/s/1TgNE2DpJtVARGqB-jb8UIQ  提取码：f6hu 

--------------

ESP-AT如何进行BQB认证？
----------------------------

  - 可参考 `ESP32 更新多项 BQB 蓝牙认证 <https://mp.weixin.qq.com/s?__biz=MzA4Nzc5MjkwNw==&mid=2651783810&idx=1&sn=fb0e132af240606d8178347966721542&chksm=8bcfaee6bcb827f03992aa200a2eb2baef5114712a4001da0c8282502a9183f5379605412cea&mpshare=1&scene=1&srcid=0920VLpOLubCew48DrCRdjCT&sharer_sharetime=1583218643838&sharer_shareid=1a1137fefea7b87a843519e48151f9a4&rd2werd=1#wechat_redirect>`__

----------------

新客户使用 ESP8266 NONOS 版本 AT 固件，如何建议客户切换到 RTOS 版本的 AT 固件？
-------------------------------------------------------------------------------------

  -  NONOS 版本 AT 固件属于老版本的固件，我们推荐使用 RTOS 版本 AT 版本，目前这个是我们主推的版本。
  -  RTOS 和 NONOS 逻辑有很大的差异，并且 RTOS 上支持了更多的功能，fix 掉了更多的问题， 这些问题有可能在 NONOS 版本 AT 上出现，以后 RTOS AT 也是我们重点维护的版本，会更加及时的修复问题和不断的添加新的功能。
  -  请下载 RTOS 版本的 `AT bin <https://docs.espressif.com/projects/esp-at/en/latest/AT_Binary_Lists/ESP8266_AT_binaries.html/>`_ 。

----------------

ESP-AT 是否可以设置 BLE 发射功率？
--------------------------------------------------

  - 可以。ESP32 的 Wi-Fi 和 BLE 共用一根天线，设置指令<https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-rfpower>`_。

----------------

针对 AT+CIPTCPOPT 指令，在 ESP32 作 server 时，如果多个 client 进行了不定时连上-断开的动作，那么 AT+CIPTCPOPT 是否要每次都配置一次？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 不需要每次都配置一次。这个设置是针对连接的，不是针对 client 的，也就是你配置 link0-link4, 后面 client 使用哪个 link, 就用哪个 link 的 socket option。

--------------

ESP8266 从 NONOS AT 切换到 RTOS AT(v2.0.0.0 以及以上版本)， 烧录成功后， AT 固件启动没有收到 ready 字样？
-----------------------------------------------------------------------------------------------------------

  - ESP8266 RTOS 版本 AT 通信管脚做了修改，更换为 GPIO13 和 GPIO15 管脚了。
  - `硬件接线参考 <https://docs.espressif.com/projects/esp-at/en/latest/Get_Started/Hardware_connection.html#esp8266-series/>`_ 。

--------------

官网上放置的 AT 固件如何下载？
-----------------------------------------------------------------------------------------------------------

  - 烧录工具： 下载 `Flashdownload tool 工具 <https://www.espressif.com/sites/default/files/tools/flash_download_tool_v3.8.5_1.zip/>`_。
  - 烧录地址请参考 `AT 下载指南 <https://docs.espressif.com/projects/esp-at/zh_CN/latest/Get_Started/Downloading_guide.html/>`_。 

--------------

新购买的 ESP32-WROVE-B 模组上电后，串口打印错误 “flash read err,1000" 是什么原因？该模组如何使用 AT 指令？
------------------------------------------------------------------------------------------------------------------------

  - ESP32 WROVER 的模组出厂没有烧录 AT 固件，因此出现 "flash read err" 的错误。
  - 如果想要使用 ESP32-WROVER-B 模组的 AT 指令功能 ，请参考如下链接获取固件和烧录固件。
  
    - `固件获取 <https://docs.espressif.com/projects/esp-at/en/latest/AT_Binary_Lists/ESP32_AT_binaries.html#esp32-wrover-32-series>`_
    - `硬件连接 <https://docs.espressif.com/projects/esp-at/en/latest/Get_Started/Hardware_connection.html#esp32-wrover-series>`_
    - `固件烧录 <https://docs.espressif.com/projects/esp-at/en/latest/Get_Started/Downloading_guide.html#downloading-guide>`_

----------------

如何整合 esp-at 编译出来的所有 bin 文件？
--------------------------------------------------

  - 可以使用 flash downloat tool<https://www.espressif.com/sites/default/files/tools/flash_download_tool_v3.8.5_1.zip/>`_ 的 combine 按钮进行整合，或者使用指令<https://docs.espressif.com/projects/esp-at/en/latest/Compile_and_Develop/How_to_clone_project_and_compile_it.html>`_进行整合。

--------------

ESP32 使用 AT 指令进入透传模式,如果连接的热点断开,ESP32 能否给出相应的提示信息？
-----------------------------------------------------------------------------------------------

  - 可以通过指令 `AT+SYSMSG <https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#at-sysmsg-configure-system-prompt-information>`_ 进行配置,
    可设置 AT+SYSMSG=4,如果连接的热点断开,串口会上报 "WIFI DISCONNECT\r\n"。
  - 需要注意的是,该指令在 AT v2.1.0 之后添加,v2.1.0 及之前的版本无法使用该指令.

----------------

AT 指令集是否支持 IPv6？
------------------------------

  - 当前 AT 不支持 IPv6, 只支持 IPv4。 

-----------------

ESP8266 如何使用 AT 指令获取半时区的 SNTP 的时间？
------------------------------------------------------------------------------------------

    ESP8266  AT-V2.2.0.0 版本的固件及其后续版本支持半时区获取 SNTP 时间。示例如下：

  .. code-block:: text

    AT+GMR
    AT+CWMODE=1                     //设置当前设备为 Station 模式
    AT+CWJAP="SSID","password"      //连接 AP ，输入 AP 的账号、密码
    AT+CIPSNTPCFG=1,530             //设置获取半时区为 5:30 的 SNTP 时间
    AT+CIPSNTPTIME?                 //查询获取后的半时区时间

--------------

AT 指令中特殊字符如何处理？
-----------------------------------------------------------------------------------------------

  - 可以参考 AT `转义字符语法 <https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/index.html#at-command-types/>`_  。

--------------

如何获取 AT 固件源码？
------------------------------

  - ESP-AT 固件部分开源， 开源仓库参考 `esp-at <https://github.com/espressif/esp-at>`_。

--------------

ESP-AT 固件，上电后发送第一个指令总是会返回下面的信息，为什么？
--------------------------------------------------------------------

  .. code-block:: text

    ERR CODE:0x010b0000
    busy p...

  - 此信息代表的是“正在处理上一条指令”。
  - 一般情况下只会显示“busy p...”，显示 ERR CODE 是因为打开了错误代码提示，
  - 如果是上电的第一条指令就返回了这个错误码信息，可能的原因是：这条指令后面多跟了换行符/空格/其他符号，或者连续发送了两个或多个 AT 指令。

--------------

ESP8266 AT+MQTTPUB 指令是否支持 json 格式数据 ？
-------------------------------------------------------------

  - 支持， 参考示例如下：

  .. code-block:: text

    AT+CWMODE=1                                                         # 设置当前设备为 Station 模式
    AT+CWJAP="ssid","passwd"                                            # 连接指定的 AP 
    AT+MQTTUSERCFG=0,1,"ESP32","espressif","1234567890",0,0,""          # 设置 MQTT 参数
    AT+MQTTCONN=0,"192.168.10.234",1883,0                               # 连接指定的 MQTT 服务器
    AT+MQTTPUB=0,"topic","\"{\"timestamp\":\"20201121085253\"}\"",0,0   # 向 Topic 主题上 publish 一条 json 数据

----------------

ESP32 AT 如何使用 BLE 向调试 APP 发数据？
--------------------------------------------------

  - ESP32 使用 BLE 向调试 APP 发数据可通过如下指令实现：

  .. code-block:: text

    AT+RESTORE                          // 初始化设备
    AT+BLEINIT=2                        // ESP32 设为 SERVER 模式  
    AT+BLEGATTSSRVCRE                   // GATTS 创建服务
    AT+BLEGATTSSRVSTART                 // GATTS 开启服务
    AT+BLEADDR?                         // 查询 BLE  设备 MAC 地址
    AT+BLEADVSTART                      // 开始 BLE 广播，使用 APP 与设备建立连接
    AT+BLEGATTSCHAR?                    // 查询允许 Notify 的特征
    AT+BLEGATTSNTFY=0,1,6,6             // 使⽤ 1 号服务的 6 号特征通知⻓度为 6 的数据
                                        // 然后 ESP32 设备通过串口助手发送数据给 APP，例如 ：12345

----------------

ESP32 模组如何使用 AT 指令实现静态秘钥进行蓝牙加密配对？
----------------------------------------------------------------------

  - 具体实现的 AT 命令如下：

  .. code-block:: text

    AT+RESTORE                          # 格式化模块
    AT+BLEINIT=2                        # 将模组初始化为 server
    AT+BLEGATTSSRVCRE                   # GATTS 创建服务
    AT+BLEGATTSSRVSTART                 # GATTS 开启服务
    AT+BLEADDR?                         # 查询 BLE 设备地址
    AT+BLESECPARAM=1,0,16,3,3           # 设置 BLE 加密参数
    AT+BLESETKEY=123456                 # 设置 BLE 配对静态秘钥
    AT+BLEADVSTART                      # 开始 BLE 广播，使用 APP 与ESP32 建立连接
    AT+BLEENC=0,3                       # 连接后，发送此条命令即可产生加密配对请求，输入秘钥

--------------

ESP32 AT 以太网功能如何使用？
---------------------------------------

  - 硬件上，可以用 ESP32-Ethernet-Kit 测试。
  - 由于 ESP32-Ethernet-Kit 开发板的 GPIO19 和 GPIO22 已经被占用，需要将默认的 AT 指令改为其他空闲 GPIO，例如 GPIO4 和 GPIO2。
  - 另外需要在 esp-at 编译中通过make menuconfig 配置使能以太网功能，官网链接中下载的标准版本 AT.bin 固件中未开启以太网支持。

ESP32 下载 ESP-AT V2.1.0.0 版本的 AT 固件，发送 AT+BLUFI=1 命令为何返回 ERROR ？
----------------------------------------------------------------------------------------------------------------------

  - ESP-AT V2.1.0.0 版本的 AT 固件不支持 Blufi  配网功能。如果要使用 Blufi 功能，需要编译最新 master （V2.2.0.0）版本的 esp-at 代码生成固件。
  - 编译时需要在 menuconfig ->Component config -> AT -> (键 "Y" Enable) AT  blufi command support 命令支持。代码仓库参考 `esp-at <https://github.com/espressif/esp-at>`_。

  .. code-block:: text

    AT+RESTORE            #格式化设备
    AT+GMR                      #查询固件版本信息
    AT+BLUFI=1              #开启 Blufi 功能
    AT+BLEADDR?          #查询设备地址
    
