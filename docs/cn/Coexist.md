# 共存

## ESP32 的蓝⽛和 Wi-Fi

- `Q:`
  - ESP32 的蓝⽛和 Wi-Fi 如何共存？

- `A:`
  - 在 menuconfig 中，有个特殊选项 “Software controls WiFi/Bluetooth coexistence”，⽤于通过软件来控制 ESP32 的蓝⽛和 Wi-Fi 共存，可以平衡 Wi-Fi、蓝⽛控制 RF 的共存需求。请注意，如果使能 Software controls WiFi/Bluetooth coexistence 选项，BLE scan 间隔不应超过 0x100 slots（约 160ms）。
  若只是 BLE 与 Wi-Fi 共存，则开启这个选项和不开启均可正常使⽤。但不开启的时候需要注意 “BLE scan interval - BLE scan window > 150 ms”, 并且 BLE scan interval 尽量⼩于 500 ms。
  若经典蓝⽛与 Wi-Fi 共存，则建议开启这个选项。
