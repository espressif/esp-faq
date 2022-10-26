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
--------------------------------------------------------------------------------------

  The ESP32 has ESP32-WROOM and ESP32-WROVER series modules. Please pay attention to the following configurations with GPIOs.

  The WROOM-32/32D/32U series have 26 pins available for customers. Please note:

  - GPIO6 ~ GPIO11 are used by the internal flash and cannot be used elsewhere;
  - GPIO34, 35, 36 and 39 are input-only pins and cannot be used for outputs;
  - The ESP32 has a built-in GPIO Matrix, and some peripheral interfaces can be connected to any free pins. That is, for hardware designs, there is no need to strictly distribute some functions on certain pins.

  For detailed information, please refer to Table 9 in `ESP32 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_.

  The WROVER／WROVER-I／WROVER-B／WROVER-IB series have 24 pins available for customers. Please note:

  - GPIO6 ~ GPIO11 are used by the internal flash and cannot be used elsewhere;
  - GPIO34, 35, 36 and 39 are input-only pins and cannot be used for outputs;
  - For WROVER series, it is not recommended to use GPIO12 for Touch Sensor functions since it has been pulled up in the module;
  - The ESP32 has a built-in Matrix, and some peripheral interfaces can be connected to any free pins. That is, for hardware designs, there is no need to strictly distribute some functions on certain pins.

  For detailed information, please refer to Table 9 in `ESP32 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_.

  There are three sets of UARTs in ESP32, but only UART0 can be used for downloading with fixed pins.

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
    - Use the co-processor in the chip as a single chip without an operation system. But it only supports assembly language for now.

--------------

What is the turning speed of ESP32 GPIO levels?
---------------------------------------------------------------------

  It takes around 300 ns.

--------------

When certain RTC peripherals (SARADC1, SARADC2, AMP, HALL) are powered on, the inputs of GPIO36 and GPIO39 will be pulled down for approximately 80 ns. How to solve the issue?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  When enabling power for any of these peripherals, ignore input from GPIO36 and GPIO39. 

--------------

The ESP32 GPIO peripheral may not trigger interrupts correctly if multiple GPIO pads are configured with edge-triggered interrupts. How to resolve such issue?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Solution 1: 

    - Follow the steps below to trigger a GPIO interrupt on a rising edge: 

      1. Set the GPIO interrupt type to high.
      2. Set the interrupt trigger type of the CPU to edge. 
      3. After the CPU services the interrupt, change the GPIO interrupt type to low. A second interrupt occurs at this time, and the CPU needs to ignore the interrupt service routine. 

    - Similarly, follow the steps below to trigger a GPIO interrupt on a falling edge: 

      1. Set the GPIO interrupt type to low.
      2. Set the interrupt trigger type of the CPU to edge.
      3. After the CPU services the interrupt, change the GPIO interrupt type to high. A second interrupt occurs at this time, and the CPU needs to ignore the interrupt service routine.

  - Solution 2: 

    Assuming GPIO0 ~ GPIO31 is Group1 and GPIO32 ~ GPIO39 is Group2. 

      - If an edge-triggered interrupt is configured in either group then no other GPIO interrupt of any type should be configured in the same group.
      - Any number of level-triggered interrupts can be configured in a single group, if no edge-triggered interrupts are configured in that group. 

-----------------------

Using ESP-WROOM-02D module, can GPIO0, GPIO15, GPIO1 and GPIO3 be used as normal GPIOs?
-----------------------------------------------------------------------------------------------------------------------------------------------------

  - Strapping pins (GPIO0 and GPIO15) and download pins (GPIO1 and GPIO3) can be used as normal GPIOs.
  - When using the strapping pin as a normal GPIO, you need to pay attention to the level of the strapping pin in the Flash download mode.

---------------

After configuring the GPIO19 for ESP32-C3 as pulled-down input, the level of this pin still stays high. However other pins in ESP32-C3 does not have this issue. What is the reason?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - In ESP32-C3, GPIO19 is a USB pin, whose pull-up resistor is controlled by the pin's pull-up value together with USB's pull-up value. If any of the two pull-up values is 1, the pin's pull-up resistor will be enabled.
  - The USB pull-up value of GPIO19 is 1 by default, so when the pin is pulled down, GPIO19 still keeps high level. 
  - You can configure it via the register ``USB_SERIAL_JTAG_DP_PULLUP``.

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