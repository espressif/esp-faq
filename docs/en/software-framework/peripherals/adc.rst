Analog-to-Digital Converter (ADC)
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

What is the resolution of ESP8266 ADC?
----------------------------------------------------------

  - The 10-bit ESP8266 ADC has a theoretical resolution of 2 :sup:`10` = 1024.
  - After connected to a router, the ESP8266 will enter Modem-sleep mode from STA mode, causing the change of the reference value inside the chip. Therefore, the ADC could measure the data change.
  - If you expect an accurate result, please read the ADC value using function ``system_adc_fast_read`` after turning off Wi-Fi.

--------------

How to get the Bitmap information of the ADC register?
----------------------------------------------------------------------------

  Since the ADC of ESP8266 is highly integrated with the internal RF circuit, the Bitmap and register information is not opened. Please contact sales@espressif.com if you have any special needs.

--------------

How many channels does ESP32 ADC have? What is the sampling rate and significant digit?
---------------------------------------------------------------------------------------------------------------

  - The ESP32 ADC has 18 channels.
  - If you stop Wi-Fi and use ADC DMA, the sampling rate does not exceed 2 MHz theoretically. However, we recommend you to use a smaller sampling rate in practice.
  - Its sampling rate can reach 1000 times per second with Wi-Fi.
  - The internal significant digit of ADC is 12 bits.

--------------

When calling the API ``adc_read_fast()`` with ESP8266, will it cause a Wi-Fi disconnection?
----------------------------------------------------------------------------------------------------------------------

  - Please turn off Wi-Fi and interrupts first before calling ``adc_read_fast()``. Please refer to the `Specification <https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/api-reference/peripherals/adc.html?highlight=adc_read#_CPPv413adc_read_fastP8uint16_t8uint16_t>`_ of this API.
  - Since the ``API adc_read_fast()`` performs continuous acquisition and the ADC is partially coupled internally with Wi-Fi RF, so it is not possible to call this function with Wi-Fi turned on.
  - Please use ``adc_read()`` for ADC acquisition when Wi-Fi is on. To ensure data stability, you need to use function ``esp_wifi_set_ps(WIFI_PS_NONE)`` to turn off Wi-Fi Modem-sleep mode.
 
.. note::

    ADC sampling rate: can reach 100000 times per second with Wi-Fi turned off, and 1000 times per second with Wi-Fi turned on.

----------------

If I float the ADC pin and print out VDD3P3 value (65535), then the voltage of VDD3P3 should be 65535/1024 ≈ 63 V. Why this is not the correct voltage value?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The input of ADC should be in the range of 0 V to 3.3 V (the upper limit varies in different chips). The floating measurement is an undefined state.

---------------

What is the input resistance of ESP32 ADC?
-----------------------------------------------------------------------------------------------------------------------------

  ADC is capacitive and can be considered as a large resistance.

-------------------------

When using ESP32's ADC to detect the power supply voltage, is it necessary to divide the voltage?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The ADC reference voltage of ESP32 is 1100 mV, but the ADC measurable range can be increased by configuring the internal attenuation. For more information on the measurable range, please refer to `ADC Section <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`__ in the chip datasheet. If the measurable range cannot satisfy your requirement, please add an external voltage division circuit.

-----------------

What is ESP32's highest sampling rate in ADC DMA mode?
--------------------------------------------------------------------------------------------------------------------------------------------------------------

  ESP32 supports up to 2 MHz of sampling rate theoretically.
  
-----------------

When an ESP32 calling ``adc2_get_raw()`` between ``esp_wifi_start()`` and ``esp_wifi_stop()``, the read operation fails. What is the reason?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Since Wi-Fi also requires the use of ADC2, and the Wi-Fi driver has a higher priority. Therefore, the application can only use ADC2 when the Wi-Fi driver is closed.

---------------

Does ESP32 support using ADC2 and Bluetooth simultaneously?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Yes.

-----------------

What is the sampling rate range supported by the ADC DMA mode of the ESP32-S2 chip?
--------------------------------------------------------------------------------------------------------------------------

  Frequency limit : 611 Hz ~ 83333 Hz.

----------------------

Does the ADC of ESP32 support simultaneous sampling of multiple channels?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  No, If you are using ADC to do multi-channel sampling, please implement it via ADC polling scheme.

--------------------

When using the ESP32-WROVER-B module with release/v4.2 version of ESP-IDF, I set the GPIO as an ADC interface, and then set GPIO to other IO mode while with IO mode not effective without any hardware reset, this GPIO does not respond. How do I release the corresponding GPIO mode?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Please do not set the ADC interface as input-only GPIO.
  - When disabling the ADC interface mode, please use ``adc_digi_stop()`` to disable the ADC.

---------------------

What is the measurement error between the ADCs of the ESP32 chip?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  By default, the measurement error between ESP32 ADCs is ±6%, please refer to `ESP32 datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_ for details.

-------------

Can ESP32 measure different data from two ADC channels at the same time, such as current and voltage?
---------------------------------------------------------------------------------------------------------------------------------------------------
   
  It is not possible to read multiple ADC channels at the same time using one ADC, but you can poll the data of both ADC channels in turn.

-------------

When ESP32-S3 ADC is configured as ``ADC_ATTEN_DB_11``, why does the measured voltage not reach ``3100 mV``?
-------------------------------------------------------------------------------------------------------------------

  When ESP32-S3 ADC1 or ADC2 is configured as ``ADC_ATTEN_DB_11``, the voltage measurement should be in the range of ``0 ~ 3100 mV``. However, the maximum voltage measurement of some chips may be less than ``3100 mV`` due to consistency issues. You may use the following two solutions to fix this issue:

- Solution 1: Try to avoid using the boundary voltage values. You can use a divider circuit to reduce the input voltage to an intermediate value for higher accuracy and consistency. 
- Solution 2: Use the software `ADC Range Extension Solution <https://docs.espressif.com/projects/espressif-esp-iot-solution/en/latest/others/adc_range.html>`_ to increase the maximum voltage measurement to ``3300 mV``.