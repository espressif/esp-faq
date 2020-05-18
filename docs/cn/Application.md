# 基本使用

## AP 扫描

- `Q:`
  - 内存不够时，如何进⾏ AP 扫描？

- `A:`
  - 存放扫描结果的内存时动态申请的，因此当周边存在⼤量的 AP 时会占⽤很多内存，内存不够时，⼀个缓解办法是逐信道扫描。

## ESP32 扫描时间

- `Q:`
  - ESP32 扫描⼀次需要花多⻓时间？

- `A:`
  - 扫描花费的总时间取决于：
  1. 是被动扫描还是主动扫描，默认为主动扫描：每个信道停留留的时间，默认主动扫描为 120 ms，被动扫描为 360 ms。
  2. 是快速扫描还是全信道扫描，默认为快速扫描：国家码与配置的信道范围，默认为 1~13 信道。

## ⽋压复位

- `Q:`
  - 发⽣⽋压复位的原因是什么？

- `A:`
  - 电源低于低电压阈值；
  芯⽚⼯作时候电流波动⽐较⼤，电源的驱动能⼒不⾜导致；
  如果使⽤ USB 为板⼦供电，USB 的稳定性也会影响供电性能。

## ESP32 引脚占用

- `Q:`
  - 使⽤ ESP32 的哪些引脚被占⽤了？

- `A:`
  - IO6 - IO11 为 Flash 引脚，作为 flash 通信使⽤， ⽆法⽤于 GPIO。如果是 WROVER 模块，GPIO16 和 GPIO17 会被系统占⽤，⽆法⽤于 GPIO。此外，ESP32 有 5 个 strapping 引脚，在使⽤时也因应该注意，请[参考《ESP32 技术规格书》](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf)

## 查看线程

- `Q:`
  - 怎样查看线程使⽤过的最⼤栈⼤⼩？

- `A:`
  - 请使⽤ UBaseType_t uxTaskGetStackHighWaterMark( TaskHandle_t xTask ) 函数，任务的堆栈空间会随着任务执⾏以及中断处理⽽增⻓或缩⼩。该函数可以返回任务启动后的最⼩剩余堆栈空间。换句话说，可以间接估算出⼀个任务最多需要多少堆栈空间。在⽂件 FreeRTOSConfig.h 中，宏 INCLUDE_uxTaskGetStackHighWaterMark 必须设置成 1，此函数才有效。注意，该选项默认有效。详情⻅ https://www.freertos.org/uxTaskGetStackHighWaterMark.html

## 参考设计中 I2S 信号管脚分布

- `Q:`
  - 乐鑫提供的参考设计中 I2S 信号分布太散，是否可以配置集中⼀些，⽐如配知道 GPIO5，GPIO18，GPIO23、GPIO19、GPIO22 管脚上；I2C 配置到 GPIO25、GPIO26 或 GPIO32、GPIO33 管脚上？

- `A:`
  - 所有 I2S 的 I/O 均可任意分配，需要注意有的 I/O 只能作为输⼊，请[参考《ESP32 技术规格书》](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf)最后⼀⻚

## OTA 升级的 demo

- `Q:`
  - OTA 升级有没有相关 demo 参考？

- `A:`
  - ESP8266 OTA 请参考 https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/system/ota
  ESP32 及 ESP32-S2 OTA 请参考 https://github.com/espressif/esp-idf/tree/master/examples/system/ota

## RTOS 3.0 的寄存器⼿册

- `Q:`
  - RTOS 3.0 有没有详细的寄存器⼿册？

- `A:`
  - 请参考 《8266 TRM appendix》部分

## Wi-Fi 设备的名称

- `Q:`
  - Win 10 系统上直接装 linux ⼦系统 ubuntu 18.04，此⼦系统下 Wi-Fi 设备的名称是什么？

- `A:`
  - WIN 10 系统下设备名称的标准格式是 /dev/ttyS*

## boundary scan

- `Q:`
  - Does Espressif support boundary scans？

- `A:`
  - ESP32 不⽀持 boundary scan. 

## 分开编译

- `Q:`
  - 应⽤层与底层的 bin ⽂件可以分开编译吗?

- `A:`
  - 不⽀持分开编译。

## NONOS_SDK 2.2.2 连接时间

- `Q:`
  - NONOS_SDK 2.1.0 升级到 2.2.2 后，连接时间太⻓?

- `A:`
  - 请升级到 SDK ver: 3.0.1，此版本中解决了 CCMP 加密与某些 AP 不兼容的问题。

## light-sleep 模式下 VDD3P3_RTC 的电平

- `Q:`
  - ESP32-WROVER-B 进⼊ light-sleep 后，pads powered by VDD3P3_RTC 对应的 GPIO 的电平会被拉低

- `A:`
  - 根本原因是进⼊ light sleep 后 RTC 掉电导致的。使⽤函数 esp_sleep_pd_config(ESP_PD_DOMAIN_RTC_PERIPH, ESP_PD_OPTION_ON); 维持 RTC 的供电。

## idf.exe 闪退

- `Q:`
  - idf.exe使⽤时总是闪退？

- `A:`
  - 可能为安全频道⽀持出错，需修改 TLS 版本修复；请根据链接，勾选 TLS 和 SSL：https://jingyan.baidu.com/article/bad08e1ef76ef209c85121eb.html。

## IDF 升级 API 说明

- `Q:`
  - IDF 升级后 API 更新在哪⾥有说明吗？

- `A:`
  - 请在 Github release note 查看相关说明。

## ARM 板 对 esp32 进⾏升级

- `Q:`
  - ARM 板（MCU端） 如何通过发指令对 esp32 进⾏升级？

- `A:`
  - 我们集成了升级固件的相关指令，可以参考链接link：https://github.com/espressif/esptool/wiki/Serial-Protocol 。

## 使⽤ SPI 接⼝下载

- `Q:`
  - ESP_WROOM_S2 作为从机，STM32 作为 MCU ，可以使⽤ SPI 接⼝下载吗？

- `A:`
  - 不可以，固件下载⽤的是 UART 接⼝，通信可以使⽤ API 通信。也可以在固件中⾃⾏设计⽀持 OTA 功能。

## ESP32 E03 区别

- `Q:`
  - ESP32 E03 版本芯⽚在使⽤上和之前芯⽚软件使⽤上有什么区别呢？

- `A:`
  - 软件上使⽤⽆区别，是可以兼容之前的固件的，硬件上修复了⼀些bug，具体的可以参考该⽂档：https://www.espressif.com/sites/default/files/documentation/ESP32_ECO_V3_User_Guide__CN.pdf

## mpcie 协议

- `Q:`
  - ESP32 是否⽀持 mpcie 协议呢？

- `A:`
  - 不支持

## CCS（Cisco Compatible eXtensions）

- `Q:`
  - ESP8285 是否⽀持 CCS（Cisco Compatible eXtensions）？

- `A:`
  - 不支持

## ESP32 I2C 管脚配置

- `Q:`
  - ESP32 I2C 管脚配置需要注意什么事项？

- `A:`
  - 可以通过 IO_MUX 进⾏任意管脚配置，需要注意：GPIO34〜39（⽤作输⼊ IO），GPIO16 和 GPIO17 被 PSRAM 占⽤，GPIO9〜GPIO11 被 Flash 引脚占⽤， GPIO1 和 GPIO3 是 UART0 的 TX 和 RX 引脚，是⽆法配置的。

## wifi 和 ble 桥接功能

- `Q:`
  - ESP32 可以实现 wifi 和 ble 桥接的功能吗？

- `A:`
  - 可以实现的，这个属于应⽤层开发，客户可以直接通过 ble 获取数据，wifi 转出去，我们⽬前没有demo，但是客户可以参考⼀下 wifi 和蓝⽛共存的 demo：https://github.com/espressif/esp-idf/tree/release/v4.0/examples/bluetooth/esp_ble_mesh/ble_mesh_wifi_coexist， 修改为⾃⼰的应⽤即可

## 外部 FLASH 理解

- `Q:`
  - ESP32 使⽤ 16MB 的外部 FLASH，是否只有 11MB 是程序空间跑程序，另外的 4MB 多映射到 CPU 数据空间不能跑程序，不知理解是否对？

- `A:`
  - 理解是正确的，对于因为 cache 最⼤映射地址是 11MB， 超过的⽆法映射， 所以⽆法加载程序运⾏，可以正常对地址读写数据

## lora 的协议栈

- `Q:`
  - ESP32 内是否集成了 lora 的协议栈？

- `A:`
  - ESP32 没有集成 lora 协议栈，lora 芯⽚⽚中已经集成好了了协议栈，作为 MCU，只需要驱动它，把它当成⼀⼀个外接设备来使⽤就可以了。

## Hostname validation

- `Q:`
  - ESP8266 openssl 是否⽀持 Hostname validation？

- `A:`
  - openssl 不⽀持，建议使⽤ wolfssl 协议，接⼝是 WolfSSL_CTX_set_verify(ctx, SSL_VERIFY_NONE, NULL),参考 openssl 的示例 demo，将 openssl 中的接⼝换为 wolfssl 测试就可以了。

## 单核与双核的区别

- `Q:`
  - 单核与双核的区别有哪些？从编程开发⽅式、性能表现、功耗表现等⽅⾯列举⼀下。

- `A:`
  - 单核与双核主要差异是多了⼀个独⽴核⼼， 可以把⼀些实时性⾼的操作放在独⽴的⼀个核⼼上。
  - 编程⽅式⼀致， 仅仅需要配置 freertos 运⾏在单核上。
  - 性能表现仅在⾼负载运算时有差异，若⽆⼤量计算差异使⽤上⽆明显差异（例如 AI 算法， ⾼实时性中断）。
  - 功耗⽅⾯仅在 modem-sleep 的时候会有细微差别，详情可参考芯⽚⼿册。

## no module named yaml 的错误

- `Q:`
  - ESP32-AT 编译过程中，出现 no module named yaml 的错误？

- `A:`
  - 安装 yaml 模块， 需使⽤ python -m pip install pyyaml。
