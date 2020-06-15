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
