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

How is the accuracy of ESP8266 ADC?
----------------------------------------------------------

  - The ESP8266 ADC is 10 bits, and its theoretical accuracy is 2 :sup:`10` = 1024.
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
  - Its sampling rate can reach 100000 times per second without Wi-Fi.
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

  ADC input range cannot reach 3.3 V. See `ADC Attenuation <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/adc.html#adc-attenuation>`__ for details.

---------------

What is the input resistance of ESP32 ADC?
-----------------------------------------------------------------------------------------------------------------------------

  ADC is capacitive and can be considered as a large resistance.

-------------------------

When using ESP32's ADC to detect the power supply voltage, is it necessary to divide the voltage?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The ADC reference voltage of ESP32 is 1100 mV, but the ADC measurable range can be increased by internal attenuation. For more information on the measurable range, please refer to `ADC Attenuation <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/peripherals/adc.html#adc-attenuation>`__. If it exceeds the range, voltage division is required.

-----------------

What is ESP32's highest sampling rate in ADC DMA mode?
--------------------------------------------------------------------------------------------------------------------------------------------------------------

  ESP32 supports up to 2 MHz of sampling rate theoretically.
  
-----------------

When an ESP32 calling ``adc2_get_raw()`` between ``esp_wifi_start()`` and ``esp_wifi_stop()``, the read operation fails. What is the reason?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Because ADC2 is shared with the Wi-Fi module. The Wi-Fi driver uses ADC2 and has higher priority. Therefore, the application can only use ADC2 when the Wi-Fi driver is not activated.

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
