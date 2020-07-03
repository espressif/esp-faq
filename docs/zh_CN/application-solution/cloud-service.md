# 云服务

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## OTA 升级有没有相关 demo 参考？

请参考如下链接：\
&emsp;[ESP8266 OTA](https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/system/ota)\
&emsp;[ESP32 及 ESP32-S2 OTA](https://github.com/espressif/esp-idf/tree/master/examples/system/ota)  

---

## ESP8266 NONOS SDK OTA 为何云端需要 "user1.bin" 和 "user2.bin" 两个 bin 文件？

&emsp;ESP8266 Cache 偏移仅支持 1MB 的单位偏移。
- 当分区设置为 512+512 模式时，user1.bin 与 user2.bin 指令地址并不相同，不可以相互替换；所以，同一版本需要云端放置两个不同版本的固件用于设备升级。
- 当分区设置为 1024+1024 模式时，分区大小满足 Cache 偏移，不受该限制。
