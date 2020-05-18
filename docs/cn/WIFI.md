# Wi-Fi

## wifi 性能指标

- `Q:`
  
- 乐鑫芯⽚支持的 Wi-Fi 协议以及性能指标有哪些？
  
- `A:`

  | Standard/Speed (bps) | TX EVM (db) | TX Power (dbm) | RX EVM (db) | RX Sensitivity (dbm)|
  | :---------------------| :--------: | :----------: | :-------: | :----------------: |
  | 802.11b 1M                    | -10 | 19.5 ± 2 dB | -17 | -98 |
  | 802.11b 2M                    | -10 | 19.5 ± 2 dB | -17 | -96 |
  | 802.11b 5.5M                  | -10 | 19.5 ± 2 dB | -17 | -94 |
  | 802.11b 11M                   | -10 | 19.5 ± 2 dB | -17 | -91 |
  | 802.11g 6M                    | -5  | 18 ± 2   dB | -19 | -93 |
  | 802.11g 9M                    | -8  | 18 ± 2   dB | -19 | -92 |
  | 802.11g 12M                   | -10 | 18 ± 2   dB | -19 | -90 |
  | 802.11g 18M                   | -13 | 18 ± 2   dB | -20 | -88 |
  | 802.11g 24M                   | -16 | 16.5 ± 2 dB | -20 | -85 |
  | 802.11g 36M                   | -19 | 16.5 ± 2 dB | -24 | -82 |
  | 802.11g 48M                   | -22 | 15 ± 2   dB | -26 | -78 |
  | 802.11g 54M                   | -25 | 14 ± 2   dB | -27 | -74 |
  | 802.11n HT20 MCS0/6.5M/7.2M   | -5  | 18 ± 2   dB | -19 | -90 |
  | 802.11n HT20 MCS1/13M/14.4M   | -10 | 18 ± 2   dB | -19 | -90 |
  | 802.11n HT20 MCS2/19.5M/21.7M | -13 | 18 ± 2   dB | -21 | -87 |
  | 802.11n HT20 MCS3/26M/28.9M   | -16 | 16.5 ± 2 dB | -20 | -84 |
  | 802.11n HT20 MCS4/39M/43M     | -19 | 16.5 ± 2 dB | -23 | -81 |
  | 802.11n HT20 MCS5/52M/57.8M   | -22 | 15 ± 2   dB | -26 | -77 |
  | 802.11n HT20 MCS6/58.5M/65M   | -25 | 14 ± 2   dB | -27 | -75 |
  | 802.11n HT20 MCS7/65M/72M     | -27 | 13 ± 2   dB | -29 | -71 |
  | 802.11n HT40 MCS0/6.5M/7.2M   | -5  | 18 ± 2   dB | -19 | -89 |
  | 802.11n HT40 MCS1/13M/14.4M   | -10 | 18 ± 2   dB | -19 | -87 |
  | 802.11n HT40 MCS2/19.5M/21.7M | -13 | 18 ± 2   dB | -21 | -84 |
  | 802.11n HT40 MCS3/26M/28.9M   | -16 | 16.5 ± 2 dB | -20 | -82 |
  | 802.11n HT40 MCS4/39M/43M     | -19 | 16.5 ± 2 dB | -23 | -79 |
  | 802.11n HT40 MCS5/52M/57.8M   | -22 | 15 ± 2   dB | -26 | -75 |
  | 802.11n HT40 MCS6/58.5M/65M   | -25 | 14 ± 2   dB | -27 | -73 |
  | 802.11n HT40 MCS7/65M/72.2M   | -27 | 13 ± 2   dB | -29 | -69 |

## 802.11 raw 报文

- `Q:`
  - 如何发送 RAW 802.11 报文？

- `A:`
  - 可调用 esp_wiﬁ_80211_tx 发送 (IDF v3.1 可⽤)。

## 无法连接路由器

- `Q:`
  - 路由器配置是正确的，但是发生找不到路由，连接失败，为什么？

- `A:`
  - 如果 SSID 和密码配置是正确的，可能的原因有 2 个：
    - 推荐使⽤用英⽂文字符，不不要使⽤用中⽂文。
    - 需要注意 bssid_set 的设置，如果不不需要指定路路由的 MAC 地址，那么需配置 stationConf.bssid_set = 0。

## 无法修改 ESP8266 的 SoftAP SSID 和 PASSWORD

- `Q:`
  
- 调⽤ wiﬁ_softap_set_conﬁg() 时，函数返回成功，但为何⽆法修改 ESP8266 的 SoftAP SSID 和密码？
  
- `A:`
  - 使⽤用函数 wiﬁ_softap_set_conﬁg() 时，如果 API 从回调函数内部调⽤用，ESP8266 SoftAP 的配置有时候会修改失败。例例如，当应⽤用程序试图在 SoftAP 事件的回调函数内，从 SoftAP 模式切换到 Station 模式时，可能出现这种情况。
  - 为确保 wiﬁ_softap_set_conﬁg() 所做的修改⽴立即⽣生效，请使用 system_os_task() API 创建一个更改 SoftAP 设置的任务。在调⽤任何 SoftAP API 之前，请确保 ESP8266 已成功切换到 SoftAP 模式。例如：

    ```c
    LOCAL void ICACH_FLASH_ATTR

    some_callback_function (void)
    {
    unsigned char res;
    os_event_t *testQueue;
    res = wifi_set_opmode_current (0x02); // 确保 ESP8266 处于 SoftAP 模式。
    os_printf ("\r\nSet op mode returned: %d", res);
    testQueue = (os_event_t *)os_malloc(sizeof(os_event_t)*4);
    system_os_task (set_ap_config, USER_TASK_PRIO_1, testQueue, 4);
    ap_server_setup (AP_PORT); // 继续设置服务器等。
    }

    void set_ap_config (os_event_t *e)
    {
    struct softap_config ap;
    wifi_softap_get_config(&ap);
    os_memset(ap.ssid, 0, 32);
    os_memset(ap.password, 0, 64);
    os_memcpy(ap.ssid, "SSIDhere", 8);
    os_memcpy(ap.password, "PASSWDhere", 10);
    ap.authmode = AUTH_WPA2_PSK;
    ap.ssid_len = 0; // 或者 SSID 的实际 ⻓度。
    ap.max_connection = 1; // 允许接⼊ Station 的最⼤数量
    wifi_softap_set_config (&ap); // 更新 ESP8266 SoftAP 设置
    }
    ```

## Wi-Fi 信道是什么

- `Q:`
  - Wi-Fi 信道是什么？可以自行选择信道吗？

- `A:`
  - 信道指的是 Wi-Fi 使用的指定频段中特定频率的波段。不同国家地区使用的信道数是不是同的。  
  - ⽤户可以参考[《ESP8266 Wi-Fi 信道选择指南》](https://www.espressif.com/zh-hans/support/documents/technical-documents)

## ESP8266 配置

- `Q:`
  
- 如何配置 ESP8266，以便连接到⽆线路由器？
  
- `A:`
  - 有关配置连接⽆线路路由器 ， ⼀般有以下⼏种⽅式：
  1. smartconfig ⼀键配置⽅式，设备在 sniffer 模式扫描特征包的⽅式。
  2. 设备开启 SoftAP， ⼿机连接 SoftAP 后建⽴稳定的 TCP/UDP 连接后，发送 SSID 和密码。
  3. WPS 配置⽅式，此⽅式需要设备中增加按键；或连接到设备的 SoftAP 后使⽤⼿机软件控制开启 WPS。

## 开启 SoftAP + Station 模式连接的路由失败

- `Q:`
  - 设备开启 SoftAP + Station 模式下，连接的路由是 192.168.4.X ⽹段时，为什么会失败？

- `A:`
  - ESP8266 SoftAP 默认 IP 地址是 192.168.4.1。
  - ESP8266 如果要连接 192.168.4.X 的路由时，不能分辨是要连接⾃⼰本身的 SoftAp 还是外部路由，所以会造成错误。

## ESP8266 wifi 11n

- `Q:`
  - ESP8266 softap 模式下是否⽀持 wifi 11n？

- `A:`
    1. ⽀持 11n 的部分 feature，有些硬件限制的⽆法⽀持，有些软件可实现的会继续添加。
    2. 可通过 esp8266 datasheet 看到具体的⽀持功能，包括：⽀持的速率、协议等；如 `最⾼只能到 72M`

## ESP8266 ⽹络问题

- `Q:`
  
- ESP8266 SoftAP + Station 模式下⽹络断开或丢包的情况？
  
- `A:`
  - 虽然 ESP8266 ⽀持 SoftAP + Station 共存模式，但是 ESP8266 实际只有⼀个硬件信道，由 ESP8266 Station 与 SoftAP 接⼝共⽤。因此在 SoftAP + Station 模式时，ESP8266 SoftAP 会动态调整信道值与 ESP8266 Station ⼀致。这个限制会导致 ESP8266 SoftAP + Station 模式时⼀些⾏为上的不便，⽤户请注意。例如：
  
  **情况⼀：**
      - 如果 ESP8266 Station 连接到 ⼀个路由 (假设路路由信道号为 6)；
      - 通过接⼝ wifi_softap_set_config 设置 ESP8266 SoftAP；
      - 若设置值合法有效，该 API 将返回 true，但信道号仍然会⾃动调节成与 ESP8266 Station 接⼝⼀致，在这个例⼦⾥也就是信道号为 6。

  **情况⼆：**
      - 调⽤接⼝ wifi_softap_set_config 设置 ESP8266 SoftAP (例例如信道号为 5)；
      - 其他 Station 连接到 ESP8266 SoftAP；
      - 将 ESP8266 Station 连接到路由 (假设路路由信道号为 6)；
      - ESP8266 SoftAP 将⾃动调整信道号与 ESP8266 Station ⼀致 (信道 6);
      - 由于信道改变，之前连接到 ESP8266 SoftAP 的 Station 的 Wi-Fi 连接断开。

    **情况三：**
      - 其他 Station 与 ESP8266 SoftAP 建⽴连接；
      - 如果 ESP8266 Station ⼀直尝试扫描或连接某路由，可能导致 ESP8266 SoftAP 端的连接断开，或者 UDP 丢包，ping 丢包等情况。

  - 因为 ESP8266 Station 会遍历各个信道查找⽬标路路由，意味着 ESP8266 其实在不停切换信道，ESP8266 SoftAP 的信道也因此在不停更改。这可能导致 ESP8266 SoftAP 端的原有连接断开，或者 UDP 丢包，ping 丢包等情况。
  - 这种情况，⽤户可以通过设置定时器，超时后调⽤ wifi_station_disconnect 停⽌ ESP8266 Station 不断连接路由的尝试；或者在初始配置时，调⽤ wifi_station_set_reconnect_policy 和 wifi_station_set_auto_connect 禁⽌   ESP8266 Station 尝试重连路由。

## smartconfig 配⽹ WiFi 要求

- `Q:`
  - 关于 smartconfig 配⽹ WiFi 名字和密码有什么要求吗？⻓度最多⽀持多少？

- `A:`
  - 按照 wifi spec 上的，ssid 不超过 32 个 bytes，pwd 不超过 64bytes。

## ESP8266 和 ESP32 wifi 的 SSID

- `Q:`
  - 关于 wifi 连接，ESP8266 和 ESP32 是否⽀持中⽂ ssid？

- `A:`
  - 这个是可以的，不过与路由器和⼿机的编解码有关，如果两者都是 utf-8 格式，那么 ESP8266 通过 utf-8 的格式解析出来，就是正确的了，如果编解码格式不统⼀的话，解析出来的可能是乱码，没有办法连接成功。

## Wi-Fi Mesh 批量 OTA

- `Q:`
  - Wi-Fi Mesh 能不能批量 OTA？？

- `A:`
    1. wifi mesh 设备可以批量 ota 的。
    2. ota 的⽅式是固件下载根节点，根节点再将固件发送⾄其他节点。
    3. 具体示例请参考 https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mupgrade

## Wi-Fi Mesh 内存要求

- `Q:`
  - Wi-Fi Mesh 对内存要求⾼吗？是否需要外接PSRAM？

- `A:`
  - 不需要外接 PSRAM，内存要求在 60kByte 左右。

## ESP8266 支持 softap

- `Q:`
  - ESP8266 ⽀持多少个 softap？

- `A:`
  - 硬件上最多⽀持 8 个，我们推荐 4 个，这样可以保证模组性能。

## Wi-Fi 性能

- `Q:`
  - 如何测试 Wi-Fi 性能？

- `A:`
  - 请使⽤ `example/wifi/iperf` ⽬录下代码进⾏测试。

## ESP32 Wi-Fi 吞吐量

- `Q:`
  - ESP32 Wi-Fi 吞吐量？

- `A:`
  - 请联系 salesforce@espressif.com 获得吞吐量测试报告。

## Wi-Fi 内存占用

- `Q:`
  - Wi-Fi 启动后，会占⽤多少内存？

- `A:`
  - Wi-Fi 启动申请的内存主要包含以下⼏部分：
    1. Wi-Fi 任务和队列：6.144 KB
    2. Wi-Fi AMPDU：2.092 KB (IDF V3.0 及之后的版本优化了了第 2 项，节省 2.092KB 内存)
    3. Wi-Fi 电源管理任务和队列：3.44 KB (IDF V3.1 及之后的版本优化了了第 3 项，节省 3.44 KB 内存)
    4. Wi-Fi 内部数据结构：1.348 KB
    5. 事件任务和队列：6.164 KB
    6. LWIP 任务和邮箱：3.868 KB
    7. Wi-Fi/LwIP 静态 RX/TX 缓存取决于 menuconfig 的配置
    8. Wi-Fi/LwIP 动态 RX/TX 缓存取决于 menuconfig 的配置
  - 1 ~ 6 项在初始化时分配，总共占 ⽤：23.056 KB。
  - 7 ~ 8 项取决于 menuconfig 配置以及收发包情况，占⽤内存会动态变化。
