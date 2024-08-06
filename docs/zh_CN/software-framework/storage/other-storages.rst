其他存储相关
============

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

ESP32 是否可以使用 LittleFS 文件系统？
---------------------------------------------------

  LittleFS 为第三方移植组件 `esp_littlefs <https://components.espressif.com/components/joltwallet/littlefs>`_，可直接在 ESP-IDF 中使用。匹配 LittleFS 文件系统镜像的工具为 `mklittlefs <https://github.com/earlephilhower/mklittlefs>`_。

----------------

ESP32 如何查看芯片内存（例如：DRAM、IRAM、rodata）使用情况？
------------------------------------------------------------------------------------------------------------------

  可以在工程终端目录下输入 ``idf.py size-components`` 指令来查看静态存储空间使用估算情况。如需查询运行时内存动态申请信息，请使用 `heap_caps_get_info <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/mem_alloc.html#_CPPv418heap_caps_get_infoP17multi_heap_info_t8uint32_t>`_ 查询。

-----------------

ESP8266 用户可用的 RTC RAM 是多大？
----------------------------------------------------------------------------------------------

  - ESP8266 用户可用的 RTC RAM 为 512 字节 (0x200)。可参见 `esp8266.ld <https://github.com/espressif/ESP8266_RTOS_SDK/blob/release/v3.4/components/esp8266/ld/esp8266.ld>`_ 文件说明。

----------------

如何使能 exFAT？
--------------------------------------------------------------------------------------------------

  :CHIP\: ESP32:

  - 需要在代码中将 #define FF_FS_EXFAT  0 修改为 #define FF_FS_EXFAT  1 , 具体的请参考 `ffconf.h <https://github.com/espressif/esp-idf/blob/178b122c145c19e94ac896197a3a4a9d379cd618/components/fatfs/src/ffconf.h#L255>`_。

----------------

ESP32 分区表中的分区数量有限制吗？
-----------------------------------------------

  - 有限制，分区表的长度为 0xC00 字节（最多可以保存 95 条分区表条目）。参考链接 `分区表 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/partition-tables.html>`_ 的说明。

----------------

ESP32 如何读取芯片剩余内存？
--------------------------------------------------------------------------------------------------

  - 可通过 `esp_get_free_heap_size() <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/system/misc_system_api.html#id3>`__ 来读取芯片 RAM 剩余内存。

---------------

在 ESP-IDF 下使用 xTaskCreateStatic() 需要注意什么？
-----------------------------------------------------------------------------------------------------------------------------------------------------

  - 可以参考 `xTaskCreateStatic() 说明 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/system/freertos_idf.html#_CPPv417xTaskCreateStatic14TaskFunction_tPCKcK8uint32_tPCv11UBaseType_tPC11StackType_tPC12StaticTask_t>`__。
