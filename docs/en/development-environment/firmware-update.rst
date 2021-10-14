Firmware update
===============

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

How does the host MCU flash ESP32 via serial interfaces?
----------------------------------------------------------------

  - For the related protocol, please refer to `ESP32 Serial Protocol <https://github.com/espressif/esptool/wiki/Serial-Protocol>`_.
  - For code examples, please refer to `esp-serial-flasher <https://github.com/espressif/esp-serial-flasher>`_.

--------------

How to automatically flash Espressif's modules using the USB-Serial tool?
------------------------------------------------------------------------------------

  The methods are as follows:

  +------------+-------+-------+-------+-------+-------+-------+
  |  Modules   | 3V3   | GND   | TXD   | RXD   | IO0   | EN    |
  +============+=======+=======+=======+=======+=======+=======+
  |Serial tool | 3V3   | GND   | RXD   | TXD   | DTR   | RTS   |
  +------------+-------+-------+-------+-------+-------+-------+

  .. note:: For ESP8266 modules, IO15 should be specially connected to ground.

--------------

How to flash firmware in macOS and Linux systems?
------------------------------------------------------------

  - For Apple system (macOS), you can use `esptool <https://github.com/espressif/esptool>`_ downloaded via brew or git to flash firmware.
  - For Linux system (e.g., ubuntu), you can use `esptool <https://github.com/espressif/esptool>`_ downloaded via apt-get or git to flash firmware.

--------------

Does ESP32 support programming using JTAG pins directly?
--------------------------------------------------------------------

  Yes, please refer to `JTAG Debugging <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/jtag-debugging/index.html#jtag-upload-app-debug>`_.

--------------

Does ESP_Flash_Downloader_Tool support customized programming control？
--------------------------------------------------------------------------------------------

  - The GUI tool is not open sourced and does not support embedded executive script.
  - The low-level component ESPtool is open sourced and can be used to perform functions such as flashing and encryption. It is recommended to conduct secondary development based on this component.

---------------

Can I enable the Security Boot function for ESP32 via OTA?
------------------------------------------------------------------------------------------------

  - This is not recommended since it may cause risks and needs to upgrade OTA firmware for multiple times.
  - Since the Security Boot function is in Bootloader, please update Bootloader first to enable this function.

    1. First, check the partition table of your current device to see if it can store the Bootloader with Security Boot function enabled.
    2. Then, update an intermediate firmware which can be written in Bootloader partition. By default, the Bootloader partition cannot be erased or written, you need to enable them via `make menuconfig`.
    3. Sign the intermediate firmware and upgrade it to the target device through OTA. Then upgrade the Bootloader of this firmware and the signed new firmware through OTA.
    4. If there are situations as powered-down or network break-down and restart during the Bootloader OTA process, the device cannot be started and needs to be re-flashed.
 
--------------

When flashing firmware to ESP32-S2, an error occurred as “A fatal error occurred: Invalid head of packet (0x50)”. How to resolve such issue?
--------------------------------------------------------------------------------------------------------------------------------------------------------

  **Scenario:**

  When flashing firmware to an ESP32-S2 device based on ESP-IDF v4.1, the following error code occurred:

  .. code-block:: shell

    esptool.py v2.9-dev
    Serial port /dev/ttyUSB0
    Connecting....
    Chip is ESP32S2 Beta
    Features: Engineering Sample
    Crystal is 40MHz
    MAC: 7c:df:a1:01:b7:64
    Uploading stub...
    Running stub...

    A fatal error occurred: Invalid head of packet (0x50)
    esptool.py failed with exit code 2

  **Solution**

  If the chip you are using is ESP32-S2, not ESP32-S2 Beta, please update ESP-IDF to v4.2 or later versions.

  **Notes:**

  - ESP-IDF v4.1 only supports ESP32-S2 Beta, which is not compatible with ESP32-S2.
  - The version of esptool came with ESP-IDF v4.1 is v2.9-dev, which also only supports ESP32-S2 Beta.
  - ESP-IDF v4.2 supports ESP32-S2 chips, and its esptool is v3.0-dev, which supports ESP32-S2 too.

--------------

How to download firmware based on esp-idf using flash_download_tool?
------------------------------------------------------------------------------

  - Taken hello-world example for instance, please refer to `get-started-guide <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html>`_ when building an esp-idf project for the first time.
  - Run ``idf.py build`` (Only for esp-idf v4.0 or later versions. Please use ``make`` for previous versions). After the build finished, the following flash command for the bin file will be generated:

  .. code:: shell 

    #Project build complete. To flash, run this command:
    ../../../components/esptool_py/esptool/esptool.py -p (PORT) -b 921600 write_flash --flash_mode dio --flash_size detect --flash_freq 40m 0x10000 build/hello-world.bin  build 0x1000 build/bootloader/bootloader.bin 0x8000 build/partition_table/partition-table.bin
    or run 'idf.py -p PORT flash'

--------------
  
What is the communicationg protocol for flashing ESP chips?
----------------------------------------------------------------------

  - ESP Serial Protocol: `Serial-Protocol <https://github.com/espressif/esptool/wiki/Serial-Protocol>`_.
  - Python-based implementation: `esptool <https://github.com/espressif/esptool>`_.
  - C-language based implementation: `esp-serial-flasher <https://github.com/espressif/esp-serial-flasher>`_.

--------------

How to program ESP32-C3's firmware offline?
--------------------------------------------------------------------------------

   - Download the latest Flash Download Tools from espressif.com. Versions after v3.8.8 and later versions already support ESP32-C3 series programming.

----------------------

How does ESP32 set Flash SPI to QIO mode?
----------------------------------------------------------------------------------------------

  - It can be set in configuration terminal through "menuconfig -> Serial flasher config -> Flash SPI mode" , the corresponding API is esp_image_spi_mode_t();
  - It can also be configured using the `Flash download tools <https://www.espressif.com/sites/default/files/tools/flash_download_tool_v3.8.8_0.zip>`_.
  
