Bluetooth LE & Bluetooth
============================

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

When porting example gatt_server, an error occurred indicating head file does not exist. What could be the reasons?
---------------------------------------------------------------------------------------------------------------------------------------

  When porting example gatt_server, an error occurred as ``fatal error: esp_gap_ble_api.h: No such file or directory``, but this file is already included in the head file.

  - Check sdkconfig to see whether sdkconfig.defaults is ported from the example or not. By default, Bluetooth® is disabled in SDK and needs to be enabled manually.
  - If you are using cmake, the link configurations in the CMakeLists.txt file should be copied from the example too.

--------------

Does ESP32 support Bluetooth 5.0?
---------------------------------------------

  No, the ESP32 hardware only supports Bluetooth LE 4.2.

  The ESP32 has passed the Bluetooth LE 5.0 certification, but some of its functions are still not supported on ESP32 (there will be a future chip which supports all functions in Bluetooth LE 5.0).

--------------

After the Bluetooth® LE starts advertising, why some mobile phones cannot successfully scan them?
------------------------------------------------------------------------------------------------------------------------

  - Please check whether your mobile phone supports Bluetooth LE function. Some mobile phones, such as iPhones, display Classic Bluetooth only in “Settings” -> “Bluetooth” (by default), and the Bluetooth LE advertisement will be filtered out.
  - It is recommended to use a dedicated Bluetooth LE application to debug the Bluetooth LE function. For example, LightBlue application can be used on iPhone.
  - Please check whether the advertising packet conforms to the specified format. Mobile phones tend to filter out packets that do not conform to the specified format and display only the correct ones.

--------------

Can I process OTA through Bluetooth® on ESP32?
-------------------------------------------------------------------

  Yes, please operate basing on `bt\_spp\_acceptor <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/classic_bt/bt_spp_acceptor>`_ and `bt\_spp\_initiator <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/classic_bt/bt_spp_initiator>`_.

  If using Bluetooth LE, please operate basing on `ble\_spp\_server <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/ble/ble_spp_server>`_ and `ble\_spp\_client <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/ble/ble_spp_client>`_.

--------------

How do ESP32 Bluetooth® and Bluetooth® LE dual-mode coexist and how can I use this coexistence mode?
---------------------------------------------------------------------------------------------------------------------------------------

  The ESP32 Bluetooth and Bluetooth LE dual-mode does not require complex configurations. For developers, it is simple as calling Bluetooth LE API for Bluetooth LE, and calling Classic Bluetooth API for Classic Bluetooth.

  For specifications on Classic Bluetooth and Bluetooth LE coexistence, please refer to `ESP32 BT&BLE Dual-mode Bluetooth <https://www.espressif.com/sites/default/files/documentation/btble_coexistence_demo_en.pdf>`_.

--------------

What is the throughput of ESP32 Bluetooth® LE?
------------------------------------------------------------

  - The throughput of ESP32 Bluetooth LE depends on various factors such as environmental interference, connection interval, MTU size, and the performance of peer devices.
  - The maximum throughput of Bluetooth LE communication between ESP32 boards can reach up to 700 Kbps, which is about 90 KB/s. For details, please refer to example ble_throughput in ESP-IDF.

--------------

Does ESP32 support Bluetooth® 4.2 DLE (Data Length Extension)？
----------------------------------------------------------------------------

  Yes, Bluetooth 4.2 DLE is supported in all versions of ESP-IDF. There is no sample code provided currently. You can implement this by calling corresponding APIs directly. Please refer to `esp_ble_gap_set_pkt_data_len <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/esp_gap_ble.html?highlight=esp_ble_gap_set_pkt_data_len#_CPPv428esp_ble_gap_set_pkt_data_len13esp_bd_addr_t8uint16_t>`_.

--------------

How do ESP32 Bluetooth® and Wi-Fi coexist?
----------------------------------------------------

  In the ``menuconfig``, there is a special option called ``Software controls WiFi/Bluetooth coexistence``, which is used to control the coexistence of Bluetooth and Wi-Fi for ESP32 using software, thus balancing the coexistence requirement for controlling the RF module by both the Wi-Fi and Bluetooth modules.

  - Please note that if ``Software controls WiFi/Bluetooth coexistence`` is enabled, the Bluetooth LE scan interval shall not exceed ``0x100 slots`` (about 160 ms). If the Bluetooth LE and Wi-Fi coexistence is required, this option can be enabled or disabled. However, if this option is not enabled, please note that the Bluetooth LE scan window should be larger than 150 ms, and the Bluetooth LE scan interval should be less than 500 ms.
  - If the Classic Bluetooth and Wi-Fi coexistence is required, it is recommended to enable this option.

--------------

How can I get ESP32 Bluetooth® Compatibility Test Report?
----------------------------------------------------------------

  Please contact sales@espressif.com.

--------------

What is the transmit power of ESP32 Bluetooth®?
---------------------------------------------------------

  The ESP32 Bluetooth has 8 transmit power levels, corresponding to -12 ~ 9 dBm of transmit power, with a 3 dBm interval. The controller software limits the transmit power and selects the power level according to the corresponding power level declared by the product.

--------------

Could ESP32 realize bridging between Wi-Fi and Bluetooth® LE?
------------------------------------------------------------------------

  Yes, this function is developed on the application layer. You can retrieve data through Bluetooth LE and send them out via Wi-Fi. For detailed information, please refer to `Wi-Fi and Bluetooth LE Coexist demo <https://github.com/espressif/esp-idf/tree/release/v4.0/examples/bluetooth/esp_ble_mesh/ble_mesh_wifi_coexist>`_.

--------------

What is the operating current of ESP32 Bluetooth® LE?
------------------------------------------------------------------

  +---------------------------------------------------------------+---------------+---------------+----------------+
  | Current                                                       | MAX (mA)      | Min (mA)      | Average (mA)   |
  +===============================================================+===============+===============+================+
  | Advertising: Adv Interval = 40 ms                             | 142.1         | 32            | 42.67          |
  +---------------------------------------------------------------+---------------+---------------+----------------+
  | Scanning: Scan Interval = 160 ms, Window = 20 ms              | 142.1         | 32            | 44.4           |
  +---------------------------------------------------------------+---------------+---------------+----------------+
  | Connection(Slave): Connection Interval = 20 ms, latency = 0   | 142.1         | 32            | 42.75          |
  +---------------------------------------------------------------+---------------+---------------+----------------+
  | Connection(Slave): Connection Interval = 80 ms, latency = 0   | 142.1         | 32            | 35.33          |
  +---------------------------------------------------------------+---------------+---------------+----------------+

--------------

What kinds of Bluetooth® LE profiles does ESP32 support?
-------------------------------------------------------------------

  Currently, ESP32 Bluetooth LE fully supports some basic profiles, such as GATT/SMP/GAP, as well as some self-defined profiles. The ones that have already been implemented include Bluetooth LE HID (receiving side), Bluetooth LE SPP-Like, Battery, DIS, BluFi (Bluetooth Network Configuration-transmitting side), and so on.

--------------

How do I connect mobile phones and play music using ESP32 Bluetooth®?
--------------------------------------------------------------------------------

  ESP32 is used as an A2DP receiver when connected to a cell phone to play music. Please note that the A2DP Sink Demo uses a mobile phone to obtain SBC encoded data stream only. In order to play sounds, you will also need to decode the data and some peripherals, including codec modules, D/A converter, and speaker.

--------------

How is the ESP32 SPP performance?
------------------------------------------------

  When we use two ESP32 boards to run SPP, one-way throughput can reach up to 1900 Kbps (about 235 KB/s), which is close to the theoretical value in the specifications.

--------------

What is the maximum transmission rate for ESP32 Bluetooth® LE?
--------------------------------------------------------------------------

  The transmission rate of ESP32 Bluetooth LE can reach 700 Kbps when it is tested in a shielded box.

--------------

How does ESP32 Bluetooth® LE enter Light-sleep mode?
--------------------------------------------------------------

  On the hardware level, a 32 kHz external crystal should be added, or the Light-sleep mode will not take effect.

  On the software level (SDK4.0 and later versions), the following configurations should be enabled in menuconfig:

  - Power Management:| ``menuconfig`` > ``Component config`` > ``Power management`` > ``[*] Support for power management``

  - Tickless Idle:| ``menuconfig`` > ``Component config`` > ``FreeRTOS`` > ``[*] Tickless idle support (3) Minimum number of ticks to enter sleep mode for (NEW)``

  .. note:: Tickless idle needs to be enabled to allow automatic light-sleep mode. FreeRTOS will enter Light-sleep mode if no tasks need to run for 3 ticks (by default), that is 30 ms if tick rate is 100 Hz. Configure the FreeRTOS tick rate to be higher if you want to allow shorter duration of light-sleep mode, for example: ``menuconfig > ``Component config`` > ``FreeRTOS`` > ``(1000) Tick rate (Hz)``.

  - | Configure external 32.768 kHz crystal as RTC clock source :| ``menuconfig`` > ``Component config`` > ``ESP32-specific`` > ``RTC clock source (External 32 kHz crystal)[*] Additional current for external 32 kHz crystal``

  .. note:: The "additional current" option is a workaround for a hardware issue on ESP32 that the crystal can fail in oscillating. Please enable this option when you use external 32 kHz crystal. This hardware issue will be resolved in the next chip revision.

  - | Enable Bluetooth modem sleep with external 32.768kHz crystal as low power clock :| ``menuconfig`` > ``Component config`` > ``Bluetooth`` > ``Bluetooth controller`` > ``MODEM SLEEP Options`` > ``[*] Bluetooth modem sleep``

--------------

Are there any documentation references for ESP32 BluFi networking?
---------------------------------------------------------------------------------

  For BluFi networking, please refer to `ESP32 Blufi <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/blufi.html?highlight=blufi>`_. For BluFi networking examples, please refer to `Blufi <https://github.com/espressif/esp-idf/tree/v4.4.2/examples/bluetooth/blufi>`_.

--------------

What is the maximum transmission rate for ESP32 Classic Bluetooth® SPP?
-------------------------------------------------------------------------------------

  In an open environment, the transmission rate for ESP32 Classic Bluetooth SPP can reach 1400+ Kbps ~ 1590 Kbps (only for reference, please do tests based on your actual application environment) with bi-directional transmitting and receiving simultaneously.

--------------

Is ESP32 Bluetooth® compatible to Bluetooth® ver2.1 + EDR protocol?
-----------------------------------------------------------------------------

  Yes. The ESP32 Bluetooth is downward-compatible, you can do tests using our official `Bluetooth examples <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth>`_.

--------------

How many Bluetooth® clients can be connected to ESP32?
--------------------------------------------------------------------

  The Bluetooth LE server supports up to nine client connections, please check the configuration of parameter ble_max_conn for applications. For stable connection, three clients should be good.

--------------

How can I get the MAC address of Bluetooth® devices for ESP32?
------------------------------------------------------------------

  You can get the MAC address configured by Bluetooth via API `esp_bt_dev_get_address(void); <https://github.com/espressif/esp-idf/blob/f1b8723996d299f40d28a34c458cf55a374384e1/components/bt/host/bluedroid/api/include/api/esp_bt_device.h#L33>`_, also the system pre-defined MAC address types via API `esp_err_t esp_read_mac(uint8_t* mac,esp_mac_type_ttype); <https://github.com/espressif/esp-idf/blob/6c17e3a64c02eff3a4f726ce4b7248ce11810833/components/esp_system/include/esp_system.h#L233>`_.

--------------

What is the default Bluetooth® transmit power for ESP32 SDK?
------------------------------------------------------------------------

  - By default, the power level of ESP32 SDK is 5, and the corresponding transmit power is +3 dBm.
  - The power level of ESP32 Bluetooth ranges from 0 to 7, with the corresponding transmit power ranges from -12 dBm to 9 dBm. Each time the power level increases by 1, the corresponding transmit power will increase by 3 dBm.

--------------

Is it possible to use Wi-Fi Smartconfig and Bluetooth® LE Mesh for ESP32 simultaneously?
--------------------------------------------------------------------------------------------------

  It is not recommended to use them simultaneously.

  - The Smartconfig will need to receive the networking data, thus occupying the antenna all the time. If it is used together with Bluetooth LE Mesh, there will be an extremely high rate of failure.
  - The Bluetooth LE Mesh can be used together with BluFi. So it is recommended to use BluFi for networking.

--------------

What is the operating current for ESP32 Classic Bluetooth®？
------------------------------------------------------------------------

  A2DP (Single core CPU 160 Mhz，DFS = false，commit a7a90f)

  +--------------------------------------------------------------+---------------+---------------+--------------+
  | Current                                                      | Maximum (mA)  | Minimum (mA)  | Average (mA) |
  +==============================================================+===============+===============+==============+
  | Scanning                                                     | 106.4         | 30.8          | 37.8         |
  +--------------------------------------------------------------+---------------+---------------+--------------+
  | Sniff                                                        | 107.6         | 31.1          | 32.2         |
  +--------------------------------------------------------------+---------------+---------------+--------------+
  | Play Music                                                   | 123           | 90.1          | 100.4        |
  +--------------------------------------------------------------+---------------+---------------+--------------+

------------

How can I modify the transmit power of Bluetooth® for ESP32 series chips？
--------------------------------------------------------------------------------

  For ESP32/ESP32-S3/ESP32-C3, the Bluetooth transmit power can be configured via function esp_ble_tx_power_set(). For details, please refer to `esp_bt.h <https://github.com/espressif/esp-idf/blob/c77c4ccf6c43ab09fd89e7c907bf5cf2a3499e3b/components/bt/include/esp_bt.h>`_.
  For ESP32-C6/ESP32-C2/ESP32-H2, you can set the transmit power by calling the `esp_ble_tx_power_set_enhanced() <https://github.com/espressif/esp-idf/blob/b3f7e2c8a4d354df8ef8558ea7caddc07283a57b/components/bt/include/esp32h4/include/esp_bt.h#L139>`__ API.
  For Classic Bluetooth, use `esp_bredr_tx_power_set() <https://github.com/espressif/esp-idf/blob/b3f7e2c8a4d354df8ef8558ea7caddc07283a57b/components/bt/include/esp32/include/esp_bt.h#L336>`__ for setting the transmit power.

--------------

How is the networking compatibility of ESP32 Bluetooth® LE? Is it open-sourced?
--------------------------------------------------------------------------------------------

  - ESP32 Bluetooth networking, BluFi networking for short, has a good compatibility as Bluetooth LE and is compatible with many mainstream mobile phones such as Apple, HUAWEI, Mi, OPPO, MEIZU, OnePlus, ZTE and etc.
  - Currently, the BluFi protocol and phone application code is open-sourced.

--------------

When I execute example bt_spp_acceptor on ESP32, the IOS device cannot find the ESP32 device during scanning. What could be the reasons?
---------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Apple has opened Bluetooth® as: A2DP, HID's keyboard, avrcp, SPP (need MFI), high-level Bluetooth LE and ANCS for Bluetooth LE.
  - If the IOS device expects to communicate with the end device via SPP, the SPP of the end device should have the MFI certificate. However, ESP32 SPP does not have the MFI certificate, thus the IOS device cannot find ESP32 during scanning.

--------------

How is the security of ESP32 Bluetooth® LE/Bluetooth® Secure Simple Pairing (SSP) compared to legacy pairing?
-----------------------------------------------------------------------------------------------------------------------------

  - Secure Simple Pairing (SSP) is more secure than legacy pairing.
  - The legacy pairing uses symmetric encryption algorithm, while Secure Simple Pairing (SSP) uses asymmetric cryptography algorithm.

--------------

How can I confirm the MTU size of ESP32 Bluetooth® LE?
------------------------------------------------------------------

  - By default, the MTU size of ESP32 Bluetooth LE is 23 bytes, and can be configured to reach 517 bytes.
  - For phones, the MTU size can be self-defined. Then, the end device with a smaller MTU will be chosen for communication.

--------------

When advertising in ESP32 Bluetooth® LE mode, an error occurred as "W (17370) BT_BTM: data exceed max adv packet length". How can I resolve such issue?
----------------------------------------------------------------------------------------------------------------------------------------------------------------

  - This is because the advertising data has exceeded the maximum advertising packet length.
  - The maximum data length of advertising payload is 31 bytes. If the actual data length exceeds 31 bytes, the Bluetooth protocol stack will drop some data and generate an error warning.
  - If the data to be advertised exceeds the maximum packet length, the extra data can be put in the scan response packet.

--------------

Does ESP32 Bluetooth® LE support Client-Server mode, in which gatt server and gatt client can coexist?
-----------------------------------------------------------------------------------------------------------------------------------

  - Yes, please refer to example `gattc_gatts_coex <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/coex/gattc_gatts_coex>`_.

--------------

What are the risks if there are over six devices connected to ESP32 Bluetooth® LE?
---------------------------------------------------------------------------------------------

  - Usually it depends on the specific application scenario. In general, the ESP32 Bluetooth LE can communicate stably with three devices connected.
  - There is no exact number for maximum Bluetooth LE connections. When there are multiple devices connected to Bluetooth LE simultaneously, the RF is time-multiplexed, thus requiring the designer to ensure that each device is not overly occupied, causing other devices to timeout and disconnected.
  - The connection parameters include: connection interval, connection window, latency and timeout. It is ok for devices to not respond within the ``latency``, but if the responding time exceeds ``timeout`` threshold, the device will be disconnected.
  - If the ``interval`` is configured to 100 and ``window`` to 5, the Bluetooth LE will be able to connect to more devices with Wi-Fi disconnected. However, If Wi-Fi is connected and the value of ``interval`` is too small, only a few devices can be connected.
  - When the Bluetooth LE supports multiple devices connected simultaneously, there will be bigger possibility for RF solt management to generate error. So when there are multiple connections for Bluetooth LE, it is necessary to debug for different scenarios.

----------------

When using ESP32 device as the server of Bluetooth® LE, how many client devices can be connected?
---------------------------------------------------------------------------------------------------------------------

  - The ESP32 Bluetooth LE supports up to nine client devices for connection. It is recommended to hold this number within three.
  - Please make configurations via ``menuconfig`` > ``Component config`` > ``Bluetooth`` > ``Bluetooth controller`` > ``BLE MAX Connections``.

----------------

How can I send files via Bluetooth® BR/EDR for ESP32?
------------------------------------------------------------

  - Please refer to example ``bt_spp_acceptor`` or ``bt_spp_initiator`` in `classic bt <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/classic_bt>`_.

---------------

When I download example ESP_SPP_SERVER for ESP32, how can I modify the name of the Bluetooth® device?
------------------------------------------------------------------------------------------------------------------

  - The name of the Bluetooth device can be modified via ``adv`` parameter:

  .. code-block:: text

    static const uint8_t spp_adv_data[23] = {
      0x02,0x01,0x06,
      0x03,0x03,0xF0,0xAB,
      0x0F,0x09,0x45,0x53,0x50,0x5f,0x53,0x50,0x50,0x5f,0x53,0x45,0x52,0x56,0x45,0x52};

  - The "0x0F" in the third line means the length of the following data is 15, "0x09" stands for data type (fixed) and data from "0x45" indicates the corresponding ASCII code of the device names (BLE_SPP_SERVER by default).

----------------------

When I use the "BluFi" example to configure network for ESP32, the Wi-Fi cannot be connected during the distribution process via the EspBluFi application since a wrong Wi-Fi has been configured. Then the device is restarted after sending a SCAN command from the application. What is the reason?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The "BluFi" example stipulates that Wi-Fi "SCAN" commands cannot be sent when Wi-Fi is connected.
  - To solve this issue, you can add ``ESP_ERROR_CHECK(esp_wifi_disconnect());`` to the first line of the ``ESP_BLUFI_EVENT_GET_WIFI_LIST:{};`` function under the ``blufi_example_main.c`` file.

-------------------

How can I specify a BLE connection/transmit operation to run on core 0 when I use ESP32?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Currently, ESP32's BLE connection/transmit operation only can be run on core 1. You can enable this via ``menuconfig`` > ``Component config`` > ``FreeRTOS`` > ``Run FreeRTOS only on first core`` .
  - Based on the application requirements, you can use the `xTaskCreatePinnedToCore()` or `xTaskCreateStaticPinnedToCore()` API to create and allocate tasks. For detailed instructions, refer to `Creating Tasks <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/freertos_idf.html#creation>`__.

--------------

When I set name for the bluetooth of an ESP32 device using Chinese characters, messy code shows instead. What is the reason？
----------------------------------------------------------------------------------------------------------------------------------------

  - This is because the Chinese encoding format of the editor is not UTF-8 at this time, and the encoding format of the editor needs to be changed to UTF-8.

----------------

When I upload sub-packages to the Bluetooth channel using ESP32, the maximum transmission data length of a packet is 253 (MTU is set to 263). This results in slower transmission when a large number of data packets are transmitted for multi-packet reading. Is there a BluFi extension protocol that can support the transmission of a larger length of data in one packet, or are there other solutions to increase the transmission rate?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The transmission is slow When a large number of data packets on the Bluetooth channel are transmitted for multi-packet reading. You can improve the transmission speed by adjusting the Bluetooth connection parameters.
  - The BLE packet length setting depends on the ``ESP_GATT_MAX_MTU_SIZE`` setting, please refer to the `Description <https://github.com/espressif/esp-idf/blob/cf056a7d0b90261923b8207f21dc270313b67456/examples/bluetooth/bluedroid/ble/gatt_client/tutorial/Gatt_Client_Example_Walkthrough.md>`_.
  - The configured MTU size will affect the data transmission rate. The effective MTU length needs to be changed by MTU exchange to change the default MTU size. The MTU size used in the final MTU exchange is used as the MTU size for the communication between the two devices. You can check the value of the MTU after exchange, such as the follows:

  .. code-block:: text

    case ESP_GATTS_MTU_EVT:
            ESP_LOGI(GATTS_TAG, "ESP_GATTS_MTU_EVT, MTU%d", param->mtu.mtu);

----------------

What profile does ESP32's classic Bluetooth® support?
-------------------------------------------------------

  - Currently, it supports A2DP, AVRCP, SPP, HFP, and HID.

----------------

How many stable connections can be reached for ESP32-C3's Bluetooth® LE (BLE)?
------------------------------------------------------------------------------------------------

  - We recommend the connection number does not exceed four.

----------------

How can I adjust the BLE advertising interval?
------------------------------------------------------------------------------------------

  - The advertising interval is decided by ``adv_int_min`` and ``adv_int_max`` parameters in BLE advertising struct, which configures the minimum and maximum advertising interval respectively.
  - The advertising interval ranges from 0x0020 to 0x4000 and the default value is 0x0800. The interval time is the value * 0.625 ms, i.e., 20 ms to 10.24 sec.
  - If the values of ``adv_int_min`` and ``adv_int_max`` are different, the advertising interval is within the range of the two values. If the values are the same, the interval will be this fixed value.

----------------

How can I input the PIN code via mobile phone during ESP32's Classic Bluetooth Pairing mode?
-----------------------------------------------------------------------------------------------------------------------------

  You can disable ``Secure Simple Pairing`` to support only ``Legacy Pairing``.

  - From esp-idf v3.3 to v4.0 (not include v4.0): ``Component config`` > ``Bluetooth`` > ``Bluedroid Enable`` > ``[*] Classic Bluetooth`` > ``[ ]Secure Simple Pairing``
  - esp-idf v4.0 and above: ``Component config`` > ``Bluetooth`` > ``Bluedroid Options`` > ``[ ] Secure Simple Pairing``

----------------

How much memory does ESP32 Bluetooth occupy?
----------------------------------------------------------------------------------------

  - Controller:

    - BLE single mode: 40 KB
    - BR/EDR single mode: 65 KB
    - Dual mode: 120 KB

  - Main equipment:

    - BLE GATT Client (Gatt Client demo): 24 KB (.bss+.data) + 23 KB (heap) = 47 KB
    - BLE GATT Server (GATT Server demo): 23 KB (.bss+.data) + 23 KB (heap) = 46 KB
    - BLE GATT Client & GATT Server: 24 KB (.bss+.data) + 24 KB (heap) = 48 KB
    - SMP: 5 KB
    - Classic Bluetooth (Classic Bluetooth A2DP_SINK demo, including SMP/SDP/A2DP/AVRCP): 48 KB (.bss+.data) + 24 KB (heap) = 72 KB (an additional 13 KB is added when the example is running)

  .. note:: The above heap (Heap) all include the task stack (Task Stack), because the task stack is allocated from the heap and considered as a heap.

  - Optimized PSRAM version:

  In ESP-IDF v3.0 and later versions, if you open the PSRAM related options of the Bluetooth menu in ``menuconfig``, and put part of the .bss/.data section and heap of Bluedroid (Host) into PSRAM, almost 50 KB memory space can be saved.

----------------------

When I use the "gattc_gatts_coex.c" example on ESP32 to test BLE multi-connection, it can only connect to four devices even after I set the ``BLE Max connections`` in ``menuconfig`` to five. What is the reason?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Please set the ``BT/BLE MAX ACL CONNECTION`` in ``menuconfig`` to five.

----------------

Does ESP32-C3 BLE support master and slave mode at the same time? What is the number of connections in master mode and slave mode?
-------------------------------------------------------------------------------------------------------------------------------------------------------------

  :IDF\: release/v4.3, master:

  - ESP32-C3 supports master and slave mode at the same time, which share 8 connections. For example, if ESP32-C3 connects to 4 slave devices, it can be connected by 8 - 4 = 4 master devices.
  - In addition, when ESP32-C3 is used as a slave, it can be connected by 8 master devices; when used as a master, it can connect to 8 slave devices.

-------------------

What is the maximum MTU Size of ESP32 Classic Bluetooth?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP32 Classic Bluetooth has two protocols, namely A2DP and SPP. The maximum MTU Size setting of BT A2DP (default) is 1008 bytes, of which the header occupies 12 bytes and the actual amount of data transmitted by the application layer is 1008 - 12 = 996 (bytes); the maximum MTU Size of BT SPP (default) Set to 990 bytes.

---------------

How can I resolve the frequently occurred ELxXX error (such as ELx200) when Wi-Fi and Ble co-exit？
-----------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32:

  - It has been fixed in commit 386a8e37f19fecc9ef62e72441e6e1272fa985b9. Please switch to the corresponding commit to test.

---------------

How does BLE capture packets?
--------------------------------------------------------------------------------------------------------------------------------

  - There are many available tools, such as:

    - TI Packet sniffer
    - NRF Packet sniffer

---------------------

When I use an ESP32 development board to test several versions of bluefi example under ESP-IDF for networking, the following error kept printing. What is the reason?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    E (117198) BT_L2CAP: l2ble_update_att_acl_pkt_num not found p_tcb
    W (117198) BT_BTC: btc_blufi_send_encap wait to send blufi custom data

  - When this error occurs, please modify the ``esp_ble_get_cur_sendable_packets_num(blufi_env.conn_id)`` to ``esp_ble_get_sendable_packets_num()`` in the ``components/bt/host/bluedroid/btc/profile/esp/blufi/blufi_prf.c`` file.
  - This bug has been fixed in all branches, you can update ESP-IDF to the latest release version.

--------------------

When I use ESP32, can Light-sleep mode be enabled for Bluetooth and can Bluetooth be kept connected in Light-sleep mode?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - To use Light-sleep mode for ESP32, release/4.0 or above versions of ESP-IDF and a 32.768 kHz crystal are needed.
  - Bluetooth can be kept connected in Light-sleep mode. Please refer to `Bluetooth modem sleep with external 32.768 kHz xtal under light sleep <https://github.com/espressif/esp-idf/issues/947#issuecomment-500312453>`_.

--------------

How can I modify the Bluetooth device name of ESP32?
---------------------------------------------------------------------------------------

  - The structure to be modified is as follows:

    .. code-block:: text

      static uint8_t raw_adv_data[] = {

              /* flags*/

              0x02, 0x01, 0x06,

              Tx power*/

              0x02, 0x0a, 0xeb,

              /* service uuid*/

              0x03, 0x03, 0xFF, 0x00,

              /* device name*/

              0x0f, 0x09,'E','S','P','_','G','A','T','T','S','_','D','E ','M','O'

      };

  - The above ``/* device name*/`` is the modified item. Among them, 0x0f is the total length of the field type plus specific content, and 0x09 indicates that this type refers to the device name. Subsequent'E','S','P','_','G','A','T','T','S','_','D','E', 'M','O' are the ASCII code of the broadcast device name.

----------------

What is the maximum supported broadcast length of BLE 5.0 broadcast after it is set to legacy mode?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The maximum supported length is 31-byte.

---------------

How can I set a BLE broadcast package as unconnectable package?
--------------------------------------------------------------------------------------------------

  :CHIP\: ESP32:

  - please reffer to the `gatt_server demo <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/ble/gatt_server>`_，and set adv_type as ADV_TYPE_NONCONN_IND.

    .. code:: text

      static esp_ble_adv_params_t adv_params = {
        .adv_int_min        = 0x20,
        .adv_int_max        = 0x40,
        .adv_type           = ADV_TYPE_NONCONN_IND,
        .own_addr_type      = BLE_ADDR_TYPE_PUBLIC,
        //.peer_addr            =
        //.peer_addr_type       =
        .channel_map        = ADV_CHNL_ALL,
        .adv_filter_policy = ADV_FILTER_ALLOW_SCAN_ANY_CON_ANY,
        }

---------------

How can I send Bluetooth HCI commands directly to ESP32-WROOM-32D module through the serial port?
--------------------------------------------------------------------------------------------------------

  - Please refer to `controller_hci_uart_esp32 <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/hci/controller_hci_uart_esp32>`_.
  - When ESP32 is used as a controller, and the other device serves as a host, HCI commands can be sent to ESP32 via UART.

--------------

Does ESP32 support transmitting audio stream using A2DP?
----------------------------------------------------------------------------

  Yes, please refer to example `a2dp_source <https://github.com/espressif/esp-idf/tree/d85d3d969ff4b42e2616fd40973d637ff337fae6/examples/bluetooth/bluedroid/classic_bt/a2dp_source>`_.

--------------------

How many devices can be connected at the most as suggested by the White List of ESP32 Bluetooth LE?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The maximum supported number is 12.

----------------

Can ESP32 Bluetooth LE use PSRAM?
-------------------------------------------------------------------

  To enable Bluetooth LE to use PSRAM, please go to ``Component config`` > ``Bluetooth`` > ``Bluedroid Options`` and enable `BT/BLE will first malloc the memory from the PSRAM <https://docs.espressif.com/projects/esp-idf/en/release-v4.4/esp32/api-reference/kconfig.html?highlight=config_bt_allocation_from_spiram_first#config-bt-allocation-from-spiram-first>`_。

-------------

When using ESP32-C3 BLE Scan, can I set it to only scan the Long Range devices?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes, you can make tests based on `esp-idf/examples/bluetooth/bluedroid/ble_50/ble50_security_client <https://github.com/espressif/esp-idf/tree/release/v5.0/examples/bluetooth/bluedroid/ble_50/ble50_security_client>`_. By changing the configuration `.cfg_mask = ESP_BLE_GAP_EXT_SCAN_CFG_UNCODE_MASK | ESP_BLE_GAP_EXT_SCAN_CFG_CODE_MASK` in `ext_scan_params <https://github.com/espressif/esp-idf/blob/7f4bcc36959b1c483897d643036f847eb08d270e/examples/bluetooth/bluedroid/ble_50/ble50_security_client/main/ble50_sec_gattc_demo.c#L58>`_ to `.cfg_mask = ESP_BLE_GAP_EXT_SCAN_CFG_CODE_MASK`, you can scan the broadcast packets whose primary PHY type is LE CODED PHY.

--------------

Is there a limit to the name length of ESP32 as a Bluetooth device?
------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The names should be no longer than 248 bytes. However, in practice, the name length is also limited by the length of Bluetooth advertising packets. For the description of configurations, please refer to `CONFIG_BT_MAX_DEVICE_NAME_LEN <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v5.0/esp32/api-reference/kconfig.html#config-bt-max-device-name-len>`__.

--------------

How do I set the ESP32 BLE Scan to the permanent scan without generating a timeout?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - You can realize this by setting "duration" to 0 before using the `esp_ble_gap_start_scanning() <https://github.com/espressif/esp-idf/blob/490216a2ace6dc3e1b9a3f50d265a80481b32f6d/examples/bluetooth/bluedroid/ble/gatt_client/main/gattc_demo.c#L324>`__ function to start BLE Scan.

------------------

How can I get RSSI of BLE devices through ESP32?
-------------------------------------------------------------------------------------------------------------------------------------------------------------

  - You can use the `esp_ble_gap_read_rssi() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/esp_gap_ble.html#_CPPv421esp_ble_gap_read_rssi13esp_bd_addr_t>`__ function to get RSSI of connected BLE devices.
  - If you want to get RSSI of all scanned BLE devices around, please use the `ble_scan_result_evt_param <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/esp_gap_ble.html#_CPPv4N22esp_ble_gap_cb_param_t8scan_rstE>`__ structure in the ESP_GAP_BLE_SCAN_RESULT_EVT event to enable the printing of RSSI.

----------------

How can I increase the transmission distance of BLE5.0? How can I set BLE5.0 to long-range mode?
--------------------------------------------------------------------------------------------------------------------------------

  - In practice, the transmission distance of BLE5.0 is about 200 m. It is recommended to refer to the actual test distance. ESP32-S3 supports the features of BLE5.0, and supports long-range communication through Coded PHY (125 Kbps and 500 Kbps) and broadcast extension.
  - You can realize long-range communication by using 125 Kbps Coded PHY and increasing the transmit power (tx_power). Refer to the following settings:

    .. code:: text

      esp_ble_gap_ext_adv_params_t ext_adv_params_coded = {
        .type = ESP_BLE_GAP_SET_EXT_ADV_PROP_SCANNABLE,
        .interval_min = 0x50,
        .interval_max = 0x50,
        .channel_map = ADV_CHNL_ALL,
        .filter_policy = ADV_FILTER_ALLOW_SCAN_ANY_CON_ANY,
        .primary_phy = ESP_BLE_GAP_PHY_CODED,
        .max_skip = 0,
        .secondary_phy = ESP_BLE_GAP_PHY_CODED,
        .sid = 0,
        .scan_req_notif = false,
        .own_addr_type = BLE_ADDR_TYPE_RANDOM,
        .tx_power = 18,
      };

  - For the BLE5.0 examples, please refer to `ble_50 examples <https://github.com/espressif/esp-idf/tree/v4.4.4/examples/bluetooth/bluedroid/ble_50>`__ in ESP-IDF.

------------------

I have changed the name of the Bluetooth device with `esp_ble_gap_set_device_name() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/api-reference/bluetooth/esp_gap_ble.html#_CPPv427esp_ble_gap_set_device_namePKc>`_ in ESP32-C3. It works for Android devices and the customized device name can be shown. However, it does not work on IOS devices. The device name is still the default Bluetooth name. How can I make it work on Apple devices as well?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - In this case, you need to use raw data to create BLE advertising packets. First, enable the ``CONFIG_SET_RAW_ADV_DATA`` option in ``menuconfig`` (``idf.py menuconfig`` > ``Example 'GATT SERVER' Config`` > ``Use raw data for advertising packets and scan response data``), and then customize `Broadcast packet structure <https://github.com/espressif/esp-idf/blob/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_server/main/gatts_demo.c#L77>`__ in the `gatt server example <https://github.com/espressif/esp-idf/blob/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_server>`__.
  - Please use nRF Connect APP to test. We have tested and it works on the nRF connect APP. This issue is related to IOS APPs.

------------------

I want to use two ESP32 development boards to test the Bluetooth connection. How can I set the specified key to automatically connect them with `gatt_security_client <https://github.com/espressif/esp-idf/tree/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_security_client>`__ and `gatt_security_server <https://github.com/espressif/esp-idf/tree/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_security_server>`__ examples?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - In `gatt_security_client <https://github.com/espressif/esp-idf/tree/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_security_client>`__ and `gatt_security_server <https://github.com/espressif/esp-idf/tree/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_security_server>`__ examples, the default key is 123456. For details, please refer to `uint32_t passkey = 123456 <https://github.com/espressif/esp-idf/blob/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_security_server/main/example_ble_sec_gatts_demo.c#L561>`__. You can also set other passwords.
  - Since the ESP32 device has no display or input keyboard by default, the example sets the IO capability to `No output No input <https://github.com/espressif/esp-idf/blob/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_security_server/main/example_ble_sec_gatts_demo.c#L556>`__. For more details, please refer to `Gatt Security Server Example Walkthrough <https://github.com/espressif/esp-idf/blob/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_security_server/tutorial/Gatt_Security_Server_Example_Walkthrough.md>`__.
  - To manually input the key, please set `esp_ble_io_cap_t iocap <https://github.com/espressif/esp-idf/blob/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_security_server/main/example_ble_sec_gatts_demo.c#L556>`__ in the `gatt_security_server <https://github.com/espressif/esp-idf/tree/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_security_server>`__ example to ESP_IO_CAP_OUT mode, and then you can use the nRF Connect APP to establish a connection with the BLE Server.

------------------

After setting `gatt_security_server <https://github.com/espressif/esp-idf/tree/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_security_server>`__ to ESP_IO_CAP_OUT mode and setting `gatt_security_client <https://github.com/espressif/esp-idf/tree/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_security_client>`__ to ESP_IO_CAP_OUT mode, I deliberately set the wrong passkey. However, the two development boards can still be connected. What is the reason?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - When the server is set to ESP_IO_CAP_OUT mode, gatt_security_client should be set to ESP_IO_CAP_IN mode.
  - To avoid such a situation, please add the following code into the `case ESP_GAP_BLE_PASSKEY_REQ_EVT <https://github.com/espressif/esp-idf/blob/v4.4.4/examples/bluetooth/bluedroid/ble/gatt_security_client/main/example_ble_sec_gattc_demo.c#_L386>`__ event on the gatt_security_client side:

    .. code:: text

      esp_ble_passkey_reply(param->ble_security.ble_req.bd_addr, true, 123457);

------------------

Does ESP32-C3/ESP32-C6/ESP32-S3 support Bluetooth AOA/AOD?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP32-C3/ESP32-C6/ESP32-S3 does not support Bluetooth AOA/AOD. Currently, none of Espressif products support Bluetooth AOA/AOD.

------------------

What is the maximum length of data in a BLE advertising packet supported by ESP32-C3 with the BLE5.0 feature?
---------------------------------------------------------------------------------------------------------------------------------------------------------------

  -  The maximum length is 1650 bytes, which can be set via the `esp_ble_gap_config_ext_adv_data_raw() <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v5.0/esp32c3/api-reference/bluetooth/esp_gap_ble.html#_CPPv435esp_ble_gap_config_ext_adv_data_raw7uint8_t8uint16_tPK7uint8_t>`__ API.

-----------------

Does ESP32 have any API to check whether BLE advertising has started or stopped?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - For bluedroid stack, there is no such API currently.
  - For Nimble stack (and using non-extended advertising of BLE 4.2), you can use the `ble_gap_adv_active <https://github.com/espressif/esp-nimble/blob/f8f02740acdf4d302d5c2f91ee2e34444d405671/nimble/host/include/host/ble_gap.h#L831>`_ API.

-------------------

Does ESP32 support multiple clients connecting at the same time when used as a BLE server? How to realize it?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP32 can be used as a BLE server to support multiple BLE clients to access simultaneously. Meanwhile, it can also be used as a BLE client to connect to multiple BLE servers simultaneously. The supported number of BLE stable connections is 3.
  - When used as a BLE server, you can simply enable advertising again after a client connects. Take `gatt_server_service_table <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/ble/gatt_server_service_table>`_ as an example, after receiving the ``ESP_GATTS_CONNECT_EVT`` event, please call ``esp_ble_gap_start_advertising()`` to enable advertising.
  - When used as a BLE client, please refer to `gattc_multi_connect <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/ble/gattc_multi_connect>`_.

-------------

How to set the continuous scanning time for BLE5.0?
---------------------------------------------------------------------------------------------------

  - You can use the `esp_err_t esp_ble_gap_start_ext_scan(uint32_t duration, uint16_t period); <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/bluetooth/esp_gap_ble.html?highlight=esp_ble_gap_start_ext_scan#_CPPv426esp_ble_gap_start_ext_scan8uint32_t8uint16_t>`__ API for configuration. When the period is set to 0, the duration time is the continuous scanning time.

-------------

How to set up the GATT service with a 128-bit UUID based on the `GATT Server <https://github.com/espressif/esp-idf/tree/v5.1/examples/bluetooth/bluedroid/ble/gatt_server>`_ example?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  You can refer to the following code:

    .. code:: c

      static const uint8_t pctool_service_uuid[16] = {
          0x00, 0x03, 0xcd, 0xd0, 0x00, 0x00, 0x10, 0x00, 0x80, 0x00, 0x00, 0x80, 0x5f, 0x9b, 0x01, 0x31
      };
      static const uint8_t pctool_write_uuid[16] = {
          0x00, 0x03, 0xcd, 0xd2, 0x00, 0x00, 0x10, 0x00, 0x80, 0x00, 0x00, 0x80, 0x5f, 0x9b, 0x01, 0x31
      };
      /* Full Database Description - Used to add attributes into the database */
      static const esp_gatts_attr_db_t gatt_db[HRS_IDX_NB] =
      {
          // Service Declaration
          [IDX_SVC]        =
          {
      {ESP_GATT_AUTO_RSP}, {ESP_UUID_LEN_16, (uint8_t *)&primary_service_uuid, ESP_GATT_PERM_READ,
            sizeof(pctool_service_uuid), sizeof(pctool_service_uuid), (uint8_t *)&pctool_service_uuid}
      },
          /* Characteristic Declaration */
          [IDX_CHAR_A]     =
          {
      {ESP_GATT_AUTO_RSP}, {ESP_UUID_LEN_16, (uint8_t *)&character_declaration_uuid, ESP_GATT_PERM_READ,
            CHAR_DECLARATION_SIZE, CHAR_DECLARATION_SIZE, (uint8_t *)&char_prop_read_write_notify}
      },
          /* Characteristic Value */
          [IDX_CHAR_VAL_A] =
          {
      {ESP_GATT_AUTO_RSP}, {ESP_UUID_LEN_128, (uint8_t *)&pctool_write_uuid, ESP_GATT_PERM_READ | ESP_GATT_PERM_WRITE,
            GATTS_DEMO_CHAR_VAL_LEN_MAX, sizeof(char_value), (uint8_t *)char_value}
      },
      }

------------

When testing based on the `GATT Server <https://github.com/espressif/esp-idf/tree/v5.1/examples/bluetooth/bluedroid/ble/gatt_server>`_ example, is it possible to delete the default 1800 and 1801 service attributes?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The 1800 and 1801 service attributes are two standard GATT service attributes in the BLE protocol, which cannot be deleted or disabled. They are part of the BLE protocol specifications, providing basic device information and general access capabilities, and maintaining compatibility with the standard BLE protocol.
  - 0x1800 refers to generic access, defining the general attributes of the device, while 0x1801 refers to generic attribute, a simple GATT service used to provide basic information about the device.

-----------

Is there an explanation for the BLE error codes in the ESP-IDF SDK?
----------------------------------------------------------------------------------------------

  - The BLE error codes in the ESP-IDF SDK refer to the BLE standard protocol. The corresponding error code descriptions can be found in `LIST OF BLE ERROR CODES <https://github.com/chegewara/esp32-ble-wiki/issues/5>`_.

------------

The error below occurred when setting the Bluetooth mode to ``Component config`` > ``Bluetooth`` > ``Controller Options`` > ``Bluetooth controller mode (BR/EDR/BLE/DUALMODE)`` dual mode based on the `BLE SPP Server <https://github.com/espressif/esp-idf/tree/v5.1/examples/bluetooth/bluedroid/ble/ble_spp_server>`_ example. What could be the reason for this?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    .. code:: text

      E (2906) GATTS_SPP_DEMO: spp_gatt_init enable controller failed: ESP_ERR_INVALID_ARG

  - The current reported error is due to the BLE SPP Server example releases the memory of Class Bluetooth controller by default. Please refer to the API description for `esp_bt_controller_mem_release() <https://docs.espressif.com/projects/esp-idf/en/release-v5.0/esp32/api-reference/bluetooth/controller_vhci.html#_CPPv429esp_bt_controller_mem_release13esp_bt_mode_t>`_.
  - After setting the Bluetooth Dual Mode, you need to delete `ESP_ERROR_CHECK(esp_bt_controller_mem_release(ESP_BT_MODE_CLASSIC_BT)); <https://github.com/espressif/esp-idf/blob/cbce221e88d52665523093b2b6dd0ebe3f1243f1/examples/bluetooth/bluedroid/ble/ble_spp_server/main/ble_spp_server_demo.c#L666>`_, then modify `ret = esp_bt_controller_enable(ESP_BT_MODE_BLE); <https://github.com/espressif/esp-idf/blob/cbce221e88d52665523093b2b6dd0ebe3f1243f1/examples/bluetooth/bluedroid/ble/ble_spp_server/main/ble_spp_server_demo.c#L674>`_ to ``ret = esp_bt_controller_enable(ESP_BT_MODE_BTDM);``.

-------------

Is there an example of implementing a Bluetooth LE Eddystone beacon based on ESP32?
---------------------------------------------------------------------------------------------------------------------------------

  - Currently, there is no such example. You can implement such an application by modifying the `esp-idf/examples/bluetooth/bluedroid/ble/ble_eddystone <https://github.com/espressif/esp-idf/tree/v5.1.2/examples/bluetooth/bluedroid/ble/ble_eddystone/main>`_ example and referring to `Eddystone Protocol Specification <https://github.com/google/eddystone/blob/master/protocol-specification.md>`_.
  
