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

ESP-ADF 使用 VOIP 功能，手机和 ESP32 设备进行通话如何消除回音？
----------------------------------------------------------------------

  - 从软件层面来讲，回声消除 (Acoustic Echo Cancelation, AEC) 对系统性能要求较高，而当前芯片性能无法支持通过软件实时 AEC。因此，VOIP 目前没有 AEC 的软件解决方案。
  - 建议使用支持 AEC 的 DSP 芯片来消除回音。

--------------

使用 ESP32-Korvo-DU1906 开发板必须用百度云吗？
----------------------------------------------

  - ESP32-Korvo-DU1906 开发板例程只限于使用百度云进行测试，并且需要 Profile。请联系百度获取 Profile。
  - 与其他服务器通信（亚马逊、图灵等等）理论上是可以实现的，但当前未有相关测试用例。

--------------

乐鑫官网给出的网络电话例程是否支持 RTP？
----------------------------------------

  - 当前网络电话协议是 `VoIP <https://www.espressif.com/zh-hans/news/ESP32_VoIP>`_，媒体协议是 RTP。
  - 可使用 Espressif SDK ESP-ADF 下的 `VOIP 例程 <https://github.com/espressif/esp-adf/tree/master/examples/advanced_examples/voip>`_。

--------------

ESP-ADF 中 RTP 协议是否开源？
----------------------------------------

  - 目前 RTP 协议未开源，是以 lib 形式供外部调用。

--------------

ESP-ADF 例程能否实现蓝牙耳机的音量调节功能？
---------------------------------------------------

  如：pipeline_a2dp_sink_and_hfp, pipeline_a2dp_sink_stream, pipeline_bt_sink

  - 目前 ESP-ADF 还不支持 AVRCP 的调音操作，IDF release/v4.0 及以上已经支持了，您可以尝试使用 ESP-IDF 中 a2dp_sink 的 Demo 和 a2dp_source 对跑。
  - 后续会在 ADF 的 Demo 中直接支持。

--------------

我想在 ESP32-LyraT 的 I2C 接一个传感器使用，请问有如何读取 I2C 设备数据的例程吗？
---------------------------------------------------------------------------------------------------------------------------

  请参考 `Demo <https://github.com/espressif/esp-idf/tree/722043f734fa556d66d57473ac266fb1d0ec5ad2/examples/peripherals/i2c>`_。

--------------

如何输出 32bit 的 I2S 音频数据？
---------------------------------

  - 重新写一个 my_i2s_write 函数调用 i2s_write_expand, 然后把 my_i2s_write 用 ``audio_element_set_write_cb`` 修改 i2s_stream element 的 write 函数。

  .. code:: c

    int my_i2s_write(audio_element_handle_t self, char *buffer, int len, TickType_t ticks_to_wait, void *context)
    {
      i2s_stream_t *i2s = (i2s_stream_t *)audio_element_getdata(self);
      size_t bytes_written = 0;
      i2s_write_expand(i2s->config.i2s_port, buffer, len, 16, 32, &bytes_written, ticks_to_wait);
      return bytes_written;
    }

      i2s_stream_cfg_t i2s_writer = I2S_STREAM_CFG_DEFAULT();
      i2s_writer.type = AUDIO_STREAM_WRITER;
      i2s_writer.stack_in_ext = true;
      i2s_writer.i2s_config.sample_rate = 48000;
      i2s_writer.i2s_config.mode = I2S_MODE_MASTER | I2S_MODE_TX;
      i2s_writer.i2s_config.bits_per_sample = 32; //for cupid digital loopback
      audio_element_handle_t my_i2s = i2s_stream_init(&i2s_writer);
      audio_element_set_write_cb(my_i2s, my_i2s_write, NULL);

--------------

请问为何用 ESP-ADF 和 ESP-IDF v4.1 编译 example/get-started/play-pm3 时总是报错？
------------------------------------------------------------------------------------

  错误日志：``fatal error: audio_type_def.h: No such file or directory``

  - 文件 audio_type_def.h 位于 ESP-ADF 的 esp-adf-libs 中。如果在编译过程中找不到该文件，则说明 ESP-ADF v2.4 可能未被正确检测出。特别是子模块可能尚未更新。
  - 要正确检测 ESP-ADF v2.4，请按照所述的步骤进行操作：`更新至一个稳定发布版本 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/versions.html#id7>`_。
  - 尝试执行以下命令并重复编译。

  .. code:: shell

    cd $ADF_PATH
    git fetch
    git checkout v2.4
    git submodule update --init --recursive 

--------------

请问官方有没有可以支持 ESP-IDF v4.4 的 ESP-ADF 版本？
---------------------------------------------------------------------

  `ESP-ADF Release v2.4 <https://github.com/espressif/esp-adf/releases/tag/v2.4>`_ 支持 ESP-IDF v3.3，v4.1，v4.2，V4.3 和 v4.4。

--------------

加入 DuerOS 是否会将 esp32-lyrat 开发板的录音功能全程占用？
--------------------------------------------------------------------------------------------------------

  目前的设计是全程占用录音数据。但是您可以通过使能 ``I2S_stream`` 的 ``multi_output`` 功能, 让录音的数据通过这个通道输出到想要的地方。

--------------

ESP32-LyraT V4.3 不支持 dueros 吗？烧进去 dueros 固件，机器一直重启？
-----------------------------------------------------------------------

  - 设置 ram 为 64 M 或是自动 ``Component config -> ESP32 Specific -> SPI RAM config -> Type of SPIRAM in use->select ESP-PSRAM64``。

--------------

ESP-ADF 支持语音识别关键词自定义开发吗？
----------------------------------------

  暂时还未开放语音训练接口，您可以直接使用免费唤醒词 “嗨 乐鑫”。如果目前您有定制需求，可以发送邮件至 Sales@espressif.com 咨询。

--------------

ESP-ADF 是否支持 ESP32-LyraTD-MSC V2.1 开发板跑 Alexa 例程？
---------------------------------------------------------------------

  - 对于 Alexa 例程，请使用 `esp-prov-v2 <https://github.com/espressif/esp-avs-sdk/releases/download/v1.0b1r3/esp-prov-v2.apk>`_ 进行配网。
  - ESP-ADF 已经支持 ESP32-LyraTD-MSC，将 ``ADF git submodule update`` 后可以直接使用 Demo 编译。

--------------

ESP32 关于语音识别方面，要能本地化，能否推荐相应的开发板？
----------------------------------------------------------------------------

  - `ESP-Skainet <https://github.com/espressif/esp-skainet>`_ 是乐鑫推出的智能语音助手，目前支持唤醒词识别和命令词识别。
  - 要运行 ESP-Skainet，您需要有一个集成了音频输入模块的 ESP32 开发板。在示例中，我们使用 ESP32-LyraT-Mini 或 ESP32-Korvo V1.1。

---------------

ESP32 是否有同时支持 MIC 和 AUX 拾音的开发板？
------------------------------------------------------------------------------

  - ESP32-lyraT-4.3 开发板支持 MIC 和 AUX 拾音。开发板说明参见 `esp32-lyrat-v4-3 <https://docs.espressif.com/projects/esp-adf/zh_CN/latest/get-started/get-started-esp32-lyrat.html#esp32-lyrat-v4-3>`__。

---------------

如何利用 ESP32-LyraT 开发板实现通话功能？
-------------------------------------------------------

  - 可参考语音通话例程 `voip <https://github.com/espressif/esp-adf/tree/master/examples/advanced_examples/voip>`__。

---------------

ESP32 系列音频开发板支持多大功率的扬声器？
------------------------------------------------------------------

  - ESP32 开发板默认使用 NS4150 的 PA，其 datasheet 提到功率不超过 3 W。

---------------

Alexa solution 对环境噪声是否有一定的要求？
------------------------------------------------------------------------

  - 当前乐鑫的语音方案可以满足信噪比 5 dB 以内的环境要求，对于一些固定的噪音场景还可以做到 0 dB 以内（需要针对实际产品进行优化）。

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

  - 使用一路 I2S 可以实现同时播音和录音。可以参考 `ESP32-LyraT 开发板 <https://docs.espressif.com/projects/esp-adf/zh_CN/latest/get-started/get-started-esp32-lyrat.html#esp32-lyrat-v4-3>`_。

----------------

乐鑫模块是否支持 Spotify Connect？
--------------------------------------------------------------------------------------------------

  :CHIP\: ESP32 | ESP32-S2 | ESP32-S3 :

 - 当前不支持，建议考虑使用 dlna，会有类似的效果。

----------------

ESP32-Korvo-DU1906 开发板运行 `korvo_du1906 <https://github.com/espressif/esp-adf/tree/master/examples/korvo_du1906>`_ 示例重启，错误提示如下：Guru Meditation Error: Core  0 panic'ed (IllegalInstruction). Exception was unhandled，如何解决？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 建议检查供电。
  - 为整个系统提供电源。建议使用至少 5 V/2 A 电源适配器供电，保证供电稳定。
  
----------------

ESP-DSP fft 可以运行 4096、8192 以及更多采样吗？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 可以，最大支持到 32 K 采样。最大值可以在 menuconfig 中配置，以 `fft demo <https://github.com/espressif/esp-dsp/tree/master/examples/fft>`_ 为例为 ``idf.py menuconfig--->Component config--->DSP Library--->Maximum FFT length--->(*)32768``。

---------------

ESP32 如何连接麦克风？
------------------------------

  - 如果连接数字麦克风，可以连接 I2S 外设。
  - 如果连接模拟麦克风，可以连接 ADC 外设。

--------------

ESP32 是否支持模拟音频或是数字音频输出？
-----------------------------------------------------

  - ESP32 支持 DAC 模拟音频输出，可以使用它播放提示音等简单音频。
  - ESP32 支持 PWM 模拟音频输出，相比 DAC 效果稍好，演示代码：`esp-iot-solution  <https://github.com/espressif/esp-iot-solution/tree/master/examples/audio/wav_player>`__。
  - ESP32 同时支持 I2S 数字音频输出，I2S 可配置引脚可以在 `《ESP32 技术规格书》 <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf>`_ > 外设接口和传感器章节。

----------------

ESP32 芯片支持哪些音频格式？
-------------------------------------------------------------------------------

  ESP32 支持的音频格式有 MP3、AAC、FLAC、WAV、OGG、OPUS、AMR、G.711 等，可参考 `ESP-ADF <https://github.com/espressif/esp-adf#overview>`_ SDK 下的说明。
