# 存储

## PSRAM 使用

- `Q:`
  - 如何使⽤ PSRAM，有相关资料例程吗？

- `A:`
  - 使⽤ RSPRM，可前往 make menuconfig -> Component config -> ESP32-specific 进⾏设置：
    - ESP-IDF V2.1：请选择 Capability allocator can allocate SPI RAM memory 
    - ESP-IDF V3.0 及之后版本，请选择 Support for external, SPI-connected RAM 

  - 使能 PSRAM 后，通过 malloc 使能 malloc() can also allocate in SPI SRAM 动态分配 PSRAM。在允许的情况下，将使⽤ PSRAM ⾃动进⾏动态内存分布。
    此外，可以使⽤ Always put malloc()s smaller than this size, in bytes, in internal RAM 设置阈值。
    如果 malloc 动态内存分配⼤于设定值，则使⽤ PSRAM。否则，使⽤ RAM。
    如果剩余 RAM 不⾜，则使⽤ PSRAM。

## PSRAM 和 RAM 剩余获取

- `Q:`
  - 如何获取剩余 PSRAM 和 RAM？

- `A:`

  | 版本 | 类型 | 子类型 | API |
  | :-----: | :----: | :----: | :----: |
  | ESP-IDF V3.0 及以后版本 | 有 PSRAM | 所有剩余内存 (包括 PSRAM 和内部 RAM)| esp_get_free_heap_size() |
  | ESP-IDF V3.0 及以后版本 | 有 PSRAM | 剩余 RAM 内存 | heap_caps_get_free_size(MALLOC_CAP_INTERNAL) |
  | ESP-IDF V3.0 及以后版本 | 有 PSRAM | 剩余 DRAM 内存 | heap_caps_get_free_size(MALLOC_CAP_INTERNAL | MALL) |
  | ESP-IDF V3.0 及以后版本 | 无 PSRAM | 剩余 RAM 内存 | heap_caps_get_free_size(MALLOC_CAP_INTERNAL)|
  | ESP-IDF V3.0 及以后版本 | 无 PSRAM | 剩余 DRAM 内存 | esp_get_free_heap_size() |
  | ESP-IDF V2.1 | 有 PSRAM | 所有剩余内存 (包括 PSRAM 和内部 RAM) | xPortGetFreeHeapSizeCaps(MALLOC_CAP_SPIRAM) |
  | ESP-IDF V2.1 | 有 PSRAM | 剩余 DRAM 内存 | xPortGetFreeHeapSizeCaps(MALLOC_CAP_INTERNAL) |
  | ESP-IDF V2.1 | 有 PSRAM | 剩余 DRAM 内存 | xPortGetFreeHeapSizeCaps(MALLOC_CAP_INTERNAL | MALLOC_CAP_8BIT) |
  | ESP-IDF V2.1 | 无 PSRAM | 剩余 RAM 内存 | esp_get_free_heap_size()|

## SD 卡和 PSRAM 引脚合并

- `Q:`
  - ESP32 pin 脚不够⽤是否可以将 SD 卡和 PSRAM 合并到⼀起？类似于 PC 的硬盘划出⼀⽚空间做虚拟内存，不同的是，把 SD 卡接到 PSRAM 的位置；这样不仅能释放 SD 卡占⽤的 6 个管脚，还可以省去 PSRAM 的成本？

- `A:`
  1. SD 卡可以挂载到 psram 的位置，但是不能与 psram 同时挂载，也不能直接当 psram 使⽤，公⽤ flash 还要避免 cache 操作冲突等相当多的问题。
  2. SD 卡充当虚拟内存理论上可以但是我们当前的 SDK 不⽀持，⾃⼰实现的难度未知。

## Flash 和 QSPI FLASH

- `Q:`
  - Flash 最⼤⽀持 16M，全部都能够作为程序空间进⾏询址吗？是否⽀持 QSPI FLASH 以提⾼数据的读取速度？

- `A:`
  - Flash 都可以⽤来存放程序，能寻址。⽀持 QSPI flash。
