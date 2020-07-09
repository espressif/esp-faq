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

## 节点的模型可以使用哪些函数发送消息？

- 对于客户端模型，用户可以调用 API `esp_ble_mesh_client_model_send_msg()` 发送消息。
- 对于服务器模型，用户可以调用 API `esp_ble_mesh_server_model_send_msg()` 发送消息。
- 对于发布，用户可以调用 API `esp_ble_mesh_model_publish()` 发布消息。

---

## 如何实现消息传输不丢包？

&emsp;&emsp;如果用户要实现消息传输不丢包，则需有应答的消息。等待应答的默认时间在 [CONFIG_BLE_MESH_CLIENT_MSG_TIMEOUT](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/kconfig.html#config-ble-mesh-client-msg-timeout) 中设置。如果发送端等待应答超时，就会触发对应的超时事件。

&emsp;&emsp;**注：** API `esp_ble_mesh_client_model_send_msg()` 中可以设置应答的超时时间。如果参数 `msg_timeout` 设为 0， 那么超时时间便会采用默认值（4 秒）。

---

## 如何发送无应答的消息？

- 对于客户端模型，用户可以调用 API `esp_ble_mesh_client_model_send_msg()` with the parameter `need_rsp` set to `false` 发送无应答消息。

- 对于服务器模型，调用 API `esp_ble_mesh_server_model_send_msg()` 发送的消息总是无应答的消息。

---

## 发送不分包消息时，最多可携带多少有效字节？

&emsp;&emsp;不分包消息的总有效载荷长度（可由用户设置）为 11 个八位位组，因此，如果消息的 opcode 为 2 个八位位组，则该消息可以携带 9 个八位位组的有效信息。 对于 vendor 消息，由于 opcode 是 3 个八位位组，剩余的有效负载长度为 8 个八位位组。

---

## 什么时候应该使能节点的 [Proxy](https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.1/api-guides/esp-ble-mesh/ble-mesh-terminology.html#ble-mesh-terminology-features) 功能？

&emsp;&emsp;如果未配网设备将由电话配网，则未配网设备应该使能 Proxy 功能，因为当前几乎所有电话都不支持通过广播承载层发送 ESP-BLE-MESH 数据包。并且，未配网设备成功配网成为 Proxy 节点后，其会通过 GATT 承载层和广播承载层与 mesh 网络中的其他节点通信。

---

## 如何使用代理过滤器?

&emsp;&emsp;代理过滤器用于减少 Proxy Client（如手机）和 Proxy Server（如节点）之间交换的 Network PDU 的数量。另外，通过代理过滤器，Proxy Client 可以明确请求仅接收来自 Proxy Server 的某些目标地址的 mesh 消息。

---

## 如何实现将节点自检的信息发送出来？

&emsp;&emsp;推荐节点通过 Health Server Model 定期发布其自检结果。

---

## Relay 节点什么时候可以中继消息？

&emsp;&emsp;如果要中继消息，消息需满足以下要求。

- 消息存在于 mesh 网络中。
- 消息的目的地址不是节点的单播地址。
- 消息的 TTL 值需大于 1。

---

## 如果一条消息分成几段，那么其他 Relay 节点是接收到一段消息就中继还是等接收到完整的数据包才中继？

&emsp;&emsp;Relay 节点收到其中一段消息时就中继，而非一直等到接收所有的消息。

---

## 设备断电后上电，如何能继续在网络中进行通讯？

&emsp;&emsp;在 menuconfig 中启用配置 `Store BLE Mesh Node configuration persistently` 。

---

## 使用 [Low Power](https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.1/api-guides/esp-ble-mesh/ble-mesh-terminology.html#ble-mesh-terminology-features) 功能降低功耗的原理是什么？

- 开启无线电进行收听时，设备消耗能量。使能节点的低功耗功能后，它将在大多数时间内关闭无线电功能。
- 低功耗节点和好友节点需要合作，因此低功耗节点可以以适当或较低的频率接收消息，而无需一直收听。
- 当低功耗节点有一些新消息时，好友节点将为其存储消息。低功耗节点可以间隔固定时间轮询好友节点，以查看是否有新的消息。

---

## 节点间如何传输消息？

节点间传输信息的可能应用场景是，一旦烟雾警报检测到高浓度的烟雾，就会触发喷淋设备。 有两种实现方法。

- 方法 1：喷淋设备订阅组地址。当烟雾警报器检测到高浓度的烟雾时，它会发布一条消息，该消息的目标地址是喷淋设备已订阅的组地址。
- 方法 2：Provisioner 可以配置喷淋设备的单播地址为烟雾报警器的地址。当检测到高浓度的烟雾时，烟雾警报器以喷淋设备的单播地址为目标地址，将消息发送到喷淋设备。

---

## 何时使用 IV Update 更新程序？

&emsp;&emsp;一旦节点的底层检测到发送的消息的序列号达到临界值，IV Update 更新程序便会启用。

---

## 为什么需要快速配网？

&emsp;&emsp;通常而言，存在少量未配网设备时，用户可以逐个配置。但是如果有大量未配网设备（比如 100 个）时，逐个配置会耗费大量时间。通过快速配网，用户可以在约 50 秒内配网 100 个未配网设备。

---

## 如何启用 IV Update 更新程序？

&emsp;&emsp;节点可以使用带有 Secure Network Beacon 的 IV Update 更新程序。
