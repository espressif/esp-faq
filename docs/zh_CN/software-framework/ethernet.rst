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

ESP32 以太网开发板示例出现 "emac: Reset EMAC Timeout" 有哪些原因？
-------------------------------------------------------------------------

  此 log 为 EMAC 初始化超时，与 RMII 时钟有关，建议排查硬件问题，查看 PHY 晶振是否虚焊等。

--------------

ESP32 外接 LAN8720，GPIO0 对其提供 CLK，Ethernet 例程初始化出错。如何解决？
--------------------------------------------------------------------------------

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

    ELF file SHA256: ``597d55ebf237c1cffa5f47c73148a159b22726d94a7b78100bd941d7d5fc906e``

    Backtrace: 0x40083cdc:0x3ffb5e80 0x40084143:0x3ffb5ea0 0x400d32c1:0x3ffb5ec0 0x400d1742:0x3ffb5f20 0x40085d91:0x3ffb5f40
    0x40083cdc: invoke_abort at /mnt/hgfs/workspace/esp32/IDF/esp-idf-v3.3/components/esp32/panic.c:715

    0x40084143: _esp_error_check_failed at /mnt/hgfs/workspace/esp32/IDF/esp-idf-v3.3/components/esp32/panic.c:721

    0x400d32c1: app_main at /mnt/hgfs/workspace/esp32/project/ethernet/main/ethernet_example_main.c:153 (discriminator 1)

    0x400d1742: main_task at /mnt/hgfs/workspace/esp32/IDF/esp-idf-v3.3/components/esp32/cpu_start.c:542

    0x40085d91: vPortTaskWrapper at /mnt/hgfs/workspace/esp32/IDF/esp-idf-v3.3/components/freertos/port.c:403


    Rebooting...

  - 请检查 IO0 上是否有电容。作为 CLK 输出 pin 的时候最好 IO0 上没有接电容，这会影响时序。
  - GPIO0 输出 RMII 时钟切记在 Kconfig 中要勾选 ``CONFIG_PHY_CLOCK_GPIO0_OUT``。
  - 另外，以太网部分除了可以参考 example 中的 README 讲解，也可以参阅官方文档 `API 参考 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/network/esp_eth.html>`_。

--------------

使用 ESP-IDF 中的 Ethernet 示例时，出现错误代码 "Timed out waiting for PHY register 0x3 to have value 0xc0f0 (mask 0xfff0). Current value 0xffff"，请问该如何解决？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 请参考：`BBS issue <https://www.esp32.com/viewtopic.php?f=12&t=6322&p=27381#p27381>`_ 与 `Github issue <https://github.com/espressif/esp-idf/pull/1127#issuecomment-340727923>`_。
  - 读 PHY 寄存器值为 0xFFFF 时，通常情况可以这样排查：

      a. 检查 MDIO 和 MDC 的接线是否错误
      b. 检查 RMII 需要的 50 MHz 时钟是否正常
      c. 检查 PHY 地址是否配置正确（包括软件和硬件）
      
  - 强烈建议检查一遍控制 PHY 地址的 strap 引脚，保证其不要悬空，**不要默认**！确保这些 strap 引脚已经被外部电阻上拉或者下拉了。
  - 如果还是不够确定 PHY 地址究竟是多少，可以在软件中尝试设置 PHY 地址从 0 开始到 31，然后读取 PHY ID 寄存器，看看是否能够读到正常的数据，如果正确，记录下当前 PHY 地址。


--------------

使用 ESP-IDF v4.1，ESP32 Ethernet 如何设置静态 IP？
---------------------------------------------------------------------------

  由于 ESP-IDF v4.1 以及以上版本会摒弃掉 tcp/ip 的接口，推荐使用 `ESP-NETIF <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_netif.html>`_ 的接口。

  参考示例代码如下：

  .. code-block:: c

    {
        ...
        esp_netif_config_t cfg = ESP_NETIF_DEFAULT_ETH();
        esp_netif_t *eth_netif = esp_netif_new(&cfg);
        // Set default handlers to process TCP/IP stuffs
        ESP_ERROR_CHECK(esp_eth_set_default_handlers(eth_netif));
        ...
        char* ip= "192.168.5.241";
        char* gateway = "192.168.5.1";
        char* netmask = "255.255.255.0";
        esp_netif_ip_info_t info_t;
        memset(&info_t, 0, sizeof(esp_netif_ip_info_t));

        if (eth_netif)
        {
            ESP_ERROR_CHECK(esp_netif_dhcpc_stop(eth_netif));
            info_t.ip.addr = esp_ip4addr_aton((const char *)ip);
            info_t.netmask.addr = esp_ip4addr_aton((const char *)netmask);
            info_t.gw.addr = esp_ip4addr_aton((const char *)gateway);
            esp_netif_set_ip_info(eth_netif, &info_t);
        }
        ...
    }

--------------

ESP32-Ethernet-Kit 开发板模组替换成 ESP32-WROOM-32D 以太网功能是否存在影响？
-----------------------------------------------------------------------------------------

  - ESP32-Ethernet-Kit 上的 ESP32-WROVER-B 可以更换成 ESP32-WROOM-32D，且以太网功能不受影响。
  - ESP32-WROOM 和 ESP32-WROVER 系列模组最大的区别是：ESP32-WROVER 带有 4 MB PSRAM，而 ESP32-WROOM 默认没有 PSRAM。请参考：

     - `ESP32-WROOM-32D 技术规格书 <https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32d_esp32-wroom-32u_datasheet_cn.pdf>`_
     - `ESP32-WROVER-B 技术规格书 <https://www.espressif.com/sites/default/files/documentation/esp32-wrover-b_datasheet_cn.pdf>`_

  - ESP32-WROOM 和 ESP32-WROVER 模组都使用的是 ESP32 芯片，ESP32 芯片支持以太网，详情可以参考 `ESP32 技术规格书 <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf>`_。
  - 相关文档：`ESP32-Ethernet-Kit 入门指南 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/hw-reference/esp32/get-started-ethernet-kit.html>`_。

------------------

使用 ESP32 设计自行开发以太网的板子，下载官方 esp-idf/examples/ethernet 例程，报错如下，是什么原因？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    E (5556) emac: Timed out waiting for PHY rdgister 0x2 to have value 0x0022 (mask 0xffff). Current value 0xffff
    E (6556) emac: Timed out waiting for PHY register 0x3 to have value 0x1430 (mask 0xfff0). Current value 0xffff 

  - 此报错说明硬件电路有问题，RMII 时钟没有正常供给 PHY，遇到读 PHY 寄存器失败。关于 RMII 时钟部分，可参见 `说明 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/network/esp_eth.html>`_。
  
----------------

ESP32 以太网支持 MII 接口吗？
------------------------------------------------------------------------------------------------------------------------------------------------------

  - 硬件支持，软件正在适配中，用户自行实现可参考 `Ethernet doc <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/network/esp_eth.html>`_。 

--------------------------------

ESP32-S2 是否可以外接以太网？ 
------------------------------------------------------------------------

  - 可以，目前 ESP-IDF 已经提供了 DM9051 模块的驱动，该模块内部集成以太网的 MAC 和 PHY 功能，可以和 MCU 之间通过 SPI 接口进行通讯。DM9051 上集成了 MAC+PHY 的模块，请参考 `参考示例 <https://github.com/espressif/esp-idf/tree/master/examples/ethernet/>`_ 以及 `使用说明 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32s2/api-reference/network/index.html#id1>`_。

---------------------

ESP32 是否支持 EMAC 与 SPI 以太网模块同时使用？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 支持，ESP32 可同时使用 EMAC 和一至两个 SPI 以太网模块。可基于 `esp-idf/examples/ethernet/basic <https://github.com/espressif/esp-idf/tree/master/examples/ethernet/basic>`_ 例程在 menuconfig 中同时开启 PHY 和 SPI 以太网进行测试。

---------------------

如何诊断 ESP32 快速以太网传输中的数据包延迟问题？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  可以在 ESP-IDF 库中的 ``ethernetif.c`` 文件里添加调试打印，重点检查 TCP 序列号和确认号 (ACK)，确定延迟是否来自以太网层或 LWIP 层。
