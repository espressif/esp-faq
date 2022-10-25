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
  
  During RF initialization, the partial calibration solution is used by default, in which the value of byte 115 in esp_init_data_default.bin is ``0x01``. The initialization only takes a short time. If the boot time is not critical, the full calibration solution can be used instead.

  **For NONOS SDK and earlier versions of RTOS SDK 3.0**:

  - Call system_phy_set_powerup_option(3) in function user_pre_init or user_rf_pre_init.
  - In phy_init_data.bin, modify the value of byte 115 to ``0x03``.

  **For RTOS SDK 3.0 and later versions**:

  - Go to menuconfig and disable CONFIG_ESP_PHY_CALIBRATION_AND_DATA_STORAGE.
  - If CONFIG_ESP_PHY_INIT_DATA_IN_PARTITION is enabled in menuconfig, please modify the value of byte 115 in phy_init_data.bin to ``0x03``. If CONFIG_ESP_PHY_INIT_DATA_IN_PARTITION is disabled, please modify the value of byte 115 in phy_init_data.h to ``0x03``.

  **If you use the default partial calibration solution, and want to add the function of triggering the full calibration operation:**

  - For NONOS SDK and earlier versions of RTOS SDK 3.0, please erase the RF parameters to trigger the full calibration operation. 
  - For RTOS SDK 3.0 and later versions, please erase the NVS partition to trigger the full calibration operation.

--------------

How to troubleshoot in ESP32 Boot mode？
------------------------------------------

  - The ESP32-WROVER uses 1.8 V flash and PSRAM, which are ``0x33`` by default in boot status and ``0x23`` in download mode.
  - Other modules use 3.3 V flash and PSRAM, which are ``0x13`` by default and ``0x03`` in download mode.
  - For detailed information, please refer to Section Strapping Pins in `ESP32 Series Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_. Taken ``0x13`` as an example, the pins are as follows:

  +--------+--------+-------+-------+-------+--------+-------+
  | Pins   | GPIO12 | GPIO0 | GPIO2 | GPIO4 | GPIO15 | GPIO5 |
  +========+========+=======+=======+=======+========+=======+
  | Level  |    0   |   1   |   0   |   0   |    1   |   1   |
  +--------+--------+-------+-------+-------+--------+-------+ 

--------------

When debugging with ESP32 JLINK, an ERROR occurs as: No Symbols For Freertos. How to resolve such issue?
---------------------------------------------------------------------------------------------------------------

  Such issue will not affect actual operations. For solutions, please go to the `ST Community <https://community.st.com/s/question/0D50X0000BVp8RtSQJ/thread-awareness-debugging-in-freertos-stm32cubeide-110-has-a-bug-for-using-rtos-freertos-on-stlinkopenocd>`_.

--------------

How to monitor the free space of the task stack?
-----------------------------------------------------

  The function ``vTaskList()`` can be used to print the available space of the task stack regularly. For detailed information, please check `CSDN Blog <https://blog.csdn.net/espressif/article/details/104719907>`_.

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

  - Please make sure that when ESP8266 boots, the strapping pins are held in the required logic levels. If externally connected peripherals drive the strapping pins to an inappropriate logic level, ESP8266 may boot into a wrong mode of operation. With the absence of a valid program, the WDT may then reset the chip.

  - Thus, in design practices, it is recommended to only use the strapping pins for input to high resistive external devices so that the Strapping pin is not forced high/low at power-up. For more information, please refer to `ESP8266 Boot Mode Selection <https://github.com/espressif/esptool/wiki/ESP8266-Boot-Mode-Selection>`_.

---------------

When using the ESP-WROVER-KIT board with openocd, an error occurred as: Can't find board/esp32-wrover-kit-3.3v.cfg. How to resolve such issue?
--------------------------------------------------------------------------------------------------------------------------------------------------

  - With 20190313 and 20190708 versions of openocd, please use instruction ``openocd -f board/esp32-wrover.cfg``.
  - With 20191114 and 20200420 (2020 later versions) versions of openocd, please use instruction ``openocd -f board/esp32-wrover-kit-3.3v.cfg``.

--------------

The RTC_watch_dog keeps resetting during ESP32 SPI boot, what is the reason?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Reason: The flash has a requirement for time interval between VDD_SDIO power-up and the first access. For example, GD's 1.8 V flash requires 5 ms of time interval, while the time interval of ESP32 is about 1 ms (XTAL frequency is 40 MHz). Under such condition, the flash access will fail and either timer watchdog reset or RTC watchdog reset is triggered, depending on which one is triggered first. The threshold for RTC watchdog reset is 128 KB cycle, while the threshold for timer watchdog reset is 26 MB cycle. Taking a 40 MHz XTAL clock as an example, when the frequency of RTC slow clock is greater than 192 KHz, RTC watchdog reset will be triggered first, otherwise timer watchdog reset will be triggered. VDD_SDIO will be continuously powered when timer watchdog is reset, so there will be no problem in accessing flash and the chip will work normally. When RTC watchdog is reset, the VDD_SDIO power supply will be disabled and the access to flash will fail, thus the RTC_watch_dog resets continuously.
  - Solution: When an RTC watchdog reset occurs, the power supply to VDD_SDIO is disabled. You can add a capacitor to VDD_SDIO to ensure that the voltage of VDD_SDIO does not drop below the voltage that the flash can tolerate during this period.

--------------

How to obtain and parse coredump with ESP32? 
-------------------------------------------------

  - To obtain the 64 KB coredump file from the whole firmware, you need to know its offset from the partition table. Assuming the offset is ``0x3F0000``, the instruction should be as follows:

  .. code-block:: text

    python esp-idf/components/esptool_py/esptool/esptool.py -p /dev/ttyUSB* read_flash 0x3f0000 0x10000  coredump.bin

  - Use the coredump reading script to convert the file obtained at the first step into readable messages. Assuming the coredump file is coredump.bin and the elf file is hello_wolrd.elf, the instruction should be as follows:

  .. code-block:: text

    python esp-idf/components/espcoredump/espcoredump.py info_corefile -t raw -c coredump.bin hello_world.elf

--------------

How to do RF performance test with ESP32, ESP8266, and ESP32S2?
--------------------------------------------------------------------------------------------

- Please refer to `ESP RF Test Guide <https://www.espressif.com/sites/default/files/tools/ESP_RF_Test_EN.zip>`_.
  
--------------

My PC cannot recognize the device connected in Win10 system. What could be the reasons?
------------------------------------------------------------------------------------------------

  - Check if the device is identified in the Linux virtual subsystem of Win10.
  - If the device cannot be identified only in Win10 system, go to Device Manager to see whether such device exists (e.g., COM x). If the answer is still no, please check your cable and driver.
  - If the device cannot be identified only in Linux virtual subsystem, taken VMWare as an example, please go to "Settings > USB Controller" and select "Show all USB input devices".

--------------

One error occurred with ESP32 as: Core 1 paniced (Cache disabled but cache memory region accessed). What could be the reasons?
------------------------------------------------------------------------------------------------------------------------------------

  Reasons:

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

--------------

What should I do when the Ethernet demo in debugging ESP-IDF outputs the following log？
--------------------------------------------------------------------------------------------

  .. code-block:: text

    emac: Timed out waiting for PHY register 0x2 to have value 0x0243(mask 0xffff). Current value:

  You can refer to the following configurations of the development board. Please see the schematics for details:

    - CONFIG_PHY_USE_POWER_PIN=y
    - CONFIG_PHY_POWER_PIN=5

---------------

I found "Brownout detector was triggered" failure on my ESP32. How to resolve such issue?
------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP32 has a built-in brownout detector which can detect if the voltage is lower than a specific value. If this happens, it will reset the chip in order to prevent unintended behavior.
  - This message may be reported in various scenarios, while the root cause should always be that the chip with a power supply has momentarily or permanently dropped below the brownout threshold. Please try replacing power supply, USB cable, or installing capacitor on power supply terminals of your module.
  - You can do configuration to reset the threshold value or disable the brownout detector. Please refer to `config-esp32-brownout-det <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/kconfig.html#brownout-detector>`_ for details.
  - For ESP32 power-up and reset timing descriptions, see `ESP32 Series Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_.

---------------

After imported the protocol_examples_common.h header file, how come it cannot be found while compling?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32:

  - Please add "set(EXTRA_COMPONENT_DIRS $ENV{IDF_PATH}/examples/common_components/protocol_examples_common)" in CMakeLists.txt under the project.

---------------

When using ESP8266 NonOS v3.0 SDK, the following error occurred. What could be the reasons?
------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    E:M 536    E:M 1528

  Any error logs beginning with E:M indicate insufficient memory.
