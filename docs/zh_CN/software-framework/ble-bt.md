# 蓝牙

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## 移植例程 gatt_server 出现头文件不存在的错误 ？

>  移植例程 gatt_server 出现错误 fatal error: esp_gap_ble_api.h: No such file or directory，但头文件已经包含。

- 检查 sdkconfig，是否未从例程中移植 sdkconfig.defaults, 通常 SDK 中蓝牙默认关闭不编译，需要配置开启。
- 如果使用 cmake 需要将例程中 CMakeLists.txt 文件内的链接配置一同复制。

---

## ESP32 可以支持 BLE 5.0 吗？

ESP32 硬件不支持 BLE 5.0，支持 BLE4.2。
ESP32 目前通过了 BLE 5.0 的认证，但 BLE 5.0 的新功能 ESP32 都不支持 。
未来我们会有其它芯片支持 BLE 5.0 。
可以使用蓝牙进行 OTA。如果是用 BT，可以基于 [bt_spp_acceptor](https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/classic_bt/bt_spp_acceptor) 和 [bt_spp_initiator](https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/classic_bt/bt_spp_initiator) 修改；如果是用 BLE，可以基于 [ble_spp_server](https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/ble/ble_spp_server) 和 [ble_spp_client](https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/ble/ble_spp_client) 修改。

---

## 为什么 BLE 开始广播后，有些手机扫描不到？

需确认手机是否支持 BLE 功能：有的手机在“设置” -> “蓝牙”中只显示默认的经典蓝牙，BLE 广播会被手机过滤掉。建议使用专用的 BLE 应用来调试 BLE 功能。例如，苹果手机可以使用 LightBlue 应用。需确认广播包的格式符合规范，手机一般会对不符合格式的广播包进行过滤，只有格式正确的才能被显示出来。

---

## ESP32 能否使用蓝牙进行 OTA？

可以使用蓝牙进行 OTA。如果是用 BT，可以基于 [bt_spp_acceptor](https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/classic_bt/bt_spp_acceptor) 和 [bt_spp_initiator](https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/classic_bt/bt_spp_initiator) 修改；如果是用 BLE，可以基于 [ble_spp_server](https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/ble/ble_spp_server) 和 [ble_spp_client](https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/ble/ble_spp_client) 修改。

---

## ESP32 的蓝牙双模如何共存及使用？

ESP32 支持的双模蓝牙并没有特殊的地方，不需要做复杂的配置或调用即可使用。从开发者的⻆度来看，BLE 调用 BLE 的 API，经典蓝牙调用经典蓝牙的 API。经典蓝牙与 BLE 共存说明可参考文档 [ESP32 BT&BLE 双模蓝牙共存说明](https://www.espressif.com/sites/default/files/documentation/btble_coexistence_demo_cn.pdf)。

---

## ESP32 的 BLE 吞吐量是多少？

ESP32 的 BLE 吞吐率取决于各种因素，例如环境干扰、连接间隔、MTU 大小以及对端设备性能等等。具体可以参考 IDF 中的 ble_throughput example，ESP32 板子之间的 BLE 通信最大吞吐量量可达 700 Kbps，约 90 KB/s。

---

## ESP32 是否支持 BT4.2 DLE ( Data Length Extension )？

支持。ESP-IDF 所有版本都支持 BT 4.2 DLE，暂无对应的 sample code，可直接调相关接口实现，参看：[esp_ble_gap_set_pkt_data_len](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/esp_gap_ble.html?highlight=esp_ble_gap_set_pkt_data_len#_CPPv428esp_ble_gap_set_pkt_data_len13esp_bd_addr_t8uint16_t)。

---

## ESP32 的蓝⽛和 Wi-Fi 如何共存？

- 在 menuconfig 中，有个特殊选项 “Software controls WiFi/Bluetooth coexistence”，⽤于通过软件来控制 ESP32 的蓝⽛和 Wi-Fi 共存，可以平衡 Wi-Fi、蓝⽛控制 RF 的共存需求。请注意，如果使能 `Software controls WiFi/Bluetooth coexistence` 选项，BLE scan 间隔不应超过 `0x100 slots`（约 160ms）。
- 若只是 BLE 与 Wi-Fi 共存，则开启这个选项和不开启均可正常使⽤。但不开启的时候需要注意 “BLE scan interval - BLE scan window > 150 ms”, 并且 BLE scan interval 尽量⼩于 500 ms。
  若经典蓝⽛与 Wi-Fi 共存，则建议开启这个选项。

---

## ESP32 蓝牙的兼容性测试报告如何获取？

请联系 sales@espressif.com 获得兼容性测试报告。

---

## ESP32 蓝牙的发射功率是多少？

ESP32 蓝牙的发射功率有 9 档，对应功率 -12 ~ 12dBm，间隔 3dBm 一档。控制器软件对发射功率进行限制，根据产品声明的对应功率等级选取档位。

---

## ESP32 可以实现 wifi 和 ble 桥接的功能吗？

可以实现的，这个属于应⽤层开发，客户可以直接通过 ble 获取数据，wifi 转出去，我们⽬前没有 demo，但是客户可以参考⼀下 wifi 和蓝⽛共存的 demo：https://github.com/espressif/esp-idf/tree/release/v4.0/examples/bluetooth/esp_ble_mesh/ble_mesh_wifi_coexist， 修改为⾃⼰的应⽤即可

---

## ESP32 的 BLE 工作电流是多少？

| 电流                                                         | 最大值 (mA) | 最小值 (mA) | 平均值 |
| :-------------------------------------------------------------- | :------: | :------: | :-----: |
| Advertising: <br> Adv Interval = 40ms                           |  142.1   |    32    |  42.67  |
| Scanning: <br> Scan Interval = 160ms,Window = 20ms              |  142.1   |    32    |  44.4   |
| Connection(Slave): <br> Connection Interval = 20ms, Iatency = 0 |  142.1   |    32    |  42.75  |
| Connection(Slave): <br> Connection Interval = 80ms, Iatency = 0 |  142.1   |    32    |  35.33  |


---

## ESP32 支持哪些 BLE Profile？

> 目前支持完整的 GATT/SMP 等基础模块，可自行实现自定义配置；已经实现的配置有 BLE HID（设备端）、电池、DIS、Blu-Fi（蓝牙配网）等。

目前支持完整的 GATT/SMP 等基础模块，可自行实现自定义配置；已经实现的配置有 BLE HID（设备端）、电池、DIS、Blu-Fi（蓝牙配网）等。

---

## 如何使用 ESP32 蓝牙连接手机播放音乐？

用手机通过蓝牙播放音乐，ESP32 用作 A2DP Sink，A2DP Sink Demo 只是通过手机获取 SBC 编码的数据流，若要播放出声音，需要做编解码转换及编解码器 、数/模转换器 、扬声器等模块以最终输出声音。

---

## ESP32 的 SPP 性能如何？

使用两块 ESP32 开发板对跑 SPP，单向吞吐量量可达 1900 Kbps，约 235 KB/s，已接近规范里的理论值。
