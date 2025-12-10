Production Test
===================

:link_to_translation:`zh_CN:[中文]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

---------------

Why can some modules download firmware normally when using DIO/DOUT, but encounter program abnormality when using QOUT/QIO?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Firstly, please check the modes supported by flash in the module and whether the module routing meets the requirements of modes.
  - Secondly, please check the QE bit of the status register of flash, which determines whether the flash supports the QUAD mode or not.
  - Different ESP chips/modules use flashes from different manufacturers. Some flashes have QE disabled by default. Thus, it is necessary to check whether the flash supports Quad mode through actual testing.
  - When ROM boots a second stage bootloader, the secondary read will fail if the configuration parameters are read in the QIO mode because the QE bit is disabled.
  - It is recommended to program firmware in the DIO mode and to configure the QIO mode in ``menuconfig``. The configuration enables the QE bit in the second stage bootloader and then boots the app bin to use the QUAD mode.

---------------

How to get the production test tool?
------------------------------------------------------------

  :CHIP\: ESP32 | ESP8266:

  - Please click `production test tool <https://download.espressif.com/fac_tool_release/Qrelease/the_latest_release/ESP_PRODUCTION_TEST_TOOL_NORMAL.zip>`_ to download.

----------------

When I use the ``esptool.py burn_custom_mac`` command to write the user-defined MAC address, why is the MAC address read by the ``esptool.py read_mac`` command still factory default?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The ``esptool.py read_mac`` command can only read the MAC address written in eFuse BLOCK0 by default, but the user-defined MAC address written with the ``esptool.py burn_custom_mac`` command is in eFuse BLOCK3. You may use the ``espefuse.py get_custom_mac`` command to check the MAC address written to eFuse BLOCK3.
  - For more information, please refer to `esptool documentation <https://docs.espressif.com/projects/esptool/en/latest/esp32/>`__.

---------------

When downloading bin files to ESP32-WROVER-E (16 MB flash) using Flash Download Tool, multiple separate bin files can be downloaded successfully, but downloading the combined firmware (12 MB) failed. Why?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Since the combined firmware is mostly "0xFF" with relatively high compression rate, the amount of data after decompression would be relatively large for the same length of compressed data, resulting in a timeout error (default 7 seconds) after a long download time. To solve this issue, in Flash Download Tool, go to ``configure`` > ``esp32`` > ``spi_download``, and disable the compression configuration option as follows:

  .. code-block:: c

    compress = False
    no_compress = True

Where can I find the MTBF report for a chip or module?
------------------------------------------------------

MTBF (Mean Time Between Failures) values are not publicly provided. MTBF can vary widely depending on test scope, operating conditions, and actual application scenarios. Publishing a single number may cause misunderstanding or lead to incorrect conclusions for real-world use.
