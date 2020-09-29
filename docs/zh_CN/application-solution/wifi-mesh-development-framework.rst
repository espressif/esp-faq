Wi-Fi Mesh 应用框架
===================

:link_to_translation:`en:[English]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

--------------

Wi-Fi Mesh 占用多大内存？是否需要外部 PSRAM ？
----------------------------------------------

  Wi-Fi Mesh 内存占用约 60KB，是否需要外部 PSRAM 取决于应用场景的复杂情况，一般性应用无需外部 PSRAM。

--------------

Wi-Fi Mesh 能否批量 OTA ？
--------------------------

  Wi-Fi Mesh 设备支持批量 OTA。OTA ⽅式为：根节点下载固件，然后再发至其他节点。具体示例请参考: `mupgrade <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mupgrade>`__。

--------------

ESP32 支持多少设备进行 Wi-Fi Mesh 组网？
----------------------------------------

  ESP32 支持 1000 个设备进行 Wi-Fi Mesh 组网。若要稳定连接大量设备，建议在每个 Wi-Fi Mesh 网络下，组网设备不超过 512 台设备。

--------------

ESP32 的 Wi-Fi Mesh Router 模式与 No Router 模式有什么区别？
------------------------------------------------------------

  - WiFi Mesh 网络的 Router 模式是根据路由器进行组网，根节点连路由器。
  - No Router 模式是无路由器的场景下进行自组网，此模式下不可与外部数据交互。

--------------

ESP32 的 Wi-Fi Mesh 能否在子设备搜索不到路由器信号时完成组网？
--------------------------------------------------------------

  ESP32 的 Wi-Fi Mesh 能实现：在拥有配置相同 Wi-Fi 的 SSID ，子设备没有搜索到 Wi-Fi 时，子设备也可以连接到根节点。

--------------

ESP32 Wi-Fi Mesh 是否可自动修复网络？
-------------------------------------

  ESP32 Wi-Fi Mesh 可自动修复网络，Wi-Fi Mesh 有检测网络断线的机制。

--------------

使用 ESP32 Wi-Fi Mesh，如何设置可以在没连接到 Wi-Fi 的情况下形成自组网？
------------------------------------------------------------------------

  需要指定一个设备作为 Root 节点，可参考 `说明 <https://github.com/espressif/esp-mdf/blob/master/examples/function_demo/mwifi/README_cn.md>`_ 和 `示例 <https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mwifi>`_。

--------------

使用 ESP32 进行 Wi-Fi MESH 应用，在组网自动选举根节点时，是否可以指定局部模块进行选举？
---------------------------------------------------------------------------------------

  ESP32 Wi-Fi MESH 可以指定设备为子节点，它将不参与根节点的选举，可实现局部模块进行选举。

--------------

使用 ESP32 进行 Wi-Fi MESH 应用，无路由场景下，多个根节点之间能互发消息吗？
---------------------------------------------------------------------------

  无路由的场景下，多个根节点之间不能互发消息。

--------------

Wi-Fi Mesh 可以批量 OTA 吗？
-------------------------------

  - Wi-Fi mesh 设备可以批量 OTA 的。
  - OTA 的方式是根节点下载固件，然后再发至其他节点。
  - 具体示例请参考 https://github.com/espressif/esp-mdf/tree/master/examples/function_demo/mupgrade
