# 芯片功能对比

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## ESP32 单核与双核的区别？

> 单核与双核的区别有哪些？从编程开发⽅式、性能表现、功耗表现等⽅⾯列举⼀下。

- ESP32 单核与双核主要差异是多了⼀个独⽴核⼼， 可以把⼀些实时性⾼的操作放在独⽴的⼀个核⼼上。
- 编程⽅式⼀致， 单核芯片需要配置 freertos 运⾏在单核上。示例： `make menuconfig-->Component config → FreeRTOS -> [*] Run FreeRTOS only on first core`
- 性能表现仅在⾼负载运算时有差异，若⽆⼤量计算差异使⽤上⽆明显差异（ 例如 AI 算法， ⾼实时性中断 ）。
- 功耗⽅⾯仅在 modem-sleep 的时候会有细微差别，详情可参考芯⽚⼿册。

---

## ESP32 E03 版本芯⽚在使⽤上和之前芯⽚软件使⽤上有什么区别呢？

- 软件上使⽤⽆区别，是可以兼容之前的固件的，硬件上修复了⼀些bug，具体的可以参考该⽂档：https://www.espressif.com/sites/default/files/documentation/ESP32_ECO_V3_User_Guide__CN.pdf

---

## ESP32 的 GPIO34 ~ GPIO39 管脚是否只能设置为输入模式？

ESP32 的 GPIO34 ~ GPIO39 只能设置为输入模式，没有软件上拉或下拉功能，不能设置为输出模式，参见[说明](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/peripherals/gpio.html?highlight=gpio34#gpio-rtc-gpio)。
