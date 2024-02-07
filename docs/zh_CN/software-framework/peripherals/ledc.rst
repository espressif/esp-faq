LED PWM 控制器 (LEDC)
=========================

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

ESP8266 PWM 频率范围是多少呢？
----------------------------------------------------

  ESP8266 PWM 是软件模拟的，受定时器限制 CLK 最大为 1 M。推荐频率为 1 K，也可以通过降低占空比分辨率的方式提高频率。

--------------

ESP32 GPIO 管脚输出 PWM 存在限制吗？是否可以分配至任意一个 I/O 上？
------------------------------------------------------------------------------------------------------------------------------------------

  - ESP32 PWM 可通过 IO Matrix 切换至任意 GPIO 输出。除了只有输⼊功能的 I/O（例如：GPIO34 ～ GPIO39）之外，理论上 PWM 可以输出到任何管脚。
  - 实际使用中仍会受到模组与芯片限制、模组未引出管脚或 flash 占用等情况影响。

--------------

ESP8266 NonOS SDK PWM 的变化缓慢，有哪些原因？
--------------------------------------------------------------

  - 如果使用 SDK example/IOT_demo 中的渐变 API，如 ``light_set_aim`` 或 ``light_set_aim_r`` 这些 API，需要渐变的过程。
  - 若需要 PWM Duty 设置后⽴即⽣效，则可以调⽤接⼝ ``pwm_set_duty``，需要注意调⽤ ``pwm_set_duty`` 后要调⽤ ``pwm_start`` 此次设置才能⽣效。

--------------

ESP32 LEDC 递减渐变，Duty 值溢出错误，如何解决？
--------------------------------------------------------------

  使⽤ LEDC 的过程中，应避免以下三个条件同时成⽴：

  - LEDC 启动递减渐变功能；
  - LEDC 渐变过程中 Scale 寄存器设置为 1；
  - LEDC 递减渐变开始时刻或者过程中的某⼀时刻，Duty 值为 2 :sup:`LEDC_HSTIMERx_DUTY_RES` 或 2 :sup:`LEDC_LSTIMERx_DUTY_RES`。

---------------------

ESP8266 通过直接写硬件定时器 FRC1 的寄存器产⽣ PWM，发现初始化 Wi-Fi 时，Wi-Fi 产⽣的中断会⼲扰硬件定时器的中断，导致错误的 PWM 输出，是否可以使⽤ FRC2 产⽣ PWM？是否可以使 FRC1 的优先级⾼于 Wi-Fi？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  不可以使⽤ FRC2，其被系统占⽤。Wi-Fi 使⽤ NMI 中断，其优先级⾼于其他普通中断，推荐使⽤ ESP8266 RTOS SDK 的 PWM 库，参考 `ESP8266_RTOS_SDK/examples/peripherals/pwm <https://github.com/espressif/ESP8266_RTOS_SDK/tree/release/v3.4/examples/peripherals/pwm>`_。

----------------

使用 v3.3.3 版本 ESP-IDF 在 ESP32 设备上测试 ledc 例程，当启用了 auto light sleep，LED PWM 无输出；但不启用 auto light sleep，LED PWM 有输出。ESP-IDF 编程指南里关于 `LED PWM <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/peripherals/ledc.html?highlight=pwm#id1>`_  的说明表示 LED PWM 在 Sleep 模式下是能工作的，请问是什么原因？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  esp-idf v3.3.3 版本的 SDK 不支持 LED PWM 在 Sleep 模式下工作。请使用新版的 esp-idf（v4.0 以上版本）下的 LEDC 例程来测试，例如 esp-idf release/v4.2 版本的 SDK，且需要将 LED PWM 时钟源改为内部 RTC8M 时钟源。如下：

  .. code-block:: c

      ledc_timer_config_t ledc_timer = {
            .duty_resolution = LEDC_TIMER_13_BIT,
            .freq_hz = 5000,
            .speed_mode = LEDC_LOW_SPEED_MODE,
            .timer_num = LEDC_TIMER_0,
            .clk_cfg = LEDC_USE_RTC8M_CLK,
        };

--------------

ESP32 PWM 支持两路死区互补输出吗？
--------------------------------------------------------------

  - LEDC 不支持，MCPWM 外设支持两路死区互补输出。
  - 实测 ESP32-S3 可以通过 MCPWM 产生频率 10 k、占空比精度 1 us、死区精度 100 ns 的互补输出波形。

LEDC 支不支持硬件伽马调光？
--------------------------------------------------------------

  支持宏 ``SOC_LEDC_GAMMA_CURVE_FADE_SUPPORTED`` 的芯片可以开启硬件伽马调光，通过调用 ``ledc_fill_multi_fade_param_list`` 和 ``ledc_set_multi_fade_and_start`` 来实现