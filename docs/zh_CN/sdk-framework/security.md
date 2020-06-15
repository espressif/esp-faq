# 安全

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## ESP8266 的固件是否能被读取？

ESP8266 固件由于放置在外部 flash, 数据可被外部读取。并且 ESP8266 不支持 flash 加密，所有数据均为明文。
