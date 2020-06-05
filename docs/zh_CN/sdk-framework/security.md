# 安全

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

## ESP8266 的固件是否会出现被其他⼈拷⻉的现象？

会，因为 ESP8266 不⽀持硬件加密，不过软件上可以做⼀些加密（⽐如对mac 地址进⾏加密校验，如果验证失败，固件就⽆法启动），这样，其他⼈就算拷⻉到了固件，也是没有办法正常运⾏的。

---