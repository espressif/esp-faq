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

  - If you need to change the PSRAM chip, please update configuration options in  "menuconfig -> Component config -> ESP32-specific -> Support for external, SPI-connected RAM -> SPI RAM config -> Type of SPI RAM chip in use".
  - If you cannot find the corresponding type options of the new PSRAM chip you are about to use, please add the chip driver manually.

----------------------

Why is the following error printed when I download the hello-world example into the ESP32-WROOM-32E module?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: c

    E (225) psram: PSRAM ID read error: 0xffffffff
    E (225) spiram: SPI RAM enabled but initialization failed. Bailing out. 

  The reason for the error is that the PSRAM (``Component config`` > ``ESP32-specific`` > ``Support for external, SPI-connected RAM``) setting is enabled in the software, but there is no PSRAM support in the hardware.

--------------

Does ESP32 support coexistence between 16 MB External Flash and 8 MB External PSRAM?
-------------------------------------------------------------------------------------------------

  Yes, ESP32 supports coexistence between 16 MB External Flash and 8 MB External PSRAM.
