低功耗蓝牙
===========

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

移植例程 gatt_server 出现头文件不存在的错误？
-----------------------------------------------

  移植例程 gatt_server 出现错误提示 ``fatal error: esp_gap_ble_api.h: No such file or directory``，但头文件已经包含此文件。

  - 检查 sdkconfig，是否未从例程中移植 sdkconfig.defaults。通常 SDK 中蓝牙默认关闭不编译，需要配置开启。
  - 如果使用 cmake 需要将例程中 CMakeLists.txt 文件内的链接配置一同复制。

--------------

ESP32 可以支持 Bluetooth LE 5.0 吗？
---------------------------------------------

  ESP32 硬件不支持 Bluetooth LE 5.0，支持 Bluetooth LE 4.2。

  ESP32 目前通过了 Bluetooth LE 5.0 的认证，但不支持 Bluetooth LE 5.0 的新功能。如需使用 Bluetooth LE 5.0 的功能，请选择其它 ESP32 系列芯片。

--------------

为什么 Bluetooth® LE 开始广播后，有些手机扫描不到？
------------------------------------------------------------

  - 需确认手机是否支持 Bluetooth LE 功能：有的手机在“设置” -> “蓝牙”中只显示默认的经典蓝牙，Bluetooth LE 广播会被手机过滤掉。
  - 建议使用专用的 Bluetooth LE App 来调试 Bluetooth LE 功能。例如，苹果手机可以使用 LightBlue App。
  - 需确认广播包的格式符合规范，手机一般会对不符合格式的广播包进行过滤，只有格式正确的才能被显示出来。

--------------

ESP32 能否使用 Bluetooth LE 进行 OTA？
-----------------------------------------

  可以，请参考例程 `BLE_OTA <https://github.com/espressif/esp-iot-solution/tree/master/examples/bluetooth/ble_ota>`_。

--------------

ESP32 的 Bluetooth® LE 吞吐量是多少？
---------------------------------------------

  - ESP32 的 Bluetooth LE 吞吐率取决于各种因素，例如环境干扰、连接间隔、MTU 大小以及对端设备性能等等。
  - ESP32 板子之间的 Bluetooth LE 通信最大吞吐量可达 700 Kbps，约 90 KB/s，具体可以参考 ESP-IDF 中的 ble_throughput example。

--------------

ESP32 是否支持 BT4.2 DLE (Data Length Extension)？
---------------------------------------------------------

  支持。ESP-IDF 所有版本都支持 Bluetooth® 4.2 DLE，可直接调相关接口实现，参见 `esp_ble_gap_set_pkt_data_len <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/bluetooth/esp_gap_ble.html?highlight=esp_ble_gap_set_pkt_data_len#_CPPv428esp_ble_gap_set_pkt_data_len13esp_bd_addr_t8uint16_t>`_。

--------------

ESP32 蓝牙的兼容性测试报告如何获取？
------------------------------------

  请联系 sales@espressif.com 获得兼容性测试报告。

--------------

ESP32 Bluetooth LE 的发射功率是多少？
-----------------------------------------

  ESP32 Bluetooth LE的发射功率有 8 档，对应功率 -12 ~ 9 dBm，间隔 3 dBm 一档。控制器软件对发射功率进行限制，根据产品声明的对应功率等级选取档位。

--------------

ESP32 可以实现 Wi-Fi 和 Bluetooth® LE 桥接的功能吗？
--------------------------------------------------------------------

  可以实现，这个属于应⽤层开发：可以通过 Bluetooth LE 获取数据，由 Wi-Fi 转出去。可参考 `Wi-Fi 和蓝⽛共存的 demo <https://github.com/espressif/esp-idf/tree/release/v4.0/examples/bluetooth/esp_ble_mesh/ble_mesh_wifi_coexist>`_，修改为⾃⼰的应⽤即可。

--------------

ESP32 的 Bluetooth® LE 工作电流是多少？
------------------------------------------------

  +--------------------------------------------------------------+---------------+---------------+----------+
  | 电流                                                         | 最大值 (mA)   | 最小值 (mA)   | 平均值   |
  +==============================================================+===============+===============+==========+
  | Advertising: Adv Interval = 40 ms                            | 142.1         | 32            | 42.67    |
  +--------------------------------------------------------------+---------------+---------------+----------+
  | Scanning: Scan Interval = 160 ms,Window = 20 ms              | 142.1         | 32            | 44.4     |
  +--------------------------------------------------------------+---------------+---------------+----------+
  | Connection(Slave): Connection Interval = 20 ms, Iatency = 0  | 142.1         | 32            | 42.75    |
  +--------------------------------------------------------------+---------------+---------------+----------+
  | Connection(Slave): Connection Interval = 80 ms, Iatency = 0  | 142.1         | 32            | 35.33    |
  +--------------------------------------------------------------+---------------+---------------+----------+

--------------

ESP32 支持哪些 Bluetooth® LE Profile？
--------------------------------------------

  目前支持完整的 GATT/SMP 等基础模块，支持自定义配置；已经实现的配置有 Bluetooth LE HID（设备端）、电池、DIS、BluFi（蓝牙配网）等。

--------------

ESP32 的 Bluetooth® LE 传输速率最大为多少？
-----------------------------------------------------

  屏蔽箱测试 Bluetooth LE 传输速率可以达到 700 Kbps。

--------------

ESP32 Bluetooth® LE 如何进入 Light-sleep 模式呢？
---------------------------------------------------------

  硬件上需要外加 32 kHz 的外部晶振，否则 Light-sleep 模式不会生效。

  软件上（SDK4.0 以及以上版本才会支持）在 menuconfig 中需要使能以下配置：

  - Power Management:| ``menuconfig`` > ``Component config`` > ``Power management`` > ``[*] Support for power management``

  - Tickless Idle:| ``menuconfig`` > ``Component config`` > ``FreeRTOS`` > ``[*] Tickless idle support (3) Minimum number of ticks to enter sleep mode for (NEW)``

  .. note:: 需使能 "Tickless idle" 功能使 ESP32 自动进入 Light-sleep 模式。如果在 3 个节拍（默认）内无任务运行，则 FreeRTOS 将进入 Light-sleep 模式，即 100 Hz 节拍率下为 30 ms。若您希望缩短 Light-sleep 模式的持续时间，可通过将 FreeRTOS 节拍率调高来实现，如：``menuconfig`` > ``Component config`` > ``FreeRTOS`` > ``(1000) Tick rate (Hz)``。

  - | Configure external 32.768 kHz crystal as RTC clock source :| ``menuconfig`` > ``Component config`` > ``ESP32-specific`` > ``RTC clock source (External 32 kHz crystal)[*] Additional current for external 32 kHz crystal``

  .. note:: "additional current" 选项为解决 ESP32 晶振失败的替代方案。请在您使用外部 32 kHz 晶体时使能该选项。该硬件问题将在下一个芯片版本中解决。

  - | Enable Bluetooth modem sleep with external 32.768 kHz crystal as low power clock :| ``menuconfig`` > ``Component config`` > ``Bluetooth`` > ``Bluetooth controller`` > ``MODEM SLEEP Options`` > ``[*] Bluetooth modem sleep``

--------------

选择 ESP32 芯片实现蓝牙配网的方式，是否有文档可以提供参考？
-----------------------------------------------------------

  蓝牙配网说明可参考 `ESP32 Blufi <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/blufi.html?highlight=blufi>`_。蓝牙配网示例可以参考 `Blufi <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/blufi>`_。

--------------

ESP32 支持多少低功耗蓝牙客户端连接？
-------------------------------------

  Bluetooth® LE Server 最大支持 9 个客户端连接，应用中需查看配置参数 ble_max_conn。测试稳定连接为 3 个客户端。

--------------

ESP32 如何获取蓝牙设备的 MAC 地址？
------------------------------------

  可调用 `esp_bt_dev_get_address(void); <https://github.com/espressif/esp-idf/blob/f1b8723996d299f40d28a34c458cf55a374384e1/components/bt/host/bluedroid/api/include/api/esp_bt_device.h#L33>`_ API 来获取蓝牙配置的 MAC 地址。也可以调用 `esp_err_t esp_read_mac(uint8_t* mac,esp_mac_type_ttype); <https://github.com/espressif/esp-idf/blob/6c17e3a64c02eff3a4f726ce4b7248ce11810833/components/esp_system/include/esp_system.h#L233>`_ API 获取系统预设的分类 MAC 地址。

--------------


ESP32 Wi-Fi Smartconfig 配网和 Bluetooth® LE Mesh 可以同时使用吗？
-------------------------------------------------------------------

  不推荐同时打开。

  - Smartconfig 需要一直收配网数据，所以会一直占用天线，如果和 Bluetooth LE Mesh 共同使用，会导致失败率非常高。
  - Bluetooth LE Mesh 可以和 BluFi 同时使用，所以推荐配网方式选择 BluFi 配网。

------------

ESP32 系列如何修改低功耗蓝牙的发射功率？
---------------------------------------------------

  - ESP32/ESP32-S3/ESP32-C3 蓝牙发射功率可通过 `esp_ble_tx_power_set()` 函数进行设置，可参见 `esp_bt.h <https://github.com/espressif/esp-idf/blob/c77c4ccf6c43ab09fd89e7c907bf5cf2a3499e3b/components/bt/include/esp_bt.h>`_。
  - 对于ESP32-C6/ESP32-C2/ESP32-H2 可以通过调用 `esp_ble_tx_power_set_enhanced() <https://github.com/espressif/esp-idf/blob/b3f7e2c8a4d354df8ef8558ea7caddc07283a57b/components/bt/include/esp32h4/include/esp_bt.h#L139>`__ API设置发射功率。

--------------

ESP32 的 Bluetooth® LE 蓝牙配网兼容性如何？是否开源？
-----------------------------------------------------------------

  - ESP32 的蓝牙配网，简称 BluFi 配网，兼容性与 Bluetooth LE 兼容性一致，测试过苹果、华为、小米、OPPO、魅族、一加、中兴等主流品手机，兼容性良好。
  - 目前 BluFi 协议及手机应用部分的代码都已经开源。

--------------

ESP32 Bluetooth® LE/Bluetooth® Secure Simple Pairing (SSP) 与 legacy pairing 安全性对比？
----------------------------------------------------------------------------------------------------------

  - Secure Simple Pairing (SSP) 比 legacy pairing 更加安全。
  - legacy pairing 使用对称加密算法， Secure Simple Pairing (SSP) 使用的是非对称加密算法。

--------------

ESP32 Bluetooth® LE MTU 大小如何确定？
----------------------------------------

  - ESP32 端蓝牙 Bluetooth LE 默认的 MTU 为 23 字节，最大可以设置为 517 字节。
  - 手机端的 MTU 由手机端自行定义，最终通信的 MTU 选择两端 MTU 较小的那一个。

--------------

ESP32 Bluetooth® LE 能否同时支持主从模式，作 gatt server 的同时，也可作为 gatt client 接收其他设备的广播数据？
-----------------------------------------------------------------------------------------------------------------------------------

  - 支持，可参考例程 `gattc_gatts_coex <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/coex/gattc_gatts_coex>`_。

--------------

ESP32 的 Bluetooth® LE 连接数 6 个以上会有哪些风险？
---------------------------------------------------------------

  - 通常要根据具体的应用决定，在常规场景下，ESP32 Bluetooth LE 连接 3 个设备可以稳定通信。
  - Bluetooth LE 的最大连接数未有一个准确的值，在多个 Bluetooth LE 设备同时连接的的时候，RF 是分时复用的，需要设计者保证每一个设备不会长时间占用导致其他设备超时断开。
  - 连接参数里面有 connection interval、connection window、latency、timeout, 可以在 ``latency`` 以内的不应答，但是若超过 ``timeout`` 的时间，将会导致连接断开。
  - 假设配置参数中 ``interval`` 是 100，window 是 5，Wi-Fi 关闭时，将会连接较多设备。如果用了 Wi-Fi，或者 ``interval`` 设置的太小，将只能连接较少设备。
  - 当 Bluetooth LE 支持多个设备并发连接时，RF 的 solt 管理出错概率会增加，所以 Bluetooth LE 设备连接较多时，需要针对具体场景调试。

----------------

使用 ESP32 设备作为 Bluetooth® LE 主机，最大支持多少台从机设备进行连接？
--------------------------------------------------------------------------------------

  - ESP32 的 Bluetooth LE 最大支持 9 台从机设备进行连接，建议连接数量不超过 3 个。
  - 可通过 ``menuconfig`` > ``Component config`` > ``Bluetooth`` > ``Bluetooth controller`` > ``BLE MAX Connections`` 进行配置。

---------------

ESP32 下载 BluFi 例程进行配网，若使用 EspBluFi APP 在配网过程配置了一个错误的 Wi-Fi 从而无法连接，此时从 APP 端向设备端发送“扫描”命令后就会导致设备重启，是什么原因？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - BluFi 例程规定在 Wi-Fi 连接时不可以发送 Wi-Fi 扫描命令。
  - 但可在 blufi_example_main.c 文件下的  case ESP_BLUFI_EVENT_GET_WIFI_LIST:{}; 函数的首行增加 ESP_ERROR_CHECK(esp_wifi_disconnect()); 函数来解决此问题。

----------------

ESP32 设置中文蓝牙设备名称会异常显示乱码，原因是什么？
-------------------------------------------------------------------------------------------------------

  - 这是因为此时编辑器的中文编码格式不是 UTF-8，需要把编辑器的编码格式改成 UTF-8。

----------------

使用 ESP32 在蓝牙通道上传分包时，一包最大传输数据长度为 253（MTU 设置为 263），导致在传输大量数据包进行多包读取时传输较慢。请问是否有 BluFi 扩展协议，可支持一包传输较大长度的数据，或者有其他解决方案可提高传输速率吗？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 在蓝牙通道上传输大量数据包进行多包读取时传输较慢，可通过调整蓝牙连接参数来改善传输速度。
  - BLE 包长度设置取决于 ESP_GATT_MAX_MTU_SIZE 设置，可参见 `说明 <https://github.com/espressif/esp-idf/blob/cf056a7d0b90261923b8207f21dc270313b67456/examples/bluetooth/bluedroid/ble/gatt_client/tutorial/Gatt_Client_Example_Walkthrough.md>`__。
  - 设置的 MTU Size 大小会影响数据传输率，有效的 MTU 长度需要通过 MTU 交换方式来改变默认的 MTU 的大小。最终进行 MTU 交换使用的 MTU Ｓize 才是作为两者通信时的 MTU Size。可查看 MTU 交换后的值是多大，例如这样的值：

  .. code-block:: text

    case ESP_GATTS_MTU_EVT:
            ESP_LOGI(GATTS_TAG, "ESP_GATTS_MTU_EVT, MTU %d", param->mtu.mtu);   

----------------

ESP32-C3 Bluetooth® LE  稳定连接的数目可以达到多少个？
------------------------------------------------------------

  视连接参数而定，最多不超过八个。如需优化多连接性能，可选用 ESP32-C6 系列。

----------------

BLE 中如何修改广播的时间间隔？
------------------------------------------------------------

  - 通过修改广播结构体中的 ``adv_int_min`` 和 ``adv_int_max`` 两个参数来设置。这两个分别对应了广播时间间隔的最小值和最大值。
  - 广播时间间隔参数的取值范围为 0x0020 to 0x4000，默认值为 0x0800。对应的广播时间为参数值 * 0.625 ms，即广播时间间隔为 20 ms 到 10.24 s。
  - 当 ``adv_int_min`` 和 ``adv_int_max`` 不同时，广播的时间间隔在两者区间内产生，当最小值和最大值设置成同一个值时，时间间隔固定为该值。

----------------

ESP32 蓝牙占用多少内存？
-------------------------------------

  - 控制器：

    - BLE 单模：40 KB
    - BR/EDR 单模：65 KB
    - 双模：120 KB

  - 主设备：

    - BLE GATT Client（Gatt Client 演示）：24 KB (.bss+.data) + 23 KB (heap) = 47 KB
    - BLE GATT Server（GATT Server 演示）：23 KB (.bss+.data) + 23 KB (heap) = 46 KB
    - BLE GATT Client & GATT Server: 24 KB (.bss+.data) + 24 KB (heap) = 48 KB
    - SMP: 5 KB
    - 经典蓝牙（经典蓝牙 A2DP_SINK 演示，包含 SMP/SDP/A2DP/AVRCP）：48 KB (.bss+.data) + 24 KB (heap) = 72 KB（示例运行时额外增加 13 KB）

  .. note:: 以上堆 (Heap) 均包含任务栈 (Task Stack)，因为任务栈是从堆里分配出来的，算为堆。

  - 优化 PSRAM 版本：

  在 ESP-IDF V3.0 及以后，打开 ``menuconfig`` 里蓝牙菜单的 PSRAM 相关选项，将 Bluedroid(Host) 的部分 .bss/.data 段及堆放入 PSRAM，可额外省出近 50 KB。

---------------

ESP32 使用 gattc_gatts_coex.c 例程测试 BLE 多连接，在 ``menuconfi`` 中将 ``BLE Max connection`` 配置选项设置为 "5" ，但实际只能连 4 个设备，连接第 5 个设备的时候会报错，是什么原因？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 请在 ``menuconfig`` 中将 ``BT/BLE MAX ACL CONNECTIONS`` 配置选项设置为 “5”。

----------------

ESP32-C3 BLE 同时支持主从模式吗？主、从模式连接数分别是多少？
--------------------------------------------------------------------------------------

  :IDF\: release/v4.3, master:

  - ESP32-C3 同时支持主从模式，共用 8 个连接。例如，ESP32-C3 连接了 4 个 slave 设备，那么可被 8 - 4 = 4 个 master 设备连接。
  - 另外，ESP32-C3 用作 slave 时，可被 8 个 master 设备连接；用作 master 时，可连接 8 个 slave 设备。

---------------

BLE 如何抓包？
--------------------------------------------------------------------------------------------------------------------------------

  - 市面上有很多工具可供选择，比如：

    - TI Packet sniffer
    - NRF Packet sniffer

------------

使用 ESP32 开发板，测试好几个版本的 ESP-IDF 下的 BluFi 例程进行配网，点击配网之后都会打印如下报错，是什么原因？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    E (117198) BT_L2CAP: l2ble_update_att_acl_pkt_num not found p_tcb
    W (117198) BT_BTC: btc_blufi_send_encap wait to send blufi custom data

  - 当出现此报错，请在 ``components/bt/host/bluedroid/btc/profile/esp/blufi/blufi_prf.c`` 文件下，把 ``esp_ble_get_cur_sendable_packets_num(blufi_env.conn_id)`` 换成  ``esp_ble_get_sendable_packets_num()``。
  - 此问题已经在所有分支上面进行修复，可以更新 ESP-IDF 为最新 Release 版本。

--------------

使用 ESP32，请问蓝牙能否使用 light-sleep 模式，并在 light-sleep 模式下保持蓝牙连接？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP32 使用 light-sleep 模式，需要 ESP-IDF release/4.0 以上版本的 SDK 外加 32.768 kHz 晶振。
  - light-sleep 模式下，蓝牙可以保持连接。请参考 `Bluetooth modem sleep with external 32.768 kHz xtal under light sleep <https://github.com/espressif/esp-idf/issues/947#issuecomment-500312453>`_ 指南。

----------------------------

如何修改 ESP32 的蓝牙广播名称？
----------------------------------------------------------------------------

  - 要修改的结构体如下：

    .. code-block:: text

      static uint8_t raw_adv_data[] = {

              /* flags*/

              0x02, 0x01, 0x06,

              Tx power*/

              0x02, 0x0a, 0xeb,

              /* service uuid*/

              0x03, 0x03, 0xFF, 0x00,

              /* device name*/

              0x0f, 0x09,'E','S','P','_','G','A','T','T','S','_','D','E ','M','O'

      };

  - 上述 ``/* device name*/`` 为修改项。其中 0x0f 为此字段类型加具体内容的总长度，0x09 表示此类型代指设备名。后续的 'E', 'S', 'P', '_', 'G', 'A', 'T', 'T', 'S', '_', 'D','E', 'M', 'O' 为广播设备名的 ASCII 码表达。

----------------

BLE 5.0 广播设置为 legacy 模式时支持最大广播长度为多少？
-------------------------------------------------------------------------------

  - 最大支持到 31-byte。

---------------

BLE 广播包如何设置为不可连接包?
---------------------------------------------------------------------------------------------

  :CHIP\: ESP32:

  - 可参考 `gatt_server demo <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/ble/gatt_server>`_， 将广播包类型 adv_type 变量修改为 ADV_TYPE_NONCONN_IND。

    .. code:: text

      static esp_ble_adv_params_t adv_params = {
        .adv_int_min        = 0x20,
        .adv_int_max        = 0x40,
        .adv_type           = ADV_TYPE_NONCONN_IND,
        .own_addr_type      = BLE_ADDR_TYPE_PUBLIC,
        //.peer_addr            =
        //.peer_addr_type       =
        .channel_map        = ADV_CHNL_ALL,
        .adv_filter_policy = ADV_FILTER_ALLOW_SCAN_ANY_CON_ANY,
        }

----------------

ESP32 Bluetooth LE 白名单最多支持多少个设备？
--------------------------------------------------------------------------------------

  - 最多支持 12 个。

-------------

ESP32 低功耗蓝牙可以使用 PSRAM 吗？
-------------------------------------------------------------------

  请前往 ``Component config`` > ``Bluetooth`` > ``Bluedroid Options`` 开启 `BT/BLE will first malloc the memory from the PSRAM <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.4/esp32/api-reference/kconfig.html?highlight=config_bt_allocation_from_spiram_first#config-bt-allocation-from-spiram-first>`_ 配置，即可让低功耗蓝牙使用 PSRAM。

------------

使用 ESP32-C3 BLE Scan 时，是否可以设置仅扫描 Long Range 的设备？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 可以，可基于 `esp-idf/examples/bluetooth/bluedroid/ble_50/ble50_security_client <https://github.com/espressif/esp-idf/tree/release/v5.0/examples/bluetooth/bluedroid/ble_50/ble50_security_client>`_ 例程来测试。将 `ext_scan_params <https://github.com/espressif/esp-idf/blob/7f4bcc36959b1c483897d643036f847eb08d270e/examples/bluetooth/bluedroid/ble_50/ble50_security_client/main/ble50_sec_gattc_demo.c#L58>`_ 参数配置中 `.cfg_mask = ESP_BLE_GAP_EXT_SCAN_CFG_UNCODE_MASK | ESP_BLE_GAP_EXT_SCAN_CFG_CODE_MASK` 改为 `.cfg_mask = ESP_BLE_GAP_EXT_SCAN_CFG_CODE_MASK`, 这样就可以仅扫描到 primary PHY 类型为 LE CODED PHY 的广播包。

------------------

ESP32 蓝牙设备名称长度是否有限制？
---------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP32 蓝牙设备名称长度不超过 248 字节，实际蓝牙设备名称受限于蓝牙广播数据包的长度。关于配置选项说明，请参见 `CONFIG_BT_MAX_DEVICE_NAME_LEN <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v5.0/esp32/api-reference/kconfig.html#config-bt-max-device-name-len>`__。

----------------

使用 ESP32 如何设置 BLE Scan 永久扫描而不产生超时？
--------------------------------------------------------------------------------------------------------------------------

  - 在使用 `esp_ble_gap_start_scanning() <https://github.com/espressif/esp-idf/blob/490216a2ace6dc3e1b9a3f50d265a80481b32f6d/examples/bluetooth/bluedroid/ble/gatt_client/main/gattc_demo.c#L324>`__ 函数开始 BLE Scan 时，将 duration 参数设置为 0 即可。

------------------

如何通过 ESP32 获取 BLE 设备的 RSSI 的值？
---------------------------------------------------------------------------------------------------------------------------------------------------

  - 可使用 `esp_ble_gap_read_rssi() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/esp_gap_ble.html#_CPPv421esp_ble_gap_read_rssi13esp_bd_addr_t>`__ 函数来获取已连接的 BLE 设备的 RSSI 的值。
  - 若需要获取周围扫描到的所有 BLE 设备的 RSSI 的值，请在 ESP_GAP_BLE_SCAN_RESULT_EVT 事件中使用 `ble_scan_result_evt_param <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/esp_gap_ble.html#_CPPv4N22esp_ble_gap_cb_param_t8scan_rstE>`__ 结构体设置 RSSI 参数的打印。

----------------

如何增大 BLE5.0 传输距离？如何设置 BLE5.0 的 Long Range 模式？
--------------------------------------------------------------------------------------------------------------------------

  - 在实际应用中，BLE5.0 的传输距离在 200 米左右，建议以实际测试距离为准。ESP32-S3 支持 BLE5.0 的特性，支持通过 Coded PHY（125 Kbps 和 500 Kbps）与广播扩展实现远距离 (Long Range) 通信。
  - 您可以使用 125 Kbps Coded PHY 和增大发射功率 (tx_power)，来实现远距离通信。参考如下设置：

    .. code:: text

      esp_ble_gap_ext_adv_params_t ext_adv_params_coded = {
        .type = ESP_BLE_GAP_SET_EXT_ADV_PROP_SCANNABLE,
        .interval_min = 0x50,
        .interval_max = 0x50,
        .channel_map = ADV_CHNL_ALL,
        .filter_policy = ADV_FILTER_ALLOW_SCAN_ANY_CON_ANY,
        .primary_phy = ESP_BLE_GAP_PHY_CODED,
        .max_skip = 0,
        .secondary_phy = ESP_BLE_GAP_PHY_CODED,
        .sid = 0,
        .scan_req_notif = false,
        .own_addr_type = BLE_ADDR_TYPE_RANDOM,
        .tx_power = 18,
      };

  - BLE5.0 例程参见 ESP-IDF 里的 `ble_50 示例 <https://github.com/espressif/esp-idf/tree/v4.4.4/examples/bluetooth/bluedroid/ble_50>`__。

------------------

基于 ESP32-C3 通过 `esp_ble_gap_set_device_name() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/api-reference/bluetooth/esp_gap_ble.html#_CPPv427esp_ble_gap_set_device_namePKc>`_ 更改了蓝牙名称，在 Android 设备上运行良好，并显示自定义设备名称。在 IOS 设备上，设备名称仍然是之前默认的蓝牙名称，怎样才能使它在 Apple 设备上也能正常工作？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 此时需要使用 Raw data 的形式来创建 BLE 广播包，首先在 ``menuconfig`` 里使能 ``CONFIG_SET_RAW_ADV_DATA`` 选项（``idf.py menuconfig`` > ``Example 'GATT SERVER' Config`` > ``Use raw data for advertising packets and scan response data``），然后自定义 `gatt server 示例 <https://github.com/espressif/esp-idf/blob/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_server>`__ 里的 `广播包结构体 <https://github.com/espressif/esp-idf/blob/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_server/main/gatts_demo.c#L77>`__ 即可。
  - 请使用 nRF Connect APP 进行测试。我们测试过，在nRF connect APP 上是正常的, 这种现象与 IOS APP 本身有关。

------------------

使用两块 ESP32 开发板测试蓝牙连接，使用 `gatt_security_client <https://github.com/espressif/esp-idf/tree/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_security_client>`__ 和 `gatt_security_server <https://github.com/espressif/esp-idf/tree/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_security_server>`__ 示例怎么设置指定密钥自动连接？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - `gatt_security_client <https://github.com/espressif/esp-idf/tree/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_security_client>`__ 和 `gatt_security_server <https://github.com/espressif/esp-idf/tree/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_security_server>`__ 示例默认设置的固定配对密钥就是 123456，参见代码 `uint32_t passkey = 123456 <https://github.com/espressif/esp-idf/blob/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_security_server/main/example_ble_sec_gatts_demo.c#L561>`__，您也可以自行设置为其他密码。
  - 由于 ESP32 设备端默认没有显示器和输入键盘，因此例程将 IO 能力设置为 `No output No input <https://github.com/espressif/esp-idf/blob/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_security_server/main/example_ble_sec_gatts_demo.c#L556>`__。您也可以参考 `Gatt Security Server Example Walkthrough <https://github.com/espressif/esp-idf/blob/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_security_server/tutorial/Gatt_Security_Server_Example_Walkthrough.md>`__ 来了解更多细节。
  - 若要设置为可手动输入配对密钥，可将 `gatt_security_server <https://github.com/espressif/esp-idf/tree/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_security_server>`__ 示例中的 `esp_ble_io_cap_t iocap <https://github.com/espressif/esp-idf/blob/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_security_server/main/example_ble_sec_gatts_demo.c#L556>`__ 设置为 ESP_IO_CAP_OUT 模式，然后您可以使用 nRF Connect APP 与 BLE Server 建立连接。

------------------

将 `gatt_security_server <https://github.com/espressif/esp-idf/tree/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_security_server>`__ 设置为 ESP_IO_CAP_OUT 模式，并将 `gatt_security_client <https://github.com/espressif/esp-idf/tree/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_security_client>`__ 也设置为 ESP_IO_CAP_OUT 模式，然后故意设置错误的 passkey，但是还是能连接上，请问是什么原因？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - server 设置为 ESP_IO_CAP_OUT 模式时，gatt_security_client 应该设置为 ESP_IO_CAP_IN 模式。
  - 同时需要在 gatt_security_client 端的 `case ESP_GAP_BLE_PASSKEY_REQ_EVT <https://github.com/espressif/esp-idf/blob/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_security_client/main/example_ble_sec_gattc_demo.c#L386>`__ 事件下，增加以下代码即可避免故意设置错误的 passkey 但是还是能连接上的情况：

    .. code:: text

      esp_ble_passkey_reply(param->ble_security.ble_req.bd_addr, true, 123457);

------------------

ESP32-C3/ESP32-C6/ESP32-S3 是否支持蓝牙 AOA/AOD?
---------------------------------------------------------------------------------------------------------------------------------------------------

  ESP32-C3/ESP32-C6/ESP32-S3 均不支持蓝牙 AOA/AOD。

--------------

ESP32-C3 芯片使用 BLE5.0 特性支持的最大 BLE 广播数据包长是多大？
-------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP32-C3 BLE5.0 支持的最大广播数据包长为 1650 字节，可通过 `esp_ble_gap_config_ext_adv_data_raw() <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v5.0/esp32c3/api-reference/bluetooth/esp_gap_ble.html#_CPPv435esp_ble_gap_config_ext_adv_data_raw7uint8_t8uint16_tPK7uint8_t>`__ API  进行设置。

-------------------

ESP32 是否有 API 可用于检查设备 BLE 广播是否开始或停止？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 如果使用的是 bluedroid 协议栈，目前没有 API 可用于检查。
  - 如果使用的是 Nimble 协议栈（且使用的是 BLE 4.2 的非扩展广播），则可使用 `ble_gap_adv_active <https://github.com/espressif/esp-nimble/blob/f8f02740acdf4d302d5c2f91ee2e34444d405671/nimble/host/include/host/ble_gap.h#L831>`_ API 来检查。

-------------------

ESP32 用作 BLE server 时支持多个 client 同时连接吗？如何实现呢？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP32 可以作为 BLE 服务器支持多个 BLE 客户端同时接入，也可以作为 BLE 客户端同时连接多个 BLE 服务器。
  - 用作 BLE 服务器时，只要在客户端连接之后，再次开启广播即可。以 `gatt_server_service_table <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/ble/gatt_server_service_table>`_ 为例，在收到 ``ESP_GATTS_CONNECT_EVT`` 事件后，调用 ``esp_ble_gap_start_advertising`` 重新广播。
  - 用作 BLE 客户端时，可以参考 `gattc_multi_connect <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/ble/gattc_multi_connect>`_ 例程。

-------------

如何设置 BLE5.0 的持续扫描时间？
---------------------------------------------------------------------------------------------------

  - 使用 `esp_err_t esp_ble_gap_start_ext_scan(uint32_t duration, uint16_t period); <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32s3/api-reference/bluetooth/esp_gap_ble.html?highlight=esp_ble_gap_start_ext_scan#_CPPv426esp_ble_gap_start_ext_scan8uint32_t8uint16_t>`__ API 进行设置，当 period 设置为 0 时，duration 的时间就是持续扫描时间。

-------------

如何基于 `GATT Server <https://github.com/espressif/esp-idf/tree/v5.1/examples/bluetooth/bluedroid/ble/gatt_server>`_ 例程设置一个 128 位 UUID 的 GATT 服务？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  可参考如下代码：

    .. code:: c

      static const uint8_t pctool_service_uuid[16] = {
          0x00, 0x03, 0xcd, 0xd0, 0x00, 0x00, 0x10, 0x00, 0x80, 0x00, 0x00, 0x80, 0x5f, 0x9b, 0x01, 0x31
      };
      static const uint8_t pctool_write_uuid[16] = {
          0x00, 0x03, 0xcd, 0xd2, 0x00, 0x00, 0x10, 0x00, 0x80, 0x00, 0x00, 0x80, 0x5f, 0x9b, 0x01, 0x31
      };
      /* Full Database Description - Used to add attributes into the database */
      static const esp_gatts_attr_db_t gatt_db[HRS_IDX_NB] =
      {
          // Service Declaration
          [IDX_SVC]        =
          {
      {ESP_GATT_AUTO_RSP}, {ESP_UUID_LEN_16, (uint8_t *)&primary_service_uuid, ESP_GATT_PERM_READ,
            sizeof(pctool_service_uuid), sizeof(pctool_service_uuid), (uint8_t *)&pctool_service_uuid}
      },
          /* Characteristic Declaration */
          [IDX_CHAR_A]     =
          {
      {ESP_GATT_AUTO_RSP}, {ESP_UUID_LEN_16, (uint8_t *)&character_declaration_uuid, ESP_GATT_PERM_READ,
            CHAR_DECLARATION_SIZE, CHAR_DECLARATION_SIZE, (uint8_t *)&char_prop_read_write_notify}
      },
          /* Characteristic Value */
          [IDX_CHAR_VAL_A] =
          {
      {ESP_GATT_AUTO_RSP}, {ESP_UUID_LEN_128, (uint8_t *)&pctool_write_uuid, ESP_GATT_PERM_READ | ESP_GATT_PERM_WRITE,
            GATTS_DEMO_CHAR_VAL_LEN_MAX, sizeof(char_value), (uint8_t *)char_value}
      },
      }

------------

基于 `GATT Server <https://github.com/espressif/esp-idf/tree/v5.1/examples/bluetooth/bluedroid/ble/gatt_server>`_ 例程进行测试，是否可以删除默认的 1800 和 1801 服务属性？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 1800 和 1801 服务属性是 BLE 协议中的两个标准的 GATT 服务属性，不可以删除或禁用。它们是 BLE 协议规定的一部分，提供了设备的基本信息和通用访问能力，并保持与标准 BLE 协议的兼容性。
  - 0x1800 代表“通用访问”，定义了设备的通用属性；而 0x1801 代表“通用属性”，是一个简单的 GATT 服务，用于提供设备的基本信息。

-----------

是否有 ESP-IDF SDK 中对应 BLE 错误码的说明？
----------------------------------------------------------------------------------------------

  - ESP-IDF SDK 中的 BLE 错误码参考的是 BLE 标准协议，对应的错误码说明可参见 `LIST OF BLE ERROR CODES <https://github.com/chegewara/esp32-ble-wiki/issues/5>`_。

------------

基于 `BLE SPP Server <https://github.com/espressif/esp-idf/tree/v5.1/examples/bluetooth/bluedroid/ble/ble_spp_server>`_ 例程将蓝牙模式设置为 ``Component config`` > ``Bluetooth`` > ``Controller Options`` > ``Bluetooth controller mode (BR/EDR/BLE/DUALMODE)`` 双模式后进行测试，出现如下报错，是什么原因？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    .. code:: text

      E (2906) GATTS_SPP_DEMO: spp_gatt_init enable controller failed: ESP_ERR_INVALID_ARG

  - 当前报告的错误是由于 BLE SPP Server 示例默认为 Class Bluetooth 控制器释放了内存。请参考 `esp_bt_controller_mem_release() <https://docs.espressif.com/projects/esp-idf/en/release-v5.0/esp32/api-reference/bluetooth/controller_vhci.html#_CPPv429esp_bt_controller_mem_release13esp_bt_mode_t>`_ API 说明。
  - 设置 Bluetooth Dual Mode 模式后，需要删除 `ESP_ERROR_CHECK(esp_bt_controller_mem_release(ESP_BT_MODE_CLASSIC_BT)); <https://github.com/espressif/esp-idf/blob/cbce221e88d52665523093b2b6dd0ebe3f1243f1/examples/bluetooth/bluedroid/ble/ble_spp_server/main/ble_spp_server_demo.c#L666>`_，然后修改 `ret = esp_bt_controller_enable(ESP_BT_MODE_BLE); <https://github.com/espressif/esp-idf/blob/cbce221e88d52665523093b2b6dd0ebe3f1243f1/examples/bluetooth/bluedroid/ble/ble_spp_server/main/ble_spp_server_demo.c#L674>`_  为 ``ret = esp_bt_controller_enable(ESP_BT_MODE_BTDM);``。

-------------

是否有基于 ESP32 实现的发送 Bluetooth LE Eddystone beacon 例程？
---------------------------------------------------------------------------------------------------------------------------------

  - 目前没有基于 ESP32 的发送 Bluetooth LE Eddystone beacon 例程，可参考 `Eddystone Protocol Specification <https://github.com/google/eddystone/blob/master/protocol-specification.md>`_ 说明，基于 `esp-idf/examples/bluetooth/bluedroid/ble/ble_eddystone <https://github.com/espressif/esp-idf/tree/v5.1.2/examples/bluetooth/bluedroid/ble/ble_eddystone/main>`_ 例程修改代码，自行实现发送 Bluetooth LE Eddystone beacon 的应用。

------------

有官方的 Bluetooth LE OTA 例程吗？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 有的，见 `esp-iot-solution/examples/bluetooth/ble_ota <https://github.com/espressif/esp-iot-solution/tree/master/examples/bluetooth/ble_ota>`_。
  - 此外，Android 和 IOS 版本的 Bluetooth LE OTA APP 源码均已在 GitHub 开放，见 `Android 源码 <https://github.com/EspressifApps/esp-ble-ota-android>`_ 和 `IOS 源码 <https://github.com/EspressifApps/esp-ble-ota-ios>`_，需要手动将待升级的 bin 文件放入特定的 APP 路径下，对应 GitHub 工程的 README 对放置路径有进行说明。

------------

使用官方的 esp-iot-solution 下的 ble_ota 例程，蓝牙协议栈默认为 Bluedroid，使用 Android EspBleOTA APP 扫描不到设备名称 ``ESP&C919``，而 IOS EspBleOTA APP 可以扫描到，是什么原因？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 对于 `ble_ota <https://github.com/espressif/esp-iot-solution/tree/master/examples/bluetooth/ble_ota>`_ 例程，蓝牙协议栈默认为 Bluedroid，Bluetooth LE 5.0 features 默认是使能的，配置路径为：``menucofnig`` > ``Component config`` > ``Bluetooth`` > ``Bluedroid Options`` > ``Enable BLE 5.0 features``，而目前 Android EspBleOTA APP 不能支持扫描 Bluetooth LE 5.0 设备，所以扫描不到设备名称。
  - Android 系统蓝牙 4.0 和 5.0 的蓝牙扫描是两套 API，而 IOS 是同一套，所以 IOS APP 可以扫描到设备。
  - Android APP 需要做兼容处理才能扫描到设备，不过目前没有开发计划。如果希望 Android APP 可以扫描到设备，可以关闭 Bluetooth LE 5.0 features。
  - 此外，当配置为 Nimble 协议栈时，可以发现 Android APP 可以扫描到设备名称 ``nimble-ble-ota``，这是因为使用 Nimble 时，Bluetooth LE 5.0 扩展广播默认是关闭的，配置路径为：``menuconfig`` > ``Example Configuration`` > ``Enable Extended Adv``。

--------------

ESP32-C3 的 nimble 是否支持 Coded PHY 模式？
-----------------------------------------------------------------------------------------------------------------------------

 支持，但仅在 v5.0 及以上版本的 esp-idf SDK 中支持 nimble 的 Coded PHY 模式，可参考 `esp-idf/examples/bluetooth/nimble/ble_phy <https://github.com/espressif/esp-idf/tree/v5.0/examples/bluetooth/nimble/ble_phy>`_ 例程，支持在 1 Mbps PHY、2 Mbps PHY 和 Coded PHY（125 Kbps 与 500 Kbps）之间切换。

-------------

ESP32-S3 支持同时在 125 Kbps Coded PHY 和 1 Mbps PHY 下进行广播\扫描\连接吗？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  支持，可参考例程:

    - `esp-idf/examples/bluetooth/bluedroid/ble_50/multi-adv <https://github.com/espressif/esp-idf/tree/v5.2.1/examples/bluetooth/bluedroid/ble_50/multi-adv>`_
    - `esp-idf/examples/bluetooth/nimble/ble_multi_adv <https://github.com/espressif/esp-idf/tree/v5.2.1/examples/bluetooth/nimble/ble_multi_adv>`_
    - `esp-idf/examples/bluetooth/nimble/ble_multi_conn/ble_multi_conn_cent <https://github.com/espressif/esp-idf/tree/v5.2.1/examples/bluetooth/nimble/ble_multi_conn/ble_multi_conn_cent>`_

------------------

蓝牙运行过程中打印 ``A stack overflow in stack BTC_TASK has been detected`` 错误，如何解决？
---------------------------------------------------------------------------------------------------------------------------------------------------

  这是由于蓝牙控制器的任务堆栈外溢导致的，可以在 menuconfig 调大蓝牙控制器的任务堆栈大小：``idf.py menuconfig`` --> ``Component config`` --> ``Bluetooth`` --> ``Bluedriod options`` --> ``(3072)Bluetooth event(callback to application) task stack size``。

-----------

ESP-IDF 可以同时使能 BLE4.2 和 BLE5.0 吗？
----------------------------------------------------------------------------------------------

  目前可以在 menuconfig 里同时使能 BLE4.2 和 BLE5.0，但 BLE4.2 和 BLE5.0 的 API 有区别，不能混用。因此在未来会被修改为仅允许使能 BLE4.2 或 BLE5.0，无法同时使能两项。

-----------

ESP32 设备作为 BLE 服务器时，从机端如何发起 MTU 协商？
----------------------------------------------------------------------------------------------

  根据 BLE 协议，MTU 协商必须由客户端发起，服务器无法主动发起。因此，从机可以作为客户端来发起 MTU 协商。