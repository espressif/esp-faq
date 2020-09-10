BLE & BT
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