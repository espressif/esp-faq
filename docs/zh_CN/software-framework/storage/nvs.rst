非易失性存储 (NVS)
====================

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

若每分钟保存或者更新数据到 flash 中，ESP32 设备的 NVS 能否满足该需求？
----------------------------------------------------------------------------------

  根据 `NVS 说明 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/storage/nvs_flash.html>`_，NVS 库在其操作中主要使用两个实体：页面和条目。逻辑页面对应 flash 的一个物理扇区。假设 flash 扇区大小为 4096 字节，每个页面可容纳 126 个条目（每个条目大小为 32 字节），页面的其余部分用于页头部（32 字节）和条目状态位图（32 字节）。每个扇区的典型 flash 寿命为 100 k 个擦除周期。假设期待设备的运行时间为 10 年，每分钟写入 flash 的数据大小为 4 字节，并且不使用 flash 加密，计算 flash 写操作的次数为：60×24×365×10=5256000。这样，在 NVS 中会导致不超过 42 k 个擦除周期 (5256000/126)，而 42 k < 100 k，因此，即使在没有多扇区影响的情况下也可以支持。在实际使用中，分配给 NVS 的大小一般为多个扇区，NVS 会在多扇区之间分配擦除周期，那么每个扇区的擦除周期的次数必然小于 42 k。

  因此，NVS 可以满足该擦写需求。

--------------

NVS 是否具有磨损均衡？
----------------------------

  是，NVS 使用的不是 ESP-IDF 中的 wear_levelling 组件，而是在其内部实现的一种擦写平衡机制，使用中 flash 磨损是处于均衡状态。

--------------

NVS 扇区是否会因写入时意外断电而损坏？
------------------------------------------------

  NVS 设计之初就具有抵抗意外断电的能力，因此不会损坏。

--------------

ESP32 是否可以在外挂的 SPI flash 中挂载文件系统分区？
---------------------------------------------------------------

  在 ESP-IDF v4.0 以及之后的版本添加了该功能。需要注意的是，当挂载了两个分区时，不能多个任务同时向一个分区写入文件。

--------------

配置好的 Wi-Fi SSID 和 PASSWORD 在 ESP 系列开发板上重新上电后是否会消失，需要重新输入吗？
------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 默认会存在 NVS 里，不会因为掉电而消失，您也可以通过 ``esp_wifi_set_storage()`` 设置，此时分为两种情况：

    - 如果想要实现掉电保存 Wi-Fi SSID 和 PSAAWORD，可通过调用 ``esp_wifi_set_storage(WIFI_STORAGE_FLASH)`` 将 Wi-Fi 信息存储在 flash 内。
    - 如果想要实现掉电不保存 Wi-Fi SSID 和 PASSWORD 的操作，可通过调用 ``esp_wifi_set_storage(WIFI_STORAGE_RAM)`` 将 Wi-Fi 信息存储在 RAM 内。
