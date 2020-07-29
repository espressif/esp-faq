# 储存

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## ESP32 Flash 空间与使用要求？

- 外部 Flash 可以同时映射到 CPU 指令和只读数据空间。外部 Flash 最大可支持 16 MB。 
  - 当映射到 CPU 指令空间时，一次最多可映射 11 MB + 248 KB。如果一次映射超过 3 MB + 248 KB， 则 Cache 性能可能由于 CPU 的推测性读取而降低。 
  - 当映射到只读数据空间时，一次最多可以映射 4 MB。支持 8-bit、16-bit 和 32-bit 读取。

---

## ESP8266 是否可以搭配 TF 卡使用？

不建议这么使用。
  - 虽然硬件上是可以连接的（通过 spi 与 TF 卡通信），但是因为 ESP8266 的资源有限，根据不同的应用场景，很可能会出现内存不足等情况。所以不建议 ESP8266 搭配 TF 卡使用。
  - 如果您只需要单 Wi-Fi 模组，并且要连接 TF 卡，建议使用[ESP32-S2](https://www.espressif.com/sites/default/files/documentation/esp32-s2_datasheet_cn.pdf)芯片。
