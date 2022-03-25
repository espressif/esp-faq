Power consumption verification
==============================

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

What sleep modes does ESP32 have? What is the difference between them?
--------------------------------------------------------------------------

  ESP32 has three sleep modes: modem sleep, light sleep, and deep sleep.

  - Modem sleep: CPU works normally and the clock is configurable. After the station (ESP32) is connected to the AP, it is automatically turned on. After the station enters the modem sleep mode, the RF module is shut down. During the sleep, the connection to the AP is maintained. After the AP disconnects from the station, modem sleep does not work. When ESP32 is in the modem sleep mode, the CPU clock frequency can be lowered to further reduce the current.
  - Light sleep: CPU is suspended and the digital core clock is limited. It differs from the modem sleep in that besides the RF module, the CPU and part of the system clock are suspended during the sleep. After ESP32 exits the light sleep mode, the CPU resumes working. 
  - Deep sleep: The digital core is powered off and the CPU content is lost. After ESP32 enters the deep sleep mode, all modules are closed except for RTC modules; After ESP32 exits the deep sleep mode, the entire system restarts, which is similar to the system reboot; During the deep sleep, no connection to the AP is maintained.

--------------

What is the power consumption of ESP8266 when the CHIP_PU pin is low?
-------------------------------------------------------------------------------------------------------------------------------------------------

   - CHIP_PU pin is the module EN pin. When the pin is set to low level, the power consumption of the chip is about 0.5 uA.
   - In `ESP8266 datasheet <https://www.espressif.com/sites/default/files/documentation/0a-esp8266ex_datasheet_cn.pdf>`_ Table 3-4, the power consumption mode is off, which means the CHIP_PU is pulled down and the chip is disabled.
