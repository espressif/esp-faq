# 系统

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## ESP8266 看⻔狗的超时间隔是多久？出发超时事件会有什么现象？

- 硬件看⻔狗中断时间为 0.8*2048ms，即 1638.4s，中断后处理时间为 0.8*8192ms，即 6553.6ms。其中中断处理后时间为硬件看⻔狗中断发⽣后，需要进⾏喂狗操作的时间，如果超过该时间，即会触发硬件看⻔狗复位。因此，在仅有硬件看⻔狗的情况下，⼀个程序段如果运⾏时间超过 6553.6ms，即有可能触发硬件看⻔狗复位，若超过 8192ms 则⼀定会触发复位。
- 软件看⻔狗建⽴在 MAC timer 以及系统调度之上，中断时间为 1600ms，中断后处理时间 1600ms。因此，在有软件+硬件看⻔狗的情况下，⼀个程序段如果运⾏时间超过 1600ms，即有可能会触发软件看⻔狗复位，若超过 3200ms 则⼀定会触发复位。
