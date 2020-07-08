# BLE Mesh 应用框架

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## 如何知道当前 Provisioner 正在配网哪个未配网设备？

&emsp;&emsp;`esp_ble_mesh_prov_t` 中 `prov_attention` 的值由 Provisioner 在配网过程中设置给未配网设备。该值只能在初始化期间设置一次，此后不能修改。未配网设备加入 mesh 网络后可以用特定的方式来显示自己正在配网，比如灯光闪烁，以告知 Provisioner 其正在配网。

---

## Provisioner 如何将节点添加至多个子网？

&emsp;&emsp;节点配置期间，Provisioner 可以为节点添加多个网络密钥，拥有相同网络密钥的节点属于同一子网。Provisioner 可以通过不同的网络密钥与不同子网内的节点进行通信。

---

## 何时使用 IV Update 更新程序？

&emsp;&emsp;一旦节点的底层检测到发送的消息的序列号达到临界值，IV Update 更新程序便会启用。

---

## 为什么需要快速配网？

&emsp;&emsp;通常而言，存在少量未配网设备时，用户可以逐个配置。但是如果有大量未配网设备（比如 100 个）时，逐个配置会耗费大量时间。通过快速配网，用户可以在约 50 秒内配网 100 个未配网设备。

---

## 如何启用 IV Update 更新程序？

&emsp;&emsp;节点可以使用带有 Secure Network Beacon 的 IV Update 更新程序。
