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

- ESP8266 OTA 请参考 https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/system/ota
- ESP32 及 ESP32-S2 OTA 请参考 https://github.com/espressif/esp-idf/tree/master/examples/system/ota
