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
  - 如要求更高速率，可以通过 `esp_wifi_config_espnow_rate <https://docs.espressif.com/projects/esp-idf/zh_CN/v4.4.2/esp32/api-reference/network/esp_now.html#_CPPv427esp_wifi_config_espnow_rate16wifi_interface_t15wifi_phy_rate_t>`_ 进行配置。

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

如何设置 ESP-NOW 数据的发送速率？
------------------------------------------------------------------------------

  使用 `esp_wifi_config_espnow_rate() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_now.html#_CPPv427esp_wifi_config_espnow_rate16wifi_interface_t15wifi_phy_rate_t>`_ 函数进行配置即可，例如 ``esp_wifi_config_espnow_rate(WIFI_IF_STA, WIFI_PHY_RATE_MCS0_LGI)``。

-----------------

ESP-NOW 配对限制最多 20 个设备，是否有办法控制更多的设备？
------------------------------------------------------------------------------------------

  使用广播包进行控制即可，目的地址包含在 payload 中，不受配对数量限制。仅需配置正确的广播地址即可。

-----------------

ESP-NOW 最多可以控制多少个设备？
------------------------------------------------------------------------------------------

  这取决于具体的通信方式：

  - 如使用单播包，支持同时最多配对并控制 20 个设备。
  - 如使用 ESP-NOW 加密模式，支持同时最多配对并控制 6 个设备。
  - 如使用广播包，仅需配置正确的广播地址即可。控制设备的数量理论上没有上限，但需考虑设备过多时的干扰问题。

-----------------

ESP-NOW 设备间通信需要连接路由器吗？
------------------------------------------------------------------------------------------

  ESP-NOW 的交互方式为直接从设备到设备进行通信，不需要通过路由器来转发数据。

-----------------

为什么将 ESP-NOW 每笔包的最大数据长度限制为 250 字节，这个数值可以修改吗？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 最长长度目前不能修改。因为 ESP-NOW 使用动作帧中的供应商特定元素字段传输数据，802.11 协议规定一个供应商特定元素中的``长度``字段只有 1 个字节 (0xff = 255)，因此限制了正文部分 ESP-NOW 数据长度，最长为 250 字节。
  - 或者您可以使用 API ``esp_wifi_80211_tx()`` 发送数据，使用 sniffer 模式接收数据。这样同样可以实现只工作在 Wi-Fi 层并且不使用 TCP/IP 协议栈。

--------------

使用 ESP-NOW 应用时，需要注意什么？
---------------------------------------------------------------------------------------------------------

  - 连接 Wi-Fi 以后不能再切换信道，只能在当前 Wi-Fi 信道收发数据。
  - 如果设备进入 Modem-sleep 模式，将无法接受来自 ESP-NOW 的数据。

---------------

使用 ESP-NOW 方案时，如何降低功耗？
---------------------------------------------------------------------------------------------------------

  - 可使用如下方式来降低功耗：

    - 若使用 ESP-IDF v5.0 以下版本的 SDK，可以在未连接 AP 的时候，通过 `esp_now_set_wake_window() <https://docs.espressif.com/projects/esp-idf/en/release-v4.4/esp32/api-reference/network/esp_now.html#_CPPv423esp_now_set_wake_window8uint16_t>`__ 和 `esp_wifi_set_connectionless_wake_interval() <https://docs.espressif.com/projects/esp-idf/en/v4.4.4/esp32/api-reference/network/esp_wifi.html#_CPPv441esp_wifi_set_connectionless_wake_interval8uint16_t>`__ 这两个函数设置唤醒的窗口和间隔，节省功耗。

    -  若使用 ESP-IDF v5.0 版本或者最新的 master 版本，函数名称和含义有变化，可以在连接 AP 或者在未连接 AP 的时候，使用 `esp_now_set_wake_window() <https://docs.espressif.com/projects/esp-idf/en/release-v5.0/esp32/api-reference/network/esp_now.html#_CPPv423esp_now_set_wake_window8uint16_t>`__ 和 `esp_wifi_connectionless_module_set_wake_interval() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv448esp_wifi_connectionless_module_set_wake_interval8uint16_t>`__ 这两个函数来设置醒来的窗口和间隔。

  - 注意，需要在应用层设计时考虑发送端和接收端窗口同步的问题。芯片会在每个间隔醒来并工作设置好的窗口时间。此时，还需额外在 sdkconfig.defaults 里配置 CONFIG_ESP_WIFI_STA_DISCONNECTED_PM_ENABLE=y。

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
