# Wi-Fi Mesh 应用框架

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## Wi-Fi Mesh 占用多大内存？是否需要外部 PSRAM ？

&emsp;Wi-Fi Mesh 内存占用约 60KB，是否需要外部 PSRAM 取决于应用场景的复杂情况，一般性应用无需外部 PSRAM。

---

## Wi-Fi Mesh 能否批量 OTA ？

&emsp;Wi-Fi Mesh 设备支持批量 OTA。\
&emsp;OTA ⽅式为：根节点下载固件，然后再发至其他节点。具体示例请参考: [mupgrade](https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mupgrade)

---

## ESP32 Wi-Fi Mesh 是否可自动修复网络？

ESP32 Wi-Fi Mesh 可自动修复网络，Wi-Fi Mesh 有检测网络断线的机制。

---

## 使用 ESP32 Wi-Fi Mesh，如何设置可以在没连接到 Wi-Fi 的情况下形成自组网？

&emsp;需要指定一个设备作为 Root 节点，可参考[说明]（https://github.com/espressif/esp-mdf/blob/master/examples/function_demo/mwifi/README_cn.md）和[示例]（https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mwifi）。

