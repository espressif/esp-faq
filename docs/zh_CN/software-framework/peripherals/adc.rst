模拟数字转换器 (ADC)
=======================

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

ESP8266 ADC 的分辨率如何？
-------------------------------------------------

  - ESP8266 ADC 为 10 位，理论分辨率为 2 :sup:`10` = 1024。
  - ESP8266 连接路由器后，单 STA 模式会进⼊ Modem-sleep 模式，导致芯⽚内部参考值变化，因此 ADC 测量得数据变化。
  - 如果想要测量精确，可以在关闭 Wi-Fi 后，使用 ``system_adc_fast_read`` 函数读取。

--------------

ESP8266 如何获取 ADC 寄存器位图信息？
---------------------------------------------------------

  由于 ESP8266 ADC 是和内部 RF 电路⾼度集成的，所以位图和寄存器信息没有公开，如有特殊需求请联系 sales@espressif.com。

--------------

ESP32 ADC 有⼏个通道？采样率和有效位数是多少？
---------------------------------------------------------

  - ESP32 的 ADC 共有 18 个通道。
  - 在停⽌ Wi-Fi 的情况且使用 ADC DMA 的情况下，采样率理论不超过 2 MHz。但实际建议使用更小的采样率。
  - 在 Wi-Fi 正常⼯作的情况下，能达到每秒 1000 次。
  - ADC 内部有效位数为 12 位。

--------------

使用 ESP8266 调用 ``adc_read_fast()`` API 会导致 Wi-Fi 断连吗？
---------------------------------------------------------------------------------

  - 调用 ``adc_read_fast()`` API 前需要将 Wi-Fi 和中断关闭，可参见此 API 的 `使用说明 <https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/api-reference/peripherals/adc.html?highlight=adc_read#_CPPv413adc_read_fastP8uint16_t8uint16_t>`_。
  - 由于 ``adc_read_fast()`` API 会进行连续采集，ADC 内部与 Wi-Fi RF 存在耦合部分，无法在 Wi-Fi 开启的状态下调用该函数。
  - 在 Wi-Fi 开启的时候请使用 ``adc_read()`` API 进行 ADC 采集。为保证数据稳定，需要使用 ``esp_wifi_set_ps(WIFI_PS_NONE)`` 函数关闭 Wi-Fi Modem-sleep 休眠模式。

.. note::

    ADC 采样率：在停⽌ Wi-Fi 的情况下，能达到每秒 100000 次。Wi-Fi 正常⼯作的情况下，能达到每秒 1000 次。

----------------

悬空 ADC 引脚，打印出 VDD3P3 的值为 65535，那么 VDD3P3 的电压就是 65535/1024 ≈ 63 V。这个电压值不符，是什么原因？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ADC 输入范围需要大于 0 V 小于 3.3 V（不同型号芯片上限不同），悬空测量为未定义状态。

----------------

ESP32 ADC 的输入电阻是多少？
---------------------------------------------------------

  ADC 是电容性的，可以认为电阻很大。

----------------

使用 ESP32 的 ADC 来检测电源电压，是否需要进行分压？
-------------------------------------------------------------------------------------

  ESP32 的 ADC 参考电压为 1100 mV，可以通过配置内部衰减来增大 ADC 量程，量程范围可参考芯片手册 `ADC 章节 <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`__ 如量程无法满足需求，可使用外部分压电路。

--------------

ESP32 芯片 ADC DMA 模式最高支持多大的采样频率？
-------------------------------------------------------------------------------------------------------------------------------------------

  理论最高支持 2 MHz 的采样频率。

---------------------

使用 ESP32，在 ``esp_wifi_start()`` 和 ``esp_wifi_stop()`` 之间读取 ``adc2_get_raw()`` 操作失败，是什么原因？
----------------------------------------------------------------------------------------------------------------------------------------------

  由于 Wi-Fi 也需要使用 ADC2， 且 Wi-Fi 具有更高的访问优先级。因此，在 Wi-Fi 工作期间，应用程序使用 ``adc2_get_raw()`` 可能读取失败，建议检测该函数的返回值, 失败后重新进行一次测量。

---------------

ESP32 是否支持 ADC2 与蓝牙同时使用？
---------------------------------------------------------

  支持。

------------------

ESP32-S2 芯片 ADC DMA 模式支持的采样率范围是多大？
-----------------------------------------------------------------------------------------------------------------

  频率限制：611 Hz ~ 83333 Hz。

----------------------

ESP32 的 ADC 支持多通道同时采样吗？
----------------------------------------------------------------------------------------------------------------------

  ESP32 的 ADC 不支持多通道同时采样，若使用 ADC 多通道采样，需采取轮询采样的方式来实现。

----------------

使用 ESP32-WROVER-B 模组，ESP-IDF 为 release/v4.2 版本，当 GPIO 设置为 ADC 接口后，在不进行硬件重启的情况下，再将 GPIO 设置为其他 IO 模式且其他 IO 模式不生效后，此 GPIO 无反应，请问如何释放对应的 GPIO 模式？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 请不要将 ADC 接口设置为只输入的 GPIO。
  - 结束 ADC 接口模式时，请使用 `adc_digi_stop() <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.4/esp32/api-reference/peripherals/adc.html#_CPPv413adc_digi_stopv>`__ 关闭 ADC。

-------------

ESP32 芯片的 ADC 之间的测量误差是多大？
----------------------------------------------------------------------------------------------

  默认情况下，ESP32 芯片 ADC 之间的测量差异是 ±6%，可参考 `《ESP32 技术规格书》 <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf>`_。

-------------

ESP32 能同时用两个 ADC 通道来测量不同的数据吗？比如电流和电压？
-----------------------------------------------------------------------------------------------

  使用一个 ADC 无法做到同一时刻读取多个 ADC 通道的值，可以依次轮询读取两个 ADC 通道的数据。

-------------

ESP32-S3 ADC 配置为 ``ADC_ATTEN_DB_12`` 时，为何测量电压无法达到标称 3100 mV？
-----------------------------------------------------------------------------------------------

  ESP32-S3 ADC1 或 ADC2 配置为 ``ADC_ATTEN_DB_12`` 时，测量电压范围为 ``0 ~ 3100 mV``，但部分芯片最大电压测量值小于 ``3100 mV``，可使用以下两种方法来解决这个问题：

- 方案 1：避开使用边界电压值，可通过外部分压电路将输入电压维持在中间电压值附近，以获得更高的精度和一致性。
- 方案 2：使用软件 `ADC 扩展量程方案 <https://docs.espressif.com/projects/espressif-esp-iot-solution/zh_CN/latest/others/adc_range.html>`_ ，将最大测量电压扩展到 ``3300 mV``。

--------------

我们可以使用 GPIO0 作为 ADC 管脚，同时将 ESP32 作为 Wi-Fi 热点吗？
-----------------------------------------------------------------------------------------------------------------------------------------

   - 当使用 Wi-Fi 时，ESP32 ADC2 管脚不能同时使用。 因此，如果您在使用 Wi-Fi 时无法从 ADC2 GPIO 获取值，您可以考虑改用 ADC1 GPIO，这应该可以解决您的问题。有关详细信息，请参阅 `ADC 连续模式的硬件限制 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/adc_continuous.html>`__ 和 `ADC Oneshot 模式的硬件限制 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/adc_oneshot.html>`__。
   - GPIO0、GPIO2、GPIO5、GPIO12 (MTDI) 和 GPIO15 (MTDO) 是 strapping 管脚。 将 GPIO0 用于其他功能时，需要注意上电时的 GPIO 电平。 如果上电时 GPIO0 为低电平，则很容易进入下载模式。 有关更多信息，请参阅 `ESP32 技术规格书 <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf>`__。

---------------

使用 ESP32-S3 的 GPIO19 和 GPIO20 基于 `"esp-idf/examples/peripherals/adc/oneshot_read" <https://github.com/espressif/esp-idf/tree/release/v5.0/examples/peripherals/adc/oneshot_read>`_ 例程测试 ADC2 功能，ADC2 衰减参数设置为 11 dB，当输入电压为 0.6 V 时，测试结果却为 1.1 V 和 2.8 V，是什么原因？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 建议检查是否两个 ADC2 通道都进行了 `adc_oneshot_config_channel() <https://github.com/espressif/esp-idf/blob/886e98a2c1311556eb6be02775d49703d6050222/examples/peripherals/adc/oneshot_read/main/oneshot_read_main.c#L90>`_ 的配置。

---------------

ESP32 在同一个 ADC 控制器下，能同时支持部分 ADC 通道是 DMA 模式，部分 ADC 通道是 one shot 模式吗？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP32 ADC 使用 DMA 模式，要求使用 esp-idf v5.0 及以上版本的 SDK。
  - ESP32 的 ADC2 不支持 DMA 模式。
  - 在同一个 ADC 控制器下，不支持部分 ADC 通道为 DMA 模式，部分 ADC 通道为 oneshot 模式。请参考 `ESP32 ADC hardware-limitations <https://docs.espressif.com/projects/esp-idf/en/v5.1.1/esp32/api-reference/peripherals/adc_continuous.html#hardware-limitations>`_ 说明。
  - 在软件上，建议使用 `adc_continuous_config_t <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v5.0/esp32/api-reference/peripherals/adc_continuous.html#_CPPv423adc_continuous_config_t>`_ 将 ADC1 设置为 DMA 通道; 使用 `adc_oneshot_config_channel <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v5.0/esp32/api-reference/peripherals/adc_oneshot.html?highlight=adc_oneshot_config_channel#_CPPv426adc_oneshot_config_channel25adc_oneshot_unit_handle_t13adc_channel_tPK22adc_oneshot_chan_cfg_t>`_ 将 ADC2 设置为 oneshot 通道。

------------

使用 ESP-IDF v5.1 基于 ESP32-S3-WROOM-1 模组测试 ADC2，当 GPIO12 输入 3.3 V 电压时，读出的电压为 5 V，为什么？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: c

    I (455346) EXAMPLE: ADC2 Channel[1] Raw Data: 4095
    I (455346) EXAMPLE: ADC2 Channel[1] Cali Voltage: 4985 mV
    I (456346) EXAMPLE: ADC2 Channel[1] Raw Data: 4095
    I (456346) EXAMPLE: ADC2 Channel[1] Cali Voltage: 4985 mV

  - ADC Raw Data 读数正常，ADC 转换值变成 5 V 是因为 ESP32-S3 ADC 有效测量范围是 2900 mV，参见 `ESP32-S3 ADC 衰减等级对应有效测量范围 <https://docs.espressif.com/projects/esp-hardware-design-guidelines/zh_CN/latest/esp32s3/schematic-checklist.html#adc>`_。
  - 超过 2900 mV 的输入电压是未定义的输入电压，因此会出现这种情况。如果要测量大于 2900 mV 的输入电压建议分压或采用 `ESP32-S3 ADC 扩展量程方案 <https://docs.espressif.com/projects/espressif-esp-iot-solution/zh_CN/latest/others/adc_range.html#esp32-s3-adc>`_。

ADC 的参考基准源能否从外部加？如果可以加，应该加在哪个引脚？ADC 的内部基准电压是多少？
------------------------------------------------------------------------------------------------------------------------------------------------------

  - 不支持外部参考电压，只能使用内部参考电压。
  - 内部基准电压 1.1 V。
