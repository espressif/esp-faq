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

- 上电时 RF 初始化默认采⽤部分校准的⽅案：打开 menuconfig 中 `CONFIG_ESP32_PHY_CALIBRATION_AND_DATA_STORAGE` 选项。
- 不关注上电启动时间，可修改使⽤上电全校准⽅案：关闭 menuconfig 中 `CONFIG_ESP32_PHY_CALIBRATION_AND_DATA_STORAGE` 选项。
- 建议默认使用**部分校准**的方案，这样既可以保证上电启动的时间，也可以在业务逻辑中增加擦除 NVS 中 RF 校准信息的操作，以触发全校准的操作。

---

## ESP32 boot 启动模式不正常如何排查？

- 我司模组种使用 1.8V flash 与 psram 的 ESP32-WROVER 默认为 `0x33`, 下载模式 `0x23` 。其余使用 3.3V flash 与 psram  模组默认为 `0x13`, 下载模式 `0x03` 。详情请参考 ESP32 datasheet 种 Strapping 管脚部分。
- ESP32 正常启动的 boot 信息应该是 `0x13`，这⼏个⽣效的管脚如下：
  - 管脚：GPIO12，GPIO0，GPIO2，GPIO4，GPIO15，GPIO5
  - 电平： 0， 1， 0， 1, 0， 1

---

## 使用 ESP32 JLINK 调试，发现会报 ERROR：No Symbols For Freertos ，如何解决呢？

- 首先，这个不影响使用，解决措施可以参考：https://community.st.com/s/question/0D50X0000BVp8RtSQJ/thread-awareness-debugging-in-freertos-stm32cubeide-110-has-a-bug-for-using-rtos-freertos-on-stlinkopenocd。




