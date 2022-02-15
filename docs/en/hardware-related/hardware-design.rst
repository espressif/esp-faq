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

How to avoid the VDD3P3\_RTC being powered down after ESP32 entering light-sleep mode?
-----------------------------------------------------------------------------------------

  After ESP32-WROVER-B entering light-sleep mode, the GPIO levels corresponding to pads powered by VDD3P3\_RTC may be decreased. It is generally because of the power-down of RTC after entering light-sleep mode. Please call ``esp_sleep_pd_config(ESP_PD_DOMAIN_RTC_PERIPH, ESP_PD_OPTION_ON)`` to maintain the power supply of RTC.

--------------

The pins for I2S signals
----------------------------

  The pins for I2S signals are located far apart from one another in the reference designs provided by Espressif. Can these pins be located closer together? For example, configure all the I2S signals to GPIO5, GPIO18, GPIO23, GPIO19 and GPIO22; and configure all the I2C signals to GPIO25 and GPIO26, or GPIO32 and GPIO33.

  All I2S I/Os can be allocated freely. Please note that some I/Os can only be used as input pins. For details, please refer to the last page of `ESP32 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_.

--------------

What are the general power supply requirements of the ESP8266?
--------------------------------------------------------------------

  - Digital voltage requirement: 1.8 V - 3.3 V
  - Analog voltage requirement: 3.0 V - 3.6 V (The lowest possible analog voltage is 2.7 V.)
  - Peak analog circuit current: 350 mA
  - Peak digital circuit current: 200 mA
  
  Note: CHIP_EN works at 3.0 V - 3.6 V, please use a level converter to ensure compatibility with digital logic at 1.8 V.

----------------------

How to configure the RMII synchronization clock for Ethernet of the ESP32?
--------------------------------------------------------------------------------------------------------------------------------------------------------

  - Please download the "esp-idf/examples/ethernet/basic" example for testing.
  - The IP101 PHY chip will experience network instability when GPIO0 outputs CLK. Therefore, it is recommended to connect a 50MHz crystal oscillator to the PHY and GPIO0 as input.
  - Due to the special character of GPIO0, it is necessary to configure the IO to control the enable pin of the PHY.
  - Please read `Configure MAC and PHY <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_eth.html#configure-mac-and-phy>`_.
  - You can see `SCH_ESP32-ETHERNET-KIT schematic design <https://dl.espressif.com/dl/schematics/SCH_ESP32-ETHERNET-KIT_A_V1.1_20190711.pdf>`_ for reference.
  
---------------

How to hardware reset ESP8266? Is the hardware reset signal low level or high level active? What are the conditions for the reset?
--------------------------------------------------------------------------------------------------------------------------------------------------------

  - The Pin32 EXT_RSTB of ESP8266 is the reset pin. This pin has an internal pull-up resistor, active in low level. To prevent the restart caused by external interference, it is recommended that the EXT_RSTB cabling be as short as possible and that an RC circuit be added to the EXT_RSTB pin.
  - ESP8266's CHIP_EN pin can also be used as a hardware reset pin. When using the CHIP_EN pin as a reset pin, the reset signal is low level effective. The reset condition is: when the input level is lower than 0.6 V and lasts more than 200 μs, then the ESP8266 will be reset and restart. It is recommended to use the CHIP_EN pin for chip reset. Please refer to Section "1.4.2.2 Reset" in `ESP8266 Hardware Design Guide <https://www.espressif.com/sites/default/files/documentation/esp8266_hardware_design_guidelines_en.pdf>`_ for more information.

--------------

What does the term ``NC`` mean in Espressif schematics?
------------------------------------------------------------------------------------

  - NC is the acronym of No Component. If you see a pull-up resistor is marked NC as shown in the figure below, it indicates that the component is not installed.
  
  .. figure:: ../../_static/no-component.png
    :align: center
    :scale: 100%
    :alt: no-component
    :figclass: align-center

--------------

How to use multiple antennas in ESP32-S2?
--------------------------------------------------------------------------

  - It is similar to ESP32, you can refer to `ESP32-WROOM-DA <https://www.espressif.com/sites/default/files/documentation/esp32-wroom-da_datasheet_en.pdf>`_.
  - For detailed operation instructions, please refer to `ESP-IDF Programming Guide <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s2/api-guides/wifi.html#wi-fi-multiple-antennas>`_.
  - You can add an RF switch to select a working antenna.

--------------
 
Does ESP32-C3F SPI CS0 pin need an external 10 K pull-up resistor?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32-C3F:

  - No.

--------------

Is there any hardware design reference for ESP-Skainet Speech recognition?
--------------------------------------------------------------------------------------------------------------------------------

  - Please refer to ` ESP32-Korvo V1.1 Hardware Reference Design <https://github.com/espressif/esp-skainet/blob/master/docs/en/hw-reference/esp32/user-guide-esp32-korvo-v1.1.md#2%E7%A1%AC%E4%BB%B6%E5%8F%82%E8%80%83>`_.
  
