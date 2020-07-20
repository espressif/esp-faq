# mesh 网络

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## ESP32 MESH 网络时间同步的精度是多少?

- 目前 ESP32 MESH 时间同步的机制 <30ms 。
- ESP32 MESH 中 API: [esp_mesh_get_tsf_time](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/network/esp_mesh.html#_CPPv421esp_mesh_get_tsf_timev) ，这个时间源为 router 的 tfs 时间。
