Chip comparison
===============

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

What's the difference between single-core and dual-core of ESP32 (programming method, features performance, power consumption, and etc.)?
----------------------------------------------------------------------------------------------------------------------------------------------

  The main difference would be the additional independent core, on which some highly real-time operations can be located.

  - The programming method is the same, and users only have to configure the freertos to run on the single core. See ``make menuconfig → Component config → FreeRTOS → [*] Run FreeRTOS only on first core``;
  - From the performance aspect, they are only different when it comes to high-load calculations. If not regarding to such calculations, there is no obvious difference in use (e.g., AI algorithm, high real-time interruption);
  - There is only a slice of difference in power consumption when entering modem-sleep mode. For more details, please refer to `ESP32 Technical Reference Manual <https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf>`_.

--------------

What's the difference between ESP32 E03 and the previous version in software use?
------------------------------------------------------------------------------------

  Not much differences in software use, and this version is  compatible to old firmwares and some bugs in hardware have been solved. For more information, please refer to `ESP32 ECO V3 User Guide <https://www.espressif.com/sites/default/files/documentation/ESP32_ECO_V3_User_Guide__EN.pdf>`_.