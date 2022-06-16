Chip Comparison
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

What is the difference between ESP32 with a single core and ESP32 with dual cores (programming method, feature performance, power consumption, and etc.)?
----------------------------------------------------------------------------------------------------------------------------------------------------------------

  Compared with the single-core chip, the dual-core chip has one more independent core, on which some highly real-time operations can be located.

  - The two chips employ the same programming method except the following step only. You have to configure FreeRTOS to make it run on the single-core chip. The configuration path is ``make menuconfig`` > ``Component config`` > ``FreeRTOS`` > ``[*] Run FreeRTOS only on first core``. However, you do not need to configure FreeRTOS manually on the dual-core chip. 
  - The two chips have similar performance in most cases, except in high-load such as AI algorithm, high real-time interrupts. However, they present similar performance in other calculations.
  - The dual-core chip consumes a little more power than the single-core chip in Modem-sleep mode. For more details, please refer to `ESP32 Series Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_.

--------------

What's the difference between ESP32 ECO V3 and previous chip versions in software and hardware?
---------------------------------------------------------------------------------------------------

  - ESP32 ECO V3 is same with chips of previous versions in software usage, and it can be compatible with old firmwares.
  - Some bugs have been fixed in ESP32 ECO V3. For more information on design changes, please refer to `ESP32 ECO V3 User Guide <https://www.espressif.com/sites/default/files/documentation/ESP32_ECO_V3_User_Guide__EN.pdf>`_.

---------------

Can the GPIO34 ~ GPIO39 of ESP32 only be set to the input mode?
--------------------------------------------------------------------

  - GPIO34 ~ GPIO39 of ESP32 can only be set to the input mode. They cannot be set to the output mode and they cannot be pulled up or down by software.
  - For more details, please refer to `GPIO & RTC GPIO <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/gpio.html>`_.

---------------

Does ESP32 support a driver for Linux?
-----------------------------------------

  Yes, please refer to the example `esp-hosted <https://github.com/espressif/esp-hosted>`_.

  .. note:: This example is adapted to the 802.3 protocol, not the 802.11 protocol.

---------------

What is the meaning of the acquired data when you scan the data matrix on the module's shield cover?
----------------------------------------------------------------------------------------------------------------
  
  - Taking 0920118CAAB5D2B7B4 as an example, '09' indicates the factory code; '20' indicates the last two numbers of the year of manufacturing, which is 2020 in this example; '11' indicates the week number of manufacturing; and the last 12 numbers, '8CAAB5D2B7B4' is the MAC address of this module. For the latest information, please refer to `Module Packaging Information <https://www.espressif.com/sites/default/files/documentation/espressif_module_packaging_information_en.pdf>`_.

----------------------

Can VDD3P3_RTC of ESP32 be powered by an independent battery?
-------------------------------------------------------------------

  - The internal RTC of ESP32 cannot work independently as it requires main CPU to participate in the configuration. Even if the RTC domain is powered by an independent battery, it may still suddenly be powered down.
  - If you want to save the clock information when power-off occurs, please use an external RTC clock chip.

--------------------

What is the difference between ESP32-PICO-D4, ESP32-PICO-V3, and ESP32-PICO-V3-02?
-----------------------------------------------------------------------------------

  - ESP32-PICO-D4 is based on the ECO V1 version of ESP32, whereas ESP32-PICO-V3 and ESP32-PICO-V3-02 adopt the ECO V3 version of ESP32.
  - The three kinds of SiPs employ the same body size in package. Most of the GPIOs are same in the three kinds of SiPs except flash and PSRAM. The ECO V3 version changes functions of partial pins. For more information, please refer to the datasheets.

---------------

Do ESP modules support Thread?
--------------------------------------------------------------------------------------------------------------------------------
  :CHIP\: ESP32 | ESP32-C3 | ESP32-S3:

  - Currently, no ESP modules support Thread. 
  - However, ESP32-H2, which will be released later, supports Thread.

---------------

Does ESP modules support WAPI (Wireless LAN Authentication and Privacy Infrastructure)?
---------------------------------------------------------------------------------------------------------------------------------

  - Yes.

---------------

Does ESP8266 support the 32 MHz crystal?
---------------------------------------------------

  - No. ESP8266 supports 26 MHz and 40 MHz crystals, and the 26 MHz crystal is recommended.

---------------------

Do ESP32 modules support Zephyr?
----------------------------------------------------------------------------------------------------------------------------------

  - Some ESP32 modules support Zephyr. For details, please refer to `Zephyr Doc <https://docs.zephyrproject.org/latest/boards/riscv/index.html>`_. This file will be continuously updated to add new products.