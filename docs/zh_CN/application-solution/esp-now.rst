ESP-NOW
=======

:link_to_translation:`en:[English]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

----------

ESP32 ESP-Now 模式下一对一的通信速率是多少？
---------------------------------------------

  测试数据如下：

  - 测试样板：`ESP32-DevKitC V4 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/hw-reference/esp32/get-started-devkitc.html>`__。
  - Wi-Fi 模式：station 模式。
  - 物理层速率默认为 1 Mbps。
  - open 环境下大约是 214 Kbps。
  - 屏蔽箱内测试大约是 555 Kbps。
  - 如要求更高速率，可通过配置发送速率实现。具体方法请参考下文 :ref:`如何设置 ESP-NOW 数据的发送速率？ <esp-now-set-tx-rate>`。

--------------

ESP-NOW 是什么？它有哪些优势与适用场景？
-----------------------------------------------------------

  - `ESP-NOW <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/network/esp_now.html>`_ 是由乐鑫定义的无连接通信协议。
  - 在 ESP-NOW 中，应用程序数据被封装在各个供应商的动作帧中，在无连接的情况下，从一个 Wi-Fi 设备传输到另一个 Wi-Fi 设备。
  - ESP-NOW 广泛应用于智能照明、远程控制、传感器等领域。

--------------

ESP-NOW 是否可以与 Wi-Fi 一起使用？
----------------------------------------------------------------------------------------------------------------------------------------------------

  - 可以，但需要注意的是 ESP-NOW 的信道要和所连接的 AP 的信道相同。

--------------------

.. _esp-now-set-tx-rate:

如何设置 ESP-NOW 数据的发送速率？
------------------------------------------------------------------------------

  推荐使用 `esp_now_set_peer_rate_config() <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/network/esp_now.html>`__ 按配对设备分别配置发送速率，支持所有速率（含 Wi-Fi 6 HE 速率）。该接口需在 ``esp_wifi_start()``、``esp_now_init()`` 且通过 ``esp_now_add_peer()`` 添加配对设备之后调用。

  .. note::

     - ESP-IDF v5.2 之前：请使用旧接口 ``esp_wifi_config_espnow_rate()`` （例如 ``esp_wifi_config_espnow_rate(WIFI_IF_STA, WIFI_PHY_RATE_MCS0_LGI)``，仅支持非 HE 速率）。
     - ESP-IDF v5.2 至 v5.x：新增 ``esp_now_set_peer_rate_config()``，两个接口均可使用（旧接口已标记为 deprecated），无需强制迁移。
     - ESP-IDF v6.0 及以上：``esp_wifi_config_espnow_rate()`` 已移除，必须改用 ``esp_now_set_peer_rate_config()``。

-----------------

ESP-NOW 配对限制最多 20 个设备，是否有办法控制更多的设备？
------------------------------------------------------------------------------------------

  使用广播包进行控制即可，目的地址包含在 payload 中，不受配对数量限制。仅需配置正确的广播地址即可。

-----------------

.. _esp-now-max-control-devices:

ESP-NOW 最多可以控制多少个设备？
------------------------------------------------------------------------------------------

  以下限制针对 ESP-IDF 协议层 (``esp_now``)，取决于具体的通信方式：

  - 如使用单播包，支持同时最多配对并控制 20 个设备 (``ESP_NOW_MAX_TOTAL_PEER_NUM``)。
  - 如使用 ESP-NOW 加密模式，加密设备数量上限与 ESP-IDF 版本有关：

    - ESP-IDF v5.1 之前：固定为 6 个，不可修改。
    - ESP-IDF v5.1 及以上：可配置，默认 7 个、最多 17 个（ESP32-C2 为默认 2 个、最多 4 个），可通过 Wi-Fi menuconfig 的 ``CONFIG_ESP_WIFI_ESPNOW_MAX_ENCRYPT_NUM`` 修改。

  - 如使用广播包，仅需配置正确的广播地址即可。控制设备的数量理论上没有上限，但需考虑设备过多时的干扰问题。

  如使用 `esp-now 组件 <https://github.com/espressif/esp-now>`__ （应用级封装）：其控制采用广播 + 群组 (group) + 绑定表 (bindlist) 模型，控制指令以广播下发，被控设备数量不受协议层 20 个配对设备的限制（实际数量受广播干扰等因素影响）；组件采用应用层加密，也不受协议层加密配对设备数量上限 (6/17) 的限制。

-----------------

ESP-NOW 设备间通信需要连接路由器吗？
------------------------------------------------------------------------------------------

  ESP-NOW 的交互方式为直接从设备到设备进行通信，不需要通过路由器来转发数据。

-----------------

ESP-NOW 单包最大数据长度是多少？可以修改吗？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 以下为 ESP-IDF 协议层 (``esp_now``) 的限制。ESP-NOW 目前支持两个版本，单包最大数据长度不同：

    - v1.0：最大 250 字节 (``ESP_NOW_MAX_DATA_LEN``)。受限于 802.11 协议中一个供应商特定元素的 ``长度`` 字段只有 1 个字节 (0xff = 255)，因此单个元素的正文最长为 250 字节。
    - v2.0：最大 1470 字节 (``ESP_NOW_MAX_DATA_LEN_V2``)，通过在动作帧中拼接多个供应商特定元素实现。

  - 各 ESP-IDF 版本支持的最大长度：

    - v5.4 之前：仅支持 v1.0，单包最大 250 字节。
    - v5.4 及以上：支持 v2.0，单包最大 1470 字节（早期的 v5.4、v5.4.1 为 1490 字节，自 v5.4.2 起修正为 1470 字节），并向下兼容 v1.0（250 字节）。

  - 上述长度上限由协议版本决定，不能由用户任意修改。如需绕过该封装，可使用 API ``esp_wifi_80211_tx()`` 发送数据，并用 sniffer 模式接收数据，同样可只工作在 Wi-Fi 层且不使用 TCP/IP 协议栈。
  - 若使用 `esp-now 组件 <https://github.com/espressif/esp-now>`__ （应用级封装）：

    - 单帧可用 payload 为 ``ESPNOW_PAYLOAD_LEN``，即协议层单包最大长度减去组件包头（20 字节， ``sizeof(espnow_data_t)``）：支持 v2.0 的 IDF 为 1450 字节（早期 v5.4、v5.4.1 为 1470 字节），v5.4 之前为 230 字节。
    - 启用应用层加密后还会再占用 TAG(4) + IV(8) 共 12 字节，单包可用长度为 ``ESPNOW_SEC_PACKET_MAX_SIZE`` （即 ``ESPNOW_PAYLOAD_LEN`` − 12，例如 v5.5 为 1438 字节）。
    - 组件还支持分片传输，可用于 OTA、日志回传等大数据场景。

--------------

ESP-NOW v1.0 与 v2.0 有什么区别？两者可以混用吗？
----------------------------------------------------------------------------------------------------------

  - 主要区别在于单包最大数据长度：v1.0 为 250 字节 (``ESP_NOW_MAX_DATA_LEN``)，v2.0 为 1470 字节 (``ESP_NOW_MAX_DATA_LEN_V2``)。可调用 ``esp_now_get_version()`` 查询当前设备的 ESP-NOW 版本。
  - 兼容性说明：

    - v2.0 设备可以接收来自 v2.0 和 v1.0 设备的数据包。
    - v1.0 设备可以接收来自 v1.0 设备的数据包；对于长度不超过 250 字节 (``ESP_NOW_MAX_IE_DATA_LEN``) 的 v2.0 数据包仍可接收，超过 250 字节时则只保留前 250 字节或整包丢弃。

  - 因此，在 v1.0 与 v2.0 设备混用的网络中，建议发送端将单包长度控制在 250 字节以内以保证互通。更多信息请参考 `ESP-NOW 文档 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/network/esp_now.html>`__。

--------------

使用 ESP-NOW 应用时，需要注意什么？
---------------------------------------------------------------------------------------------------------

  - 连接 Wi-Fi 以后不能再切换信道，只能在当前 Wi-Fi 信道收发数据。
  - 默认情况下，设备可以正常接收 ESP-NOW 数据（ ``esp_now_set_wake_window()`` 的唤醒窗口默认为最大值，射频保持常开）。仅当主动配置较小的唤醒窗口使设备周期性休眠时，窗口之外发来的数据将无法收到，需在应用层做收发窗口同步。唤醒窗口配置在已连接 AP 时即可生效；未连接 AP 时需额外使能 ``CONFIG_ESP_WIFI_STA_DISCONNECTED_PM_ENABLE`` 才生效（详见下方降低功耗相关问题）。

---------------

使用 ESP-NOW 方案时，如何降低功耗？
---------------------------------------------------------------------------------------------------------

  - 可使用如下方式来降低功耗：

    - 若使用 ESP-IDF v5.0 以下版本的 SDK，可以在未连接 AP 时，通过 `esp_now_set_wake_window() <https://docs.espressif.com/projects/esp-idf/en/release-v4.4/esp32/api-reference/network/esp_now.html#_CPPv423esp_now_set_wake_window8uint16_t>`__ 和 `esp_wifi_set_connectionless_wake_interval() <https://docs.espressif.com/projects/esp-idf/en/v4.4.4/esp32/api-reference/network/esp_wifi.html#_CPPv441esp_wifi_set_connectionless_wake_interval8uint16_t>`__ 这两个函数设置唤醒窗口和间隔，节省功耗。

    - 若使用 ESP-IDF v5.0 及以上版本，函数名称和含义有变化，可以在连接 AP 或未连接 AP 时，使用 `esp_now_set_wake_window() <https://docs.espressif.com/projects/esp-idf/en/release-v5.0/esp32/api-reference/network/esp_now.html#_CPPv423esp_now_set_wake_window8uint16_t>`__ 和 `esp_wifi_connectionless_module_set_wake_interval() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv448esp_wifi_connectionless_module_set_wake_interval8uint16_t>`__ 这两个函数来设置唤醒窗口和间隔。

  - 注意，需要在应用层设计时考虑发送端和接收端窗口同步的问题。芯片会在每个间隔醒来并工作设置好的窗口时间。此时，还需额外在 ``sdkconfig.defaults`` 里配置 ``CONFIG_ESP_WIFI_STA_DISCONNECTED_PM_ENABLE=y``。

-----------------

一对多，多对多通信除了 ESP-NOW 的设备无线通信方式，还有其他更好的方式吗？
---------------------------------------------------------------------------------------------------------------------------------------

  也可以使用 SoftAP + Station 的方式实现。主设备使用 Wi-Fi SoftAP 模式，同时与多个从设备（Wi-Fi Station）建立连接。

-----------------

ESP-NOW 应用是否支持通过每个 Wi-Fi 信道发送数据包？
---------------------------------------------------------------------------------------------------------------------------------------

  支持，请参考 `ESP-NOW 文档 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/network/esp_now.html>`__。

-----------------

将 ESP-NOW 技术用于商业用途是否需要任何特殊程序？可以提供关于 ESP-NOW 技术的详细技术文档吗？为了评估无线通信质量，我想了解以下内容，例如 CSMA/CA、调制方式、比特率等。
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP-NOW 申请不需要任何特殊程序。
  - 技术文档请阅读 `ESP-NOW 用户指南 <https://www.espressif.com/sites/default/files/documentation/esp-now_user_guide_cn.pdf>`__，您可以使用 `ESP-NOW SDK <https://github.com/espressif/esp-now>`__ 示例进行测试。
  - 默认的 ESP-NOW 比特率是 1 Mbps。

-----------------

为什么使用 ESP32 测试 `esp-idf/examples/wifi/espnow <https://github.com/espressif/esp-idf/tree/master/examples/wifi/espnow>`__ 例程，最多仅支持连接 7 个加密设备？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 该现象与 ESP-IDF 版本有关：

    - ESP-IDF v5.1 及以上：ESP32 加密设备数量默认为 7 个、最多 17 个，可通过 Wi-Fi menuconfig 的 ``CONFIG_ESP_WIFI_ESPNOW_MAX_ENCRYPT_NUM`` 修改。
    - ESP-IDF v5.1 之前：固定为 6 个，不可修改。

  - 详见上文 :ref:`ESP-NOW 最多可以控制多少个设备？ <esp-now-max-control-devices>`，以及 `添加配对设备 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/network/esp_now.html>`__ 说明。

-----------

使用 ESP-NOW 传输数据，如何获取对应的 RSSI？
---------------------------------------------------------------------------------------------------------------------------

  - 以下为 ESP-IDF 协议层 (``esp_now``) 的获取方式，与 ESP-IDF 版本有关（接收回调 ``esp_now_recv_cb_t`` 的签名在 v5.1 发生了变化）：

    - ESP-IDF v5.1 之前：回调仅提供 ``mac_addr`` / ``data`` / ``data_len``，不含 ``rx_ctrl``，无法在回调内获取 RSSI。如需在旧版本获取，只能用混杂 (sniffer) 模式抓取同信道 802.11 帧的 ``rx_ctrl.rssi``，并自行按源 MAC 与 ESP-NOW 数据包关联。建议升级到 v5.1 及以上，以便直接从回调获取。
    - ESP-IDF v5.1 及以上：回调的第一个参数为 ``esp_now_recv_info_t``，可通过其 ``rx_ctrl`` 字段（类型为 `wifi_pkt_rx_ctrl_t <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/network/esp_wifi.html#_CPPv418wifi_pkt_rx_ctrl_t>`__ ）中的 ``rssi`` 获取对应的 RSSI。

  - 若使用 `esp-now 组件 <https://github.com/espressif/esp-now>`__，则无需自行处理上述版本差异：组件的数据接收回调（通过 ``espnow_set_config_for_data_type()`` 注册的 ``handler_for_data_t``）直接提供 ``wifi_pkt_rx_ctrl_t *rx_ctrl`` 参数，读取 ``rx_ctrl->rssi`` 即可。

-------------

如何在 ESP-NOW 中使用 RSSI 实现选择性范围控制？
--------------------------------------------------------------------------------------------------------------

  可以通过修改 `espnow_ctrl.c 中的 g_initiator_frame <https://github.com/espressif/esp-now/blob/master/src/control/src/espnow_ctrl.c>`__ 的 ``.forward_ttl`` 和 ``.forward_rssi`` 参数来实现。对应参数说明参见 `esp-now/src/espnow/include/espnow.h <https://github.com/espressif/esp-now/blob/master/src/espnow/include/espnow.h>`__ 中的 ``espnow_frame_head_t``。
