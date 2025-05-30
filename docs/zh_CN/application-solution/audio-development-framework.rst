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

使用 ESP-ADF 的 VoIP 功能时，手机和 ESP32 设备进行通话如何消除回音？
-----------------------------------------------------------------------

  - 乐鑫提供基于 ESP32、ESP32-S3 芯片的回声消除 (Acoustic Echo Cancelation, AEC) 算法，可以参考 `算法例程 <https://github.com/espressif/esp-adf/tree/master/examples/advanced_examples/algorithm>`_。
  - 需要注意，AEC 的效果不仅仅依赖于软件参数配置和调试，还依赖于硬件设计，例如播放不能失真、录音不能有杂音以及回升参考信号没有问题等等，此部分推荐参考乐鑫 `ESP32-Lyrat-Mini 开发板 <https://espressif-docs.readthedocs-hosted.com/projects/esp-adf/zh_CN/latest/design-guide/dev-boards/get-started-esp32-lyrat-mini.html>`_ 以及 `ESP32-S3-Korvo-2 开发板 <https://espressif-docs.readthedocs-hosted.com/projects/esp-adf/zh_CN/latest/design-guide/dev-boards/user-guide-esp32-s3-korvo-2.html>`_ 的设计。

--------------

有接入百度语音或大模型的参考例程吗？
----------------------------------------------

  请参考 `dueros 例程 <https://github.com/espressif/esp-adf/tree/master/examples/dueros>`_。

--------------

乐鑫官网提供的网络电话例程是否支持 RTP？
----------------------------------------

  - ESP-ADF 当前默认提供的网络电话协议是基于 SIP 实现的 VoIP，协议部分有用到 RTP。
  - 可使用 Espressif SDK ESP-ADF 下的 `VoIP 例程 <https://github.com/espressif/esp-adf/tree/master/examples/protocols/voip>`_。

--------------

ESP-ADF 中 SIP 协议是否开源？
----------------------------------------

  目前协议未开源，以 lib 形式供外部调用。

--------------

ESP-ADF 例程能否实现蓝牙耳机的音量调节功能？
---------------------------------------------------

  可以参考例程：`pipeline_bt_sink <https://github.com/espressif/esp-adf/tree/master/examples/player/pipeline_bt_sink>`_

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

  请参考 `ESP-ADF 下支持的 ESP-IDF 版本 <https://github.com/espressif/esp-adf/blob/master/README.md#idf-version>`__。

--------------

加入 DuerOS 是否会将 ESP32-LyraT 开发板的录音功能全程占用？
--------------------------------------------------------------------------------------------------------

  目前的设计是全程占用录音数据。但是您可以通过使能 ``I2S_stream`` 的 ``multi_output`` 功能，让录音的数据通过这个通道输出到想要的地方。

--------------

ESP-ADF 支持语音识别唤醒词自定义开发吗？
----------------------------------------

  暂时还未开放语音训练接口，您可以直接使用免费唤醒词 “嗨，乐鑫”。如果您有定制需求，可以发送邮件至 sales@espressif.com 咨询。

--------------

ESP-ADF 是否支持 ESP32-LyraTD-MSC v2.1 开发板跑 Alexa 例程？
---------------------------------------------------------------------

  - ESP-ADF 中还没有直接支持 Alexa 的例程。对于 Alexa 例程，请参考 `esp-va-sdk <https://github.com/espressif/esp-avs-sdk>`_。
  - 需要注意的是，从 2024 年下半年开始，Alexa 已关闭了主机侧（Build-in）语音接口。如果后续需要接入 Alexa 语音生态，可以尝试使用 ACK 方案或 Matter 方案。

--------------

ESP32 关于语音识别方面，要实现本地化，能否推荐相应的开发板？
----------------------------------------------------------------------------

  推荐使用 `ESP32-Lyrat-Mini 开发板 <https://espressif-docs.readthedocs-hosted.com/projects/esp-adf/zh_CN/latest/design-guide/dev-boards/get-started-esp32-lyrat-mini.html>`_ 或者 `ESP32-S3-Korvo-2 开发板 <https://espressif-docs.readthedocs-hosted.com/projects/esp-adf/zh_CN/latest/design-guide/dev-boards/user-guide-esp32-s3-korvo-2.html>`_ 来实现本地化。

---------------

ESP32 是否有同时支持 MIC 和 AUX 拾音的开发板？
------------------------------------------------------------------------------

  `ESP32-lyraT-4.3 开发板 <https://docs.espressif.com/projects/esp-adf/zh_CN/latest/design-guide/dev-boards/get-started-esp32-lyrat.html>`__ 支持 MIC 和 AUX 拾音。

---------------

如何利用 ESP32-LyraT 开发板实现通话功能？
-------------------------------------------------------

  可参考语音通话例程 `VoIP <https://github.com/espressif/esp-adf/tree/master/examples/protocols/voip>`__。

---------------

ESP32 系列音频开发板支持多大功率的扬声器？
------------------------------------------------------------------

  - ESP32 开发板默认使用 NS4150 的 PA，一般不超过 3 W 大小。
  - 如果有另外需求，可以更换 PA 设计。

---------------

乐鑫的语音唤醒方案对环境噪声是否有一定的要求？
------------------------------------------------------------------------

  当前乐鑫的语音方案可以满足信噪比 5 dB 以内的环境要求，对于一些固定的噪音场景还可以做到 0 dB 以内（需要针对实际产品进行优化）。

---------------------

ESP32 的 AI 开发板上有 AUX 输入，MIC 就无法拾音了吗？
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

  - 硬件上 MCLK 只能使用 GPIO0、GPIO1、GPIO3 管脚，不可使用其他管脚，可阅读 `《ESP32 技术规格书》 <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf>`__ 的 IO_MUX 表内的 CLK_OUT*，默认使用 GPIO0。
  - 可参考 `ESP32-LyraT-Mini 开发板的硬件原理图 <https://dl.espressif.com/dl/schematics/SCH_ESP32-LYRAT-MINI_V1.2_20190605.pdf>`_ 设计。
  - 管脚分配可参见 `ESP32-LyraT-Mini V1.2 Hardware Reference <https://docs.espressif.com/projects/esp-adf/zh_CN/latest/design-guide/board-esp32-lyrat-mini-v1.2.html>`_。

----------------

ESP32-WROVER-E 模组使用一路 I2S 是否可实现同时播音和录音？
--------------------------------------------------------------------------------------------------------------------------------------------------

  使用一路 I2S 可以实现同时播音和录音。可以参考 `ESP32-LyraT 开发板入门指南 <https://docs.espressif.com/projects/esp-adf/zh_CN/latest/design-guide/dev-boards/get-started-esp32-lyrat.html>`_。

----------------

乐鑫模块是否支持 Spotify Connect？
--------------------------------------------------------------------------------------------------

  :CHIP\: ESP32 | ESP32-S2 | ESP32-S3 :

 当前不支持，建议考虑使用 dlna，可以达到类似的效果。

----------------

ESP32-Korvo-DU1906 开发板运行 `korvo_du1906 <https://github.com/espressif/esp-adf/tree/master/examples/korvo_du1906>`_ 例程重启，错误提示如下：Guru Meditation Error: Core  0 panic'ed (IllegalInstruction). Exception was unhandled，如何解决？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 建议检查供电。
  - 为整个系统提供电源。建议使用至少 5 V/2 A 电源适配器供电，保证供电稳定。

----------------

ESP-DSP fft 可以运行 4096、8192 以及更多采样吗？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  可以，最大支持到 32 K 采样。最大值可以在 menuconfig 中配置，以 `fft demo <https://github.com/espressif/esp-dsp/tree/master/examples/fft>`_ 为例，配置步骤为 ``idf.py menuconfig`` > ``Component config`` > ``DSP Library`` > ``Maximum FFT length`` > ``(*)32768``。

---------------

ESP32 如何连接麦克风？
------------------------------

  - 如果连接数字麦克风，可以连接 I2S 外设。
  - 如果连接模拟麦克风，可以连接 ADC 外设。
  - 考虑到录音质量，更建议使用外扩 AD。

--------------

ESP32 是否支持模拟音频或是数字音频输出？
-----------------------------------------------------

  - ESP32 支持 DAC 模拟音频输出，可以使用它播放提示音等简单音频。
  - ESP32 支持 PWM 模拟音频输出，相比 DAC 效果稍好，演示代码：`esp-iot-solution <https://github.com/espressif/esp-iot-solution/tree/master/examples/audio/wav_player>`__。
  - ESP32 同时支持 I2S 数字音频输出，I2S 可配置引脚可以查看 `《ESP32 技术规格书》 <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf>`_ 外设接口和传感器章节。

----------------

ESP32 芯片支持哪些音频格式？
-------------------------------------------------------------------------------

  ESP32 支持的音频格式有 MP3、AAC、FLAC、WAV、OGG、OPUS、AMR、G.711 等，可参考 `ESP-ADF <https://github.com/espressif/esp-adf>`_ SDK 下的说明。

---------------

如何使用 ESP32 芯片解码压缩音频?
---------------------------------------------------------------------------------------

  使用 ESP32 芯片解码压缩音频的应用可参考 `esp-adf/examples/recorder <https://github.com/espressif/esp-adf/tree/c50f3dc43bd754568d0f52dbc111b543f0baa5cd/examples/recorder>`_ 文件夹中的例程。

---------------

`ESP-LED-Strip <https://www.espressif.com/zh-hans/news/ESP-LEDStrip>`_ 对应的代码示例在哪?
---------------------------------------------------------------------------------------------------------------------------------------------------------

  对应的代码示例存放在 ESP-ADF 中，请参考 `led_pixels 例程 <https://github.com/espressif/esp-adf/tree/master/examples/display/led_pixels>`_。

------------

ESP32 是否支持在线语音识别？
----------------------------------------------------------------------------------------------------

  支持。可参考例程 `esp-adf/examples/dueros <https://github.com/espressif/esp-adf/blob/master/examples/dueros/README_CN.md>`_。

-------------

ESP32 能否实现蓝牙耳机的音量调节功能？
---------------------------------------------------------------------------------------------------------------

  可以。ESP32 使用的是蓝牙的 AVRCP 调音协议，可基于 `pipeline_a2dp_sink_stream <https://github.com/espressif/esp-adf/tree/master/examples/player/pipeline_a2dp_sink_stream>`_ 例程测试。

---------------

Wi-Fi 和 FFT 可以同时使用吗？
-----------------------------------------------------------------------------------------------------------------

  Wi-Fi 和 FFT 可同时使用。例如，可以在包含 FFT 功能的 `律动灯示例 <https://github.com/espressif/esp-adf/tree/master/examples/display/led_pixels>`__ 上直接添加 Wi-Fi 功能。

-----------------

在 ESP-ADF SDK 中，RECORD_HARDWARE_AEC 宏为 True 或 False 的含义是什么？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  RECORD_HARDWARE_AEC 宏为 True 还是 False 表示开发板否具备硬件 AEC（回声消除）电路。如果为 True，表示开发板具备硬件 AEC 电路，如果为 False，表示开发板不具备硬件 AEC 电路。

---------------

想基于乐鑫的产品开发一个室外纯语音对讲机的方案，是否有推荐的产品型号和应用参考？
---------------------------------------------------------------------------------------------------------------------------------------------------------------

  纯语音对讲机方案推荐使用 `ESP32-S3 <https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_cn.pdf>`_ 系列的产品进行开发，应用软件可参考 `esp-adf/examples/protocols/voip <https://github.com/espressif/esp-adf/tree/master/examples/protocols/voip>`__ 例程。

-------------

ESP-ADF 音频应用开发框架中，软件 AEC（Acoustic Echo Cancelation，回声消除）与硬件 AEC 有什么区别？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  硬件 AEC 与 软件 AEC 的区别在于参考信号的来源。若参考信号来自于非主控芯片（比如 ES8311、ES7210），则是硬件 AEC；若由主控设备自行复制出参考信号进行回声消除，则是软件 AEC。
