# AT

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

## ESP8266 SmartConfig 配⽹失败有哪些原因？

请按如下顺序进⾏排查：
1. APP 版本是否⽀持 SDK 版本或 SmartConfig 版本
2. ⼿机连接的路由器不能是单 5G 路由（双频路路由器除外）
3. SmartConfig 过程中不要调⽤其他 API 
4. 使⽤ AT 时，设备没有获得 IP 之前，不要调⽤ smartconfig_stop

如以上排除，请把连接失败和成功的 log 发至邮箱 sales@espressif.com 以便我们进行⽀持分析

---
