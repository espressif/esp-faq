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
--------------------------------------------------------

  Yes, because the firmware in ESP8266 is located in the external flash, thus can be read externally. In addition, ESP8266 does not support flash encryption and all the data is written in plaintext.

--------------

Is it possible to encrypt firmware for ESP8285?
--------------------------------------------------------------

  - No, the ESP8285 chip does not support firmware encryption function.
  - Both ESP32 and ESP32-S2 support firmware encryption, thus can be your substitution.
  - If you insist on using ESP8285, you can achieve data encryption by adding an encrypted chip externally.

--------------

After enabling secure boot, there is a build error indicating missing files. What could be the reasons？
-------------------------------------------------------------------------------------------------------------------------------

  Error log: /d/ESP32/esp-mdf/esp-idf/components/bootloader_support/Makefile.projbuild:7/f/ESP32Root/secure_boot_signing_key.pem。

  Reason: security boot is a function for firmware signature verification, which requires generating a pair of certificates. For detailed information, please refer to `Secure Boot <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/secure-boot-v1.html>`_.

--------------

After enabling secure boot, is it possible for modules to be flashed again?
-------------------------------------------------------------------------------------------------

  - If the secure boot is configured as one-time, then it can only be flashed once and the bootloader firmware cannot be reflashed.
  - If the secure boot is configured as reflashable, then the bootloader firmware can be flashed again.

--------------

With flash encrypted enabled, a module has an error as ``flash read error`` after reflashed. How to resolve such issue?
---------------------------------------------------------------------------------------------------------------------------------------------------

  With flash encrypted enabled, the module will not support plaintext firmware flash. You can reflash it after disabling the encryption function via espefuse.py, or used the encryption key to flash ciphertext.
  
  .. note::
      
      Please note there is a time limit for flash encrypted function: it can only be enabled and disabled for 3 times.

--------------

After enabling flash encryption and secure boot for ESP32, how to disable them?
-------------------------------------------------------------------------------------------------

  - If you are using the one-time flash (Release) mode, both flash encryption and secure boot cannot be disabled.
  - If you are using the reflashable (Development (NOT SECURE)) mode, the flash encryption can be disabled, please refer to `Disabling Flash Encryption <https://docs.espressif.com/projects/esp-idf/en/release-v4.1/security/flash-encryption.html#disabling-flash-encryption>`_; while the secure boot cannot be disabled.

--------------

Is there any security strategy for ESP32 to protect its firmware?
-----------------------------------------------------------------------------------

  - ESP32 supports flash encryption and secure boot.
  - For flash encryption, please refer to `flash encryption <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/flash-encryption.html>`_.
  - For secure boot, please refer to `secure boot <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/secure-boot-v1.html>`_.
  - For secure boot V2, please refer to `ECO3 Chip secure boot V2 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/secure-boot-v2.html>`_.

--------------

When ESP32 debugging GDB after enabling flash encryption, why does it always continue to reset and restart?
---------------------------------------------------------------------------------------------------------------------------------

  - After ESP32 enabling flash encryption or secure boot, it will restrict JTAG debugging by default, please refer to `Tips and Quirks <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/jtag-debugging/tips-and-quirks.html#jtag-with-flash-encryption-or-secure-boot>`_.
  - You can read the current JTAG status of your chip using the ``espefuse.py summary`` command from esptool.

------------------

How to enable flash encryption for ESP32?
----------------------------------------------------------------------------------------------------------------------------------------

  - It can be enabled via `make menuconfig` or `idf.py menuconfig --> Security features --> Enable flash encryption on boot (READ DOCS FIRST)` configurations.
  - Please refer to `Flash encryption instructions <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/flash-encryption.html#flash>`_.
  
------------------

After GPIO0 is pulled down, the ESP32 cannot enter download mode and prints "download mode is disable". What is the reason?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - It means the chip's UART Download mode has been disabled, you can check this via the ``UART_DOWNLOAD_DIS`` bit in `efuse <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/efuse.html?highlight=download%20mode>`_.
  - Please note that after the Production mode of flash encryption is enabled, the UART Download mode will be disabled by default. For more information, please refer to `UART ROM download mode <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/kconfig.html#config-secure-uart-rom-dl-mode>`_.
  
