# 硬件

## ESP8266 电压电流需求

- `Q:`
  - ESP8266 电压电流需求？

- `A:`
  - ESP8266 的数字部分的电压范围是 1.8V ~ 3.3V。
  模拟部分的⼯作电压是 3.0V ~ 3.6V，最低 2.7V。
  模拟电源峰值 350mA。
  数字电源峰值 200mA。
  ==注意：== 选择的 SPI Flash ⼯作电压也需要与 GPIO 的电压匹配。CHIP_EN 还是⼯作在 3.0 ~ 3.6V，使⽤ 1.8V GPIO 控制时需要注意电平转换。

## ESP8266 供电设计

- `Q:`
  - 设计 ESP8266 的供电时，需要注意哪些问题？

- `A:`
  - 请注意如下⼏点：
  1. 如果是使⽤ LDO 变压，请确保输⼊电压和输出电压要⾜够⼤。
  2. 电源轨去耦电容器必须接近 ESP8266 摆放，等效电阻要⾜够低。
  3. ESP8266 不能直连 5V 电压。
  4. 如果是通过 DC-DC 给 ESP8266 供电，必要时要加上 LC 滤波电路。

## ESP8266 上电电流

- `Q:`
  - ESP8266 上电时，电流很⼤，是什么原因？

- `A:`
  - ESP8266 的 RF 和数字电路具有极⾼的集成度。上电后，RF ⾃校准会需要⼤电流。模拟部分电路路最⼤的极限电路可能达到 500mA；数字电路部分最⼤电流达到 200mA。 ⼀般的操作，平均电流在 100mA 左右。
  因此，ESP8266 需要供电能达到 500mA，能够保证不会有瞬间压降。

## ESP8266 供电选择

- `Q:`
  - 可以使⽤锂电池或者两节 AA 纽扣电池直接给 ESP8266 供电吗？

- `A:`
  - 两节 AA 纽扣电池可以给 ESP8266 供电。锂电池放电时压降 ⽐较 ⼤，不适合直接给 ESP8266 供电。ESP8266 的 RF 电路会受温度及电压浮动影响。不推荐不加任何校准的电源直接给 ESP8266 供电，推荐使 ⽤ DC-DC 或者 LDO 给 ESP8266 供电。

## SPI Flash 上电

- `Q:`
  - SPI Flash 上电时，是否有特殊要求？

- `A:`
  - SPI Flash ⽤于存储⽤户的程序和数据。为了保证兼容性，SPI Flash 的电压应该和 GPIO 的电压相匹配。

## ESP8266 的 RAM 使用结构  

- `Q:`
  - ESP8266 的 RAM 的使⽤结构是怎样的？

- `A:`
  - ESP8266 的 RAM 总共 160KB。
  1. IRAM 空间为 64KB：
  32KB ⽤作 IRAM，⽤来存放没有加 ICACHE_FLASH_ATTR 的代码，即 .text 段，会通过 ROM code 或⼆级 boot 从 SPI Flash 中的 BIN 中加载到 IRAM 后，32KB 被映射作为 iCache，放在 SPI Flash 中的，加了 ICACHE_FLASH_ATTR 的代码会被从 SPI Flash ⾃动动态加载到 iCache。
  2. DRAM 空间为 96KB：
  对于 Non-OS_SDK，前 80KB ⽤来存放 .data/.bss/.rodata/heap，heap 区的⼤⼩取决于 .data/.bss/.rodata 的⼤⼩；还有 16KB 给 ROM code 使⽤。
  对于 RTOS_SDK，96KB ⽤来存放 .data/.bss/.rodata/heap，heap 区的⼤⼩取决于.data/.bss/.rodata 的⼤⼩。 

## GPIO 直接连 5V

- `Q:`
  - GPIO 可以直接连 5V吗？

- `A:`
  - 不可以。GPIO 只能承受 3.6V，需要通过降压电路，否则会造成 GPIO 损坏。
