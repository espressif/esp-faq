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

---

## ESP32 扫描⼀次需要花多⻓时间？

扫描花费的总时间取决于:

- 是被动扫描还是主动扫描，默认为主动扫描。
- 每个信道停留的时间，默认主动扫描为 120 ms，被动扫描为 360 ms。
- 国家码与配置的信道范围，默认为 1~13 信道。
- 是快速扫描还是全信道扫描，默认为快速扫描。
- Station 模式还是 Station-AP 模式，当前是否有连接。

默认情况下，1~11 信道为主动扫描，12〜13 信道为被动扫描。

- 在 Station 模式没有连接的情况下，全信道扫描总时间为：11*120 + 2*360 = 2040 ms；
- 在 Station 模式有连接，或者 Station-AP 模式下，全信道扫描总时间为：11*120 + 2*360 + 13\*30 = 2430 ms。
