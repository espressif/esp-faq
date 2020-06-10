# AT

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

## AT 提示 busy 是什么原因？

AT 指令的处理是线性的，也就是处理完前⼀条指令后，才能接收下⼀条指令进⾏处理。提示 "busy" 表示正在处理前⼀条指令，⽆法响应当前输⼊。

⽽任何串⼝的输⼊，均被认为是指令输⼊，因此，当有多余的不可⻅字符输⼊时，系统也会提示 "busy" 或者 "ERROR"。

例如，串⼝输⼊ AT+GMR (换⾏符 CR LF) (空格符)，由于 AT+GMR (换⾏符 CR LF) 已经是⼀条完整的 AT 指令了，系统会执⾏该指令。

如果系统尚未完成 AT+GMR 操作，就收到了后⾯的空格符，将被认为是新的指令输⼊，系统提示 "busy"。

如果系统已经完成了 AT+GMR 操作，再收到后⾯的空格符，空格符将被认为是⼀条错误的指令，系统提示 "ERROR"。

---
