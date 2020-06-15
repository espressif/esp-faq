# 蓝牙

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

## ESP32 的蓝牙双模如何共存及使用？

ESP32 支持的双模蓝牙并没有特殊的地方，不需要做复杂的配置或调用即可使用。从开发者的⻆度来看，BLE 调用 BLE 的 API，经典蓝牙调用经典蓝牙的 API。经典蓝牙与 BLE 共存说明可参考文档 [ESP32 BT&BLE 双模蓝牙共存说明](https://www.espressif.com/sites/default/files/documentation/btble_coexistence_demo_cn.pdf)。

---
