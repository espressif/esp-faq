# wifi

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## ESP32 和 ESP8266 是否支持中文 SSID？

是支持的，使用中需要路由器或者手机的中文编码方式一致。
示例：路由器中文编码使用 UTF-8 ，设备中文编码使用 UTF-8 ，设备就可以正确连接中文 SSID 的路由器。
