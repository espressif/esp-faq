以太网
======

:link_to_translation:`en:[English]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

--------------

ESP32 以太网开发板示例出现 ` emac:Reset EMAC Timeout` 有哪些原因？
------------------------------------------------------------------------

  此 log 为 emac 初始化超时，与 RMII 时钟有关，建议排查硬件问题，查看 PHY 晶振是否虚焊等。

--------------

ESP32 外接 LAN8720，GPIO0 对其提供 CLK ，Ethernet 例程初始化出错？
------------------------------------------------------------------

  .. code-block:: text

    I (229) cpu_start: App cpu up.
    I (247) heap_init: Initializing. RAM available for dynamic allocation:
    I (254) heap_init: At 3FFAE6E0 len 00001920 (6 KiB): DRAM
    I (260) heap_init: At 3FFB40A8 len 0002BF58 (175 KiB): DRAM
    I (266) heap_init: At 3FFE0440 len 00003AE0 (14 KiB): D/IRAM
    I (273) heap_init: At 3FFE4350 len 0001BCB0 (111 KiB): D/IRAM
    I (279) heap_init: At 400885D0 len 00017A30 (94 KiB): IRAM
    I (285) cpu_start: Pro cpu start user code
    I (303) cpu_start: Chip Revision: 1
    W (303) cpu_start: Chip revision is higher than the one configured in menuconfig. Suggest to upgrade it.
    I (307) cpu_start: Starting scheduler on PRO CPU.
    I (0) cpu_start: Starting scheduler on APP CPU.
    I (319) system_api: Base MAC address is not set, read default base MAC address from BLK0 of EFUSE
    E (1329) emac: Timed out waiting for PHY register 0x2 to have value 0x0007(mask 0xffff). Current value 0xffff
    E (2329) emac: Timed out waiting for PHY register 0x3 to have value 0xc0f0(mask 0xfff0). Current value 0xffff
    E (2329) emac: Initialise PHY device Timeout
    ESP_ERROR_CHECK failed: esp_err_t 0xffffffff (ESP_FAIL) at 0x40084140
    0x40084140: _esp_error_check_failed at /mnt/hgfs/workspace/esp32/IDF/esp-idf-v3.3/components/esp32/panic.c:720

    file: "/mnt/hgfs/workspace/esp32/project/ethernet/main/ethernet_example_main.c" line 153
    func: app_main
    expression: esp_eth_enable()

    ELF file SHA256: 597d55ebf237c1cffa5f47c73148a159b22726d94a7b78100bd941d7d5fc906e

    Backtrace: 0x40083cdc:0x3ffb5e80 0x40084143:0x3ffb5ea0 0x400d32c1:0x3ffb5ec0 0x400d1742:0x3ffb5f20 0x40085d91:0x3ffb5f40
    0x40083cdc: invoke_abort at /mnt/hgfs/workspace/esp32/IDF/esp-idf-v3.3/components/esp32/panic.c:715

    0x40084143: _esp_error_check_failed at /mnt/hgfs/workspace/esp32/IDF/esp-idf-v3.3/components/esp32/panic.c:721

    0x400d32c1: app_main at /mnt/hgfs/workspace/esp32/project/ethernet/main/ethernet_example_main.c:153 (discriminator 1)

    0x400d1742: main_task at /mnt/hgfs/workspace/esp32/IDF/esp-idf-v3.3/components/esp32/cpu_start.c:542

    0x40085d91: vPortTaskWrapper at /mnt/hgfs/workspace/esp32/IDF/esp-idf-v3.3/components/freertos/port.c:403


    Rebooting...

  - 请检查 IO0 上是否有电容, 作为 CLK 输出 pin 的时候最好 IO0 上没有接电容, 这会影响时序
  - GPIO0 输出 RMII 时钟切记在 Kconfig 中要勾选 ``CONFIG_PHY_CLOCK_GPIO0_OUT``
  - 另外，以太网部分除了可以参考 example 中的 README 讲解，也可以参阅官方的 `API Reference 文档 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_eth.html>`_

--------------

使用 idf中 的 Ethernet 示例时，出现错误代码 `Timed out waiting for PHY register 0x3 to have value 0xc0f0 (mask 0xfff0). Current value 0xffff` 请问该如何解决？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 可以参考以下这个：https://www.esp32.com/viewtopic.php?f=12&t=6322&p=27381#p27381 https://github.com/espressif/esp-idf/pull/1127#issuecomment-340727923
  - 读PHY寄存器为 0xFFFF 通常情况可以这样排查：
      a. 检查 MDIO 和 MDC 的接线是否错误
      b. 检查 RMII 需要的 50MHz 时钟是否正常
      c. 检查 PHY 地址是否配置正确（包括软件和硬件）
  - 这里强烈建议，检查一遍控制 PHY 地址的 strap 引脚，不要悬空，**不要默认**！确保这些 strap 引脚已经被外部电阻上拉或者下拉了。
  - 如果还是不够确定 PHY 地址究竟是多少，可以在软件中尝试设置 PHY 地址从 0 开始到 31，然后读取 PHY ID 寄存器，看看是否能够读到正常的数据，如果正确，记录下当前 PHY 地址。
