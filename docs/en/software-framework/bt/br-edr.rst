Classic Bluetooth
===================

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

Can I process OTA through Classic Bluetooth® on ESP32?
-------------------------------------------------------------------

  Yes, please operate basing on `bt\_spp\_acceptor <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/classic_bt/bt_spp_acceptor>`_ and `bt\_spp\_initiator <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/classic_bt/bt_spp_initiator>`_.

--------------

How do I connect mobile phones and play music using ESP32 Bluetooth®?
--------------------------------------------------------------------------------

  ESP32 is used as an A2DP receiver when connected to a cell phone to play music. Please note that the A2DP Sink Demo uses a mobile phone to obtain SBC encoded data stream only. In order to play sounds, you will also need to decode the data and some peripherals, including codec modules, D/A converter, and speaker.

--------------

What is the maximum transmission rate for ESP32 Classic Bluetooth® SPP?
-------------------------------------------------------------------------------------

  In an open environment, the transmission rate for ESP32 Classic Bluetooth SPP can reach 1400+ Kbps ~ 1590 Kbps (only for reference, please do tests based on your actual application environment) with bi-directional transmitting and receiving simultaneously.

--------------

Is ESP32 Bluetooth® compatible to Bluetooth® ver2.1 + EDR protocol?
-----------------------------------------------------------------------------

  Yes. The ESP32 Bluetooth is downward-compatible, you can do tests using our official `Bluetooth examples <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth>`_.

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

How can I modify the transmit power of Classic Bluetooth® for ESP32 series chips？
---------------------------------------------------------------------------------------------

  Use `esp_bredr_tx_power_set() <https://github.com/espressif/esp-idf/blob/b3f7e2c8a4d354df8ef8558ea7caddc07283a57b/components/bt/include/esp32/include/esp_bt.h#L336>`__ for setting the transmit power.

--------------

When I execute example bt_spp_acceptor on ESP32, the IOS device cannot find the ESP32 device during scanning. What could be the reasons?
---------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Apple has opened Bluetooth® as: A2DP, HID's keyboard, avrcp, SPP (need MFI), high-level Bluetooth LE and ANCS for Bluetooth LE.
  - If the IOS device expects to communicate with the end device via SPP, the SPP of the end device should have the MFI certificate. However, ESP32 SPP does not have the MFI certificate, thus the IOS device cannot find ESP32 during scanning.

----------------

How can I send files via Bluetooth® BR/EDR for ESP32?
------------------------------------------------------------

  - Please refer to example ``bt_spp_acceptor`` or ``bt_spp_initiator`` in `classic bt <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/classic_bt>`_.

----------------

What profile does ESP32's classic Bluetooth® support?
-------------------------------------------------------

  - Currently, it supports A2DP, AVRCP, SPP, HFP, and HID.

----------------

How can I input the PIN code via mobile phone during ESP32's Classic Bluetooth Pairing mode?
-----------------------------------------------------------------------------------------------------------------------------

  You can disable ``Secure Simple Pairing`` to support only ``Legacy Pairing``.

  - From esp-idf v3.3 to v4.0 (not include v4.0): ``Component config`` > ``Bluetooth`` > ``Bluedroid Enable`` > ``[*] Classic Bluetooth`` > ``[ ]Secure Simple Pairing``
  - esp-idf v4.0 and above: ``Component config`` > ``Bluetooth`` > ``Bluedroid Options`` > ``[ ] Secure Simple Pairing``

-------------------

What is the maximum MTU Size of ESP32 Classic Bluetooth?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP32 Classic Bluetooth has two protocols, namely A2DP and SPP. The maximum MTU Size setting of BT A2DP (default) is 1008 bytes, of which the header occupies 12 bytes and the actual amount of data transmitted by the application layer is 1008 - 12 = 996 (bytes); the maximum MTU Size of BT SPP (default) Set to 990 bytes.

--------------

Does ESP32 support transmitting audio stream using A2DP?
----------------------------------------------------------------------------

  Yes, please refer to example `a2dp_source <https://github.com/espressif/esp-idf/tree/d85d3d969ff4b42e2616fd40973d637ff337fae6/examples/bluetooth/bluedroid/classic_bt/a2dp_source>`_.

----------------

Does ESP32 Classic Bluetooth support AVRCP 1.5 or AVRCP 1.6?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  AVRCP 1.5 is now supported on esp-idf v5.0.4 and later versions, while AVRCP 1.6 (deprecated) is not supported. For more details, please refer to `esp-idf/components/bt/host/bluedroid/stack/avrc/avrc_sdp.c <https://github.com/espressif/esp-idf/blob/8fbf4ba6058bcf736317d8a7aa75d0578563c38b/components/bt/host/bluedroid/stack/avrc/avrc_sdp.c#L55C35-L55C40>`__.
