# BLE Mesh 应用框架

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## ESP-BLE-MESH 如何打印数据包？

&emsp;&emsp;示例使用如下函数 `ESP_LOG_BUFFER_HEX()` 打印信息语境，而 ESP-BLE-MESH 协议栈使用 `bt_hex()` 打印。

---

## Device UUID 可以用于设备识别吗？

&emsp;&emsp;是的。每个设备都有独一无二的 Device UUID, 用户可以通过 Device UUID 识别设备。

---

## 如何知道当前 Provisioner 正在配网哪个未配网设备？

&emsp;&emsp;`esp_ble_mesh_prov_t` 中 `prov_attention` 的值由 Provisioner 在配网过程中设置给未配网设备。该值只能在初始化期间设置一次，此后不能修改。未配网设备加入 mesh 网络后可以用特定的方式来显示自己正在配网，比如灯光闪烁，以告知 Provisioner 其正在配网。

---

## Provisioner 如何通过 Configuration Client Model 获取并且解析节点的[构成数据](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/esp-ble-mesh/ble-mesh-terminology.html#ble-mesh-terminology-composition) ？

- Provisioner 可以调用 [Configuration Client Model](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/esp-ble-mesh/ble-mesh-terminology.html#ble-mesh-terminology-foundation-models) API `esp_ble_mesh_config_client_set_state()` 设置参数，调用 `esp_ble_mesh_cfg_client_get_state_t` 中的 `comp_data_get` 获取节点的构成数据。
- 用户可以参考以下代码解析 Composition Data:

``` c
#include <stdio.h>
#include <string.h>
#include <stdint.h>

//test date: 0C001A0001000800030000010501000000800100001003103F002A00
//0C00 1A00 0100 0800 0300 0001 05 01 0000 0080 0100 0010 0310 3F002A00

// CID is 0x000C
// PID is 0x001A
// VID is 0x0001
// CRPL is 0x0008
// Features is 0x0003 – Relay and Friend features.
// Loc is “front” – 0x0100
// NumS is 5
// NumV is 1
// The Bluetooth SIG Models supported are: 0x0000, 0x8000, 0x0001, 0x1000, 0x1003
// The Vendor Models supported are: Company Identifier 0x003F and Model Identifier 0x002A

typedef struct {
    int16_t cid;
    int16_t pid;
    int16_t vid;
    int16_t crpl;
    int16_t features;
    int16_t all_models;
    uint8_t sig_models;
    uint8_t vnd_models;
} esp_ble_mesh_composition_head;

typedef struct {
    uint16_t model_id;
    uint16_t vendor_id;
} tsModel;

typedef struct {
    // reserve space for up to 20 SIG models
    uint16_t SIG_models[20];
    uint8_t numSIGModels;

    // reserve space for up to 4 vendor models
    tsModel Vendor_models[4];
    uint8_t numVendorModels;
} esp_ble_mesh_composition_decode;

int decode_comp_data(esp_ble_mesh_composition_head *head, esp_ble_mesh_composition_decode *data, uint8_t *mystr, int size)
{
    int pos_sig_base;
    int pos_vnd_base;
    int i;

    memcpy(head, mystr, sizeof(*head));

    if(size < sizeof(*head) + head->sig_models * 2 + head->vnd_models * 4) {
        return -1;
    }

    pos_sig_base = sizeof(*head) - 1;

    for(i = 1; i < head->sig_models * 2; i = i + 2) {
        data->SIG_models[i/2] = mystr[i + pos_sig_base] | (mystr[i + pos_sig_base + 1] << 8);
        printf("%d: %4.4x\n", i/2, data->SIG_models[i/2]);
    }

    pos_vnd_base = head->sig_models * 2 + pos_sig_base;

    for(i = 1; i < head->vnd_models * 2; i = i + 2) {
        data->Vendor_models[i/2].model_id = mystr[i + pos_vnd_base] | (mystr[i + pos_vnd_base + 1] << 8);
        printf("%d: %4.4x\n", i/2, data->Vendor_models[i/2].model_id);

        data->Vendor_models[i/2].vendor_id = mystr[i + pos_vnd_base + 2] | (mystr[i + pos_vnd_base + 3] << 8);
        printf("%d: %4.4x\n", i/2, data->Vendor_models[i/2].vendor_id);
    }

    return 0;
}

void app_main(void)
{
    esp_ble_mesh_composition_head head = {0};
    esp_ble_mesh_composition_decode data = {0};
    uint8_t mystr[] = { 0x0C, 0x00, 0x1A, 0x00,
                        0x01, 0x00, 0x08, 0x00,
                        0x03, 0x00, 0x00, 0x01,
                        0x05, 0x01, 0x00, 0x00,
                        0x00, 0x80, 0x01, 0x00,
                        0x00, 0x10, 0x03, 0x10,
                        0x3F, 0x00, 0x2A, 0x00};
    int ret;

    ret = decode_comp_data(&head, &data, mystr, sizeof(mystr));
    if (ret == -1) {
        printf("decode_comp_data error");
    }
}
```

---

## Provisioner 如何通过获取的 Composition Data 进一步配置节点？

&emsp;&emsp;Provisioner 通过调用 [Configuration Client Model](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/esp-ble-mesh/ble-mesh-terminology.html#ble-mesh-terminology-foundation-models) API `esp_ble_mesh_config_client_set_state()` 来进行如下配置。

- 正确设置参数 `esp_ble_mesh_cfg_client_set_state_t` 中的 `app_key_add`，将应用密钥添加到节点中。
- 正确设置参数 `esp_ble_mesh_cfg_client_set_state_t` 中的 `model_sub_add`，将订阅地址添加到节点的模型中。
- 正确设置参数 `esp_ble_mesh_cfg_client_set_state_t` 中的 `model_pub_set`，将发布地址添加到节点的模型中。

---

## 节点可以自己添加相应的配置吗？

&emsp;&emsp;本法可用于特殊情况，如测试阶段。
- 此示例展示了节点如何为自己的模型添加新的组地址。
```
esp_err_t example_add_fast_prov_group_address(uint16_t model_id, uint16_t group_addr)
{
    const esp_ble_mesh_comp_t *comp = NULL;
    esp_ble_mesh_elem_t *element = NULL;
    esp_ble_mesh_model_t *model = NULL;
    int i, j;

    if (!ESP_BLE_MESH_ADDR_IS_GROUP(group_addr)) {
        return ESP_ERR_INVALID_ARG;
    }

    comp = esp_ble_mesh_get_composition_data();
    if (!comp) {
        return ESP_FAIL;
    }

    for (i = 0; i < comp->element_count; i++) {
        element = &comp->elements[i];
        model = esp_ble_mesh_find_sig_model(element, model_id);
        if (!model) {
            continue;
        }
        for (j = 0; j < ARRAY_SIZE(model->groups); j++) {
            if (model->groups[j] == group_addr) {
                break;
            }
        }
        if (j != ARRAY_SIZE(model->groups)) {
            ESP_LOGW(TAG, "%s: Group address already exists, element index: %d", __func__, i);
            continue;
        }
        for (j = 0; j < ARRAY_SIZE(model->groups); j++) {
            if (model->groups[j] == ESP_BLE_MESH_ADDR_UNASSIGNED) {
                model->groups[j] = group_addr;
                break;
            }
        }
        if (j == ARRAY_SIZE(model->groups)) {
            ESP_LOGE(TAG, "%s: Model is full of group addresses, element index: %d", __func__, i);
        }
    }

    return ESP_OK;
}
```

&emsp;&emsp; **注：** 使能了节点的 NVS 存储器后，通过该方式添加的组地址以及绑定的应用密钥在设备掉电的情况下不能保存。这些配置信息只有通过 Configuration Client Model 配置时才会保存。

---

## Provisioner 如何通过分组的方式控制节点？

&emsp;&emsp;通常而言，在 ESP-BLE-MESH 网络中实现组控制有两种方法，即组地址方法和虚拟地址方法。假设有 10 个设备，即 5 个带蓝灯的设备和 5 个带红灯的设备。
- 方案一：5 个蓝灯设备订阅一个组地址，5 个红灯设备订阅另一个组地址。Provisioner 往不同的组地址发送消息，即可实现分组控制设备。
- 方案二：5 个蓝灯设备订阅一个虚拟地址，5 个红灯设备订阅另一个虚拟地址，Provisioner 往不同的虚拟地址发送消息，即可实现分组控制设备。

---

## Provisioner 如何知道网络中的某个设备是否离线？

&emsp;&emsp;节点离线通常定义为：电源故障或其他原因导致的节点无法与 mesh 网络中的其他节点正常通信的情况。\
&emsp;&emsp;ESP-BLE-MESH 网络中的节点间彼此不连接，它们通过广播通道进行通信。\
&emsp;&emsp;此示例展示了如何通过 Provisioner 检测节点是否离线。

- 节点定期给 Provisioner 发送心跳包。如果 Provisioner 超过一定的时间未接收到心跳包，则视该节点离线。

&emsp;&emsp;**注：** 心跳包的设计应该采用单包（字节数小于 11 个字节）的方式，这样收发效率会更高。

---

## Provisioner 如何将节点添加至多个子网？

&emsp;&emsp;节点配置期间，Provisioner 可以为节点添加多个网络密钥，拥有相同网络密钥的节点属于同一子网。Provisioner 可以通过不同的网络密钥与不同子网内的节点进行通信。

---

## BLE MESH Log `ran out of retransmit attempts` 代表什么？

&emsp;&emsp;节点发送分段消息时，由于某些原因，接收端未收到完整的消息。节点会重传消息。当重传次数达到最大重传数时，会出现该警告，当前最大重传数为 4。

---

## BLE Mesh log `Duplicate found in Network Message Cache` 代表什么？

&emsp;&emsp;当节点收到一条消息时，它会把该消息与网络缓存中存储的消息进行比较。如果在缓存中找到相同的消息，这意味着之前已接受过该消息，则该消息会被丢弃。

---

## BLE Mesh log `Incomplete timer expired` 代表什么？

&emsp;&emsp;当节点在一定时间段（比如 10 秒）内未收到分段消息的所有段时，则 Incomplete 计时器到时，并且出现该警告。

---

## BLE Mesh log `No free slots for new incoming segmented messages` 代表什么？

&emsp;&emsp;当节点没有空间来接收新的分段消息时，会出现该警告。用户可以通过配置 [CONFIG_BLE_MESH_RX_SEG_MSG_COUNT](https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.1/api-reference/kconfig.html#config-ble-mesh-rx-seg-msg-count) 扩大空间。

---

## BLE Mesh log `No matching TX context for ack` 代表什么？

&emsp;&emsp;当节点收到一个分段 ack 且不能找到任何自己发送的与该 ack 相关的消息时，会出现该警告。

---

## BLE Mesh log `Model not bound to AppKey 0x0000` 代表什么？

&emsp;&emsp;当节点发送带有模型的消息且该模型尚未绑定到索引为 0x000 的应用密钥时，会出现该报错。

---

## BLE Mesh log `Busy sending message to DST xxxx` 代表什么？

&emsp;&emsp;该错误表示节点的客户端模型已将消息发送给目标节点，并且正在等待响应，用户无法将消息发送到单播地址相同的同一节点。接收到相应的响应或计时器到时后，可以发送另一条消息。

---

## 为什么会出现 EspBleMesh App 在快速配网期间长时间等待的情况？

&emsp;&emsp;快速配网期间，代理节点在配置完一个节点后会断开与 APP 的连接，待所有节点配网完成后再与 APP 重新建立连接。

---

## Provisoner 如何控制节点的服务器模型？

&emsp;&emsp;ESP-BLE-MESH 支持所有 SIG 定义的客户端模型。Provisioner 可以使用这些客户端模型控制节点的服务器模型。客户端模型分为 6 类，每类有相应的功能。

- Configuration Client Model
  -  API `esp_ble_mesh_config_client_get_state()` 可用于获取 Configuration Server Model 的 `esp_ble_mesh_cfg_client_get_state_t` 值。
  - API `esp_ble_mesh_config_client_set_state()` 可用于获取 Configuration Server Model 的 `esp_ble_mesh_cfg_client_set_state_t` 值。
- Health Client Model
  - API `esp_ble_mesh_health_client_get_state()` 可用于获取 Health Server Model 的 `esp_ble_mesh_health_client_get_state_t` 值。
  - API `esp_ble_mesh_health_client_set_state()` 可用于获取 Health Server Model 的 `esp_ble_mesh_health_client_set_state_t` 值。
- Generic Client Models
  - API `esp_ble_mesh_generic_client_get_state()` 可用于获取 Generic Server Model 的 `esp_ble_mesh_generic_client_get_state_t` 值。
  - API `esp_ble_mesh_generic_client_set_state()` 可用于获取 Generic Server Model 的 `esp_ble_mesh_generic_client_set_state_t` 值。
- Lighting Client Models
  - API `esp_ble_mesh_light_client_get_state()` 可用于获取 Lighting Server Model 的 `esp_ble_mesh_light_client_get_state_t` 值。
  - API `esp_ble_mesh_light_client_set_state()` 可用于获取 Lighting Server Model 的 `esp_ble_mesh_light_client_set_state_t` 值。
- Sensor Client Models
  - API `esp_ble_mesh_sensor_client_get_state()` 可用于获取 Sensor Server Model 的 `esp_ble_mesh_sensor_client_get_state_t` 值。
  - API `esp_ble_mesh_sensor_client_set_state()` 可用于获取 Sensor Server Model 的 `esp_ble_mesh_sensor_client_set_state_t` 值。
- Time and Scenes Client Models
  - API `esp_ble_mesh_time_scene_client_get_state()` 可用于获取 Time and Scenes Server Model 的 `esp_ble_mesh_time_scene_client_get_state_t` 值。
  - API `esp_ble_mesh_time_scene_client_set_state()` 可用于获取 Time and Scenes Server Model 的 `esp_ble_mesh_time_scene_client_set_state_t` 值。

---

## 设备通信必须要网关吗？

- 情况 1：节点仅在 mesh 网络内通信。这种情况下，不需要网关。ESP-BLE-MESH 网络是一个泛洪的网络，网络中的消息没有固定的路径，节点与节点之间可以随意通信.
- 情况 2：如果用户想要远程控制网络，比如在到家之前打开某些节点，则需要网关。

---

##  Provisioner 删除网络中的节点时，需要进行哪些操作？

&emsp;&emsp;通常而言，Provisioner 从网络中移除节点主要涉及三个步骤：

- 首先，Provisioner 将需要移除的节点添加至“黑名单”。
- 其次，Provisioner 启动 [密钥更新程序](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/esp-ble-mesh/ble-mesh-terminology.html#ble-mesh-terminology-network-management)。
- 最后，节点执行节点重置程序，切换自身身份为未配网设备。

---

## 在密钥更新的过程中，Provisioner 如何更新节点的网络密钥？

- 通过正确设置参数 `esp_ble_mesh_cfg_client_set_state_t` 中的 `net_key_update`，使用 [Configuration Client Model](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/esp-ble-mesh/ble-mesh-terminology.html#ble-mesh-terminology-foundation-models) API `esp_ble_mesh_config_client_set_state()`，Provisioner 更新节点的网络密钥。
- 通过正确设置参数 `esp_ble_mesh_cfg_client_set_state_t` 中的 `app_key_update`，使用 [Configuration Client Model](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/esp-ble-mesh/ble-mesh-terminology.html#ble-mesh-terminology-foundation-models) API `esp_ble_mesh_config_client_set_state()`，Provisioner 更新节点的应用密钥。

---

## Provisioner 如何管理 mesh 网络中的节点？

&emsp;&emsp;ESP-BLE-MESH 在示例中实现了一些基本的节点管理功能，比如 `esp_ble_mesh_store_node_info()`。 ESP-BLE-MESH 还提供可用于设置节点本地名称的 API `esp_ble_mesh_provisioner_set_node_name()` 和可用于获取节点本地名称的 API `esp_ble_mesh_provisioner_get_node_name()`。

---

## Provisioner 想要控制节点的服务器模型时需要什么？

&emsp;&emsp;Provisioner 在控制节点的服务器模型前，必须包括相应的客户端模型。
&emsp;&emsp;Provisioner 应当添加本地的网络密钥和应用密钥。
- Provisioner 调用 API `esp_ble_mesh_provisioner_add_local_net_key()` 以添加网络密钥。
- Provisioner 调用 API `esp_ble_mesh_provisioner_add_local_app_key()` 以添加应用密钥。

&emsp;&emsp;Provisioner 应当配置自己的客户端模型。
- Provisioner 调用 API `esp_ble_mesh_provisioner_bind_app_key_to_local_model()` 以绑定应用密钥至自己的客户端模型。

---

## 什么时候应该使能节点的 [Relay](https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.1/api-guides/esp-ble-mesh/ble-mesh-terminology.html#ble-mesh-terminology-features) 功能？

- 如果 mesh 网络中检测到的节点很稀疏，用户可以使能节点的 Relay 功能。
- 如果 mesh 网络中检测到的节点很密集，用户可以选择仅使能一些节点的 Relay 功能。
- 如果 mesh 网络大小未知，用户可以默认使能 Relay 功能。

---

## 节点包含什么样的模型？

- ESP-BLE-MESH 中，节点由一系列的模型组成，每个模型实现节点的某些功能。
- 模型分为两种，客户端模型和服务器模型。客户端模型可以获取并设置服务器模型的状态。
- 模型也可以分为 SIG 模型和自定义模型。 SIG 模型的所有行为都由官方定义，而自定义模型的行为均由用户定义。

---

## 每个模型对应的消息格式是不是固定的？

- 消息由 opcode 和 payload 组成，通过 opcode 进行区分。
- 与模型对应的消息的类型和格式都是固定的，这意味着模型之间传输的消息是固定的。

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
