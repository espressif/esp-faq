# 储存

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## ESP32 Flash 空间与使用要求？

- 外部 Flash 可以同时映射到 CPU 指令和只读数据空间。外部 Flash 最大可支持 16 MB。 
  - 当映射到 CPU 指令空间时，一次最多可映射 11 MB + 248 KB。如果一次映射超过 3 MB + 248 KB， 则 Cache 性能可能由于 CPU 的推测性读取而降低。 
  - 当映射到只读数据空间时，一次最多可以映射 4 MB。支持 8-bit、16-bit 和 32-bit 读取。
