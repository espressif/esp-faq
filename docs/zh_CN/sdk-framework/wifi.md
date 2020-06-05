# wifi

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

## 关于 wifi 连接，ESP8266 和 ESP32 是否⽀持中⽂ ssid？

这个是可以的，不过与路由器和⼿机的编解码有关，如果两者都是 utf-8 格式，那么 ESP8266 通过 utf-8 的格式解析出来，就是正确的了，如果编解码格式不统⼀的话，解析出来的可能是乱码，没有办法连接成功。

---
