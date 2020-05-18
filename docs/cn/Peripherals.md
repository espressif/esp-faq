# 驱动及外设

## ESP32 CHIP_PU 管脚实现复位功能

- `Q:`
  - ESP32 只有⼀个 CHIP_PU 管脚，没有复位管脚，该芯⽚上的 CHIP_PU 管脚可实现相同的复位功能吗？

- `A:`
  - 可以，CHIP_PU 即复位管脚。

## PWM 信号使用引脚范围

- `Q:`
  - 脉冲宽度调制（PWM）信号输出是否可以分配到除了 Flash、SD、I2S、I2C、UART 之外的任⼀ I/O 上？

- `A:`
  - PWM 可输⼊到任何管脚，除了只有输⼊功能的 I/O 之外。

## ESP32 触摸相关应⽤

- `Q:`
  - 想使⽤ ESP32 做触摸相关应⽤时，哪⾥有相关资料参考？

- `A:`
  - 请参考推荐的软硬件设计：https://github.com/espressif/esp-iot-solution/tree/master/examples/touch_pad_evb

## FRC1 和 FRC2 的寄存器产⽣ PWM

- `Q:`
  - 通过直接写硬件定时器 FRC1 的寄存器产⽣ PWM，发现初始化 Wi-Fi 时，Wi-Fi 产⽣的中断会⼲扰硬件定时器的中断，导致错误的 PWM 输出，是否可以使⽤ FRC2 产⽣ PWM？是否可以使 FRC1 的优先级⾼于 WiFi？

- `A:`
  - 不可以使⽤ FRC2，其被系统占⽤。Wi-Fi 使⽤ NMI 中断，其优先级⾼于其他普通中断，推荐使⽤ ESP8266 RTOS SDK 的 PWM 库，参考 https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/peripherals/pwm

## ESP32 LCD 显示屏示例

- `Q:`
  - 有⽆ ESP32 SPI 接 LCD 显示屏测试数据及示例？ESP32 的 SD 1bit 例程在哪⾥？

- `A:`
  - 请参考 https://github.com/espressif/esp-iot-solution/tree/master/components/spi_devices/lcd

## ADC 性能参数

- `Q:`
  - ADC 的性能参数有⼏个通道？采样率和有效位数是多少？

- `A:`
  - 请通道：1
  - 采样率：
    - 停⽌ Wi-Fi 的情况下，能达到每秒 100000 次。
    - Wi-Fi 正常⼯作的情况下，能达到每秒 1000 次。
  - 有效位数：
    - 内部 ADC 有效位数为 12 位。
    - system_adc_read() //API 返回值的有效位数是 10 位。

## ADC 寄存器 bitmap 信息

- `Q:`
  - 从哪⾥可以得到 ADC 的寄存器 bitmap 信息？

- `A:`
  - ADC 是和内部 RF 电路⾼度集成的，所以 bitmap 和寄存器信息没有公开，如有特殊需求请联系 sales@espressif.com。

## ESP8266 ADC 的精度

- `Q:`
  - ESP8266 ADC 的精度如何？

- `A:`
  - ESP8266 连接路由器后，单 STA 模式会进⼊ modem-sleep，导致芯⽚内部电流发⽣变化，参考值变化，因此 ADC 采集异常。
  ⽤户如果需要测量的⾮常准确，可以⽤ system_adc_fast_read 的函数，但是测量之前需要关闭 RF，Wi-Fi 连接会断开。如果需要测试⽐较准确，数值相差 1 或 2，可以配置 Wi-Fi 为 non-sleep 模式 wifi_set_sleep_type(NONE_SLEEP_T)；建议该⽤户这样配置。
  如果对精确性要求不⾼，可以允许模块进⼊ sleep 模式，功耗较低。

## 内部 ADC 的⽤途

- `Q:`
  - 内部 ADC 的⽤途是什么？

- `A:`
  - 内部 ADC 可以⽤于温度检测和粗略地测量外部设备电流。由于 ADC 容易受噪声影响，所以推荐只在低精度的需求时使⽤。⽐如熔断机制。

## u8 tx_addr, u8 tx_cmd, u8 tx_rep 参数

- `Q:`
  - `(u8 tx_addr, u8 tx_cmd, u8 tx_rep)` 这三个参数是什么意思？

- `A:`
  - `tx_addr` 是发送地址；
  `u8 tx_cmd` 是发送指令；
  `u8 tx_rep` 是重复发送的次数。

## ESP8266 上电出现乱码

- `Q:`
  - 为什么 ESP8266 上电时会出现乱码？如何修改波特率？

- `A:`
  - 如果使⽤的是 26MHz 晶振，ESP8266 UART0 上电后的波特率是 74880，所以上电时会有乱码。
  客户可以在 user_main.c ⾥⾯修改 UART 配置， ⽐如：

    ```c
    void ICACHE_FLASH_ATTR
    uart_init(UartBautRate uart0_br, UartBautRate uart1_br)
    {
    // rom use 74880 baut_rate, here reinitialize
    UartDev.baut_rate = uart0_br;
    uart_config(UART0);
    UartDev.baut_rate = uart1_br;
    uart_config(UART1);
    }
    ```

## SD 卡

- `Q:`
  - SDIO 是否⽀持 SD 卡？

- `A:`
  - ESP8266 是 SDIO Slave，不⽀持 SD 卡。

## SDIO 最⾼速度

- `Q:`
  - SDIO 最⾼速度能⽀持到多少？

- `A:`
  - SDIO 时钟能到 50 MHz, 理论最⾼速度是 200 Mbps。

## 上电 LED 灯闪一下

- `Q:`
  - 为什么上电时会有 LED 灯闪⼀下的情况？

- `A:`
  - 要看灯的驱动是如何设计的。如是低电平灯亮，并且在上电的时候将 IO 强制拉为低电平，那么在上电的瞬间可能会出现灯闪⼀下。是因为除了了 Flash 相关的 IO 和 GPIO4，GPIO5，其他 IO 上电后上拉默认使能。
  - 解决⽅法：
  1. 上电的瞬间，user_init 中将上拉关闭。
  2. 如第⼀条⽆效的，需要我们提供相应的 boot.bin。在该 BIN 被搬到 RAM 的过程⾥，IO 的上拉就会被关闭。这⽐ user_init ⽣效要早。

## 使用 PWM 开始有窄波

- `Q:`
  - 使⽤ PWM 时，发现最开始有窄波，是什么原因？

- `A:`
  - 这个是精度较⾼的 PWM 的调节⽅式，PWM 的精度可以达到 22222 深度。精度的调节主要靠后⾯的窄波。注意这种⽅式的 PWM Duty ⽆法配置为 100%。

## PWM 的变化缓慢

- `Q:`
  - 发现 PWM 的变化缓慢，是什么原因？

- `A:`
  - 客户采⽤了 SDK example/IOT_demo 中的渐变 API。如 light_set_aim 或 light_set_aim_r 这些 API 使⽤的是渐变⽅式。不会⽴即⽣效，需要渐变的过程。如⽤户需要 PWM Duty 设置后⽴即⽣效，需要调⽤接⼝ pwm_set_duty，需要注意调⽤ pwm_set_duty 后要调⽤ pwm_start 此次设置才能⽣效。

## GPIO 的 register 和 bitmap 信息

- `Q:`
  - 哪⾥能找到 GPIO 的 register 和 bitmap 信息？

- `A:`
  - 请[参考⽂档《ESP8266 技术参考》](https://www.espressif.com/sites/default/files/documentation/esp8266-technical_reference_cn.pdf)。

## 使能 UART 流控

- `Q:`
  - 如何使能 UART 流控？

- `A:`

  - UART 通信时，如需配置 UART 通信的数据格式，请参考 SDK/driver_lib/driver/ 路径下的 uart.c ⽂件。
  - UART 通信，如需配置硬件流控，请执⾏下⾯两个步骤：
    - 请在 uart.h 中将下⾯的宏置 true

    ``` c
    #define UART_HW_RTS 1 //set 1: enable part hw flow control RTS, PIN MTDO, FOR UART0
    #define UART_HW_CTS 1 //set1: enable usrt hw flow control CTS, PIN MTCK, FOR UART0

    ```

    - 配置硬件流控的⻔限值
      - 截图中红⾊标注部分为硬件流控的⻔限值，在 RXFIFO 中字节数⼤于 110 后，RTS 会被拉⾼。

      ```c
      if(uart_no == UART0){
          // set rx fifo trigger
          WRITE_PERI_REG(UART_CONF1(uart_no)),
          ((10 & UART_RXFIFO_FULL_THRHD) << UART_RXFIFO_FULL_THRHD_S)|
          # if UART_HW_RTS
          ((110 & UART_RX_FLOW_THRHD) << UART_RX_FLOW_THRHD_S)|
          UART_RX_FLOW_EN |  //enable rx flow control
          # endif
      }
      ```

## UART1 打印信息

- `Q:`
  - 如何配置信息打印到 UART1 上 ？

- `A:`
  - UART1 只有 Tx 功能，可以在 UART0 ⽤于通讯时，做打印 log ⽤途。请参考如下代码：

    ```c
    void ICACHE_FLASH_ATTR

    uart_init_new(void)
    {
    // Wait for FIFOs to be emptied
    UART_WaitTxFifoEmpty(UART0);
    UART_WaitTxFifoEmpty(UART1;
    // Configure UART settings
    UART_ConfigTypeDef uart_config;
    uart_config.baud_rate = BIT_RATE_74880;
    uart_config.data_bits = UART_WordLength_8b;
    uart_config.parity = USART_Parity_None;
    uart_config.stop_bits = USART_StopBits_1;
    uart_config.flow_ctrl = USART_HardwareFlowControl_None;
    uart_config.UART_RxFlowThresh = 120;
    uart_config.UART_InverseMask = UART_None_Inverse;
    UART_ParamConfig(UART0, &uart_config);
    UART_IntrConfTypeDef uart_intr;
    uart_intr.UART_IntrEnMask = UART_RXFIFO_TOUT_INT_ENA;
    UART_FRM_ERR_INT_ENA | UART_RXFIFO_FULL_INT_ENA;
    uart_intr.UART_RX_FifoFullIntrThresh = 100;
    uart_intr.UART_RX_TimeOutIntrThresh = 2;
    uart_intr.UART_TX_FifoEmptyIntrThresh = 20;
    UART_IntrConfig(UART0, &uart_intr);
    //Set UART1 for printing
    UART_SetPrintPort(UART1);
    //Register interrupt handler
    UART_intr_handler_register(uart0_rx_intr_handler);
    ETS_UART_INTR_ENABLE();
    }
    ```
