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
----------------------------------------------------------------------------------------------------------

  - Please refer to `ESP8266 Technical Reference Manual <https://www.espressif.com/sites/default/files/documentation/esp8266-technical_reference_en.pdf>`_ regarding the related APIs.
  - If you are using NonOS SDK, please refer to `ESP8266 Non-OS SDK API Reference <https://www.espressif.com/sites/default/files/documentation/2c-esp8266_non_os_sdk_api_reference_en.pdf>`_.
  - Generally, when using hardware interrupts, you should finish executions as soon as possible and put the callback function into IRAM to avoid the potential impacts of Cache.

    - For RTOS SDK, IRAM_ATTR should be added to the function.
    - For NonOS SDK, ICACHE_FLASH_ATTR should not be added before the function.

-----------------------------------------------------------------------------------------------------

How to set interrupt priority for timers?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - esp_timer is implemented based on task, so interrupt priority cannot be configured.
  - timer_group can have interrupt priority by modifying the last parameter of the `timer_isr_callback_add <https://docs.espressif.com/projects/esp-idf/en/v4.4/esp32/api-reference/peripherals/timer.html#_CPPv422timer_isr_callback_add13timer_group_t11timer_idx_t11timer_isr_tPvi>`_ interface.