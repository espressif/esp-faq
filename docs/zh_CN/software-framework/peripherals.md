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

- SDIO 时钟能到 50 MHz, 理论最⾼速度是 200 Mbps。

---

## 使⽤ ESP32 做触摸相关应⽤时，哪⾥有相关资料可参考？

- 请参考推荐的[软硬件设计](https://github.com/espressif/esp-iot-solution/tree/master/examples/touch_pad_evb)

---

## ESP-WROOM-02D 模块是否可以外接 SPI Flash ？

- ESP-WROOM-02D 有空闲 SPI 外设，可外接 SPI Flash, 用以存储数据。

---

## ESP-WROOM-S2 作为从机，STM32 作为 MCU ，可以使⽤ SPI 接⼝下载吗？

- 不可以，默认下载功能仅支持串口 UART0，固件启动后可应用中使能其他外设，在应用中⾃⾏设计⽀持 OTA 功能。

---

## ESP8266 的 SDIO 是否⽀持 SD 卡？

- ESP8266 是 SDIO Slave，不⽀持 SD 卡。

---

## ESP8266 是否支持 I2C slave 模式？

- 不支持，如果要使用此功能，推荐使用 ESP32-S2 或者 ESP32 芯片。
- ESP32 参考示例：[i2C_self_test](https://github.com/espressif/esp-idf/tree/master/examples/peripherals/i2c/i2c_self_test)

---

## ESP32 管脚配置需要注意什么？

ESP32 系列模组分为 ESP32-WROOM 系列和 ESP32-Wrover 系列, GPIO 使用配置注意事项如下，请参考! \
WROOM-32/32D/32U 系列：
- 共有 26 个 pin 脚可供客户使用, 注意事项如下：
- GPIO6～GPIO11 被内置 flash 占用，不可用做它用；
- GPIO34，35，36 和 39 为 input only pin 脚，不具备 output 能力
- ESP32 内置 GPIO 矩阵，部分外设接口可以配置到任意空闲 pin 脚上，即硬件设计时，不需要严格将某些功能固定在某些 pin 脚上。详细信息可以参考 [ESP32 datasheet](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf) 中表格 9 的内容
- ESP32 有 3 组 UART，但下载只可使用 UART0，且 pin 脚固定

WROVER／WROVER-I／WROVER-B／WROVER-IB
- 共有 24 个 pin 脚可供客户使用，注意事项如下：
- GPIO6～GPIO11 被内置 flash 占用，不可用做它用；
- GPIO34，35，36 和 39 为 input only pin 脚，不具备 output 能力；
- WROVER 系列模组中，GPIO12 由于在模组内部被上拉，不建议用做触摸传感功能
- ESP32 内置 GPIO 矩阵，部分外设接口可以配置到任意空闲 pin 脚上，即硬件设计时，不需要严格将某些功能固定在某些 pin 脚上。详细信息可以参考 [ESP32 datasheet](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf) 中表格 9 的内容
- ESP32 有 3 组 UART，但下载只可使用 UART0，且 pin 脚固定

---

## ESP8266 I2C 是软件模拟的吗？

- ESP8266 I2C 是使用 gpio 软件模拟。
