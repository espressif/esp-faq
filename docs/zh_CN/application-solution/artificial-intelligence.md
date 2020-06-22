# AI 应用

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## AI 图像识别产品可兼容哪些摄像头？

- ESP-EYE 主控芯⽚为 ESP32，可兼容 0v2640，3660， 5640 等多款摄像头。

---

## esp-who 是否⽀持 IDF 4.1？

- 截止 esp-who commit: `2470e47 Update esp32-camera` ，暂时仅⽀持 IDF v3.3.1 和 v4.0.0。
- esp-who 最新链接为 https://github.com/espressif/esp-who。
