协议
====

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


ESP8266 OpenSSL 是否⽀持 Hostname validation？
----------------------------------------------

  ⽀持，目前 ESP8266 OpenSSL 是基于 mbedTLS 封装的接口，mbedTLS 支持 ``Hostname validation``。使用 esp-tls 可以根据配置切换 mbedTLS 与 wolfSSL。

--------------

ESP32 是否⽀持 PCI-E 协议？
---------------------------

  ESP32 不支持 PCI-E 协议。

--------------

ESP32 如何优化通信延时？
------------------------

  - 建议关闭 Wi-Fi 休眠功能，调用 ``API：esp_wifi_set_ps(WIFI_PS_NONE)``。
  - 建议在 menucongfig 关掉 ``AMPDU`` 功能。

--------------

ESP8285 是否⽀持 CCS（Cisco Compatible eXtensions）？
-----------------------------------------------------

  - ESP8285 不支持 CCS （Cisco Compatible eXtensions。

--------------

ESP8266 ⽀持 HTTP 服务端吗？  
----------------------------

  ⽀持。ESP8266 在 SoftAP 和 Station 模式下都可以作服务端。

  - 在 SoftAP 模式下，ESP8266 的服务端 IP 地址是 192.168.4.1。
  - 如果 Station 模式，服务端的 IP 地址为路由器分配给 ESP8266 的 IP。
  - 如果基于 SDK 进行⼆次开发，可参考相关应用示例。
  - 如果使⽤ AT 指令，需使⽤ ``AT+CIPSERVER`` 开启服务端。

--------------

ESP32 是否 lora 通信？
----------------------

  ESP32 自身并不支持 lora 通信，芯片没有集成 lora 协议栈与对应的射频部分。ESP32 可以外接集成 lora 协议的芯⽚，作为主控 MCU连接 lora 芯片，可以实现 Wi-Fi 与 lora 设备的通信。

--------------

TCP 链接关闭后占用的相关资源何时释放 ？
---------------------------------------

  TCP 链接关闭后占用的相关资源会在 20 s 或者发送的 ``linger/send_timeout`` 超时之后释放。

--------------

如何使用 mqtt 配置服务器地址为自主云平台？
------------------------------------------

  可以参考例程 `mqtt example <https://github.com/espressif/esp-idf/tree/master/examples/protocols/mqtt>`_。

--------------

使用 ESP32 ，请问 ULP 里面用 jump 跳转到一个函数，是否有返回的指令？
--------------------------------------------------------------------

  目前 ULP CPU 指令列表以及说明 `参见 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/ulp_instruction_set.html#add-add-to-register>`_。返回指令通常使用一个通用寄存器备份 PC 地址，用于后续跳回，由于目前 ULP 只有 4 个通用寄存器，所以需要合理使用。

--------------

ESP8266 RTOS SDK rel3.2 sntp 校准后误差会逐渐变大，如何解决？
-------------------------------------------------------------

  原因是 8266 系统定时器有误差，采用软件定时器，自身存在误差较大。可通过以下几种方法改善：

  - releaseV3.2 分支可以通过创建 task 定时重新从服务器同步时间（推荐 300s）。
  - releaseV3.3 与 master 分支的系统时钟代码有进行重构，目前测试误差较小，并且也可以定时同步服务器时间。
  - master 分支继承了 releaseV3.3 上的代码重构，除此之外，可通过 menuconfig 配置 sntp 同步间隔，路径如下：``Component config > LWIP > SNTP -> Request interval to update time (ms)``。

-----------------

ESP8266 是否支持设备端 UDP 广播自发自收？
------------------------------------------------------------------------------------------------------

  - ESP8266 设备端支持 UDP 广播自发自收.
  - 需要在 menuconfig 配置选项中，需要把 LWIP 的 LOOPBACK 选项打开，``menuconfig -> Component config -> Enable per-interface lookback (键 "Y" 使能)``。

--------------

TCP/IP 默认配置的数据包长度是多少？
-----------------------------------

  在默认配置中，单包数据，TCP 1460 字节，UDP 1472 字节。

--------------

SNTP 协议中使用 UTC 与 GMT 的方法为何获取不到目标时区的时间？
-----------------------------------------------------------------

  TZ = UTC-8 被解释为 POSIX 时区，在 POSIX 时区格式中，这 3 个字母是时区的缩写(任意)，数字是时区落后于 UTC 的小时数。 
  UTC-8 表示时区,缩写为 “ UTC” ，比实际 UTC 晚 -8 小时, 即 UTC + 8 小时。故 UTC+8 是比 UTC 落后 8 小时, 就出现了 UTC+8 比正确的北京时间相差 16 小时的情况。

--------------

ESP32 是否有特殊的固件或者 SDK ，可以不使用芯片内部的 TCP/IP 协议，仅提供 AP/STA（TCP/IP bypass），给开发者更多的权限？
----------------------------------------------------------------------------------------------------------------------------

  - ESP-Dongle 的软件方案符合您的上述需求，烦请联系 `我司商务 <https://www.espressif.com/zh-hans/contact-us/sales-questions>`__，签署 NDA 后获取相关方案。

--------------

请问安卓 EspTouch 可以添加自己想要广播的数据吗？比如添加设备ID，希望ESP32能接收到这个ID。
--------------------------------------------------------------------------------------------

  - 目前的 EspTouch 协议下发送的数据内容都是固定的，不支持自定义数据
  - 如果需要发送自定义数据的话，建议使用 Blufi ，这是基于 BLE 的配网协议
  - 设备端：https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/blufi
  - Android APP：https://github.com/EspressifApp/EspBlufiForAndroid
  - iOS APP：https://github.com/EspressifApp/EspBlufiForiOS

----------------

ESP8266 测试 RTOS-SDK mqtt/ssl_mutual_auth 为何连接服务器失败？
-----------------------------------------------------------------------------

  - 出现 SSL 无法连接可能是由于 ESP8266 内存不足导致。
  - 请使用 ESP8266-RTOS-SDK Master 版本来测试此例程，Master 版本支持在 menuconfig 配置端动态分配内存，可以减少峰值内存的开销。
  - 通过 menuconfig -> Component  config -> mbadTLS -> (键 “Y” Enable)Using  dynamic TX /RX buffer  -> (键 “Y” Enable) Free SSL peer certificate after its usage -> (键 “Y” Enable) Free certificate, key and DHM data after its usage 。
