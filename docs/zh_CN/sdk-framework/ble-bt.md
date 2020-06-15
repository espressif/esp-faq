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
