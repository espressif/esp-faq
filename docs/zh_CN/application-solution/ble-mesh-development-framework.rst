BLE Mesh 应用框架
=================

:link_to_translation:`en:[English]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

--------------

被 Provisioner 配网到 ESP-BLE-MESH 网络中的第一个节点的单播地址是不是固定的？
-----------------------------------------------------------------------------

  ``esp_ble_mesh_prov_t`` 中 ``prov_start_address`` 的值用于设置 Provisioner 配网未配网设备的起始地址，即其首先配网的节点的单播地址。单播地址只能在初始化期间设置一次，此后不能修改。

--------------

手机 App 首先配置的节点的单播地址是不是固定的？
-----------------------------------------------

  该 App 将确定单播地址，目前大多数单播地址是固定的。

--------------

配网过程中，认证设备共有多少种方法？提供的范例中 `provided examples <https://github.com/espressif/esp-idf/tree/7d75213/examples/bluetooth/esp_ble_mesh>`__ 使用了什么方法？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  共有四种设备认证方法，即 No OOB、Static OOB、Output OOB 和 Input OOB。提供的范例使用了 No OOB 的方式。

--------------

配置入网前，未配网设备的广播包可以携带哪些信息？
------------------------------------------------

  -  Device UUID
  -  OOB Info
  -  URL Hash (可选的)

--------------

ESP-BLE-MESH 如何打印数据包？
-----------------------------

  示例使用如下函数 ``ESP_LOG_BUFFER_HEX()`` 打印信息语境，而 ESP-BLE-MESH 协议栈使用 ``bt_hex()`` 打印。

--------------

Device UUID 可以用于设备识别吗？
--------------------------------

  是的。每个设备都有独一无二的 Device UUID, 用户可以通过 Device UUID 识别设备。

--------------

如何知道当前 Provisioner 正在配网哪个未配网设备？
-------------------------------------------------

  - ``esp_ble_mesh_prov_t`` 中 ``prov_attention`` 的值由 Provisioner 在配网过程中设置给未配网设备。
  - 该值只能在初始化期间设置一次，此后不能修改。未配网设备加入 mesh 网络后可以用特定的方式来显示自己正在配网，比如灯光闪烁，以告知 Provisioner 其正在配网。

--------------

Provisioner 如何通过获取的 Composition Data 进一步配置节点？
------------------------------------------------------------

  Provisioner 通过调用 `Configuration Client Model <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/esp-ble-mesh/ble-mesh-terminology.html#ble-mesh-terminology-foundation-models>`__ API ``esp_ble_mesh_config_client_set_state()`` 来进行如下配置。

  -  正确设置参数 ``esp_ble_mesh_cfg_client_set_state_t`` 中的 ``app_key_add``，将应用密钥添加到节点中。
  -  正确设置参数 ``esp_ble_mesh_cfg_client_set_state_t`` 中的 ``model_sub_add``，将订阅地址添加到节点的模型中。
  -  正确设置参数 ``esp_ble_mesh_cfg_client_set_state_t`` 中的 ``model_pub_set``，将发布地址添加到节点的模型中。

--------------

节点可以自己添加相应的配置吗？
------------------------------

  本法可用于特殊情况，如测试阶段。

  - 此示例展示了节点如何为自己的模型添加新的组地址。

  .. code:: c

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

   **注：** 使能了节点的 NVS 存储器后，通过该方式添加的组地址以及绑定的应用密钥在设备掉电的情况下不能保存。这些配置信息只有通过 Configuration Client Model 配置时才会保存。

--------------

Provisioner 如何通过分组的方式控制节点？
----------------------------------------

  通常而言，在 ESP-BLE-MESH 网络中实现组控制有两种方法，即组地址方法和虚拟地址方法。假设有 10 个设备，即 5 个带蓝灯的设备和 5 个带红灯的设备。

  - 方案一：5 个蓝灯设备订阅一个组地址，5 个红灯设备订阅另一个组地址。Provisioner 往不同的组地址发送消息，即可实现分组控制设备。
  - 方案二：5 个蓝灯设备订阅一个虚拟地址，5 个红灯设备订阅另一个虚拟地址，Provisioner 往不同的虚拟地址发送消息，即可实现分组控制设备。

--------------

Provisioner 如何知道网络中的某个设备是否离线？
----------------------------------------------

  - 节点离线通常定义为：电源故障或其他原因导致的节点无法与 mesh 网络中的其他节点正常通信的情况。
  - ESP-BLE-MESH 网络中的节点间彼此不连接，它们通过广播通道进行通信。
  - 此示例展示了如何通过 Provisioner 检测节点是否离线。
  - 节点定期给 Provisioner 发送心跳包。如果 Provisioner 超过一定的时间未接收到心跳包，则视该节点离线。

  **注：** 心跳包的设计应该采用单包（字节数小于 11 个字节）的方式，这样收发效率会更高。

--------------

Provisioner 如何将节点添加至多个子网？
--------------------------------------

  节点配置期间，Provisioner 可以为节点添加多个网络密钥，拥有相同网络密钥的节点属于同一子网。Provisioner 可以通过不同的网络密钥与不同子网内的节点进行通信。

--------------

为什么 APP 中显示的节点地址的数量比现有的节点地址更多？
-------------------------------------------------------

  每完成一次快速配网后、开始新一次快速配网前，APP 会存有上次配网的数据，因此 APP 中显示的节点地址的数量比现有的节点地址更多。

--------------

在 EspBleMesh App 中输入的 ``count`` 值有什么用途？
---------------------------------------------------------

  此 count 值提供给 App 配置的代理节点，以决定何时提前开始 Proxy 广播信息。

--------------

运行以下示例 `fast_prov_server <https://github.com/espressif/esp-idf/tree/84b51781c/examples/bluetooth/esp_ble_mesh/ble_mesh_fast_provision/fast_prov_server>`__ 的节点的 Configuration Client Model 何时开始工作？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  使能了 Temporary Provisioner 功能后，Configuration Client Model 会开始工作。

--------------

Temporary Provisioner 功能会一直处于使能的状态吗？
--------------------------------------------------

  节点收到打开/关闭电灯的消息后，所有节点会禁用其 Temporary Provisioner 功能并且转化为一般节点。

--------------

BLE MESH Log ``ran out of retransmit attempts`` 代表什么？
----------------------------------------------------------

  节点发送分段消息时，由于某些原因，接收端未收到完整的消息。节点会重传消息。当重传次数达到最大重传数时，会出现该警告，当前最大重传数为 4。

--------------

BLE Mesh log ``Duplicate found in Network Message Cache`` 代表什么？
--------------------------------------------------------------------

  当节点收到一条消息时，它会把该消息与网络缓存中存储的消息进行比较。如果在缓存中找到相同的消息，这意味着之前已接受过该消息，则该消息会被丢弃。

--------------

BLE Mesh log ``Incomplete timer expired`` 代表什么？
----------------------------------------------------

  当节点在一定时间段（比如 10 秒）内未收到分段消息的所有段时，则 Incomplete 计时器到时，并且出现该警告。

--------------

BLE Mesh log ``No free slots for new incoming segmented messages`` 代表什么？
-----------------------------------------------------------------------------

  当节点没有空间来接收新的分段消息时，会出现该警告。用户可以通过配置 `CONFIG_BLE_MESH_RX_SEG_MSG_COUNT <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.1/api-reference/kconfig.html#config-ble-mesh-rx-seg-msg-count>`__ 扩大空间。

--------------

BLE Mesh log ``No matching TX context for ack`` 代表什么？
----------------------------------------------------------

  当节点收到一个分段 ack 且不能找到任何自己发送的与该 ack 相关的消息时，会出现该警告。

--------------

BLE Mesh log ``Model not bound to AppKey 0x0000`` 代表什么？
------------------------------------------------------------

  当节点发送带有模型的消息且该模型尚未绑定到索引为 0x000 的应用密钥时，会出现该报错。

--------------

BLE Mesh log ``Busy sending message to DST xxxx`` 代表什么？
---------------------------------------------------------------

  该错误表示节点的客户端模型已将消息发送给目标节点，并且正在等待响应，用户无法将消息发送到单播地址相同的同一节点。接收到相应的响应或计时器到时后，可以发送另一条消息。

--------------

为什么会出现 EspBleMesh App 在快速配网期间长时间等待的情况？
------------------------------------------------------------

  快速配网期间，代理节点在配置完一个节点后会断开与 APP 的连接，待所有节点配网完成后再与 APP 重新建立连接。

--------------

Provisoner 如何控制节点的服务器模型？
-------------------------------------

  ESP-BLE-MESH 支持所有 SIG 定义的客户端模型。Provisioner 可以使用这些客户端模型控制节点的服务器模型。客户端模型分为 6 类，每类有相应的功能。

-  Configuration Client Model

   -  API ``esp_ble_mesh_config_client_get_state()`` 可用于获取 Configuration Server Model 的 ``esp_ble_mesh_cfg_client_get_state_t`` 值。
   -  API ``esp_ble_mesh_config_client_set_state()`` 可用于获取 Configuration Server Model 的 ``esp_ble_mesh_cfg_client_set_state_t`` 值。

-  Health Client Model

   -  API ``esp_ble_mesh_health_client_get_state()`` 可用于获取 Health Server Model 的 ``esp_ble_mesh_health_client_get_state_t`` 值。
   -  API ``esp_ble_mesh_health_client_set_state()`` 可用于获取 Health Server Model 的 ``esp_ble_mesh_health_client_set_state_t`` 值。

-  Generic Client Models

   -  API ``esp_ble_mesh_generic_client_get_state()`` 可用于获取 Generic Server Model 的 ``esp_ble_mesh_generic_client_get_state_t`` 值。
   -  API ``esp_ble_mesh_generic_client_set_state()`` 可用于获取 Generic Server Model 的 ``esp_ble_mesh_generic_client_set_state_t`` 值。

-  Lighting Client Models

   -  API ``esp_ble_mesh_light_client_get_state()`` 可用于获取 Lighting Server Model 的 ``esp_ble_mesh_light_client_get_state_t`` 值。
   -  API ``esp_ble_mesh_light_client_set_state()`` 可用于获取 Lighting Server Model 的 ``esp_ble_mesh_light_client_set_state_t`` 值。

-  Sensor Client Models

   -  API ``esp_ble_mesh_sensor_client_get_state()`` 可用于获取 Sensor Server Model 的 ``esp_ble_mesh_sensor_client_get_state_t`` 值。
   -  API ``esp_ble_mesh_sensor_client_set_state()`` 可用于获取 Sensor Server Model 的 ``esp_ble_mesh_sensor_client_set_state_t`` 值。

-  Time and Scenes Client Models

   -  API ``esp_ble_mesh_time_scene_client_get_state()`` 可用于获取 Time and Scenes Server Model 的 ``esp_ble_mesh_time_scene_client_get_state_t`` 值。
   -  API ``esp_ble_mesh_time_scene_client_set_state()`` 可用于获取 Time and Scenes Server Model 的 ``esp_ble_mesh_time_scene_client_set_state_t`` 值。

--------------

设备通信必须要网关吗？
----------------------

  -  情况 1：节点仅在 mesh 网络内通信。这种情况下，不需要网关。ESP-BLE-MESH 网络是一个泛洪的网络，网络中的消息没有固定的路径，节点与节点之间可以随意通信。
  -  情况 2：如果用户想要远程控制网络，比如在到家之前打开某些节点，则需要网关。

--------------

Provisioner 删除网络中的节点时，需要进行哪些操作？
--------------------------------------------------

  通常而言，Provisioner 从网络中移除节点主要涉及三个步骤：

  - 首先，Provisioner 将需要移除的节点添加至“黑名单”。
  - 其次，Provisioner 启动 `密钥更新程序 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/esp-ble-mesh/ble-mesh-terminology.html#ble-mesh-terminology-network-management>`_ 。
  - 最后，节点执行节点重置程序，切换自身身份为未配网设备。

--------------

在密钥更新的过程中，Provisioner 如何更新节点的网络密钥？
--------------------------------------------------------

  - 通过正确设置参数 ``esp_ble_mesh_cfg_client_set_state_t`` 中的 ``net_key_update``，使用 `Configuration Client Model <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/esp-ble-mesh/ble-mesh-terminology.html#ble-mesh-terminology-foundation-models>`_ API ``esp_ble_mesh_config_client_set_state()``，Provisioner 更新节点的网络密钥。
  - 通过正确设置参数 ``esp_ble_mesh_cfg_client_set_state_t`` 中的 ``app_key_update``，使用 `Configuration Client Model <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/esp-ble-mesh/ble-mesh-terminology.html#ble-mesh-terminology-foundation-models>`_ API ``esp_ble_mesh_config_client_set_state()``，Provisioner 更新节点的应用密钥。

--------------

Provisioner 如何管理 mesh 网络中的节点？
----------------------------------------

  - ESP-BLE-MESH 在示例中实现了一些基本的节点管理功能，比如 ``esp_ble_mesh_store_node_info()``。 
  - ESP-BLE-MESH 还提供可用于设置节点本地名称的 API ``esp_ble_mesh_provisioner_set_node_name()`` 和可用于获取节点本地名称的 API ``esp_ble_mesh_provisioner_get_node_name()``。

--------------

Provisioner 想要控制节点的服务器模型时需要什么？
------------------------------------------------

  - Provisioner 在控制节点的服务器模型前，必须包括相应的客户端模型。

  - Provisioner 应当添加本地的网络密钥和应用密钥。

     - Provisioner 调用 API ``esp_ble_mesh_provisioner_add_local_net_key()`` 以添加网络密钥。
     - Provisioner 调用 API ``esp_ble_mesh_provisioner_add_local_app_key()`` 以添加应用密钥。

  - Provisioner 应当配置自己的客户端模型。

     - Provisioner 调用 API ``esp_ble_mesh_provisioner_bind_app_key_to_local_model()`` 以绑定应用密钥至自己的客户端模型。

--------------

什么时候应该使能节点的 `Relay <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.1/api-guides/esp-ble-mesh/ble-mesh-terminology.html#ble-mesh-terminology-features>`__ 功能？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 如果 mesh 网络中检测到的节点很稀疏，用户可以使能节点的 Relay 功能。
  - 如果 mesh 网络中检测到的节点很密集，用户可以选择仅使能一些节点的 Relay 功能。
  - 如果 mesh 网络大小未知，用户可以默认使能 Relay 功能。

--------------

节点包含什么样的模型？
----------------------

  - ESP-BLE-MESH 中，节点由一系列的模型组成，每个模型实现节点的某些功能。
  - 模型分为两种，客户端模型和服务器模型。客户端模型可以获取并设置服务器模型的状态。
  - 模型也可以分为 SIG 模型和自定义模型。 SIG 模型的所有行为都由官方定义，而自定义模型的行为均由用户定义。

--------------

每个模型对应的消息格式是不是固定的？
------------------------------------

  - 消息由 opcode 和 payload 组成，通过 opcode 进行区分。
  - 与模型对应的消息的类型和格式都是固定的，这意味着模型之间传输的消息是固定的。

--------------

节点的模型可以使用哪些函数发送消息？
------------------------------------

  - 对于客户端模型，用户可以调用 API ``esp_ble_mesh_client_model_send_msg()`` 发送消息。
  - 对于服务器模型，用户可以调用 API ``esp_ble_mesh_server_model_send_msg()`` 发送消息。
  - 对于发布，用户可以调用 API ``esp_ble_mesh_model_publish()`` 发布消息。

--------------

如何实现消息传输不丢包？
------------------------

  如果用户要实现消息传输不丢包，则需有应答的消息。等待应答的默认时间在 `CONFIG_BLE_MESH_CLIENT_MSG_TIMEOUT <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/kconfig.html#config-ble-mesh-client-msg-timeout>`__ 中设置。如果发送端等待应答超时，就会触发对应的超时事件。

  **注：** API ``esp_ble_mesh_client_model_send_msg()`` 中可以设置应答的超时时间。如果参数 ``msg_timeout`` 设为 0， 那么超时时间便会采用默认值（4 秒）。

--------------

如何发送无应答的消息？
----------------------

  - 对于客户端模型，用户可以调用 API ``esp_ble_mesh_client_model_send_msg()`` with the parameter ``need_rsp`` set to ``false`` 发送无应答消息。

  - 对于服务器模型，调用 API ``esp_ble_mesh_server_model_send_msg()`` 发送的消息总是无应答的消息。

--------------

发送不分包消息时，最多可携带多少有效字节？
------------------------------------------

  不分包消息的总有效载荷长度（可由用户设置）为 11 个八位位组，因此，如果消息的 opcode 为 2 个八位位组，则该消息可以携带 9 个八位位组的有效信息。 对于 vendor 消息，由于 opcode 是 3 个八位位组，剩余的有效负载长度为 8 个八位位组。

--------------

什么时候应该使能节点的 `Proxy <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.1/api-guides/esp-ble-mesh/ble-mesh-terminology.html#ble-mesh-terminology-features>`__ 功能？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  如果未配网设备将由电话配网，则未配网设备应该使能 Proxy 功能，因为当前几乎所有电话都不支持通过广播承载层发送 ESP-BLE-MESH 数据包。并且，未配网设备成功配网成为 Proxy 节点后，其会通过 GATT 承载层和广播承载层与 mesh 网络中的其他节点通信。

--------------

如何使用代理过滤器？
-----------------------

  代理过滤器用于减少 Proxy Client（如手机）和 Proxy Server（如节点）之间交换的 Network PDU 的数量。另外，通过代理过滤器，Proxy Client 可以明确请求仅接收来自 Proxy Server 的某些目标地址的 mesh 消息。

--------------

如何实现将节点自检的信息发送出来？
----------------------------------

  推荐节点通过 Health Server Model 定期发布其自检结果。

--------------

Relay 节点什么时候可以中继消息？
--------------------------------

  如果要中继消息，消息需满足以下要求。

  - 消息存在于 mesh 网络中。
  - 消息的目的地址不是节点的单播地址。
  - 消息的 TTL 值需大于 1。

--------------

如果一条消息分成几段，那么其他 Relay 节点是接收到一段消息就中继还是等接收到完整的数据包才中继？
-----------------------------------------------------------------------------------------------

  Relay 节点收到其中一段消息时就中继，而非一直等到接收所有的消息。

--------------

设备断电后上电，如何能继续在网络中进行通讯？
--------------------------------------------

  在 menuconfig 中启用配置 ``Store BLE Mesh Node configuration persistently``。

--------------

使用 `Low Power <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.1/api-guides/esp-ble-mesh/ble-mesh-terminology.html#ble-mesh-terminology-features>`__ 功能降低功耗的原理是什么？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -  开启无线电进行收听时，设备消耗能量。使能节点的低功耗功能后，它将在大多数时间内关闭无线电功能。
  -  低功耗节点和好友节点需要合作，因此低功耗节点可以以适当或较低的频率接收消息，而无需一直收听。
  -  当低功耗节点有一些新消息时，好友节点将为其存储消息。低功耗节点可以间隔固定时间轮询好友节点，以查看是否有新的消息。

--------------

节点间如何传输消息？
--------------------

  节点间传输信息的可能应用场景是，一旦烟雾警报检测到高浓度的烟雾，就会触发喷淋设备。 有两种实现方法。

  -  方法 1：喷淋设备订阅组地址。当烟雾警报器检测到高浓度的烟雾时，它会发布一条消息，该消息的目标地址是喷淋设备已订阅的组地址。
  -  方法 2：Provisioner 可以配置喷淋设备的单播地址为烟雾报警器的地址。当检测到高浓度的烟雾时，烟雾警报器以喷淋设备的单播地址为目标地址，将消息发送到喷淋设备。

--------------

何时使用 IV Update 更新程序？
-----------------------------

  一旦节点的底层检测到发送的消息的序列号达到临界值，IV Update 更新程序便会启用。

--------------

为什么需要快速配网？
--------------------

  通常而言，存在少量未配网设备时，用户可以逐个配置。但是如果有大量未配网设备（比如 100 个）时，逐个配置会耗费大量时间。通过快速配网，用户可以在约 50 秒内配网 100 个未配网设备。

--------------

如何启用 IV Update 更新程序？
-----------------------------

  节点可以使用带有 Secure Network Beacon 的 IV Update 更新程序。

--------------

ESP-BLE-MESH 回调函数如何分类？
-------------------------------

  -  API ``esp_ble_mesh_register_prov_callback()`` 用于注册处理配网和入网相关事件的回调函数。
  -  API ``esp_ble_mesh_register_config_client_callback()`` 用于注册处理 Configuration Client Model 相关事件的回调函数。
  -  API ``esp_ble_mesh_register_config_server_callback()`` 用于注册处理 Configuration Server Model 相关事件的回调函数。
  -  API ``esp_ble_mesh_register_health_client_callback()`` 用于注册处理 Health Client Model 相关事件的回调函数。
  -  API ``esp_ble_mesh_register_health_server_callback()`` 用于注册处理 Health Server Model 相关事件的回调函数。
  -  API ``esp_ble_mesh_register_generic_client_callback()`` 用于注册处理 Generic Client Models 相关事件的回调函数。
  -  API ``esp_ble_mesh_register_light_client_callback()`` 用于注册处理 Lighting Client Models 相关事件的回调函数。
  -  API ``esp_ble_mesh_register_sensor_client_callback()`` 用于注册处理 Sensor Client Model 相关事件的回调函数。
  -  API ``esp_ble_mesh_register_time_scene_client_callback()`` 用于注册处理 Time and Scenes Client Models 相关事件的回调函数。
  -  API ``esp_ble_mesh_register_custom_model_callback()`` 用于注册处理自定义模型和未实现服务器模型的相关事件的回调函数。

--------------

未配网设备加入 ESP-BLE-MESH 网络的流程是什么？
----------------------------------------------

  设备通过 Provisioner 加入 ESP-BLE-MESH 网络分为两个阶段，配网阶段和配置阶段。

  - 配网阶段：为设备分配单播地址、添加网络密钥 (NetKey) 等。通过配网，设备加入 ESP-BLE-MESH 网络，身份从未配网设备变为节点。
  - 配置阶段：为节点添加应用密钥 (AppKey), 并将应用密钥绑定到相应模型。配置期间，有些选项是可选的，比如为节点添加订阅地址、设置发布地址等。通过配置，该节点实际上可以向 Provisioner 发送消息，也可以接收来自 Provisioner 的消息。

--------------

Provisioner 的地址是否可以作为节点上报状态消息的目的地址？
----------------------------------------------------------

  Provisioner 的单播地址只能在初始化期间设置一次，此后不能更改。理论而言，只要节点知道 Provisioner 的单播地址，此地址便可用作节点上报状态消息的目的地址。节点在网络配置的过程中可以知道 Provisioner 的单播地址，因为 Provisioner 往节点发送消息时，消息的源地址就是 Provisioner 的单播地址。

  订阅地址也可使用。Provisioner 订阅组地址或者虚拟地址，节点向该订阅地址发送消息。

--------------

如果 Provisioner 想要改变节点状态，其需满足什么条件？
-----------------------------------------------------

  -  需要有和节点的服务器模型相对应的客户端模型。
  -  需要和节点有相同的、可用于加密消息的网络密钥和应用密钥。
  -  需要知道节点的地址，可以是单播地址，也可以是订阅地址。

--------------

Provisioner 的单播地址是不是固定的？
------------------------------------

  ``esp_ble_mesh_prov_t`` 中 ``prov_unicast_addr`` 的值用于设置 Provisioner 的单播地址，只能在初始化期间设置一次，此后不能更改。
                                                                                                                                                                                                                                                                        
--------------

如何使用网络密钥和应用密钥？
----------------------------

  -  网络密钥用于加密网络层的消息。具有相同网络密钥的节点视作在同一网络中，具有不同网络密钥的节点相互之间不能进行通信。
  -  应用密钥用于加密上层传输层中的消息。如果服务器模型和客户端模型绑定的应用密钥不同，则无法实现相互通信。

--------------

是否可以采用固定的网络密钥或应用密钥？
--------------------------------------

  -  API ``esp_ble_mesh_provisioner_add_local_net_key()`` 可以用来添加包含固定值或随机值的网络密钥。
  -  API ``esp_ble_mesh_provisioner_add_local_app_key()`` 可以用来添加包含固定值或随机值的应用密钥。

--------------

如何清除 ESP32 BLE node 的组网信息？
---------------------------------------

  清除 node 的组网信息可以调用 ``esp_ble_mesh_node_local_reset()``

--------------

如何删除某个 node 的组网信息？
-------------------------------

  删除某个节点的信息可以调用 ``esp_ble_mesh_provisioner_delete_node_with_uuid()`` 或 ``esp_ble_mesh_provisioner_delete_node_with_addr()``

--------------

如果 Node 断电了，下次上电是否还要用手机 APP 重新组网？
-----------------------------------------------------------

  可以通过配置 menuconfig 的选项保存配置信息，就不需要重新组网了。``Component config--》Bluetooth Mesh support--》Store Bluetooth Mesh key and configuration persistently``

--------------

1号板子做 provisioner，2,3,4号板子做 Node 。组网成功后，如果1号板子掉电了，重新上电后还能否加入到这个 mesh 网络中？
----------------------------------------------------------------------------------------------------------------------

  1号板子重新上电后，如果 net key，和 app key 没有变化，则可以直接访问这个网络，但是 mesh 网络中 node 的地址，如果不保存会丢失掉，不过你可以通过某种方式重新获取地址。

--------------

BLE_MESH 中，某个 Node 如果掉线了，要如何知道？
-----------------------------------------------

  Node 可以周期发布消息，你可以通过 Health model 周期发送 Heartbeat 消息，或者可以通过 vender model 周期发送自定义消息。

--------------

BLE_MESH 节点间如何实现以字符串的形式通信？
----------------------------------------------

  使用 vendor model，发送端将字符串放入 vendor message 发送，接收端接收消息后按 字符串 解析即可。

--------------

配置ble mesh保存节点信息时初始化partition失败: ``BLE_MESH: Failed to init mesh partition, name ble_mesh, err 261`` 
-------------------------------------------------------------------------------------------------------------------
  
  如果选择 ``Use a specific NVS partition for BLE Meshh`` 选项，请确保 partition.csv 文件包含一个名为 ``ble_mesh`` 的特定分区。

--------------

请问如何在 provisioner 的 demo 中 添加 health_mode？
------------------------------------------------------

  进入 menuconfig，在 ``Component config ->ESP BLE Mesh Support -> Support for BLE Mesh Client Models`` 中勾选上 ``Health Client Model``

--------------

ble_mesh_fast_prov_client 当设备 provisioner 和手机当 provisioner 有什么不一样？
---------------------------------------------------------------------------------

  - ble_mesh_fast_prov_server demo 在收到 ESP_BLE_MESH_MODEL_OP_APP_KEY_ADD opcode 时，一并把 model 的配置自己做好了，并没有像手机 provisioner 那样进行发送 ESP_BLE_MESH_MODEL_OP_MODEL_APP_BIND opcode 把 model APPkey 绑定，
    发送 ``ESP_BLE_MESH_MODEL_OP_MODEL_PUB_SET`` 把 publication 配置好
  - ``ble_mesh_fast_prov_client demo`` 与 ``ble_mesh_fast_prov_server demo`` 是我们提供的一个快速配网的方案，实现了100个节点配置设备入网时间在 60s 以内。为了实现这个功能，我们添加了一些自定义消息(用于设备间自定义信息的传递)

--------------

有什么工具和办法可以查看 ble_mesh node 之间的加密消息吗？
------------------------------------------------------------

  - 数据包解密必须要配置 netkey， appkey， devkey， iv index 的，你可以找一下配置接口。
  - 广播包需要 37，38, 39 三通道同时抓才行，我们一般使用的是专门的仪器。

--------------

app key 是否是厂家可以自己设置？ Unicast address 和 app key 是否有某种关联？
---------------------------------------------------------------------------------

  app key 可以厂家自己设置，它和 Model 是绑定在一起的，和 Unicast address 没有什么关系。

--------------

如果一个 Node 突然掉线，那么通过 Health model 监测消息的机制，是整个 mesh 网络都要轮询的发送 Heartbeat 消息吗？
----------------------------------------------------------------------------------------------------------------

  BLE MESH 网络是没有建立任何连接的，直接通过广播通道发送消息。你可以使用心跳包的方式去检查，心跳包往同一个 Node 发送。 

---------------

主 Node（代理节点） -> 从 Node互相发送消息，用client-server模型可以吗？是否有提供demo来完成？
----------------------------------------------------------------------------------------------

  在我们的V6.0版本中有相关的demo，``ble_mesh_fast_provision/ble_mesh_fast_prov_server`` 中有提供。

--------------

在 NRF 的手机 app 里，右下角 “Setting” 里有个 “Network Key”，可以自由更改，这个修改的是指哪个 network key 呢？
---------------------------------------------------------------------------------------------------------------

  - 在 NRF 的手机 app 里，右下角 “Setting” 里有个 “Network Key”，修改它就意味着修改了 provisioner 的 Netkey，provisioner 配置其它设备入网时会把这个 netkey 分配给入网的节点
  - 如果 provisioner 拥有多个 Netkey ，provisioner 在配置设备时，可以选择使用哪个 NetKey 分配给设备。provisioner 可以使用不同的 Netkey 和网络中的节点进行通讯。每个节点的Netkey都是 provisioner 分配的。

----------------

设备如何加入 BLE-Mesh 网络？
--------------------------------------

  - 可以参考 `ESP-BLE-MESH 快速入门 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/esp-ble-mesh/ble-mesh-index.html#getting-started-with-ble-mesh>`__。

----------------

Bluetooth® LE (BLE) Mesh 数据传送最大的包是多少 Bytes？
--------------------------------------------------------------------------------

  - 应用层单包最大 384 bytes，底层不分包最大 11 bytes。

----------------

能否提供通过 ESP32 BLE-Mesh 组网的例程？配置组网的 APP 可以使用什么软件？
----------------------------------------------------------------------------

  - 可以使用例程 `onoff_server <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/esp_ble_mesh/ble_mesh_node/onoff_server>`_，手机 APP 可以使用 nRF Mesh。
  - 配网过程可参考 `ESP-BLE-MESH 快速入门 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/esp-ble-mesh/ble-mesh-index.html#getting-started-with-esp-ble-mesh>`__。
  
----------------

在 BLE-MESH 中，未配网设备默认的名称是 ESP-BLE-MESH，这个名称在哪里可以修改？
---------------------------------------------------------------------------------------------------------------------

  - 可以使用接口 `esp_ble_mesh_set_unprovisioned_device_name() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/esp-ble-mesh.html?highlight=esp_ble_mesh_set_unprovisioned_device_name#_CPPv442esp_ble_mesh_set_unprovisioned_device_namePKc>`_, 建议在 `esp_ble_mesh_init() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/esp-ble-mesh.html?highlight=esp_ble_mesh_init#_CPPv417esp_ble_mesh_initP19esp_ble_mesh_prov_tP19esp_ble_mesh_comp_t>`_ 后进行调用，否则还会是默认的 ESP-BLE-MESH。

-------------

ESP32 的 BLE-MESH 应用可以连接多少个节点设备？
------------------------------------------------------------------------------------------------------------------------------------------

  - 理论上，ESP32 的 BLE-MESH 应用最大支持接入设备为 32767 个，实际应用中的接入设备数取决于内存占用情况。
  
--------------------------------------------------------

ESP32 如何手动重置 BLE mesh 设备（不通过 mobile provisioning app 或 provisioning device）？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 可以调用 `esp_ble_mesh_node_local_reset <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.1/api-reference/bluetooth/esp-ble-mesh.html?highlight=esp_ble_mesh_node_local_reset#_CPPv429esp_ble_mesh_node_local_resetv>`__ 接口去重置 BLE Mesh Node，擦除所有的配网信息，还需要等到重置事件到达，确认重置成功，调用后，设备需要重新配网。
