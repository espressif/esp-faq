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

When using ESP32 with my product, what is the reason for it not following up after a quick powered-down and then powered-on?
-------------------------------------------------------------------------------------------------------------------------------------------

  Scenario: 220 V to 5 V, and 5 V to 3.3 V power supply. The product failed when powered down and then powered on in 220 V voltage. The error log is as follows:

  .. code-block:: text

    brownout detector was triggered.
    rst:0xc(SW_CPU_RESET),boot:0x13(SPI_FAST_FLASH_BOOT) configsip:0,SPI

  1. The log conveys a message that the voltage has decreased to the threshold of triggering hardware watchdog during the quick powering-down process.
  2. The system did not enter bootloader due to the wrong powering-on timing. This can be resolved by force pulling-down chip_PU.
  3. For more detailed description about the powering-on and reset timing of ESP32, please refer to `ESP32 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_.

--------------

What is the serial port name of Wi-Fi devices？
--------------------------------------------------

 - In Windows system: COM\* 
 - In the Linux subsystem of Windows 10: /dev/ttyS\*
 - In Linux system: /dev/ttyUSB\*
 - In macOS system: /dev/cu.usbserial-\*

--------------

How to block debugging messages sent through UART0 by default?
-------------------------------------------------------------------------

  - For first-stage Bootloader log, connect GPIO15 to Ground.
  - For second-stage Bootloader log, go to make menuconfig > ``Bootloader config`` to do configurations.
  - For ESP-IDF log, go to make menuconfig > ``Component config`` > ``Log output`` to do configurations.

--------------

How to modify the default method of RF calibration in ESP32?
--------------------------------------------------------------------------

  - During RF initialization, the partial calibration solution is used by default. Go to menuconfig and enable the ``CONFIG_ESP32_PHY_CALIBRATION_AND_DATA_STORAGE`` option.

  - If the boot time is not critical, the full calibration solution can be used instead. Go to menuconfig and disable the ``CONFIG_ESP32_PHY_CALIBRATION_AND_DATA_STORAGE`` option.

  - It is recommended to use the **partial calibration** solution, which ensures less boot time and enables you to add the function of erasing RF calibration information in NVS so as to trigger the full calibration operation.

--------------

How to modify the default method of RF calibration in ESP8266?
----------------------------------------------------------------------------
  
  During RF initialization, the partial calibration solution is used by default. The initialization only takes little time. And for this method, the value of byte 115 in esp_init_data_default.bin is ``0x01``. If the boot time is not critical, the full calibration solution can be used instead.

  **For NONOS SDK and earlier versions of RTOS SDK 3.0:**, do either of the followings:

  - Call system_phy_set_powerup_option(3) in function user_pre_init or user_rf_pre_init.
  - In phy_init_data.bin, modify the value of byte 115 to ``0x03``.

  **For RTOS SDK 3.0 and later versions:**

  - Go to menuconfig and disable CONFIG_ESP_PHY_CALIBRATION_AND_DATA_STORAGE.
  - If CONFIG_ESP_PHY_INIT_DATA_IN_PARTITION is enabled in menuconfig, please modify the value of byte 115 in phy_init_data.bin to ``0x03``; If CONFIG_ESP_PHY_INIT_DATA_IN_PARTITION is disabled, please modify the value of byte 115 in phy_init_data.h to ``0x03``.

  **If you use the default partial calibration solution, and want to add the function of triggering the full calibration operation:**

  - For NONOS SDK and earlier versions of RTOS SDK 3.0, please erase the RF parameters to trigger the full calibration operation. 
  - For RTOS SDK 3.0 and later versions, please erase the NVS partition to trigger the full calibration operation.

--------------

How to troubleshoot in ESP32 Boot mode？
------------------------------------------

  By default, the boot information of ESP32-WROVER, which uses 1.8 V flash and psram, is ``0x33`` and ``0x23`` in Download mode. Besides, the boot information of other modules, which use 3.3 V flash and psram, is ``0x13`` and ``0x03`` in Download mode by default. for detailed information, please refer to Section Strapping Pins in `ESP32 Series Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_.

  Thus, when ESP32 is started normally, its boot information should be ``0x13``, and the enabled pins are as the follows:
  - Pins: GPIO12，GPIO0，GPIO2，GPIO4，GPIO15，GPIO5
  - Levels: 0, 1, 0, 1, 0, 1


  - The ESP32-WROVER uses 1.8 V flash and ``0x33`` psram in boot status by default, and the psram is ``0x23`` in download mode.
  - Other modules use 3.3 V flash and ``0x13`` psram by default, and the psram is ``0x03`` in download mode.
  - For detailed information, please refer to Section Strapping Pins in `ESP32 Series Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_. Taken ``0x13`` as an example, the pins are as follows:

  +--------+--------+-------+-------+-------+--------+-------+
  | Pins   | GPIO12 | GPIO0 | GPIO2 | GPIO4 | GPIO15 | GPIO5 |
  +========+========+=======+=======+=======+========+=======+
  | Level  |    0   |   1   |   0   |   1   |    0   |   1   |
  +--------+--------+-------+-------+-------+--------+-------+ 

--------------

When debugging with ESP32 JLINK, an ERROR occurs as: No Symbols For Freertos. How to resolve such issue?
---------------------------------------------------------------------------------------------------------------

  First of all, such issue will not affect your actual operations. Then, you can still find solutions on the community `here <https://community.st.com/s/question/0D50X0000BVp8RtSQJ/thread-awareness-debugging-in-freertos-stm32cubeide-110-has-a-bug-for-using-rtos-freertos-on-stlinkopenocd>`_.

--------------

How to monitor the free space of the task stack?
-----------------------------------------------------

  The function ``vTaskList()`` can be used to print the available space of the task stack regularly.

--------------

Is it possible to use JTAG to debug with ESP32-S2？
-------------------------------------------------------

  Yes. For detailed information, please refer to `ESP32-S2 JATG Debugging <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s2/api-guides/jtag-debugging/>`_.


--------------

How to modify the log output without changing the output level of menuconfig？
-----------------------------------------------------------------------------------

  The output level of log can be modified by using function ``esp_log_level_set()``.

--------------

ESP8266 enters boot mode (2,7) and hits a watchdog reset. What could be wrong?
---------------------------------------------------------------------------------

  - Please make sure that when ESP8266 boots, the strapping pins are held in the required logic levels. If externally connected peripherals drive the strapping pins to an inappropriate logic level, the ESP8266 may boot into an inappropriate mode of operation. In the absence of a valid program, the WDT may then reset the chip.

  - As good design practice, it is recommended that the strapping pins be used to interface to inputs of high impedance external devices only, which do not force the strapping pins high/ low during power-up. For more information, please refer to `ESP8266 Boot Mode Selection <https://github.com/espressif/esptool/wiki/ESP8266-Boot-Mode-Selection>`_.

---------------

When using the ESP-WROVER-KIT board with openocd, an error occurred as: Can't find board/esp32-wrover-kit-3.3v.cfg. How to resolve such issue?
--------------------------------------------------------------------------------------------------------------------------------------------------

  - With 20190313 and 20190708 versions of openocd, please use instruction ``openocd -f board/esp32-wrover.cfg``.
  - With 20191114 and 20200420 (2020 later versions) versions of openocd, please use instruction ``openocd -f board/esp32-wrover-kit-3.3v.cfg``.

--------------

How to obtain and parse coredump with ESP32? 
-------------------------------------------------

  - To obtain the 64 K coredump file from the whole firmware, you need to know its offset from the partition table. If we assume the offset is ``0x3F0000``, the instruction should be as follows:

  .. code-block:: text

    python esp-idf/components/esptool_py/esptool/esptool.py -p /dev/ttyUSB* read_flash 0x3f0000 0x10000  coredump.bin

  - Use the coredump reading script to convert the file obtained at the first step into readable messages. If we assume the coredump file is coredump.bin and the elf file is hello_wolrd.elf, the instruction should be as follows:

  .. code-block:: text

    python esp-idf/components/espcoredump/espcoredump.py info_corefile -t raw -c coredump.bin hello_world.elf

--------------


How to do RF performance test with ESP32&ESP8266&ESP32S2?
--------------------------------------------------------------

- Please refer to `ESP32&ESP8266&ESP32S2 RF Performance Test Demonstration <https://www.espressif.com/sites/default/files/tools/ESP32%26ESP8266_RF_Performance_Test_EN_0.zip>`_.
  
--------------

What could be the reason for PC cannot identify the device under Win 10 system?
-----------------------------------------------------------------------------------

  - Check if the device is identified in the Linux virtual subsystem of Win 10.
  - If the device cannot be identified only in Win 10 system, go to Device Manager to see whether such device exists (e.g., COM x). If the answer is still no, please check your cable and driver.
  - If the device cannot be identified only in Linux virtual subsystem, taken VMWare as an example, please go to "Settings" > "USB Controller" and select "Show all USB input devices".

--------------

One error occurred with ESP32 as: Core 1 paniced(Cache disabled but cache memory region accessed). What could be the reason?
------------------------------------------------------------------------------------------------------------------------------------

  Reason:

  - During the time when cache is disabled (e.g., when using the API spi_flash to read/write/erase/map the SPI flash), an interrupt is generated and the interrupt program accesses the flash resources.
  - It is usually because the processor called programs from the flash and used its constants. One important thing is that since the Double variable is implemented through software, thus when this kind of variable is used in the interrupt programs, it is also implemented in the flash (e.g., forced type conversion operation).

  Solution:
  
  - Add an IRAM_ATTR modifier to the accessed function during interrupt
  - Add an DRAM_ATTR modifier to the accessed constant during interrupt
  - Do not use Double variable in the interrupt programs

--------------

How to read flash model information of the modules?
-----------------------------------------------------------

  - Please use the python script `esptool <https://github.com/espressif/esptool>`_ to read information of Espressif's chips and modules.

  .. code-block:: text

    esptool.py --port /dev/ttyUSB* flash_id





