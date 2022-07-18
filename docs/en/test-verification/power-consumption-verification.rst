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
-----------------------------------------------------------------------

  When ESP32 is in Deep-sleep mode, the digital core is powered off and the information stored in CPU will be lost. After ESP32 is woken up from Deep-sleep mode, it re-boots firmwares and re-loads them to the internal memory. The application information that requires to be reserved can be saved in RTC as RTC is still powered on in Deep-sleep mode. The reserved information can be loaded after wake-up.


-------------

Which sleep modes does ESP32 support? What is the difference between them?
---------------------------------------------------------------------------

  ESP32 supports three sleep modes: Modem-sleep, Light-sleep, and Deep-sleep.

  - Modem-sleep: CPU works normally and the clock is configurable. The station (ESP32) automatically turns on after it is connected to the AP. After ESP32 enters Modem-sleep mode, the RF module is shut down, and the station remain connection to the AP. If ESP32 disconnects to the AP, it will not work in Wi-Fi Modem-sleep mode. In Modem-sleep mode, the CPU clock frequency can be lowered to further reduce the current consumption.
  - Light-sleep: CPU is suspended and the digital core clock is limited. When ESP32 is in Light-sleep mode, not only the RF module is closed, CPU and partial system clocks are also suspended. After ESP32 exits Light-sleep mode, the CPU resumes working. 
  - Deep-sleep: The digital core is powered off and the information stored in CPU is lost. After ESP32 enters Deep-sleep mode, all modules are closed except for RTC. After it exits Deep-sleep mode, the entire system restarts, which is similar to the system reboot. ESP32 does not remain connection to the AP in Deep-sleep mode.

--------------

Can ESP32 in Deep-sleep mode be woken up by any RTC_GPIO?
---------------------------------------------------------------

  Yes. For the configuration of RTC_GPIO, please refer to `ESP32 datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_ > Chapter *Pin Definitions* > Section *Pin Description*.

---------------

What is the power consumption of ESP8266 when the CHIP_PU pin is at the low level?
-------------------------------------------------------------------------------------------------------------------------------------------------

   - CHIP_PU pin is the module EN pin. When the pin is set to the low level, the power consumption of the chip is about 0.5 μA.
   - In Table Power Consumption by Power Modes of `ESP8266 Datasheet <https://www.espressif.com/sites/default/files/documentation/0a-esp8266ex_datasheet_en.pdf>`_, shut down power mode means CHIP_PU is pulled down and the chip is disabled.

--------------

Why does the minimum current of ESP32 in Light-sleep increase when the timer is not used as a wakeup source?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - By default, to avoid potential issues, `esp_light_sleep_start <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/sleep_modes.html#_CPPv421esp_light_sleep_startv>`_ and `esp_deep_sleep_start <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/sleep_modes.html#_CPPv420esp_deep_sleep_startv>`_ functions will not power down flash. It takes time to power down the flash and during this period the system may be woken up, which then actually powers up the flash before this flash could be powered down completely.
  - And the flash will be powered down if the timer wakeup source is enabled. As a result, the minimum current will be relatively small. 
  - For power-sensitive applications without timer wakeup, you can close the ``Power down flash in light sleep when there is no SPIRAM`` and open ``Flash leakage current workaround in light sleep`` in menuconfig.
