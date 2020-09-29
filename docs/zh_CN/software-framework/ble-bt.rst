蓝牙
====

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

移植例程 gatt\_server 出现头文件不存在的错误 ？
-----------------------------------------------

  移植例程 gatt\_server 出现错误提示 ``fatal error: esp_gap_ble_api.h: No such file or directory``，但头文件已经包含此文件。

  - 检查 sdkconfig，是否未从例程中移植 sdkconfig.defaults。通常 SDK 中蓝牙默认关闭不编译，需要配置开启。
  - 如果使用 cmake 需要将例程中 CMakeLists.txt 文件内的链接配置一同复制。

--------------

ESP32 可以支持 Bluetooth® LE 5.0 吗？
-------------------------------------

  ESP32 硬件不支持 Bluetooth® LE 5.0，支持 Bluetooth® LE 4.2。

  ESP32 目前通过了 Bluetooth® LE 5.0 的认证，但 Bluetooth® LE 5.0 的新功能 ESP32 不支持（未来会有其它芯片支持 Bluetooth® LE 5.0 全部新功能）。

--------------

为什么 Bluetooth® LE 开始广播后，有些手机扫描不到？
------------------------------------------------------------

  - 需确认手机是否支持 Bluetooth® LE 功能：有的手机在“设置” -> “蓝牙”中只显示默认的经典蓝牙，Bluetooth® LE 广播会被手机过滤掉。
  - 建议使用专用的 Bluetooth® LE App 来调试 Bluetooth® LE 功能。例如，苹果手机可以使用 LightBlue App。
  - 需确认广播包的格式符合规范，手机一般会对不符合格式的广播包进行过滤，只有格式正确的才能被显示出来。

--------------

ESP32 能否使用蓝牙进行 OTA？
----------------------------

  可以使用蓝牙进行 OTA。如果是用 Bluetooth®，可以基于 `bt\_spp\_acceptor <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/classic_bt/bt_spp_acceptor>`_ 和 `bt\_spp\_initiator <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/classic_bt/bt_spp_initiator>`_ 修改；如果是用 Bluetooth® LE，可以基于 `ble\_spp\_server <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/ble/ble_spp_server>`_ 和 `ble\_spp\_client <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/ble/ble_spp_client>`_ 修改。

--------------

ESP32 的蓝牙双模如何共存及使用？
--------------------------------

  ESP32 支持的双模蓝牙并没有特殊的地方，不需要做复杂的配置或调用即可使用。从开发者的⻆度来看，Bluetooth® LE 调用 Bluetooth® LE 的 API，经典蓝牙调用经典蓝牙的 API。

  经典蓝牙与 Bluetooth® LE 共存说明可参考文档 `ESP32 Bluetooth® & Bluetooth® LE 双模蓝牙共存说明 <https://www.espressif.com/sites/default/files/documentation/btble_coexistence_demo_cn.pdf>`_。

--------------

ESP32 的 Bluetooth® LE 吞吐量是多少？
-------------------------------------

  ESP32 的 Bluetooth® LE 吞吐率取决于各种因素，例如环境干扰、连接间隔、MTU 大小以及对端设备性能等等。ESP32 板子之间的 Bluetooth® LE 通信最大吞吐量可达 700 Kbps，约 90 KB/s，具体可以参考 IDF 中的 ble\_throughput example。

--------------

ESP32 是否支持 BT4.2 DLE (Data Length Extension)？
----------------------------------------------------

  支持。ESP-IDF 所有版本都支持 BT 4.2 DLE，暂无对应的 sample code，可直接调相关接口实现，参见：`esp\_ble\_gap\_set\_pkt\_data\_len <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/esp_gap_ble.html?highlight=esp_ble_gap_set_pkt_data_len#_CPPv428esp_ble_gap_set_pkt_data_len13esp_bd_addr_t8uint16_t>`_。

--------------

ESP32 的蓝⽛和 Wi-Fi 如何共存？
-------------------------------

  在 menuconfig 中，有个特殊选项 “Software controls WiFi/Bluetooth coexistence”，⽤于通过软件来控制 ESP32 的蓝⽛和 Wi-Fi 共存，可以平衡 Wi-Fi、蓝⽛控制 RF 的共存需求。

  请注意，如果使能 ``Software controls WiFi/Bluetooth coexistence`` 选项，Bluetooth® LE scan 间隔不应超过 ``0x100 slots`` （约 160 ms）。若只是 Bluetooth® LE 与 Wi-Fi 共存，则开启这个选项和不开启均可正常使⽤。但不开启的时候需要注意 “BLE scan interval - BLE scan window > 150 ms”, 并且 Bluetooth® LE scan interval 尽量⼩于 500 ms。 若经典蓝⽛与 Wi-Fi 共存，则建议开启这个选项。

--------------

ESP32 蓝牙的兼容性测试报告如何获取？
------------------------------------

  请联系 sales@espressif.com 获得兼容性测试报告。

--------------

ESP32 蓝牙的发射功率是多少？
----------------------------

  ESP32 蓝牙的发射功率有 9 档，对应功率 -12 ~ 12 dBm，间隔 3 dBm 一档。控制器软件对发射功率进行限制，根据产品声明的对应功率等级选取档位。

--------------

ESP32 可以实现 Wi-Fi 和 Bluetooth® LE 桥接的功能吗？
--------------------------------------------------------------------

  可以实现，这个属于应⽤层开发：可以通过 Bluetooth® LE 获取数据，由 Wi-Fi 转出去。可参考 `Wi-Fi 和蓝⽛共存的 demo <https://github.com/espressif/esp-idf/tree/release/v4.0/examples/bluetooth/esp_ble_mesh/ble_mesh_wifi_coexist>`_，修改为⾃⼰的应⽤即可。

--------------

ESP32 的 Bluetooth® LE 工作电流是多少？
------------------------------------------------

+--------------------------------------------------------------+---------------+---------------+----------+
| 电流                                                         | 最大值 (mA)   | 最小值 (mA)   | 平均值   |
+==============================================================+===============+===============+==========+
| Advertising: Adv Interval = 40ms                             | 142.1         | 32            | 42.67    |
+--------------------------------------------------------------+---------------+---------------+----------+
| Scanning: Scan Interval = 160ms,Window = 20ms                | 142.1         | 32            | 44.4     |
+--------------------------------------------------------------+---------------+---------------+----------+
| Connection(Slave): Connection Interval = 20ms, Iatency = 0   | 142.1         | 32            | 42.75    |
+--------------------------------------------------------------+---------------+---------------+----------+
| Connection(Slave): Connection Interval = 80ms, Iatency = 0   | 142.1         | 32            | 35.33    |
+--------------------------------------------------------------+---------------+---------------+----------+

--------------

ESP32 支持哪些 Bluetooth® LE Profile？
---------------------------------------

  目前支持完整的 GATT/SMP 等基础模块，支持自定义配置；已经实现的配置有 Bluetooth® LE HID（设备端）、电池、DIS、Blu-Fi（蓝牙配网）等。

--------------

如何使用 ESP32 蓝牙连接手机播放音乐？
-------------------------------------

  用手机通过蓝牙播放音乐，ESP32 用作 A2DP Sink。A2DP Sink Demo 只是通过手机获取 SBC 编码的数据流，若要播放出声音，需要做编解码转换，通常需要编解码器、数/模转换器、扬声器等模块。

--------------

ESP32 的 SPP 性能如何？
-----------------------

  使用两块 ESP32 开发板对跑 SPP，单向吞吐量量可达 1900 Kbps，约 235 KB/s，已接近规范里的理论值。

--------------

ESP32 的 Bluetooth® LE 传输速率最大为多少？
-----------------------------------------------------

  屏蔽箱测试 Bluetooth® LE 传输速率可以达到 800 kbits/s。

--------------

ESP32 Bluetooth® LE 如何进入 light sleep 模式呢？
---------------------------------------------------------

  硬件上需要外加 32 Khz 的外部晶振，否则 light sleep 模式不会生效。

  软件上（SDK4.0 以及以上版本才会支持）在 menuconfig 中需要使能以下配置：

  - | Enable Power Management :| menuconfig ---> Component config ---> Power management --->[\*] Support for power management

  - | Enable Tickless Idle :| menuconfig ---> Component config ---> FreeRTOS --->[\*] Tickless idle support (3) Minimum number of ticks to enter sleep mode for (NEW)

    Note : Tickless idle needs to be enabled to allow automatic light sleep . FreeRTOS will enter light sleep if no tasks need to run for 3 (by default) ticks , that is 30ms if tick rate is 100Hz . Configure the FreeRTOS tick rate to be higher if you want to allow shorter duration light sleep , for example : menuconfig ---> Component config ---> FreeRTOS ->(1000) Tick rate (Hz)

  - | Configure external 32.768Hz crystal as RTC clock source :| menuconfig ---> Component config ---> ESP32-specific --->RTC clock source (External 32kHz crystal)[\*] Additional current for external 32kHz crystal

   | Note : that the " additional current " option is a workaround for a hardware issue on ESP32 that the crystal can fail in oscillating. Please enable this option when you use external 32kHz crystal . This hardware issue will be resolved in the next ECO chip .

  - | Enable Bluetooth modem sleep with external 32.768kHz crystal as low power clock :| menuconfig ---> Component config ---> Bluetooth ---> Bluetooth controller ---> MODEM SLEEP Options --->[\*] Bluetooth modem sleep

--------------

选择 ESP32 芯片实现蓝牙配网的方式，是否有文档可以提供参考？
-----------------------------------------------------------

  蓝牙配网说明可参考 `ESP32 blufi <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/blufi.html?highlight=blufi>`_。蓝牙配网示例可以参考 `blufi <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/ble/blufi>`_。

--------------

ESP32 经典蓝牙 SPP 的传输速率能达到多少？
-----------------------------------------

  在开放环境下，双向同时收发，实测可达到 1400+ ～ 1590 kbit/s（此数据仅作为参考，实际情况建议客户根据应用环境实测）。

--------------

ESP32 的蓝牙是否兼容 Bluetooth® ver2.1 + EDR 协议？
---------------------------------------------------------------------

  兼容。ESP32 的蓝牙是向下兼容的，您可以使用官方的 `蓝牙示例 <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth>`_ 进行测试。

--------------

ESP32 支持多少蓝牙客户端连接？
------------------------------

  Bluetooth® LE Server 最大支持 9 个客户端连接，应用中需查看配置参数 ble\_max\_conn。测试稳定连接为 3 个客户端。

--------------

ESP32 如何获取 蓝牙设备的 MAC 地址？
------------------------------------

  可调用 `esp\_bt\_dev\_get\_address(void); <https://github.com/espressif/esp-idf/blob/f1b8723996d299f40d28a34c458cf55a374384e1/components/bt/host/bluedroid/api/include/api/esp_bt_device.h#L33>`_ API 来获取蓝牙配置的 MAC 地址。也可以调用 `esp\_err\_t esp\_read\_mac(uint8\_t\* mac,esp\_mac\_type\_ttype); <https://github.com/espressif/esp-idf/blob/6c17e3a64c02eff3a4f726ce4b7248ce11810833/components/esp_system/include/esp_system.h#L233>`_ API 获取系统预设的分类 MAC 地址。

--------------

ESP32 是否有修复 `Sweyntooth Bluetooth® LE vulnerability <https://asset-group.github.io/disclosures/sweyntooth/>`_ 呢？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ESP32 已修复。 

  - 对于 "Invalid Channel Map"问题，请参考提交：https://github.com/espressif/esp-idf/commit/49d69bb235b7a5e558d24a101f77533e97992377；

  - 对于 "HCI Desync" 问题，它仅影响 NimBLE 主机，不影响 Bluedroid 主机，请参考提交：https://github.com/espressif/esp-idf/commit/4cd6f094278e81b436a3f71fc11b80ebed25cf98。

--------------

ESP32 如何获取蓝牙 MAC 地址？
------------------------------------

  - 可以通过下面示例 API 读取芯片默认的 MAC 地址。

  .. code-block:: text

    esp_err_t esp_read_mac(uint8_t* mac, esp_mac_type_t type);

--------------

ESP32 SDK 中默认的蓝牙的发射功率是多少？
-------------------------------------------------

  - ESP32 SDK 中默认情况下使用功率级别 4 ，相应的发射功率为 0 dBm。
  - ESP32 蓝牙的发射功率从 0 到 7，共有 8 个功率级别，发射功率范围从 –12 dBm 到 9 dBm。功率电平每增加 1 时，发射功率增加 3 dB。

--------------

ESP32 Wi-Fi Smartconfig 配网和 BLE Mesh 可以同时使用吗？
-------------------------------------------------------------------

  不推荐同时打开。
  
  - Smartconfig 需要一直收配网数据，所以会一直占用天线，如果和 BLE Mesh 共同使用，会导致失败率非常高。

  - BLE Mesh 可以和 Blufi 同时使用，所以推荐配网方式选择 Blufi 配网。

--------------

ESP32 的经典蓝牙工作电流是多少？
---------------------------------------

  A2DP( Single core CPU 160 Mhz，DFS = false，commit a7a90f)

+--------------------------------------------------------------+---------------+---------------+----------+
| 电流                                                         | 最大值 (mA)   | 最小值 (mA)   | 平均值   |
+==============================================================+===============+===============+==========+
| Scanning                                                     | 106.4         | 30.8          | 37.8     |
+--------------------------------------------------------------+---------------+---------------+----------+
| Sniff                                                        | 107.6         | 31.1          | 32.2     |
+--------------------------------------------------------------+---------------+---------------+----------+
| Play Music                                                   | 123           | 90.1          | 100.4    |
+--------------------------------------------------------------+---------------+---------------+----------+

--------------

ESP32 的 BLE 蓝牙配网兼容性如何？是否开源？
---------------------------------------------

  - ESP32 的蓝牙配网，简称 Blu-Fi 配网，兼容性与 BLE 兼容性一致，测试过苹果、华为、小米、OPPO、魅族、 一加、中兴等主流品手机，兼容性良好。
  - 目前 Blu-Fi 协议及手机应用部分的代码不开源。

--------------

ESP32 运行 bt_spp_acceptor 例程时， IOS 设备无法扫描到 ESP32 设备是什么原因？
-----------------------------------------------------------------------------

  - 苹果开放的蓝牙有： A2DP、HID 的 keyboard、avrcp 以及 SPP(需要 MFI) 和高端的 BLE 外加给予 BLE 的 ANCS。
  - 如果 IOS 设备想要和 对端设备通过 SPP 通信，那么对端设备的 SPP 需要通过 MFI 认证。
    目前 ESP32 SPP 没有通过 MFI 认证，因此 IOS 设备无法扫描到 ESP32。

--------------

ESP32 BLE/BT Secure Simple Pairing (SSP) 与 legacy pairing 安全性对比 ？
----------------------------------------------------------------------------

  - Secure Simple Pairing (SSP) 比 legacy pairing 更加安全。
  - legacy pairing 使用对称加密算法， Secure Simple Pairing (SSP) 使用的是非对称加密算法。
