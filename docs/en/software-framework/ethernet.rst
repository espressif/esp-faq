Ethernet
========

:link_to_translation:`zh_CN:[中文]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

--------------

When building an example on ESP32 Ethernet development board, an error occurred as "emac: Reset EMAC Timeout". What could be the reasons?
----------------------------------------------------------------------------------------------------------------------------------------------------------

  This is because the EMAC initialization is timeout, and is possibly related to the RMII clock. It is recommended to check your hardware, e.g., see if the PHY crystal oscillator is a cold joint.

--------------

When ESP32 connected to LAN8720 externally, with GPIO0 providing CLK, the initialization of Ethernet example failed. How to resolve such issue?
--------------------------------------------------------------------------------------------------------------------------------------------------------------

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

  - Please check if there are capacitors on IO0. It is better to have no capacitors on IO0 when it is used as the CLK output pin, or it would affect the timing.
  - When GPIO0 starts to output RMII clock, please remember to check the ``CONFIG_PHY_CLOCK_GPIO0_OUT`` option in Kconfig.
  - For references about Ethernet, besides the README in example, you can also refer to `API Reference <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_eth.html>`_.

--------------

When using the Ethernet example in ESP-IDF, an error occurred as "Timed out waiting for PHY register 0x3 to have value 0xc0f0 (mask 0xfff0). Current value 0xffff". How to resolve such issue?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Please refer to `BBS issue <https://www.esp32.com/viewtopic.php?f=12&t=6322&p=27381#p27381>`_ and `Github issue <https://github.com/espressif/esp-idf/pull/1127#issuecomment-340727923>`_.
  - When the value of the PHY register is 0xFFFF, please check the following:

      a. If the wiring of MDIO and MDC is correct
      b. If the 50 MHz clock required by RMII is normal
      c. If the address of PHY (both software and hardware) is correctly configured
      
  - It is strongly recommended to check the strapping pins that control the PHY address to make sure they are not floating and **not in the default state**. Please make sure they have already been pulled up or down by external resistance.
  - If you are still not sure about the PHY address, you can try to set the PHY address from 0 to 31, and read the PHY ID register to see if you can get the correct data. If yes, then write down the current PHY address.


--------------

When using ESP-IDF v4.1, how to set the static IP for ESP32 Ethernet?
------------------------------------------------------------------------------------

  Since v4.1 and later versions of ESP-IDF will remove the tcp/ip interface, it is recommended to use the `ESP-NETIF <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_netif.html>`_ interface.

  Code example:

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

Is there any impact on Ethernet functionality if replacing the module of ESP32-Ethernet-Kit with ESP32-WROOM-32D?
--------------------------------------------------------------------------------------------------------------------------------

  - The ESP32-WROVER-B of ESP32-Ethernet-Kit can be replaced with ESP32-WROOM-32D, and its Ethernet functionality will not be affected.
  - The main difference between ESP32-WROOM and ESP32-WROVER module series: ESP32-WROVER modules have a 4 MB PSRAM while ESP32-WROOM modules do not have any PSRAM by default. Please refer to:

     - `ESP32-WROOM-32D Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32d_esp32-wroom-32u_datasheet_en.pdf>`_
     - `ESP32-WROVER-B Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32-wrover-b_datasheet_en.pdf>`_

  - The ESP32-WROOM and ESP32-WROVER modules all use the ESP32 chip as their core, which supports Ethernet. For more information, please refer to `ESP32 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_.
  - Related document: `ESP32-Ethernet-Kit Getting Started Guide <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/esp32/get-started-ethernet-kit.html>`_.

--------------------

When using ESP32 to design a self-developed Ethernet board, after downloaded the official esp-idf/examples/ethernet example, errors are reported as follows, what is the reason?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    E (5556) emac: Timed out waiting for PHY rdgister 0x2 to have value 0x0022 (mask 0xffff). Current value 0xffff
    E (6556) emac: Timed out waiting for PHY register 0x3 to have value 0x1430 (mask 0xfff0). Current value 0xffff 

  - This error indicates something is wrong with your hardware circuit. The RMII clock is not working normally with the PHY, causing the PHY failed to read registers. For the more information about RMII clock, please refer to `Instructions <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_eth.html>`_.
  
----------------

Does ESP32 Ethernet support MII interface?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Supported on hardware level, software adaptation is in development. Please refer to `Ethernet doc <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_eth.html>`_ for self implementation. 

--------------------------------

Is it possible to connect ESP32-S2 to Ethernet externally? 
------------------------------------------------------------------------

  - Yes, ESP-IDF currently provides drivers for the DM9051 module, which has integrated Ethernet MAC and PHY functionality and can communicate with the MCU via the SPI interface. The DM9051 has an integrated MAC+PHY module, please refer to `example reference <https://github.com/espressif/esp- idf/tree/master/examples/ethernet/> `_ and `API reference <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32s2/api-reference/network/index.html#id1>`_.

------------

Do the ESP32 series chips support to use EMAC and SPI-Ethernet modules simultaneously?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes. ESP32 series chips support to use EMAC and one or two SPI-Ethernet modules simultaneously. You can start PHY and SPI-Ethernet modules simultaneously in menuconfig to test by referring to the example `esp-idf/examples/ethernet/basic <https://github.com/espressif/esp-idf/tree/master/examples/ethernet/basic>`_.

---------------------

How to diagnose packet delay issues in ESP32 Fast Ethernet transmission?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Please add debug prints in ``ethernetif.c`` file in the ESP-IDF repository, focusing on checking the TCP sequence number and acknowledgment number (ACK), to help determine whether the delay comes from the Ethernet layer or the LWIP layer.
