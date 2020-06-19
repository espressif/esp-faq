# 外设

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## SDIO 最⾼速度能⽀持到多少？

SDIO 时钟能到 50 MHz, 理论最⾼速度是 200 Mbps。

---

## 使⽤ ESP32 做触摸相关应⽤时，哪⾥有相关资料可参考？

请参考推荐的[软硬件设计](https://github.com/espressif/esp-iot-solution/tree/master/examples/touch_pad_evb)

---

## ESP-WROOM-02D 模块是否可以外接 SPI Flash ？

> ESP-WROOM-02D 模块，外接 64M SPI Flash 用于保存数据，WiFi 工作时，接收的数据写入 SPI Flash 。

- ESP-WROOM-02D 有空闲 SPI 外设，可以使用该外设完成 flash 的读写功能。

---

## ESP_WROOM_S2 作为从机，STM32 作为 MCU ，可以使⽤ SPI 接⼝下载吗？

不可以，固件下载⽤的是 UART 接⼝，通信可以使⽤ API 通信。也可以在固件中⾃⾏设计⽀持 OTA 功能。

---

## ESP8266 的 SDIO 是否⽀持 SD 卡？

ESP8266 是 SDIO Slave，不⽀持 SD 卡。
