# AT

## ESP8266 云端升级与 BIN 文件

- `Q:`
  - ESP8266 云端升级为什么需要 2 个 BIN ⽂件？“user .bin”和 “user2.bin”有什么区别？

- `A:`
  - user1.bin 和 user2.bin 是 2 个不同的 BIN ⽂件。 ⽣成 user1.bin 和 user2.bin 时，必须使⽤相同的 Flash 和 boot 设置，以保证 OTA 升级成功。2 个 BIN ⽂件是互补的，运⾏ user1.bin 的时候，升级是下载 user2.bin；运⾏ user2.bin 的时候，升级是下载user1.bin。这样可以保证升级过程中，如果有掉线的情况发⽣，设备还是可以正常运⾏⾏。

## ESP8266 生成 bin 文件

- `Q:`
  - ESP8266 如何⽣成“user1.bin”和“user2.bin”？

- `A:`
  - 编译环境下，执⾏ gen_misc.sh 分别得到 user1.bin 和 user2.bin。步骤如下：
  1. 使⽤正确的 Flash 和 boot 配置，编译⽣成 user1.bin 
  2. 执⾏ make clean，以便清除之前的残余信息
  3. 使⽤相同的 Flash 和 boot 配置，编译⽣成 user2.bin

## ESP8266 云端升级失败

- `Q:`
  - ESP8266 云端升级失败有哪些原因？

- `A:`
  - 远端升级的详细介绍参考⽂档为《ESP8266 云端升级指南》
  建议按如下顺序，进⾏排查：
  1. 确认使⽤了正确⼤⼩的 Flash 
  2. 确认是否烧录了 blank.bin 做初始化
  3. 确认 user1.bin 和 user2.bin 下载到了正确的地址
  4. 确认⽣成 user1.bin 和 user2.bin 使⽤了相同的 Flash、boot 配置

## ESP8266 云端升级与服务器

- `Q:`
  - 使⽤ ESP8266，如何通过⾃⼰的服务器进⾏云端升级？

- `A:`
  - 如果通过客户⾃⼰的服务器升级，请确认服务器满⾜下⾯的要求。
  - 发送 HEAD 指令到云端服务器 ，询问待升级的 BIN ⽂件⻓度，服务器回复的 HTTP 包头中要求带有 BIN ⽂件的⻓度信息。
  - 根据上述⽅法查询到的 BIN ⽂件⻓度，在 ESP8266 模块的 Flash 待升级区域，擦除该指定⻓度 （spi_flash_erase_sector），等待下载
  - 发送 GET 指令，从服务器下载 BIN ⽂件，写⼊到 Flash 的待升级区域

## SmartConfig 配⽹

- `Q:`
  - 使⽤ ESP8266，SmartConfig 配⽹配不上有哪些原因？

- `A:`
  - 请按如下顺序进⾏排查：
  1. APP 版本是否⽀持 SDK 版本或 SmartConfig 版本
  2. ⼿机连接的路由器不能是单 5G 路由（双频路路由器除外）
  3. SmartConfig 过程中不要调⽤其他 API 
  4. 使⽤ AT 时，设备没有获得 IP 之前，不要调⽤ smartconfig_stop
  如以上排除，请把连接失败和成功的 log 发给我们技术做⽀持分析

## HTTP 服务端

- `Q:`
  - ESP8266 ⽀持 HTTP 服务端吗？

- `A:`
  - ⽀持。ESP8266 在 SoftAP 和 Station 模式下都可以作服务端。
  1. 在 SoftAP 模式下，ESP8266 的服务端 IP 地址是 192.168.4.1。
  2. 如果 Station 模式，服务端的 IP 地址为路路由器 分配给 ESP8266 的 IP。
  3. 如果是基于 SDK ⼆次开发，那么需使 ⽤ espconn 结构体和相关 API。
  4. 如果是使 ⽤ AT 指令，需使 ⽤ AT+CIPSERVER 开启服务端。

## 添加⾃定义 AT 命令

- `Q:`
  - ESP8266 如何添加⾃定义 AT 命令，⾃定义 AT 命令字段和参数段⻓度限制是多少？

- `A:`
  - 客户可以基于 ESP8266_NONOS_SDK\examples\at 示例例代码，在 ESP8266 ⾃带 AT 命令的基础上，添加客户⾃定义的 AT 命令。
  关于⾃定义 AT 命令，SDK 限制整条 AT 命令数据⻓度最⼤ 128 字节（含结束符“\r\n”），不单独限制命令段和参数段。

  > 例如：AT+CMDTEST=param1,param2,param3,….paramN\r\n 
  则：strlen(“AT+CMDTEST=param1,param2,param3,....paramN\r\n”)<=128 bytes 
  
  相关 SDK 及参考资料请⾄乐鑫官⽹下载：[ESP8266 SDK 和 Demo](https://www.espressif.com/zh-hans/support/download/sdks-demos)

## ESP32 AT 相关资源

- `Q:`
  - ESP32 AT 相关资源从哪⾥获得？

- `A:`
  - ESP32 AT bin ⽂件：https://www.espressif.com/zh-hans/support/download/at
  ESP32 AT ⽂档：[中⽂版 | English](https://www.espressif.com/sites/default/files/documentation/esp32_at_instruction_set_and_examples_en.pdf)
  此外，客户也可以基于乐鑫的 AT 核 ⾃ ⾏⾏开发更更多的 AT 指令，ESP32 AT ⼯程可以在 GitHub 下载：https://github.com/espressif/esp32-at

## AT 提示 busy

- `Q:`
  - AT 提示 busy 是什么原因？

- `A:`
  - AT 指令的处理是线性的，也就是处理完前⼀条指令后，才能接收下⼀条指令进⾏处理。提示 “busy” 表示正在处理前⼀条指令，⽆法响应当前输⼊。
  ⽽任何串⼝的输⼊，均被认为是指令输⼊，因此，当有多余的不可⻅字符输⼊时，系统也会提示 “busy” 或者 “ERROR”。
  例如，串⼝输⼊ AT+GMR (换⾏符 CR LF) (空格符)，由于 AT+GMR (换⾏符 CR LF) 已经是⼀条完整的 AT 指令了了，系统会执⾏该指令。
  如果系统尚未完成 AT+GMR 操作，就收到了后⾯的空格符，将被认为是新的指令输⼊，系统提示 “busy”。如果系统已经完成了 AT+GMR 操作，再收到后⾯的空格符，空格符将被认为是⼀条错误的指令，系统提示 “ERROR”。

## ESP32 AT Wi-Fi 连接时间

- `Q:`
  - ESP32 AT release/v2.0 测试 Wi-Fi 初始化（模块启动）到 Wi-Fi 连接的整个时间⼤概是多久？

- `A:`
  - 在ESP32 AT release/v2.0.0 版本上实测是 11 s，Wi-Fi 连接时间取决于路由器⽹络环境，不同的环境测试结果差异较⼤。

## ESP32 deep sleep模式唤醒不重启

- `Q:`
  - ESP32 deep sleep模式，有没有那种唤醒⽅式类似于ISR，唤醒的时候不要重启？

- `A:`
  - 深度睡眠唤醒都是需要重新进⾏初始化操作，是因为系统cpu 与 memory 模组均掉电， 数据丢失。
  - 在深度睡眠 模式中 RTC 内存模块数据是通电保存的，您可以将任务模组分类后将参数放⼊ RTC 内存，在唤醒后执⾏后续操作。

## ESP32 AT 测试吞吐量

- `Q:`
  - ESP32 是否可以使⽤ AT 测试吞吐量？

- `A:`
  - AT 测试 TCP/UDP 吞吐量影响因素⽐较多，例如每次要等到响应才可以发送下⼀包数据。所以如果要测试 ESP32 的性能不建议使⽤ AT 测试，建议使⽤ esp-idf 中的 iperf 示例进⾏测试。
  使⽤ AT 测试时，可以修改成透传进⾏测试，这样可以不⽤等到响应再发送下⼀包数据。适当增加 buff 到1460 字节，数据也是 1460 字节⼀发，可适当提⾼速率。若速率仍然不满⾜需求，则可以⾃⼰编译 esp-at ，并修改 esp-idf 中 menuconfig 的 iperf 参数从⽽提⾼速率，但是这样会导致⼀些资源被占⽤，所以不建议这么做。
