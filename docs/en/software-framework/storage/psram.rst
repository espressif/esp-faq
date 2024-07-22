PSRAM
=====

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

When using ESP32 modules, how to check the size of their PSRAM?
--------------------------------------------------------------------------------

  For ESP32 modules, the `esp_spiram_get_size() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/migration-guides/release-5.x/5.0/system.html?highlight=esp_spiram_get_size#psram>`_ function in ESP-IDF can be used to obtain the size of a module's PSRAM. This function returns the total size of the PSRAM in bytes and can be used for memory allocation and management.

  The following is an example for obtaining the size of PSRAM:

  .. code-block:: c

    size_t psram_size = esp_spiram_get_size();
    printf("PSRAM size: %d bytes\n", psram_size);

  Note that the esp_spiram_get_size() function should be called before using the PSRAM to ensure the correct PSRAM size can be obtained. Additionally, PSRAM functionality should be enabled in ``make menuconfig``, so that PSRAM can be used and configured.
  Furthermore, the PSRAM size can also be obtained in the bootloader log.

--------------

When ESP32 connected to a PSRAM externally, how to change its clock source?
----------------------------------------------------------------------------------------------

  In menuconfig: menuconfig -> Component config -> ESP32-specific -> SPI RAM config.

--------------

When a 8 MB PSRAM mounted on ESP32, why only 4 MB of it is actually mapped?
-----------------------------------------------------------------------------------------------------------------------

  - It is recommended to use the official ESP-PSRAM chip in conjunction with the ESP32 chip.
  - Up to 4 MB (0x3F80_0000 ~ 0x3FBF_FFFF) of external RAM can be mapped into data address space, please refer to the specifications of Section 3.1.4 Memory Map in `ESP32 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_.
  - For a 8 MB PSRAM, you can access the other 4 MB following example `himem <https://github.com/espressif/esp-idf/tree/master/examples/system/himem>`_.

--------------------

I'm using an ESP32 development board with the official PSRAM chip PSRAM64H embedded. But after replacing another type of PSRAM chip to PSRAM64H, it failed to recognize when I ran an ESP-IDF example and enabled the PSRAM configuration. What is the reason?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - To change the model of the PSRAM chip, you need to modify the configuration option in ``menuconfig`` > ``Component config`` > ``ESP32-specific`` > ``Support for external, SPI-connected RAM`` > ``SPI RAM config`` > ``Type of SPI RAM chip in use``.
  - If you cannot find the corresponding type options of the new PSRAM chip you are about to use, please add the chip driver manually.

----------------------

Why is the following error printed when I download the hello-world example into the ESP32-WROOM-32E module?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: c

    E (225) psram: PSRAM ID read error: 0xffffffff
    E (225) spiram: SPI RAM enabled but initialization failed. Bailing out. 

  The error is due to: The PSRAM setting is enabled in the software (``Component config`` > ``ESP32-specific`` > ``Support for external, SPI-connected RAM``), but no available PSRAM was detected on the hardware.

--------------

Does ESP32 support coexistence between 16 MB External Flash and 8 MB External PSRAM?
-------------------------------------------------------------------------------------------------

  Yes, ESP32 supports coexistence between 16 MB External Flash and 8 MB External PSRAM.

--------------

After enabling the ``BT/BLE will first malloc the memory form the PARAM`` configuration option on ESP32-S3-WROOM-N4R2, the software prints the following error log. However, it runs normally after disabling the Bluetooth LE 5.0 configuration. Why?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: c

    E(36997)BLE_INIT:Mallocfailed
    E(37307)BLE_INIT:Mallocfailed
    E(38307)BLE_INIT:Mallocfailed
    E(39307)BLE_INIT:Mallocfailed
    E(40307)BLE_INIT:Mallocfailed

  - The error is caused by insufficient Malloc memory. When the application memory is less than the configuration of ``idf.py menuconfig > ``Component config`` > ``ESP PSRAM`` > ``Support for external, SPI-connected RAM`` > ``SPI RAM config`` > ``(16384) Maximum malloc() size, in bytes, to always put in internal memory``, it will use the chip's internal memory by default. You can reduce this configuration option, or change ``idf.py menuconfig`` > ``Component config`` > ``ESP PSRAM`` > ``Support for external, SPI-connected RAM`` > ``SPI RAM config`` > ``SPI RAM access method`` to ``Make RAM allocatable using heap_caps_malloc(...... MALLOC_CAP_SPIRAM)``.

-------------

Does ESP32-C6 support external PSRAM?
-------------------------------------------------------------------------------------------------------------------

  - ESP32-C6 does not support external PSRAM, but ESP32-C61 supports.

---------

When developing with the ESP32-PICO-V3-02 chip on ESP-IDF v5.1.2, does the PSRAM speed only support 40 MHz?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - PSRAM speed also supports 80 MHz. To set it to 80 MHz, please update the configuration ``idf.py menuconfig`` > ``Serial flasher config`` > ``Flash SPI speed`` to 80 MHz.
  - Typically, we recommend the software settings of 80 MHz flash speed + 80 MHz PSRAM speed.

-------------

When using the `xTaskCreateWithCaps() <https://docs.espressif.com/projects/esp-idf/en/v5.2.1/esp32/api-reference/system/freertos_additions.html#_CPPv419xTaskCreateWithCaps14TaskFunction_tPCKc22configSTACK_DEPTH_TYPEPCv11UBaseType_tP12TaskHandle_t11UBaseType_t>`_ API to allocate external PSRAM, I encountered the following error. Why?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: c

    assert failed: xTaskCreateStaticPinnedToCore freertos_tasks_c_additions.h:314 (xPortcheckValidStackMem(puxStackBuffer))

When using ``xTaskCreateWithCaps()`` to allocate PSRAM, you need to enable the ``Component config`` > ``ESP PSRAM`` > ``Support for external, SPI-connected RAM`` configuration in menuconfig. Then, set the ``SPI RAM config`` > ``SPI RAM access method`` to ``(X) Make RAM allocatable using malloc() as well`` mode. Finally, you need to enable the ``[*] Allow external memory as an argument to xTaskCreateStatic`` configuration option.
