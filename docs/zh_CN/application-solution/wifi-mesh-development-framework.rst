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

.. note::

  如您有新的 Wi-Fi Mesh 相关应用场景需求，推荐您直接使用我们新推出的 `ESP-Mesh-Lite 方案 <https://github.com/espressif/esp-mesh-lite>`__，而不是 Wi-Fi Mesh。

--------------

ESP-WIFI-MESH 占用多大内存？是否需要外部 PSRAM？
-----------------------------------------------------

  ESP-WIFI-MESH 内存占用约 60 KB。是否需要外部 PSRAM 取决于应用场景的复杂情况，一般性应用无需外部 PSRAM。

--------------

ESP-WIFI-MESH 能否批量 OTA？
---------------------------------

  ESP-WIFI-MESH 设备支持批量 OTA。OTA ⽅式为：根节点下载固件，再发至其他节点。具体示例请参考 `Mupgrade <https://github.com/espressif/esp-mdf/blob/master/examples/function_demo/mupgrade/README_cn.md>`__。

--------------

ESP32 支持多少设备进行 ESP-WIFI-MESH 组网？
--------------------------------------------------------

  ESP32 支持 1000 个设备进行 ESP-WIFI-MESH 组网。若要稳定连接大量设备，建议每个 ESP-WIFI-MESH 网络下的组网设备不超过 512 台。

--------------

ESP32 的 ESP-WIFI-MESH Router 模式与 No Router 模式有什么区别？
-----------------------------------------------------------------------------

  - ESP-WIFI-MESH 网络的 Router 模式是根据路由器进行组网，根节点连路由器。
  - No Router 模式是在无路由器的场景下进行自组网，此模式下不可与外部数据交互。

--------------

ESP32 的 ESP-WIFI-MESH 能否在子节点搜索不到路由器信号时完成组网？
---------------------------------------------------------------------

  若拥有配置相同 Wi-Fi 的 SSID，在子节点没有搜索到 Wi-Fi 时，ESP32 的 ESP-WIFI-MESH 也支持子节点连接到根节点。

--------------

ESP32 的 ESP-WIFI-MESH 是否可自动修复网络？
------------------------------------------------

  ESP32 的 ESP-WIFI-MESH 有检测网络断线的机制，可自动修复网络。

--------------

使用 ESP32 的 ESP-WIFI-MESH，在没连接到 Wi-Fi 的情况下，如何设置形成自组网？
-----------------------------------------------------------------------------------------------

  需要指定一个设备作为根节点，可参考 Mwifi `说明 <https://github.com/espressif/esp-mdf/blob/master/examples/function_demo/mwifi/README_cn.md>`_ 及 `示例 <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mwifi>`_。

--------------

使用 ESP32 的 ESP-WIFI-MESH，在组网自动选举根节点时，是否可以指定局部模块进行选举？
----------------------------------------------------------------------------------------------------

  ESP32 的 ESP-WIFI-MESH 可以指定设备为子节点。指定后，该设备将不参与根节点的选举，从而实现局部 Mesh 网络进行选举。

--------------

使用 ESP32 的 ESP-WIFI-MESH，在无路由场景下，多个根节点之间能互发消息吗？
-------------------------------------------------------------------------------------------------

  无路由场景下，多个根节点之间不能互发消息。

--------------

如何查询 ESP-WIFI-MESH APP 端源码？
---------------------------------------

  - iOS 端源码链接：https://github.com/EspressifApp/EspMeshForiOS
  - 安卓端源码链接：https://github.com/EspressifApp/EspMeshForAndroid

--------------

ESP-WIFI-MESH 是否有完成自组网的无路由方案？
-----------------------------------------------------

  有 `No Router <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mwifi/no_router>`__ 以及 `get_started <https://github.com/espressif/esp-mdf/tree/master/examples/get-started>`__ 两个无路由方案，可以参考。

--------------

利用 Mwifi 自动组网后，如何获得某个节点的所有潜在父节点的信号强度 (RSSI)？
------------------------------------------------------------------------------------------

  - 可以通过 ``mwifi_get_parent_rssi()`` 获取其父节点的信号强度。
  - 可以参考 `ESP-NOW debug 接收板示例 <https://github.com/espressif/esp-mdf/blob/master/examples/wireless_debug/README_cn.md>`__，获取其他节点的信号强度。

--------------

在 esp-mdf 的 Mesh 网络内部，节点之间基于什么协议进行通信？
-------------------------------------------------------------------

  Mesh 网络内部是基于数据链路层的自定义协议，这也是我们的核心协议之一。支持 ACK 机制，但是没有超时/重传机制，如有需求可以自行在应用层添加。

--------------

ESP-WIFI-MESH 可以将所有的节点都连接至路由上吗？
----------------------------------------------------------

  只有根节点才可以连接上路由器，下面的子节点将会直接或者间接地连接上根节点，然后通过根节点和路由通讯。

--------------

ESP-WIFI-MESH 的根节点能否通过 4G 拨号实现联网？
------------------------------------------------------

  可以实现，但目前没有专门针对该场景的应用。可参考 ESP-MDF 中的 `No Router <https://github.com/espressif/esp-mdf/blob/master/examples/function_demo/mwifi/no_router/README_cn.md>`__ 示例，根节点直接通过串口和电脑通讯，也可配置为通过 4G 模块传输数据。

--------------

esp_mesh_set_parent 函数成功连接后，如果断开 AP，则该函数会不断发起重新连接，如何设置重新连接次数？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 如果您使用自组网方案，ESP-WIFI-MESH 默认不会重连。当断开时，您需要调用 ``esp_wifi_scan_start``，获取可以连接的设备，重新设置父节点，请参见 `Mesh 手动组网示例 <https://github.com/espressif/esp-idf/tree/4a9f339447cd5b3143f90c2422d8e1e1da9da0a4/examples/mesh/manual_networking>`__。
  - 推荐您使用自组网的方案进行开发。

--------------

为什么设置按钮后报错：``phy_init: failed to load RF calibration data``？
------------------------------------------------------------------------

  乐鑫芯片初次上电会有 RF 自校准，并将数据存在 NVS 里。若擦除了该部分，就会打印此行报错，做全校准。

--------------

如何暂停/恢复 Mwifi？
------------------------

  使用 ``mwifi_stop/mwifi_start`` 暂停/恢复 Mesh。

--------------

ESP32 系列芯片无路由 Mesh 组网，APP 怎么连接 root 接口的 softAP？
------------------------------------------------------------------------------------------------------------------------------------------------------------

  无路由 Mesh 场景下，Mesh 设备开启的 softAP 不支持除了 Mesh 设备以外的设备接入。如果需要手机等非 Mesh 设备接入，建议使用 `ESP-Mesh-Lite <https://github.com/espressif/esp-mesh-lite/tree/master>`__。

--------------

ESP-WIFI-MESH 能连到 AP，但不能连到 AP 上的 TCP SERVER，如何解决？
--------------------------------------------------------------------------------------------------------------------------------------------------------

  请参考 GitHub issue: `mesh -> "with-router" example doesn't work with espressif IDF softAP #71 <https://github.com/espressif/esp-mdf/issues/71>`__。

--------------

Mwifi 示例怎么修改网络的 AP 连接和最大层数？通信时的最大带宽和延时是多少？
----------------------------------------------------------------------------------

  - 可以前往 menuconfig，通过 ``Component config`` > ``MDF Mwifi`` > ``Capacity config`` 修改配置。
  - 通信性能可参考 `性能 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/esp-wifi-mesh.html#mesh-network-performance>`__ 小节。
  - WIFI-MESH 带宽可通过 `ESP-WIFI-MESH 控制台调试示例 <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mwifi/console_test>`__ 进行测试。

--------------

如何获得实时的传感器返回值？
-------------------------------------

  由于设备端是一个 HTTP 服务器，所以只能由 APP 发起请求，您可以采用如下两种方式获取实时数据：

  - 当传感器数据变化时，通过 UDP 通知手机来主动请求数据。如果使用我们本地通信的协议，发送如下命令使 APP 主动请求设备数据：

  .. code-block:: c

    data_type.protocol = MLINK_PROTO_NOTICE;
    ret = mwifi_write(NULL, &data_type, "status", strlen("status"), true);
    MDF_ERROR_CONTINUE(ret != MDF_OK, "<%s> mlink_handle", mdf_err_to_name(ret));

  - 搭建一个服务器 (TCP/MQTT/HTTP server)，与服务器建立 TCP 长连接后，传感器数据变化将主动上报。

--------------

新节点可能已经安装在设备中，且该设备已经安装在距离根节点较远的位置，请问该节点如何加入 ESP-WIFI-MESH 网络？
----------------------------------------------------------------------------------------------------------------------

  - 您使用的应该是 get-started 示例。为了方便用户测试，该示例是无路由的一种方案，即指定了根节点，所以在根节点崩溃后，其余设备将无法恢复。
  - 可参考 development_kit 中的 light 示例。该示例可配合 ESP-Mesh App 进行使用（Android 版可在 `官网 <https://www.espressif.com/zh-hans/support/download/apps>`_ 下载，iOS 版可在 App Store 搜索 ESP-Mesh 下载测试）。
  - 该示例不指定根节点，由设备自行选举产生，需要配合路由器使用。此种方案下，如果根节点出现故障，剩余设备会自动重新完成组网并连上路由，不需要用户干预。

--------------

ESP-WIFI-MESH App 源码是否开放？
-----------------------------------------------

  - 我们已经将 ESP-Mesh App 源码开放到了 GitHub 上，请参考 `EspMeshForAndroid <https://github.com/EspressifApp/EspMeshForAndroid>`_ 和 `EspMeshForiOS <https://github.com/EspressifApp/EspMeshForAndroid>`_。
  - 如果在使用中有任何疑问或 Bug，都可以在 GitHub 或者这里进行留言提问，我们会在第一时间进行处理。

--------------

Wi-Fi Mesh 数据传送最大的包为多少字节？
------------------------------------------------------------------------------------------

  最大为 1456 字节。

--------

ESP32 的 Wi-Fi Mesh 支持无路由自组网吗？
--------------------------------------------------------------------------------------------------------------------------

  ESP32 的 Wi-Fi Mesh 支持无路由自组网，可参见 `No Router <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mwifi/no_router>`_ 示例。

-----------------

ESP32 使用 Wi-Fi Mesh 时允许的最大节点层数是多少？
-------------------------------------------------------------------------------------------

  - 在 Wi-Fi Mesh 网络中，可以通过 `esp_mesh_set_max_layer() <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/network/esp-wifi-mesh.html#_CPPv422esp_mesh_set_max_layeri>`_ 函数设置网络最大层数。
  - 对于树形拓扑结构，最大值为 25；对于链式拓扑结构，最大值为 1000。

---------------------

使用 ESP32 开发板测试 `esp-mdf/examples/function_demo/mwifi/router <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mwifi/router>`_ 示例，ESP32 连接路由器后，在路由器连接端显示的设备名称为 “espressif”，如何修改此名称？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  前往 menuconfig，在 ``Component config`` > ``LWIP`` > ``(espressif) Local netif hostname`` 中修改即可。

---------------------

Wi-Fi Mesh 可以通过 TCP 服务器给特定节点发送消息吗？
------------------------------------------------------------------------------------------------------------------------------

  Wi-Fi Mesh 网络可在 TCP 服务器中发送数据到指定节点或组地址，可参考 `Mwifi 有路由器示例 <https://github.com/espressif/esp-mdf/blob/master/examples/function_demo/mwifi/router/README_cn.md>`_。

--------------------

在 ESP32 Wi-Fi Mesh 网络运行过程中，若根节点丢失，系统会反馈什么事件？
--------------------------------------------------------------------------------------------

  若根节点丢失，所有节点将会触发 MDF_EVENT_MWIFI_PARENT_DISCONNECTED (MESH_EVENT_PARENT_DISCONNECTED)，随即开始重新扫描，进行重新选举，直到选举出新的根节点。

----------------

使用 ESP32 进行 Wi-Fi Mesh 应用开发，目前使用的是 esp_mesh_send() 函数，发现服务器没有接收到任何数据。如何将数据从叶节点传输到外部服务器？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - esp_mesh_send() 只能用于 Wi-Fi Mesh 网络内部数据通信。
  - 叶节点往外部服务器发送数据，需要通过根节点转发数据。
  - 正确的做法是：叶节点先将数据发给根节点，根节点再把数据发给外部服务器。

---------------

ESP-MESH 设备组网之后如何实现 OTA 升级？
--------------------------------------------------------------------------------------------------------------------------------

  - 根节点可以连接服务器获取到升级 bin 文件，然后把固件通过 MAC 地址发送给对应的模组进行 OTA 升级。
  - 详情请参考 `Mupgrade 示例 <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mupgrade>`_。

---------------

是否有 ESP-MESH 灯参考设计？
--------------------------------------------------------------------------------------------------------------------------------

  - 灯的整体设计是由第三方工厂完成的，我们并没有相关原理图或者 PCB 布局。但是单从模块角度，我们只需要给芯片供电，芯片输出 PWM 控制灯的颜色或色温变化即可，并没有太复杂的设计。
  - 可以参考 `ESP-MDF <https://github.com/espressif/esp-mdf>`_ 获取更多关于 Mesh 的信息。

---------------

ESP-MESH 节点默认是什么模式？
--------------------------------------------------------------------------------------------------------------------------------

  默认为 IDLE 模式。

---------------

ESP-MESH 启动时开启 AP+STA 模式，手机可以搜索到 AP 吗？
-----------------------------------------------------------------------------------------------------------------------------------

  不可以，ESP-MESH 是乐鑫私有协议。详情请参考 `WIFI-MESH 介绍 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/esp-wifi-mesh.html>`_。

---------------

设备已经组网完成，新增设备是否需要全部重新扫描？
--------------------------------------------------------

  不需要，只需要在当前子节点中扫描，找到信号强度最好的那个节点作为它的父节点即可。

------------------------

ESP32 作为主设备对多个从设备进行时间同步，是否可以满足误差在 2 ms 内的需求？
------------------------------------------------------------------------------------------------------------------------------------------

  - 针对此应用场景，建议基于 esp-mdf 来开发，可参考 `light_example <https://github.com/espressif/esp-mdf/blob/master/examples/development_kit/light/main/light_example.c>`_ 示例。
  - 使用 `esp_mesh_get_tsf_time() <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/network/esp-wifi-mesh.html#_CPPv421esp_mesh_get_tsf_timev>`_ 可满足此精度需求。

---------------

ESP-MESH 中如何获取节点类型？
--------------------------------------------------------------------------------------------------------------------------------

  可以调用 `esp_mesh_get_type <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.1/api-reference/network/esp_mesh.html?highlight=esp_mesh_get_type#_CPPv417esp_mesh_get_typev>`_ 接口获取节点类型。

---------------

有没有 ESP-Mesh 根节点通过 Ethernet 向服务发消息的示例？
---------------------------------------------------------------------------------

  请参考 `Mwifi Ethernet 根节点示例 <https://github.com/espressif/esp-mdf/blob/master/examples/function_demo/mwifi/root_on_ethernet/README_cn.md>`_。

---------------

`ESP-Mesh-Lite <https://github.com/espressif/esp-mesh-lite/tree/master>`_ 解决方案是否支持无路由器的应用场景？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 支持，ESP-Mesh-Lite 解决方案支持的应用场景可参见 `ESP-Mesh-Lite 特性 <https://github.com/espressif/esp-mesh-lite/blob/master/components/mesh_lite/CHANGELOG_CN.md>`_ 说明。
  - 可基于 `Mesh-Lite 局域网控制示例 <https://github.com/espressif/esp-mesh-lite/blob/master/examples/mesh_local_control/README_CN.md>`_ 使能 ``Component config`` > ``ESP Wi-Fi Mesh Lite`` > ``Enable Mesh-Lite`` > ``Mesh-Lite info configuration`` > ``[*] Join Mesh no matter whether the node is connected to router`` 配置选项来测试。
  - 对于无路由器的方案需要注意如下：

    - 尽量确定一个根节点，可通过 ``esp_mesh_lite_set_allow_level(1)`` 设置。
    - 对于其他节点，建议使用 ``esp_mesh_lite_set_disallow_level(1)`` 函数来禁止它们成为根节点。
    - Mesh-Lite 的应用场景下，建立 Mesh 网络需要依靠设备物理距离和 Wi-Fi 信号质量等因素，因此需要进行充分的实地测试和调试，以保证 Mesh 网络的性能和稳定性。

----------------

ESP-WIFI-MESH 已经组网时，根节点或子节点可以同时开启 Wi-Fi Scan 扫描周围可用的 AP 信息吗？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ESP-WIFI-MESH 已经组网时，任何节点设备都不支持开启 Wi-Fi Scan 功能。

----------------

使用 ESP-WIFI-MESH Router 解决方案时，如何切换新的路由器进行组网？
-----------------------------------------------------------------------------------------------------------------------------------

  - 可以在 ``MESH_EVENT_PARENT_DISCONNECTED`` 事件后，修改如下代码：

    .. code:: text

            mesh_router_t change_router = {
                .ssid = "TP-LINK_CSW",
                .password = "12345678",
                .ssid_len = strlen("TP-LINK_CSW"),
            };
            esp_mesh_set_self_organized(false, false);
            esp_mesh_set_router(&change_router);
            esp_mesh_set_self_organized(true, true);
