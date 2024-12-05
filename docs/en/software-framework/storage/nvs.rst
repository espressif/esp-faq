Non-Volatile Storage (NVS)
==========================

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

If data needs to be stored or updated to flash every minute, can ESP32 NVS meet this requirement?
--------------------------------------------------------------------------------------------------------------------------

  According to `NVS Specifications <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/storage/nvs_flash.html>`_, NVS uses two main entities in its operation: pages and entries. Logical page corresponds to one physical sector of flash memory. For now, we assume that flash sector is 4096 bytes and each page can contain 126 entries (32 bytes for one entry), with the left spaces for page header (32 bytes) and entry state bitmap (32 bytes). Typical flash lifetime is 100 k erase cycles. Assuming that the device is expected to run for 10 years, and the data size written to flash is 4 bytes per minute with flash encryption disabled, then the number of flash write operation can be calculated as: 60×24×365×10=5256000. In this way, no more than 42 k of erase cycles (5256000/126) will be caused in NVS, which does not exceed 100 k. Therefore, such operation is supported even without the effects of multiple sectors. In actual use, usually there will be multiple sectors given to NVS, and the NVS can distribute erase cycles to different sectors, making the number of erase cycles in each sector necessarily less than 42 k.

  Therefore, theoretically, NVS can meet the erasure requirements. Please note that the lifespan of different flash models may vary, which should be evaluated based on the actual situation.

--------------

Is it feasible to perform 10,000,000 erase/write operations each time when writing data of 1 KB or less?
--------------------------------------------------------------------------------------------------------

  If each write operation involves 1 KB of data, and the smallest erasable unit of flash is a 4 KB page , then a single erase block can be considered as containing four logical addresses of 1 KB each. Therefore, 10,000,000 write operations are equivalent to 2,500,000 erase/write cycles for a single page (10,000,000 * 1 KB / 4 KB). To avoid exceeding the erase/write cycle limit for each physical block (typically 100,000 cycles), at least 25 physical 4 KB blocks are required to distribute these operations evenly (2,500,000 cycles / 100,000 cycles per block = 25 blocks).

  Considering that the actual available space in each sector may be reduced due to system overhead, and in order to improve the reliability and stability of the system, it is recommended to reserve more physical space. For example, you can allocate about 150 KB of space to ensure sufficient margin to accommodate extra system requirements and future scalability.

--------------

Does NVS have wear levelling function?
-------------------------------------------------

  Yes, NVS (Non-Volatile Storage) has wear leveling functionality. When storing data in flash memory, the limited number of writing and erasing operations to the flash will cause some storage blocks to have shorter service life than others, affecting the overall working life of the memory. To address this issue, NVS uses an erase-write balancing mechanism implemented internally, rather than the wear_levelling component in ESP-IDF, to evenly distribute data across the flash memory blocks, ensuring that each block is used as much as possible to extend the overall working life of the flash memory.

  See more information in `Wear Levelling API <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/storage/wear-levelling.html#api>`_.

--------------

Can NVS sectors be corrupted by accidental power loss during writing?
--------------------------------------------------------------------------------------

  No, NVS is designed to resist accidental power loss, so it will not be damaged.

--------------

Will the configured Wi-Fi SSID and PASSWORD disappear after the ESP series development board is powered on again and need to be reconfigured?
---------------------------------------------------------------------------------------------------------------------------------------------------------------

  - It will be stored in NVS by default and will not disappear due to power failure. You can also set it through ``esp_wifi_set_storage()``, which can be divided into two situations:

    - If you want to save the Wi-Fi SSID and PSAAWORD when powered off, you can store the Wi-Fi information in flash by calling ``esp_wifi_set_storage(WIFI_STORAGE_FLASH)``.
    - If you want to achieve the operation of not saving the Wi-Fi SSID and PASSWORD when powered off, you can call ``esp_wifi_set_storage(WIFI_STORAGE_RAM)`` to store the Wi-Fi information in RAM.

---------------

How to realize that stored user data can be saved after power off, not erased by OTA, and can be re-written or modified?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Non-volatile storage can meet the above requirements, and only eFuse and flash can be used to store the data. Since the data should be modifiable, only flash is suitable. It is recommended to use NVS or MFG mechanism. For details, please refer to

    - `Manufacturing Utility <https://docs.espressif.com/projects/esp-idf/en/release-v5.0/esp32/api-reference/storage/mass_mfg.html#manufacturing-utility>`_    
    - `NVS Partition Generator Utility <https://docs.espressif.com/projects/esp-idf/en/release-v5.0/esp32/api-reference/storage/nvs_partition_gen.html#nvs-partition-generator-utility>`_ 

--------------

Is the API provided by the NVS library thread-safe?
------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The NVS initialization and de-initialization functions are not thread-safe, but other NVS functions (open/get/set/commit/close) are thread-safe.

----------------

What are the meanings of NVS error codes in the ESP-IDF SDK?
----------------------------------------------------------------------------------------------------------------------

  - For the meanings of NVS error codes in the ESP-IDF SDK, refer to `esp-idf/components/nvs_flash/include/nvs.h <https://github.com/espressif/esp-idf/blob/v5.1.2/components/nvs_flash/include/nvs.h#L29>`__.

----------------

Is the cache disabled when writing data to NVS?
-------------------------------------------------------------------------------------------------------

  - When writing data to NVS, the cache will be disabled, and no functions that operate flash can be called within the interrupt function.
