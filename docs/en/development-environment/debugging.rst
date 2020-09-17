Debugging
=========

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

How to troubleshoot in ESP32 Boot mode？
------------------------------------------

  By default, the boot information of ESP32-WROVER, which uses 1.8 V flash and psram, is ``0x33`` and ``0x23`` in Download mode. Besides, the boot information of other modules, which use 3.3 V flash and psram, is ``0x13`` and ``0x03`` in Download mode by default. for detailed information, please refer to Section Strapping Pins in `ESP32 Series Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_.

  Thus, when ESP32 is started normally, its boot information should be ``0x13``, and the enabled pins are as the follows:
  - Pins: GPIO12，GPIO0，GPIO2，GPIO4，GPIO15，GPIO5
  - Levels: 0, 1, 0, 1, 0, 1

--------------

How can I make sending messages by UART0 disabled by default?
---------------------------------------------------------------

  - For first-stage Bootloader log, connect GPIO15 to Ground.
  - For second-stage Bootloader log, go to make menuconfig > ``Bootloader config`` to do configurations.
  - For ESP-IDF log, go to make menuconfig > ``Component config`` > ``Log output`` to do some configurations.

--------------

How can I modify the default method of RF calibration in ESP32?
-----------------------------------------------------------------

  - During RF initialization, the partial-calibration method is used by default for RF calibration.

    To use this method, please go to menuconfig and enable ``CONFIG_ESP32_PHY_CALIBRATION_AND_DATA_STORAGE``.

  - If boot duration is not critical, please use the overall-calibration method instead. 

    To switch to the overall-calibration method, go to menuconfig and disable ``CONFIG_ESP32_PHY_CALIBRATION_AND_DATA_STORAGE``.

  - It is recommended to use the **partial calibration** method, which ensures less boot time and enables you to add the function of triggering overall calibration as a last-resort remedy by erasing the NVS partition.

--------------

How can I modify the default method of RF calibration in ESP8266?
---------------------------------------------------------------------
  
  During RF initialization, the partial-calibration method is used by default for RF calibration. The initialization only takes little time, and for this method, the value of byte 115 in esp_init_data_default.bin is ‘0x01’. If boot duration is not critical, please use the overall-calibration method instead.

  **For NONOS SDK and versions of RTOS SDK earlier than 3.0**, do either of the following:

  - Call system_phy_set_powerup_option(3) in the function user_pre_init or user_rf_pre_init.
  - In phy_init_data.bin, modify the value of byte 115 to ‘0x03’.

  **For RTOS SDK 3.0 and later versions:**

  - Go to menuconfig and disable CONFIG_ESP_PHY_CALIBRATION_AND_DATA_STORAGE.
  - If CONFIG_ESP_PHY_INIT_DATA_IN_PARTITION is enabled in menuconfig, please modify the value of byte 115 in phy_init_data.bin to ‘0x03’; If CONFIG_ESP_PHY_INIT_DATA_IN_PARTITION is disabled, please modify the value of byte 115 in phy_init_data.h to ‘0x03’.

  **If you use the default method of RF calibration, and want to add the function of triggering overall calibration as a last-resort remedy:**

  - For NONOS SDK and versions of RTOS SDK earlier than 3.0: Please erase the RF parameters to rigger overall calibration. 
  - For RTOS SDK 3.0 and later versions: Please erase the NVS partition to trigger overall calibration.

---------------

ESP8266 enters boot mode (2,7) and hits a watchdog reset. What could be wrong?
---------------------------------------------------------------------------------

  Please make sure that when ESP8266 boots, the strapping pins are held in the required logic levels. If externally connected peripherals drive the strapping pins to an inappropriate logic level, the ESP8266 may boot into an inappropriate mode of operation. In the absence of a valid program, the WDT may then reset the chip.

  As good design practice, it is recommended that the strapping pins be used to interface to inputs of high impedance external devices only, which do not force the strapping pins high/ low during power-up. For more information, please refer to `ESP8266 Boot Mode Selection <https://github.com/espressif/esptool/wiki/ESP8266-Boot-Mode-Selection>`_.
