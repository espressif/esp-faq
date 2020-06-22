# 固件更新

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## Host MCU 如何通过串口对 ESP32 进行烧录升级？

- 相关协议说明请参考：[ESP32 串口协议](https://github.com/espressif/esptool/wiki/Serial-Protocol)
- 示例实现代码参考: [esp-serial-flasher](https://github.com/espressif/esp-serial-flasher)

---

## 如何使用 USB 转串口工具对乐鑫模组进行自动烧录？

- USB 转串口对乐鑫模组进行自动烧录接线方式如下：

| 乐鑫模组 | 3V3  | GND  | TXD  | RXD  | IO0  | EN   |
| :------- | :--: | :--: | :--: | :--: | :--: | :--: |
| 串口工具 | 3V3  | GND  | RXD  | TXD  | DTR  | RTS  |

> ESP8266 模组需要额外将 IO15 接地。
