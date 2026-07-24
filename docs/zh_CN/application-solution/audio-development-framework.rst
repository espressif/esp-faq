音频应用框架
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

使用 ESP-ADF 的 VoIP 功能时，如何消除通话回音？
-----------------------------------------------------------------------

  - 乐鑫提供回声消除 (Acoustic Echo Cancellation, AEC) 算法，可参考 `算法例程 <https://github.com/espressif/esp-adf/tree/release/v2.x/examples/advanced_examples/algorithm>`_。新方案推荐使用 `ESP32-S3-Korvo-2 开发板 <https://espressif-docs.readthedocs-hosted.com/projects/esp-adf/zh_CN/latest/design-guide/dev-boards/user-guide-esp32-s3-korvo-2.html>`_。
  - 需要注意，AEC 效果不仅依赖软件参数配置和调试，还依赖硬件设计，例如播放不能失真、录音不能有杂音、回声参考信号正常等。存量设计也可参考 `ESP32-Lyrat-Mini 开发板 <https://espressif-docs.readthedocs-hosted.com/projects/esp-adf/zh_CN/latest/design-guide/dev-boards/get-started-esp32-lyrat-mini.html>`_。

--------------

AEC 或唤醒效果较差时，如何排查硬件问题？
-----------------------------------------------------------------------

  如果遇到 AEC 效果差、唤醒效果差等情况，建议先验证硬件录音与回放链路是否正常：

  - 设备端可烧录 `esp_audio_analyzer_app <https://github.com/espressif/esp-adf/tree/master/adf_examples/checks/esp_audio_analyzer_app>`_ 例程进行采集与自检。
  - 再配合网络分析网页 `ESP Audio Analyzer <https://audio-tools.espressif.com.cn/>`_ 查看频谱、失真、噪声等指标，便于定位硬件问题。

--------------

有接入百度语音或大模型的参考例程吗？
----------------------------------------------

  请参考 `dueros 例程 <https://github.com/espressif/esp-adf/tree/release/v2.x/examples/dueros>`_。

--------------

乐鑫官网提供的网络电话例程是否支持 RTP？
----------------------------------------

  - ESP-ADF 当前默认提供的网络电话协议是基于 SIP 实现的 VoIP，协议部分用到了 RTP。
  - 可使用 ESP-ADF 下的 `VoIP 例程 <https://github.com/espressif/esp-adf/tree/release/v2.x/examples/protocols/voip>`_。

--------------

ESP-ADF 中 SIP 协议是否开源？
----------------------------------------

  目前协议未开源，以 lib 形式供外部调用。

--------------

ESP-ADF 例程能否实现蓝牙耳机的音量调节功能？
---------------------------------------------------

  可以。该功能依赖经典蓝牙的 AVRCP 协议，可参考 `pipeline_bt_sink <https://github.com/espressif/esp-adf/tree/release/v2.x/examples/player/pipeline_bt_sink>`_ 或 `pipeline_a2dp_sink_stream <https://github.com/espressif/esp-adf/tree/release/v2.x/examples/player/pipeline_a2dp_sink_stream>`_ 例程。支持经典蓝牙的芯片（如 ESP32、ESP32-S31）可使用该方案。

--------------

我想在 ESP32-LyraT 的 I2C 接一个传感器使用，请问有如何读取 I2C 设备数据的例程吗？
---------------------------------------------------------------------------------------------------------------------------

  请参考 `i2c 例程 <https://github.com/espressif/esp-idf/tree/722043f734fa556d66d57473ac266fb1d0ec5ad2/examples/peripherals/i2c>`_。

--------------

如何输出 32 位的 I2S 音频数据？
---------------------------------

  参考以下代码即可：

  .. code:: c

    i2s_stream_cfg_t i2s_writer_cfg = I2S_STREAM_CFG_DEFAULT();
    i2s_writer_cfg.type = AUDIO_STREAM_WRITER;
    i2s_writer_cfg.stack_in_ext = true;
    i2s_writer_cfg.task_core = 1;
    i2s_writer_cfg.need_expand = true;
    i2s_writer_cfg.expand_src_bits = 16;
    i2s_writer = i2s_stream_init(&i2s_writer_cfg);

--------------

请问为何用 ESP-ADF 和 ESP-IDF v4.1 编译 example/get-started/play-mp3 时总是报错？
------------------------------------------------------------------------------------

  错误日志：``fatal error: audio_type_def.h: No such file or directory``

  - 文件 audio_type_def.h 位于 ESP-ADF 的 esp-adf-libs 中。如果在编译过程中找不到该文件，则说明 ESP-ADF v2.4 可能未被正确检测出，特别是子模块可能尚未更新。
  - 要正确检测 ESP-ADF v2.4，请按照 `更新至一个稳定发布版本 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/versions.html#id10>`_ 中所述的步骤进行操作。
  - 尝试执行以下命令并重复编译。

    .. code:: shell

      cd $ADF_PATH
      git fetch
      git checkout v2.4
      git submodule update --init --recursive

--------------

请问在哪里可以查看 ESP-ADF 版本支持的 ESP-IDF 版本情况？
---------------------------------------------------------------------

  请参考 `ESP-ADF 下支持的 ESP-IDF 版本 <https://github.com/espressif/esp-adf/blob/release/v2.x/README.md#idf-version>`__。

--------------

加入 DuerOS 是否会将开发板的录音功能全程占用？
--------------------------------------------------------------------------------------------------------

  目前的设计是全程占用录音数据。但是您可以通过使能 ``I2S_stream`` 的 ``multi_output`` 功能，让录音的数据通过这个通道输出到想要的地方。

--------------

ESP-ADF 支持语音识别唤醒词自定义开发吗？
----------------------------------------

  暂时还未开放语音训练接口，您可以直接使用免费唤醒词“嗨，乐鑫”。涉及唤醒等语音方案，推荐优先选用 ESP32-S3 系列开发板（如 Korvo-2）。如果您有定制需求，可以发送邮件至 sales@espressif.com 咨询。

--------------

ESP-ADF 是否支持 ESP32-LyraTD-MSC v2.1 开发板跑 Alexa 例程？
---------------------------------------------------------------------

  - ESP-ADF 中还没有直接支持 Alexa 的例程。对于 Alexa 例程，请参考 `esp-va-sdk <https://github.com/espressif/esp-avs-sdk>`_。
  - 需要注意的是，从 2024 年下半年开始，Alexa 已关闭了主机侧（Built-in）语音接口。如果后续需要接入 Alexa 语音生态，可以尝试使用 ACK 方案或 Matter 方案。

--------------

要实现本地语音识别，能否推荐相应的开发板？
----------------------------------------------------------------------------

  推荐优先使用 `ESP32-S3-Korvo-2 开发板 <https://espressif-docs.readthedocs-hosted.com/projects/esp-adf/zh_CN/latest/design-guide/dev-boards/user-guide-esp32-s3-korvo-2.html>`_；也可参考 `ESP32-Lyrat-Mini 开发板 <https://espressif-docs.readthedocs-hosted.com/projects/esp-adf/zh_CN/latest/design-guide/dev-boards/get-started-esp32-lyrat-mini.html>`_。

---------------

是否有同时支持 MIC 和 AUX 拾音的开发板？
------------------------------------------------------------------------------

  `ESP32-lyraT-4.3 开发板 <https://docs.espressif.com/projects/esp-adf/zh_CN/latest/design-guide/dev-boards/get-started-esp32-lyrat.html>`__ 支持 MIC 和 AUX 拾音。

---------------

如何利用 ESP-ADF 实现通话功能？
-------------------------------------------------------

  可参考语音通话例程 `VoIP <https://github.com/espressif/esp-adf/tree/release/v2.x/examples/protocols/voip>`__。新方案推荐使用 ESP32-S3 系列开发板。

---------------

乐鑫音频开发板支持多大功率的扬声器？
------------------------------------------------------------------

  - 开发板默认使用 NS4150 的 PA，一般不超过 3 W。
  - 如有其他需求，可以更换 PA 设计。

---------------

乐鑫的语音唤醒方案对环境噪声是否有一定的要求？
------------------------------------------------------------------------

  当前乐鑫的语音方案可以满足信噪比 5 dB 以内的环境要求，对于一些固定的噪音场景还可以做到 0 dB 以内（需要针对实际产品进行优化）。

---------------------

开发板上有 AUX 输入，MIC 就无法拾音了吗？
----------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP-ADF 开发框架可以选择多种方式拾音，有 MIC 输入和 Line-in。
  - 拾音方式选择如下：

    .. code-block:: text

      typedef enum {
        AUDIO_HAL_CODEC_MODE_ENCODE = 1, /*! <select adc */      // MIC pickup
        AUDIO_HAL_CODEC_MODE_DECODE, /*! <select dac*/
        AUDIO_HAL_CODEC_MODE_BOTH, /*! <select both adc and dac */   //  MIC + speaker
        AUDIO_HAL_CODEC_MODE_LINE_IN, /*! <set adc channel */,             // microphone pickup
      } Audio_hal_codec_mode_t;

  - 拾音方式配置如下：

    .. code-block:: text

      audio_board_handle_t board_handle = audio_board_init();
      audio_hal_ctrl_codec(board_handle->audio_hal, AUDIO_HAL_CODEC_MODE_DECODE, AUDIO_HAL_CTRL_START);     //若要 MIC 拾音，修改这个配置选项。

---------------------

使用 ESP32-WROVER-B 模组 + ES8311 设计音频开发板，MCLK 时钟可选择哪些管脚？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 在经典 ESP32 上，MCLK 仅支持 GPIO0、GPIO1、GPIO3，默认推荐 GPIO0。详见 `《ESP32 技术规格书》 <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf>`__ 中 IO_MUX 表的 CLK_OUT* 说明。
  - 可参考 `ESP32-LyraT-Mini 开发板的硬件原理图 <https://dl.espressif.com/dl/schematics/SCH_ESP32-LYRAT-MINI_V1.2_20190605.pdf>`_ 设计。
  - 管脚分配可参见 `ESP32-LyraT-Mini V1.2 Hardware Reference <https://docs.espressif.com/projects/esp-adf/zh_CN/latest/design-guide/board-esp32-lyrat-mini-v1.2.html>`_。

----------------

使用一路 I2S 是否可实现同时播音和录音？
--------------------------------------------------------------------------------------------------------------------------------------------------

  使用一路 I2S 可以实现同时播音和录音。可以参考 `ESP32-LyraT 开发板入门指南 <https://docs.espressif.com/projects/esp-adf/zh_CN/latest/design-guide/dev-boards/get-started-esp32-lyrat.html>`_。

----------------

乐鑫模块是否支持 Spotify Connect？
--------------------------------------------------------------------------------------------------

  如有需要，可联系 sales@espressif.com 咨询。

----------------

ESP-DSP fft 可以运行 4096、8192 以及更多采样吗？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  可以，最大支持到 32 K 采样。最大值可以在 menuconfig 中配置，以 `fft demo <https://github.com/espressif/esp-dsp/tree/master/examples/fft>`_ 为例，配置步骤为 ``idf.py menuconfig`` > ``Component config`` > ``DSP Library`` > ``Maximum FFT length`` > ``(*)32768``。

---------------

如何连接麦克风？
------------------------------

  - 如果连接数字麦克风，可以连接 I2S 外设。
  - 如果连接模拟麦克风，部分芯片可连接 ADC 外设；考虑到录音质量，更建议使用外扩 ADC/codec。

--------------

是否支持模拟音频或是数字音频输出？
-----------------------------------------------------

  - 部分芯片（如经典 ESP32）支持 DAC、PWM 模拟音频输出，可用于播放提示音等简单音频。PWM 演示代码：`esp-iot-solution <https://github.com/espressif/esp-iot-solution/tree/master/examples/audio/wav_player>`__。
  - 推荐使用 I2S 数字音频输出对接外部 codec，具体管脚请参考对应的芯片技术规格书。

----------------

ESP-ADF 支持哪些音频格式？
-------------------------------------------------------------------------------

  支持的音频格式有 MP3、AAC、FLAC、WAV、OGG、OPUS、AMR、G.711 等，可参考 `ESP-ADF <https://github.com/espressif/esp-adf>`_ SDK 下的说明。

---------------

如何解码压缩音频？
---------------------------------------------------------------------------------------

  可参考 `esp-adf/examples/player <https://github.com/espressif/esp-adf/tree/release/v2.x/examples/player>`_ 文件夹中的例程。

---------------

`ESP-LED-Strip <https://www.espressif.com/zh-hans/news/ESP-LEDStrip>`_ 对应的代码示例在哪?
---------------------------------------------------------------------------------------------------------------------------------------------------------

  对应的代码示例存放在 ESP-ADF 中，请参考 `led_pixels 例程 <https://github.com/espressif/esp-adf/tree/release/v2.x/examples/display/led_pixels>`_。

------------

是否支持在线语音识别？
----------------------------------------------------------------------------------------------------

  支持。可参考例程 `esp-adf/examples/dueros <https://github.com/espressif/esp-adf/blob/release/v2.x/examples/dueros/README_CN.md>`_。涉及唤醒等语音交互时，推荐优先选用 ESP32-S3 系列。

-------------

Wi-Fi 和 FFT 可以同时使用吗？
-----------------------------------------------------------------------------------------------------------------

  Wi-Fi 和 FFT 可同时使用。例如，可以在包含 FFT 功能的 `律动灯示例 <https://github.com/espressif/esp-adf/tree/release/v2.x/examples/display/led_pixels>`__ 上直接添加 Wi-Fi 功能。

-----------------

在 ESP-ADF SDK 中，``RECORD_HARDWARE_AEC`` 宏为 True 或 False 的含义是什么？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ``RECORD_HARDWARE_AEC`` 宏为 True 或 False，表示开发板是否具备硬件 AEC（回声消除）电路。True 表示具备，False 表示不具备。

---------------

想基于乐鑫的产品开发一个室外纯语音对讲机的方案，是否有推荐的产品型号和应用参考？
---------------------------------------------------------------------------------------------------------------------------------------------------------------

  纯语音对讲机方案推荐使用 `ESP32-S3 <https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_cn.pdf>`_ 系列的产品进行开发，应用软件可参考 `esp-adf/examples/protocols/voip <https://github.com/espressif/esp-adf/tree/release/v2.x/examples/protocols/voip>`__ 例程。

-------------

ESP-ADF 音频应用开发框架中，软件 AEC（Acoustic Echo Cancellation，回声消除）与硬件 AEC 有什么区别？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  硬件 AEC 与软件 AEC 的区别在于参考信号的来源。若参考信号来自于非主控芯片（比如 ES8311、ES7210），则是硬件 AEC；若由主控设备自行复制出参考信号进行回声消除，则是软件 AEC。

--------------

是否支持语音活动检测 (Voice Activity Detection, VAD)？
----------------------------------------------------------------------------------------------------------------------------------

  支持。

  - 多数产品可通过软件算法配合 I2S/PDM 麦克风输入实现语音活动检测。详情请参考 `esp-sr/include/esp32c5/esp_vad.h <https://github.com/espressif/esp-sr/blob/master/include/esp32c5/esp_vad.h>`__。
  - 部分产品（如 ESP32-P4）内置硬件 VAD 单元，可以通过配置 LP I2S 和 VAD 驱动来检测语音活动状态。详情请参考 `esp-sr/include/esp32p4/esp_vad.h <https://github.com/espressif/esp-sr/blob/master/include/esp32p4/esp_vad.h>`__。
  - 有关更多产品对 VAD 的支持，请在 `esp-sr/include <https://github.com/espressif/esp-sr/blob/master/include>`__ 下查找。
