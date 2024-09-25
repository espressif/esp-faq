Security
========

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

Is the firmware in ESP8266 readable?
---------------------------------------------------------

  Yes, because the firmware in ESP8266 is located in the external flash, thus can be read externally. In addition, ESP8266 does not support flash encryption and all the data is written in plaintext.

--------------

Is it possible to encrypt firmware for ESP8285?
--------------------------------------------------------------

  - No, the ESP8285 chip does not support firmware encryption function.
  - Both ESP32 and ESP32-S2 support firmware encryption, thus can be your substitution.
  - If you insist on using ESP8285, you can achieve data encryption by adding an encrypted chip externally.

--------------

What is the difference between secure boot v1 and v2?
------------------------------------------------------
  
  Compared with secure boot v1, secure boot v2 has the following improvements:
  - The bootloader and app use the same signature format.
  - The bootloader and app use the same signing key.

  Currently, `secure boot v1 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/secure-boot-v1.html>`_ is only reommended for earlier versions than ESP32 v3.0. For ESP32 v3.0 and later versions, ESP32-C3, ESP32-S2, and ESP32-S3, it is recommended to use `secure boot v2 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/secure-boot-v2.html>`_.

--------------

After enabling secure boot, there is a build error indicating missing files. What could be the reasons？
-------------------------------------------------------------------------------------------------------------------------------

  Error log: /Makefile.projbuild:7/f/ESP32Root/secure_boot_signing_key.pem

  Reason: security boot is a function for firmware signature verification, which requires generating key pairs.
  - For the method of generating key pairs when enabling secure boot v1, please refer to `secure boot v1 generate key <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/secure-boot-v1.html#secure-boot-generate-key>`_.
  - For the method of generating a key pair when secure boot v2 is enabled, please refer to `secure boot v2 key generation <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/secure-boot-v2.html#generating-secure-boot-signing-key>`_.

--------------

After enabling secure boot, is it possible for modules to be flashed again?
-------------------------------------------------------------------------------------------------

  - If the secure boot v1 is configured as one-time, then it can only be flashed once and the bootloader firmware cannot be reflashed.
  - If the secure boot v1 is configured as reflashable, then the bootloader firmware can be flashed again.
  - The secure boot v2 allows reflashing the bootloader and app firmware.

--------------

With flash encryption enabled, a module reports an error as ``flash read error`` after reflashed. How to resolve such issue?
---------------------------------------------------------------------------------------------------------------------------------------------------

  With flash encryption enabled, the module will not support plaintext firmware flash. For common failures, please refer to `Possible Failures <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/flash-encryption.html#possible-failures>`_. You can use the `espefuse <https://docs.espressif.com/projects/esptool/en/latest/esp32/espefuse/index.html>`_ script to disable the encryption and then reflash the plaintext firmware, or directly flash the encrypted firmware to devices referring to the `flash encryption example <https://github.com/espressif/esp-idf/tree/master/examples/security/flash_encryption>`_.
  
  .. note::
      
      Please note there is a time limit for the flash encrypted function.

--------------

After enabling flash encryption and secure boot for ESP32, how to disable them?
-------------------------------------------------------------------------------------------------

  - If you are using the one-time flash (Release) mode, both flash encryption and secure boot cannot be disabled.
  - If you are using the reflashable (Development (NOT SECURE)) mode, the flash encryption can be disabled, please refer to `Disabling Flash Encryption <https://docs.espressif.com/projects/esp-idf/en/v4.4.2/esp32/security/flash-encryption.html#disabling-flash-encryption>`_; while the secure boot cannot be disabled.

--------------

Is there any security strategy for ESP32 to protect its firmware?
-----------------------------------------------------------------------------------

  - ESP32 supports flash encryption and secure boot.
  - For flash encryption, please refer to `flash encryption <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/flash-encryption.html>`_.
  - For secure boot, please refer to `secure boot <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/secure-boot-v1.html>`_.
  - For secure boot V2, please refer to `secure boot V2 for chip revision v3.0 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/secure-boot-v2.html>`_.

--------------

When ESP32 debugging GDB after enabling flash encryption, why does it continuously reset and restart?
---------------------------------------------------------------------------------------------------------------------------------

  - After ESP32 enabling flash encryption or secure boot, it will restrict JTAG debugging by default, please refer to `Tips and Quirks <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/jtag-debugging/tips-and-quirks.html#jtag-with-flash-encryption-or-secure-boot>`_.
  - You can read the current JTAG status of your chip using the ``espefuse.py summary`` command from esptool.

------------------

How to enable flash encryption for ESP32?
----------------------------------------------------------------------------------------------------------------------------------------

  - It can be enabled via menuconfig or idf.py menuconfig by configuring ``Security features`` -> ``Enable flash encryption on boot (READ DOCS FIRST)``.
  - Please refer to `Flash encryption instructions <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/flash-encryption.html#flash-encryption-process>`_.
  
------------------

After GPIO0 is pulled down, the ESP32 cannot enter download mode and prints "download mode is disable". What could be the reason?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The log means the chip's UART Download mode has been disabled. You can check this via the ``UART_DOWNLOAD_DIS`` bit in `eFuse <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/efuse.html?highlight=download%20mode>`_.
  - Please note that after the Production mode of flash encryption is enabled, the UART Download mode will be disabled by default. For more information, please refer to `UART ROM download mode <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/kconfig.html#config-secure-uart-rom-dl-mode>`_.
  
-----------------------

Can the secure boot function be enabled for ESP32 in Arduino development environment?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - No. If you want to use Arduino for development, the only way to enable the secure boot function is to use Arduino as an IDF component.

------------

What are the use scenarios for secure boot and flash encryption?
--------------------------------------------------------------------

  - When secure boot is enabled, the device will only load and run firmware that is signed by the specified key. Therefore, it can prevent the device from loading illegal firmware and prevent unauthorized firmware from being flashed to the device.
  - When flash encryption is enabled, the partitions on the flash where firmware is stored and the data in the partitions marked as "encrypeted" will be encrypted. Therefore, it can prevent the data from being illegally viewed, and firmware data copied from flash cannot be applied to other devices.

------------

What are the data stored in eFuse involved in secure boot and flash encryption?
----------------------------------------------------------------------------------

  - For the storage used in secure boot v1, please refer to `secure boot v1 efuses <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/secure-boot-v1.html#background>`_.
  - For the data stored in eFuse used in secure boot v2, please refer to `secure boot v2 efuses <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/secure-boot-v2.html#efuse-usage>`_。
  - For the data stored in eFuse used in flash encryption, please refer to `flash encryption efuses <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/flash-encryption.html#relevant-efuses>`_。

------------

Enabling secure boot failed with the log "Checksum failure". How to fix it?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - After enabling secure boot, the size of bootloader.bin will increase, please check whether the size of the bootloader partition is enough to store the compiled bootloader.bin. For more information, please refer to `Bootloader Size <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/bootloader.html#bootloader-size>`_。


NVS encryption failed to start and an error occurred as ``nvs: Failed to read NVS security cfg: [0x1117] (ESP_ERR_NVS_CORRUPT_KEY_PART)``. How can I solve this issue?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Please erase flash once using the flash tool before starting NVS encryption, and then flash the firmware which can enable the NVS encryption to the SoC.


After flash encryption was enabled, a warning occurred as ``esp_image: image at 0x520000 has invalid magic byte (nothing flashed here)``. How can I solve this issue?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - After SoC starts flash encryption, it will try to encrypt the data of all the partitions of the app type. If there is no corresponding app firmware stored in one app partition, the above log will appear. To avoid this warning, you can flash pre-compiled app firmware to the partitions of the app type when starting flash encryption.

Why is reltead data not encrypted after I enable ``CONFIG_EFUSE_VIRTUAL`` and flash encryption?
-----------------------------------------------------------------------------------------------------------

  - Currently, Virtual eFuses is only used to test the update of eFuse data. Thus, flash encryption is not enabled completely even this function is enabled.

Can I update an app firmware which enables flash encryption in a device which does not enable fash encryption through OTA?
-------------------------------------------------------------------------------------------------------------------------------------------

  - Yes, please deselect ``Check Flash Encryption enabled on app startup`` when compiling.

How can I delete keys of secure boot?
--------------------------------------------------

  - Keys of secure boot should be deleted in the firmware ``new_app.bin``. First, please assure that ``new_app.bin`` is employed with two signatures. Then, flash ``new_app.bin`` to the device. At last, when the original signatures are verified, you can delete the original keys through ``esp_ota_revoke_secure_boot_public_key()`` in ``new_app.bin``. Please note that if you use the OTA rollback scheme, please call ``esp_ota_revoke_secure_boot_public_key()`` after ``esp_ota_mark_app_valid_cancel_rollback()`` returns ``ESP_OK``. For more details, please refer to `Key Revocation <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/security/secure-boot-v2.html?highlight=esp_ota_revoke_secure_boot_public_key#key-revocation>`_.

After I enabled secure boot or flash encryption (development mode), I cannot flash the new firmware, and an error occured as ``Failed to enter Flash download mode``. How can I solve this issue?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Generally, the above log indicates that your flash command is incorrect. Please use script ``idf.py`` to execute ``idf.py bootloader`` and ``idf.py app`` to compile ``bootloader.bin`` and ``app.bin``. Then execute the flash command through ``idf.py`` according to the tips after compiling. If you still cannot flash your firmware, please use ``espefuse.py -p PORT summary`` to check the eFuse of the current device and check whether the flash download mode is enabled or not.

----------------------

After I input the command ``espefuse.py read_protect_efuse BLOCK3 command`` in the terminal configured with ESP-IDF to enable the read-protection for Efuse BLOCK3, why is the data of the Efuse BLOCK3 all 0x00 when I input ``esp_efuse_read_block()`` to read the Efuse BLOCK3?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - After the Efuse BLOCK3 is read protected, it cannot be read anymore.

-----------------------------------------

How can I enable secure boot or flash encryption by pre-burning eFuse?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  By default, you can enable secure boot or flash encryption by burning firmware with secure boot or flash encryption enabled. In addition, you can also enable secure boot or flash encryption by pre-burning eFuse in the following two methods:
  - With `flash_download_tool <https://www.espressif.com/zh-hans/support/download/other-tools>`__, eFuse will be pre-burned automatically if secure boot or flash encryption is enabled.
  - You can generate the key and burn corresponding eFuse blocks with `espsecure.py <https://docs.espressif.com/projects/esptool/en/latest/esp32/espsecure/index.html>`__ and `espefuse.py <https://docs.espressif.com/projects/esptool/en/latest/esp32/espefuse/index.html>`__.

------------

After enabling Secure Boot, why can't the new bootloader.bin be flashed using the ``idf.py flash`` command?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - After enabling Secure Boot, compile the new bootloader.bin using the ``idf.py bootloader`` command. Then, flash the new bootloader.bin using the ``idf.py -p (PORT) bootloader-flash`` command.
  - In ESP-IDF v5.2 and later versions, you can also solve this problem by enabling the ``CONFIG_SECURE_BOOT_FLASH_BOOTLOADER_DEFAULT`` option. For details, please refer to `CONFIG_SECURE_BOOT_FLASH_BOOTLOADER_DEFAULT <https://docs.espressif.com/projects/esp-idf/en/release-v5.2/esp32/api-reference/kconfig.html?highlight=secure_boot_flash#config-secure-boot-flash-bootloader-default>`_.

------------

After enabling Secure Boot or flash encryption, how can I view the security-related information in the device?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Please use the command `esptool.py --no-stub get_security_info` to view the security information of the device.

------------

After enabling Secure Boot or flash encryption, what should I pay attention to during OTA (Over-The-Air) updates?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - After enabling Secure Boot, you must sign the new firmware to be used for OTA updates. Otherwise, the new firmware cannot be applied to the device.
  - After enabling flash encryption, when generating a new firmware, please ensure that the flash encryption option is enabled.

---------------

Which USB functions will be disabled after the ESP32-S3 enables flash encryption or `Secure Boot <https://docs.espressif.com/projects/esp-idf/en/release-v5.1/esp32s3/security/secure-boot-v2.html#restrictions-after-secure-boot-is-enabled>`__?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - After enabling flash encryption or secure boot on ESP32-S3, the `USB-JTAG debugging <https://docs.espressif.com/projects/esp-idf/en/release-v5.1/esp32s3/api-guides/jtag-debugging/index.html#jtag-debugging>`__ function will be disabled, and it does not support burning firmware with the `idf.py dfu-flash <https://docs.espressif.com/projects/esp-idf/en/release-v5.1/esp32s3/api-guides/dfu.html#api-guide-dfu-flash>`__ command via the USB interface.
  - After enabling flash encryption or secure boot on ESP32-S3, it supports `USB Host <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/usb/host>`__ and `USB Device <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/usb/device>`__ features; it also supports downloading firmware through the USB interface using the ``idf.py flash`` command.

------------

After enabling flash encryption, if there are multiple flash encryption keys for ``XTS_AES_128_KEY`` in the device's eFuse, how will the device select the key?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The device will always choose the key with the smallest ``Key ID``.

------------

When Secure Boot V2 is enabled, how can I store the public key used for signature verification on the device?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The information of public key is stored in the device's signature block. When Secure Boot V2 is initially enabled, the device will automatically read the public key information from the signature block and write it into the device.

------------

After enabling the Secure Boot V2 feature on ESP series products, is it still possible to reflash the firmware?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - After enabling the Secure Boot V2 feature on ESP series products, if the download mode is not disabled, re-flashing of firmware is supported.
  - Note: For the ESP series chips, when the Secure Boot V2 function is enabled, the default configuration of the Flash Download Tool does not support firmware reflashing. You need to modify the default configuration in the tool to support firmware reflashing. Take ESP32-C3 as an example:

    - Modify the default configuration in the ``esp32c3 > security.conf`` file: Change ``flash_force_write_enable = False`` to ``flash_force_write_enable = True``.
    - Modify the default configuration in the ``esp32c3 > spi_download.conf`` file: Change ``no_stub = False` to `no_stub = True``.
    - If using esptool, run the following command to reflash the firmware:
  
      .. code-block:: c

        esptool.py --chip esp32c3 -p COM68 -b 460800 --before=default_reset --after=no_reset --no-stub write_flash --force --flash_mode dio --flash_freq 80m --flash_size keep 0x0 bootloader.bin 0xF000 partition-table.bin 0x20000 blink.bin 

------------

Does the flash encryption scheme support encryption for the file system?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  It supports encryption on the fatfs file system, but does not support encryption on the spiffs file system.

------------

How to create an encrypted ``nvs_data.bin`` when using NVS encryption?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - When enabling the NVS encryption scheme, the device will not encrypt the NVS data during flashing, so it is necessary to use the `script tool <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/storage/nvs_partition_gen.html#generate-encrypted-nvs-partition>`__ on the PC side to encrypt ``nvs_data.bin``.
  - After enabling the NVS encryption scheme, the device will automatically encrypt NVS data when executing APIs of the ``nvs_set_*`` type; it will automatically decrypt NVS data when executing APIs of the ``nvs_get_*`` type.

-----------------

Does the SPIFFS file system based on ESP32 support the flash encryption scheme?
-------------------------------------------------------------------------------------------------------------------------

  No. The internal structure of SPIFFS does not support integration with flash encryption. If you need a file system that supports 

------------

Using the ESP32-C3 SDK based on ESP-IDF v5.0.6, NVS encryption based on Flash Encryption is enabled in the software configuration. After the device completes Flash Encryption and restarts the firmware, the firmware runs with the following error. What is the reason?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: c

    I (438) main_task: Calling app_main()
    E (438) nvs: Failed to read NVS security cfg: [0x1117] (ESP_ERR_NVS_CORRUPT_KEY_PART)
    ESP_ERROR_CHECK failed: esp_err_t 0x1117 (ESP_ERR_NVS_CORRUPT_KEY_PART) at 0x42007e96
    0x42007e96: app_main at /home/caiguanhong/esp/esp-idf-5.0.6/esp-idf/examples/wifi/getting_started/softAP/build/../main/softap_example_main.c:95 (discriminator 1)

    file: "../main/softap_example_main.c" line 95
    func: app_main
    expression: ret

    abort() was called at PC 0x40386249 on core 0
    0x40386249: _esp_error_check_failed at /home/caiguanhong/esp/esp-idf-5.0.6/esp-idf/components/esp_system/esp_err.c:47

    Stack dump detected
    Core  0 register dump:
    MEPC    : 0x40380938  RA      : 0x40386254  SP      : 0x3fc9a260  GP      : 0x3fc91400  
    0x40380938: panic_abort at /home/caiguanhong/esp/esp-idf-5.0.6/esp-idf/components/esp_system/panic.c:425

    0x40386254: __ubsan_include at /home/caiguanhong/esp/esp-idf-5.0.6/esp-idf/components/esp_system/ubsan.c:313

  - When using `NVS Encryption: Flash Encryption-Based Scheme <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/api-reference/storage/nvs_encryption.html#nvs-encryption-flash-encryption-based-scheme>`_, it is necessary to thoroughly erase the nvs_keys partition before starting the application. Otherwise, the application may generate an `ESP_ERR_NVS_CORRUPT_KEY_PART` error code.
  - Before downloading the firmware, please use the `idf.py erase-flash` command to erase the flash.
