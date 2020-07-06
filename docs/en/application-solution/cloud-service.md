# Cloud service

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## 有没有 ESP32-WROOM-32SE 使用内部 ATECC608A 与 AWS 通讯的示例？

您可以将这两个示例结合起来使用：
  - [esp-aws-iot](https://github.com/espressif/esp-aws-iot)
  - [ATECC608A](https://github.com/espressif/esp-idf/tree/master/examples/peripherals/secure_element/atecc608_ecdsa)
