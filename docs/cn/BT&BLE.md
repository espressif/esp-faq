# 蓝⽛/低功耗蓝⽛

## BLE Profile

- `Q:`
  - ESP32 ⽀持哪些 BLE Profile？

- `A:`
  - ⽬前⽀持完整的 GATT/SMP 等基础模块，可⾃⾏实现⾃定义配置；已经实现的配置有 BLE HID（设备端）、电池、DIS、Blu-Fi（蓝⽛配⽹）等。

## ESP32 的 BLE 蓝⽛配⽹兼容性

- `Q:`
  - ESP32 的 BLE 蓝⽛配⽹兼容性如何？是否开源？

- `A:`
  - ESP32 的蓝⽛配⽹，简称 Blu-Fi。
  Blu-Fi 配⽹兼容性与 BLE 兼容性⼀致，测试过苹果、华为、⼩⽶、OPPO、魅族、 ⼀加、中兴等主流品牌⼿机，兼容性良好。
  Blu-Fi 配⽹过程在 1s~2s 内就可完成。 ⽬前 Blu-Fi 配 ⽹ ⽀持诸多特性，如 WPA2 企业级证书传输、连接状态汇报、加密⽅式任意选择等， ⽬前 Blu-Fi 协议及⼿机应⽤部分的代码不开源，但后续有可能开源。

## ESP32 的 BLE ⼯作电流

- `Q:`
  - ESP32 的 BLE ⼯作电流是多少？

- `A:`

  | Current  |  Max (mA)  |  Min (mA)  |  Average  |
  | :-------------------------------------------------------------- | :------: | :------: | :------: |
  | Advertising: <br> Adv Interval = 40ms                           |   142.1  |    32    |   42.67  |
  | Scanning: <br> Scan Interval = 160ms,Window = 20ms              |   142.1  |    32    |   44.4   |
  | Connection(Slave): <br> Connection Interval = 20ms, Iatency = 0 |   142.1  |    32    |   42.75  |
  | Connection(Slave): <br> Connection Interval = 80ms, Iatency = 0 |   142.1  |    32    |   35.33  |

## ESP32 的经典蓝⽛⼯作电流

- `Q:`
  - ESP32 的经典蓝⽛⼯作电流是多少？

- `A:`
  - A2DP(CPU 160 Mhz，DFS = false，commit a7a90f)

  | Current | Max (mA) | Min (mA) | Average (mA) |
  | :-----: | :----: | :----: | :----: |
  | Scanning | 106.4 | 30.8 | 37.8 |
  | Sniff | 107.6 | 31.1 | 32.2 |
  | Play Music | 123 | 90.1 | 100.4 |

## ESP32 的 SPP 性能

- `Q:`
  - ESP32 的 SPP 性能如何？

- `A:`
  - 使⽤两块 ESP32 板⼦对跑 SPP，单向吞吐量量可达 1900 Kbps，约 235 KB/s，已接近规范⾥的理论值。

## ESP32 的经典蓝⽛配置

- `Q:`
  - ESP32 的经典蓝⽛⽀持哪些配置？

- `A:`
  - ESP-IDF V3.1: HFP Client (not HF gateway)
  - ESP-IDF V3.0: A2DP Source/A2DP Sink/AVRCP/AVDTP/SPP/RFCOMM

## ESP32 蓝⽛连接⼿机播放⾳乐

- `Q:`
  - 如何使⽤ ESP32 蓝⽛连接⼿机播放⾳乐？

- `A:`
  - ⽤⼿机通过蓝⽛播放⾳乐，ESP32 ⽤作 A2DP Sink，A2DP Sink Demo 只是通过⼿机获取 SBC 编码的数据流，若要播放出声⾳，需要做编解码转换及编解码器 、数/模转换器 、扬声器等模块以最终输出声⾳。

## ESP32 的经典蓝⽛连接兼容性

- `Q:`
  - ESP32 的经典蓝⽛连接兼容性如何？

- `A:`
  - 请联系 sales@espressif.com 获得兼容性测试报告。

## 蓝⽛的发射功率

- `Q:`
  - 蓝⽛的发射功率是多少？

- `A:`
  - ESP32 蓝⽛的发射功率有 9 档，对应功率 -12 ~ 12dBm，间隔 3dBm ⼀档。控制器软件对发射功率进⾏限制，根据产品声明的对应功率等级选取档位。

## ESP32 的蓝⽛内存占⽤

- `Q:`
  - ESP32 的蓝⽛内存占⽤是多少？

- `A:`
  - 控制器：
    - BLE 单模：40 KB（.data + .bss + 硬件）
    - BR/EDR 单模：65 KB（.data + .bss + 硬件）
    - 双模：120 KB（.data + .bss + 硬件）
  - 主设备：
    - BLE
    - GATT Client（Gatt Client 演示）：24 KB (.bss+.data) + 23 KB (heap) = 47 KB
    - GATT Server（GATT Server 演示）：23 KB (.bss+.data) + 23 KB (heap) = 46 KB
    - GATT Client & GATT Server: 24 KB (.bss+.data) + 24 KB (heap) = 48 KB
    - SMP: 5KB
    - 经典蓝⽛（经典蓝⽛ A2DP_SINK 演示，包含 SMP/SDP/A2DP/AVRCP）：48 KB (.bss+.data) + 24 KB (heap) = 72 KB（示例例运⾏⾏时额外增加 13 KB）
==注：== 以上堆 (Heap) 均包含任务栈 (Task Stack)，因为任务栈是从堆⾥⾥分配出来的，算为堆。
  - 优化 PSRAM 版本：
    - 在 ESP-IDF V3.0 及以后，打开 menuconfig ⾥⾥蓝⽛菜单的 PSRAM 相关选项，将 Bluedroid(Host) 的部分 .bss/.data 段及堆放⼊ PSRAM，可额外省出近 50KB。

## ESP32 的蓝⽛双模

- `Q:`
  - ESP32 的蓝⽛双模如何共存及使⽤？

- `A:`
  - ESP32 ⽀持的双模蓝⽛并没有特殊的地 ⽅，不需要做复杂的配置或调⽤即可使⽤。从开发者的⻆度来看，BLE 调⽤ BLE 的 API，经典蓝⽛调 ⽤经典蓝⽛的 API。经典蓝⽛与 BLE 共存说明可参考⽂档 [ESP32 BT&BLE 双模蓝⽛共存说明](https://www.espressif.com/sites/default/files/documentation/btble_coexistence_demo_cn.pdf)

## ESP32 的 BLE 吞吐量

- `Q:`
  - ESP32 的 BLE 吞吐量是多少？

- `A:`
  - ESP32 的 BLE 吞吐率取决于各种因素，例如环境⼲扰、连接间隔、MTU ⼤⼩以及对端设备性能等等。具体可以参考 IDF 中的 ble_throughput example，ESP32 板⼦之间的 BLE 通信最⼤吞吐量量可达 700 Kbps，约 90 KB/s。

## BIE 广播

- `Q:`
  - 为什么 BLE 开始⼴播后，有些⼿机扫描不到？

- `A:`
  - 需确认⼿机是否⽀持 BLE 功能：有的⼿机在“设置” -> “蓝⽛”中只显示默认的经典蓝⽛，BLE ⼴播会被⼿机过滤掉。建议使⽤专⻔的 BLE 应⽤来调试 BLE 功能。例如，苹果⼿机可以使⽤ LightBlue 应⽤。需确认⼴播包的格式符合规范，⼿机⼀般会对不符合格式的⼴播包进⾏过滤，只有格式正确的才能被显示出来。

## ESP32 与 BT 5.0

- `Q:`
  - ESP32 可以⽀持 BT 5.0 吗？

- `A:`
  - ESP32 硬件不⽀持 BLE5.0，⽀持 BLE4.2，⽬前通过了 BLE5.0 的部分认证。详细⽀持的 feature list 在不断更新，请联系 sales@espressif.com 获得最新 feature list。

## 蓝牙 OTA 升级

- `Q:`
  - 能否使⽤蓝⽛进⾏ OTA？

- `A:`
  - 可以使⽤蓝⽛进⾏ OTA。如果是⽤ BT，可以基于 bt_spp_acceptor 和 bt_spp_initiator 修改；如果是⽤ BLE，可以基于 ble_spp_server 和 ble_spp_client 修改。

## SSP 与 legacy pairing

- `Q:`
  - 为什么说 SSP ⽐ legacy pairing 更安全？

- `A:`
  - legacy pairing 使⽤对称加密算法， SSP 采⽤⾮对称加密算法。
