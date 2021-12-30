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

  ESP32 has three sleep modes: Modem-sleep, Light-sleep, and Deep-sleep.

  - Modem-sleep:

     - The Station Legacy Fast sleep mode specified in the Wi-Fi specification, in which the Station sends a NULL frame to notify the AP to sleep or wake up.
     - After the station is connected to the AP, the station is automatically turned on. After the station enters the Modem-sleep mode, the RF module is shut down. During the modem sleep, the connection to the AP is maintained. After the AP disconnects from the station, Modem-sleep does not work.
     - After ESP32 enters Modem-sleep mode, the CPU clock frequency can be lowered to further reduce the current.

  - Light-sleep:

     - A Station sleep mode based on Modem-sleep;
     - The differences between Light-sleep and Modem-sleep are:

         - After ESP32 enters the Light-sleep mode, not only the RF module but also the CPU and part of the system clock are suspended.
         - After ESP32 exits the Light-sleep mode, the CPU resumes working. 

  - Deep-sleep:

     - A sleep mode that is not specified in the Wi-Fi specification;
     - After ESP32 enters the Deep-sleep mode, all modules are closed except for RTC modules;
     - After ESP32 exits the Deep-sleep mode, the entire system reruns, which is similar to the system reboot;
     - During the deep sleep, no connection to the AP is maintained.

--------------

What is the power consumption of ESP8266 when the CHIP_PU pin is low?
-------------------------------------------------------------------------------------------------------------------------------------------------

   - CHIP_PU pin is the module EN pin. When the pin is set to low level, the power consumption of the chip is about 0.5 uA.
   - In `ESP8266 datasheet <https://www.espressif.com/sites/default/files/documentation/0a-esp8266ex_datasheet_cn.pdf>`_ Table 3-4, the power consumption mode is off, which means the CHIP_PU is pulled down and the chip is disabled.
