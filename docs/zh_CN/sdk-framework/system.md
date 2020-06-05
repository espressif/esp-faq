# 系统

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## 如果我的应⽤不需要看⻔狗，如何关闭看⻔狗？

- 当前 SDK 仅⽀持关闭软件看⻔狗， ⽀持同时喂软硬件看⻔狗。可以通过如下⽅式防⽌执⾏时间过⻓的⽤户程序导致看⻔狗复位：
  - 如果⼀个程序段运⾏时间在触发软件看⻔狗和触发硬件看⻔狗复位之间，则可通过 system_soft_wdt_stop() 的⽅式关闭软件看⻔狗，在程序段执⾏完毕后⽤ system_soft_wdt_restart() 重新打开软件看⻔狗。
  - 可以通过在程序段中添加 system_soft_wdt_feed() 来进⾏喂软硬件狗操作，防⽌软硬件看⻔狗复位。

---

## 为什么 ESP8266 进⼊启动模式（2，7）并触发看⻔狗复位？

请确保 ESP8266 启动时，strapping 管脚处于所需的电平。如果外部连接的外设使 strapping 管脚进⼊到错误的电平，ESP8266 可能进⼊错误的操作模式。在⽆有效程序的情况下，看⻔狗计时器将复位芯⽚。
因此在设计实践中，建议仅将 strapping 管脚⽤于连接⾼阻态外部器件的输⼊，这样便不会在上电时强制 strapping 管脚为⾼/低电平。
