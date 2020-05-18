# 安全

## ESP8266 固件拷贝

- `Q:`
  - ESP8266 的固件是否会出现被其他⼈拷⻉的现象？

- `A:`
  - 会，因为 ESP8266 不⽀持硬件加密，不过软件上可以做⼀些加密（⽐如对mac 地址进⾏加密校验，如果验证失败，固件就⽆法启动），这样，其他⼈就算拷⻉到了固件，也是没有办法正常运⾏的。

## ESP32 硬件加密

- `Q:`
  - ESP32 是否⽀持硬件加密？

- `A:`
  - ⽀持，可以参考官⽹上secure boot 和flash encrypted 资料（link：https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/security/flash-encryption.html）

## ESP-WROOM-32 模组使能 secure boot 和flash encrypted 报错

- `Q:`
  - ESP-WROOM-32 模组使能了 secure boot 和 flash encrypted，配置的是 one time flash，重新烧录后，发现会出现flash read error 的现象，这是什么原因？

- `A:`
  - 原因是模组配置为了 one time flash，说明只能烧录⼀次，如果客户重新烧录后，那么相当于在加密的基础上⼜做了加密，这样按照之前的⽅式解密，解密出来的其实还是密⽂，所以会出现 flash read error 的现象.
