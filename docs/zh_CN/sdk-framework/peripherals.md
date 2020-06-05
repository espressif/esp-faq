# 外设

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

## 使⽤ ESP32 做触摸相关应⽤时，哪⾥有相关资料可参考？

请参考推荐的[软硬件设计](https://github.com/espressif/esp-iot-solution/tree/master/examples/touch_pad_evb)

---

