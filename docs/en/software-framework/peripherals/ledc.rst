LED Control (LEDC)
==================

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

What is the frequency range for ESP8266 PWM?
-----------------------------------------------------------------

  The PWM of ESP8266 is realized via software programming, so the maximum CLK value is 1 M limited by timer. It is recommended to set the frequency to 1 K. The PWM frequency can also be improved by decreasing the resolution of duty cycle.

--------------

Are there any limits on outputting PWM via ESP32 GPIO pins? Can I distribute it to any I/O?
--------------------------------------------------------------------------------------------------------

  - The ESP32 can output PWM using any GPIO via IO Matrix. Theoretically, the PWM can be distributed to any I/O except for those that only have input functions (e.g., GPIO34 ~ GPIO39).
  - In the actual use, this could also be affected by the limitations of chips and modules, the un-pinned I/Os, flash occupations and etc.

--------------

The PWM of ESP8266 NonOS SDK changes slow. What could be the reasons?
---------------------------------------------------------------------------------------------------

  - If you are using the gradient APIs in SDK example/IOT_demo, e.g., ``light_set_aim`` or ``light_set_aim_r``, it will need a gradual process for PWM changes.
  - If you need the PWM Duty to take effect immediately after configuration, please call API ``pwm_set_duty``, and call ``pwm_start`` next to make this configuration take effect.

--------------

When the LEDC is in decremental fade mode, a duty overflow error can occur. How to solve the issue?
----------------------------------------------------------------------------------------------------------------

  When using LEDC, avoid the concurrence of following three cases:

  - The LEDC is in decremental fade mode;
  - The scale register is set to 1;
  - The duty is 2 :sup:`LEDC_HSTIMERx_DUTY_RES` or 2 :sup:`LEDC_LSTIMERx_DUTY_RES`.

-----------------

When using ESP8266 to generate PWM by directly writing to the register of the hardware timer FRC1, I found there are error PWM outputs after Wi-Fi is initialized since it may disturb the interrupt of FRC1. Is it possible to use FRC2 instead to generate PWM? Or is it possible to set FRC1 higher priority than Wi-Fi?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  FRC2 cannot be used as it is occupied by the system. Wi-Fi uses NMI interrupt, which have a higher priority than other ordinary interrupts. It is recommended to use the PWM library of ESP8266_RTOS_SDK. Please refer to `ESP8266_RTOS_SDK/examples/peripherals/pwm <https://github.com/espressif/ESP8266_RTOS_SDK/tree/release/v3.4/examples/peripherals/pwm>`_ example.

-------------------------

I'm using v3.3.3 version of ESP-IDF to test the ledc example on ESP32. The LED PWM outputs when Auto Light Sleep mode is disabled, but does not output when this mode is enabled. According the description of  `LED PWM <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/peripherals/ledc.html?highlight=pwm#id1>`_  in ESP-IDF programming guide, LED PWM should work in sleep modes. What is the reason?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  v3.3.3 does not support LED PWM working in sleep modes. Please use the LEDC example under the new versions of ESP-IDF (v4.0 and later versions) to test, e.g., ESP-IDF release/v4.2 version of the SDK. Plus, it is also necessary to change the LED PWM clock source to the internal RTC_8M clock source. Please see below:

  .. code-block:: c

      ledc_timer_config_t ledc_timer = {
            .duty_resolution = LEDC_TIMER_13_BIT,
            .freq_hz = 5000,
            .speed_mode = LEDC_LOW_SPEED_MODE,
            .timer_num = LEDC_TIMER_0,
            .clk_cfg = LEDC_USE_RTC8M_CLK,
        };

-------------------------

Does ESP32 PWM support complementary outputs with dead bands on two channels?
------------------------------------------------------------------------------------------------------------

  - This feature is not supported by LEDC but by the MCPWM peripheral.
  - By measurement, ESP32-S3 can generate complementary output waveforms with the frequency of 10 k, the duty cycle accuracy of 1 us and the dead band accuracy of 100 ns by MCPWM.

Does LEDC support hardware gamma dimming?
--------------------------------------------------------------

  Chips that support the macro ``SOC_LEDC_GAMMA_CURVE_FADE_SUPPORTED`` can enable hardware gamma dimming by calling ``ledc_fill_multi_fade_param_list`` and ``ledc_set_multi_fade_and_start``.
