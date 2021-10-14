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

Does ESP32 support Bluetooth® 5.0?
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

Is it able to process OTA through Bluetooth® on ESP32?
-------------------------------------------------------------------

  Yes, please operate basing on `bt\_spp\_acceptor <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/classic_bt/bt_spp_acceptor>`_ and `bt\_spp\_initiator <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/classic_bt/bt_spp_initiator>`_. 

  If using Bluetooth LE, please operate basing on `ble\_spp\_server <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/ble/ble_spp_server>`_ and `ble\_spp\_client <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/ble/ble_spp_client>`_.

--------------

How does ESP32 Bluetooth® and Bluetooth® LE dual-mode coexist and use?
------------------------------------------------------------------------------------

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
  
  In the menuconfig, there is a special option called “Software controls WiFi/Bluetooth coexistence”, which is used to control the coexistence of Bluetooth and Wi-Fi for ESP32 using software, thus balancing the coexistence requirement for controlling the RF module by both the Wi-Fi and Bluetooth modules. Please note that if ``Software controls WiFi/Bluetooth coexistence`` is enabled, the Bluetooth LE scan interval shall not exceed ``0x100 slots`` (about 160 ms).

  - If the Bluetooth LE and Wi-Fi coexistence is required, this option can be enabled or disabled. However, if this option is not enabled, please note that the Bluetooth LE scan window should be larger than 150 ms, and the Bluetooth LE scan interval should be less than 500 ms.
  - If the Classic Bluetooth and Wi-Fi coexistence is required, it is recommended to enable this option.

--------------

How to get ESP32 Bluetooth® Compatibility Test Report?
----------------------------------------------------------------

  Please contact sales@espressif.com.

--------------

What is the transmit power of ESP32 Bluetooth®?
---------------------------------------------------------
  
  The ESP32 Bluetooth has 9 transmit power levels, corresponding to -12 ~ 12 dBm of transmit power, with a 3 dBm interval. The controller software limits the transmit power and selects the power level according to the corresponding power level declared by the product. 

--------------

Could ESP32 realize bridging between Wi-Fi and Bluetooth® LE?
------------------------------------------------------------------------

  Yes, this function is developed on application layer. Users can retrieve data through Bluetooth LE and send them out via Wi-Fi. For detailed information, please refer to `Wi-Fi and Bluetooth LE Coexist demo <https://github.com/espressif/esp-idf/tree/release/v4.0/examples/bluetooth/esp_ble_mesh/ble_mesh_wifi_coexist>`_.

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
  
  Currently, ESP32 Bluetooth LE fully supports some basic profiles, such as GATT/SMP/GAP, as well as some self-defined profiles. The ones that have already been implemented include Bluetooth LE HID (receiving side), Bluetooth LE SPP-Like, Battery, DIS, Blu-Fi (Bluetooth Network Configuration- transmitting side), and so on.

--------------

How to connect mobile phones and play music using ESP32 Bluetooth®?
--------------------------------------------------------------------------------
  
  ESP32 is used as an A2DP receiver when connected to a cell phone to play music. 

  Please note that the A2DP Sink Demo uses a mobile phone to obtain SBC encoded data stream only. In order to play sounds, you will also need to decode the data and some peripherals, including codec modules, D/A converter, and speaker.

--------------

How is the ESP32 SPP performance?
------------------------------------------------

  When using two ESP32 boards to run SPP, one-way throughput can reach up to 1900 Kbps (about 235 KB/s), which is close to the theoretical value in the specifications.

--------------

What is the maximum transmission rate for ESP32 Bluetooth® LE?
--------------------------------------------------------------------------

  The transmission rate of ESP32 Bluetooth LE can reach 800 Kbps tested in a shielded box.

--------------

How does ESP32 Bluetooth® LE enter Light-sleep mode?
--------------------------------------------------------------

  In hardware level, a 32 kHz external crystal oscillator should be added, or the Light-sleep mode will not take effect.

  In software level (SDK4.0 and later versions), the following configurations should be enabled in menuconfig:

  - Power Management:| menuconfig ---> Component config ---> Power management --->[*] Support for power management

  - Tickless Idle:| menuconfig ---> Component config ---> FreeRTOS --->[*] Tickless idle support (3) Minimum number of ticks to enter sleep mode for (NEW)

  .. note:: Tickless idle needs to be enabled to allow automatic light sleep. FreeRTOS will enter Light-sleep mode if no tasks need to run for 3 ticks (by default), that is 30 ms if tick rate is 100 Hz. Configure the FreeRTOS tick rate to be higher if you want to allow shorter duration light sleep, for example: menuconfig —> Component config —> FreeRTOS ->(1000) Tick rate (Hz).

  - | Configure external 32.768Hz crystal as RTC clock source :| menuconfig ---> Component config ---> ESP32-specific --->RTC clock source (External 32kHz crystal)[*] Additional current for external 32kHz crystal

  .. note:: The "additional current" option is a workaround for a hardware issue on ESP32 that the crystal can fail in oscillating. Please enable this option when you use external 32 kHz crystal. This hardware issue will be resolved in the next ECO chip.

  - | Enable Bluetooth modem sleep with external 32.768kHz crystal as low power clock :| menuconfig ---> Component config ---> Bluetooth ---> Bluetooth controller ---> MODEM SLEEP Options --->[*] Bluetooth modem sleep

--------------

Are there any documentation references for ESP32 BluFi networking?
---------------------------------------------------------------------------------

  For BluFi networking, please refer to `ESP32 Blufi <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/blufi.html?highlight=blufi>`_. For BluFi networking examples, please refer to `Blufi <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/ble/blufi>`_.

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

How to get the MAC address of Bluetooth® devices for ESP32?
------------------------------------------------------------------

  You can get the MAC address configured by Bluetooth via API `esp_bt_dev_get_address(void); <https://github.com/espressif/esp-idf/blob/f1b8723996d299f40d28a34c458cf55a374384e1/components/bt/host/bluedroid/api/include/api/esp_bt_device.h#L33>`_, also the system pre-defined MAC address types via API `esp_err_t esp_read_mac(uint8_t* mac,esp_mac_type_ttype); <https://github.com/espressif/esp-idf/blob/6c17e3a64c02eff3a4f726ce4b7248ce11810833/components/esp_system/include/esp_system.h#L233>`_.

--------------

What is the default Bluetooth® transmit power for ESP32 SDK?
------------------------------------------------------------------------

  - By default, the power level of ESP32 SDK is 4, and the corresponding transmit power is 0 dBm.
  - The power level of ESP32 Bluetooth ranges from 0 to 7, with the corresponding transmit power ranges from -12 dBm to 9 dBm. Each time the power level increases 1, the corresponding transmit power will increase by 3 dBm.

--------------

Is it possible to use Wi-Fi Smartconfig and Bluetooth® LE Mesh for ESP32 simultaneously?
--------------------------------------------------------------------------------------------------

  It is not recommended to use them simultaneously.
  
  - The Smartconfig will need to receive the networking data, thus occupying the antenna all the time. If it is used together with Bluetooth LE Mesh, there will be an extremely high rate of failure.
  - The Bluetooth LE Mesh can be used together with Blufi. So it is recommended to use Blufi for networking.

--------------

What is the operating current for ESP32 Classic Bluetooth®？
------------------------------------------------------------------------

  A2DP (Single core CPU 160 Mhz，DFS = false，commit a7a90f)

  +--------------------------------------------------------------+---------------+---------------+----------+
  | Current                                                      | Maximum (mA)  | Minimum (mA)  | Average  |
  +==============================================================+===============+===============+==========+
  | Scanning                                                     | 106.4         | 30.8          | 37.8     |
  +--------------------------------------------------------------+---------------+---------------+----------+
  | Sniff                                                        | 107.6         | 31.1          | 32.2     |
  +--------------------------------------------------------------+---------------+---------------+----------+
  | Play Music                                                   | 123           | 90.1          | 100.4    |
  +--------------------------------------------------------------+---------------+---------------+----------+

------------

How to modify the transmit power for ESP32 Bluetooth®？
-------------------------------------------------------------------

  The Bluetooth transmit power can be configured via function esp_ble_tx_power_set();. Please refer to `esp_bt.h <https://github.com/espressif/esp-idf/blob/c77c4ccf6c43ab09fd89e7c907bf5cf2a3499e3b/components/bt/include/esp_bt.h>`_.

--------------

How is the networking compatibility of ESP32 Bluetooth® LE? Is it open-sourced?
--------------------------------------------------------------------------------------------

  - ESP32 Bluetooth networking, Blu-Fi networking for short, has a good compatibility as Bluetooth LE and is compatible with many mainstream mobile phones such as Apple, HUAWEI, Mi, OPPO, MEIZU, OnePlus, ZTE and etc.
  - Currently, the Blu-Fi protocol and phone application code is not open-sourced.

--------------

When executing example bt_spp_acceptor on ESP32, the IOS device cannot find the ESP32 device during scanning. What could be the reasons?
---------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Apple has opened Bluetooth® as: A2DP, HID's keyboard, avrcp, SPP (need MFI), high-level Bluetooth LE and ANCS for Bluetooth LE.
  - If the IOS device expects to communicate with the end device via SPP, the SPP of the end device should have the MFI certificate. However, ESP32 SPP does not have the MFI certificate, thus the IOS device cannot find ESP32 during scanning.

--------------

How is the security of ESP32 Bluetooth® LE/Bluetooth® Secure Simple Pairing (SSP) compared to legacy pairing?
-----------------------------------------------------------------------------------------------------------------------------

  - Secure Simple Pairing (SSP) is more secure than legacy pairing.
  - The legacy pairing uses symmetric encryption algorithm, while Secure Simple Pairing (SSP) uses asymmetric cryptography algorithm.

--------------

How to certify the MTU size of ESP32 Bluetooth® LE?
------------------------------------------------------------------

  - By default, the MTU size of ESP32 Bluetooth LE is 23 bytes, and can be configured to reach 517 bytes.
  - For phones, the MTU size can be self-defined. Then, the end device with a smaller MTU will be chose for communication.

--------------

When advertising in ESP32 Bluetooth® LE mode, an error occurred as "W (17370) BT_BTM: data exceed max adv packet length". How to resolve such issue?
----------------------------------------------------------------------------------------------------------------------------------------------------------------

  - This is because the advertising data has exceeded the maximum advertising packet length.
  - The maximum data length of advertising payload is 31 bytes. If the actual data length exceeds 31 bytes, the Bluetooth protocol stack will drop some data and generate an error warning.
  - If the data to be advertised exceeds the maximum packet length, the extra data can be put in the scan response packet.

--------------

Does ESP32 Bluetooth® LE support Client-Server mode, in which gatt server and gatt client can coexist?
-----------------------------------------------------------------------------------------------------------------------------------

  - Yes, please refer to example `gattc_gatts_coex <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/coex/gattc_gatts_coex>`_.

--------------

What are the risks if there are over 6 devices connected to ESP32 Bluetooth® LE?
---------------------------------------------------------------------------------------------

  - Usually it depends on the specific application scenario. In general, the ESP32 Bluetooth LE can communicate stably with 3 devices connected.
  - There is no exact number for maximum Bluetooth LE connections. When there are multiple devices connected to Bluetooth LE simultaneously, the RF is time-multiplexed, thus requiring the designer to ensure that each device is not overly occupied, causing other devices to timeout and disconnected.
  - The connection parameters include: connection interval, connection window, latency and timeout. It is ok for devices to not respond within the ``latency``, but if the responding time exceeds ``timeout`` threshold, the device will be disconnected.
  - If the ``interval`` is configured to 100 and ``window`` to 5, the Bluetooth LE will be able to connect to more devices with Wi-Fi disconnected. However, If Wi-Fi is connected and the value of ``interval`` is too small, only a few devices can be connected.
  - When the Bluetooth LE supports multiple devices connected simultaneously, there will be bigger possibility for RF solt management to generate error. So when there are multiple connections for Bluetooth LE, it is necessary to debug for different scenarios.

----------------

When using ESP32 device as the server of Bluetooth® LE, how many client devices can be connected?
---------------------------------------------------------------------------------------------------------------------

  - The ESP32 Bluetooth LE supports up to 9 client devices for connection. It is recommended to hold this number within 3.
  - Please make configurations via menuconfig -> Component config -> Bluetooth -> Bluetooth controller -> BLE MAX Connections.

----------------

How to send files via Bluetooth® BR/EDR for ESP32?
------------------------------------------------------------

  - Please refer to example ``bt_spp_acceptor`` or ``bt_spp_initiator`` in `classic bt <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/classic_bt>`_.

---------------

When downloading example ESP_SPP_SERVER for ESP32, how to modify the name of the Bluetooth® device?
------------------------------------------------------------------------------------------------------------------

  - The name of the Bluetooth device can be modified via ``adv`` parameter:

  .. code-block:: text

    static const uint8_t spp_adv_data[23] = {
      0x02,0x01,0x06,
      0x03,0x03,0xF0,0xAB,
      0x0F,0x09,0x45,0x53,0x50,0x5f,0x53,0x50,0x50,0x5f,0x53,0x45,0x52,0x56,0x45,0x52};

  - The "0x0F" on the third line means the length of the following data is 15, "0x09" stands for data type (fixed) and data from "0x45" indicates the corresponding ASCII code of the device names (BLE_SPP_SERVER by default).
  
