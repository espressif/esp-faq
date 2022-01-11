ESP-WIFI-MESH development framework
=======================================

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

What is the maximum data transmission load for Wi-Fi mesh?
--------------------------------------------------------------------------------------------------

  - Up to 1456 bytes.

-------------------

Does ESP32's Wi-Fi Mesh supports No Router self-networking?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes, please refer to example `esp-mdf/examples/function_demo/mwifi/no_router <https://github.com/espressif/esp-mdf/tree/master/examples/ function_demo/mwifi/no_router>`_.

-----------------

What is the maximum number of node layers allowed when ESP32 uses Wi-Fi Mesh?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - In the Wi-Fi Mesh network, you can set the maximum number of layers via `esp_mesh_set_max_layer() <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/network/esp_mesh.html#_CPPv422esp_mesh_set_max_layeri>`_.
  - For tree topology structure, the maximum number is 25; while for chain topology structure, the maximum number is 1000.
  
-----------------------

When using an ESP32 development board to test the `esp-mdf/examples/function_demo/mwifi/router <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mwifi/router>`_ example, After ESP32 is connected to the router, the device name in connection is "espressif". How to modify this name?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Please modify the "menuconfig → Component config → LWIP  → (espressif) Local netif hostname" setting.
