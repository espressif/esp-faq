GPIO & RTC GPIO
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

What should I pay attention to for ESP32 pin configurations?
---------------------------------------------------------------------------------------

  The ESP32 has ESP32-WROOM and ESP32-WROVER series modules. Please pay attention to the following configurations with GPIOs.

  The WROOM-32\ :sup:`*`/32D/32U/32E/32UE series has 26 pins available for customer use, with the following considerations:

  - GPIO6-GPIO11 of the WROOM-32\ :sup:`*`/32D/32U series are occupied by the internal flash and cannot be used for other purposes;
  - GPIO6-GPIO11 of the WROOM-32E/32UE series are occupied by the internal flash and are no longer pulled out to the module pins;
  - GPIO34, 35, 36 and 39 are input-only pins and cannot be used for outputs;
  - ESP32 has a built-in GPIO matrix, and some peripheral interfaces can be connected to any free pin. That is, during hardware design, there is no need to strictly fix certain functions on certain pins;
  - WROOM-32\ :sup:`*`/32D/32U are not recommended for new designs. It is suggested to use the WROOM-32E/32UE series instead.
  - In the WROOM-32E/32UE series with QSPI PSRAM, GPIO16 is used to connect to the embedded PSRAM and cannot be used for other functions.

  Detailed information can be found in Table 6-2 GPIO_Matrix of `ESP32 Series Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_.

  The WROVER\ :sup:`*`/WROVER-I\ :sup:`*`/WROVER-B/WROVER-IB/WROVER-E/WROVER-IE all have 24 pins available for customer use, with the following considerations:

  - GPIO6-GPIO11 of the WROVER\ :sup:`*`/WROVER-I\ :sup:`*`/WROVER-B/WROVER-IB series are occupied by the built-in flash and cannot be used for other purposes;
  - GPIO6-GPIO11 of the WROVER-E/WROVER-IE series are occupied by the built-in flash and are no longer pulled out to the module pins;
  - GPIO34, 35, 36 and 39 are input-only pins and cannot be used for outputs;
  - For WROVER series, it is not recommended to use GPIO12 for Touch Sensor functions since it has been pulled up in the module;
  - ESP32 has a built-in GPIO matrix, and some peripheral interfaces can be connected to any free pin. That is, during hardware design, there is no need to strictly fix certain functions on certain pins;
  - WROVER\ :sup:`*`/WROVER-I\ :sup:`*`/WROVER-B/WROVER-IB are not recommended for new designs. It is suggested to use the WROVER-E/WROVER-IE series instead.

  Detailed information can be found in Table 6-2 GPIO_Matrix of `ESP32 Series Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_.

  There are three sets of UARTs in ESP32, but only UART0 can be used for downloading with fixed pins.

  \ :sup:`*` indicates that the product is in EOL status.

--------------

Some ESP8266 GPIOs are high level. What could be the reasons?
----------------------------------------------------------------------------------------

  - According to the hardware design, some GPIOs are pulled up or down by default. Thus the level of these pins are not controlled by the program during system initialization, causing some incorrect levels of GPIOs during the boot process.
  - If you expect to use these GPIOs, it is recommended to keep the hardware peripherals be consistent with the default level status, or adjust level status in software during bootloader process. When using the later method, you may also encounter temporary level exception.

--------------

Can I disable the thread scheduling and use a single CPU for ESP32 to realize real-time control of GPIO?
-------------------------------------------------------------------------------------------------------------------------

  - For now, we do not have any related configurations for SDK to support the single operation of CPU1. Both cores of ESP32 support SMP only, but not AMP.
  - The following solutions can be used to resolve the issue of output waveform being interrupted:

    - Use hardware signal outputs, and choose related digital protocols to realize SPI, I2C, I2S and etc. For special usage with SPI, you can generate waveform using signal output lines.
    - See if the hardware RMT can generate the desired waveform with enough length.
    - When the hardware interrupt generated corresponding waveform, all callbacks need to be put in IRAM.
    - Use the co-processor in the chip as a single chip without an operation system.

--------------

What is the turning speed of ESP32 GPIO levels?
---------------------------------------------------------------------

  It takes around 300 ns.

--------------

When certain RTC peripherals (SARADC1, SARADC2, AMP, HALL) are powered on, the inputs of GPIO36 and GPIO39 will be pulled down for approximately 80 ns. How to solve the issue?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  For applications that require accurate timing and detecting digital input status, the above problems can be avoided by software:
    - Ignore the inputs from GPIO36 and GPIO39 when turning on the power domain of the above sensors.
    - Debounce digital inputs through software. When reading the input states of GPIO36 and GPIO39, debouncing can be implemented through software by sampling and filtering the inputs for multiple times, thus reducing misjudgments caused by short voltage drops.

--------------

The ESP32 GPIO peripheral may not trigger interrupts correctly if multiple GPIO pads are configured with edge-triggered interrupts. How to resolve such issue?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Please search for this question and its answer in `ESP32 Series SoC Errata <https://www.espressif.com/sites/default/files/documentation/esp32_errata_en.pdf>`_.

-----------------------

Using ESP-WROOM-02D module, can GPIO0, GPIO15, GPIO1 and GPIO3 be used as normal GPIOs?
-----------------------------------------------------------------------------------------------------------------------------------------------------

  - Strapping pins (GPIO0 and GPIO15) and download pins (GPIO1 and GPIO3) can be used as normal GPIOs.
  - When using the strapping pin as a normal GPIO, you need to pay attention to the level of the strapping pin in the Flash download mode.

---------------

After configuring the GPIO19 for ESP32-C3 as pulled-down input, the level of this pin still stays high. However other pins in ESP32-C3 does not have this issue. What is the reason?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - In ESP32-C3, GPIO19 is a USB D+ pin, whose pull-up resistor is controlled by the pin's pull-up value together with USB's pull-up value. If any of the two pull-up values is 1, the pin's pull-up resistor will be enabled.
  - The USB pull-up value of GPIO19 is 1 by default, so when the pin is pulled down, GPIO19 still keeps high level.
  - This issue has been fixed in the GPIO driver in ESP-IDF v4.4.3 and later versions. For other versions, please write the register ``USB_SERIAL_JTAG_DP_PULLUP`` to 0 for configuration.

------------------

When using the release/v4.2 version of ESP-IDF, how to set a single GPIO as input/output mode simultaneously for ESP32?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  You can set via the `esp_err_t gpio_set_direction(gpio_num_t gpio_num, gpio_mode_t mode) <https://docs.espressif.com/projects/esp-idf/en/release-v4.2/esp32/api-reference/peripherals/gpio.html# _CPPv418gpio_set_direction10gpio_num_t11gpio_mode_t>`_ API.

-----------------------

Is it possible to set the drive capability of the GPIO in ESP-IDF?
--------------------------------------------------------------------------------------------------------

  Yes. Please use `API gpio_set_drive_capability <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/gpio.html#_CPPv425gpio_set_drive_capability10gpio_num_t16gpio_drive_cap_t>`_ to set the GPIO drive capability.

------------------------

When ESP32 uses `gpio_install_isr_service() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/gpio.html#_CPPv424gpio_install_isr_servicei>`_ to attach a new interrupt service routine on GPIO, why does it return `ESP_ERR_NOT_FOUND`?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Generally, this error means that ESP32 does not have enough available interrupt sources. In this case, there are multiple peripherals occupying the interrupt sources at the same time. You can try to reduce the interrupt sources used by other components to attach new GPIO interrupts.

-----------

How do I get the input level of the ESP32 RTC_GPIO?
-------------------------------------------------------------------------------------------------------------------------------------

  - You can obtain the input level of RTC_GPIO by reading the macro of the register address corresponding to RTC GPIO. Please refer to `“esp-idf\components\soc\esp32\include\soc\rtc_io_reg.h” <https://github.com/espressif/esp-idf/blob/8a08cfe7d162bb9c07568b0635193bf922377123/components/soc/esp32/include/soc/rtc_io_reg.h#L91>`_.
  - The related code is as follows :

  .. code-block:: c

    uint8_t level = (uint8_t)((REG_GET_FIELD(RTC_GPIO_IN_REG, RTC_GPIO_IN_NEXT) & BIT(gpio_num)) ? 1 : 0);

----------

How to use GPIO buttons in Light-sleep mode?
----------------------------------------------------------------

  The wake-up function of the button can be enabled. Please note that non-RTC GPIO cannot enable GPIO edge triggering and level triggering at the same time. You can use the existing functions of the `Button <https://components.espressif.com/components/espressif/button>`_ component to implement this.

----------

The default state of GPIO20 on ESP32-C6 is initially set as SDIO. How can it be changed to the regular GPIO mode?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  You can refer to the following code to change the initial SDIO state of ESP32-C6's GPIO20 to the regular GPIO mode:

    .. code:: c

      gpio_hal_iomux_func_sel(GPIO_PIN_MUX_REG[20], PIN_FUNC_GPIO);

----------

Is it possible to set different levels for different GPIOs of ESP32-P4? For example, setting GPIOs in the HP power domain to 3.3 V while setting GPIOs in the LP power domain to 1.8 V?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Mixed settings are not allowed. The levels of all GPIO pins must be uniform, either all at 1.8 V or all at 3.3 V. For example, if a 1.8 V voltage is input to VDDPST_4, then all GPIO levels under this power domain are 1.8 V.
