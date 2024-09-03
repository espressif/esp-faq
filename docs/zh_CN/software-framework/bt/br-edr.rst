经典蓝牙
========

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

ESP32 能否使用经典蓝牙进行 OTA？
----------------------------------

  可以使用经典蓝牙进行 OTA。请参考 `bt_spp_acceptor <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/classic_bt/bt_spp_acceptor>`_ 和 `bt_spp_initiator <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/classic_bt/bt_spp_initiator>`_ 修改。

--------------

如何使用 ESP32 蓝牙连接手机播放音乐？
-------------------------------------

  用手机通过蓝牙播放音乐，ESP32 用作 A2DP Sink。A2DP Sink Demo 只是通过手机获取 SBC 编码的数据流，若要播放出声音，需要做编解码转换，通常需要编解码器、数/模转换器、扬声器等模块。

--------------

ESP32 经典蓝牙 SPP 的传输速率能达到多少？
-----------------------------------------

  在开放环境下，双向同时收发，实测可达到 1400+ Kbps 到 1590 Kbps（此数据仅作为参考，实际情况建议客户根据应用环境实测）。

--------------

ESP32 的蓝牙是否兼容 Bluetooth® ver2.1 + EDR 协议？
---------------------------------------------------------------------

  兼容。ESP32 的蓝牙是向下兼容的，您可以使用官方的 `蓝牙示例 <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth>`_ 进行测试。

--------------

ESP32 的经典蓝牙工作电流是多少？
---------------------------------------

  A2DP (Single core CPU 160 Mhz，DFS = false，commit a7a90f)

  +--------------------------------------------------------------+---------------+---------------+----------+
  | 电流                                                         | 最大值 (mA)   | 最小值 (mA)   | 平均值   |
  +==============================================================+===============+===============+==========+
  | Scanning                                                     | 106.4         | 30.8          | 37.8     |
  +--------------------------------------------------------------+---------------+---------------+----------+
  | Sniff                                                        | 107.6         | 31.1          | 32.2     |
  +--------------------------------------------------------------+---------------+---------------+----------+
  | Play Music                                                   | 123           | 90.1          | 100.4    |
  +--------------------------------------------------------------+---------------+---------------+----------+

------------

ESP32 系列如何修改经典蓝牙的发射功率？
---------------------------------------------------

  可以使用 `esp_bredr_tx_power_set() <https://github.com/espressif/esp-idf/blob/b3f7e2c8a4d354df8ef8558ea7caddc07283a57b/components/bt/include/esp32/include/esp_bt.h#L336>`__ 进行设置。

--------------

ESP32 运行 bt_spp_acceptor 例程时， IOS 设备无法扫描到 ESP32 设备是什么原因？
-----------------------------------------------------------------------------

  - 苹果开放的蓝牙有：A2DP、HID 的 keyboard、avrcp 以及 SPP（需要 MFI）和高端的 Bluetooth® LE 外加给予 Bluetooth LE 的 ANCS。
  - 如果 IOS 设备想要和对端设备通过 SPP 通信，那么对端设备的 SPP 需要通过 MFI 认证。目前 ESP32 SPP 没有通过 MFI 认证，因此 IOS 设备无法扫描到 ESP32。

----------------

ESP32 如何通过 Bluetooth® BR/EDR 传文件？
------------------------------------------------------------

  - 可参考链接 `classic bt <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/classic_bt>`_ 下的 ``bt_spp_acceptor`` 或者 ``bt_spp_initiator`` 例程。

----------------

ESP32 经典蓝牙支持哪些 Profile？
------------------------------------------------------------

  - 目前支持 A2DP、AVRCP、SPP、HFP、HID。

----------------

ESP32 经典蓝牙配对时如何使手机端输入 PIN 码？
--------------------------------------------------------------------------------------

  可以通过禁用 ``Secure Simple Pairing``，从而仅支持 ``Legacy Pairing``。

  - v3.3 到 v4.0（不包含 v4.0）：``Component config`` > ``Bluetooth`` > ``Bluedroid Enable`` > ``[*] Classic Bluetooth`` > ``[ ]Secure Simple Pairing``
  - v4.0 及以上：``Component config`` > ``Bluetooth`` > ``Bluedroid Options`` > ``[ ] Secure Simple Pairing``

-----------------

ESP32 经典蓝牙的 MTU Size 最大可设多大呢？
--------------------------------------------------------------------------------

  - ESP32 经典蓝牙有两种协议，分别为 A2DP 和 SPP 协议。BT A2DP 的 MTU Size 最大设置（默认）为 1008 字节，其中包头占 12 字节，应用层实际传输的数据量即为 1008 - 12 = 996（字节）；BT SPP 的 MTU Size 最大（默认）设置为 990 字节。 

--------------

ESP32 是否支持 A2DP 发送音频？
--------------------------------------

  ESP32 支持 A2DP 发送音频，可参考例程 `a2dp_source <https://github.com/espressif/esp-idf/tree/d85d3d969ff4b42e2616fd40973d637ff337fae6/examples/bluetooth/bluedroid/classic_bt/a2dp_source>`_。

----------------

ESP32 经典蓝牙支持 AVRCP 1.5 或 AVRCP 1.6 吗？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  目前已经在 esp-idf v5.0.4 及之后的版本上支持 AVRCP 1.5，不支持 AVRCP 1.6（已废弃），详情参见 `esp-idf/components/bt/host/bluedroid/stack/avrc/avrc_sdp.c <https://github.com/espressif/esp-idf/blob/8fbf4ba6058bcf736317d8a7aa75d0578563c38b/components/bt/host/bluedroid/stack/avrc/avrc_sdp.c#L55C35-L55C40>`__。
