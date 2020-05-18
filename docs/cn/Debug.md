# 调试

## 关闭默认 UART0 调试信息

- `Q:`
  - 如何关闭默认通过 UART0 发送的调试信息？

- `A:`
  - Bootloader 信息：GPIO15 接地
  IDF 信息：可前往 menuconfig/Component config/Log output 进⾏相关配置

## ESP32 boot 启动模式

- `Q:`
  - ESP32 boot 启动模式不正常如何排查？

- `A:`
  - ESP32 正常启动的 boot 信息应该是0x13，这⼏个⽣效的管脚如下：
  管脚：GPIO12，GPIO0，GPIO2，GPIO4，GPIO15，GPIO5
  电平： 0， 1， 0， 1, 0， 1

## 默认上电校准⽅式

- `Q:`
  - 如何修改默认上电校准⽅式？

- `A:`
  - 上电时 RF 初始化默认采⽤部分校准的⽅案：打开 menuconfig 中 CONFIG_ESP32_PHY_CALIBRATION_AND_DATA_STORAGE 选项。
  不关注上电启动时间，可修改使⽤上电全校准⽅案：关闭 menuconfig 中CONFIG_ESP32_PHY_CALIBRATION_AND_DATA_STORAGE 选项。
  继续使⽤上电部分校准⽅案，若需在业务逻辑中增加触发全校准操作的功能擦除 NVS 分区中的内容，触发全校准操作。