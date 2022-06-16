BLE Mesh development framework
================================

:link_to_translation:`zh_CN:[中文]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>
   
----------------

What is the maximum data transmission load for Bluetooth® LE (BLE) mesh?
--------------------------------------------------------------------------------

  - Up to 384 bytes for the single packet in application layer, up to 11 bytes in the bottom layer with no sub-packages.

----------------

Could you provide an example of networking through ESP32 BLE-Mesh? What APP can be used for BLE-Mesh networking?
-------------------------------------------------------------------------------------------------------------------------

  - Please use example `onoff_server <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/esp_ble_mesh/ble_mesh_node/onoff_server>`_，and use nRF Mesh APP for mobile phones.
  - For the network configuration process, please refer to `Getting Started with ESP-BLE-MESH <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/esp-ble-mesh/ble-mesh-index.html#getting-started-with-esp-ble-mesh>`__.
  
----------------

For unprovisioned device in BLE-MESH, the default name is ESP-BLE-MESH, how to modify this name?
------------------------------------------------------------------------------------------------

  - You can use API `esp_ble_mesh_set_unprovisioned_device_name() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/esp-ble-mesh.html?highlight=esp_ble_mesh_set_unprovisioned_device_name#_CPPv442esp_ble_mesh_set_unprovisioned_device_namePKc>`_, it is suggested to call it after `esp_ble_mesh_init() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/esp-ble-mesh.html?highlight=esp_ble_mesh_init#_CPPv417esp_ble_mesh_initP19esp_ble_mesh_prov_tP19esp_ble_mesh_comp_t>`_, otherwise the device name is still ESP-BLE-MESH.

--------------

How many node devices can ESP32's BLE-MESH application connect to?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -  Theoretically, the ESP32 BLE-MESH application supports 32767 node devices. The number of connections supported in actual application depends on the memory usage.
  
