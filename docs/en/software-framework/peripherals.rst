Peripherals
============

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

What is the maximum speed supported by the SDIO interface?
-------------------------------------------------------------------------

  The maximum clock speed supported by the hardware SDIO slave module is 50 MHz. As SDIO specifies use of quad data lines, the effective maximum bit rate is 200 Mbps.

--------------

When using ESP32 to develop Touch Sensor applications, where can I find references?
-----------------------------------------------------------------------------------------------------------

  Please refer to `Software and Hardware Designs <https://github.com/espressif/esp-iot-solution/tree/master/examples/touch_pad_evb>`_.

--------------

Is ESP-WROOM-02D module able to connect SPI flash?
------------------------------------------------------------------------------

  The ESP-WROOM-02D has free SPI peripherals, and can be externally connected to SPI flash to store data.

--------------

Taken ESP-WROOM-S2 as the slave device and STM32 as MCU, is it possible to download through SPI interface?
----------------------------------------------------------------------------------------------------------------------------------------------

  No, we use UART0 to download by default. You can also design OTA support yourself in firmware.


--------------

Does the hardware SDIO interface support SD cards?
----------------------------------------------------------------------

  Please note that the SDIO hardware only supports the device or slave profile, i.e. it cannot act as a host to control SDIO devices such as SD cards.

--------------

Does ESP8266 support I2C slave mode?
--------------------------------------------------

  No. If you want to use this function, it is recommended to choose ESP32 or ESP32-S2 chips instead. For ESP32 examples, please refer to `i2C_self_test <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/i2c/i2c_self_test>`_.

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

Does ESP32 support transmitting audio stream using A2DP?
----------------------------------------------------------------------------

  Yes, please refer to example `a2dp_source <https://github.com/espressif/esp-idf/tree/d85d3d969ff4b42e2616fd40973d637ff337fae6/examples/bluetooth/bluedroid/classic_bt/a2dp_source#esp-idf-a2dp-source-demo>`_.

--------------

Is ESP8266 I2C realized via software programming?
-----------------------------------------------------------------------

  Yes, ESP8266 I2C is realized via GPIO software programming.

--------------

When using ESP8266 NonOS v3.0 SDK, the following error occurred. What could be the reasons?
------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    E:M 536    E:M 1528

  Any error logs beginning with E:M indicate insufficient memory.

--------------

What is the frequency range for ESP8266 PWM?
----------------------------------------------------------------

  The PWM of ESP8266 is realized via software programming, so the maximum CLK value is 1 M limited by timer. It is recommended to set the frequency to 1 K. The PWM frequency can also be improved by decreasing the resolution of duty cycle.

--------------

Are there any limits on outputting PWM via ESP32 GPIO pins?
------------------------------------------------------------------------------------------

  The ESP32 can output PWM using any GPIO switched via IO Matrix except for GPIO34 ~ GPIO39, which are used for input only.

--------------

When there is water on ESP32-S2 Touch Sensor, does it block or recognize the Touch event with its waterproof function?
------------------------------------------------------------------------------------------------------------------------------------------------------

  When the impact of water on the Touch Sensor is small (with droplets), the sensor will adapt to it actively; when the impact of water on the Touch Sensor is large (with large water flow), the sensor can avoid certain extent of the impact by configuring software to lock some sensor channels.


--------------

While the waterproof feature of ESP32-S2 Touch Sensor shielding the Touchpad with water flow, does other pads with no water still usable?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

  Yes, the specific shielding channel can be selected via software.

--------------

Are there any recommendations for materials that can be used to test Touch Sensor, can trigger Touch Sensor stably and is close to the parameters of human touches？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  For experiments with high consistency requirements, it is doable to replace human hands with cell phone pencils.

--------------

Can the pins of Touch Sensor be remapped？
---------------------------------------------------------------------

  No, because Touch Sensor is realized via software programming.

--------------

Do I need to reset a check threshold for Touch Sensor after covering it with a acrylic plate？
-----------------------------------------------------------------------------------------------------------------------------

  Yes.

--------------

Is it possible for Touch Sensor to detect whether there is a acrylic plate on the top, so that it can switch to the pre-defined threshold value automatically when there is a acrylic plate added or removed?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  For now, it cannot adapt to the impacts brought by physical changes.

--------------

What is the maximum capacity for ESP32 SD card?
-----------------------------------------------------------------------

  - In the SD3.01 Specifications, the SDXC card supports a maximum capacity of 2 TB (2048 GB).
  - The ESP32 SDMMC Host also complies with the SD3.01 Specifications, which means up to 2 TB areas of it can be accessed by peripherals. When accessing the card via SPI bus using the SDSPI driver, there are also 2 TB of areas can be accessed in hardware level.
  - In software level, the usable area of the card is also affected by the file system.

--------------

Does ESP32 support USB function?
---------------------------------------------------

  - No, ESP32 does not support USB function.
  - However, ESP32-S2 supports USB1.1.

--------------

What should I pay attention to when using the HW timer interrupt with ESP8266?
----------------------------------------------------------------------------------------------------------

  - Please refer to `ESP8266 Technical Reference Manual <https://www.espressif.com/sites/default/files/documentation/esp8266-technical_reference_en.pdf>`_ regarding the related APIs.
  - If you are using NonOS SDK, please refer to `ESP8266 Non-OS SDK API Reference <https://www.espressif.com/sites/default/files/documentation/2c-esp8266_non_os_sdk_api_reference_en.pdf>`_.
  - Generally, when using hardware interrupts, you should finish executions as soon as possible and put the callback function into IRAM to avoid the potential impacts of Cache.

    - For RTOS SDK, IRAM_ATTR should be added to the function.
    - For NonOS SDK, ICACHE_FLASH_ATTR should not be added before the function.

--------------

Can I distribute the ESP32 PWM to any I/O?
-------------------------------------------------------------------

  - Theoretically, the PWM can be distributed to any I/Os except for those that only have input functions (e.g., GPIO34 ~ GPIO39).
  - In the actual use, this could also be affected by the limitations of chips and modules, the un-pinned I/Os, flash occupations and etc.

--------------

Is there any example code for I2S driving LCD with ESP32?
-------------------------------------------------------------------------------------

  Please refer to I2S LCD Driver：`esp-iot-solution i2s_devices <https://github.com/espressif/esp-iot-solution/tree/master/components/i2s_devices>`_.

--------------

When using ESP8266 RTOS SDK v2.1 and previous versions, how to set LOG to UART1?
----------------------------------------------------------------------------------------------------------------

  After initializing UART1, you can switch LOG to UART1 via API:

  .. code-block:: c

    UART_SetPrintPort(UART1);

-----------------

When using ESP8266 RTOS SDK v3.0 and later versions, how to set LOG to UART1?
----------------------------------------------------------------------------------------------------------

  Go to  ``menuconfig -> Component config -> ESP8266-specific -> UART for console output -> custom -> UART peripheral to use for console output -> UART0`` and change the option to "UART1".

--------------

How to enable UART Flow Control in ESP32 IDF?
---------------------------------------------------------------------------

  - Hardware enable: `uart-flow-control <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/uart.html?highlight=uart%20flow%20control#multiple-steps>`_.
  - Software enable: `software-flow-control <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/uart.html?highlight=uart%20flow%20control#software-flow-control>`_.

--------------

The PWM of ESP8266 NonOS SDK changes slow. What could be the reasons?
---------------------------------------------------------------------------------------------------

  - If you are using the gradient APIs in SDK example/IOT_demo, e.g., light_set_aim or light_set_aim_r, it will need a gradual process for PWM changes.
  - If you need the PWM Duty to take effect immediately after configuration, please call API pwm_set_duty, and call pwm_start next to make this configuration take effect.

--------------

Some ESP8266 GPIOs are high level. What could be the reasons?
----------------------------------------------------------------------------------------

  - According to the hardware design, some GPIOs are pulled up or down by default. Thus the level of these pins are not controlled by the program during system initialization, causing some incorrect levels of GPIOs during the boot process.
  - If you expect to use these GPIOs, it is recommended to keep the hardware peripherals be consistent with the default level status, or adjust level status in software during bootloader process. When using the later method, you may also encounter temporary level exception.

--------------

How is the accuracy of ESP8266 ADC?
----------------------------------------------------------

  - The ESP8266 ADC is 10 bit, and its theoretical accuracy is 2 :sup:`10` = 1024.
  - After connected to a router, the ESP8266 will enter Modem-sleep mode from STA mode, causing the change of the reference value inside the chip. Therefore, the ADC could measure the data change.
  - If you expect an accurate result, please read the ADC value using function system_adc_fast_read after turning off Wi-Fi.

--------------

How to get the Bitmap information of the ADC register?
----------------------------------------------------------------------------

  Since the ADC of ESP8266 is highly integrated with the internal RF circuit, the Bitmap and register information is not opened. Please contact sales@espressif.com if you have any special needs.

--------------

How many channels does ESP32 ADC have? What is the sampling rate and significant digit？
---------------------------------------------------------------------------------------------------------------

  - The ESP32 ADC has 18 channels.
  - Its sampling rate can reach 100000 times per second without Wi-Fi.
  - Its sampling rate can reach 1000 times per second with Wi-Fi.
  - The internal significant digit of ADC is 12-bit.

--------------

Can I disable the thread scheduling and use a single CPU for ESP32 to realize real-time GPIO?
-------------------------------------------------------------------------------------------------------------------------

  - For now, we do not have any related configurations for SDK to support the single operation of CPU1. Both cores of ESP32 support SMP only, but not AMP.
  - The following solutions can be used to resolve the issue of output waveform being interrupted:

    - Use hardware signal outputs, and choose related digital protocols to realize SPI, I2C, I2S and etc. For special usage with SPI, you can generate waveform using signal output lines.
    - See if the hardware RMT can generate the desired waveform with enough length.
    - When the hardware interrupt generated corresponding waveform, all callbacks need to be put in IRAM.
    - Use the co-processor in the chip as a single chip without an operation system. But it only supports assembly language for now.

--------------

Is there any reference for ESP32 Touch application?
--------------------------------------------------------------------------

  For ESP32 Touch application, please refer to `Touch Software and Hardware Designs <https://github.com/espressif/esp-iot-solution/tree/master/examples/touch_pad_evb>`_.


--------------

Is it possible to use ESP32 SD card together with flash & PSRAM?
---------------------------------------------------------------------------------------------

  - Yes, they can be used simultaneously.
  - However, they do not share the same group of SDIO.

--------------

When using UART0 as a serial communication port for ESP32, what should I pay attention to?
---------------------------------------------------------------------------------------------------------------------

  - Generally, it is not recommended to use UART0 as a normal serial communication port, because it is the default LOG output port.
  - If the UART number in ESP32 is not enough for you or it is not convenient to change your hardware designs anymore, and UART0 is therefore going to be used as a normal communication port, please pay attention to the following suggestions:

  **Software**: 

    You need to protect the serial communication port from being affected by printing. The UART0 mainly has three print settings in the default program:

    - First, power-on ROM print. You can set the MTDO pin as low level when powered on to block the power-on ROM print.
    - Second, bootloader log output. You can set ``menuconfig -> Bootloader config -> Bootloader log verbosity`` as ``Not output`` to block bootloader log output.
    - Third, app log output. You can set ``menuconfig -> Component config -> Log output -> Default log verbosity`` as ``Not output`` to block app log output.
    
  **Hardware**：

    - Pay attention to other devices on UART0 when downloading programs since they could affect downloading. It is recommended to reserve a 0 Ω resistance between ESP32 and other devices so that if there is something wrong while downloading, you can still disconnect this resistance.

-----------------

Is it possible to use GPIO34 ～ GPIO39 from ESP32-SOLO-1 as the RX signal pin for UART and TWAI®?
-----------------------------------------------------------------------------------------------------------------------------

  Yes, GPIO34 ～ GPIO39 are for receive only and can be used as the RX signal pins for UART and TWAI®.
  
---------------

Does ESP-WROOM-S2 module support using SDIO as a slave？
---------------------------------------------------------------------------------------

  Yes, because ESP-WROOM-S2 flash uses SPI interfaces.

-----------------

Does ESP32 support using crystal oscillator as the clock source of I2S？
---------------------------------------------------------------------------------------------------

  No. Please go to `ESP32 Technical Reference Manual <https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf>`_ to read about clock source configurations of I2S.

---------------

When calling the API adc_read_fast() with ESP8266, will it cause a Wi-Fi disconnection?
----------------------------------------------------------------------------------------------------------------------

  - Please turn off Wi-Fi and interrupts first before calling adc_read_fast(). Please refer to the `Specification <https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/api-reference/peripherals/adc.html?highlight=adc_read#_CPPv413adc_read_fastP8uint16_t8uint16_t>`_ of this API.
  - Since the API adc_read_fast() performs continuous acquisition and the ADC is partially coupled internally with Wi-Fi RF, so it is not possible to call this function with Wi-Fi turned on.
  - Please use adc_read() for ADC acquisition when Wi-Fi is on. To ensure data stability, you need to use function esp_wifi_set_ps(WIFI_PS_NONE); to turn off Wi-Fi Modem-sleep mode.
 
.. note::

    ADC sampling rate: can reach 100000 times per second with Wi-Fi turned off, and 1000 times per second with Wi-Fi turned on.

----------------

How to dynamically change the serial baud rate and make it take effect immediately with ESP32?
------------------------------------------------------------------------------------------------------------------------------

  Please use the API uart_set_baudrate() to change the baud rate of UART. Please see `API Reference <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/uart.html?highlight=uart_set_baud#_CPPv417uart_get_baudrate11uart_port_tP8uint32_t>`_.

--------------

Since ESP32-S2 has removed the SDIO interface, does it still support external TF card?
--------------------------------------------------------------------------------------------------------------------------------

  The ESP32-S2 has four groups of SPI interfaces, and you can use the interface of SPI2/SPI3 to connect an external TF card. When doing so, the SPI should be set to general SPI mode.

----------------

What is the turning speed of ESP32 GPIO levels?
---------------------------------------------------------------------

  It will take around 300 ns.

--------------

How to connect MIC with ESP32?
-----------------------------------------------------

  - You can connect I2S peripheral if it is digital MIC.
  - You can connect ADC peripheral if it is analog MIC.

--------------

Does ESP32 support analog audio output or digital audio output?
-------------------------------------------------------------------------------------------

  - The ESP32 supports DAC analog audio output for simple outputs such as warning tones. But if you use it for music playing, the effect will not be so desirable. 
  - The ESP32 also supports I2S digital audio output. For I2S configurable pins, please see Section four in `ESP32 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_.

---------------

What is the difference of SPI, HSPI and VSPI in ESP32?
-------------------------------------------------------------------------------------

  - The SPI/HSPI/VSPI in the `parallel QSPI` interface are groups to connect the external flash, which is mounted on the SPI group.
  - Any usable HSPI/VSPI in the driver are general-purpose SPIs. The difference in their names are only used to distinguish between groups.

--------------

When certain RTC peripherals（SARADC1，SARADC2，AMP，HALL） are powered on, the inputs of GPIO36 and GPIO39 will be pulled down for approximately 80 ns. 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  When enabling power for any of these peripherals, ignore input from GPIO36 and GPIO39. 

--------------

When the LEDC is in decremental fade mode, a duty overflow error can occur.
----------------------------------------------------------------------------------------------------------------

  When using LEDC, avoid the concurrence of following three cases: 

  - The LEDC is in decremental fade mode;
  - The scale register is set to 1;
  - The duty is 2 :sup:`LEDC_HSTIMERx_DUTY_RES` or 2 :sup:`LEDC_LSTIMERx_DUTY_RES`. 

--------------

When the TWAI® controller enters reset mode or when the TWAI controller undergoes bus-off recovery, the REC is still permitted to change. How to resolve such issue?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  When entering reset mode, the TWAI controller should set the the LISTEN_ONLY_MODE to freeze the REC. The desired mode of operation should be restored before exiting reset mode or when bus-off recovery completes. 

--------------

When the TWAI® controller undergoes the bus-off recovery process, the controller must monitor 128 occurrences of the bus free signal before it can become error active again. How to resolve such issue?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  When undergoing bus-off recovery, an error warning interrupt does not necessarily indicate the completion of recovery. Users should check the ``STATUS_NODE_BUS_OFF`` bit to verify whether bus-off recovery has completed. 

--------------

Upon completion of bus-off recovery, the next message that the TWAI® controller transmits may be erroneous?
---------------------------------------------------------------------------------------------------------------------------------------------------

  Upon detecting the completion of bus-off recovery (via the error warning interrupt), the CAN controller should enter then exit reset mode so that the controller’s internal signals are reset. 

--------------

When the TWAI® Controller receives an erroneous data frame, the data bytes of the next received data frame become invalid, how to resolve such issue?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Users can detect the errata triggering condition (i.e., bit or stuff error in the data or CRC field) by setting ``INTERRUPT_BUS_ERR_INT_ENA`` and checking ``ERROR_CODE_CAPTURE_REG`` when a bus error interrupt occurs. If the errata condition is met, the following workarounds are possible: 

  - The TWAI controller can transmit a dummy frame with 0 data byte to reset the controller’s internal signals. It is advisable to select an ID for the dummy frame that can be filtered out by all nodes on the TWAI bus. 
  - Hardware reset the TWAI controller (will require saving and restoring the current register values). 
  
--------------

The ESP32 GPIO peripheral may not trigger interrupts correctly if multiple GPIO pads are configured with edge-triggered interrupts. How to resolve such issue?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Workaround 1: 

    - Follow the steps below to trigger a GPIO interrupt on a rising edge: 

      1. Set the GPIO interrupt type to high.
      2. Set the interrupt trigger type of the CPU to edge. 
      3. After the CPU services the interrupt, change the GPIO interrupt type to low. A second interrupt occurs at this time, and the CPU needs to ignore the interrupt service routine. 

    - Similarly, follow the steps below to trigger a GPIO interrupt on a falling edge: 

      1. Set the GPIO interrupt type to low.
      2. Set the interrupt trigger type of the CPU to edge.
      3. After the CPU services the interrupt, change the GPIO interrupt type to high. A second interrupt occurs at this time, and the CPU needs to ignore the interrupt service routine.

  - Workaround 2: 

    Assuming GPIO0 ~ GPIO31 is Group1 and GPIO32 ~ GPIO39 is Group2. 

      - If an edge-triggered interrupt is configured in either group then no other GPIO
        interrupt of any type should be configured in the same group.
      - Any number of level-triggered interrupts can be configured in a single group, if no
        edge-triggered interrupts are configured in that group. 

---------------

Does ESP8266 support pulse counting?
---------------------------------------------------------------

  - The ESP8266 does not include a hardware pulse counting module, thus only supports counting via the interrupt of GPIO rising edge or falling edge.
  - When Wi-Fi is turned on in ESP8266, it may cause a vacuum in the GPIO sampling due to its high priority, thus interrupting the collected counts and causing data loss.
  - In conclusion, it is recommended to use ESP32 and subsequent chips for scenarios with high counting demands.
