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
-------------------------------------------------------------------------------

  The ESP-WROOM-02D module is a Wi-Fi module based on the ESP8266 chip, which supports communication with external SPI flash devices using SPI interfaces. Specifically, the ESP-WROOM-02D module provides 4 SPI interface pins, GPIO12, GPIO13, GPIO14, and GPIO15. Among these pins, GPIO12~GPIO14 can be used as the MISO, MOSI, and SCLK pins for the SPI master interface, and GPIO15 can be used as the CS pin for the SPI slave interface.

  To connect an external SPI flash device to the ESP-WROOM-02D module, the MOSI, MISO, SCK, and CS pins of the SPI flash device should be connected to the GPIO12~GPIO14 and GPIO15 pins of the ESP-WROOM-02D module. Additionally, the SPI interface needs to be properly configured and initialized in the firmware to ensure correct communication of ESP8266 with the external SPI flash device.

  It should be noted that the model and capacity of the external SPI flash device should be selected based on the specific application requirements. In addition, timing characteristics and reliability of the SPI flash device should be considered to ensure data can be transmitted correctly and stably. Moreover, factors such as environment noise and physical distance between the SPI flash device and the ESP-WROOM-02D module should be considered to improve the reliability and performance of the system as much as possible.

--------------

Taking ESP-WROOM-S2 as the slave device and STM32 as MCU, is it possible to download through SPI interface?
----------------------------------------------------------------------------------------------------------------------------------------------

  No, we use UART0 to download by default. You can also design OTA support yourself in firmware.

--------------

What is the difference among SPI0, SPI1, HSPI and VSPI in ESP32?
-------------------------------------------------------------------------------------

  - ESP32 has 4 SPIs, SPI0 and SPI1 are two peripherals, also known as MSPI. SPI0 and SPI1 share the same SPI bus (same signals and IOs). The difference is, MSPI CS0 is connected to the main flash for firmware storage, and MSPI CS1 is connected to PSRAM. SPI2 and SPI3 are general-purpose SPIs that are available for customers to use.
  - HSPI represents the above-mentioned SPI2, and VSPI represents the SPI3. The two sets of SPIs are general-purpose SPIs and support QSPI.

-------------------------

The maximum data transmission of SPI DMA on ESP series chips is 4095 bytes. Is it because of hardware limitation?
----------------------------------------------------------------------------------------------------------------------------------------------

  - Yes, this is a hardware limitation. A single node in the DMA table can only mount 4095 bytes of data.
  - However, a single SPI DMA transmission can mount more data through several nodes. At this time the maximum data transfer byte number is limited by the hardware register ``SPI_LL_DATA_MAX_BIT_LEN`` (whose value varies with different chip series and can be found in ESP-IDF), i.e., ``max_transfer_sz <= (SPI_LL_DATA_MAX_BIT_LEN / 8)``.

--------------------

Does the SPI of the ESP series chip need to perform semaphore synchronization to access three SPI slave devices simultaneously?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The same SPI peripheral, as the master, can only communicate with one slave at a time, and CS decides which slave to communicate with. If you connect 3 slave devices to the SPI driver and communicate with them separately, it is okay and recommended.
  - It is recommended to operate devices sharing the same SPI in only one task. Otherwise, it is not thread-safe. Communication needs to be synchronized through semaphores. For specific issues, see `SPI Master Driver > Driver Features <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/spi_master.html#driver-features>`_.

---------------------------

When using an ESP32 board for development and testing based on ESP-IDF release/v4.3, I received the following error log during compilation. What is the reason?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    spi_flash:Detected size(8192K) smaller than the size in the binary image header(16384K).Probe failed.

  The reason is that the configured flash size is larger than the actual flash size. In order to avoid misuse of a larger address space, the actual flash size is checked.

----------------

What is the maximum transmission speed supported by SPI slave?
-------------------------------------------------------------------------------
  :CHIP\: ESP32:

  ESP32 can support up to 10 M of transmission speed when serves as an SPI slave.

------------------------------

How many bytes of data can be transferred at once using the ESP series chip as an SPI host device in non-DMA mode?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Due to the limitations of the SPI hardware FIFO, a maximum of 64 bytes can be transferred at once in non-DMA mode. Refer to `SPI Master Driver > Transaction Duration <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/spi_master.html#transaction-duration>`__.
  - When transmitting no more than 32 bits, the 4-byte array inside the SPI Master driver can be used as the buffer for sending data. Refer to `SPI Master Driver > Transactions with Data Not Exceeding 32 Bits <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/spi_master.html#transactions-with-data-not-exceeding-32-bits>`_ for details.
  - When transmitting more than 32 bits, you need to create an SPI data transmission buffer yourself. You can refer to the `SPI Master Driver > SPI Transactions <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/spi_master.html#spi-transactions>`_ for instructions.

--------------------------------

When using the ESP32-S3-WROOM-1 (ESP32-S3R2) module to enable its PSRAM configuration based on the "hello-world" example in ESP-IDF v4.4, the following error is printed. What is the reason?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

      E (232) spiram: Virtual address not enough for PSRAM!

  ESP32-S3R2 chip integrates a 4-wire 2 MB PSRAM, please set PSRAM Mode to **Quad** mode in menuconfig before your action as follows:

  ``menuconfig`` > ``Component config`` > ``ESP32S3 Specific`` > ``Support for external, SPI connected RAM`` > ``SPI RAM config`` > ``Mode (QUAD/OCT) of SPI RAM chip in use (Ouad Mode PSRAM)``

-------------------------

When using the ESP32-S3-WROOM-2 (ESP32-S3R8V) module to enable the PSRAM configuration based on the "hello-world" example in ESP-IDF v4.4, the following error is printed. What is the reason?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

      E (453) psram: psram ID read error: 0x00ffff
      E (454) cpu start: Failed to init external RAM!

  ESP32-S3R8V chip integrates a 8-wire 8 MB PSRAM, please set PSRAM mode to **Octal** mode in menuconfig before your action as follows:

    ``menuconfig`` > ``Component config`` > ``ESP32S3 Specific`` > ``Support for external, SPI connected RAM`` > ``SPI RAM config`` > ``Mode (QUAD/OCT) of SPI RAM chip in use (Octal Mode PSRAM)``

-------------------

Does ESP8266 RTOS SDK support full duplex for SPI?
--------------------------------------------------------------------------------------------------

  :CHIP\: ESP8266:

  No, it doesn't. Because ESP8266 doesn't support DMA, in order to improve the transmission performance, the entire FIFO is used. So it can only be half duplex. Please refer to `spi readme <https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/peripherals/spi>`_ for more details.

---------------

Can the ESP series chips support the 9-bit clock mode of three-wire SPI (i.e., the mode where the first bit indicates whether the following 8 bits are command or data)?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Currently, the ESP32, ESP32-S, ESP32-C series chips do not support non-byte aligned data transmission, i.e., they only support 8-bit aligned data transmission. For a detailed explanation of this issue, see `Github issue <https://github.com/espressif/esp-idf/issues/8487>`_ and `documentation <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/spi_master.html#transactions-with-integers-other-than-uint8-t>`__.
  - Subsequent new versions of the ESP chip may support non-byte aligned data transmission, but there is currently no specific timetable.

---------------

After setting a pin of the ESP series chip as the SDA data line, the expected result is that the SDA line should be low when idle, and high when writing data. But why is this pin high when idle upon power-up, and low when writing data? How can I achieve the expected result?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - In SPI, the idle levels of the MOSI (SDA) and SCK signal lines are controlled by the SPI mode.
  - This can be achieved by modifying the `mode` member variable in the `spi_device_interface_config_t` structure `<https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/spi_master.html#_CPPv4N29spi_device_interface_config_t4modeE>`_.

----------------

How many bytes can a single DMA Buffer support when the ESP32-C6 is in SPI DMA mode?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - For ESP32-C6 in SPI DMA mode, a single DMA Buffer supports 4092 bytes at the maximum.

---------------

Does ESP32, as an SPI host, support a 30 MHz clock?
------------------------------------------------------------------------------------------------------------------------------

  - Not supported. When ESP32 acts as an SPI host, it can support up to 80 MHz CLK when using SPI IO_MUX pins, and supports integer division at 80 MHz.
  - When using GPIO matrix pins, it can support up to 40 MHz CLK. If using the full-duplex transmission mode of GPIO matrix pins, it only supports up to 26 MHz CLK. For detailed instructions, refer to the `SPI Master Driver <https://docs.espressif.com/projects/esp-idf/en/release-v5.2/esp32/api-reference/peripherals/spi_master.html#spi>`_ software usage instructions.
