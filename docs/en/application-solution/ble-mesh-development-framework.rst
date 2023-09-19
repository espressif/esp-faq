ESP-BLE-MESH Development Framework
==================================

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

For more FAQs about ESP-BLE-MESH, please refer to `ESP-BLE-MESH FAQ <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/esp-ble-mesh/ble-mesh-faq.html>`__.

Why does the ESP-BLE-MESH application wait for a long time during fast provisioning?
----------------------------------------------------------------------------------------------

  After the app provisioned one Proxy node, it will disconnect from the app during fast provisioning, and reconnect with the app when all the nodes are provisioned. The long wait during fast provisioning may be due to:

  - Complex network topology. If there are many nodes in the network and the topology is complex, the Provisioner may need more time to scan the network and communicate with the nodes.
  - Unstable network signal. If the network signal is unstable, communication may be interfered with or lost, resulting in a longer waiting time for the application.
  - Long node response time. If the node response time is long, the Provisioner may wait for a timeout and resend the message, resulting in a longer waiting time for the application.
  - Communication failure between the application and the Provisioner. Such failure may result in a longer waiting time for the application.

--------------

How to clear the network information of the ESP32 ESP-BLE-MESH node?
--------------------------------------------------------------------------

  To clear the network information of a node, you can call `esp_ble_mesh_node_local_reset() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/esp-ble-mesh.html?highlight=esp_ble_mesh_node_local_reset#_CPPv429esp_ble_mesh_node_local_resetv>`_.

--------------

How to delete the network information of a node?
--------------------------------------------------------------

  To delete the information of a node, you can call `esp_ble_mesh_provisioner_delete_node_with_uuid() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/esp-ble-mesh.html?highlight=esp_ble_mesh_provisioner_delete_node_with_uuid#_CPPv446esp_ble_mesh_provisioner_delete_node_with_uuidAL16E_K7uint8_t>`_ or `esp_ble_mesh_provisioner_delete_node_with_addr() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/esp-ble-mesh.html?highlight=esp_ble_mesh_provisioner_delete_node_with_uuid#_CPPv446esp_ble_mesh_provisioner_delete_node_with_addr8uint16_t>`_.

--------------

When a node is powered off and then powered on again, do I need to re-provision it?
----------------------------------------------------------------------------------------------------------------------

  To save yourself from re-provisioning, go to ``menuconfig`` -> ``Component config`` -> ``Bluetooth Mesh support`` and enable ``Store Bluetooth Mesh key and configuration persistently`` to save the configuration information.

--------------

Assuming development board 1 acts as a Provisioner, and boards 2, 3, and 4 act as nodes. After successful provisioning, if board 1 loses power and is then powered on again, can it join the mesh network?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  After board 1 is powered on again, if the NetKey and AppKey have not changed, it can directly join the network. However, the addresses of the nodes in the mesh network will be lost if they are not saved in advance.

--------------

In ESP-BLE-MESH, how do I know if a node is offline?
------------------------------------------------------

  Nodes can periodically publish messages. You can configure them to periodically send Heartbeat messages through the Health Model or vendor messages through the Vendor Model.

--------------

How do ESP-BLE-MESH nodes communicate with each other in strings?
-----------------------------------------------------------------------

  They can use the Vendor Model. The sender puts the string into the vendor message, and the receiver parses it as a string after receiving the message.

--------------

Failed in initializing the partition when configuring ESP-BLE-MESH to save node information. The error message is ``BLE_MESH: Failed to init mesh partition, name ble_mesh, err 261``. How to fix it?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  If you selected the ``Use a specific NVS partition for BLE Mesh`` option, please make sure that the partition.csv file contains a specific partition named ``ble_mesh``.

--------------

How to add Health Model to the Provisioner's example?
----------------------------------------------------------

  In menuconfig, go to ``Component config`` -> ``ESP BLE Mesh Support`` -> ``Support for BLE Mesh Client Models`` and enable ``Health Client Model``.

--------------

What's the difference between using ble_mesh_fast_prov_client as a Provisioner and a mobile phone as a Provisioner?
-----------------------------------------------------------------------------------------------------------------------------------

  - The ``ble_mesh_fast_prov_server`` example configures the model when it receives the ESP_BLE_MESH_MODEL_OP_APP_KEY_ADD opcode, while the phone Provisioner needs to send the ESP_BLE_MESH_MODEL_OP_MODEL_APP_BIND opcode to bind the model's AppKey, and then send the ``ESP_BLE_MESH_MODEL_OP_MODEL_PUB_SET`` to configure the publication.
  - The ``ble_mesh_fast_prov_client`` and ``ble_mesh_fast_prov_server`` examples are fast provision solutions provided by Espressif. It can provision 100 nodes within 60 s. To achieve this function, some vendor messages are added for the transmission of vendor information between devices.

--------------

Are there any tools or methods to view the encrypted messages transmitted between ESP-BLE-MESH nodes?
----------------------------------------------------------------------------------------------------------------

  - To decrypt the data packet, you need to configure the NetKey, AppKey, DevKey, and IV Index. You can view the configuration interface.
  - Broadcast packets should be captured simultaneously on channels 37, 38, and 39, usually using specialized equipment.

--------------

Can the AppKey be set by the manufacturer? Is it related to the unicast address?
-------------------------------------------------------------------------------------------------------------------------------

  The application key can be set by the manufacturer. It is bound with the model and is not related to the unicast address.

--------------

If a node suddenly goes offline, does the entire mesh network need to poll and send Heartbeat messages through the Health Model monitoring mechanism?
-----------------------------------------------------------------------------------------------------------------------------------------------------------

  The ESP-BLE-MESH network does not establish any connections. It sends messages directly through the broadcast channel. You can send a heartbeat packet to the same node to check its status.

---------------

Can the main node (Proxy node) and the slave node send messages to each other using the client-server model? Is there an example?
------------------------------------------------------------------------------------------------------------------------------------------------

  Please refer to the `ble_mesh_fast_provision/ble_mesh_fast_prov_server <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/esp_ble_mesh/fast_provisioning/fast_prov_server>`__ example.

--------------

In the lower-right corner of the nRF mobile application, tap ``Setting`` and you will find a configurable ``Network Key`` field. Whose NetKey does this field configure?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - In the nRF mobile application, the ``Network Key`` configures the NetKey of the Provisioner. When the Provisioner provisions other devices, this NetKey is assigned to the nodes that are connected to the network.
  - If the Provisioner has multiple NetKeys, the Provisioner can choose which NetKey to assign to the device during configuration. The Provisioner can communicate with nodes in the network using different NetKeys. Each node's NetKey is assigned by the Provisioner.

----------------

How can a device join the ESP-BLE-MESH network?
-----------------------------------------------------

  You can refer to `Getting Started with ESP-BLE-MESH <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/esp-ble-mesh/ble-mesh-index.html#getting-started-with-ble-mesh>`__.

----------------

What is the maximum packet size for ESP-BLE-MESH transmission?
-------------------------------------------------------------------------------------

  The maximum single packet size at the application layer is 384 bytes, and the maximum size at the lower layer without packet segmentation is 11 bytes.

----------------

Can you provide an application example of provisioning through ESP32 ESP-BLE-MESH? What software can be used as the provisioning configuration application?
--------------------------------------------------------------------------------------------------------------------------------------------------------------

  - You can use the application example `onoff_server <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/esp_ble_mesh/onoff_models/onoff_server>`_ and the nRF Mesh mobile application.
  - For the provisioning process, refer to `Getting Started with ESP-BLE-MESH <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/esp-ble-mesh/ble-mesh-index.html#getting-started-with-ble-mesh>`__.

----------------

In ESP-BLE-MESH, the default name of the unprovisioned device is ESP-BLE-MESH. How to modify it?
---------------------------------------------------------------------------------------------------------------------

  You can use the `esp_ble_mesh_set_unprovisioned_device_name() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/esp-ble-mesh.html?highlight=esp_ble_mesh_set_unprovisioned_device_name#_CPPv442esp_ble_mesh_set_unprovisioned_device_namePKc>`_ API. It is recommended to call it after `esp_ble_mesh_init() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/esp-ble-mesh.html?highlight=esp_ble_mesh_init#_CPPv417esp_ble_mesh_initP19esp_ble_mesh_prov_tP19esp_ble_mesh_comp_t>`_. Otherwise, the name will still be the default ESP-BLE-MESH.

-------------

How many node devices can the ESP32 ESP-BLE-MESH application connect to?
------------------------------------------------------------------------------

  Theoretically, the ESP32 ESP-BLE-MESH application can connect up to 32767 devices, but the actual number of connected devices depends on memory usage.

--------------------------------------------------------

How to manually reset the ESP32 ESP-BLE-MESH device (not through the mobile provisioning application or provisioning device)?
-----------------------------------------------------------------------------------------------------------------------------------

  You can call the `esp_ble_mesh_node_local_reset <https://docs.espressif.com/projects/esp-idf/en/release-v4.1/api-reference/bluetooth/esp-ble-mesh.html?highlight=esp_ble_mesh_node_local_reset#_CPPv429esp_ble_mesh_node_local_resetv>`__ API to reset the ESP-BLE-MESH node, erase all provisioning information, and wait for the reset event to arrive to confirm the reset is successful. After the API is called, the device needs to be provisioned again.

--------------------------------------------------------

After ESP32 runs the ESP-BLE-MESH program for a long time, a segmentation error occurs when the client sends a message to the server, and the ESP-BLE-MESH prints ``NO multi-segment messsage contexts available``. How to solve the issue?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  You can go to ``Component config`` -> ``ESP BLE Mesh Support`` -> ``Maximum number of simultaneous outgoing segmented messages``, and expand the space by configuring ``BLE_MESH_TX_SEG_MSG_COUNT``.

-----------

Can I disable NetKey and IV Update when using the ESP32 ESP-BLE-MESH application?
----------------------------------------------------------------------------------------------

  No. NetKey and IV Update must stay enabled.
