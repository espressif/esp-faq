Wi-Fi
=======

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

ESP32 和 ESP8266 是否支持中文 SSID？
----------------------------------------

  ESP32 和 ESP8266 均支持中文 SSID，但需要使用相应的库和设置。需要注意的是，由于中文字符占用的字节数不同，因此使用中文 SSID 时需要特殊处理。

  对于 ESP32，可以使用 ESP-IDF 提供的 Wi-Fi 相关 API。在连接 AP 时，可以使用 `esp_wifi_set_config() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv419esp_wifi_set_config16wifi_interface_tP13wifi_config_t>`_ 函数设置 Wi-Fi 配置，其中的 ssid 参数可以设置为中文字符串。例如：

  .. code-block:: c

    wifi_config_t wifi_config = {
      .sta = {
          .ssid = "你好，世界",
          .password = "password123",
      },
    };
    ESP_ERROR_CHECK(esp_wifi_set_config(ESP_IF_WIFI_STA, &wifi_config));


--------------

[Scan] ESP32 扫描⼀次需要花多长时间？
----------------------------------------

  扫描花费的总时间取决于：

  - 是被动扫描还是主动扫描，默认为主动扫描。
  - 每个信道停留的时间，默认主动扫描为 120 ms，被动扫描为 360 ms。
  - 国家码与配置的信道范围，默认为 1~13 信道。
  - 是快速扫描还是全信道扫描，默认为快速扫描。
  - Station 模式还是 Station-AP 模式，当前是否有连接。

  默认情况下，1~11 信道为主动扫描，12〜13 信道为被动扫描。

  - 在 Station 模式没有连接的情况下，全信道扫描总时间为：11*120 + 2*360 = 2040 ms；
  - 在 Station 模式有连接，或者 Station-AP 模式下，全信道扫描总时间为：11*120 + 2*360 + 13*30 = 2430 ms。

--------------

[Scan] 乐鑫是否支持 boundary scans(边界扫描)？
--------------------------------------------------

  ESP32 不⽀持 boundary scan。

--------------

Wi-Fi 信道是什么？可以自行选择信道吗？
--------------------------------------

  信道指的是 Wi-Fi 使用的指定频段中特定频率的波段。不同国家地区使用的信道数是不同的。例如在北美，Wi-Fi 信道范围是 1 到 11，而在欧洲，Wi-Fi 信道范围是 1 到 13。⽤户可以参考 `ESP8266 Wi-Fi 信道选择指南 <https://www.espressif.com/sites/default/files/documentation/esp8266_wi-fi_channel_selection_guidelines_cn_1.pdf>`_。

--------------

[LWIP] 使用 ESP-IDF v4.1，ESP32 用作 SoftAP 模式时如何设置 IP 地址?
----------------------------------------------------------------------------------

  由于 ESP-IDF v4.1 以及以上版本会摒弃掉 TCP/IP 的接口，推荐使用 `ESP-NETIF <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_netif.html>`_ 的接口.

  参考示例代码如下：

  .. code-block:: c

    {
        ...
        esp_netif_t *ap_netif = esp_netif_create_default_wifi_ap();
        char* ip= "192.168.5.241";
        char* gateway = "192.168.5.1";
        char* netmask = "255.255.255.0";
        esp_netif_ip_info_t info_t;
        memset(&info_t, 0, sizeof(esp_netif_ip_info_t));

        if (ap_netif)
        {
            ESP_ERROR_CHECK(esp_netif_dhcps_stop(ap_netif));
            info_t.ip.addr = esp_ip4addr_aton((const char *)ip);
            info_t.netmask.addr = esp_ip4addr_aton((const char *)netmask);
            info_t.gw.addr = esp_ip4addr_aton((const char *)gateway);
            esp_netif_set_ip_info(ap_netif, &info_t);
            ESP_ERROR_CHECK(esp_netif_dhcps_start(ap_netif));
        }
        ...
    }

--------------

[LWIP] ESP32 Station 模式，如何设置静态 IP？
----------------------------------------------------

  由于 v4.2 以及以上版本会摒弃掉 TCP/IP 的接口，推荐使用 `ESP-NETIF <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_netif.html>`_ 的接口.参考示例代码如下：

  .. code-block:: c

    esp_netif_t *sta_netif = esp_netif_create_default_wifi_sta();
    if (sta_netif)
    {
        esp_netif_ip_info_t info_t = {0};
        esp_netif_dhcpc_stop(sta_netif);

        info_t.ip.addr = ESP_IP4TOADDR(192, 168, 3, 23);
        info_t.gw.addr = ESP_IP4TOADDR(192, 168, 3, 1);
        info_t.netmask.addr = ESP_IP4TOADDR(255, 255, 255, 0);
        esp_netif_set_ip_info(sta_netif, &info_t);
    }
    esp_netif_dns_info_t dns_info = {0};

--------------

[LWIP] ESP-IDF 里如何设置 DHCP Server 的 Option 内容？
--------------------------------------------------------------------

  由于 v4.1 以及以上版本会摒弃掉 tcp/ip 的接口，推荐使用 `ESP-NETIF <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_netif.html>`_ 的接口。DHCP Client 设置方法也可以参考本示例。参考示例代码如下：

  .. code-block:: c

    // 创建 softap 的 netif 句柄
    esp_netif_t *ap_netif = esp_netif_create_default_wifi_ap();

    // ESP_NETIF_IP_ADDRESS_LEASE_TIME, DHCP Option 51, 设置分发的 IP 地址有效时间
    uint32_t dhcps_lease_time = 60; // 单位是分钟
    ESP_ERROR_CHECK(esp_netif_dhcps_option(ap_netif,ESP_NETIF_OP_SET,ESP_NETIF_IP_ADDRESS_LEASE_TIME,&dhcps_lease_time,sizeof(dhcps_lease_time)));

    // ESP_NETIF_DOMAIN_NAME_SERVER , DHCP Option 6, 设置 DNS SERVER
    // 设置 DNS 之前先要设置本地主 DNS
    esp_netif_dns_info_t dns_info = {0};
    dns_info.ip.u_addr.ip4.addr = ESP_IP4TOADDR(8,8,8,8);
    ESP_ERROR_CHECK(esp_netif_set_dns_info(ap_netif,ESP_NETIF_DNS_MAIN,&dns_info));

    uint8_t dns_offer = 1; // 传入 1 使修改的 DNS 生效，如果是 0，那么用 softap 的 gw ip 作为 DNS server (默认是 0)
    ESP_ERROR_CHECK(esp_netif_dhcps_option(ap_netif,ESP_NETIF_OP_SET,ESP_NETIF_DOMAIN_NAME_SERVER,&dns_offer,sizeof(dns_offer)));

    // ESP_NETIF_ROUTER_SOLICITATION_ADDRESS, DHCP Option 3 Router, 传入 0 使 DHCP Option 3(Router) 不出现（默认为 1）
    uint8_t router_enable = 0;
    ESP_ERROR_CHECK(esp_netif_dhcps_option(ap_netif,ESP_NETIF_OP_SET,ESP_NETIF_ROUTER_SOLICITATION_ADDRESS,&router_enable, sizeof(router_enable)));

    // ESP_NETIF_SUBNET_MASK, DHCP Option 1, 设置子网掩码
    // 通过 ESP_NETIF_SUBNET_MASK 设置子网掩码无效， 请通过 esp_netif_set_ip_info 修改

--------------

[Performance] 如何测试 Wi-Fi 模组的通信速率？
--------------------------------------------------

  可以使⽤ ESP-IDF 里的 `iperf <https://github.com/espressif/esp-idf/tree/v4.4.4/examples/wifi/iperf>`_ 示例 进⾏测试。

--------------

[LWIP] ESP8266 SoftAP 默认使用哪个网段？
---------------------------------------------

  ESP8266 SoftAP 默认使用网段 192.168.4.*。

--------------

ESP8266 SoftAP + Station 模式下，连接的 192.168.4.X ⽹段时，为什么会失败？
----------------------------------------------------------------------------------------------

  ESP8266 SoftAP 默认使用网段 192.168.4.*，IP 地址是 192.168.4.1。ESP8266 如果要连接 192.168.4.X 的路由时，不能分辨是要连接⾃⼰本身的 SoftAp 还是外部路由，所以会造成错误。

--------------

[Connect] ESP8266 SoftAP 模式支持几个设备？
-----------------------------------------------

  ESP8266 SoftAP 模式最多可以支持八个设备连接。这是由于 ESP8266 芯片在 SoftAP 模式下使用的 NAT（网络地址转换）机制只支持最多八个设备的连接。
  但需要注意的是，每个连接的设备会占用一定的带宽和资源，因此我们推荐连接四个设备，因为连接过多设备可能会影响 Wi-Fi 模组的性能和稳定性。

--------------

ESP8266/ESP32/ESP32-S2/S3/C2/C3 是否支持 web/softAP 配网？
-----------------------------------------------------------------

  支持。

  - ESP8266 请参考此示例 `ESP8266 softap_prov <https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/provisioning/legacy/softap_prov>`_；
  - ESP32/ESP32-S2/S3/C2/C3 请参考此示例 `ESP32/ESP32-S2/S3/C2/C3 wifi_prov_mgr <https://github.com/espressif/esp-idf/tree/master/examples/provisioning/wifi_prov_mgr>`_。

--------------

[Connect] ESP8266 和 ESP32 作为 softap 模式如何隐藏 SSID？
----------------------------------------------------------------

  要隐藏 ESP8266 或 ESP32 作为 SoftAP 模式下的 SSID，可以通过以下方法实现：

  调用 `esp_wifi_set_config() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv419esp_wifi_set_config16wifi_interface_tP13wifi_config_t>`_ 来配置 SoftAP 模式下的 SSID，密码以及是否隐藏。例如，以下代码设置 SSID 为 "MySoftAP"，密码为 "MyPassword"，函数中使用 .ssid_hidden = 1 选项来隐藏 SSID：

  .. code-block:: c

    wifi_config_t config = {
      .ap = {
        .ssid = "MySoftAP",
        .ssid_len = strlen("MySoftAP"),
        .password = "MyPassword",
        .max_connection = 4,
        .authmode = WIFI_AUTH_WPA_WPA2_PSK
        .ssid_hidden = 1
      },
    };
    esp_wifi_set_config(WIFI_IF_AP, &config);

  配置完后调用 `esp_wifi_start() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv414esp_wifi_startv>`_ 启动 Wi-Fi。

--------------

`esp_wifi_802.11_tx <https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/api-reference/wifi/esp_wifi.html?highlight=esp_wifi_802.11_tx#_CPPv417esp_wifi_80211_tx16wifi_interface_tPKvib>`_ 接口中的 buffer 参数中包括 FCS 吗？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  不包括， FCS 帧是硬件自动生成的。

--------------

ESP-WROOM-32D 支持的 Wi-Fi 频段信息和功率表分别是什么？
-------------------------------------------------------

  Wi-Fi 频段是 2412 ~ 2484 MHz，软件里可配置可用信道和对应的工作频率。功率表有默认值，也可支持软件配置。详细指导请参考 `《ESP32 Phy Init Bin 重要参数配置说明》 <https://www.espressif.com/sites/default/files/documentation/esp32_phy_init_bin_parameter_configuration_guide_cn.pdf>`_。

--------------

ESP32 Wi-Fi RF 功率最高值是多少？
---------------------------------

  ESP32 的 Wi-Fi RF（无线电频率）功率输出最高可以配置为 20 dBm。
  请注意，最大功率输出水平可能会因不同的国家/地区和规定而有所不同。在使用 ESP32 时，请确保您遵守当地的规定和法规，以确保合法和安全使用。另外，高功率输出也会对电池寿命和 Wi-Fi 信号稳定性产生影响，因此在选择功率输出水平时，需要根据具体的应用场景和要求进行权衡和选择。

--------------

ESP32 如何调整 Wi-Fi 的发射功率？
---------------------------------

  - 可通过 menuconfig 配置 ``Component config`` > ``PHY`` > ``Max Wi-Fi TX power(dBm)`` 来调整 Wi-Fi 的发射功率，最大是 20 dBm。
  - 或者使用 API `esp_err_t esp_wifi_set_max_tx_power(int8_t power);` 设置调整。

--------------

[Connect] ESP32 AP 模式最多支持多少设备连接？
----------------------------------------------

  ESP32 AP 模式，最多可配置为支持 10 个设备连接，默认配置为支持 4 设备。

--------------

[Connect] Wi-Fi 模组如何通过 RSSI 数值划分信号强度等级？
---------------------------------------------------------

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

[Connect] ESP32 做 soft-AP 时为什么会把 STA 踢掉？
--------------------------------------------------------

  - 默认情况下连续 5 min 收不到 STA 发过来的数据包就会把 STA 踢掉。该时间可以通过 `esp_wifi_set_inactive_time <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv426esp_wifi_set_inactive_time16wifi_interface_t8uint16_t>`_ 进行修改。

  - 注: esp_wifi_set_inactive_time 新增的 API。

    - master commit: ``63b566eb27da187c13f9b6ef707ab3315da24c9d``
    - 4.2 commit: ``d0dae5426380f771b0e192d8ccb051ce5308485e``
    - 4.1 commit: ``445635fe45b7205497ad81289c5a808156a43539``
    - 4.0 commit: ``0a8abf6ffececa37538f7293063dc0b50c72082a``
    - 3.3 commit: ``908938bc3cd917edec2ed37a709a153182d511da``

--------------

[Connect] ESP32 进行 Wi-Fi 连接时，如何通过错误码判断失败原因？
--------------------------------------------------------------------

  ESP-IDF v4.0 及以上版本可参考如下代码获取 Wi-Fi 连接失败的原因：

  .. code-block:: c

    if (event_base == WIFI_EVENT && event_id == WIFI_EVENT_STA_DISCONNECTED) {
      wifi_event_sta_disconnected_t *sta_disconnect_evt = (wifi_event_sta_disconnected_t*)event_data;
      ESP_LOGI(TAG, "wifi disconnect reason:%d", sta_disconnect_evt->reason);
      esp_wifi_connect();
      xEventGroupClearBits(s_wifi_event_group, CONNECTED_BIT);
    }

  当回调函数接收到 ``WIFI_EVENT_STA_DISCONNECTED`` 事件时，可以通过结构体 `wifi_event_sta_disconnected_t <https://github.com/espressif/esp-idf/blob/5454d37d496a8c58542eb450467471404c606501/components/esp_wifi/include/esp_wifi_types_generic.h#L815>`__ 的变量 ``reason`` 获取到失败原因。

  - ``WIFI_REASON_AUTH_EXPIRE`` 在连接的 auth 阶段，STA 发送了 auth，但在规定时间内未收到 AP 的 auth 回复，有较低概率会出现。

  - ``WIFI_REASON_AUTH_LEAVE`` 通常是由 AP 因为某种原因断开了 STA 连接，reason code 是由 AP 发过来的。

  -  ``WIFI_REASON_4WAY_HANDSHAKE_TIMEOUT`` 或者 ``WIFI_REASON_HANDSHAKE_TIMEOUT`` 失败原因为密码错误。

     其中，``WIFI_REASON_4WAY_HANDSHAKE_TIMEOUT`` 为标准通用的错误码，而 ``WIFI_REASON_HANDSHAKE_TIMEOUT`` 为自定义错误码。两者区别在于 ``WIFI_REASON_4WAY_HANDSHAKE_TIMEOUT`` 为路由器在密码错误时告知设备，产生的错误，``WIFI_REASON_HANDSHAKE_TIMEOUT`` 为路由器在密码错误时不告知设备，由设备本身超时机制产生的错误。

  - ``WIFI_REASON_CONNECTION_FAIL`` 扫描阶段返回的错误码，主要是由于 STA 扫描到了匹配的 AP，但是这个 AP 在黑名单里。AP 在黑名单里面的原因是上次 AP 主动踢掉了 STA，或者 STA 连接 AP 的过程中失败了。

--------------

ESP32 系列芯片每次连接服务器都会执行域名解析吗？
-------------------------------------------------

  在协议栈内，域名会通过 DNS 进行解析，解析后的数据会在时效内进行缓存。缓存时间基于从 DNS 服务器获取的 TTL 数据，该数据是配置域名时填入的参数，通常为 10 分钟。

--------------

[Connect] Wi-Fi Log 中状态机切换后面数字的含义？
-------------------------------------------------

  eg: run -> init (fc0)，fc0 含义为 STA 收到了 deauth 帧，reason 为密码错误。

    - c0 代表收到的帧类型（00 代表超时）
    - f 代表 reason

  帧类型: [a0 disassoc]、[b0 auth]、[c0 deauth]。

--------------

[Connect] bcn_timeout, ap_probe_send_start 是什么意思？
--------------------------------------------------------------

  在规定时间内（ESP32 默认 6 s，即 60 个 Beacon Interval），STA 未收到 Beacon 帧。
  造成该现象可能有:

    - 内存不足。"ESP32_WIFI_MGMT_SBUF_NUM" 不够 (log 中会打出 "esf_buf: t=8, l=beacon_len, ..." 这样的 Error)。内存不够，可在收到 disconnect event 时打出 heap 大小来排查。
    - AP 未发出 beacon。可通过抓包 AP 的 beacon 来排查。
    - Rssi 值太低。在复杂环境下 Rssi 值较低时，可能导致 STA 收不到 beacon，可通过调用 ``esp_wifi_sta_get_ap_info`` 获取 Rssi 值来排查。
    - 硬件原因。收包性能差。

  出现 bcn_timeout 时，STA 会尝试发送 5 次 Probe Request，如果 AP 回 Probe Reponse，就保持连接；如果 AP 未回复，STA 发送 Disconnect 事件，并断开连接。

--------------

[Connect] Wi-Fi 连接断开后如何重连？
------------------------------------------

  收到 ``WIFI_EVENT_STA_DISCONNECTED`` 之后调用 `esp_wifi_connect <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv416esp_wifi_connectv>`_。

--------------

[Connect] ESP32 作为 station 时什么时候会把 SoftAP 踢掉？
-----------------------------------------------------------------

  默认情况下 6 s 未收到 AP 的 beacon 就会把 AP 踢掉。该时间可以通过 `esp_wifi_set_inactive_time <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv426esp_wifi_set_inactive_time16wifi_interface_t8uint16_t>`_ 进行修改。

--------------

[Scan] 为什么有时候扫描不到 AP？
---------------------------------------

  ESP32 和 ESP8266 扫描不到 AP 的原因可能有很多，以下是一些常见的原因和解决方法：

  - AP 距离过远或信号质量差：ESP32 和 ESP8266 的 Wi-Fi 功能只能在一定范围内工作。如果 AP 距离过远或 Wi-Fi 信号质量太差，ESP32 和 ESP8266 可能无法扫描到 AP。可以尝试将 ESP32 或 ESP8266 靠近 AP，或者使用信号增强器来增强 AP 信号强度。
  - AP 的 SSID 隐藏：一些 AP 可能隐藏其 SSID，这意味着它不会被广播到附近的设备。在这种情况下，ESP32 和 ESP8266 无法扫描到 AP。要解决这个问题，您可以手动输入 AP 的 SSID 和密码进行连接。
  - AP 已满载或故障：如果 AP 已满载或故障，它可能无法处理新的连接请求，这会导致 ESP32 和 ESP8266 无法连接到 AP。您可以尝试等待一段时间，然后再次扫描 AP。
  - ESP32 或 ESP8266 的软件问题：有时候，ESP32 或 ESP8266 的软件可能会出现问题，导致无法正确扫描 AP。在这种情况下，您可以尝试重置 ESP32 或 ESP8266，并重新启动 Wi-Fi 功能。如果问题仍然存在，您可能需要更新 ESP32 或 ESP8266 的固件。
  - 其他因素：其他因素，如无线干扰、安全设置、网络配置等，也可能会影响 ESP32 或 ESP8266 的 Wi-Fi 功能。在这种情况下，您需要仔细检查 Wi-Fi 环境并进行相应的设置。

--------------

[Scan] 最多能够扫描多少个 AP？
-----------------------------------

  能够扫描到的 AP 最大个数没有限制，取决于扫描时周边 AP 的数目与扫描参数的配置，比如每个信道停留的时间，停留时间越长越可能找到全部的 AP。

--------------

[Scan] 连接时周围存在多个相同 ssid/password 时能否选出最佳 AP 连接？
----------------------------------------------------------------------------

  默认情况下为 WIFI_FAST_SCAN, 总是连接第一个扫描到的 AP。如果要连接最佳AP，需要在设置 station 时将 scan_method 配置成 WIFI_ALL_CHANNEL_SCAN，同时配置 sort_method 来决定选择 RSSI 最强或者是最安全的 AP。

--------------

[Scan] wifi_sta_config_t 中 scan_method 怎么配置？全信道扫描和快速扫描的区别在哪里？
----------------------------------------------------------------------------------------

  全信道扫描和快速扫描是用在连接前寻找合适 AP 所需要的，scan_method 设定了 fast_scan，可以配合 threshold 来过滤信号或加密方式不强的 AP。

  - 选择了 fast_scan 会在扫描到第一个匹配的 AP 的情况下停止扫描，然后进行连接，节省连接的时间。
  - 选择了 all_channel_scan 的时候扫描会进行全信道扫描，然后根据 sort_method 中设定的排序方法，存储四个信号最好或者加密方式最安全的 AP，等到扫描结束后选择其中信号最好或者加密方式最安全的 AP 进行连接。

--------------

[LWIP] 如何获取 socket 的错误码？
------------------------------------

  - ESP-IDF v4.0 版本以上(含v4.0) 标准的做法是 socket API 返回失败后直接通过 `errno` 的值来获取错误码。
  - ESP-IDF v4.0 版本以下标准的做法是 socket API 返回失败后调用 `getsockopt(sockfd, SOL_SOCKET, SO_ERROR, …)` 的方式获取错误码，否则当多个 socket 并行操作的时候可能会获取到不正确的错误码。

--------------

[LWIP] 默认 TCP keep-alive 时间为多少？
----------------------------------------

  默认情况下，如果连续两个小时收不到任何 TCP 报文，会每隔 75 秒发送一个 TCP keep-alive 报文，连续发送 9 个 tcp keep-alive 报文，如果依然收不到对方发过来的任何报文 LWIP 会断开 TCP 连接。

  Keep-alive 可通过 socket option 进行配置。

--------------

[LWIP] TCP 重传间隔？
-----------------------

  ESP32 作为发送方时，TCP 协议的重传间隔初始值为 3 秒，如果接收方没有发送 ACK 消息，则会依据 Jacoboson 算法决定下次重传间隔,即指数级地增加重传间隔时间，一般是按照 2、4、8、16、32 秒逐渐增加。这个重传间隔时间不是固定的，TCP 协议的实现者可以通过调整一些参数，如超时时间、滑动窗口大小等来影响重传间隔的计算。

--------------

[LWIP] 最多能够创建多少个 socket ？
---------------------------------------

  最多 16 个，默认为 10 个。

--------------

[Sleep] ESP32 有哪几种休眠方式及其区别是什么？
-----------------------------------------------

  - 一共有三种休眠方式: Modem sleep, Light sleep 和 Deep sleep。

    - Modem sleep: WiFi 协议规定的 station WMM 休眠方式(station 发送 NULL 数据帧通知 AP 休眠或醒来)，station 连接上 AP 之后自动开启，进入休眠状态后关闭射频模块，休眠期间保持和 AP 的连接，station 断开连接后 modem sleep 不工作。ESP32 modem sleep 进入休眠状态后还可以选择降低 CPU 时钟频率，进一步降低电流。
    - Light sleep: 基于 modem sleep 的 station 休眠方式，和 modem sleep 的不同之处在于进入休眠状态后不仅关闭射频模块，还暂停 CPU，退出休眠状态后 CPU 从断点处继续运行。
    - Deep sleep: 非 WiFi 协议规定的休眠方式，进入休眠状态后关闭除 RTC 模块外的所有其他模块，退出休眠状态后整个系统重新运行(类似于系统重启)，休眠期间不能保持和 AP 的连接。

--------------

[Sleep] ESP32 modem sleep 动态调频功能在哪打开？
-------------------------------------------------

  在 ``menuconfig`` > ``Component Config`` > ``Power Management`` > ``Support for power management`` > ``Enable dynamic frequency scaling (DFS) at startup`` 中打开。

--------------

[Sleep] ESP32 modem sleep 降频功能最低能降到多少？
----------------------------------------------------

  目前 CPU 时钟最低能降到 40 MHz。

--------------

[Sleep] ESP32 modem sleep 平均电流大小影响因素？
--------------------------------------------------

  ESP32 的 modem sleep 是通过设定一个唤醒周期，每个周期开始时打开芯片的射频进行通信其余时间关闭射频来降低功耗。

  该模式下平均电流的大小受多种因素影响，下面列举了一些主要的影响因素：

  - 唤醒周期：如果设定的唤醒周期越短，则单位时间内芯片唤醒的越频繁，平均电流也会相应增大。
  - 信号质量：如果 Wi-Fi 信号质量较差，芯片会不断尝试重新连接或发送数据，或者改用较大发射功率的通信协议进行数据通信，这些都会导致平均电流增大。
  - 硬件配置：芯片的硬件配置也会对功耗产生影响，如 CPU 单核还是双核、CPU 时钟频率、CPU 空闲时间比、电源电压、是否外接晶振等因素都会对平均电流大小产生影响。
  - 其他因素：例如测试路由器发送 beacon 时间点是否准确，是否发送过多的广播包，芯片本身是否有外设模块工作等

--------------

[Sleep] 为什么测到的 modem sleep 平均电流偏高？
--------------------------------------------------

  - 测试过程中有较多的 Wi-Fi 数据收发。数据收发越多，进入休眠状态的机会越少，平均电流就越高。
  - 测试用的路由器发送 beacon 时间点不准确。Station 需要定时醒来监听 beacon，若 beacon 时间点不准确，station 会等待较长时间，进入休眠状态的时间就越少，平均电流就越高。
  - 测试过程中有外设模块在工作，请关闭外设模块再进行测试。
  - 开启了 station + softap 模式，modem sleep 只在 station only 模式下才会降低电流。

--------------

[Sleep] 为什么测到的 light sleep 平均电流偏高？
-------------------------------------------------

  除了上述四个原因之外还可能是：

  - 应用层代码在不停地运行，CPU 没有机会暂停。
  - 应用层使用了 ets timer 或者 esp timer，且 timer 的超时时间间隔较短，CPU 没有机会暂停。

--------------

[Sleep] ESP32 有哪几种 Wi-Fi 节能模式及其区别？
--------------------------------------------------------------------------

  ESP32 的节能模式一共有三种类型：modem 最小节能模式、modem 最大节能模式、以及不节能模式。

  - modem 最小节能模式：该模式为默认模式。在该模式下，ESP32 从 Light-sleep 中醒来收 beacon 的时间间隔由路由器端的 DTIM 决定，为 (DTIM * 102.4) ms，即假如路由器的 DTIM 为 1，则每隔 100 ms ESP32 会醒来进行一次收包。
  - modem 最大节能模式：在该模式下，ESP32 从 Light-sleep 中醒来收 beacon 的时间间隔由 ``wifi_sta_config_t`` 这个结构体中的 ``listen_interval`` 参数决定，为 (listen interval * 102.4) ms，即假如路由器的 DTIM 为 1，而 listen_interval = 10，则每隔 1 s ESP32 会醒来进行一次收包。
  - 不节能模式：不进行节能处理。

--------------

ESP8266 是否支持 802.11k/v/r 协议？
-----------------------------------------

  当前只支持 802.11k 和 802.11v，可参考示例 `roaming <https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/wifi/roaming>`__。

--------------

ESP32 Wi-Fi 支持相同的 SSID 不同的 AP 之间漫游吗？
-------------------------------------------------------------------------------------------

  支持，当前支持 802.11k 和 802.11v 协议，请参考示例 `roaming <https://github.com/espressif/esp-idf/tree/master/examples/wifi/roaming>`__。

-----------------------------

[Connect] NONOS_SDK `2.1.0` 升级到 `2.2.2` 后，连接时间变长？
----------------------------------------------------------------

  请升级到 NONOS_SDK `master` 版本，该版本中解决了 CCMP 加密与某些 AP 不兼容的问题。

--------------

ESP32 如何收发 Wi-Fi 802.11 数据包？
----------------------------------------

  - 可以通过如下 API 进行 802.11 数据包收发：

  .. code-block:: c

    esp_err_t esp_wifi_80211_tx(wifi_interface_t ifx, const void *buffer, int len, bool en_sys_seq);
    esp_wifi_set_promiscuous_rx_cb(wifi_sniffer_cb);

  - 上述 API 在 MDF 项目中有用到，可以参考：`mconfig_chain <https://github.com/espressif/esp-mdf/blob/master/components/mconfig/mconfig_chain.c>`_。

--------------

[Connect] ESP32 系列 & ESP8266 路由器连接失败有哪些可能原因？
---------------------------------------------------------------

  - 检查配置中的 SSID 与 Password 是否正确。
  - 不建议使用中文 SSID，可能存在不同中文编码带来的异常。
  - 需要注意 bssid_set 的设置，如果不需要指定路由的 MAC 地址，那么需配置 stationConf.bssid_set = 0。
  - wifi_config_t wifi_config 建议使用静态变量 `static` 来定义。

--------------

[Connect] ESP8266 有那些配网方式？
---------------------------------------------------------------

  - SmartConfig 模式：⼀键配置⽅式，设备在 sniffer 模式扫描特征包的⽅式。
  - SoftAP 模式：设备开启 SoftAP， ⼿机连接 SoftAP 后建⽴稳定的 TCP/UDP 连接后，发送 SSID 和密码。
  - WPS 模式：此⽅式需要设备中增加按键；或连接到设备的 SoftAP 后使⽤⼿机软件控制开启 WPS。

--------------

[Connect] SmartConfig 配⽹ Wi-Fi 参数信息有哪些要求？
---------------------------------------------------------------

  SmartConfig 是一种通过局域网广播方式配置 Wi-Fi 参数的方案，用户可以通过使用配套的 APP 将 Wi-Fi 账号和密码发送给设备。下面是 SmartConfig 配网 Wi-Fi 参数信息的要求：

    - SSID 名称：支持中英文和数字字符，长度不超过 32 个字节。
    - Wi-Fi 密码：8-64 个字符，区分大小写。
    - Wi-Fi 安全加密方式：目前 SmartConfig 支持的加密方式有：WPA、WPA2 和 WEP，不支持开放式无加密方式。

--------------

[Connect] ESP8266 Wi-Fi 是否支持 WPA2 企业级加密？
---------------------------------------------------------------

  - 支持。请参考示例 `wpa2_enterprise <https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/wifi/wpa2_enterprise>`_。
  - 可使用 FreeRADIUS 服务搭建 RADIUS 服务器，请参考 `FreeRADIUS <https://freeradius.org/documentation/>`_。

--------------

[Connect] ESP32 保持 Wi-Fi 连接的低功耗模式有哪些？
---------------------------------------------------------------

  - 在保存 Wi-Fi 连接的场景中，芯片会在 Active 和 Modem-sleep 模式之间自动切换，功耗也会在两种模式间变化。
  - ESP32 支持在 light sleep 下 Wi-Fi 保活，自动唤醒间隔由 DTIM 参数决定。
  - 例程参见：ESP-IDF - > examples - > wifi - > power_save。

--------------

乐鑫芯片是否支持 WPA3？
----------------------------------

  - ESP32 系列：esp-idf 从 release/v4.1 版本开始支持 WPA3，默认使能，可在 menuconfig > Component config > Wi-Fi 中配置。
  - ESP8266：ESP8266_RTOS_SDK 的 release/v3.4 分支开始支持 WPA3，默认使能，可在 menuconfig > Component config > Wi-Fi 中配置。

--------------

[Connect] 当环境内存在多个相同 SSID 时，设备如何连接 ？
-----------------------------------------------------------

  - 设备会连接优先扫描到的 AP 设备。
  - 如果想要根据信号质量等排序，可以使用 Scan 方法自主筛选。
  - 如果想要连接指定 AP, 可以在连接参数中填入 BSSID 信息。

--------------

[Connect] ESP8266 有中继器方案吗？
-----------------------------------------------------------

  - 乐鑫官方未推出中继类应用方案。
  - 社区中有相关中继的应用，可以在 github 中查询，中继速率建议基于实际测试。

--------------

ESP32 数据帧和管理帧的重传次数是多少？是否可以配置？
-----------------------------------------------------------

  重传次数是 31 次，不可以配置。

--------------

ESP32 如何自定义 hostname？
---------------------------------------

  - 以 ESP-IDF v4.2 为例，可以在 menuconfig > Component Config > LWIP > Local netif hostname，然后输入指定的 hostname 即可。
  - 不同的版本在命名上可能略有区别。

--------------

如何获取 802.11 无线数据包？
-----------------------------------

  - 可以参考 ESP-IDF 编程文档中的 `Wireshark 使用指南 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/wireshark-user-guide.html>`_ 。
  - 需要注意的是，所使用的无线网卡需要支持 Monitor 模式。

--------------

ESP32 Wi-Fi 支持 PMF(Protected Management Frames) 和 PFS(Perfect Forward Secrecy) 吗？
-----------------------------------------------------------------------------------------------------

  WPA2/WPA3 中均支持 PMF， WPA3 中支持 PFS。

--------------

ESP8266 在使用 esptouch v2 出现 AES PN 错误 log？
------------------------------------------------------------------------------

  ESP8266 收到路由器重传了好几次的包会报这个错误，但是不影响使用。

---------------

ESP32 WFA 认证支持多播吗？
------------------------------------------

  不支持，建议参考 ASD-1148 方式测试。

---------------------------------

使用 ESP32，是否可以在建立热点之前，先扫描所有的 AP 以及所占用的信道，从中选择一个占用最小最干净的信道来建立自己的 AP 呢？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 可以在建立热点之前，先扫描所有的 AP 以及所占用的信道，参考 API esp_wifi_scan_get_ap_records。
  - 不能自动选择最干净的信道来建立自己的 AP，需要自定义信道选择算法。

---------------

使用 ESP32，ESP-IDF 版本为 release/v3.3，Wi-Fi Scan 时，当有多个相同的 SSID 时，获取的列表中有多个重复的 SSID，是否有 API 进行过滤，只保留一个 SSID？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  不能对重复 SSID 进行过滤。因为 SSID 重复不代表是同一个路由器，扫描到的 SSID 相同的路由器的 BSSID 是不同的。

--------------

ESP8266 是否支持 EDCF (AC) 方案？
----------------------------------------------------------------------------

  当前最新 master 版本的 ESP8266-RTOS-SDK 支持 EDCF (AC) 应用，但没有应用实例。您可以在 ``menuconfig`` > ``Component config`` -> ``Wi-Fi`` 配置中开启 Wi-Fi QoS 配置，以获得支持。

---------------

使用 master 版本的  ESP8266-RTOS-SDK，开启 Wi-Fi Qos 应用获得 EDCF 的支持，请问 ESP8266 是如何决定哪个数据包应该分配到 EDCF AC 类别的?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  可以通过设置 IPH_TOS_SET(iphdr, tos) 来确定。

---------------

使用 ESP32，在不考虑内存与功耗的情况下，如何配置最大 Wi-Fi 传输速度与稳定性呢？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  如需配置最大 Wi-Fi 传输速度与稳定性，请参考 ESP-IDF 编程指南中 `如何提高 Wi-Fi 性能 <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.3/esp32/api-guides/wifi.html#how-to-improve-wi-fi-performance>`_，在 menuconfig 中设置相关配置参数即可。配置选项路径可在 menuconfig 界面中，通过 “/” 来搜索。最优配置参数需根据实际当前的环境进行测试。

----------------

ESP8266 作为 Wi-Fi SoftAP 模式，最多支持多少个 Station 设备连接？
--------------------------------------------------------------------------------------------------------------------------------

  ESP8266 最多支持 8 个 Station 设备连接。

------------------------

使用 ESP32 设备作为 Station 模式，如何获取 CSI 数据?
----------------------------------------------------------------------------------------------------------------------------------------------------

  - 通过调用 "esp_wifi_set_csi_rx_cb()" 可获取 CSI 数据。参见 `API <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/network/esp_wifi.html#_CPPv422esp_wifi_set_csi_rx_cb13wifi_csi_cb_tPv>`_ 说明。
  - 具体使用方法参见 `Espressif CSI 示例 <https://github.com/espressif/esp-csi>`_

---------------

ESP32 在 AP + STA 模式连接 Wi-Fi 后，任意开启关闭 AP 模式是否会影响 Wi-Fi 连接？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ESP32 在 AP + STA 双模式下进行 Wi-Fi 连接后，可以任意开启关闭 AP 模式，不影响 Wi-Fi 连接。

-----------------

ESP32 使用 release/v3.3 版本的 ESP-IDF 进行开发，只需要蓝牙功能，如何通过软件关闭 Wi-Fi 功能？
-----------------------------------------------------------------------------------------------------------------

  - 调用 esp_wifi_stop() 可关闭 Wi-Fi 功能。API 说明参见 `esp_err_t esp_wifi_stop(void) <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v3.3/api-reference/network/esp_wifi.html?highlight=wifi_stop#_CPPv413esp_wifi_stopv>`_。
  - 若需要回收 Wi-Fi 占用的资源，则还需要调用 esp_wifi_deinit()，API 说明请参见 `esp_err_t esp_wifi_deinit(void) <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v3.3/api-reference/network/esp_wifi.html?highlight=wifi_deinit#_CPPv415esp_wifi_deinitv>`_。
  - 以下是一个简单的示例代码：

  .. code-block:: c

    #include "esp_wifi.h"
    #include "esp_bt.h"

    void app_main()
    {
      // 关闭 Wi-Fi 功能
      esp_wifi_stop();

      // 初始化蓝牙功能
      esp_bt_controller_config_t bt_cfg = BT_CONTROLLER_INIT_CONFIG_DEFAULT();
      esp_bt_controller_init(&bt_cfg);
      esp_bt_controller_enable(ESP_BT_MODE_BTDM);

      // ...
    }

  在这个示例中，先调用 esp_wifi_stop() 函数关闭 Wi-Fi，然后再初始化蓝牙功能。需要注意的是，一旦关闭了 Wi-Fi 功能，就无法再使用 Wi-Fi 相关的 API 了。


----------------

使用 ESP-IDF 开发，esp_wifi_80211_tx() 接口只能发送数据包，是否有对应的接收函数接口？
---------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 接收数据包是使用回调的方法， 如下：

  .. code-block:: c

    esp_wifi_set_promiscuous_rx_cb(wifi_sniffer_cb);
    esp_wifi_set_promiscuous(true);

  - 另一个开源项目中有用到该方法，可参考 `esp-mdf <https://github.com/espressif/esp-mdf/blob/master/components/mconfig/mconfig_chain.c>`__。

---------------

esptouch 配网失败概率较高的原因有哪些？
------------------------------------------

  :CHIP\: ESP32, ESP32S2, ESP32S3, ESP32C3, ESP8266:

  - 手机连接的热点使用人数较多。
  - 手机连接的热点信号质量较差。
  - 路由器不转发组播数据。
  - 路由器开启了双频合一，手机连接到 5G 频段。

----------------

ESP32 使用 Wi-Fi 时 IRAM 不足，如何优化？
------------------------------------------------------------------------------

  可以在 menuconfig 里关闭 ``WIFI_IRAM_OPT``、``WIFI_RX_IRAM_OPT`` 以及 ``LWIP_IRAM_OPTIMIZATION`` 来优化 IRAM 空间，但这样会降低 Wi-Fi 的性能。

---------------

ESP32 如何测试 Wi-Fi 传输距离？
---------------------------------------------------------------

  可以使用 `iperf 示例 <https://github.com/espressif/esp-idf/tree/master/examples/wifi/iperf>`_ 并配置为 iperf UDP 模式，然后不断地拉开 ESP 设备，检测在怎样的距离 Wi-Fi 数据传输速率会降至 0。

----------------

ESP32 使用 Wi-Fi 通信时 MTU 的长度最大能设置多大，需要在哪进行设置？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

  利用 Wi-Fi 通信时，MTU 的长度最大只能设置为 1500。可通过 LwIP 组件中的 ``netif`` > ``mtu`` 来修改该数值，不过不建议进行修改。

---------------

ESP32 模组挂机测试有时会打印类似如下 log，代表什么含义？
--------------------------------------------------------------------------------

  log 信息如下：

  .. code-block:: text

    [21-01-27_14:53:56]I (81447377) wifi:new:<7,0>, old:<7,2>, ap:<255,255>, sta:<7,0>, prof:1
    [21-01-27_14:53:57]I (81448397) wifi:new:<7,2>, old:<7,0>, ap:<255,255>, sta:<7,2>, prof:1
    [21-01-27_14:53:58]I (81449417) wifi:new:<7,0>, old:<7,2>, ap:<255,255>, sta:<7,0>, prof:1
    [21-01-27_14:53:59]I (81450337) wifi:new:<7,2>, old:<7,0>, ap:<255,255>, sta:<7,2>, prof:1

  - 其中，``new`` 后的数值表示当前主次信道；``old`` 后的数值表示上次主次信道；``ap`` 后的数值表示当前 ESP32 AP 的主次信道，若没有使能 softAP 对应的值就是 255；``sta`` 后的数值表示当前 ESP32 sta 的主次信道；``prof`` 是 nvs 里面存储的 ESP32 softAP 的信道。
  - 有关次信道代表的数值，请参考 `wifi_second_chan_t <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/network/esp_wifi.html#_CPPv420esp_wifi_set_channel7uint8_t18wifi_second_chan_t>`__。
  - 上述 log 信息表示路由器在 HT20 和 HT40 minus 之间切换，可以检查下路由器的 Wi-Fi 频宽设置。

---------------

ESP32 在 AP + STA 模式下，如何关闭 AP 模式?
---------------------------------------------------------------------------------------------------------------

  - 关闭 AP 模式通过 esp_wifi_set_mode(wifi_mode_t mode); 函数来设置。
  - 调用 esp_wifi_set_mode(WIFI_MODE_STA); 即可。

-------------

ESP32 使用 Wi-Fi 的功能后，是否 ADC2 的所有通道都不能使用了？
-------------------------------------------------------------------------------------------------------------------------------------

  ESP32 在使用 Wi-Fi 的情况下，没有被 Wi-Fi 占用的 ADC2 的引脚可以做普通 GPIO 使用。可参考官方 `ADC 说明 <https://docs.espressif.com/projects/esp-idf/zh_CN/v4.4.2/esp32/api-reference/peripherals/adc.html#analog-to-digital-converter-adc>`_。

-----------------------------------------------------------------------------------------------------

Wi-Fi 模块如何设置国家码？
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP8266 | ESP32 | ESP32 | ESP32-C3:

  可以通过调用 `esp_wifi_set_country <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html?highlight=esp_wifi_set_country#_CPPv420esp_wifi_set_countryPK14wifi_country_t>`_  接口设置国家码。

---------------

当 ESP32 用作 SoftAP 连接苹果手机时，手机提示”低安全性　WPA/WPA2(TKIP) 并不安全。如果这是您的无线局域网，请配置路由器以使用 WPA2(AES) 或 WPA3 安全类型“，该如何解决？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  :IDF\: release/v4.0 及以上:

  - 可以参考下面的代码进行设置：

    .. code-block:: c

      wifi_config_t wifi_config = {
          .ap = {
              .ssid = EXAMPLE_ESP_WIFI_SSID,
              .ssid_len = strlen(EXAMPLE_ESP_WIFI_SSID),
              .channel = EXAMPLE_ESP_WIFI_CHANNEL,
              .password = EXAMPLE_ESP_WIFI_PASS,
              .max_connection = EXAMPLE_MAX_STA_CONN,
              .authmode = WIFI_AUTH_WPA2_PSK,
              .pairwise_cipher = WIFI_CIPHER_TYPE_CCMP
          },
      };

  - WIFI_AUTH_WPA2_PSK 是 AES，也叫 CCMP。 WIFI_AUTH_WPA_PSK 是 TKIP。WIFI_AUTH_WPA_WPA2_PSK 是 TKIP+CCMP。

-------------------------------------

ESP32 的 Wi-Fi 模块仅支持 2.4 GHz 频率的带宽，如果在进行连网配置时使用 2.4G 和 5G 多频合一的路由器，Wi-Fi 能否配网成功？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  路由器设置为多频合一的模式（一个 Wi-Fi 账号同时支持 2.4 GHz 和 5 GHz），ESP32 设备可以正常连接 Wi-Fi。

---------------

ESP32 用作 AP 模式时如何获取连接进来的 station 的 RSSI？
---------------------------------------------------------------

  - 可以调用接口 `esp_wifi_ap_get_sta_list <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html?highlight=esp_wifi_ap_get_sta_list#_CPPv424esp_wifi_ap_get_sta_listP15wifi_sta_list_t>`_，参考如下代码：

    .. code-block:: c

      {
          wifi_sta_list_t wifi_sta_list;
          esp_wifi_ap_get_sta_list(&wifi_sta_list);
          for (int i = 0; i < wifi_sta_list.num; i++) {
              printf("mac address: %02x:%02x:%02x:%02x:%02x:%02x\t rssi:%d\n",wifi_sta_list.sta[i].mac[0], wifi_sta_list.sta[i].mac[1],wifi_sta_list.sta[i].mac[2],
                        wifi_sta_list.sta[i].mac[3],wifi_sta_list.sta[i].mac[4],wifi_sta_list.sta[i].mac[5],wifi_sta_list.sta[i].rssi);
          }
      }

  - ``esp_wifi_ap_get_sta_list`` API 获取到的 RSSI 为一段时间内的平均值，不是实时的 RSSI。之前的 RSSI 权重为 13，新的 RSSI 的权重为 3。在 >= 100ms 时更新 RSSI，更新时需要使用旧的 rssi_avg：``rssi_avg = rssi_avg*13/16 + new_rssi * 3/16``。

---------------

ESP32 支持 FTM(Fine Timing Measurement) 吗？
-------------------------------------------------------------------------------

  - 不支持，FTM 需要硬件支持，ESP32 没有对应的硬件。
  - 当前 ESP32-S2 和 ESP32-C3 在硬件上支持 FTM。
  - ESP-IDF v4.3-beta1 开始支持 FTM。
  - 关于 FTM 的更多内容以及例程，请参考 `FTM <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/api-guides/wifi.html#fine-timing-measurement-ftm>`_。

---------------

当 ESP32 设置为 STA+AP 共存时，能否指定通过 STA 或者 AP 接口发送数据？
-------------------------------------------------------------------------------------------------------------------

  **问题背景：**

  ESP32 作为 AP 默认的网段是 192.168.4.x，作为 STA 连接的路由器网段也在 192.168.4.x，PC 连接到该 ESP32 AP 并创建 tcp server，此时 ESP32 作 tcp client 无法建立到 PC 的 tcp 连接。

  **解决方案：**

  - ESP32 可以指定通过 STA 或者 AP 接口发送数据，可参考例程 `tcp_client_multi_net <https://github.com/espressif/esp-idf/tree/master/examples/protocols/sockets/tcp_client_multi_net/>`_。该例程中同时使用了 Ethernet 接口和 STA 接口，可以指定接口发送数据。
  - 有两种方式将 socket 绑定到某个接口：

    - 使用 netif name (使用 socket 选项 SO_BINDTODEVICE)
    - 使用 netif local IP address (通过 esp_netif_get_ip_info() 获取接口 IP，调用 bind() 绑定)

.. note::

  - 绑定 STA 接口可以建立 ESP32 和 PC 的 tcp 连接，绑定 AP 接口无法建立 ESP32 和 PC 的 tcp 连接；
  - 默认情况下可以建立 ESP32 到手机的 tcp 连接(手机作为 STA 接入 ESP32)。

---------------------------------------------------------------------------------------

ESP8266 `wpa2_enterprise <https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/wifi/wpa2_enterprise>`_  如何开启 Wi-Fi 调试功能?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  使用 idf.py menuconfig 开启 menuconfig 配置，然后配置以下参数：

    .. code-block:: c

      menuconfig==>Component config ==>Wi-Fi ==>
      [*]Enable WiFi debug log ==>The DEBUG level is enabled (Verbose)
      [*]WiFi debug log submodule
      [*] scan
      [*] NET80211
      [*] wpa
      [*] wpa2_enterprise

      menuconfig==>Component config ==>Supplicant ==>
      [*] Print debug messages from WPA Supplicant

----------------------------------------------------------------------------------

Wi-Fi 信号格数有对应标准吗?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP8266 | ESP32 | ESP32 | ESP32-C3:

  对于 Wi-Fi 信号格数并没有对应的标准，可以根据接收到的 RSSI 进行折算，比如接收到的 RSSI 范围是 [0,-96]，如果要求信号强度的格数为 5 格，那 [0~-20] 就为满格，以此类推。

--------------------------------------------------------------------------

WFA 漏洞修复最新情况？
--------------------------------------------------------------------------------------------
  :CHIP\: ESP32 | ESP32-S2 | ESP32-C3 |  ESP8266:

  详情请参考乐鑫官网上  `Wi-Fi 安全公告 <https://www.espressif.com/sites/default/files/advisory_downloads/AR2021-003%20Security%20Advisory%20for%20WFA%20vulnerability%20EN_0.pdf>`_。

-----------------------------------------------------------------------------------------------------

Wi-Fi 连接失败时产生的错误码代表什么?
---------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32:

  - Wi-Fi 连接过程中出错都会让状态转移到 init，并且 log 里会有 16 进制数表示，例如 wifi:state, auth-> init(200)。前两位表示原因，后两位表示收到或者发送的管理帧的类型代码。常见的帧类型代码有 00 (什么都没收到，表示超时)、A0（disassoc）、B0（auth）和 C0（deauth）。
  - 前两位表示的原因可以从  `WiFi Reason Code <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/wifi.html#id35>`_ 里查看。后两位可以直接从管理帧代码里查看。

--------------

使用 ESP32 Release/v3.3 版本的 SDK 下载 Station 例程，无法连接不加密的 Wi-Fi，是什么原因？
------------------------------------------------------------------------------------------------------------------------------------

  - 例程下默认是连接加密模式的 AP，如下设置：

    .. code-block:: c

      .threshold.authmode = WIFI_AUTH_WPA2_PSK,

  - 若连接不加密的 AP，需将以下参数改为 0，

    .. code-block:: c

      .threshold.authmode = 0,

  - AP 模式选择说明可参见 `esp_wifi_types <https://github.com/espressif/esp-idf/blob/release/v3.3/components/esp32/include/esp_wifi_types.h>`_。

-------------

ESP32-S2 芯片，Wi-Fi 通信的物理层最大速率是多少？
------------------------------------------------------------------------------------------------------------------------------

  ESP32-S2 Wi-Fi 通信的物理层最大速率为 150 Mbps。

------------------------------------------------------------------------------------------------------------------------------------------------------

ESP 模块是否支持 EAP-FAST?
-------------------------------------------------------------------------------------------------------------------------------------
  :CHIP\: ESP32 | ESP32-S2 | ESP32-C3 :

  支持，请参考 `wifi_eap_fast <https://github.com/espressif/esp-idf/tree/master/examples/wifi/wifi_eap_fast>`_ demo。

---------------

ESP 模块支持 WiFi NAN (Neighbor Awareness Networking) 协议吗？
------------------------------------------------------------------------------------------------
  :CHIP\: ESP8266 | ESP32 | ESP32-C3 | ESP32-S2 | ESP32-S3:

  不支持。

---------------

使用 ESP32，ESP-IDF 版本为 release/v3.3， 配置路由器时，是否有 API 可以直接判断输入的密码不正确？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 没有 API 可直接判断密码错误，依据 Wi-Fi 协议标准，当密码出错时，路由器并不会明确告诉 station 四次握手是由于密码出错了。正常情况下获取密码是 4 个包（1/4 帧、2/4 帧、3/4 帧、4/4 帧），当密码正确时 AP 会发送 3/4 帧，而当密码错误时 AP 不会发送 3/4 帧而是会重发 1/4 帧。 但是当 AP 发送了 3/4 帧，但由于某种原因而在空气中丢掉时，AP 也会重发 1/4 帧。 因此，对于 station 来说，无法准确区分这两种情况，最终都是上报 204 错误，或者 14 错误。
  - 可参考 `Wi-Fi 原因代码 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/wifi.html#id35>`_。

--------------------------

基于 ESP-IDF v4.4 版本的 SDK 测试 ESP32 的 Station 例程，如何支持 WPA3 加密模式？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 开启 ``menuconfig → Component config → Wi-Fi → Enable WPA3-Personal`` 的配置；
  - 在应用程序中设置 ``pmf_cfg`` 里 ``capable = true`` ；
  - 可参考 `Wi-Fi Security <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.4/esp32/api-guides/wifi-security.html#wi-fi-security>`_ 说明。

---------------

ESP32 如何加快 Wi-Fi 的连接速度？
-------------------------------------------------------------------------------

  如下措施均可以加快 ESP32 的 Wi-Fi 连接速度：

  - 设置 CPU 频率到最大，可以加快密钥计算速度。除此外还可以设置 FLASH 参数为 ``QIO、80 MHz``，代价是增加功耗。
  - 关闭 ``CONFIG_LWIP_DHCP_DOES_ARP_CHECK``，可以大幅降低获取 IP 的时间，代价是不检查局域网中是否有 IP 地址冲突。
  - 打开 ``CONFIG_LWIP_DHCP_RESTORE_LAST_IP``，保存上次获得的 IP 地址，dhcp start 时直接发送 dhcp request，省去 dhcp discover 过程。
  - 固定扫描信道。

---------------

ESP32 WPA2 企业级认证是否支持 Cisco CCKM 模式？
-------------------------------------------------------

  目前不支持该模式，虽然 esp_wifi_driver.h 中的枚举有 WPA2_AUTH_CCKM，但是目前不支持。

--------------

使用 wpa2_enterprise（EAP-TLS 方式），客户端证书最大支持长度是多少？
------------------------------------------------------------------------------

  最大支持 4 KB。

--------------

ESP8089 是否支持 Wi-Fi Direct 模式？
--------------------------------------------------------------------------------------------------------------

  ESP8089 支持 Wi-Fi Direct 模式，但 ESP8089 只能使用默认的固定的程序，无法进行二次开发。

--------------

环境中有很多 AP，ESP32 如何连接 RSSI 不低于配置阈值的 AP?
-----------------------------------------------------------------------------------

  在 ESP32 staion 模式下，有一个 `wifi_sta_config_t <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.1/api-reference/network/esp_wifi.html#_CPPv4N13wifi_config_t3staE>`_ 的结构体，下面有 2 个变量，分别是 `sort_method <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.1/api-reference/network/esp_wifi.html#_CPPv4N17wifi_sta_config_t11sort_methodE>`_ 和 `threshold <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.1/api-reference/network/esp_wifi.html#_CPPv4N17wifi_sta_config_t9thresholdE>`_ 变量，通过给这两个变量赋值来设置 RSSI 阈值。

--------------

ESP32 Wi-Fi 出现信标丢失 (beacon lost) 且在 6 秒钟之后给 AP 发 5 个探测请求 (probe request)，此时 AP 没回应就会导致断开连接，这个 6 秒钟可以配置吗?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

  用 API `esp_wifi_set_inactive_time <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/network/esp_wifi.html#_CPPv426esp_wifi_set_inactive_time16wifi_interface_t8uint16_t>`__ 即可配置。

-----------------

ESP32 Wi-Fi 可以使用 PSRAM 吗？
------------------------------------------------------------------------------------------------------

  关于 Wi-Fi 使用 PSRAM 的信息，请参考 `使用 PSRAM <https://docs.espressif.com/projects/esp-idf/zh_CN/v4.4.1/esp32/api-guides/wifi.html#psram>`_。

-----------------

[Connect] ESP32 系列产品如何从软件、硬件方面来排查 Wi-Fi 连不上路由器的问题？
------------------------------------------------------------------------------------------------------

  可以按以下步骤来排查问题：

  - 首先通过 `Wi-Fi 错误码 <https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/software-framework/wifi.html#connect-esp32-wi-fi>`_ 判断可能的失败原因。
  - 然后，当在 ESP32 连接不上路由器时，尝试连接其他设备到该路由器来定位是路由器还是 ESP32 问题：

    - 如手机也无法连上路由器，请排查路由器是否存在问题。
    - 如手机可以正常连上路由器，请排查 ESP32 是否存在问题。

  - 排查路由器问题的步骤：

    - 查看路由器是否处于断电重启的阶段，在此阶段将无法正常连接此路由器，需要等待一段时间至路由器初始化完成后才能正常连接。
    - 查看配置的 SSID 和密码是否与路由器一致。
    - 查看在配置路由器为 OPEN 模式后是否能正常连上。
    - 查看是否能正常连上其他路由器。

  - 排查 ESP32 问题的步骤：

    - 排查 ESP32 硬件部分：

      - 查看是否是特定的 ESP32 才会出现此问题，如仅有固定的少许 ESP32 出现此问题，统计出现问题的 ESP32 的概率并比较它们和正常 ESP32 的硬件差异。

    - 排查 ESP32 软件部分：

      - 查看使用 ESP-IDF 里的 `station 示例 <https://github.com/espressif/esp-idf/tree/v4.4.1/examples/wifi/getting_started/station>`_ 是否能正常连上 Wi-Fi，此处示例里默认存在重连机制，可以同步观察在几次重连后是否能正常连上 Wi-Fi。
      - 查看配置的 SSID 和密码是否与路由器一致。
      - 查看在配置路由器为 OPEN 模式后是否能正常连上。
      - 查看在 Wi-Fi 连接前的代码逻辑里额外调用 API ``esp_wifi_set_ps(WIFI_PS_NONE)`` 后是否能正常连上 Wi-Fi。

  - 如进行上述所有步骤仍然没有定位到问题，建议进行 Wi-Fi 抓包来进一步分析，可参考 `乐鑫 Wireshark 使用指南 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/wireshark-user-guide.html>`_。

-----------------

ESP32 连上路由器后会每 5 分钟会反复打印几次 ``W (798209) wifi:<ba-add>idx:0 (ifx:0, f0:2f:74:9b:20:78), tid:0, ssn:154, winSize:64`` 与 ``W (798216) wifi:<ba-del>idx`` 并明显发现 ESP32 的功耗增大，这是什么原因？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 首先此日志往往没有问题，这里是 Wi-Fi 块确认机制的相关日志，``ba-add`` 表示 ESP32 收到路由器的添加块确认请求帧， ``ba-del`` 表示 ESP32 收到路由器的删除块确认请求帧。打印频繁说明路由器一直在发包。
  - 如果是每五分钟定期观察到此日志，往往是路由器在进行组秘钥更新，可以通过以下步骤来进一步验证：

    - 在 `wpa_supplicant_process_1_of_2() <https://github.com/espressif/esp-idf/blob/v4.4.1/components/wpa_supplicant/src/rsn_supp/wpa.c#L1519>`_ 里进行日志打印来确认是不是每 5 分钟调用了此函数来配合路由器每五分钟进行组秘钥更新。
    - 查看路由器的 Wi-Fi 配置界面是否存在 ``组秘钥更新时间`` 选项并被配置为 5 分钟。

-----------------

ESP32 使用函数 `esp_wifi_config_80211_tx_rate() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv429esp_wifi_config_80211_tx_rate16wifi_interface_t15wifi_phy_rate_t>`_ 为何无法固定 Wi-Fi 发送速率来保持稳定传输？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - `esp_wifi_config_80211_tx_rate() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv429esp_wifi_config_80211_tx_rate16wifi_interface_t15wifi_phy_rate_t>`_ 函数用来配置 `esp_wifi_80211_tx() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv417esp_wifi_80211_tx16wifi_interface_tPKvib>`_ 这个函数的发送速率。
  - 如要设置并固定 Wi-Fi 的发送速率，请使用函数 `esp_wifi_internal_set_fix_rate <https://github.com/espressif/esp-idf/blob/v4.4.1/components/esp_wifi/include/esp_private/wifi.h#L267>`_。

-----------------

ESP32 做 station 连接路由器时发现没有正常获取到 IP，如何调试？
-------------------------------------------------------------------------------------------

  - 打开 lwIP 里 DHCP 的调试日志，在 ESP-IDF menuconfig 配置 ``Component config`` > ``LWIP`` > ``Enable LWIP Debug(Y)`` 和 ``Component config -> LWIP`` > ``Enable DHCP debug messages(Y)``。
  - 早期 IDF 版本没有上述选项时，请参考 `lwipopts.h <https://github.com/espressif/esp-idf/blob/v4.0.1/components/lwip/port/esp32/include/lwipopts.h>`_ 里的 806 到 807 行，将这两行代码里的 ``LWIP_DBG_OFF`` 都改成 ``LWIP_DBG_ON``，如下所示。

    .. code-block:: c

      #define DHCP_DEBUG           LWIP_DBG_ON
      #define LWIP_DEBUG           LWIP_DBG_ON

-----------------

ESP32 做 softAP 时发现连接它的 station 没有正常获取到 IP，如何调试？
-------------------------------------------------------------------------------------------

  请将 `dhcpserver.c <https://github.com/espressif/esp-idf/blob/v4.0.1/components/lwip/apps/dhcpserver/dhcpserver.c#L63>`_ 中的 ``#define DHCPS_DEBUG 0`` 修改为 ``#define DHCPS_DEBUG 1``，即可打开 lwIP 里 DHCP 的调试日志进调试。

-----------------

在 ESP-IDF menuconfig 配置 ``Component config`` > ``PHY`` > ``Max Wi-Fi TX power(dBm)`` 来调整 Wi-Fi 发射功率后实际功率如何？比如设置 17 dBm 时实际最大发射功率是多少？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 对于 ESP32，此时的实际最大发射功率为 16 dbm，具体请参考 `esp_wifi_set_max_tx_power() <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/network/esp_wifi.html#_CPPv425esp_wifi_set_max_tx_power6int8_t>`_ 函数描述的映射规则。
  - 对于 ESP32-C3，在 menuconfig 中配置的最大发射功率值即为实际最大功率值。

-----------------

ESP-IDF 目前支持连接 UTF-8 编码的中文 SSID 路由器，是否有方法连接到编码为 GB2312 的中文 SSID 路由器？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  此时让 ESP 设备端的编码方式和路由器保持一致即可，比如这种情况下让 ESP 设备端也采用基于 GB2312 编码的中文 SSID。

-----------------

ESP32 在连接上路由器后发现在空闲状态下功耗偏高，大约有 60 mA 的平均电流，如何排查？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 此时建议进行 Wi-Fi 抓包来进一步分析，可参考 `乐鑫 Wireshark 使用指南 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/wireshark-user-guide.html>`_。抓包后查看设备发送的 NULL data 包里是否包含 ``NULL(1)``，其中若每 10 秒发送一次 ``NULL(1)`` 则说明是和路由器在进行保活交互。
  - 也可以查看 Wi-Fi 抓包结果里的 beacon 包中 ``TIM(Traffic Indication Map)`` 字段，如果 ``Traffic Indication`` 等于 1，说明存在广播包缓存 (Group Frames Buffered)，ESP32 在此时会打开 RF，导致功耗增高。

-----------------

当 ESP 终端产品需要销往全球时，对应的 Wi-Fi 国家码要如何配置？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 需要在不同国家的产品中，设置不同的 Wi-Fi 国家码。
  - 默认的国家码配置可以用于大多数国家，但不能兼容一些特殊情况。默认的国家码为 ``CHINA {.cc="CN", .schan=1, .nchan=13, policy=WIFI_COUNTRY_POLICY_AUTO}``，在 ESP-IDF v5.0 后，默认为 ``"01" (world safe mode) {.cc="01", .schan=1, .nchan=11, .policy=WIFI_COUNTRY_POLICY_AUTO}）``。由于 12 和 13 信道默认为被动扫描，所以不会违反大多数国家的法规。同时 ESP 终端产品连上路由器后国家码会自动根据路由器改变。断开路由器后，会自动配置为默认的国家码。

  .. note::

    - 此时可能存在一个问题：如果路由器隐藏了 SSID，且于 12 或 13 信道，ESP 终端产品就扫描不到路由器。此时需要设置 ``policy=WIFI_COUNTRY_POLICY_MANUAL`` 来让 ESP 终端产品在 12、13 信道进行主动扫描。
    - 对于其他特殊的国家，比如日本支持 1-14 信道，14 信道只支持 802.11b。ESP 终端产品在默认配置下，无法连接 14 信道的路由器。

-----------------

进行 iperf 测试时发现一段时间后速率会下降甚至中断发射，这是什么原因，需要如何解决？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 可能原因：

    - 网络环境不好
    - 电脑或手机与 ESP32-S2 或 ESP32-S3 softAP 的兼容性问题，导致断线或者吞吐速率下降。
    - 休眠影响了吞吐，在较早的版本时，v5.1 前，进行 iperf 测试最好手动关闭休眠。

  - 解决方法：

    - 针对第一种情况，尝试更换网络环境或者在屏蔽箱里进行测试。
    - 针对第二种情况，关闭 ``menuconfig`` > ``Component config`` > ``Wi-Fi`` > ``WiFi AMPDU RX`` 选项，如果还存在断线现象，关闭 ``menuconfig`` > ``Component config`` > ``Wi-Fi`` > ``WiFi AMPDU TX`` 选项。
    - 针对第三种情况，关闭 Modem-sleep ``esp_wifi_set_ps(WIFI_PS_NONE)``。

  .. note::

    - AMPDU 代表聚合 MAC 协议数据单元，是 IEEE 802.11n 标准中用来提高网络吞吐量的技术。
    - 关闭 ``WiFi AMPDU RX`` 表示不支持接收 AMPDU 包，此时会影响设备的 RX 性能。
    - 关闭 ``WiFi AMPDU TX`` 表示不支持发送 AMPDU 包，此时会影响设备的 TX 性能。

----------------

基于 ESP-IDF v5.0 版本的 SDK 创建 ESP32-S3 设备作为 Wi-Fi AP 模式，当手机连接上 AP 后，会频繁打印如下日志，是什么原因？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    พ (13964) wifi:<ba-del>idx
    ฟ (13964) wifi:<ba-add>idx:2 (ifx:1, 48:2c:a0:7b:4e:ba), tid:0, ssn:5, winSize:64

  打印此日志是因为一直在创建、删除 A-MPDU，此打印只是辅助作用，不影响通信。若需要屏蔽该日志，可以在 Wi-Fi 初始化程序之前加上如下代码进行测试：

  .. code-block:: c

    esp_log_level_set("wifi", ESP_LOG_ERROR);

--------------

ESP32 的网口 (LAN8720) 与 Wi-Fi (Wifi-AP) 能否共存？
---------------------------------------------------------

  可以共存的。将两个连接的检测事件写成一个就可以实现共存。

-----------------

ESP32 在弱网环境或干扰环境下，Wi-Fi 连上以后获取 IP 地址比较慢如何优化？
--------------------------------------------------------------------------------------------

  - 可以在 Wi-Fi start 之后先关闭 Modem-sleep `esp_wifi_set_ps(WIFI_PS_NONE);`, 在获取到 `IP_EVENT_STA_GOT_IP` 事件后再开启 Modem-sleep。
  - 对于断开重连情况，可以在连接之前先主动关闭 Modem-sleep, 获取到 `IP_EVENT_STA_GOT_IP` 事件后再开启 Modem-sleep。
  - 注意：该优化对于 Wi-Fi/BT 共存场景不适用。

-----------------

ESP32/ESP32-S2/ESP32-S3 工作在 SoftAP 模式时，与其他厂商手机、PC 等进行通信时容易出现断连该如何优化？
---------------------------------------------------------------------------------------------------------------------------------------

  - 建议关闭 menuconfig 里的 ``WiFi AMPDU RX`` 和 ``WiFi AMPDU TX`` 选项。
  - 如果需要进一步确认详细原因，可以进行抓包分析。

----------------

ESP32 Wi-Fi TX power 的取值范围是多少？
---------------------------------------------------------------------------------------------------------

  - ESP32 Wi-Fi TX power 的取值范围为 2-20 dBm。在 ESP-IDF 中，可以使用函数 ``esp_wifi_set_max_tx_power()`` 设置 TX power 的最大值，同时也可以使用 ``esp_wifi_get_max_tx_power()`` 函数获取当前系统所支持的最大 TX power 值。
  - 需要注意的是，设置 TX power 过高可能会影响系统的稳定性和电池寿命，同时也可能违反国家和地区的无线电规定，因此应该谨慎使用。详细请参考 `esp_wifi_set_max_tx_power API <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv425esp_wifi_set_max_tx_power6int8_t>`__。

--------------

使用 ESP32 时如何获取 Wi-Fi RSSI 值？
-----------------------------------------------------------------------------------------------

  在 ESP-IDF release/v4.1 中，当 ESP32 作为 station 使用时，要获取连接到的 AP 的 RSSI，可以使用以下代码示例：

  .. code-block:: c

    wifi_ap_record_t ap_info;
    if (esp_wifi_sta_get_ap_info(&ap_info) == ESP_OK) {
      int rssi = ap_info.rssi;
      // 处理 rssi
    }

  ``wifi_ap_record_t`` 结构体中包含了连接到的AP的信息，包括 SSID 、BSSID 、频道、加密方式等， RSSI 字段则表示 AP 的RSSI 值。调用 ``esp_wifi_sta_get_ap_info()`` 函数即可获取该结构体信息。
  API 说明参见 `esp_err_t esp_wifi_sta_get_ap_info(wifi_ap_record_t *ap_info) <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/network/esp_wifi.html#_CPPv424esp_wifi_sta_get_ap_infoP16wifi_ap_record_t>`_。

--------------

ESP32 支持 WPA3 企业版吗？
--------------------------------------------------------------------------------------------------------

  - ESP32 支持 WPA/WPA2/WPA3/WPA2-Enterprise/WPA3-Enterprise/WAPI/WPS 和 DPP Wi-Fi 功能。有关信息，请参考`ESP32 Wi-Fi 功能列表 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/wifi.html#esp32-wi-fi-feature-list>`__。
  - 在 esp-idf release/v5.0 版本 SDK 中，我们提供了 `wifi_enterprise 示例 <https://github.com/espressif/esp-idf/tree/v5.0/examples/wifi/wifi_enterprise>`__。 在 ESP-IDF 中，支持设置 WPA3-Enterprise 模式进行测试。可通过如下步骤进行配置 ``idf.py menuconfig`` > ``Example Configuration`` > ``Enterprise configuration to be used`` > ``WPA3_ENT``。

---------------

ESP 模组支持 WAPI (Wireless LAN Authentication and Privacy Infrastructure) 功能吗？
--------------------------------------------------------------------------------------------------------------------------------

  支持，请参考 `Wi-Fi 功能列表 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/wifi.html#esp32-wi-fi>`__。

-------------

使用 ESP32 作为 Wi-Fi Station 连接路由器，如何增加扫描路由器的时间？
---------------------------------------------------------------------------------------------------------------

  - 在 ESP32 中，默认情况下 1 ~ 11 信道为主动扫描，12 ~ 13 信道为被动扫描。主动扫描和被动扫描所需时间不同，详情可参考 `Wi-Fi 扫描配置 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/wifi.html#id19>`_。主动扫描的默认时间是每个信道 120 ms，被动扫描为每个信道 360 ms。如果希望增加扫描时间，可在 ``esp_wifi_start()`` 函数之前，调用如下函数来增加扫描路由器的时间：

  .. code-block:: c

      extern void scan_set_act_duration(uint32_t min, uint32_t max);
      extern void scan_set_pas_duration(uint32_t time);
      scan_set_act_duration(50, 500);
      scan_set_pas_duration(500);
  
  - 或者可以直接通过修改 ``wifi_ap_record_t`` 结构体里的值修改主动扫描和被动扫描的时间

  .. note::

    - 由于一个 beacon 的时间间隔一般在 102.4 ms，主动扫描的时间不宜小于这个时间，尽量在 120 ms 及以上。

-------------

ESP32 是否支持 LDPC？
---------------------------------------------------------------------------------------------------------------

  支持。ESP32 已经在驱动中实现 LDPC，无需额外配置或调用。

-------------

ESP 模组支持 WAPI AS 吗？
---------------------------------------------------------------------------------------------------------------

  不支持。WAPI 有两种鉴别方式，即证书鉴别方式和预共享密钥鉴别方式。目前，ESP 模组只支持预共享密钥鉴别方式 (WAPI-PSK)，而 WAPI AS 则是用于证书鉴别方式。

-------------

当基于 UDP 进行传输测试时，出现 ``Error occurred during sending: errno 12`` 时应该怎么处理？
----------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 返回值是 12 表示空间不足，造成这个的原因是上下层处理速度不匹配。上层应用不断产生大量的数据并发给 UDP 协议进行传输，但是底层网络或接收端的能力无法跟上发送速度，就会导致数据堆积空间不足。
  - 处理这种问题的方法是可以对这个返回值进行处理，比如收到这个返回值后上层进行重发，或者上层添加 delay 来延缓发送速度。

---------------

ESP 模组支持 Wi-Fi HaLow 功能吗？
------------------------------------------------------------------------------------------------------------------

  不支持，Wi-Fi HaLow 基于 802.11ah 协议。

--------------

在 ESP32 Wi-Fi Scan 模式下如何实现不发送任何射频波？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 使用 `esp_wifi_scan_start() <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v5.2/esp32/api-reference/network/esp_wifi.html?highlight=wifi_scan#_CPPv419esp_wifi_scan_startPK18wifi_scan_config_tb>`_ API 将 ESP32 设置为被动扫描模式 `WIFI_SCAN_TYPE_PASSIVE <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v5.2/esp32/api-reference/network/esp_wifi.html?highlight=wifi_scan#_CPPv4N16wifi_scan_type_t22WIFI_SCAN_TYPE_PASSIVEE>`_ 即可。

-------------

ESP32-C6 开启 Wi-Fi AP 模式时，默认使用的 802.11 Wi-Fi 协议类型是什么？
----------------------------------------------------------------------------------------------------------------------------------------------

  - ESP32-C6 开启 Wi-Fi AP 模式时，默认使用 802.11b/g/n 混合模式。可通过 `esp_wifi_set_protocol() <https://docs.espressif.com/projects/esp-idf/zh_CN/v5.1.2/esp32c6/api-reference/network/esp_wifi.html#_CPPv421esp_wifi_set_protocol16wifi_interface_t7uint8_t>`_ 设置协议类型。

-------------------

ESP32 Wi-Fi Station 无法连接上 2.4 GHz Enhanced Open mode 模式的 Wi-Fi 热点，是什么原因？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 仅在 release/v5.2 及以上版本的 ESP-IDF SDK 上支持连接 2.4 GHz 的 Enhanced Open mode 模式的 Wi-Fi 热点。并且在软件上需要开启 ``Component config > ``Wi-Fi`` > ``Enable OWE STA`` 配置选项，请参见 `Wi-Fi Enhanced Open <https://github.com/espressif/esp-idf/blob/release/v5.2/docs/en/api-guides/wifi-security.rst#wi-fi-enhanced-open>`_ 说明。

--------------

如何判断连上的 Wi-Fi 是 Wi-Fi 4 还是 Wi-Fi 6？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 可以使用 `esp_wifi_sta_get_negotiated_phymode(wifi_phy_mode_t *phymode) <https://github.com/espressif/esp-idf/blob/5f4249357372f209fdd57288265741aaba21a2b1/components/esp_wifi/include/esp_wifi.h#L1454>`__ API 来得到当前连接的 station 的模式。以下是使用示例：
    
  .. code-block:: c

      wifi_phy_mode_t phymode;
      esp_wifi_sta_get_negotiated_phymode(&phymode);
      printf("111=%d\n",phymode);
  
  - 如果打印的值是 3，则表明用 Wi-Fi 4 和 station 建立了连接，如果打印的值为 5，则表明用 Wi-Fi 6 和 station 建立了连接。

--------------

ESP32-S3 支持 AP 和 STA 同时工作吗？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
  - 支持，参考例程 `softap_sta <https://github.com/espressif/esp-idf/tree/v5.2/examples/wifi/softap_sta>`_。

--------------

ESP Wi-Fi 模块在 SoftAp 模式下支持省电机制吗？
------------------------------------------------------------------------------------------------------------------------------------
 
  目前暂不支持该功能。

--------------

ESP32S3 FTM 支持最大测距带宽能达到多少呢？
----------------------------------------------------------------------------------------------------------------------------------------
  
  最大测距带宽支持到 40 MHz。

--------------

ESP 芯片支持一个 STA 同时和多个 AP 进行 FTM 吗？
------------------------------------------------------------------------------------------------------------------------------------
 
  不支持，STA 一次只能对一个 AP 执行 FTM。

-------------

在 WiFi Station 模式下，当路由器同时开启 WiFi 4 和 WiFi 6 模式时，ESP32-C6 将使用哪种 WiFi 模式与路由器建立连接？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ESP32-C6 将优先使用 WiFi 6 与路由器建立连接。

-----------------

在 WiFi AP 模式下，ESP32-C2 系列产品最多支持几个 WiFi Station 设备连接？
-------------------------------------------------------------------------------------------------------------------------------------------------

  - 由于硬件限制，ESP32-C2 在 WiFi AP 模式下最多支持四个 WiFi Station 连接。
  - 不同型号的芯片在 WiFi AP 模式下支持的最大连接数不一样，详情请参阅 `esp-idf/components/esp_wifi/include/esp_wifi_types.h <https://github.com/espressif/esp-idf/blob/a322e6bdad4b6675d4597fb2722eea2851ba88cb/components/esp_wifi/include/esp_wifi_types.h#L379>`_。

---------------

ESP32 支持 WPA3 WiFi AP 模式吗？
-----------------------------------------------------------------------------------------------------------------------

 支持。ESP-IDF v5.1 及以上版本支持 WPA3 WiFi AP 模式，参见 `ESP-IDF v5.1 Release <https://github.com/espressif/esp-idf/releases/tag/v5.1>`_ 中的说明。

---------------

ESP 芯片在 SoftAP 模式下支持 Short GI 吗？
------------------------------------------------------------------------------------------------------------------------------------
 
  目前暂不支持该功能。

---------------

STA 和 AP 是否需要先建立连接才能执行 FTM？
-----------------------------------------------------------------------------------------------------------------

  不需要建立连接，STA 可以直接通过 AP 启动 FTM。建议先扫描 AP，确认其是否支持 FTM 应答模式。具体操作可以参考 esp-idf/wifi 目录下的 `FTM 示例 <https://github.com/espressif/esp-idf/tree/master/examples/wifi/ftm>`_。

---------------

ESP 芯片在 SoftAP 模式下支持 uAPSD 吗？
------------------------------------------------------------------------------------------------------------------------------------
 
  uAPSD 是一种 Wi-Fi 功能, 可在低周期性滞后时间敏感的通信模式（如 VoIP）中为客户端节约功耗。ESP 芯片目前不支持该功能。

-----------------

基于 Espressif 系列的产品启用 WiFi AP 模式时，是否支持设置自动信道？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Espressif 系列的产品是 WiFi 软 AP (SoftAP) 模式，不支持设置自动信道。

-------------

ESP 系列的产品是否支持作为 Wi-Fi AP 模式的漫游功能？
-----------------------------------------------------------------------------------------------------------------------

  - 不支持。ESP 系列的产品仅支持作为 Wi-Fi Station 模式连接支持漫游特性的路由器。
  - 软件参考：`esp-idf/examples/wifi/roaming <https://github.com/espressif/esp-idf/tree/release/v5.3/examples/wifi/roaming>`_。
