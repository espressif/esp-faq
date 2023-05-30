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

.. note::

  If you have new requirements for Wi-Fi Mesh related application scenarios, we recommend that you directly use our newly launched `ESP-Mesh-Lite solution <https://github.com/espressif/esp-mesh-lite>`__, instead of Wi-Fi Mesh.

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

  - In the Wi-Fi Mesh network, you can set the maximum number of layers via `esp_mesh_set_max_layer() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp-wifi-mesh.html#_CPPv422esp_mesh_set_max_layeri>`_.
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

  - No, ESP-MESH is a private protocol of Espressif, please refer to `WIFI-MESH Introduction <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/esp-wifi-mesh.html>`_ .

---------------

Do I need to rescan for all the newly added devices when the original device has already been networked?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - No, just scan through the current child nodes and find the one with the strongest signal as its parent node.

---------------------

When using an ESP32 as a master device to synchronize time for multiple slave devices, can the time error be less than 2 ms? 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - For this application scenario, it is recommended to develop based on esp-mdf, please refer to `esp-mdf/examples/development_kit/light <https://github.com/espressif/esp-mdf/blob/master/examples/development_kit/light /main/light_example.c>`_ example.
  - Please use `esp_mesh_get_tsf_time() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp-wifi-mesh.html#_CPPv421esp_mesh_get_tsf_timev>`_, whose accuracy can meet your demand.

---------------

How do I get the type of the node in ESP-MESH?
--------------------------------------------------------------------------------------------------------------------------------

  - You can call `esp_mesh_get_type <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.1/api-reference/network/esp_mesh.html? highlight=esp_mesh_get_type#_CPPv417esp_mesh_get_typev>`_ interface to get it.

---------------

Is there any demo of ESP-Mesh root node sending messages to a service via ethernet?
------------------------------------------------------------------------------------------------------

  - Please see `root_on_ethnernet <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mwifi/root_on_ethernet/>`_ demo.

-------------

Does the `esp-mesh-lite <https://github.com/espressif/esp-mesh-lite/blob/master/components/mesh_lite/README.md#esp-wi-fi-mesh-lite>`_ solution support the applications without routers?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes, it supports. For the applications supported by esp-mesh-lite, please refer to `esp-mesh-lite features <https://github.com/espressif/esp-mesh-lite/blob/master/components/mesh_lite/CHANGELOG.md#mesh>`_.
  - You can conduct tests by enabling ``Component config`` > ``ESP Wi-Fi Mesh Lite`` > ``Enable Mesh-Lite`` > ``Mesh-Lite info configuration`` > ``[*] Join Mesh no matter whether the node is connected to router`` in the `esp-mesh-lite/examples/mesh_local_control <https://github.com/espressif/esp-mesh-lite/tree/master/examples/mesh_local_control>`_ example.
  -  Please pay attention to the following tips if you want to use esp-mesh-lite without routers:

    - Identify a root node if possible, which can be set via ``esp_mesh_lite_set_allow_level(1)``.
    - It is recommended to use the ``esp_mesh_lite_set_disallow_level(1)`` function to prohibit the other nodes from being the root node.
    - In the applications of Mesh-Lite, a mesh network should be established based on some factors such as the distance of devices and the quality of Wi-Fi signal. As a result, you should test and debug the meash network to ensure its performance and stability.
