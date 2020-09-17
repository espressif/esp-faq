Bluetooth® LE & Bluetooth®
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

Does ESP32 support Bluetooth® 5.0?
--------------------------------------

  No, the ESP32 hardware only supports Bluetooth® LE 4.2.

  The ESP32 has passed the Bluetooth® LE 5.0 certification, but some of its functions are still not supported on ESP32 (there will be a future chip which supports all functions in Bluetooth® LE 5.0).

--------------

Is it able to process OTA through Bluetooth on ESP32?
---------------------------------------------------------

  Yes, please operate basing on `bt\_spp\_acceptor <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/classic_bt/bt_spp_acceptor>`_ and `bt\_spp\_initiator <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/classic_bt/bt_spp_initiator>`_ if using Bluetooth®; and basing on `ble\_spp\_server <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/ble/ble_spp_server>`_ and `ble\_spp\_client <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/ble/ble_spp_client>`_ is using Bluetooth® LE.

--------------

Could ESP32 realize bridging between Wi-Fi and Bluetooth® LE?
----------------------------------------------------------------

  Yes, this function is developed on application layer. Users can retrieve data through Bluetooth® LE and send them out via Wi-Fi. For detailed information, please refer to `Wi-Fi and Bluetooth® LE Coexist demo <https://github.com/espressif/esp-idf/tree/release/v4.0/examples/bluetooth/esp_ble_mesh/ble_mesh_wifi_coexist>`_.

--------------

After the Bluetooth® LE starts broadcasting, why some mobile phones cannot successfully scan broadcasts?
----------------------------------------------------------------------------------------------------------

  - Please check whether your mobile phone supports Bluetooth® LE function. Some mobile phones, such as iPhones, display Classic Bluetooth only in “Settings” -> “Bluetooth” (by default), and the Bluetooth® LE broadcast will be filtered out by the mobile phone. 
  - It is recommended to use a dedicated Bluetooth® LE application to debug the Bluetooth® LE function. For example, LightBlue application can be used on iPhone.
  - Please check whether the broadcast packet conforms to the specified format. Mobile phones tend to filter out packets that do not conform to the specified format and display only the correct ones.

--------------

What is ESP32 Bluetooth® LE throughput?
------------------------------------------
  - ESP32's Bluetooth® LE throughput depends on various factors such as environmental interference, connection interval, MTU size, and the performance of peer devices. 
  - The maximum throughput of Bluetooth® LE communication between ESP32 boards can reach up to 700 Kbps, which is about 90 KB/s. For details, please refer to ble_throughput example in IDF.

--------------

How do ESP32 Bluetooth and Wi-Fi coexist?
--------------------------------------------
  In the menuconfig menu, there is a special option called “Software controls WiFi / Bluetooth coexistence”, which is used to control the ESP32's Bluetooth and Wi-Fi coexistence using software, thus balancing the coexistence requirement for controlling the RF module by both the Wi-Fi and Bluetooth modules. Please note that if ``Software controls WiFi/Bluetooth coexistence`` is enabled, the Bluetooth® LE scan interval shall not exceed ``0x100 slots`` (about 160 ms).

  - If the Bluetooth® LE and Wi-Fi coexistence is required, this option can be enabled or disabled. However, if this option is not enabled, please note that the “Bluetooth® LE scan interval - Bluetooth® LE scan window” should be larger than 150 ms, and the Bluetooth® LE scan interval should be less than 500 ms.
  - If the Classic Bluetooth and Wi-Fi coexistence is required, it is recommended that you enable this option.


--------------

What is the transmit power of ESP32 Bluetooth®?
-------------------------------------------------
  ESP32 Bluetooth has 9 transmit power levels, corresponding to -12 ~ 12 dBm, with a 3 dBm interval. The controller software limits the transmit power and selects the power level according to the corresponding power level declared by the product. 

--------------

What is ESP32 Bluetooth® LE operating current?
------------------------------------------------

+---------------------------------------------------------------+---------------+---------------+----------------+
| Current                                                       | MAX (mA)      | Min (mA)      | Average (mA)   |
+===============================================================+===============+===============+================+
| Advertising: Adv Interval = 40 ms                             | 142.1         | 32            | 42.67          |
+---------------------------------------------------------------+---------------+---------------+----------------+
| Scanning: Scan Interval = 160 ms, Window = 20 ms              | 142.1         | 32            | 44.4           |
+---------------------------------------------------------------+---------------+---------------+----------------+
| Connection(Slave): Connection Interval = 20 ms, Iatency = 0   | 142.1         | 32            | 42.75          |
+---------------------------------------------------------------+---------------+---------------+----------------+
| Connection(Slave): Connection Interval = 80 ms, Iatency = 0   | 142.1         | 32            | 35.33          |
+---------------------------------------------------------------+---------------+---------------+----------------+

--------------

What Bluetooth® LE profiles does ESP32 support?
--------------------------------------------------
  At the moment, ESP32 Bluetooth® LE fully supports some basic profiles, such as GATT/SMP/GAP, and some self-defined profiles. The ones that have already been implemented include Bluetooth® LE HID (receiving side), Bluetooth® LE SPP-Like, Battery, DIS, Blu-Fi (Bluetooth Network Configuration- transmitting side), and so on.

--------------

How to connect mobile phones and play music using ESP32 Bluetooth®?
--------------------------------------------------------------------
  ESP32 is used as A2DP receiver when connected to a cell phone to play music. 

  Please note that the A2DP Sink Demo uses a mobile phone to obtain SBC encoded data stream only. In order to play sounds, you will also need to decode the data and some peripherals, including codec modules, D/A converter, and speaker.

--------------

What is the SPP performance of ESP32?
----------------------------------------

  Using two ESP32 boards to run SPP, one-way throughput can reach up to 1900 Kbps (about 235 KB/s), which is close to the theoretical value in the specification.
