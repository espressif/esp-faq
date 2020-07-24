# AT

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## ESP32 AT 吞吐量如何测试及优化？

- AT 吞吐量测试的影响因素较多，建议使⽤ esp-idf 中的 iperf 示例进行测试（用 AT 测试时，请使用透传方式，并将数据量调整为 1460 字节连续发送）。
- 若测试速率不满⾜需求，可⾃行编译 esp-at ，修改 esp-idf 中 menuconfig iperf 参数，提⾼速率。

---

## ESP32 AT Wi-Fi 连接耗时多少 ？
> ESP32 AT release/v2.0 固件初始化（模块启动）到 Wi-Fi 连接的整个时间⼤概是多久？

- 在办公室场景下，ESP32 AT release/v2.0.0 版本连接耗时 实测为 11 s。
- 实际使用中，Wi-Fi 连接时间取决于路由器性能，⽹络环境，模块天线性能等多个条件。

---

## AT 提示 busy 是什么原因？

- AT 指令的处理是线性的，也就是处理完前⼀条指令后，才能接收下⼀条指令进⾏处理。提示 "busy" 表示正在处理前⼀条指令，⽆法响应当前输⼊。
- ⽽任何串⼝的输⼊，均被认为是指令输⼊，因此，当有多余的不可⻅字符输⼊时，系统也会提示 "busy" 或者 "ERROR"。
- 例如，串⼝输⼊ AT+GMR (换⾏符 CR LF) (空格符)，由于 AT+GMR (换⾏符 CR LF) 已经是⼀条完整的 AT 指令了，系统会执⾏该指令。
- 如果系统尚未完成 AT+GMR 操作，就收到了后⾯的空格符，将被认为是新的指令输⼊，系统提示 "busy"。
- 如果系统已经完成了 AT+GMR 操作，再收到后⾯的空格符，空格符将被认为是⼀条错误的指令，系统提示 "ERROR"。

---

## ESP32 AT 相关资源从哪里获得？

- ESP32 AT bin 文件：https://www.espressif.com/zh-hans/support/download/at \
- ESP32 AT 文档：[AT 指令集](https://github.com/espressif/esp-at/blob/master/docs/ESP_AT_Commands_Set.md)\
- 此外，客户也可以基于乐鑫官方的 esp-at 工程开发更多的 AT 指令，ESP32 AT 工程可以在 GitHub 下载：https://github.com/espressif/esp32-at

---

## ESP8266 云端升级失败有哪些原因？

ESP8266 云端升级参考⽂档为[《ESP8266 云端升级指南》](https://www.espressif.com/sites/default/files/documentation/99c-esp8266_fota_upgrade_cn.pdf)
建议按如下顺序，进⾏排查：

1. 确认使⽤了正确⼤⼩的 Flash
2. 确认是否烧录了 blank.bin 做初始化
3. 确认 user1.bin 和 user2.bin 下载到了正确的地址
4. 确认⽣成 user1.bin 和 user2.bin 使⽤了相同的 Flash、boot 配置

---

## ESP32-AT 编译过程中，出现 no module named yaml 的错误，应如何解决？

请安装 yaml 模块: `python -m pip install pyyaml`

---

## AT 命令中串口波特率是否可以修改？（默认：115200）

AT 命令串口的波特率是可以修改的。
  - 第一种方法，您可以通过串口命令 `AT+UART_CUR` 或者 `AT+UART_DEF`进行修改, 详情请参考 [AT 指令集](https://github.com/espressif/esp-at/blob/master/docs/en/get-started/ESP_AT_Commands_Set.md)。

  - 第二种方法，您可以重新编译 AT 固件，编译介绍：[使用 esp-at 工程编译固件](https://github.com/espressif/esp-at/blob/master/docs/en/get-started/ESP_AT_Get_Started.md)，以及波特率修改介绍 [修改 UART 的波特率](https://github.com/espressif/esp-at/blob/master/docs/zh_CN/get-started/How_To_Set_AT_Port_Pin.md)。

---

## ESP8266 如何通过 AT 指令建立 SSL 链接？

- ESP8266 建立 SLL 连接服务器示例，请使用如下指令：

 ``` shell
  AT+CWMODE=1                                 // 设置 wifi 模式  为 station 
  AT+CWJAP="espressif_2.4G","espressif"       // 连接 AP ，账号、密码
  AT+CIPMUX=0                                 // 设置 单连接 
  AT+CIPSTART="SSL","www.baidu.com",443       // 建立 SSL 连接
  ```

---

## ESP32 是否可通过 HSPI 来传输 AT 指令？

ESP32 作为从机不能通过 HSPI 来传输 AT 指令，但主机端 MCU 可通过 HSPI 来传输 AT 指令，ESP32 传输 AT 建议用 SDIO 来替代，参见[说明](https://github.com/espressif/esp-at/tree/master/examples/at_sdspi_host)。
