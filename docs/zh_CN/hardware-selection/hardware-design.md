# 硬件设计

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## 参考设计中 I2S 信号管脚分布

> 乐鑫提供的参考设计中 I2S 信号分布太散，是否可以配置集中⼀些，⽐如配知道 `GPIO5，GPIO18，GPIO23、GPIO19、GPIO22` 管脚上；I2C 配置到 `GPIO25、GPIO26` 或 `GPIO32、GPIO33` 管脚上?

所有 I2S 的 I/O 均可任意分配，需要注意有的 I/O 只能作为输⼊，请[参考《 ESP32 技术规格书》](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf)最后⼀⻚

---

## 乐鑫芯片 GPIO 最大承载电压？

不可以。GPIO 只能承受 3.6V，需要通过降压电路，否则会造成 GPIO 损坏。
目前现有芯片 ESP8266 ESP32 与 ESP32S2 各系列 GPIO 最大承载电压均为 3.6 V。超出部分建议从硬件设计上补充分压电路，否则会造成 GPIO 损坏。

---
