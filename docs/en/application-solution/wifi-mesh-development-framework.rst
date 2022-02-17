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

-----------------------

Can Wi-Fi Mesh send messages to specific nodes via TCP Server?
-------------------------------------------------------------------------------------------------------------------------------

  - Wi-Fi Mesh network can send data to the specified node or group in the TCP server, please refer to the `demo <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mwifi/router>`_.

------------------------

During the operation of the ESP32 Wi-Fi Mesh network, if the Root node is lost, what events will the system report back?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - If the Root node is lost, all nodes will trigger 'MDF_EVENT_MWIFI_PARENT_DISCONNECTED (MESH_EVENT_PARENT_DISCONNECTED)', and then start rescanning and re-election until a new Root node is elected.

------------------

I'm using ESP32 for Wi-Fi Mesh application with the ``esp_mesh_send()`` function, but the server did not receive any data. How to transfer data from leaf nodes to external servers?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ``esp_mesh_send()`` can only be used for data communication within the Wi-Fi Mesh network.
  - If leaf nodes want to send data to an external server, the data needs to be forwarded through the root node.
  - The correct approach is: the leaf node first sends the data to the root node, and the root node then sends the data to the external server.

---------------

How do I upgrade my ESP-MESH device via OTA after networking?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The ROOT node can connect to the server to get the upgrade bin file and then send the firmware to the corresponding module via MAC address for OTA upgrade.
  - For more information, please refer to `mupgrade demo <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mupgrade>`_.

---------------

Can you provide ESP-MESH light reference design?
---------------------------------------------------------------------------------------------------------------------------------

  - The overall design of the lamp is done by a third-party factory and we do not have a schematic or PCB layout. But from the module level, we only need to supply power to the chip and the chip outputs PWM to control the color or color temperature change of the lamp, which does not involve complicated design.
  - Please refer to `ESP-MDF <https://github.com/espressif/esp-mdf>`_ for more information on MESH.

---------------

What is the default mode for ESP-MESH nodes without any configuration?
---------------------------------------------------------------------------------------------------------------------------------

  - The default is IDLE mode.

---------------

ESP-MESH starts with AP+STA mode enabled, can the phone search for APs?
---------------------------------------------------------------------------------------------------------------------------------

  - No, ESP-MESH is a private protocol of Espressif, please refer to `WIFI-MESH Introduction <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/esp-wifi-mesh.html/>`_ .
