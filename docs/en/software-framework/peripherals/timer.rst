Timer
============

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

What should I pay attention to when using the HW timer interrupt with ESP8266?
-----------------------------------------------------------------------------------------------------------

  - Please refer to `ESP8266 Technical Reference Manual <https://www.espressif.com/sites/default/files/documentation/esp8266-technical_reference_en.pdf>`__ regarding the related APIs.
  - Typically, the hardware interrupt callback function should finish as quickly as possible and be placed in IRAM to avoid the impact of Cache being disabled. For RTOS SDK, add the linker attribute IRAM_ATTR before the function name.

--------------

How to set interrupt priority for timers?
--------------------------------------------

  - The esp_timer, using ESP32 as an example, allows you to configure the interrupt priority by modifying the configuration item `CONFIG_ESP_TIMER_INTERRUPT_LEVEL <https://docs.espressif.com/projects/esp-idf/en/v4.4/esp32/api-reference/kconfig.html#config-esp-timer-interrupt-level>`__ in Menuconfig.
  - The General Purpose Timer allows setting interrupt priority when registering the interrupt service function. For details, please refer to the API description of `timer_isr_callback_add <https://docs.espressif.com/projects/esp-idf/en/v4.4/esp32/api-reference/peripherals/timer.html#_CPPv422timer_isr_callback_add13timer_group_t11timer_idx_t11timer_isr_tPvi>`__.

--------------

How to improve the timeliness of interrupt response in gptimer?
---------------------------------------------------------------

  Put the interrupt function and the corresponding callback into the IRAM.
