# ESP32 系列

## 编译相关

### IRAM 内存不足

- `Q:`
  - 设备编译出现 IRAM 内存不足，超过 n 字节。

- `A:`
  - 简单方法,配置 GCC 优化选项，既可以优化 IRAM 有可以优化 flash 。推荐使用该方法。
  
    ``` shell
    make menuconfig-->Compiler options → Optimization Level -->(X) Optimize for size (-Os)
    ```

  - 复杂方法，修改 ld 文件以及系统文件
    - `components/esp32/ld/esp32.ld 文件修改`
  
    ``` c
    /* IRAM for PRO cpu. Not sure if happy with this, this is MMU area... */
    /* iram0_0_seg (RX) :                 org = 0x40080000, len = 0x20000 */
    /* 修改增加 8K */

    iram0_0_seg (RX) :                 org = 0x40080000, len = 0x22000
    ```

    - `components/soc/esp32/include/soc/soc.h 文件修改`

    ``` c
    //#define SOC_IRAM_HIGH           0x400A0000
    // 修改 IRAM 增加 8K
    #define SOC_IRAM_HIGH           0x400A2000

    //#define SOC_DIRAM_IRAM_LOW    0x400A0000
    //修改DRAM 减少 8K

    #define SOC_DIRAM_IRAM_LOW    0x400A2000
    ```
