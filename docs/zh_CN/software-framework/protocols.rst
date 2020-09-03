协议
====

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

-  ⽀持，目前 ESP8266 OpenSSL 是基于 mbedTLS 封装的接口，mbedTLS 支持
   Hostname validation。
-  使用 esp-tls 可以根据配置切换 mbedTLS 与 wolfSSL。

--------------

ESP32 是否⽀持 PCI-E 协议？
---------------------------

-  ESP32 不支持 PCI-E 协议。

--------------

ESP32 如何优化通信延时？
------------------------

-  建议关闭 Wi-Fi 休眠功能，调用 API:
   esp\_wifi\_set\_ps(WIFI\_PS\_NONE)。
-  建议在 menucongfig 关掉 AMPDU 功能。

--------------

ESP8285 是否⽀持 CCS（Cisco Compatible eXtensions）？
-----------------------------------------------------

不支持

--------------

ESP8266 ⽀持 HTTP 服务端吗？
----------------------------

-  ⽀持。ESP8266 在 SoftAP 和 Station 模式下都可以作服务端。
-  在 SoftAP 模式下，ESP8266 的服务端 IP 地址是 192.168.4.1。
-  如果 Station 模式，服务端的 IP 地址为路由器分配给 ESP8266 的 IP。
-  如果基于 SDK 进行⼆次开发，可参考相关应用示例。
-  如果使⽤ AT 指令，需使⽤ AT+CIPSERVER 开启服务端。

--------------

ESP32 是否 lora 通信？
----------------------

-  ESP32 自身并不支持 lora 通信，芯片没有集成 lora
   协议栈与对应的射频部分。
-  ESP32 可以外接集成 lora 协议的芯⽚，作为主控 MCU连接 lora
   芯片，可以实现 Wi-Fi 与 lora 设备的通信。

--------------

TCP 链接关闭后占用的相关资源何时释放 ？
---------------------------------------

-  TCP 链接关闭后占用的相关资源会在 20s 或者发送的 linger/send\_timeout
   超时之后释放。

--------------

如何使用 mqtt 配置服务器地址为自主云平台 ?
------------------------------------------

-  可以参考例程 `mqtt
   example <https://github.com/espressif/esp-idf/tree/master/examples/protocols/mqtt>`__

--------------

使用 ESP32 ，请问 ULP 里面用 jump 跳转到一个函数，是否有返回的指令？
--------------------------------------------------------------------

1. 目前 ULP CPU
   指令列表以及说明\ `参见 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/ulp_instruction_set.html#add-add-to-register>`__\ 。

2. 返回指令通常使用一个通用寄存器备份 PC 地址，用于后续跳回，由于目前
   ULP 只有 4 个通用寄存器，所以需要合理使用。

--------------

ESP8266 RTOS SDK rel3.2 sntp 校准后误差会逐渐变大，如何解决？
-------------------------------------------------------------

-  原因是 8266 系统定时器有误差，采用软件定时器，自身存在误差较大。
-  可通过以下几种方法改善：
-  releaseV3.2 分支可以通过创建 task 定时重新从服务器同步时间（推荐
   300s）。
-  releaseV3.3 与 master
   分支的系统时钟代码有进行重构，目前测试误差较小，并且也可以定时同步服务器时间。
-  master 分支继承了 releaseV3.3 上的代码重构，除此之外，可通过
   menuconfig 配置 sntp 同步间隔，路径如下：Component config > LWIP >
   SNTP -> Request interval to update time (ms)。

