ESP-WIFI-MESH Application Framework
===================================

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

  If you have new requirements for Wi-Fi Mesh applications, it is recommended to use our newly released `ESP-Mesh-Lite solution <https://github.com/espressif/esp-mesh-lite>`__, instead of Wi-Fi Mesh.

--------------

How much memory does ESP-WIFI-MESH occupy? Is external PSRAM required?
----------------------------------------------------------------------------

  ESP-WIFI-MESH occupies about 60 KB of memory. Whether external PSRAM is needed depends on the complexity of the application scenario. Generally, external PSRAM is not required for typical applications.

--------------

Can ESP-WIFI-MESH support performing OTA for multiple devices at a time?
------------------------------------------------------------------------------------------------------------

  ESP-WIFI-MESH devices support performing OTA for multiple devices at a time. The OTA approach is that the root node downloads the firmware and then disseminates it to other nodes. For a specific example, please refer to `Mupgrade <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mupgrade>`__.

--------------

How many devices can ESP32 support for ESP-WIFI-MESH networking?
----------------------------------------------------------------

  ESP32 can support 1,000 devices for ESP-WIFI-MESH networking. If you want to stably connect a large number of devices, it is recommended to avoid connecting over 512 networking devices under each ESP-WIFI-MESH network.

--------------

What is the difference between the ESP-WIFI-MESH Router mode and the No Router mode of ESP32?
---------------------------------------------------------------------------------------------------

  - The Router mode refers to router-based networking, in which the root node connects to the router.
  - The No Router mode refers to self-networking without a router, in which external data interaction is not possible.

--------------

Can ESP-WIFI-MESH of ESP32 complete networking when the child node fails to detect the router signal?
-------------------------------------------------------------------------------------------------------------------------------------

  With the same configuration SSID, even if the child node fails to detect Wi-Fi, ESP-WIFI-MESH of ESP32 supports connecting the child node to the root node.

--------------

Can ESP-WIFI-MESH of ESP32 automatically repair the network?
------------------------------------------------------------

  ESP-WIFI-MESH of ESP32 has a mechanism to detect network disconnection and can automatically repair the network.

--------------

When using ESP-WIFI-MESH of ESP32 without connecting to Wi-Fi, how can I realize a self-organizing network?
--------------------------------------------------------------------------------------------------------------------------------------------

  To designate a device as the root node, please refer to the Mwifi `description <https://github.com/espressif/esp-mdf/blob/master/examples/function_demo/mwifi/README_en.md>`_ and `example <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mwifi>`_.

--------------

When using ESP-WIFI-MESH of ESP32 for automatic root node election during networking, is it possible to designate specific local modules for the election process?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ESP-WIFI-MESH of ESP32 supports designating a device as a child node. Once designated, the device will not participate in the root node election, thereby realizing a localized Mesh network for the election.

--------------

Can multiple root nodes send messages to each other in a no-router scenario using ESP-WIFI-MESH of ESP32?
---------------------------------------------------------------------------------------------------------

  In a no-router scenario, multiple root nodes cannot send messages to each other.

--------------

How to query the source code of the ESP-WIFI-MESH application?
----------------------------------------------------------------

  - iOS source code: https://github.com/EspressifApp/EspMeshForiOS
  - Android source code: https://github.com/EspressifApp/EspMeshForAndroid

--------------

Does ESP-WIFI-MESH offer a no-router solution for self-networking?
--------------------------------------------------------------------------

  Please refer to the `No Router <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mwifi/no_router>`__ and `get_started <https://github.com/espressif/esp-mdf/tree/master/examples/get-started>`__ examples for no-router solutions.

--------------

After using Mwifi for automatic networking, how can I obtain the signal strength (RSSI) of all potential parent nodes of a specific node?
--------------------------------------------------------------------------------------------------------------------------------------------------------

  - You can call ``mwifi_get_parent_rssi()`` to obtain the signal strength of the parent node.
  - You can refer to the `ESP-NOW Debug Receiver Board Demo <https://github.com/espressif/esp-mdf/blob/master/examples/wireless_debug>`__ for ways to obtain the signal strength of other nodes.

--------------

What protocol is used for communication between nodes in the ESP-MDF Mesh network?
--------------------------------------------------------------------------------------

  Communication within the Mesh network is based on a custom protocol at the data link layer, which is one of our core protocols. It supports the ACK mechanism but lacks a built-in timeout/retransmission mechanism. You can add the corresponding mechanism at the application layer according to your needs.

--------------

Can ESP-WIFI-MESH connect all nodes to the router?
----------------------------------------------------------

  Only the root node can connect to the router. The child nodes will connect directly or indirectly to the root node, and then communicate with the router through the root node.

--------------

Can the root node of ESP-WIFI-MESH connect to the Internet via 4G dial-up?
--------------------------------------------------------------------------

  It is possible, but there is currently no dedicated application for this scenario. You can refer to the `No Router <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mwifi/no_router>`__ example in ESP-MDF, where the root node communicates directly with the computer via the serial port, or it can be configured to transmit data via a 4G module.

--------------

After a successful connection using the esp_mesh_set_parent function, if the AP is disconnected, the function will continuously attempt to reconnect. How can I set the number of reconnect attempts?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - For the self-networking solution, ESP-WIFI-MESH will not attempt to reconnect by default. If the AP is disconnected, you need to call ``esp_wifi_scan_start`` to get the devices that can be connected and reset the parent node. Please refer to `Mesh Manual Networking Example <https://github.com/espressif/esp-idf/tree/4a9f339447cd5b3143f90c2422d8e1e1da9da0a4/examples/mesh/manual_networking>`__.
  - It is recommended to use the self-networking solution for development.

--------------

Why is ``phy_init: failed to load RF calibration data`` reported after setting the button?
----------------------------------------------------------------------------------------------

  The Espressif chip will self-calibrate RF on the first power-up and store the data in NVS. If this part is erased, this error will be reported and a full calibration will be performed.

--------------

How to pause/resume Mwifi?
--------------------------

  Call ``mwifi_stop/mwifi_start`` to pause/resume Mesh.

--------------

For the ESP32 series without router Mesh networking, how can an application connect to the softAP of the root interface?
-------------------------------------------------------------------------------------------------------------------------------------

  In the scenario without a router Mesh, the softAP initiated by Mesh devices does not support the connection of devices other than Mesh devices. If there is a need for non-Mesh devices connection, such as smartphones, it is recommended to use `ESP-Mesh-Lite <https://github.com/espressif/esp-mesh-lite/tree/master>`__.

--------------

ESP-WIFI-MESH can connect to an AP but cannot connect to the TCP server on that AP. How can this issue be resolved?
-----------------------------------------------------------------------------------------------------------------------------------------

  Please refer to the GitHub issue: `mesh -> "with-router" example doesn't work with espressif IDF softAP #71 <https://github.com/espressif/esp-mdf/issues/71>`__.

--------------

How to modify the AP connection and maximum layer in the Mwifi example? What is the maximum bandwidth and delay during communication?
-------------------------------------------------------------------------------------------------------------------------------------

  - You can go to menuconfig and modify the configuration through ``Component config`` > ``MDF Mwifi`` > ``Capacity config``.
  - For communication performance, please refer to the `Performance <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/esp-wifi-mesh.html#mesh-network-performance>`__ section.
  - WIFI-MESH bandwidth can be tested through the `ESP-WIFI-MESH Console Debugging Demo <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mwifi/console_test>`__.

--------------

How to get real-time return values of the sensor?
------------------------------------------------------

  As the device end is functioning as an HTTP server, requests must be initiated by the application to obtain real-time data. You can employ the following two methods to acquire real-time data:

  - When the sensor data changes, notify the mobile phone to actively request data through UDP. If you are using our local communication protocol, send the following command to prompt the application to request device data:

  .. code-block:: c

    data_type.protocol = MLINK_PROTO_NOTICE;
    ret = mwifi_write(NULL, &data_type, "status", strlen("status"), true);
    MDF_ERROR_CONTINUE(ret != MDF_OK, "<%s> mlink_handle", mdf_err_to_name(ret));

  - Establish a TCP/MQTT/HTTP server. Once a TCP connection is established with the server, sensor data changes will be actively reported.

--------------

For a new node that might already be installed in a device that is located at a considerable distance from the root node, how can this node join the ESP-WIFI-MESH network?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - It seems that you are using the get-started example. For testing convenience, this example is a no-router solution, in which the root node is designated. Therefore, if the root node crashes, the other devices will not be able to recover.
  - You can refer to the light example in development_kit. This example can be used with the ESP-Mesh application (the Android version can be downloaded from our `official website <https://www.espressif.com/en/support/download/apps>`_, and the iOS version can be downloaded and tested by searching for ESP-Mesh in the App Store).
  - This example does not designate a root node. Instead, the root node is elected by the devices, which requires a router. In this scenario, if the root node fails, the remaining devices will automatically complete the re-networking and connect to the router without user intervention.

--------------

Is the source code for the ESP-WIFI-MESH application open?
------------------------------------------------------------------

  - We have already opened the source code for the ESP-Mesh application on GitHub. Please refer to `EspMeshForAndroid <https://github.com/EspressifApp/EspMeshForAndroid>`_ and `EspMeshForiOS <https://github.com/EspressifApp/EspMeshForAndroid>`_.
  - If you have any questions or encounter bugs during usage, feel free to leave comments and ask questions on GitHub or here. We will handle them as soon as possible.

--------------

What is the maximum packet size for Wi-Fi Mesh data transmission?
------------------------------------------------------------------------------------------

  The maximum packet size is 1,456 bytes.

--------

Does ESP32's Wi-Fi Mesh support self-networking without a router?
--------------------------------------------------------------------------------------------------------------------------

  Yes, please refer to the `No Router <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mwifi/no_router>`_ example.

-----------------

What is the maximum number of node layers allowed when using ESP32 with Wi-Fi Mesh?
-------------------------------------------------------------------------------------------

  - In a Wi-Fi Mesh network, you can set the maximum number of network layers using the `esp_mesh_set_max_layer() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp-wifi-mesh.html#_CPPv422esp_mesh_set_max_layeri>`_ function.
  - For a tree topology, the maximum number is 25. For a chain topology, the maximum number is 1,000.

---------------------

When testing the `esp-mdf/examples/function_demo/mwifi/router <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mwifi/router>`_ example with the ESP32 development board, the device name displayed on the router connection end is "espressif" after the ESP32 connects to the router. How can I change this name?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  You can go to menuconfig, and modify it through ``Component config`` > ``LWIP`` > ``(espressif) Local netif hostname``.

---------------------

Can Wi-Fi Mesh send messages to specific nodes through a TCP server?
------------------------------------------------------------------------------------------------------------------------------

  Wi-Fi Mesh can send data to specific nodes or group addresses through a TCP server. Please refer to the `Mwifi Router <https://github.com/espressif/esp-mdf/blob/master/examples/function_demo/mwifi/router/README.md>`_ example.

--------------------

During the operation of the ESP32 Wi-Fi Mesh network, what event does the system feedback if the root node is lost?
-------------------------------------------------------------------------------------------------------------------

  If the root node is lost, all nodes will trigger the MDF_EVENT_MWIFI_PARENT_DISCONNECTED (MESH_EVENT_PARENT_DISCONNECTED) event. Subsequently, the nodes will commence a re-scan and initiate a new election process until a new root node is elected.

----------------

When developing Wi-Fi Mesh applications with ESP32 using the esp_mesh_send() function, I've observed that the server is not receiving any data. How can data be transmitted from leaf nodes to an external server?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - esp_mesh_send() can only be used for internal data communication in the Wi-Fi Mesh network.
  - To send data from a leaf node to an external server, the data needs to be forwarded through the root node.
  - The correct approach is for leaf nodes to first send the data to the root node, and then the root node forwards the data to the external server.

---------------

How to perform an OTA upgrade after ESP-MESH devices are networked?
-----------------------------------------------------------------------------------------------------------------------------------------------

  - The root node can connect to the server to get the upgrade bin file, and then send the firmware to the corresponding module for OTA upgrade via MAC address.
  - For details, please refer to the `Mupgrade Example <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mupgrade>`_.

---------------

Is there a reference design for ESP-MESH lights?
--------------------------------------------------------------------------------------------------------------------------------

  - The overall design of the light is completed by a third-party factory, and we do not have related schematics or PCB layouts. But from the module perspective, you only need to power the chip, and the chip outputs PWM to control the color or color temperature change of the light, which is not too complicated.
  - Please refer to `ESP-MDF <https://github.com/espressif/esp-mdf>`_ for more information about Mesh.

---------------

What is the default mode of ESP-MESH nodes?
--------------------------------------------------------------------------------------------------------------------------------

  The default mode of ESP-MESH is IDLE.

---------------

When ESP-MESH starts in AP+STA mode, can the phone search for the AP?
-----------------------------------------------------------------------------------------------------------------------------------

  No, as ESP-MESH is a private protocol of Espressif. For details, please refer to the `WIFI-MESH Introduction <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/esp-wifi-mesh.html>`_.

---------------

After the device has completed networking, is it necessary to perform a complete re-scan when adding a new device?
-------------------------------------------------------------------------------------------------------------------------------------------

  No, it is not necessary. Only a scan within the current set of child nodes is required. The new device can connect to the node with the strongest signal strength as its parent node.

------------------------

Can ESP32, as the master device, achieve time synchronization with multiple slave devices with an error within 2 ms?
------------------------------------------------------------------------------------------------------------------------------------------

  - For this application scenario, it is recommended to develop based on ESP-MDF. Please refer to `light_example <https://github.com/espressif/esp-mdf/blob/master/examples/development_kit/light/main/light_example.c>`_.
  - Using `esp_mesh_get_tsf_time() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp-wifi-mesh.html#_CPPv421esp_mesh_get_tsf_timev>`_ can meet the precision requirements mentioned (within 2 ms).

---------------

How to get the node type in ESP-MESH?
--------------------------------------------------------------------------------------------------------------------------------

  You can call the `esp_mesh_get_type <https://docs.espressif.com/projects/esp-idf/en/release-v4.1/api-reference/network/esp_mesh.html?highlight=esp_mesh_get_type#_CPPv417esp_mesh_get_typev>`_ interface to get the node type.

---------------

Is there an example of ESP-Mesh root node sending messages to the server via Ethernet?
--------------------------------------------------------------------------------------

  Please refer to the `Mwifi Router Example <https://github.com/espressif/esp-mdf/blob/master/examples/function_demo/mwifi/root_on_ethernet/README.md>`_.

-------------

Does the `ESP-Mesh-Lite <https://github.com/espressif/esp-mesh-lite/tree/master>`_ solution support applications without a router?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes, it does. The application scenarios supported by the ESP-Mesh-Lite solution can be found in the `ESP-Mesh-Lite Features <https://github.com/espressif/esp-mesh-lite/blob/master/components/mesh_lite/CHANGELOG.md>`_.
  - You can enable the ``Component config`` > ``ESP Wi-Fi Mesh Lite`` > ``Enable Mesh-Lite`` > ``Mesh-Lite info configuration`` > ``[*] Join Mesh no matter whether the node is connected to router`` configuration option for testing based on the `Mesh Local Control Example <https://github.com/espressif/esp-mesh-lite/blob/master/examples/mesh_local_control/README.md>`_.
  - For solutions without a router, please note the following:

    - Try to determine a root node, which can be set through ``esp_mesh_lite_set_allow_level(1)``.
    - For other nodes, it is recommended to use the ``esp_mesh_lite_set_disallow_level(1)`` function to prevent them from becoming root nodes.
    - In the application scenario of Mesh-Lite, establishing a Mesh network relies on factors such as the physical distance between devices and Wi-Fi signal quality. Therefore, thorough on-site testing and debugging are necessary to ensure the performance and stability of the Mesh network.

----------------

When ESP-WIFI-MESH is networked, is it possible for the root node or child nodes to simultaneously initiate a Wi-Fi Scan to scan for available AP information around?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  No. When ESP-WIFI-MESH is networked, none of the node devices support the activation of the Wi-Fi Scan function.

----------------

When using the ESP-WIFI-MESH Router solution, how to switch to a new router for networking?
-----------------------------------------------------------------------------------------------------------------------------------

  - You can modify the following code after the ``MESH_EVENT_PARENT_DISCONNECTED`` event:

    .. code:: text

            mesh_router_t change_router = {
                .ssid = "TP-LINK_CSW",
                .password = "12345678",
                .ssid_len = strlen("TP-LINK_CSW"),
            };
            esp_mesh_set_self_organized(false, false);
            esp_mesh_set_router(&change_router);
            esp_mesh_set_self_organized(true, true);
