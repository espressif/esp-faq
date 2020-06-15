# AT

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## AT 提示 busy 是什么原因？

AT 指令的处理是线性的，也就是处理完前⼀条指令后，才能接收下⼀条指令进⾏处理。提示 "busy" 表示正在处理前⼀条指令，⽆法响应当前输⼊。

⽽任何串⼝的输⼊，均被认为是指令输⼊，因此，当有多余的不可⻅字符输⼊时，系统也会提示 "busy" 或者 "ERROR"。

例如，串⼝输⼊ AT+GMR (换⾏符 CR LF) (空格符)，由于 AT+GMR (换⾏符 CR LF) 已经是⼀条完整的 AT 指令了，系统会执⾏该指令。

如果系统尚未完成 AT+GMR 操作，就收到了后⾯的空格符，将被认为是新的指令输⼊，系统提示 "busy"。

如果系统已经完成了 AT+GMR 操作，再收到后⾯的空格符，空格符将被认为是⼀条错误的指令，系统提示 "ERROR"。

---

## ESP32 AT 相关资源从哪里获得？

ESP32 AT bin 文件：https://www.espressif.com/zh-hans/support/download/at \
ESP32 AT 文档：[AT 指令集](https://github.com/espressif/esp-at/blob/master/docs/ESP_AT_Commands_Set.md)\
此外，客户也可以基于乐鑫官方的 esp-at 工程开发更多的 AT 指令，ESP32 AT 工程可以在 GitHub 下载：https://github.com/espressif/esp32-at

---

## ESP8266 云端升级失败有哪些原因？

远端升级的详细介绍参考⽂档为《ESP8266 云端升级指南》
建议按如下顺序，进⾏排查：

1. 确认使⽤了正确⼤⼩的 Flash
2. 确认是否烧录了 blank.bin 做初始化
3. 确认 user1.bin 和 user2.bin 下载到了正确的地址
4. 确认⽣成 user1.bin 和 user2.bin 使⽤了相同的 Flash、boot 配置
