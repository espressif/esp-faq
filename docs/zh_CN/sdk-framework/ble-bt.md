# 蓝牙

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

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

## ESP32 的蓝牙双模如何共存及使用？

ESP32 支持的双模蓝牙并没有特殊的地方，不需要做复杂的配置或调用即可使用。从开发者的⻆度来看，BLE 调用 BLE 的 API，经典蓝牙调用经典蓝牙的 API。经典蓝牙与 BLE 共存说明可参考文档 [ESP32 BT&BLE 双模蓝牙共存说明](https://www.espressif.com/sites/default/files/documentation/btble_coexistence_demo_cn.pdf)。

---

## ESP32 的 BLE 吞吐量是多少？

ESP32 的 BLE 吞吐率取决于各种因素，例如环境干扰、连接间隔、MTU 大小以及对端设备性能等等。具体可以参考 IDF 中的 ble_throughput example，ESP32 板子之间的 BLE 通信最大吞吐量量可达 700 Kbps，约 90 KB/s。
