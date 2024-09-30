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
------------------------------------------------------------------------------------------

  - For the related protocol, please refer to `ESP32 Serial Protocol <https://github.com/espressif/esptool>`_. For the corresponding documentation, please refer to `Serial Protocol <https://docs.espressif.com/projects/esptool/en/latest/esp32/advanced-topics/serial-protocol.html#serial-protocol>`_.
  - For code examples, please refer to `esp-serial-flasher <https://github.com/espressif/esp-serial-flasher>`_.

--------------

How to download firmware for ESP32 series modules using the USB-Serial tool?
---------------------------------------------------------------------------------------------------------------------

  The methods are as follows:

  +------------+-------+-------+-------+-------+-------+-------+
  |  Modules   | 3V3   | GND   | TXD   | RXD   | IO0   | EN    |
  +============+=======+=======+=======+=======+=======+=======+
  |Serial tool | 3V3   | GND   | RXD   | TXD   | DTR   | RTS   |
  +------------+-------+-------+-------+-------+-------+-------+

  .. note:: For the ESP8266 modules, IO15 should be specially connected to ground.

--------------

How to flash firmware on macOS and Linux?
------------------------------------------------------------------------------------------------

  - For the Apple system (macOS), you can use `esptool <https://github.com/espressif/esptool>`_ downloaded via brew or git to flash firmware.
  - For the Linux system (e.g., Ubuntu), you can use `esptool <https://github.com/espressif/esptool>`_ downloaded via apt-get or git to flash firmware.

--------------

Does ESP32 support programming using JTAG pins directly?
---------------------------------------------------------------------------------------------------

  Yes, ESP32 supports using `JTAG Pins <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/jtag-debugging/configure-other-jtag.html#id1>`_ to flash directly. Please refer to `Upload application for debugging <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/jtag-debugging/index.html#jtag-upload-app-debug>`_.

--------------

Does ESP_Flash_Downloader_Tool support customized programming control?
--------------------------------------------------------------------------------------------

  - The GUI tool is not open-sourced and does not support embedded executive script.
  - The low-level component `esptool <https://github.com/espressif/esptool>`_ is open-sourced and can be used to perform all functions such as flashing and encryption. It is recommended to conduct secondary development based on this component.

---------------

Can I enable the Secure Boot function for ESP32 via OTA?
------------------------------------------------------------------------------------------------

  - It is not recommended to enable Secure Boot through OTA, as it poses operational risks and requires multiple OTA firmware updates.
  - Since the Secure Boot function is in Bootloader, please update Bootloader first to enable this function.

    1. First, check whether the partition table of your current device can store the Bootloader with Secure Boot enabled.
    2. Then, update an intermediate firmware which can be written in the Bootloader partition. By default, the Bootloader partition cannot be erased or written, you need to enable them via `make menuconfig`.
    3. Sign the intermediate firmware and upgrade it to the target device through OTA. Then upgrade the Bootloader of this firmware and the signed new firmware through OTA.
    4. If there are situations such as powered-down or network break-down and restart during the Bootloader OTA process, the device will not be booted and needs to be re-flashed.

--------------

How to resolve the following error that occurred when flashing firmware to ESP32-S2 based on ESP-IDF v4.1?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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


  **Solution:**

  If you are using ESP32-S2 instead of ESP32-S2 Beta, please update ESP-IDF to v4.2 or later versions.

  **Notes:**

  - ESP-IDF v4.1 only supports ESP32-S2 Beta, which is not compatible with ESP32-S2.
  - The version of esptool that comes with ESP-IDF v4.1 is v2.9-dev, which only supports ESP32-S2 Beta as well.
  - Both ESP-IDF v4.2 and its esptool v3.0-dev support ESP32-S2 series chips.

--------------

How to download firmware based on ESP-IDF using flash_download_tool?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Please refer to `get-started-guide <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html>`_ when building an ESP-IDF project for the first time.
  - Taken hello-world example for instance, run ``idf.py build`` (supports ESP-IDF v4.0 and later versions, for versions before v4.0, please use ``make``). After building, the following flash command for the bin file will be generated:

  .. code:: shell

    #Project build complete. To flash, run this command:
    ../../../components/esptool_py/esptool/esptool.py -p (PORT) -b 921600 write_flash --flash_mode dio --flash_size detect --flash_freq 40m 0x10000 build/hello-world.bin  build 0x1000 build/bootloader/bootloader.bin 0x8000 build/partition_table/partition-table.bin
    or run 'idf.py -p PORT flash'

  You can use flash_download_tool to flash according to the bin file and flash address prompted by this command.

--------------

What is the communication protocol for flashing ESP chips?
-------------------------------------------------------------------------------------------------------------------

  - ESP Serial Protocol: `Serial Protocol <https://docs.espressif.com/projects/esptool/en/latest/esp32/advanced-topics/serial-protocol.html>`__.
  - Python-based implementation: `esptool <https://github.com/espressif/esptool>`_.
  - C-language-based implementation: `esp-serial-flasher <https://github.com/espressif/esp-serial-flasher>`_.

--------------

How to program ESP32-C3's firmware offline?
-----------------------------------------------------------------------------------------------------------

  - Currently, no tool supports the offline programming of ESP32-C3's firmware. However, the official `Flash Download Tools <https://www.espressif.com/en/support/download/other-tools>`_ can directly download binary firmware and support mass production download mode for up to eight ESP32-C3 devices at the same time.
  - In addition, we also provide `Test Fixture <https://www.espressif.com/en/products/equipment/production-testing-equipment/overview>`_ for mass production, which supports up to four ESP32-C3 modules to download firmware simultaneously.

----------------------

How does ESP32 set the Flash SPI mode to QIO mode?
----------------------------------------------------------------------------------------------

  It can be set in menuconfig through ``Serial flasher config`` > ``Flash SPI mode``, the corresponding API is `esp_image_spi_mode_t() <https://docs.espressif.com/projects/esp-idf/en/release-v4.4/esp32/api-reference/system/app_image_format.html?highlight=esp_image_spi_mode_t#_CPPv420esp_image_spi_mode_t>`_.

-------------------

After downloading the program and powering on EPS8266, the serial port printed the following log. What is the reason?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    ets Jan  8 2013,rst cause:1, boot mode:(7,7)
    waiting for host

  `waiting for host` means the Boot is in SDIO mode, indicating that GPIO15 (MTDO) is pulled up (HIGH). Please refer to `ESP8266 Boot Mode Description <https://github.com/esp8266/esp8266-wiki/wiki/Boot-Process>`_.

----------------

What are the Espressif module programming tools?
-----------------------------------------------------------------------------------------------------------------

  - For Espressif programming software, please go to `Flash Download Tools <https://www.espressif.com/en/support/download/other-tools>`_. Installation-free GUI tools are for the ``Windows`` environment only.
  - Espressif programming tool `esptool <https://github.com/espressif/esptool>`_ is written based on `Python` with open-source code, supporting secondary development.

-----------------------------------------------------------------------------------------------------

What is the difference between the Factory mode and Developer mode of the flash download tool?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Factory mode supports multi-channel downloads, while Developer mode only supports single channel.
  - The path of bin files under the Factory mode is relative, while under Developer is absolute.

---------------

The ESP32-C3 chip should be able to conduct firmware download through USB, but I failed to do so under ESP-IDF v4.3. So, how can I use USB for firmware download?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  You need to compile under ESP-IDF v4.4 or above versions. After pulling the latest branch and `updating the IDF tool <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/get-started/index.html>`_, you can compile normally and use USB for download. Please refer to `usb-serial-jtag-console <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/api-guides/usb-serial-jtag-console.html>`_.

---------------

Why does the programming fail for the jig with a 4-port hub in factory mode?
------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32 | ESP8266  :

  - It is because Espressif products complete the calibration operation by transmitting some packets when starting up. This operation requires a 3.3 V voltage and a guaranteed peak current of 500 mA. Therefore, when it comes to more than one port, there will be situations where the computer cannot program or the programming is interrupted due to the insufficient power supply of the computer's USB when programming via connecting to a computer's USB. It is recommended to use the hub for programming and supply power to the hub in the meantime.

-------------------

I'm using an ESP32-WROVER-B module to download the AT firmware via the `flash download tool <https://www.espressif.com/en/support/download/other-tools>`_. However, an error occurred after writing to flash. But the same operation succeeded when replacing the module with ESP32-WEOVER-E, what is the reason?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The ESP32-WROVER-B module leads out the SPI flash pin, but the ESP32-WROVER-E module does not. Please check whether the SPI flash pin of the ESP32-WROVER-B module is re-used by other external application circuits.
  - Connecting the CMD pin of the SPI flash in ESP32-WROVER-B to GND will cause the flash to fail to start. The following error log will be printed:

  .. code:: shell

    rst:0x10 (RTCWDT_RTC_RESET),boot:0x1b (SPI_FAST_FLASH_BOOT)
    flash read err, 1000
    ets_main.c 371
    ets Jun 8 2016 00:22:57

---------------

Why can't the `Flash Download Tools <https://www.espressif.com/en/support/download/other-tools>`_ be used to reflash the firmware on a device that has enabled flash encryption but not disabled the download mode?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32 | ESP32-S2:

  - The default configuration of the flash download tool has enabled eFuse verification. If you want to reflash the firmware of a device that has already enabled flash encryption, please modify the following configuration:

    - Modify the default configuration in the `esp32 > security.conf` file, change `flash_force_write_enable = False` to `flash_force_write_enable = True`.
    - Modify the default configuration in the `esp32 > spi_download.conf` file, change `no_stub = False` to `no_stub = True`.
  
  - Note: When reflashing the firmware on devices with flash encryption enabled, the reflashed firmware must use the same flash encryption key. If the keys do not match, the new firmware will not function properly.

-----------------

When updating ESP32 firmware through the UART interface based on `esptool serial port protocol <https://github.com/espressif/esptool>`_, can I add a new app partition?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The partitions in flash depend on the data in partition_table.bin. If partition_table.bin can be updated, the storage space of other data, such as bootloader.bin and app.bin, can be redivided to create an app partition.

---------------------------

I am using ESP8266 to download the firmware via the `flash download tool <https://www.espressif.com/en/support/download/other-tools>`_. After downloading the firmware, there is no programming output log, and the serial port prints the following messages. What could be the reason?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: shell

    ets Jan  8
    2013,rst cause:1, boot mode:(3,7)
    ets_main.c

  - Please check whether the hardware wiring is correct. See `Boot mode wiring instructions <https://docs.espressif.com/projects/esptool/en/latest/esp8266/advanced-topics/boot-mode-selection.html>`_.
  - Please check whether the download offset address of ``bootloader.bin`` is correct. The offset address downloaded from ``bootloader.bin`` of ESP8266 is "0x0". If the offset address is wrong, the flash cannot be started.

----------------

Why does my USB driver fail to be recognized by the Windows 7 system?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Please download and install the `USB Serial JTAG driver <https://dl.espressif.com/dl/idf-driver/idf-driver-esp32-usb-jtag-2021-07-15.zip>` manually for the Windows 7 system.

----------------------------

After using the ESP32-WROVER-E module to download the program, the following log is printed after powered on. What could be the reason?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: shell

      rst：0x10 （RTCWDT_RTC_RESET），boot:0x37（SPI_FLASH_BOOT）
    【2020-12-11 15:51:42 049】invalrd header：0xffffffff
      invalrd header：0xffffffff
      invalrd header：0xffffffff

  - Generally, it is because the GPIO12 was pulled high. It is recommended to pull it low and see the results. Please see `ESP32 Boot Log Guide <https://docs.espressif.com/projects/esptool/en/latest/esp32/advanced-topics/boot-mode-selection.html#select-bootloader-mode>`_.

----------------

When using the `Flash Download Tools <https://www.espressif.com/en/support/download/other-tools>`_ to flash ESP32-C3 via USB, 8-download data fail occurs repeatedly. How can I solve it?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Please erase the chip completely first before flashing.
  - This problem has been solved in V3.9.4 and above versions.

--------------

On ESP32, the bootloader.bin of ESP-IDF v3.0 can not start app.bin of ESP-IDF v5.0. Why?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - When booting the app.bin of ESP-IDF v5.0 with the bootloader.bin of ESP-IDF v3.0, it is necessary to enable the configuration option ``idf.py menuconfig`` > ``Build type`` > ``[*] App compatible with bootloader and partition table before ESP-IDF v3.1`` on ESP-IDF v5.0.

------------

Does ESP32-C3 support disabling ROM code logs via OTA?
----------------------------------------------------------------------------------------------------------------------------------------------------------------

  Yes. You can disable the ROM code log by enabling the `Boot ROM Behavior → Permanently change Boot ROM output → (X) Permanently disable logging` configuration in the software, and then update the firmware via OTA.

--------------

Will the operation of other tasks be affected when the chip is undergoing an OTA firmware upgrade (`esp_ota_write() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/ota.html#_CPPv413esp_ota_write16esp_ota_handle_tPKv6size_t>`_)?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  During the OTA process, the cache will be turned off when writing to the flash, which will affect peripheral interrupts and some SPI tasks. Therefore, it is not recommended to perform other tasks during this period.
