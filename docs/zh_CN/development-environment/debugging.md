# 调试分析

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## Wi-Fi 设备的串口名称？

- windows 系统中串口设备名称格式是：COM* 
- windows 10 ⼦统系 linux 中串口设备名称的标准格式是 /dev/ttyS*
- linux 系统中串口设备名称格式是：/dev/ttyUSB*
- macos 系统中串口设备名称格式是: /dev/cu.usbserial-*

---

## ESP32 如何关闭默认通过 UART0 发送的调试信息？

- 一级 Bootloader log 信息可以通过 GPIO15 接地来使能屏蔽。
- 二级 bootloader log 信息可以通过 make menuconfig 中 `Bootloader config` 进⾏相关配置。
- IDF 中 log 信息可以通过 make menuconfig 中 `Component config/Log output` 进⾏相关配置。

---

## 如何修改默认上电校准⽅式？

&emsp;上电时 RF 初始化默认采⽤部分校准的⽅案：打开 menuconfig 中 `CONFIG_ESP32_PHY_CALIBRATION_AND_DATA_STORAGE` 选项。\
&emsp;不关注上电启动时间，可修改使⽤上电全校准⽅案：关闭 menuconfig 中 `CONFIG_ESP32_PHY_CALIBRATION_AND_DATA_STORAGE` 选项。\
&emsp;建议默认使用**部分校准**的方案，这样既可以保证上电启动的时间，也可以在业务逻辑中增加擦除 NVS 中 RF 校准信息的操作，以触发全校准的操作。

---

## ESP32 boot 启动模式不正常如何排查？

&emsp;我司模组种使用 1.8V flash 与 psram 的 ESP32-WROVER 默认为 `0x33` ,下载模式 `0x23` 。其余使用 3.3V flash 与 psram  模组默认为 `0x13` , 下载模式 `0x03` 。详情请参考 ESP32 datasheet 种 Strapping 管脚部分。\
&emsp;ESP32 正常启动的 boot 信息应该是 `0x13`，这⼏个⽣效的管脚如下：
  - 管脚：GPIO12，GPIO0，GPIO2，GPIO4，GPIO15，GPIO5
  - 电平： 0， 1， 0， 1, 0， 1

---

## 使用 ESP32 JLINK 调试，发现会报 ERROR：No Symbols For Freertos ，如何解决呢？

&emsp;首先，这个不影响使用，解决措施可以参考[此 ST 论坛链接](https://community.st.com/s/question/0D50X0000BVp8RtSQJ/thread-awareness-debugging-in-freertos-stm32cubeide-110-has-a-bug-for-using-rtos-freertos-on-stlinkopenocd)。

---

## 如何在不更改 menuconfig 输出级别的情况下改变 log 级别？

&emsp;&emsp;无需使用 menuconfig，可以通过 API `esp_log_level_set()` 修改 log 的输出级别。

---

## 为什么 ESP8266 进⼊启动模式（2，7）并触发看⻔狗复位？

&emsp;&emsp;请确保 ESP8266 启动时，strapping 管脚处于所需的电平。如果外部连接的外设使 strapping 管脚进⼊到错误的电平，ESP8266 可能进⼊错误的操作模式。在⽆有效程序的情况下，看⻔狗计时器将复位芯⽚。\
&emsp;&emsp;因此在设计实践中，建议仅将 strapping 管脚⽤于连接⾼阻态外部器件的输⼊，这样便不会在上电时强制 strapping 管脚为⾼/低电平。参考链接：[ESP8266 Boot Mode Selection](https://github.com/espressif/esptool/wiki/ESP8266-Boot-Mode-Selection)。

- 请确保 ESP8266 启动时，strapping 管脚处于所需的电平。
- 如果外部连接的外设使 strapping 管脚进⼊到错误的电平，ESP8266 可能进⼊错误的操作模式。
- 在⽆有效程序的情况下，看⻔狗计时器将复位芯⽚。
