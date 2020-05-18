# 射频

## 修改默认上电校准⽅式

- `Q:`
  - 如何修改默认上电校准⽅式？

- `A:`
  - 上电时 RF 初始化默认采⽤部分校准的⽅案：
    esp_init_data_default.bin 中第 115 字节为 0x01，RF 初始化时间较短。
  - 不关注上电启动时间，可修改使⽤上电全校准⽅案：
  **使⽤ NONOS SDK 及 RTOS SDK 3.0 以前的版本：**
    - 在 user_pre_init 或 user_rf_pre_init 函数中调 ⽤system_phy_set_powerup_option(3)；
    - 修改 phy_init_data.bin 中第 115 字节为 0x03。
  **使⽤ RTOS SDK 3.0 及以后版本：**
    - 在 menuconfig 中关闭 CONFIG_ESP_PHY_CALIBRATION_AND_DATA_STORAGE；
    - 如果在 menuconfig 中开启了 CONFIG_ESP_PHY_INIT_DATA_IN_PARTITION，修改 phy_init_data.bin 中第 115 字节为 0x03；
    如果没有开启 CONFIG_ESP_PHY_INIT_DATA_IN_PARTITION，修改 phy_init_data.h 中第 115 字节为 0x03。
    **继续使⽤上电部分校准⽅案，若需在业务逻辑中增加出发全校准操作的功能：**
    - 使⽤ NONOS SDK 及 RTOS SDK 3.0 以前的版本：擦除 RF 参数区中的内容，触发全校准操作
    - 使⽤ RTOS SDK 3.0 及以后版本：擦除 NVS 分区中的内容，触发全校准操作

## 优化⼆次谐波等杂散

- `Q:`
  - 客户⾃研产品如何优化⼆次谐波等杂散？

- `A:`
  - ⼆次谐波主要来源于射频链路路辐射和 PA 电源辐射，同时易易受到客户底板（板⼦尺⼨）及产品整机影响，因此有如下建议：在射频匹配中使⽤ ⼀个接近 2.4pF ⼤⼩的对地电容，可较好地优化射频链路路上的杂散辐射；在 PA 电源 (芯⽚ 3、4 管脚) ⼊⼝增加⼀个串串联电感可较好减少 PA 电源的杂散辐射。

## 80MHz 倍频杂散

- `Q:`
  - 80MHz 倍频杂散较差该如何解决？

- `A:`
  - 若 80MHz 倍频杂散超标，如 160MHz、240MHz、320MHz 等均⽐较⾼，可在发送数据 (TXD) 串⼝线路路中串联⼀个阻值约为 470Ω 的电阻，即可有效抑制 80MHz 倍频杂散。
