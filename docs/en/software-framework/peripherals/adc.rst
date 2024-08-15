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
-----------------------------------------------------------

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

  Since Wi-Fi also uses ADC2, and the Wi-Fi driver has a higher priority, the application may fail to read using ``adc2_get_raw()`` during the operation period of Wi-Fi. It is recommended to check the return value of this function and re-measure it after failure. 

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
  - When disabling the ADC interface mode, please use `adc_digi_stop() <https://docs.espressif.com/projects/esp-idf/en/release-v4.4/esp32/api-reference/peripherals/adc.html#_CPPv413adc_digi_stopv>`__ to disable the ADC.

---------------------

What is the measurement error between the ADCs of the ESP32 chip?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  By default, the measurement error between ESP32 ADCs is ±6%, please refer to `ESP32 datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_ for details.

-------------

Can ESP32 measure different data from two ADC channels at the same time, such as current and voltage?
---------------------------------------------------------------------------------------------------------------------------------------------------
   
  It is not possible to read multiple ADC channels at the same time using one ADC, but you can poll the data of both ADC channels in turn.

-------------

Why can't the measured voltage reach the nominal 3100 mV when the ESP32-S3 ADC is configured as ``ADC_ATTEN_DB_12``?
--------------------------------------------------------------------------------------------------------------------

  When ESP32-S3 ADC1 or ADC2 is configured as ``ADC_ATTEN_DB_12``, the voltage measurement range is ``0 ~ 3100 mV``. However, the maximum voltage measurement value of some chips is less than ``3100 mV``. The following two methods can be used to solve this problem:

- Solution 1: Try to avoid using the boundary voltage values. You can use a divider circuit to reduce the input voltage to an intermediate value for higher accuracy and consistency. 
- Solution 2: Use the software `ADC Range Extension Solution <https://docs.espressif.com/projects/espressif-esp-iot-solution/en/latest/others/adc_range.html>`_ to increase the maximum voltage measurement to ``3300 mV``.

-------------

Can we use GPIO0 as the ADC pin when using ESP32 as a Wi-Fi access point?
---------------------------------------------------------------------------------------------------------------------------------------------------

  - The ESP32 ADC2 pins cannot be used when you are using Wi-Fi. So, if you are having trouble getting the value from an ADC2 GPIO while using Wi-Fi, you may consider using an ADC1 GPIO instead. For more details, please refer to `Hardware Limitations of ADC Continuous Mode <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/adc_continuous.html>`__ and `Hardware Limitations of ADC Oneshot Mode <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/adc_oneshot.html>`__.
  - The GPIO0, GPIO2, GPIO5, GPIO12 (MTDI), and GPIO15 (MTDO) are strapping pins. When using GPIO0 for other functions, you need to pay attention to the GPIO level during power-up. If the GPIO0 level is low during power-up, the chip can enter the download mode. For more infomation, please refer to `ESP32 datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`__. 

--------------------

I tried to test the functionality of ADC2 using GPIO19 and GPIO20 of ESP32-S3 based on `"esp-idf/examples/peripherals/adc/oneshot_read" <https://github.com/espressif/esp-idf/tree/release/v5.0/examples/peripherals/adc/oneshot_read>`_ example and set the attenuation parameter of ADC2 to 11 dB. When the input voltage is 0.6 V, why are the test results 1.1 V and 2.8 V?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Please check whether both two ADC2 channels have been configured according to `adc_oneshot_config_channel() <https://github.com/espressif/esp-idf/blob/886e98a2c1311556eb6be02775d49703d6050222/examples/peripherals/adc/oneshot_read/main/oneshot_read_main.c#L90>`_.

----------

Can ESP32 support some ADC channels in DMA mode and the other ADC channels in oneshot mode under the same ADC controller?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - To use the DMA mode for ESP32 ADC, ESP-IDF v5.0 or later versions should be used.
  - ADC2 of ESP32 does not support DMA mode.
  - In the same ADC controller, it does not support that some ADC channels are in oneshot mode and other ADC channels are in DMA mode. Please refer to the `"ESP32 ADC hardware-limitations" <https://docs.espressif.com/projects/esp-idf/en/v5.1.1/esp32/api-reference/peripherals/adc_continuous.html#hardware-limitations>`__.
  - In the software, it is recommended to use the `adc_continuous_config_t <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v5.0/esp32/api-reference/peripherals/adc_continuous.html#_CPPv423adc_continuous_config_t>`_ API to set ADC1 as DMA mode and use the `adc_oneshot_config_channel <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v5.0/esp32/api-reference/peripherals/adc_oneshot.html?highlight=adc_oneshot_config_channel#_CPPv426adc_oneshot_config_channel25adc_oneshot_unit_handle_t13adc_channel_tPK22adc_oneshot_chan_cfg_t>`_ API to set ADC2 as oneshot mode.

------------

When using ESP-IDF v5.1 to test ADC2 based on the ESP32-S3-WROOM-1 module, inputting 3.3 V via GPIO12 yet getting a read voltage of 5 V. What could be the reason?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: c

    I (455346) EXAMPLE: ADC2 Channel[1] Raw Data: 4095
    I (455346) EXAMPLE: ADC2 Channel[1] Cali Voltage: 4985 mV
    I (456346) EXAMPLE: ADC2 Channel[1] Raw Data: 4095
    I (456346) EXAMPLE: ADC2 Channel[1] Cali Voltage: 4985 mV

  - With normal ADC raw data readings, the reason why ADC conversion value becomes 5 V is because that the effective measurement range of ESP32-S3 ADC is 2900 mV. Please refer to the `ESP32-S3 ADC attenuation level corresponding effective measurement range <https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/schematic-checklist.html#adc>`_.
  - An input voltage exceeding 2900 mV is undefined, which would lead to this situation. If you need to measure an input voltage greater than 2900 mV, it is recommended to use voltage division or adopt the `ESP32-S3 ADC Range Extension Solution <https://docs.espressif.com/projects/espressif-esp-iot-solution/en/latest/others/adc_range.html#esp32-s3-adc>`_.

Can the reference source of the ADC be externally applied? If it can be applied, which pin should it be applied to? What is the internal reference voltage of the ADC?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The ADC does not support external reference voltage. It can only use internal reference voltage.
  - The internal reference voltage is 1.1 V.
