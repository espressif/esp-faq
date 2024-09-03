共存
====

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

Wi-Fi 和蓝牙共存时，支持哪些共存场景？
--------------------------------------------

  支持的共存场景请参考 `共存文档 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/coexist.html>`_。

--------------

Wi-Fi 和 ESP-BLE-MESH 共存时，为什么 Wi-Fi 吞吐量很低？
--------------------------------------------------------

  未搭载 PSRAM 的 ESP32-DevKitC 开发板，Wi-Fi 和 ESP-BLE-MESH 共存可以正常运行，但是吞吐率较低。当 Wi-Fi 和 ESP-BLE-MESH 共存时，搭载 PSRAM 的 ESP32-DevKitC 速率可以稳定在 1 Mbps 以上。

  应使能 menuconfig 中的一些配置来支持 PSRAM:

  - ``ESP32-specific --> Support for external,SPI-connected RAM --> Try to allocate memories of Wi-Fi and LWIP...``
  - ``Bluetooth --> Bluedriod Enable --> BT/BLE will first malloc the memory from the PSRAM``
  - ``Bluetooth --> Bluedriod Enable --> Use dynamic memory allocation in BT/BLE stack.``
  - ``Bluetooth --> Blutooth controller --> BLE full scan feature supported.``
  - ``Wi-Fi --> Software controls Wi-Fi/Bluetooth coexistence --> Wi-Fi``

--------------

ESP32 的 ESP-WIFI-MESH 和 Bluetooth® LE Mesh 可以同时支持吗？
------------------------------------------------------------------

  不支持。

  ESP32 的 ESP-WIFI-MESH 和 BLE 可以同时支持，或者 ESP32 Wi-Fi STA 模式和 BLE Mesh 可以同时支持。

--------------

ESP32 蓝牙和 Wi-Fi 能否同时使用？
----------------------------------------

  ESP32 的 Wi-Fi 和蓝牙可共存，但需要分时控制，可在 menuconfig 中使能 Wi-Fi 和蓝牙共存设置。如下：

  :IDF\: release/v5.0:

  ``menuconfig -> Component config -> Wi-Fi -> Software controls WiFi/Bluetooth coexistence (Enable)``

  :IDF\: release/v5.1 以及以上版本:

  ``menuconfig -> Component config -> Wireless Coexistence -> Software controls WiFi/Bluetooth coexistence (Enable)``

--------------

Wi-Fi、Bluetooth® LE 和 A2DP Sink 共存，进入 Bluetooth LE 扫描的时候音频数据接收会丢失、卡顿。怎么解决？
--------------------------------------------------------------------------------------------------------

  - 使用 RingBuf 缓存音频数据
  - 暂停播放音乐，并增加提示音，例如：正在扫描设备。

--------------

BLE adverting (Connectable) + iBeacon sending(advertising) 可以共存吗？？
--------------------------------------------------------------------------------------------------

  :IDF\: release/v4.0以及以上版本 | CHIP\: ESP32:

  - 硬件上还未支持，应用层可以通过定时轮询发广播包的方式来完成。

  :IDF\: release/v4.3 以及以上版本 | CHIP\: ESP32-C3|ESP32-S3:

  - 可以。

--------------

ESP32 的蓝牙双模如何共存及使用？
------------------------------------

  ESP32 支持的双模蓝牙并没有特殊的地方，不需要做复杂的配置或调用即可使用。从开发者的⻆度来看，Bluetooth® LE 调用 Bluetooth LE 的 API，经典蓝牙调用经典蓝牙的 API。

  经典蓝牙与 Bluetooth LE 共存示例可参考 `a2dp_gatts_coex 示例 <https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/coex/a2dp_gatts_coex>`_。

--------------

ESP32 的蓝⽛和 Wi-Fi 如何共存？
----------------------------------

  在 ``menuconfig`` 中，有个特殊选项 ``Software controls WiFi/Bluetooth coexistence``，⽤于通过软件来控制 ESP32 的蓝⽛和 Wi-Fi 共存，可以平衡 Wi-Fi、蓝⽛控制 RF 的共存需求。

  - 如果使能 ``Software controls WiFi/Bluetooth coexistence`` 选项，Bluetooth® LE scan 间隔不应超过 ``0x100 slots`` （约 160 ms）。若只是 Bluetooth LE 与 Wi-Fi 共存，则开启这个选项和不开启均可正常使⽤。但不开启的时候需要注意 Bluetooth LE scan window 应大于 150 ms，并且 Bluetooth LE scan interval 尽量⼩于 500 ms。
  - 若经典蓝⽛与 Wi-Fi 共存，则建议开启这个选项。

---------------

Wi-Fi 和 蓝牙共存时，频繁通信出现 ELxXX error（比如 ELx200）如何解决?
--------------------------------------------------------------------------------------------------

  :CHIP\: ESP32:

  - 该问题目前已在 commit 386a8e37f19fecc9ef62e72441e6e1272fa985b9 修补，请切换至对应的 commit 进行测试。
