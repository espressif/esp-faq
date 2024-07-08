Development board
=================

:link_to_translation:`zh_CN:[中文]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

--------------------

Does the `ESP32-Korvo v1.1 <https://github.com/espressif/esp-skainet/blob/master/docs/en/hw-reference/esp32/user-guide-esp32-korvo-v1.1.md>`__ development board integrate an LED driver chip?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Yes.

--------------

How to improve the overheating situation of the `ESP-EYE <https://www.espressif.com/en/products/devkits/esp-eye/overview>`__ development board?
-----------------------------------------------------------------------------------------------------------------------------------------------------------

  - If the camera is not always on, and Wi-Fi transmits data periodically, the development board can enter sleep mode during idle time to reduce power consumption.
  - Add a heat sink on top of the ESP32 chip to increase the heat dissipation area.

--------------

If a development board is not powered up through USB, how to use pins to supply power for it?
-----------------------------------------------------------------------------------------------------

  - First option: Connect the 3V3 pin to the 3V3 pin and GND to GND (If there are components on the board that are not powered by 3.3 V, these components will not work).
  - Second option: Connect the 5V pin to the 5V pin and GND to GND.

  .. note:: The power supply current should be bigger than 500 mA.

----------

What are the possible reasons for the following error when ESP8266 connects to the mobile hotspot?
-------------------------------------------------------------------------------------------------------

  .. code-block:: text

    wifi: state : 0 -> 2 (b0)
    wifi: state : 2 -> 0 (200)
    simple wifi : Disconnect reason : 2

  Please check the status of the external antenna, whether the router exists, and whether the SSID is correct.

--------------

In `ESP32-Korvo-DU1906 <https://docs.espressif.com/projects/esp-adf/en/latest/design-guide/dev-boards/get-started-esp32-korvo-du1906.html>`__, how does the DU1906 chip interact with ESP32 for audio data?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  In `ESP32-Korvo-DU1906 <https://docs.espressif.com/projects/esp-adf/en/latest/design-guide/dev-boards/get-started-esp32-korvo-du1906.html>`__, the audio data of DU1906 is transmitted to ESP32 through SPI.

--------------

Is there an Ethernet development board that supports POE power supply?
----------------------------------------------------------------------------

  `ESP32-Ethernet-Kit <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/esp32/get-started-ethernet-kit.html>`_ can satisfy this requirement.

--------------

The LED light on the `ESP32-DevKitC <https://www.espressif.com/en/products/devkits/esp32-devkitc/overview>`__ development board does not light up and the device manager cannot find the device. Why?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Check if the power supply is normal: After supplying power for the board through USB, use a multimeter to test whether there is voltage between the VCC and GND pins.
  - Check if it is a specific development board fault: Check if other `ESP32-DevKitC <https://www.espressif.com/en/products/devkits/esp32-devkitc/overview>`__ development boards can be powered up with this USB cable.
  - If you cannot locate the reason using the above methods, you can connect the board through a USB to TTL device. You only need to connect the VCC, GND, TXD pins of `ESP32-DevKitC <https://www.espressif.com/en/products/devkits/esp32-devkitc/overview>`__ to test whether it is caused by chip problems, and to check with the serial port tool whether it can print logs.
  - If possible, please test whether the serial port driver chip has voltage. For the circuit, you can refer to the `ESP32-DevKitC schematic <https://www.espressif.com/sites/default/files/documentation/esp32-devkitc-v4_reference_design_0.zip>`_.

--------------

Why can't I find the EN button mentioned in the documentation on the development board?
-------------------------------------------------------------------------------------------------------

  It is recommended to check if the development board has a Reset button. As the EN button is often used for resetting, some development boards will mark it as a Reset button.

---------------

I can't find the serial port in the device manager after connecting the ESP32 development board to a Windows computer. What could be the reasons?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

  After connecting the ESP32 development board to a Windows computer, if you can't find the serial port in the device manager, it could be due to the following reasons:

  - Driver not installed: Before connecting the ESP32 development board to a Windows computer, you need to install the driver. If the driver is not installed or installed incorrectly, the development board will not be recognized as a serial port device. Download and install the `FT232R USB UART driver <https://www.usb-drivers.org/ft232r-usb-uart-driver.html>`_.
  - Loose or damaged USB cable: If the USB cable is loose or damaged, the development board cannot be correctly recognized. Users can replace the USB cable or check if the USB cable is plugged in tightly to ensure a normal connection between the USB cable and the computer.
  - Faulty development board: If the above two reasons can be excluded, it may be because development board itself is faulty. Users can try connecting to other USB ports or other computers for testing, or detect and repair the development board.

  It should be noted that when testing the connection of the development board, you need to confirm whether the serial port settings and driver settings of the development board are correct. Some development boards need to manually select the correct port and baud rate in the serial port settings to connect to the computer. At the same time, some drivers also need to manually set the port and baud rate to ensure consistency with the development board settings.

---------------

For the `ESP32-LyraT v4.3 <https://espressif-docs.readthedocs-hosted.com/projects/esp-adf/en/latest/design-guide/dev-boards/get-started-esp32-lyrat.html>`__ audio development board, it's hard to enter download mode even when the Boot button is held down for a long time. What could be the reason?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The correct procedure is holding down the Boot button and pressing the RST button (without releasing the Boot button), and then releasing the RST button (with the Boot button still held down). When the board enters download mode and starts downloading, you can release the Boot button.

---------------

How long does it take for the ESP-WROOM-02D module to restart after the reset signal?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  It will restart when the input level is lower than 0.6 V for more than 200 μs.

---------------------

According to the schematic of `ESP32-LyraT-Mini <https://espressif-docs.readthedocs-hosted.com/projects/esp-adf/en/latest/design-guide/dev-boards/get-started-esp32-lyrat-mini.html>`__, the analog output of the ES8311 codec chip is connected to the input of the ES7243 ADC chip. What is the purpose of this?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The hardware acquisition circuit of the AEC reference signal simultaneously transmits the DAC output of the Codec (ES8311) to the speaker PA and the ADC (ES7243) AINLP/N, of which the signal collected would be send back to the ESP32 as the reference signal for the AEC algorithm.

-----------------

When using the `ESP32-MINI-1 <https://www.espressif.com/sites/default/files/documentation/esp32-mini-1_datasheet_en.pdf>`__ module, the serial port printed the follows log when powered on. What could be the reason?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

      rst:0x10 (RTCWDT_RTC_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
      invalid header: 0xffffffff
      invalid header: 0xffffffff
      invalid header: 0xffffffff
      invalid header: 0xffffffff
      invalid header: 0xffffffff
      invalid header: 0xffffffff
      invalid header: 0xffffffff
      invalid header: 0xffffffff
      ets Jul 29 2019 12:21:46

  The is because flash is not programmed.

---------------

Which GPIO is connected to the RGB LED of the `ESP32-S3-DevKitC-1 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/hw-reference/esp32s3/user-guide-devkitc-1.html#esp32-s3-devkitc-1-v1-1>`_ development board?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The RGB LED on the `ESP32-S3-DevKitC-1 v1.0 <https://dl.espressif.com/dl/SCH_ESP32-S3-DEVKITC-1_V1_20210312C.pdf>`_ development board is connected to GPIO48.
  - The RGB LED on the `ESP32-S3-DevKitC-1 v1.1 <https://dl.espressif.com/dl/schematics/SCH_ESP32-S3-DevKitC-1_V1.1_20221130.pdf>`_ development board is connected to GPIO38.
  - The reason why the `ESP32-S3-DevKitC-1 v1.1 <https://dl.espressif.com/dl/schematics/SCH_ESP32-S3-DevKitC-1_V1.1_20221130.pdf>`_ development board changed the RGB LED pin to GPIO38 is that the `ESP32-S3R8V <https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf>`_ chip’s VDD_SPI voltage has been set to 1.8 V. Therefore, unlike other GPIOs, GPIO47 and GPIO48 in the VDD_SPI power domain of this chip also operate at 1.8 V.

----------------

When using the ESP32-S3-DevKitC-1 development board as a 3.3 V power supply for other devices, what is the maximum output current it can provide?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The `ESP32-S3-DevKitC-1 development board <https://dl.espressif.com/dl/schematics/SCH_ESP32-S3-DevKitC-1_V1.1_20221130.pdf>`_ uses the power chip SGM2212-3.3XKC3G, which can provide a maximum output current of 800 mA.
