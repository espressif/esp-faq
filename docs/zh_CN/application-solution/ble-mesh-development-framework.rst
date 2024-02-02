ESP-BLE-MESH 应用框架
========================

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

更多有关 ESP-BLE-MESH 的 FAQ 请参考 `ESP-BLE-MESH 常见问题手册 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/esp-ble-mesh/ble-mesh-faq.html>`__。

为什么会出现 ESP-BLE-MESH 应用程序在快速配网期间长时间等待的情况？
---------------------------------------------------------------------------------

  快速配网期间，代理节点会在配置完一个节点后断开与应用程序的连接，待所有节点配网完成后再与应用程序重新建立连接。快速配网期间长时间等待可能是由于：

  - 网络拓扑结构复杂：如果网络中节点数量较多，且拓扑结构比较复杂，Provisioner 可能需要更长的时间来扫描网络和与节点进行通信。
  - 网络信号不稳定：如果网络信号不稳定，通信可能会受到干扰或丢失，从而导致应用程序等待时间变长。
  - 节点响应时间较长：如果节点响应时间较长，可能会导致 Provisioner 等待超时并重新发送消息，从而导致应用程序等待时间变长。
  - 应用程序与 Provisioner 通信故障：如果应用程序与 Provisioner 之间通信故障，可能会导致应用程序等待时间变长。

--------------

如何清除 ESP-BLE-MESH 节点的组网信息？/ 如何手动重置 ESP-BLE-MESH 设备？
------------------------------------------------------------------------------------------------------------

  可以调用 `esp_ble_mesh_node_local_reset() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/esp-ble-mesh.html?highlight=esp_ble_mesh_node_local_reset#_CPPv429esp_ble_mesh_node_local_resetv>`_。

--------------

配网器如何删除某个节点的组网信息？
---------------------------------------------------------

  删除某个节点的信息可以调用 `esp_ble_mesh_provisioner_delete_node_with_uuid() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/esp-ble-mesh.html?highlight=esp_ble_mesh_provisioner_delete_node_with_uuid#_CPPv446esp_ble_mesh_provisioner_delete_node_with_uuidAL16E_K7uint8_t>`_ 或 `esp_ble_mesh_provisioner_delete_node_with_addr() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/esp-ble-mesh.html?highlight=esp_ble_mesh_provisioner_delete_node_with_uuid#_CPPv446esp_ble_mesh_provisioner_delete_node_with_addr8uint16_t>`_。

--------------

如果节点断电了，下次上电是否还要用手机应用程序重新组网？
-----------------------------------------------------------

  可以前往 menuconfig，通过 ``Component config`` > ``Bluetooth Mesh support`` > ``Store Bluetooth Mesh key and configuration persistently`` 的选项保存配置信息，不需要重新组网。

--------------

1 号开发板做 Provisioner，2、3、4 号开发板做节点。组网成功后，如果 1 号开发板掉电了，重新上电后还能否加入到这个 mesh 网络中？
--------------------------------------------------------------------------------------------------------------------------------------

  1 号开发板重新上电后，如果 NetKey 和 AppKey 没有变化，即可直接加入该网络。但是如果没有保存 mesh 网络中节点的地址，则地址将会丢失。

--------------

ESP-BLE-MESH 中，如果某个节点掉线了，要如何知道？
-----------------------------------------------------------

  节点可以周期发布消息，你可以通过健康模型 (Health Model) 周期发送心跳 (heart) 消息，或者可以通过自定义模型 (Vendor Model) 周期发送自定义消息 (vendor message)。

--------------

ESP-BLE-MESH 节点间如何实现以字符串的形式通信？
---------------------------------------------------------

  使用 Vendor Model，发送端将字符串放入 vendor message 发送，接收端接收消息后按字符串解析即可。

--------------

配置 ESP-BLE-MESH 保存节点信息时初始化分区失败，报错为 ``BLE_MESH: Failed to init mesh partition, name ble_mesh, err 261``，如何解决？
--------------------------------------------------------------------------------------------------------------------------------------

  如果选择 ``Use a specific NVS partition for BLE Mesh`` 选项，请确保 partition.csv 文件包含一个名为 ``ble_mesh`` 的特定分区。

--------------

如何在 Provisioner 的例程中添加 Health Model？
------------------------------------------------------

  进入 menuconfig，在 ``Component config`` -> ``ESP BLE Mesh Support`` -> ``Support for BLE Mesh Client Models`` 中勾选上 ``Health Client Model``。

--------------

使用 ble_mesh_fast_prov_client 作为 Provisioner 和手机作为 Provisioner 有什么不一样？
---------------------------------------------------------------------------------------------------

  - ``ble_mesh_fast_prov_server`` 例程在收到 ESP_BLE_MESH_MODEL_OP_APP_KEY_ADD opcode 时，一并把模型配置好了，而手机 Provisioner 则需要发送 ESP_BLE_MESH_MODEL_OP_MODEL_APP_BIND opcode 绑定模型的 AppKey，再发送 ``ESP_BLE_MESH_MODEL_OP_MODEL_PUB_SET`` 配置 publication。
  - ``ble_mesh_fast_prov_client`` 与 ``ble_mesh_fast_prov_server`` 例程是乐鑫提供的快速配网方案，实现了 100 个节点配置设备入网时间在 60 s 以内。为了实现这个功能，我们添加了一些自定义消息，用于设备间自定义信息的传递。

--------------

有什么工具和办法可以查看 ESP-BLE-MESH 节点之间的加密消息吗？
------------------------------------------------------------

  - 数据包解密必须配置 NetKey、AppKey、DevKey 以及 IV Index，您可以尝试查看配置接口。
  - 广播包需要 37、38、39 三通道同时抓，一般需要使用到专门的仪器。

--------------

厂家是否可以自行设置 AppKey？单播地址和 AppKey 是否有某种关联？
---------------------------------------------------------------------------------

  AppKey 可以厂家自行设置，它和模型是绑定在一起的，和单播地址没有关系。

--------------

如果一个节点突然掉线，那么通过 Health Model 监测消息的机制，是整个 mesh 网络都要轮询的发送 Heartbeat 消息吗？
----------------------------------------------------------------------------------------------------------------

  ESP-BLE-MESH 网络没有建立任何连接，直接通过广播通道发送消息。您可以向同一个节点发送心跳包进行检查。

---------------

主节点（代理节点）与从节点互相发送消息，可以用 client-server 模型吗？是否有提供示例？
-------------------------------------------------------------------------------------------------------------------------------

  请参见 `ble_mesh_fast_provision/ble_mesh_fast_prov_server <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/esp_ble_mesh/fast_provisioning/fast_prov_server>`__ 示例。

--------------

在 nRF 的手机应用程序里，右下角 ``Setting`` 里有个 ``Network Key``，可以自由更改，这里修改的是谁的 NetKey 呢？
---------------------------------------------------------------------------------------------------------------

  - 在 nRF 的手机应用程序里，``Network Key`` 修改的是 Provisioner 的 NetKey，Provisioner 配置其它设备入网时会把这个 NetKey 分配给入网的节点。
  - 如果 Provisioner 拥有多个 NetKey，Provisioner 在配置设备时，可以选择使用哪个 NetKey 分配给设备。Provisioner 可以使用不同的 NetKey 和网络中的节点进行通讯。每个节点的 NetKey 都是 Provisioner 分配的。

----------------

设备如何加入 ESP-BLE-MESH 网络？
--------------------------------------

  可以参考 `ESP-BLE-MESH 快速入门 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/esp-ble-mesh/ble-mesh-index.html#getting-started-with-ble-mesh>`__。

----------------

ESP-BLE-MESH 数据传送最大的包是多少字节？
--------------------------------------------------------------------------------

  应用层单包最大 384 字节，底层不分包最大 11 字节。

----------------

能否提供通过 ESP32 ESP-BLE-MESH 组网的例程？配置组网的应用程序可以使用什么软件？
--------------------------------------------------------------------------------------------

  - 可以使用例程 `onoff_server <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/esp_ble_mesh/onoff_models/onoff_server>`_，手机应用程序可以使用 nRF Mesh。
  - 配网过程可参考 `ESP-BLE-MESH 快速入门 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/esp-ble-mesh/ble-mesh-index.html#getting-started-with-ble-mesh>`__。

----------------

在 ESP-BLE-MESH 中，未配网设备默认的名称是 ESP-BLE-MESH，如何修改这个名称呢？
---------------------------------------------------------------------------------------------------------------------

  可以使用接口 `esp_ble_mesh_set_unprovisioned_device_name() <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/bluetooth/esp-ble-mesh.html?highlight=esp_ble_mesh_set_unprovisioned_device_name#_CPPv442esp_ble_mesh_set_unprovisioned_device_namePKc>`_，建议在 `esp_ble_mesh_init() <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/bluetooth/esp-ble-mesh.html?highlight=esp_ble_mesh_init#_CPPv417esp_ble_mesh_initP19esp_ble_mesh_prov_tP19esp_ble_mesh_comp_t>`_ 后进行调用，否则还会是默认的 ESP-BLE-MESH。

-------------

ESP32 的 ESP-BLE-MESH 应用可以连接多少个节点设备？
------------------------------------------------------------------------------------------------------------------------------------------

  理论上，ESP32 的 ESP-BLE-MESH 应用最大支持接入设备为 32767 个，实际应用中的接入设备数取决于内存占用情况。

--------------------------------------------------------

ESP32 长时间运行 ESP-BLE-MESH 程序后，发现客户端向服务器发送消息时出现分段错误，ESP-BLE-MESH 打印日志 ``NO multi-segment messsage contexts available``。如何解决？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  您可以前往 ``Component config`` > ``ESP BLE Mesh Support`` > ``Maximum number of simultaneous outgoing segmented messages``，通过配置 ``BLE_MESH_TX_SEG_MSG_COUNT`` 来扩展空间。

-----------

使用 ESP32 ESP-BLE-MESH 应用，是否可以关闭 NetKey 和 IV Update？
----------------------------------------------------------------------------------------------------------------------

  不可以。NetKey 和 IV Update 必须保持开启。

--------------

如何在开启 BLE MESH 情况下接收其它 ADV 广播包？
-----------------------------------------------------------------------------------------------------------------------

  在 menuconfig 中开启 BLE_MESH_BLE_COEX_SUPPORT，通过调用 `esp_ble_mesh_register_ble_callback() <https://github.com/espressif/esp-idf/blob/b3f7e2c8a4d354df8ef8558ea7caddc07283a57b/components/bt/esp_ble_mesh/api/core/include/esp_ble_mesh_ble_api.h#L84>`__ 注册回调，然后通过 `esp_ble_mesh_start_ble_scanning() <https://github.com/espressif/esp-idf/blob/b3f7e2c8a4d354df8ef8558ea7caddc07283a57b/components/bt/esp_ble_mesh/api/core/include/esp_ble_mesh_ble_api.h#L167>`__ 开启扫描，即可收到其他广播包。
