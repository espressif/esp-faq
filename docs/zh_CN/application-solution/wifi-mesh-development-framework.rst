ESP-WIFI-MESH 应用框架
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

ESP-WIFI-MESH 占用多大内存？是否需要外部 PSRAM ？
-----------------------------------------------------

  ESP-WIFI-MESH 内存占用约 60 KB。是否需要外部 PSRAM 取决于应用场景的复杂情况，一般性应用无需外部 PSRAM。

--------------

ESP-WIFI-MESH 能否批量 OTA？
---------------------------------

  ESP-WIFI-MESH 设备支持批量 OTA。OTA ⽅式为：根节点下载固件，然后再发至其他节点。具体示例请参考: `mupgrade <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mupgrade>`__。

--------------

ESP32 支持多少设备进行 ESP-WIFI-MESH 组网？
--------------------------------------------------------

  ESP32 支持 1000 个设备进行 ESP-WIFI-MESH 组网。若要稳定连接大量设备，建议在每个 ESP-WIFI-MESH 网络下，组网设备不超过 512 台。

--------------

ESP32 的 ESP-WIFI-MESH Router 模式与 No Router 模式有什么区别？
-----------------------------------------------------------------------------

  - ESP-WIFI-MESH 网络的 Router 模式是根据路由器进行组网，根节点连路由器。
  - No Router 模式是在无路由器的场景下进行自组网，此模式下不可与外部数据交互。

--------------

ESP32 的 ESP-WIFI-MESH 能否在子设备搜索不到路由器信号时完成组网？
---------------------------------------------------------------------

  ESP32 的 ESP-WIFI-MESH 能实现：若拥有配置相同 Wi-Fi 的 SSID ，在子设备没有搜索到 Wi-Fi 时，子设备也可以连接到根节点。

--------------

ESP32 的 ESP-WIFI-MESH 是否可自动修复网络？
------------------------------------------------

  ESP32 的 ESP-WIFI-MESH 可自动修复网络，ESP-WIFI-MESH 有检测网络断线的机制。

--------------

使用 ESP32 的 ESP-WIFI-MESH，如何设置可以在没连接到 Wi-Fi 的情况下形成自组网？
-----------------------------------------------------------------------------------------------

  需要指定一个设备作为 Root 节点，可参考 `说明 <https://github.com/espressif/esp-mdf/blob/master/examples/function_demo/mwifi/README_cn.md>`_ 和 `示例 <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mwifi>`_。

--------------

使用 ESP32 进行 ESP-WIFI-MESH 应用，在组网自动选举根节点时，是否可以指定局部模块进行选举？
----------------------------------------------------------------------------------------------------

  ESP32 的 ESP-WIFI-MESH 可以指定设备为子节点，它将不参与根节点的选举，可实现局部 mesh 网络进行选举。

--------------

使用 ESP32 进行 ESP-WIFI-MESH 应用，在无路由场景下，多个根节点之间能互发消息吗？
-------------------------------------------------------------------------------------------------

  无路由场景下，多个根节点之间不能互发消息。

--------------

ESP-WIFI-MESH 可以批量 OTA 吗？
-----------------------------------------

  - ESP-WIFI-MESH 设备可以批量 OTA。
  - OTA 的方式是根节点下载固件，然后再发至其他节点。
  - 具体示例请参考 https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mupgrade。

--------------

如何查询 ESP-WIFI-MESH APP 端源码？
---------------------------------------

  - iOS 端源码链接: https://github.com/EspressifApp/EspMeshForiOS
  - 安卓端源码链接: https://github.com/EspressifApp/EspMeshForAndroid

--------------

ESP-WIFI-MESH 是否有无路由方案完成自组网？
-----------------------------------------------------

  Demo 中有 `no-router <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mwifi/no_router>`__, 以及 `get-started <https://github.com/espressif/esp-mdf/tree/master/examples/get-started>`__ 两个无路由方案，可以参考。

--------------

利用 Mwifi 自动组网后，如何获得某个节点的所有潜在父节点的信号强度 (rssi) ？
------------------------------------------------------------------------------------------

  - 可以通过 ``mwifi_get_parent_rssi()`` 获取其父节点的信号强度
  - 可以通过例程 https://github.com/espressif/esp-mdf/blob/master/examples/wireless_debug 参与获取其他结点的信号强度

--------------

在 esp-mdf 的 MESH 网络内部，节点之间的通信是基于什么协议？
-------------------------------------------------------------------

  Mesh 网络内部，是基于数据链路层的自定义协议，即我们核心之一。有 ack 机制，但是没有超时/重传机制，如有需求可以自行在应用层添加。

--------------

ESP-WIFI-MESH 可以将所有的节点都连接至路由上吗？
----------------------------------------------------------

  - 只有 root 节点才可以连接上路由器，下面的子节点将会直接或者间接地连接上 root 节点，然后通过 root 节点和路由通讯。

--------------

ESP-WIFI-MESH 的 root 节点能否通过 4G 拨号实现联网？
------------------------------------------------------

  功能可以实现，但目前没有专门针对该场景的应用，可参考 ESP-MDF 中 `no-router <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mwifi/no_router>`__，该 Demo 根节点直接通过串口和电脑通讯，可修改成将数据通过 4G 模块进行传输。

--------------

esp_mesh_set_parent 函数成功连接后，断开 AP，该函数会不断发起重新连接，如何设置重新连接次数？
-----------------------------------------------------------------------------------------------

  - 如果您使用自组网方案，ESP-WIFI-MESH 默认不会重连。当断开时，您需要调用 ``esp_wifi_scan_start``，获取可以连接的设备，以重新设置父节点。参见: `Mesh Manual Networking Example <https://github.com/espressif/esp-idf/tree/4a9f339447cd5b3143f90c2422d8e1e1da9da0a4/examples/mesh/manual_networking>`__。
  - 推荐您使用自组网的方案进行开发。

--------------

设置按钮后报错：``phy_init: failed to load RF calibration data``。
------------------------------------------------------------------------

  乐鑫芯片初次上电会有 RF 自校准，并将数据存在 NVS 里，若擦除了该部分，就会出现这行打印，做全校准。

--------------

如何暂停/恢复 Mwifi？
------------------------

  使用 ``mwifi_stop/mwifi_start`` 暂停/开始 mesh。

--------------

ESP32-S 无路由 MESH 组网，APP 怎么连接 root 接口的 softAP？
-------------------------------------------------------------

  MESH 的 AP 不支持非 mesh 设备接入，您可以使用一个 ESP32 作用 softAP。

--------------

ESP-WIFI-MESH 能连到 AP，但不能连到 AP 上的 TCP SERVER？
---------------------------------------------------------

  请参考 GitHub issue: `mesh -> "with-router" example doesn't work with espressif IDF softAP #71 <https://github.com/espressif/esp-mdf/issues/71>`__。

--------------

Mwifi 例程怎么修改网络的 AP 连接和最大层数？通信时的最大带宽和延时是多少？
----------------------------------------------------------------------------------

  - 可以通过 menuconfig 里面的配置进行修改，位于：Component config -> MDF Mwifi -> Capacity config。
  - 通信性能可参考：`performance <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/mesh.html#performance>`__。

--------------

如何获得实时的传感器返回值？
-------------------------------------

  由于设备端是一个 HTTP server，所以只能由 APP 发起请求，您可以采用如下两种方式获取实时数据：

  - 当传感器数据变化时，通过 UDP 通知手机来主动请求数据。如果使用我们本地通信的协议，发送如下命令使 APP 主动请求设备数据：

  .. code-block:: c  

    data_type.protocol = MLINK_PROTO_NOTICE;
    ret = mwifi_write(NULL, &data_type, "status", strlen("status"), true);
    MDF_ERROR_CONTINUE(ret != MDF_OK, "<%s> mlink_handle", mdf_err_to_name(ret));

  - 搭建一个服务器 (TCP/MQTT/HTTP server)，与服务器建立 TCP 长连接，传感器数据变化将主动上报。

--------------

新节点可能已经安装在设备中，且该设备已经安装在距离 ROOT 节点较远的位置，请问该节点如何加入 ESP-WIFI-MESH 网络？
----------------------------------------------------------------------------------------------------------------------

  - 您使用的应该是 get-started Demo。为了方便用户测试，该 Demo 是无路由的一种方案，即指定了根节点，所以在 root crash 后，其余设备将无法恢复。
  - 可参考 development_kit 中的 light Demo。该 Demo 可配合 ESP-Mesh App 进行使用（Android 版可在 `官网 <https://www.espressif.com/zh-hans/support/download/apps>`_ 下载，iOS 版可在 App Store 搜索 ESP-Mesh 下载测试）。
  - 该 Demo 示例不指定根节点，由设备自行选举产生，需要配合路由器使用。此种方案下，如果 root 出现故障，剩余设备会自动重新完成组网并连上路由，不需要用户干预。

--------------

ESP-WIFI-MESH App 源码是否开放？
-----------------------------------------------

  - 我们已经将 ESP-Mesh App 源码开放到了 GitHub 上，请参考 `EspMeshForAndroid <https://github.com/EspressifApp/EspMeshForAndroid>`_ 和 `EspMeshForiOS <https://github.com/EspressifApp/EspMeshForAndroid>`_。
  - 如果在使用中有任何疑问或 Bug，都可以在 GitHub 或者这里进行留言提问，我们会在第一时间进行处理。

--------------

Wi-Fi Mesh 数据传送最大的包为多少 Bytes？
------------------------------------------------------------------------------------------

  - 最大为 1456 Bytes。

--------

ESP32 的 Wi-Fi Mesh 支持 No Router 自组网吗？
--------------------------------------------------------------------------------------------------------------------------

  - ESP32 的 Wi-Fi Mesh 支持 No Router 自组网，可参见例程 `esp-mdf/examples/function_demo/mwifi/no_router <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mwifi/no_router>`_。

-----------------

ESP32 使用 Wi-Fi Mesh 时允许的最大节点层数是多少？
--------------------------------------------------------------------------------------------

  - 在 WiFi Mesh 网络中，可以通过 `esp_mesh_set_max_layer() <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/network/esp_mesh.html#_CPPv422esp_mesh_set_max_layeri>`_ 函数设置网络最大层数。
  - 对于树形拓扑结构，最大值为 25；对于链式拓扑结构，最大值为 1000。
  
---------------------

使用 ESP32 开发板测试 `esp-mdf/examples/function_demo/mwifi/router <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mwifi/router>`_ 例程，ESP32 连接路由器后，在路由器连接端显示的设备名称为 “espressif”，如何修改此名称？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 在 menuconfig → Component config → LWIP ——> (espressif) Local netif hostname 中修改设置即可。

---------------------

Wi-Fi Mesh 可以通过 TCP Server 给特定节点发送消息吗？
------------------------------------------------------------------------------------------------------------------------------

  - Wi-Fi Mesh 网络可在 TCP 服务器中发送数据到指定节点或组地址，可参考 `demo <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mwifi/router>`_。
  
--------------------

在 ESP32 Wi-Fi Mesh 网络运行过程中，若根 (Root) 节点丢失，系统会反馈什么事件？
--------------------------------------------------------------------------------------------

  - 若根 (Root) 节点丢失，所有节点将会触发 MDF_EVENT_MWIFI_PARENT_DISCONNECTED (MESH_EVENT_PARENT_DISCONNECTED)，然后开始重新扫描 (Scan)，进行重新选举，直到选举出新的根 (Root) 节点。

----------------

使用 ESP32 进行 Wi-Fi Mesh 应用开发，目前使用的是 esp_mesh_send() 函数，发现服务器没有接收到任何数据。如何将数据从叶节点 (leaf node) 传输到外部服务器？ 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - esp_mesh_send() 只能用于 Wi-Fi Mesh 网络内部数据通信。
  - 叶节点 (leaf node) 往外部服务器发送数据，需要通过根节点 (root node) 转发数据。
  - 正确的做法是：叶节点先将数据发给根节点，根节点再把数据发给外部服务器。

---------------

ESP-MESH 设备组网之后如何做 OTA 升级？
--------------------------------------------------------------------------------------------------------------------------------

  - ROOT 节点可以连接服务器获取到升级 bin 文件，然后把固件通过 MAC 地址去发送给对应的模组进行 OTA 升级。
  - 详情请参考 `mupgrade demo <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mupgrade>`_。

---------------

是否有 ESP-MESH 灯参考设计？
--------------------------------------------------------------------------------------------------------------------------------

  - 灯的整体设计是由第三方工厂完成的，我们并没有相关原理图或者 PCB 布局。但是单从模块角度，我们只需要给芯片供电，芯片输出 PWM 控制灯的颜色或色温变化即可，并没有太复杂的设计。
  - 可以参考 `ESP-MDF <https://github.com/espressif/esp-mdf>`_ 获取更多关于 MESH 的信息。

---------------

ESP-MESH 节点不做任何配置，默认是什么模式？
--------------------------------------------------------------------------------------------------------------------------------

  - 默认是 IDLE 模式。

---------------

ESP-MESH 启动时开启 AP+STA 模式，手机可以搜索到 AP 吗？
-----------------------------------------------------------------------------------------------------------------------------------

  - 不可以，ESP-MESH 是乐鑫私有协议, 详情请参考 `WIFI-MESH 介绍 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/esp-wifi-mesh.html>`_。

---------------

设备已经组网完成，新增设备是否需要全部重新扫描？
--------------------------------------------------------

  - 不需要，只需要在当前子节点中扫描，找到信号强度最好的那个节点作为它的父节点即可。

------------------------

ESP32 作为主设备对多个从设备进行时间同步，是否可以满足误差在 2 ms 内的需求？ 
------------------------------------------------------------------------------------------------------------------------------------------

  - 针对此应用场景，建议基于 esp-mdf 来开发， 可参考 `esp-mdf/examples/development_kit/light <https://github.com/espressif/esp-mdf/blob/master/examples/development_kit/light/main/light_example.c>`_ 例程。
  - 使用 `esp_mesh_get_tsf_time() <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.2/esp32/api-reference/network/esp_mesh.html?highlight=esp_mesh_get_tsf_time#_CPPv421esp_mesh_get_tsf_time>`_ 来实现，此精度可满足需求。

---------------

ESP-MESH 中如何获取节点类型？
--------------------------------------------------------------------------------------------------------------------------------

  - 可以调用 `esp_mesh_get_type <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.1/api-reference/network/esp_mesh.html?highlight=esp_mesh_get_type#_CPPv417esp_mesh_get_typev>`_ 接口获取。

---------------
 
ESP-Mesh 根节点通过 ethernet 向服务发消息示例？
---------------------------------------------------------------------------------

  - 请参考 `root_on_ethnernet <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mwifi/root_on_ethernet/>`_ 示例。
