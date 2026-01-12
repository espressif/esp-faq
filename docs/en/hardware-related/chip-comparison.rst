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

What is the difference between ESP32 with a single core and ESP32 with dual cores regarding programming method, feature performance, power consumption, and so on?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Compared with the single-core chip, the dual-core chip has one more independent core, on which some highly real-time operations can be supported in a better way.

  - The two chips employ the same programming method except the following step only. For single-core chip, you have to configure FreeRTOS to make it run on the first core. The configuration path is ``make menuconfig`` > ``Component config`` > ``FreeRTOS`` > ``[*] Run FreeRTOS only on first core``. This step is not needed for the dual-core chip.
  - The two chips have similar performance in most cases, except under high-load conditions, such as AI algorithm and high real-time interrupts.
  - The dual-core chip consumes a little more power than the single-core chip in Modem-sleep mode. For more details, please refer to `ESP32 Series Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_.

--------------

What's the difference between ESP32 v3.0 and previous chip revisions in software and hardware?
-----------------------------------------------------------------------------------------------------------------------------------------------------

  - For software usage, there is no difference. ESP32 v3.0 is compatible with old firmwares. For hardware, some bugs have been fixed in ESP32 v3.0.
  - For more information on design changes, please refer to `ESP32 Chip Revision v3.0 User Guide <https://www.espressif.com/sites/default/files/documentation/esp32_chip_revision_v3_0_user_guide_en.pdf>`_.

---------------

Can the GPIO34 ~ GPIO39 of ESP32 only be set to input mode?
--------------------------------------------------------------------

  - Yes, the GPIO34 ~ GPIO39 of ESP32 can only be set to input mode. They cannot be set to the output mode as they cannot be pulled up or down by software.
  - For more details, please refer to `GPIO & RTC GPIO <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/gpio.html>`_.

---------------

Does ESP32 support a driver for Linux?
-----------------------------------------

  You can use the `esp-hosted <https://github.com/espressif/esp-hosted>`__ solution. This solution currently offers three main variants: **ESP-Hosted-NG**, **ESP-Hosted-FG**, and **ESP-Hosted-MCU**. For differences between the variants, see `Variant Comparison <https://github.com/espressif/esp-hosted#-variant-comparison>`__.

  - Both **ESP-Hosted-NG** and **ESP-Hosted-FG** support Linux hosts:

    - **ESP-Hosted-NG** provides a standard 802.11 Wi-Fi interface, and supports both STA and SoftAP modes.
    - **ESP-Hosted-FG** provides an 802.3 Ethernet interface, and supports STA, SoftAP, and STA+SoftAP modes.
  - If you use **ESP-Hosted-FG** and the target Linux platform is not yet adapted, you can refer to the `ESP-Hosted-FG Porting Guide <https://github.com/espressif/esp-hosted/blob/master/esp_hosted_fg/docs/Linux_based_host/porting_guide.md#porting-guide>`__.
  - If you use **ESP-Hosted-NG** and the target Linux platform is not yet adapted, you can refer to the `ESP-Hosted-NG Porting Guide <https://github.com/espressif/esp-hosted/blob/master/esp_hosted_ng/docs/porting_guide.md>`__.

---------------

What is the meaning of the acquired data when you scan the data matrix on the module's shielding case?
----------------------------------------------------------------------------------------------------------------

  - Taking 0920118CAAB5D2B7B4 as an example. '09' indicates the factory code; '20' indicates the last two numbers of the year of manufacturing, which is 2020 in this example; '11' indicates the week number of manufacturing; and the last 12 numbers '8CAAB5D2B7B4' is the MAC address of this module. For the latest information, please refer to `Module Packaging Information <https://www.espressif.com/sites/default/files/documentation/espressif_module_packaging_information_en.pdf>`_.

----------------------

Can VDD3P3_RTC of ESP32 support independent battery power supply?
-------------------------------------------------------------------

  - The internal RTC of ESP32 cannot work independently as it requires the main CPU to participate in the configuration. Even if the RTC domain is powered by an independent battery, it may still be powered down suddenly.
  - If you want to save the clock information when power-off occurs, please use an external RTC clock chip.

--------------------

What is the difference between ESP32-PICO-D4, ESP32-PICO-V3, and ESP32-PICO-V3-02?
-----------------------------------------------------------------------------------

  - Built-in chip version: The core chip of ESP32-PICO-V3 and ESP32-PICO-V3-02 is ESP32 (ECO V3), while that of ESP32-PICO-D4 is ESP32 (ECO V1).
  - Package size: The size of ESP32-PICO-D4 and ESP32-PICO-V3 is 7 × 7 × 0.94 (mm), while the size of ESP32-PICO-V3-02 is 7 × 7 × 1.11 (mm).
  - Built-in flash: ESP32-PICO-D4 and ESP32-PICO-V3 integrate 4 MB SPI Flash, while ESP32-PICO-V3-02 integrates 8 MB flash and 2 MB PSRAM.
  - Pin differences: Please refer to Section Compatibility with ESP32-­PICO-­V3 in the `ESP32­-PICO-­V3-­02 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32-pico-v3-02_datasheet_en.pdf>`_.

---------------

Does ESP8266 support 32 MHz crystal?
---------------------------------------------------

  - No. Currently, ESP8266 supports 26 MHz and 40 MHz crystals, and the 26 MHz crystal is recommended.

---------------------

Do ESP products support Zephyr?
----------------------------------------------------------------------------------------------------------------------------------

  - Please refer to `Espressif's Support for Zephyr <https://www.espressif.com/zh-hans/news/Zephyr_updates>`_ for detailed information about the support for Zephyr in ESP products. While there are only a few functional modules have been adapted so far, other modules will be updated further later. For feature requests, you may check or ask on the `Zephyr GitHub issue <https://github.com/zephyrproject-rtos/zephyr/issues/29394>`_ first.
  - You can also find information about ESP products in sections like `XTENSA Boards <https://docs.zephyrproject.org/latest/boards/xtensa/index.html>`_ and `RISCV Boards <https://docs.zephyrproject.org/latest/boards/riscv/index.html>`_ in `Zephyr Docs <https://docs.zephyrproject.org/latest/introduction/index.html>`.

---------------

How to identify the chip revision from the chip silk marking?
-------------------------------------------------------------------------------------------

You can do it by checking the second character of Espressif Tracking Information line in the bottom of the chip silk marking.

.. image:: ../../_static/chip-marking.png
  :width: 400
  :alt: Chip Marking Diagram

- For detailed differences between chip revisions, please refer to respective chip errata documents from Espressif's `documentation page <https://www.espressif.com/en/support/documents/technical-documents?keys=errata>`_.
- For a complete explanation of the chip silk marking, please refer to `Espressif Chip Packaging Information <https://www.espressif.com/sites/default/files/documentation/espressif_chip_packaging_information_en.pdf>`_.
