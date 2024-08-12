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

  - Please refer to `ESP8266 Technical Reference Manual <https://www.espressif.com/sites/default/files/documentation/esp8266-technical_reference_en.pdf>`_ regarding the related APIs.
  - If you are using NonOS SDK, please refer to `ESP8266 Non-OS SDK API Reference <https://www.espressif.com/sites/default/files/documentation/2c-esp8266_non_os_sdk_api_reference_en.pdf>`_.
  - Typically, the hardware interrupt callback function needs to be executed as quickly as possible, and the callback function should be placed in IRAM to avoid the impact of Cache being turned off.

    - RTOS SDK requires adding the linker attribute IRAM_ATTR before the function name.
    - NonOS SDK cannot add ICACHE_FLASH_ATTR (this attribute specifies the function is placed in flash) before the function name.

-----------------------------------------------------------------------------------------------------

How to set interrupt priority for timers?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The esp_timer, using ESP32 as an example, allows you to configure the interrupt priority by modifying the configuration item `CONFIG_ESP_TIMER_INTERRUPT_LEVEL <https://docs.espressif.com/projects/esp-idf/en/v4.4/esp32/api-reference/kconfig.html#config-esp-timer-interrupt-level>`_ in Menuconfig.
  - The General Purpose Timer allows setting interrupt priority when registering the interrupt service function. For details, please refer to the API description of `timer_isr_callback_add <https://docs.espressif.com/projects/esp-idf/en/v4.4/esp32/api-reference/peripherals/timer.html#_CPPv422timer_isr_callback_add13timer_group_t11timer_idx_t11timer_isr_tPvi>`_.

--------------

How to improve the timeliness of interrupt response in gptimer?
---------------------------------------------------------------

Put the interrupt function and the corresponding callback into the IRAM.
