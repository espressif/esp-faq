Wi-Fi
=====

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

ESP32 ESP-Now 模式下一对一的通信速率是多少？
--------------------------------------------

  测试数据如下：

  - 测试样板：ESP32\_Core\_board\_V2。
  - Wi-Fi 模式：station 模式。
  - open 环境下大约是 214 kbps。
  - 屏蔽箱内测试大约是 555 kbps。

--------------

ESP32 和 ESP8266 是否支持中文 SSID？
------------------------------------

  是支持的，使用中需要路由器或者手机的中文编码方式一致。

  示例：路由器中文编码使用 UTF-8 ，设备中文编码使用 UTF-8，设备就可以正确连接中文 SSID 的路由器。

--------------

[Scan] ESP32 扫描⼀次需要花多长时间?
------------------------------------

  扫描花费的总时间取决于:

  - 是被动扫描还是主动扫描，默认为主动扫描。
  - 每个信道停留的时间，默认主动扫描为 120 ms，被动扫描为 360 ms。
  - 国家码与配置的信道范围，默认为 1~13 信道。
  - 是快速扫描还是全信道扫描，默认为快速扫描。
  - Station 模式还是 Station-AP 模式，当前是否有连接。

  默认情况下，1~11 信道为主动扫描，12〜13 信道为被动扫描。在 Station 模式没有连接的情况下，全信道扫描总时间为：11\ *120 + 2*\ 360 = 2040 ms；在 Station 模式有连接，或者 Station-AP 模式下，全信道扫描总时间为：11\ *120 + 2*\ 360 + 13\*30 = 2430 ms。

--------------

[Scan] 乐鑫是否支持 boundary scans(边界扫描)?
---------------------------------------------

    ESP32 不⽀持 boundary scan。

--------------

客户⾃研产品如何优化⼆次谐波等杂散？
------------------------------------

  ⼆次谐波主要来源于射频链路路辐射和 PA 电源辐射，同时易易受到客户底板（板⼦尺⼨）及产品整机影响。因此有如下建议：

  - 在射频匹配中使⽤ ⼀个接近 2.4 pF ⼤⼩的对地电容，可较好地优化射频链路路上的杂散辐射；
  - 在 PA 电源 (芯⽚ 3、4 管脚) ⼊⼝增加⼀个串串联电感可较好减少 PA 电源的杂散辐射。

--------------

Wi-Fi 信道是什么？可以自行选择信道吗？
--------------------------------------

  信道指的是 Wi-Fi 使用的指定频段中特定频率的波段。不同国家地区使用的信道数是不是同的。⽤户可以参考 `ESP8266 Wi-Fi 信道选择指南 <https://www.espressif.com/sites/default/files/documentation/esp8266_wi-fi_channel_selection_guidelines_cn_1.pdf>`_。

--------------

80 MHz 倍频杂散较差该如何解决？
-------------------------------

  若 80MHz 倍频杂散超标，如 160 MHz、240 MHz、320 MHz 等均⽐较⾼，可在发送数据 (TXD) 串⼝线路路中串联⼀个阻值约为 470 Ω 的电阻，即可有效抑制 80 MHz 倍频杂散。

--------------

[LWIP] ESP32 Station 模式，如何设置静态 ip ?
--------------------------------------------

  由于 V4.2 以及以上版本会摒弃掉 tcp/ip 的接口，推荐使用 ethif 的接口.参考示例代码如下：

.. code-block:: c

    char ip_str[15];
    char ip[15] = "192.168.5.241";
    char gateway[15] = "192.168.5.1";
    char netmask[15] = "255.255.255.0";
    char dns[15] = "8.8.8.8";

    esp_netif_ip_info_t info_t;
    //esp_netif_t netif;
    esp_netif_dns_info_t dns_info;

    esp_netif_config_t netif_cfg = ESP_NETIF_DEFAULT_ETH();
    esp_netif_t *eth_netif = esp_netif_new(&netif_cfg);
    // set default handlers to do layer 3 (and up) stuffs
    esp_eth_set_default_handlers(eth_netif);

    memset(&info_t, 0, sizeof(esp_netif_ip_info_t));
    memset(&dns_info, 0, sizeof(esp_netif_dns_info_t));

    esp_netif_dhcpc_stop(eth_netif);

    ip4addr_aton((const char *)ip_str, &info_t.ip.addr);
    memcpy(&ip_str[0], &gateway[0], 15);
    ip4addr_aton((const char *)ip_str, &info_t.gw.addr);

    memcpy(&ip_str[0], &dns[0], 15);
    ip4addr_aton((const char *)ip_str, &dns_info.ip.u_addr.ip4);
    ESP_LOGI("Test", "DNS %s\n", ip4addr_ntoa(&dns_info.ip.u_addr.ip4));

    memcpy(&ip_str[0], &netmask[0], 15);
    ip4addr_aton((const char *)ip_str, &info_t.netmask.addr);
    esp_netif_set_dns_info(eth_netif,ESP_NETIF_DNS_MAIN,&dns);

--------------

[Performance] 如何测试 Wi-Fi 模组的通信速率?
--------------------------------------------

  可以使⽤ SDK 中提供的示例 ``example/wifi/iperf`` 中代码进⾏测试。

--------------

[LWIP] ESP8266 SoftAP 默认使用哪个网段?
---------------------------------------

  ESP8266 SoftAP + Station 模式下, 连接的 192.168.4.X ⽹段时，为什么会失败 ？

  - ESP8266 SoftAP 默认使用网段 192.168.4.\*，IP 地址是 192.168.4.1。ESP8266 如果要连接 192.168.4.X 的路由时，不能分辨是要连接⾃⼰本身的 SoftAp 还是外部路由，所以会造成错误。

--------------

[Connect] ESP8266 SoftAP 模式支持几个设备?
------------------------------------------

  硬件上最多⽀持 8 个，我们推荐 4 个，这样可以保证模组性能。

--------------

ESP8266/ESP32/ESP32-S2 是否支持 web 配网/softAP 配网？
-------------------------------------------------------

  支持。

  - ESP8266 请参考此示例 `ESP8266 softap\_prov <https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/provisioning/softap_prov>`_；
  - ESP32/ESP32-S2 请参考此示例 `ESP32/ESP32-S2 softap\_prov <https://github.com/espressif/esp-idf/tree/master/examples/provisioning/legacy/softap_prov>`_。

--------------

[Connect] ESP8266 和 ESP32 作为 softap 模式如何隐藏 SSID ?
----------------------------------------------------------

  `wifi\_ap\_config\_t <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/network/esp_wifi.html#_CPPv416wifi_ap_config_t>`_ 结构体中有一个变量 `ssid\_hidden <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html?highlight=hidden#_CPPv4N18wifi_scan_config_t11show_hiddenE>`_，可以设置为隐藏功能。

--------------

`esp\_wifi\_802.11\_tx <https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/api-reference/wifi/esp_wifi.html?highlight=esp_wifi_802.11_tx#_CPPv417esp_wifi_80211_tx16wifi_interface_tPKvib>`__ 接口中的 buffer 参数中包括 FCS 吗？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  不包括， FCS 帧是硬件自动生成的。

--------------

ESP-WROOM-32D 支持的 Wi-Fi 频段信息和功率表分别是什么？
-------------------------------------------------------

  Wi-Fi频段是 2412 ~ 2484 MHz，软件里可配置可用信道和对应的工作频率。功率表有默认值，也可支持软件配置。详细指导请参考 `《ESP32 Phy Init Bin 重要参数配置说明》 <https://www.espressif.com/sites/default/files/documentation/esp32_phy_init_bin_parameter_configuration_guide_cn.pdf>`_。

--------------

ESP32 Wi-Fi RF 功率最高值是多少？
---------------------------------

  ESP32 RF 功率为 20 dB，即模组最大值。

--------------

[Connect] ESP32 AP 模式最多支持多少设备连接？
----------------------------------------------

  ESP32 AP 模式，最多可配置为支持 10 个设备连接，默认配置为支持 4 设备。

--------------

[Connect] WIFi 模组如何通过 RSSI 数值划分信号强度等级?
------------------------------------------------------

  我们没有对 RSSI 信号强度进行等级划分。如果您需要标准进行划分，可以参考安卓系统的计算方法。 

  .. code-block:: java

    @UnsupportedAppUsage
    private static final int MIN_RSSI = -100;

    /** Anything better than or equal to this will show the max bars. */
    @UnsupportedAppUsage
    private static final int MAX_RSSI = -55;

    public static int calculateSignalLevel(int rssi, int numLevels) { 
      if(rssi <= MIN_RSSI) { 
        return 0; 
      } else if (rssi >= MAX_RSSI) {
        return numLevels - 1; 
      } else { 
        float inputRange = (MAX_RSSI -MIN_RSSI); 
        float outputRange = (numLevels - 1); 
        return (int)((float)(rssi - MIN_RSSI) * outputRange / inputRange); 
      }
    }

--------------

[Connect] ESP32 进行 Wi-Fi 连接时，如何通过错误码判断失败原因？
---------------------------------------------------------------

  - esp-idf V4.0 及以上版本可参考如下代码获取 Wi-Fi 连接失败的原因：

  .. code-block:: c

    if (event_base == WIFI_EVENT && event_id == WIFI_EVENT_STA_DISCONNECTED) { 
      wifi_event_sta_disconnected_t *sta_disconnect_evt = (wifi_event_sta_disconnected_t*)event_data;
      ESP_LOGI(TAG, "wifi disconnect reason:%d", sta_disconnect_evt->reason);
      esp_wifi_connect();
      xEventGroupClearBits(s_wifi_event_group, CONNECTED_BIT);
    }

  - 当回调函数接收到 ``WIFI_EVENT_STA_DISCONNECTED`` 事件时，可以通过结构体 `wifi\_event\_sta\_disconnected\_t <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/network/esp_wifi.html#_CPPv429wifi_event_sta_disconnected_t>`_ 的变量 ``reason`` 获取到失败原因。

  - ``WIFI_REASON_AUTH_EXPIRE`` 在连接的 auth 阶段，STA 发送了 auth，但在规定时间内未收到 AP 的 auth 回复，有较低概率会出现.

  - ``WIFI_REASON_AUTH_LEAVE`` 通常是由 AP 因为某种原因断开了 STA 连接，reason code 是由 AP 发过来的.

  -  ``WIFI_REASON_4WAY_HANDSHAKE_TIMEOUT`` 或者 ``WIFI_REASON_HANDSHAKE_TIMEOUT`` 失败原因为密码错误.

  其中, ``WIFI_REASON_4WAY_HANDSHAKE_TIMEOUT`` 为标准通用的错误码, 而 ``WIFI_REASON_HANDSHAKE_TIMEOUT`` 为自定义错误码.
  两者区别在于 ``WIFI_REASON_4WAY_HANDSHAKE_TIMEOUT`` 为路由器在密码错误时告知设, 产生的错误, ``WIFI_REASON_HANDSHAKE_TIMEOUT`` 为路由器在密码错误时不告知设备，由设备本身超时机制产生的错误.

  - ``WIFI_REASON_CONNECTION_FAIL`` 扫描阶段返回的错误码, 主要是由于 STA 扫描到了匹配的 AP, 但是这个 AP 在黑名单里. AP 在黑名单里面的原因是上次 AP 主动踢掉了 STA, 或者 STA 连接 AP 的过程中失败了.

--------------

ESP32 系列芯片每次连接服务器都会执行域名解析吗?
-----------------------------------------------

  在协议栈内，域名会通过 DNS 进行解析，解析后的数据会在时效内进行缓存。缓存时间基于从 DNS 服务器获取的 TTL 数据，该数据是配置域名时填入的参数，通常为 10 分钟。

--------------

[Connect] WiFi Log 中状态机切换后面数字的含义?
----------------------------------------------

  eg: run -> init (fc0)              c0 代表收到的帧类型, f 代表 reason. 即 fc0 含义为 STA 收到了deauth 帧, reason 为密码错误.

  其中后两位表示帧类型, 00 代表超时. 前两位表示 reason.  帧类型: [a0 disassoc]  [b0 auth] [c0 deauth]

--------------

[Connect] bcn_timeout,ap_probe_send_start 是什么意思?
------------------------------------------------------

  在规定时间内(ESP32 默认 6s, 即 60 个 Beacon Interval), STA 未收到 Beacon 帧.
  造成该现象可能有:
  1. 内存不足. "ESP32_WIFI_MGMT_SBUF_NUM" 不够 (log 中会打出 "esf_buf: t=8, l=beacon_len, ..." 这样的 Error). 内存不够，可在收到 disconnect event 时打出 heap 大小来排查.
  2. AP 未发出 beacon. 可通过抓包 AP 的 beacon 来排查.
  3. Rssi 值太低. 在复杂环境下 Rssi 值较低时，可能导致 STA 收不到 beacon. 可通过调用 ``esp_wifi_sta_get_ap_info`` 获取 Rssi 值来排查.
  4. 硬件原因. 收包性能差.

  出现 bcn_timeout 时, STA 会尝试发送 5 次Probe Request, 如果 AP 回 Probe Reponse, 就保持连接, 如果 AP 未回复, STA 发送 Disconnect 事件, 并断开连接.

--------------

[Connect] WiFi连接断开后如何重连?
---------------------------------

  收到 ``WIFI_EVENT_STA_DISCONNECTED`` 之后调用 `esp\_wifi\_connect <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv416esp_wifi_connectv>`__

--------------

[Connect] ESP32 做 soft-AP 时为什么会把sta踢掉?
-----------------------------------------------

  默认情况下连续 5 min 收不到 sta 发过来的数据包就会把 STA 踢掉. 该时间可以通过 `esp\_wifi\_set\_inactive\_time <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv426esp_wifi_set_inactive_time16wifi_interface_t8uint16_t>`__ 进行修改.

  注: esp_wifi_set_inactive_time 新增的 API.

  - master commit: 63b566eb27da187c13f9b6ef707ab3315da24c9d
  - 4.2 commit: d0dae5426380f771b0e192d8ccb051ce5308485e
  - 4.1 commit: 445635fe45b7205497ad81289c5a808156a43539
  - 4.0 commit: MR 未合, 待定
  - 3.3 commit: 908938bc3cd917edec2ed37a709a153182d511da

--------------

[Connect] ESP32作为station时什么时候会把softAP踢掉?
----------------------------------------------------

  默认情况下 6s 未收到 AP 的 beacon 就会把 AP 踢掉. 该时间可以通过 `esp\_wifi\_set\_inactive\_time <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv426esp_wifi_set_inactive_time16wifi_interface_t8uint16_t>`__ 进行修改.

--------------

[Scan] 为什么有时候扫描不到AP?
------------------------------

  常见的原因是AP离sta太远，也有可能是scan的参数配置不恰当导致

--------------

[Scan] 最多能够扫描多少个AP?
----------------------------

  能够扫描到的AP最大个数没有限制，取决于扫描时周边AP的数目与扫描参数的配置，比如每个信道停留的时间，停留时间越长越可能找到全部的AP

--------------

[Scan] 连接时周围存在多个相同 ssid/password 时能否选出最佳AP连接?
-----------------------------------------------------------------

  默认情况下为 WIFI_FAST_SCAN, 总是连接第一个扫描到的AP. 如果要连接最佳AP, 需要在设置 station 时将 scan_method 配置成 WIFI_ALL_CHANNEL_SCAN, 同时配置 sort_method 来决定选择RSSI最强或者是最安全的 AP

--------------

[Scan] wifi_sta_config_t中 scan_method 怎么配置，全信道扫描和快速扫描的区别在哪里?
----------------------------------------------------------------------------------

  全信道扫描和快速扫描是用在连接前寻找合适 AP 所需要的，scan_method 设定了fast_scan，可以配合 threshold 来过滤信号或加密方式不强的 AP，选择了 fast_scan 会在扫描到第一个匹配的 AP 的情况下停止扫描，然后进行连接，节省连接的时间。
  选择了 all_channel_scan 的时候扫描会进行全信道扫描，然后根据 sort_method 中设定的排序方法，存储四个信号最好或者加密方式最安全的 AP，等到扫描结束后选择其中信号最好或者加密方式最安全的AP进行连接。

--------------

[LWIP] 如何获取 socket 的错误码?
--------------------------------

  IDF-v4.0 版本以上(含v4.0) 标准的做法是 socket API 返回失败后直接通过 `errno` 的值来获取错误码.
  IDF-v4.0 版本以下标准的做法是 socket API 返回失败后调用 `getsockopt(sockfd, SOL_SOCKET, SO_ERROR, …)` 的方式获取错误码，否则当多个 socket 并行操作的时候可能会获取到不正确的错误码.

--------------

[LWIP] 默认TCP keepalive时间为多少?
-----------------------------------

  默认情况下，如果连续两个小时收不到任何 TCP 报文，会每隔 75 秒发送一个 TCP keepalive 报文，连续发送 9 个 tcp keepalive 报文依然收不到对方发过来的任何报文 LWIP 会断开 TCP 连接.
  Keepalive 可通过socket option进行配置.

--------------

[LWIP] TCP重传间隔?
-------------------

  ESP32 作为发送方时，默认情况下，首次重传通常在 2~3 秒左右, 之后依据 Jacoboson 算法决定下次重传间隔，重传间隔可以简单地理解为 2 的倍数递增.

--------------

[LWIP] 最多能够创建多少个socket?
--------------------------------

  最多32个，默认为10个.

--------------

[Sleep] 有哪几种休眠方式及其区别是什么?
---------------------------------------

  Modem sleep, Light sleep 和 Deep sleep

  Modem sleep: WiFi 协议规定的 station WMM 休眠方式(station 发送 NULL 数据帧通知 AP 休眠或醒来)，station 连接上 AP 之后自动开启，进入休眠状态后关闭射频模块，休眠期间保持和 AP 的连接，station 断开连接后 modem sleep 不工作。ESP32 modem sleep 进入休眠状态后还可以选择降低 CPU 时钟频率，进一步降低电流。
  Light sleep: 基于 modem sleep 的 station 休眠方式，和 modem sleep 的不同之处在于进入休眠状态后不仅关闭射频模块，还暂停 CPU，退出休眠状态后 CPU 从断点处继续运行。
  Deep sleep: 非 WiFi 协议规定的休眠方式，进入休眠状态后关闭除 RTC 模块外的所有其他模块，退出休眠状态后整个系统重新运行(类似于系统重启)，休眠期间不能保持和 AP 的连接。

--------------

[Sleep] ESP32 modem sleep 降频功能在哪打开?
-------------------------------------------

  在 menuconfig -> Component Config -> Power Management 中打开

--------------

[Sleep] ESP32 modem sleep 降频功能最低能降到多少?
-------------------------------------------------

  目前 CPU 时钟最低能降到 40MHz

--------------

[Sleep] ESP32 modem sleep 平均电流大小影响因素?
-----------------------------------------------

  ESP32 modem sleep 平均电流大小与 CPU 单核还是双核，CPU 时钟频率，CPU 空闲时间比，测试过程中 WiFi 是否有数据收发，数据收发频率，射频模块发射功率，测试路由器发送 beacon 时间点是否准确，是否有外设模块工作等因素有关。

--------------

[Sleep] 为什么测到的 modem sleep 平均电流偏高?
----------------------------------------------

  原因一：测试过程中有较多的 WiFi 数据收发。数据收发越多，进入休眠状态的机会越少，平均电流就越高。
  原因二：测试用的路由器发送 beacon 时间点不准确。Station 需要定时醒来监听 beacon，若 beacon 时间点不准确，station 会等待较长时间，进入休眠状态的时间就越少，平均电流就越高。
  原因三：测试过程中有外设模块在工作，请关闭外设模块再进行测试。
  原因四：开启了 station + softap 模式，modem sleep 只在 station only 模式下才会降低电流。

--------------

[Sleep] 为什么测到的 light sleep 平均电流偏高?
----------------------------------------------

  除了上述四个原因之外还可能是：
  原因五：应用层代码在不停地运行，CPU 没有机会暂停。
  原因六：应用层使用了 ets timer 或者 esp timer，且 timer 的超时时间间隔较短，CPU 没有机会暂停。

--------------

如何获取 802.11 无线数据包?
---------------------------

  推荐的Macbook内置的数据包捕获工具不需要数据包捕获卡. 它可用于捕获 802.11a/b/g/n/ac 数据包:
  https://osxdaily.com/2015/04/23/sniff-packet-capture-packet-trace-mac-os-x-wireless-diagnostics/
  或者，可以使用 Espressif 官方网站上的教程，使用 Wireshark 捕获数据包
  https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/wireshark-user-guide.html

--------------

ESP8266 是否支持 802.11k/v/r 协议?
-----------------------------------------

  当前只支持 802.11k 和 802.11v，可参考示例 `roaming <https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/wifi/roaming>`__。

--------------

[Connect] NONOS_SDK `2.1.0` 升级到 `2.2.2` 后，连接时间变长?
---------------------------------------------------------------

  请升级到 NONOS_SDK `master` 版本，该版本中解决了 CCMP 加密与某些 AP 不兼容的问题。

