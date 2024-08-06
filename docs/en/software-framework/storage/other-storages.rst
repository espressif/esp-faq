Other Storages
==============

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

Can ESP32 use LittleFS file system?
------------------------------------------------------

  LittleFS is a third-party component `esp_littlefs <https://components.espressif.com/components/joltwallet/littlefs>`_, which can be used directly in ESP-IDF. You can use the `mklittlefs <https://github.com/earlephilhower/mklittlefs>`_ tool for the image of LittleFS file system.

----------------

How to check the memory usage (e.g., DRAM, IRAM, rodata) of ESP32 chips?
------------------------------------------------------------------------------------------------------------------

  You can check the estimated occupied static storage of ESP32 chips by inputting the instruction ``idf.py size-components`` under corresponding directories in terminal. You can use `heap_caps_get_info <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/mem_alloc.html#_CPPv418heap_caps_get_infoP17multi_heap_info_t8uint32_t>`_ to obtain dynamic applied memory during operation.

-----------------

What is the available size of RTC RAM in ESP8266 for users?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The available RTC RAM in ESP8266 for users is 512 bytes (0x200). Please see descriptions in`esp8266.ld <https://github.com/espressif/ESP8266_RTOS_SDK/blob/release/v3.4/components/esp8266/ld/esp8266.ld>`_.

----------------

How to enable exFAT?
--------------------------------------------------------------------------------------------------

  :CHIP\: ESP32:

  - please modify #define FF_FS_EXFAT  0 as #define FF_FS_EXFAT  1 , please reffer to `ffconf.h <https://github.com/espressif/esp-idf/blob/178b122c145c19e94ac896197a3a4a9d379cd618/components/fatfs/src/ffconf.h#L255>`_ for details.

----------------

Is there a limit to the number of partitions in the partition table of ESP32?
---------------------------------------------------------------------------------------

  - Yes. The length of partition table is 0xC00 bytes (can store up to 95 partition table entries). Please refer to the description in `partition table <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/partition-tables.html>`_.

----------------

How to read the remaining memory of the ESP32 chip?
-------------------------------------------------------------------------------------------------------------------------------

  - The remaining memory of the chip RAM can be read through `esp_get_free_heap_size() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/misc_system_api.html#heap-memory>`__.

---------------

What should I pay attention to when using ``xTaskCreateStatic()`` in ESP-IDF?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - You can refer to the `xTaskCreateStatic() description <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/freertos_idf.html#_CPPv417xTaskCreateStatic14TaskFunction_tPCKcK8uint32_tPCv11UBaseType_tPC11StackType_tPC12StaticTask_t>`__.
