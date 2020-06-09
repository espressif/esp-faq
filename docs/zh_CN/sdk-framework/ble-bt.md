# 蓝牙

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

## ESP32 能否使用蓝牙进行 OTA？

可以使用蓝牙进行 OTA。如果是用 BT，可以基于 [bt_spp_acceptor](https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/classic_bt/bt_spp_acceptor) 和 [bt_spp_initiator](https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/classic_bt/bt_spp_initiator) 修改；如果是用 BLE，可以基于 [ble_spp_server](https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/ble/ble_spp_server) 和 [ble_spp_client](https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/ble/ble_spp_client) 修改。

---
