Hardware design
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

The I2S pins of ESP32 are scattered. Can I route I2S signals to adjacent pins? For example, to ``GPIO5, GPIO18, GPIO23, GPIO19, and GPIO22``, or to ``GPIO25, GPIO26, GPIO32, and GPIO33``.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - All I2S signals can be routed to different I/Os freely. Please note that some I/Os can only be set as input. For details, please refer to Section *Peripheral Pin Configurations* and Appendix *IO_MUX* in the `ESP32 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_.

--------------------

How can I stop the voltage through VDD3P3_RTC from going down after ESP32 enters Light-sleep mode?
-----------------------------------------------------------------------------------------------------------

  - After ESP32 enters Light-sleep mode, the GPIOs powered by VDD3P3_RTC are pulled down. This is usually because the RTC powers down during Light-sleep mode.
  - Please use ``esp_sleep_pd_config(ESP_PD_DOMAIN_RTC_PERIPH, ESP_PD_OPTION_ON)`` to maintain the power supply for RTC.

--------------

What should be noted when I configure the pins of ESP32?
---------------------------------------------------------

  - You may assign most of the digital peripherals to any pins through GPIO Matrix. However, functions such as SDIO, high speed SPI, and analog can only be realized via IO MUX.
  - For details, please refer to `GPIO & RTC GPIO <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/gpio.html>`_.

  .. note::
    - Strapping pins have default levels. Please refer to `ESP32 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`__.
    - GPIO34 ~ GPIO39 can only be set as input without software-enabled pull-up or pull-down functions.
    - GPIO6 ~ GPIO11 are saved for flash.
    - GPIO1 and GPIO3 are the TX and RX pins for UART0, which cannot be configured.
    - GPIO16 and GPIO17 are saved for PSRAM if there is any.

--------------

What is the voltage tolerance of GPIOs of ESP chips?
----------------------------------------------------------------

  - The voltage tolerance is 3.6 V. If the voltage exceeds 3.6 V, please add a voltage divider to protect GPIO pins from damage.

-------------

What are the power supply specifications for ESP8266?
--------------------------------------------------------------------

  - Digital working voltage range: 1.8 V ~ 3.3 V
  - Analog working voltage range: 3.0 V ~ 3.6 V (the lowest possible value is 2.7 V)
  - Peak analog circuit current: 350 mA
  - Peak digital circuit current: 200 mA
  
  .. note:: The operating voltage of SPI flash should be compatible with that of GPIO pins. The operating voltage of CHIP_EN ranges from 3.0 V to 3.6 V, so please use a level converter when GPIO pins operates at 1.8 V.

--------------

Do Espressif Wi-Fi modules support single-layer PCBs?
-----------------------------------------------------

  - The ESP32 module is a wireless device. It needs PCB materials that fulfills its RF performance requirements. We have tested four-layer and two-layer PCBs, but not single-layer ones.
  - Single-layer PCBs are not recommended as RF performance cannot be guaranteed. You may use single-layer PCBs in your end products and then mount Espressif modules.
  - Four-layer PCBs are recommended for desired RF performance.

----------------

What should be noted when I power ESP8266 with batteries?
----------------------------------------------------------

  - The operating voltage of ESP8266 ranges from 3.0 V to 3.6 V, so two AA batteries can be used to power ESP8266. Please ensure the battery voltage stays within the operating range of ESP8266 when it drops.
  - If the lithium battery voltage surpasses module operating voltage, and the voltage drops heavily during discharge, then such batteries should not be used to power ESP8266.
  - We recommend you to use DC/DC converters or LDO regulators to convert voltage before powering ESP8266. Please pay attention to the difference between the input and output voltages of converters or regulators.

------------------------

Where can I find the footprint of ESP32 Series?
-----------------------------------------------

  You may find the footprint in the PCB layout of different modules. Please refer to `reference designs <https://www.espressif.com/en/support/documents/technical-documents?keys=&field_download_document_type_tid%5B%5D=519>`_.

-----------------

For ESP32-S2 chips, can I have audio connection when the DVP camera interface is in use?
-----------------------------------------------------------------------------------------

  The LCD, DVP camera, and I2S interfaces of ESP32-S2 share one set of hardware, so they cannot be used at the same time.

-------------

What should be noted when I assign I2C signals to GPIO0 and GPIO4 of ESP32 modules?
--------------------------------------------------------------------------------------

  Please pull GPIO0 up when assigning I2C signals to the pin. Only pull GPIO0 down when flashing firmware on ESP32 modules.

----------------

When the external flash is connected to GPIO6 ~ GPIO11, can they be set as SPI pins?
-------------------------------------------------------------------------------------

  When the external flash is connected to GPIO6 ~ GPIO11, they cannot be set as SPI pins.

------------------

Do I need to connect an external crystal when using the ESP8285 chip?
---------------------------------------------------------------------------------

  You need to connect an external crystal, as the chip has no internal crystal.

-----------------

Where can I find the reference design for connecting an external PSRAM to ESP32-D2WD?
--------------------------------------------------------------------------------------

  You may refer to the design for the external PSRAM of ESP32-PICO-D4. Please refer to Chapter *Peripheral Schematics* in the `ESP32-PICO-D4 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32-pico-d4_datasheet_en.pdf>`_.

  .. note:: ESP32-D2WD has an 1.8 V flash, so please add a resistor and a capacitor to VDD_SDIO and connect an 1.8 V PSRAM.

------------------

Can I use ESP32 to play music with PWM or DAC?
----------------------------------------------

  You may use ESP32 to play music with PWM or DAC, and we recommend you play voice prompts. To run a test, please refer to `esp-adf/examples/player/pipeline_play_mp3_with_dac_or_pwm <https://github.com/espressif/esp-adf/tree/master/examples/player/pipeline_play_mp3_with_dac_or_pwm>`_.

------------

Why is the suggested voltage range of ESP32 modules diffrent from that of ESP32 chips?
--------------------------------------------------------------------------------------

  - For modules, the flash voltage needs to be considered. That is why the module voltage is greater.
  - For more information, please check `module and chip datasheets <https://www.espressif.com/en/support/documents/technical-documents>`_.

--------------

Why does it take a longer time to erase the flash of self-developed modules than that of Espressif modules?
-------------------------------------------------------------------------------------------------------------

  - It is common that the erasing time vaires, as it depends on factors such as the manufacturer of your flash and the size of the block you erase.
  - If you want to shorten the erasing time, you may test flash memories from different manufacturers.

------------

Why does the current surge when ESP8266 is powered on?
-----------------------------------------------------------

  - The RF and digital circuits of ESP8266 are highly integrated. When ESP8266 is powered on, the RF automatic calibration starts to work, which requires high current.
  - The maximal current of the analog circuit can reach 500 mA, while that of the digital circuit is 200 mA.
  - Usually the average current is 100 mA.
  - To wrap up, ESP8266 needs a 500 mA power supply.

--------------

What choices do I have when configuring the RMII clock for the Ethernet of ESP32?
--------------------------------------------------------------------------------------------------------------------------------------------------------

  - We recommend you connect an external crystal to GPIO0 as input. Please pay attention to the state of GPIO0 when ESP32 is powered on.
  - For details, please refer to `Configure MAC and PHY <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_eth.html#configure-mac-and-phy>`_.

--------------

What kind of socket is used on ESP32-LyraT development boards to connect a speaker?
-------------------------------------------------------------------------------------------------

  Please use a PH-2A socket.

-------------

For modules housing ESP32, which pins cannot be set by users?
--------------------------------------------------------------

  - For ESP32-WROOM Series of modules, GPIO6 ~ GPIO11 are pins for flash and cannot be set for other uses.
  - For ESP32-WROVER Series of modules, GPIO16 and GPIO17 are pins for PSRAM and cannot be set for other uses.
  - Besides, please note that ESP32 has five strapping pins. For details, please refer to `ESP32 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`__.

--------------

Which is the reset pin of ESP32?
---------------------------------

  - CHIP_PU serves as the reset pin of ESP32. The input level (VIL_nRST) for resetting the chip should be low enough and remain so for a period of time. Please refer to Section *Reset* in the `ESP32 Hardware Design Guidelines <https://www.espressif.com/sites/default/files/documentation/esp32_hardware_design_guidelines_en.pdf>`_.

--------------

What should be noted when I design the power supply for ESP8266?
------------------------------------------------------------------

  - If you use LDO regulators, please ensure the input voltage ranges from 2.7 V to 3.6 V and the output current is greater than 500 mA.
  - The decoupling capacitor must be as close to the chip as possible. The equivalent resistance should be low enough.
  - ESP8266 is not 5 V tolerant. It operates at 3.3 V, with the operating voltage ranging from 2.7 V to 3.6 V.
  - If you use DC/DC converters, please add LC filters when necessary.
  - Please refer to Section *Power Supply* in the `ESP8266 Hardware Design Guidelines <https://www.espressif.com/sites/default/files/documentation/esp8266_hardware_design_guidelines_en.pdf>`_.

--------------

When I use the TOUT pin of ESP8266 to collect ADC sample signals, will the pins be damaged if the voltage is greater than 1.0 V?
----------------------------------------------------------------------------------------------------------------------------------

  - If the input voltage is within the operating range of pins (0 V ~ 3.6 V), the pins will not be damaged.
  - If the voltage is greater than 1.0 V, it may lead to abnormal results.

--------------

For modules with PCB antennas, what should be noted when I design the PCB and the housing of the antenna?
------------------------------------------------------------------------------------------------------------

  - When adopting on-board design, you should pay attention to the layout of the module on the base board. The interference of the base board on the module's antenna performance should be reduced as much as possible.
  - It is recommended that the PCB antenna area of the module be placed outside the base board, while the module be put as close as possible to the edge of the base board so that the feed point of the antenna is closest to the board.
  - Please make sure that the module is not covered by any metal shell. The antenna area of the module and the area 15 mm outside the antenna should be kept clean (namely no copper, routing, components on it).
  - For details, please refer to `Hardware Design Guidelines <https://www.espressif.com/en/support/documents/technical-documents?keys=&field_download_document_type_tid%5B%5D=513>`__.

---------------

Can GPIO 34 ~ GPIO39 of ESP32 be used as UART RX pins?
--------------------------------------------------------

- GPIO 34 ~ GPIO39 can be used as UART RX pins.

---------------------

Where can I find the design reference for the external 32 kHz crystal of ESP32 modules?
-------------------------------------------------------------------------------------------------------

  - Please refer to Section *RTC (optional)* in the `ESP32 Hardware Design Guidelines <https://www.espressif.com/sites/default/files/documentation/esp32_hardware_design_guidelines_en.pdf>`_.

----------------

Does the flash of ESP32 modules support 80 MHz QIO access mode?
----------------------------------------------------------------

  - ESP32 modules support 80 MHz QIO access mode.
  - You are recommended to load the second-stage bootloader in QIO mode, as QE is not set by default in some flash status registers.

----------------

How to configure the RMII synchronous clock for the Ethernet of ESP32?
-------------------------------------------------------------------------

  - To run a test, please refer to `esp-idf/examples/ethernet/basic <https://github.com/espressif/esp-idf/tree/release/v4.4/examples/ethernet/basic>`_.
  - When GPIO0 provides clock output for PHY, the Ethernet connection of the IP101 PHY chip can be unstable. Therefore, you are recommended to connect a 50 MHz crystal to PHY with GPIO0 as input.
  - Because of the characteristics of GPIO0, the IO should be set to control the enable pin of PHY.
  - Please read `Ethernet document <https://docs.espressif.com/projects/esp-idf/en/v4.4.2/esp32/api-reference/network/esp_eth.html>`__.
  - You may also refer to `1SCH_ESP32-ETHERNET-KIT Schematics <https://dl.espressif.com/dl/schematics/SCH_ESP32-ETHERNET-KIT_A_V1.1_20190711.pdf>`_.

-------------

How can I hard reset ESP8266? Is hard reset active low or active high? What are the requirements for reset?
--------------------------------------------------------------------------------------------------------------------------------------------------------

  - The Pin32 EXT_RSTB of ESP8266 is the reset pin. This active low pin has an internal pull-up resistor. To prevent external factors triggering a restart, it is recommended that the EXT_RSTB cabling be as short as possible and an RC circuit be added to the EXT_RSTB pin.
  - The CHIP_EN pin of ESP8266 can also be used as a hard reset pin. When you use the CHIP_EN pin as a reset pin, the reset is active low. To reset and restart ESP8266, the input level should be lower than 0.6 V and last for more than 200 μs. It is recommended to use the CHIP_EN pin for chip reset. For more information, please refer to Section *Reset* in the `ESP8266 Hardware Design Guidelines <https://www.espressif.com/sites/default/files/documentation/esp8266_hardware_design_guidelines_en.pdf>`__.

--------------

What does the term ``NC`` mean in Espressif schematics?
------------------------------------------------------------------------------------

  - NC is the acronym of “No Component”. If you see a pull-up resistor is marked NC as shown in the figure below, it indicates that the component is not installed.
  
  .. figure:: ../../_static/no-component.png
    :scale: 100%
    :alt: no-component
    :figclass: align-center

--------------

How can I use multiple antennas with ESP32-S2?
--------------------------------------------------------------------------

  - Using multiple antennas with ESP32-S2 is similar to that with ESP32. You may refer to `ESP32-WROOM-DA Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32-wroom-da_datasheet_en.pdf>`_.
  - For detailed instructions, please refer to `ESP-IDF Programming Guide <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s2/api-guides/wifi.html#wi-fi-multiple-antennas>`_.
  - You can add an RF switch to select antennas.

--------------
 
Does ESP32-C3F SPI CS0 pin need an external 10 kΩ pull-up resistor?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32-C3F:

  - No.

--------------

Is there any hardware design reference for ESP-Skainet Speech Recognition?
--------------------------------------------------------------------------------------------------------------------------------

  - Please refer to `ESP32-Korvo V1.1 User Guide <https://github.com/espressif/esp-skainet/blob/master/docs/en/hw-reference/esp32/user-guide-esp32-korvo-v1.1.md>`_.
  
----------------------------------------------------------------------------------------

Is it necessary to connect a 32 kHz RTC crystal?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  :CHIP\: ESP32 | ESP32-C3 | ESP32-S3:

  - The external 32 kHz crystal is often used for Bluetooth Light-sleep timing. Therefore, when Bluetooth LE Light-sleep mode is not necessary, there is no need to do so.

---------------

For the ESP32-MINI-1 module, is there a component library for Altium Designer?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Our hardware schematics are developed with PADS. To find the .asc file that can be converted and opened in Altium Designer, please go to `ESP32-MINI-1 Reference Design <https://www.espressif.com/sites/default/files/documentation/ESP32-MINI-1_V1.0_Reference_Design.zip>`_.
  - For hardware reference designs of other modules, please refer to `technical documents <https://www.espressif.com/en/support/documents/technical-documents>`_.

--------------------

Can I change the input voltage of UART0 of ESP8266 from 3.3 V to 1.8 V?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes. VDDPST is the power domain for UART0, the input voltage of which can be 1.8 V theoretically.

------------------

Is the level of UART0 of ESP8266 determined by VDD (VCC_WIFI) or VDDPST (VCC_CODEC_IO)?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The digital power voltage is determined by VDDPST, so the level of UART0 of ESP8266 is determined by VDDPST (hardware power domain).

--------------

What should be noted when I connect an external PSRAM to ESP32-D2WD?
-------------------------------------------------------------------------------------------------------------------

  - Please enable ``CPU frequece 240 Mhz`` and ``RTC clock 80 Mhz`` as follows:

    - ``menuconfig`` > ``Serial flasher config`` > ``Flash SPI Speed (80 Mhz)``
    - ``Component config`` > ``CPU frequency (240 Mhz)``
    - ``Component config`` > ``ESP32 specific`` > ``[*]Support for external, SPI-connected RAM``
    - ``Component config`` > ``ESP32 specific`` > ``SPI RAM config`` > ``Set RAM clock speed (80 Mhz clock speed)``

---------------------

When the VDD power supply of ESP32 slowly rises from 0 V to 3.3 V, why does the chip not start as usual?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - This problem occurs because the power-on sequence requirements are not met. To start the chip, when VDD reaches 2.3 V, the EN voltage should not exceed 0.6 V.
  - If the VDD rise time is too long, the RC circuit on the EN side of the chip will not be able to delay EN.
  - You may modify the RC circuit, for example, increase the capacitance, adjust the resistance, or use the Reset chip to control EN state.
  - When the voltage provided to ESP32 is detected to be less than 2.3 V, you are recommended to pull down the EN pin of ESP32.
  - For ESP32 power-on sequence description, please refer to `ESP32 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`__.
  
------------------

When using the ESP32-WROOM-32D module, can I set GPIO12 for other uses?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - GPIO12 is a strapping pin that controls the startup voltage of SPI flash. The SPI flash startup voltage of the ESP32-WROOM-32D module is 3.3 V, so GPIO12 needs to be pulled down during powering on.
  - If you need to set GPIO12 for other uses, please use the command `espefuse.py set_flash_voltage 3.3v <https://docs.espressif.com/projects/esptool/en/latest/esp32/espefuse/set-flash-voltage-cmd.html#set-flash-voltage>`_ in the esptool to set the voltage through VDD_SDIO as 3.3 V.
  - It is possible to connect VDD_SDIO to 3.3 V in hardware directly without burning eFuse again.
  - In the mass production stage, you can also download the firmware directly by modifying the default configuration of ESP32_EFUSE_CONFIG to config_voltage = 3.3 V in config/esp32/utility.confgi in the flash download tool.

--------------------

When connecting an external flash to ESP32-WROOM-32D module, is it possible if I do not use GPIO6 ~ GPIO11 pins?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP32 has 3 sets of SPIs (SPI, HSPI and VSPI), which can access the external flash through the SPI0/1(HSPI/VSPI) bus. The external flash connected to other pins (pins other than GPIO6 ~ GPIO11) can only receive data for storage, but not run code. If you need to run code from flash, please connect the flash to GPIO6 ~ GPIO11 pins only. 

--------------

Do I need to add a shield cover to the PCB of ESP32 modules?
--------------------------------------------------------------------------------------------------------

  - If there is no interference such as 2G, 3G, 4G, Wi-Fi, Bluetooth, or Zigbee, then there is no need to add a shield cover.

--------------

Do I must use GPIO0, GPIO1 or GPIO3 of ESP32 as the I2S CLK pin?
------------------------------------------------------------------------------------------------------------

  - The MCLK pin must use GPIO0, GPIO1 or GPIO3. The other clock pins can use any GPIOs. Note that GPIO0 is generally not recommended for other functions because it is a strapping pin.

----------------

Does the ESP32-U4WDH chip support external PSRAM chips?
-----------------------------------------------------------------------------------------------------------------

  - The ESP32-U4WDH chip supports external PSRAM chips. However, only the `ESP-PSRAMXXH <https://www.espressif.com/en/support/documents/technical-documents?keys=psram>`_ chip released by Espressif is supported. Third-party PSRAM chips are not supported. 
  - For hardware design, all the PSRAM pins except for the CS pin can be multiplexed with Flash. For more information, please refer to the `ESP32 Hardware Design Guidelines <https://www.espressif.com/sites/default/files/documentation/esp32_hardware_design_guidelines_en.pdf>`_. 
  - Also, when designing the PCB, please make sure that the GND of the PSRAM to the GND of the ESP32-U4WDH is as short as possible; Otherwise, the signal quality may be affected.

-----------------

Does ESP32 support connection to an external SD NAND flash chip (instead of the default NOR flash chip) via the SPI0/SPI1 interface for storing application firmware?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The ESP32 chip does not support external SD NAND Flash chips using the SPI0/SPI1 (connect the core Flash) interface.
  - If you want to store external data, it is recommended to use the SPI2, SPI3, or SDIO interface of ESP32 to connect to an external NAND SD chip.
  - SPI2 and SPI3 can be used via any GPIOs, while the SDIO interface can only be used via the specified interface. For more information, please refer to Section *Peripheral Pin Configurations* in the `ESP32 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_.

-----------------

Does it support to connect a second PSRAM chip externally based on the ESP32-S3R8 chip?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - No, it is not supported. The reasons are as follows:
    
    - The PSRAM chip is connected to the MSPI bus. There are only two CS signals from the MSPI peripheral, one is connected to the flash, another is connected to the PSRAM.
    - CPU accesses external memory via cache and MSPI. A GPSPI peripheral is not accessible cache.

----------------

Could you please provide the 3D model and Footprint files of the ESP32-S3-WROOM-1 module?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The 3D models and Footprint files for the modules are available under the `espressif/kicad-libraries <https://github.com/espressif/kicad-libraries>`_ library.

----------------

Does ESP32/ESP32-S2/ESP32-C3/ESP32-S3 support powering the RTC power domain only to keep the chip working with low power consumption?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

   No, it is not supported. Take ESP32 as an example, detailed information will be updated to the RTC chapter in `ESP32 Hardware Design Guidelines <https://www.espressif.com/sites/default/files/documentation/esp32_hardware_design_guidelines_en.pdf>`_.

----------------

How can I improve the EMC performance?
------------------------------------------------------------------------------------------------------------------------------------

  - At the hardware level, the following measures can be taken to improve the EMC performance of the PCB board.
  
    - The EMC performance with a four-layer board design will be better than a two-layer board hardware design.
    - Add filtering circuits to the power supply circuit.
    - Add ESD or magnetic beads to the antenna circuit.
    - Add a zero-ohm series resistor to the SPI Flash communication lines to lower the driving current, reduce interference to RF, and adjust timing for better interference shielding.
    - Keep GND intact as much as possible.
    - For more hardware design suggestions, please refer to `《ESP Hardware Design Guidelines》 <https://www.espressif.com/en/support/documents/technical-documents?keys=Hardware+Design+Guidelines>`_.
