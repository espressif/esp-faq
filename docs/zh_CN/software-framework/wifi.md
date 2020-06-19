# wifi

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## ESP32 ESP-Now 模式下一对一的通信速率是多少？

测试数据如下：

- 测试样板：ESP32_Core_board_V2。
- Wi-Fi 模式：station 模式。
- open 环境下大约是 214kbps。
- 屏蔽箱内测试大约是 555kbps。

---

## 如何修改默认上电校准⽅式？

- 上电时 RF 初始化默认采⽤部分校准的⽅案：
  esp_init_data_default.bin 中第 115 字节为 0x01，RF 初始化时间较短。
- 不关注上电启动时间，可修改使⽤上电全校准⽅案：
**使⽤ NONOS SDK 及 RTOS SDK 3.0 以前的版本：**
  - 在 user_pre_init 或 user_rf_pre_init 函数中调 ⽤system_phy_set_powerup_option(3)；
  - 修改 phy_init_data.bin 中第 115 字节为 0x03。
**使⽤ RTOS SDK 3.0 及以后版本：**
  - 在 menuconfig 中关闭 CONFIG_ESP_PHY_CALIBRATION_AND_DATA_STORAGE；
  - 如果在 menuconfig 中开启了 CONFIG_ESP_PHY_INIT_DATA_IN_PARTITION，修改 phy_init_data.bin 中第 115 字节为 0x03；
  如果没有开启 CONFIG_ESP_PHY_INIT_DATA_IN_PARTITION，修改 phy_init_data.h 中第 115 字节为 0x03。
  **继续使⽤上电部分校准⽅案，若需在业务逻辑中增加出发全校准操作的功能：**
  - 使⽤ NONOS SDK 及 RTOS SDK 3.0 以前的版本：擦除 RF 参数区中的内容，触发全校准操作
  - 使⽤ RTOS SDK 3.0 及以后版本：擦除 NVS 分区中的内容，触发全校准操作

---

## ESP32 和 ESP8266 是否支持中文 SSID？

是支持的，使用中需要路由器或者手机的中文编码方式一致。
示例：路由器中文编码使用 UTF-8 ，设备中文编码使用 UTF-8 ，设备就可以正确连接中文 SSID 的路由器。

---

## ESP32 扫描⼀次需要花多长时间？

扫描花费的总时间取决于:

- 是被动扫描还是主动扫描，默认为主动扫描。
- 每个信道停留的时间，默认主动扫描为 120 ms，被动扫描为 360 ms。
- 国家码与配置的信道范围，默认为 1~13 信道。
- 是快速扫描还是全信道扫描，默认为快速扫描。
- Station 模式还是 Station-AP 模式，当前是否有连接。

默认情况下，1~11 信道为主动扫描，12〜13 信道为被动扫描。

- 在 Station 模式没有连接的情况下，全信道扫描总时间为：11*120 + 2*360 = 2040 ms；
- 在 Station 模式有连接，或者 Station-AP 模式下，全信道扫描总时间为：11*120 + 2*360 + 13\*30 = 2430 ms。

---

## boundary scan

> Does Espressif support boundary scans？

ESP32 不⽀持 boundary scan.

---

## 客户⾃研产品如何优化⼆次谐波等杂散？

⼆次谐波主要来源于射频链路路辐射和 PA 电源辐射，同时易易受到客户底板（板⼦尺⼨）及产品整机影响，因此有如下建议：在射频匹配中使⽤ ⼀个接近 2.4pF ⼤⼩的对地电容，可较好地优化射频链路路上的杂散辐射；在 PA 电源 (芯⽚ 3、4 管脚) ⼊⼝增加⼀个串串联电感可较好减少 PA 电源的杂散辐射。

---

## Wi-Fi 信道是什么？可以自行选择信道吗？

1. 信道指的是 Wi-Fi 使用的指定频段中特定频率的波段。不同国家地区使用的信道数是不是同的。
2. ⽤户可以参考[《ESP8266 Wi-Fi 信道选择指南》](https://www.espressif.com/zh-hans/support/documents/technical-documents)

---

## 80MHz 倍频杂散较差该如何解决？

若 80MHz 倍频杂散超标，如 160MHz、240MHz、320MHz 等均⽐较⾼，可在发送数据 (TXD) 串⼝线路路中串联⼀个阻值约为 470Ω 的电阻，即可有效抑制 80MHz 倍频杂散。

---

## ESP32 Station 模式，如何设置静态 ip ？

- 由于 V4.2 以及以上版本会摒弃掉 tcp/ip 的接口，推荐使用 ethif 的接口.
- 参考示例代码如下：

``` c
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
```

---

## 如何测试 Wi-Fi 模组的通信速率？

- 可以使⽤ SDK 中提供的示例 `example/wifi/iperf` 中代码进⾏测试。

---

## ESP8266 SoftAP 默认使用哪个网段 ？

> ESP8266 SoftAP + Station 模式下, 连接的 192.168.4.X ⽹段时，为什么会失败 ？

- ESP8266 SoftAP 默认使用哪个网段 192.168.4.*，IP 地址是 192.168.4.1。
- ESP8266 如果要连接 192.168.4.X 的路由时，不能分辨是要连接⾃⼰本身的 SoftAp 还是外部路由，所以会造成错误。

---

## ESP8266 SoftAP 模式支持几个设备 ？

- 硬件上最多⽀持 8 个，我们推荐 4 个，这样可以保证模组性能。
