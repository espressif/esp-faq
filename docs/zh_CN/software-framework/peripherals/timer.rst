定时器
============

:link_to_translation:`en:[English]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

--------------

ESP8266 使⽤ HW 定时器中断有哪些注意事项？
-------------------------------------------------------

  - 可以参考相关 API 文档 `《ESP8266 技术参考手册》 <https://www.espressif.com/sites/default/files/documentation/esp8266-technical_reference_cn.pdf>`_。
  - 如果使用 NonOS SDK，可参考 `《ESP8266 Non-OS SDK API 参考》 <https://www.espressif.com/sites/default/files/documentation/2c-esp8266_non_os_sdk_api_reference_cn.pdf>`_。
  - 通常情况下，硬件中断回调函数需要尽快执行结束，并且将回调函数放入 IRAM 中，避免 Cache 关闭的影响。

    - RTOS SDK 需要在函数名前添加链接器属性 IRAM_ATTR。
    - NonOS SDK 不能在函数名前添加 ICACHE_FLASH_ATTR（该属性指定函数放在 flash 中）。

-----------------------------------------------------------------------------------------------------

定时器如何设置中断优先级呢？
-----------------------------------------------------------------------------------------------------

  - esp_timer 以 ESP32 为例，可以通过在 Menuconfig 中修改配置项 `CONFIG_ESP_TIMER_INTERRUPT_LEVEL <https://docs.espressif.com/projects/esp-idf/zh_CN/v4.4/esp32/api-reference/kconfig.html#config-esp-timer-interrupt-level>`_ 来配置中断优先级。
  - General-Purpose Timer 可以在注册中断服务函数时设置中断优先级，具体请参考 `timer_isr_callback_add <https://docs.espressif.com/projects/esp-idf/zh_CN/v4.4/esp32/api-reference/peripherals/timer.html#_CPPv422timer_isr_callback_add13timer_group_t11timer_idx_t11timer_isr_tPvi>`_ 的 API 说明。

--------------

如何提高 gptimer 中断响应的及时性？
---------------------------------------------------------------

  可以将中断函数与相应的 callback 放入到 IRAM 中。