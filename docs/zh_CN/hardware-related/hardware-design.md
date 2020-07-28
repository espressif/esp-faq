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

- 所有 I2S 的 I/O 均可任意分配，需要注意有的 I/O 只能作为输⼊，请[参考《 ESP32 技术规格书》](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf)最后⼀⻚

---

## ESP32 避免 light-sleep 模式下 VDD3P3_RTC 掉电?

> ESP32-WROVER-B 进⼊ light-sleep 后，pads powered by VDD3P3_RTC 对应的 GPIO 的电平会被拉低

- 根本原因是进⼊ light sleep 后 RTC 掉电导致的。使⽤函数 `esp_sleep_pd_config(ESP_PD_DOMAIN_RTC_PERIPH, ESP_PD_OPTION_ON)` ; 维持 RTC 的供电。

---

## ESP32 管脚配置需要注意什么事项？

- 大部分数字外设可以通过 IO_Matrix 配置到任意管脚
  -  SDIO， SPI 高速，以及模拟类相关功能只能通过 IO_MUX 切换使用。

- 注意避免以下问题:
  - Strapping 管脚默认电平，详情参考芯片数据手册。
  - GPIO34 〜 39（⽤作输⼊ IO，并且无上下拉功能）。
  - GPIO9 〜 GPIO11 被 Flash 引脚占⽤。
  - GPIO1 和 GPIO3 是 UART0 的 TX 和 RX 引脚，是⽆法配置的。
  - 其中带有 psram 的模组， GPIO16 和 GPIO17 会被 psram 占⽤。

---

## 乐鑫芯片 GPIO 最大承载电压？

- 不可以。GPIO 只能承受 3.6V，需要通过降压电路，否则会造成 GPIO 损坏。
- 目前现有芯片 ESP8266 ESP32 与 ESP32S2 各系列 GPIO 最大承载电压均为 3.6 V。超出部分建议从硬件设计上补充分压电路，否则会造成 GPIO 损坏。

---

## ESP8266 电压电流需求？

- ESP8266 的数字部分的电压范围是 1.8V ~ 3.3V。
- 模拟部分的⼯作电压是 3.0V ~ 3.6V，最低 2.7V。
- 模拟电源峰值 350mA。
- 数字电源峰值 200mA。
- ==注意：== 选择的 SPI Flash ⼯作电压也需要与 GPIO 的电压匹配。CHIP_EN 还是⼯作在 3.0 ~ 3.6V，使⽤ 1.8V GPIO 控制时需要注意电平转换。

---

## 乐鑫 Wifi 模组是否有单面板 PCB 的方案？

- ESP32 属于无线模块，射频性能对与 PCB 材质有较高的要求。 我们测试过 4 层与 2 层的方案，但未测试过单层的设计。
- 在此不建议使用单层板子的方案,建议产品 PCB 可以使用单层板，贴装我们的模组。单层板子的模组，射频性能无法预估。

---

## ESP8266 电池供电有那些要求 ？

- ESP8266 电压范围为 2.7V ~ 3.6V，两节 AA 电池可以给 ESP8266 供电，需要注意电池压降是否满足芯片电压范围。
- 锂电池电压范围超过模组要求，并且放电时压降较⼤，不适合直接给 ESP8266 供电。
- 推荐电池使⽤ DC-DC 或 LDO 升降压后给 ESP8266 供电，并且注意电源芯片压差要求。

---

## ESP32-D2WD 外接 PSRAM 的参考设计？

- 建议参考 ESP32-PICO-D4 外接 PSRAM 的设计 [datasheet V7 章节](https://www.espressif.com/sites/default/files/documentation/esp32-pico-d4_datasheet_en.pdf).
- 注意：ESP32-D2WD 是 1.8V Flash，所以外部 VDD_SDIO 需要加电阻和电容，并且连接 1.8V PSRAM。

---

## ESP32 是否可以用 PWM 或 DAC 来播放音乐?

ESP32 可以用 PWM 或 DAC 来播放音乐，此功能有进行过播放测试，推荐用于提示音播放，示例工程可以通过邮件咨询获取。
