# 音频应用框架

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## 使用 ESP-ADF 下的 VOIP 功能，通过手机和 ESP32 设备进行通话时，如何消除回音？

- 从软件层面来讲， AEC (Acoustic Echo Cancelation) 对系统性能要求较高，而当前芯片性能无法满足，不支持通过软件实时 AEC。因此 VOIP 目前没有 AEC 的软件解决方案。

- 建议使用支持 AEC 的 DSP 芯片来消除回音。
