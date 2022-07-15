Serial Peripheral Interface (SPI)
=================================

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

Is ESP-WROOM-02D module able to connect SPI flash?
------------------------------------------------------------------------------

  The ESP-WROOM-02D has free SPI peripherals, and can be externally connected to SPI flash to store data.

--------------

Taking ESP-WROOM-S2 as the slave device and STM32 as MCU, is it possible to download through SPI interface?
----------------------------------------------------------------------------------------------------------------------------------------------

  No, we use UART0 to download by default. You can also design OTA support yourself in firmware.

--------------

What is the difference among SPI, HSPI and VSPI in ESP32?
-------------------------------------------------------------------------------------

  - ESP32 has four SPIs. SPI0 and SPI1 are occupied by default to connect to flash that stores programs. SPI2 and SPI3 are general-purpose SPIs that are available for customers to use.
  - HSPI represents the above-mentioned SPI2, and VSPI represents the SPI3. The two sets of SPIs are general-purpose SPIs. 

-------------------------

The maximum data transmission of ESP32 SPI DMA is 4092 bytes. Is it because of hardware limitation?
----------------------------------------------------------------------------------------------------------------------------------------------

  Yes. A single node can only store 4092 bytes of data, but the DMA can send more data through link lists.

--------------------

The SPI of ESP32-S2 accesses three SPI Slave devices at the same time, do I need to synchronize the semaphore to access it?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The same SPI peripheral, as the master, can only communicate with one slave at a time, and CS decides which slave to communicate with. If you connect 3 slave devices to the SPI driver and communicate with them separately, it is okay and recommended.
  - You can use the ``spi_device_transmit()`` API, which is a blocking interface and returns after a transmission is completed. If there are multiple tasks, you can call this function one by one and use different handles to communicate.

---------------------------

When using an ESP32 board for development and testing based on ESP-IDF release/v4.3, I received the following error log during compilation. What is the reason?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    spi_flash:Detected size(8192K) smaller than the size in the binary image header(16384K).Probe failed. 

  The reason is that the configured flash size is larger than the actual flash size. In order to avoid misuse of a larger address space, the actual flash size is checked.

----------------

What is the maximum transmission speed supported by SPI slave?
-------------------------------------------------------------------------------
  :CHIP\: ESP32 :

  ESP32 can support up to 10 M of transmission speed when serves as an SPI slave.

------------------------------

When using ESP32 as an SPI Master device, how many bytes of data can be transfered at one time in non-DMA mode?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Up to 64 Bytes of data can be transferred at one time in such condition.
  - But when the transmitted data exceeds 32 bits, you need to set the buffer for SPI data transmission, please refer to the description in `SPI Master Driver <https://docs.espressif.com/projects/esp-idf/en/release-v4.4 /esp32/api-reference/peripherals/spi_master.html?highlight=spi#spi-master-driver>`_.
  - When using ESP32 as an SPI Master device to transmit more than 32 bits of SPI data in non-DMA mode, please refer to the example `lcd <https://github.com/espressif/esp- idf/tree/release/v4.4/examples/peripherals/spi_master/lcd>`_.

--------------------------------

When using the ESP32-S3-WROOM-1 (ESP32-S3R2) module to enable its PSRAM configuration based on the "hello-world" example in ESP-IDF v4.4, the following error is printed. What is the reason?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    .. code-block:: text

      E (232) spiram: Virtual address not enough for PSRAM!

  - ESP32-S3R2 chip integrates a 4-wire 2 MB PSRAM, please set PSRAM Mode to **Quad** mode in menuconfig before your action as follows:

    ``menuconfig → Component config → ESP32S3 Specific → Support for external, SPI connected RAM → SPI RAM config → Mode (QUAD/OCT) of SPI RAM chip in use (Ouad Mode PSRAM)``

-------------------------

When using the ESP32-S3-WROOM-2 (ESP32-S3R8V) module to enable the PSRAM configuration based on the "hello-world" example in ESP-IDF v4.4, the following error is printed. What is the reason?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text
    
      E (453) psrm: psrm ID read error: 0x00ffff
      E (454) cpu start: Failed to init external RAM!

  ESP32-S3R8V chip integrates a 8-wire 8 MB PSRAM, please set PSRAM mode to **Octal** mode in menuconfig before your action as follows:

    ``menuconfig → Component config → ESP32S3 Specific → Support for external, SPI connected RAM → SPI RAM config → Mode (QUAD/OCT) of SPI RAM chip in use (Octal Mode PSRAM)``

-------------------

When using ESP32-C3 to drive the LCD display through the SPI interface, can I use RTC_CLK as the SPI clock to make the LCD screen display static pictures in Deep-sleep mode normally ?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Deep-sleep mode: The CPU and most peripherals will be powered down, and only the RTC memory is working. For more information, please refer to the Low Power Management section in `ESP32-C3 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf>`_.
  - The SPI of ESP32-C3 only supports two clock sources : APB_CLK and XTAL_CLK. RTC_CLK is not supported. Therefore, in the Deep-sleep mode, the LCD screen cannot display static pictures. For more information, please refer to the Peripheral Clock section in `ESP32-C3 Technical Reference Manual <https://www.espressif.com/sites/default/files/documentation/esp32-c3_technical_reference_manual_en.pdf>`_.

------------------

Does ESP8266 RTOS SDK support full duplex for SPI?
--------------------------------------------------------------------------------------------------

  :CHIP\: ESP8266:

  No, it doesn't. Because ESP8266 doesn't support DMA, in order to improve the transmission performance, the entire FIFO is used. So it can only be half duplex. Please refer to `spi readme <https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/peripherals/spi#spi-demo-user-guide>`_ for more details.

---------------

Can ESP32 support 9-bit clock mode for 3-wire SPI (i.e. a mode where the first bit indicates whether the next 8 bits are command or data)?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Yes, you can refer to the command or address phase mentioned in `SPI Transactions <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/spi_master.html#spi-transactions>`_, define one of the phases as 1-bit wide, and then assign 0 or 1 to it to distinguish whether the next 8 bits are data or command. In doing so, the 9-bit clock mode for 3-wire SPI is implemented.

---------------

After routing the SDA signal of the SPI screen to GPIO35 of ESP32-S2, I expect that the SDA signal is low when idle and high when writing data. But why does this pin turn out to be high when idle and low when writing data on power-up? How to achieve my expected result? 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Please modify the ``mode`` member variable in the `spi_device_interface_config_t <https://github.com/espressif/esp-idf/blob/master/components/driver/include/driver/spi_master.h#L58>`_ structure.

---------------

Why does ESP32 return `ESP_ERR_NOT_FOUND` when using `gpio_install_isr_service() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/gpio.html#_CPPv424gpio_install_isr_servicei>`_ to initialize a new GPIO interrupt service?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  This error often means that ESP32 is running out of available interrupt sources. In this case, there should be multiple peripherals occupying interrupt sources at the same time. Try reducing the number of interrupt sources used by other components to initialize new GPIO interrupts.