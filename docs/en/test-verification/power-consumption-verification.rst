Power Consumption Verification
===================================

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

Why does ESP32 reboot when it is woken up from Deep-sleep mode?
------------------------------------------------------------------------

  When ESP32 is in Deep-sleep mode, the digital core is powered off and the information stored in CPU will be lost. After ESP32 is woken up from Deep-sleep mode, it re-boots firmwares and re-loads them to the internal memory. The application information that requires to be reserved can be saved in RTC, as RTC is still powered on in Deep-sleep mode. The reserved information can be loaded after wake-up.


-------------

What sleep modes does ESP32 support? What is the difference between them?
---------------------------------------------------------------------------

  ESP32 supports three sleep modes: Modem-sleep, Light-sleep, and Deep-sleep.

  - Modem-sleep: CPU works normally and the clock is configurable. The station (ESP32) automatically turns on after it is connected to the AP. After ESP32 enters Modem-sleep mode, the RF module is shut down, and the station remains connected to the AP. If ESP32 disconnects to the AP, it will not work in Wi-Fi Modem-sleep mode. In Modem-sleep mode, the CPU clock frequency can be lowered to further reduce the current consumption.
  - Light-sleep: CPU is suspended and the digital core clock is limited. When ESP32 is in Light-sleep mode, not only the RF module is closed, CPU and partial system clocks are also suspended. After ESP32 exits Light-sleep mode, the CPU resumes working. 
  - Deep-sleep: The digital core is powered off and the information stored in CPU is lost. After ESP32 enters Deep-sleep mode, all modules are closed except for RTC. After it exits Deep-sleep mode, the entire system restarts, which is similar to the system reboot. ESP32 does not remain connected to the AP in Deep-sleep mode.

  Please refer to *Table 8: Power Consumption by Power Modes* in `ESP32 datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf>`__ for the corresponding sleep power consumption.

--------------

Can ESP32 in Deep-sleep mode be woken up by any RTC_GPIO?
---------------------------------------------------------------

  Yes. For the configuration of RTC_GPIO, please refer to `ESP32 datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_ > Chapter *Pin Definitions* > Section *Pin Description*.

---------------

What is the power consumption of ESP8266 when the CHIP_PU pin is at the low level?
-------------------------------------------------------------------------------------------------------------------------------------------------

   - CHIP_PU pin is the module EN pin. When the pin is set to the low level, the power consumption of the chip is about 0.5 μA.
   - In Table Power Consumption by Power Modes of `ESP8266 Datasheet <https://www.espressif.com/sites/default/files/documentation/0a-esp8266ex_datasheet_en.pdf>`_ > *Functional Description* > *Power Management*> *Table 3-4. Power Consumption by Power Modes*, shut down power mode means CHIP_PU is pulled down and the chip is disabled.

--------------

Why does the minimum current of ESP32 in Light-sleep increase when the timer is not used as a wakeup source?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - By default, to avoid potential issues, `esp_light_sleep_start <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/sleep_modes.html#_CPPv421esp_light_sleep_startv>`_ functions will not power down flash. This is to prevent errors that may be caused if the flash is not fully powered off and back on when the device has just gone to sleep and is immediately woken up.
  - For the issue details and on how to optimize power consumption in this scenario please refer to `Power-down of Flash <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/sleep_modes.html#power-down-of-flash>`_ in the ESP-IDF Programming Guide.

---------------

In ESP32's Deep-sleep mode, using an internal 150 KHz RTC clock or using an external 32 KHz, which consumes more power?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - If the RTC clock source is external 32 kHz crystal, there is no difference in power consumption.
  - If an external 32 kHz oscillator is connected to the hardware, the power consumption will increase by 50 to 100 μA regardless of which RTC clock source is selected.

-----------------

What are the requirements for CPU frequency to ensure normal operation of the RF module when reducing power consumption by reducing the CPU frequency?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  CPU frequency should be 80 Mhz at least.

-----------

When I run the `light-sleep example <https://github.com/espressif/esp-idf/tree/v5.1.1/examples/system/light_sleep>`__ on ESP32-S3 modules, if I only use the GPIO wake-up source and do not enable the timer to wake up, the power consumption is 3 mA, which is significantly different from that on the datasheet. Why? 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - When using the RTC GPIO wake-up source, please add the following code for testing before the module enters light-sleep mode. **However, please do not wake up the module immediately after the it falls asleep when only using the GPIO as the wake-up source. This is because flash may cause a failure when the duration between power-up and power-down is too short under the situation without configuring the timer.**

  .. code:: c

    esp_sleep_pd_config(ESP_PD_DOMAIN_VDDSDIO,ESP_PD_OPTION_OFF);

-----------

When using Timer for wake-up based on the `esp-idf/examples/system/deep_sleep <https://github.com/espressif/esp-idf/tree/v5.1.1/examples/system/deep_sleep>`_ example, although the wake-up time is set to 2.5 hours, it wakes up around 1 hour. What could be the reason?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 The code block is as follows:

    .. code:: c

      const int wakeup_time_sec = 9000;
      printf("Enabling timer wakeup, %ds\n", wakeup_time_sec);
      ESP_ERROR_CHECK(esp_sleep_enable_timer_wakeup(wakeup_time_sec * 1000000));

  - An overflow may occur during the ``ESP_ERROR_CHECK(esp_sleep_enable_timer_wakeup(wakeup_time_sec * 1000000));`` calculation. You may modify the code as follows:
    
    .. code:: c

      const uint64_t wakeup_time_sec = 9000;
      printf("Enabling timer wakeup, %lld\n", wakeup_time_sec);
      ESP_ERROR_CHECK(esp_sleep_enable_timer_wakeup(wakeup_time_sec * 1000000));

  - Or directly write it as ``esp_sleep_enable_timer_wakeup(9000 * 1000000ULL);``.