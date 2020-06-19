# wifi mesh 应用框架

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## Wi-Fi Mesh 占用多大内存？是否需要外部 PSRAM ？

Wi-Fi Mesh 内存使用在 60KB 左右，是否需要使用外部 PSRAM 取决于应用业务的复杂情况，一般性应用可以无需使用外部 PSRAM。

---

## Wi-Fi Mesh 能否批量 OTA ？

- wifi mesh 设备支持批量 ota 的。
- ota 的⽅式是根节点下载固件，然后再发至其他节点。
- 具体示例请参考: [mupgrade](https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mupgrade)