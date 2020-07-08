# 开发板使用

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

--- 

## ESP32-Korvo V1.1 开发板是否集成 LED driver 芯片？

- 我司出厂的 ESP32-Korvo V1.1 开发板未有 LED driver。

---

## ESP-EYE 开发板运行发热过高如何改善？

- 降低功耗: 如果摄像头并非实时开启，WIFI 可以周期传输，空闲时间可以进入休眠模式降低功耗。
- 增大散热面积: 可以通过在 ESP32 芯片上方增加散热片来实现。
