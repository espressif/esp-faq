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

使用 ESP-ADF 下的 VOIP 功能，通过手机和 ESP32 设备进行通话时，如何消除回音？
----------------------------------------------------------------------------

  - 从软件层面来讲， AEC (Acoustic Echo Cancelation) 对系统性能要求较高，而当前芯片性能无法满足，不支持通过软件实时 AEC。因此 VOIP 目前没有 AEC 的软件解决方案。

  - 建议使用支持 AEC 的 DSP 芯片来消除回音。

--------------

使用 ESP32-Korvo-DU1906 开发板必须用百度云吗？
----------------------------------------------

  - ESP32-Korvo-DU1906 开发板例程只限于使用百度云进行测试，并且需要 Profile， Profile 的获取需要联系百度获取。
  - 与其他服务器通信（亚马逊、图灵等等）理论上是可以实现的，当前未有相关测试用例。

--------------

乐鑫官网给出的网络电话例程是否支持 RTP？
----------------------------------------

  支持。

  - 现在我们用的网络电话协议是 `VoIP <https://www.espressif.com/zh-hans/news/ESP32_VoIP>`__\ ，媒体协议是RTP。
  - 可使用 `Espressif 官方例程 <https://github.com/espressif/esp-adf/tree/master/examples/advanced_examples/voip>`__。

--------------

ESP-ADF 中 RTP 协议是否开源？
----------------------------------------

  - 目前 RTP 协议未开源，是以 lib 形式供外部调用。

--------------

ESP-ADF 例程能否实现蓝牙耳机的音量调节功能？（如 pipeline_a2dp_sink_and_hfp，pipeline_a2dp_sink_stream，pipeline_bt_sink）
------------------------------------------------------------------------------------------------------------------------------

  - 目前 ADF 还不支持 AVRCP 的调音操作，IDF release/v4.0 及以上已经支持了，您可以用 IDF 中 a2dp_sink 的 demo， 和 a2dp_source 对跑看下。
  - 后续会在 ADF 的 Demo 中直接支持

--------------

我想在ESP32-LyraT的i2c接一个传感器使用，请问有如何读取i2c设备数据的例程吗？
-----------------------------------------------------------------------------

  烦请参考 `demo <https://github.com/espressif/esp-idf/tree/722043f734fa556d66d57473ac266fb1d0ec5ad2/examples/peripherals/i2c>`_

--------------

如何输出 32bit 的 i2s 音频数据?
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

请问用 ESP-ADF 和 idf4.1 编译 example/get-started/play-pm3 的时间总是报错: ``fatal error: audio_type_def.h: No such file or directory``?
------------------------------------------------------------------------------------------------------------------------------------------

  - 文件 audio_type_def.h 位于 ESP-ADF 的 esp-adf-libs 中。如果在编译过程中找不到该文件，则说明 ESP-ADF v2.0 可能未被正确检测出。特别是子模块可能尚未更新。
  - 要正确检测 ESP-ADF v2.0，请按照所述的步骤进行操作： `更新至一个稳定发布版本 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/versions.html#id7>`_
  - 尝试执行以下命令并重复编译。

.. code:: bash

  cd $ADF_PATH
  git fetch
  git checkout v2.0
  git submodule update --init --recursive 

--------------

请问官方有没有可以支持 IDF v4.1 的 ESP-ADF 版本?
-------------------------------------------------

  `ESP-ADF Release v2.0 <https://github.com/espressif/esp-adf/releases/tag/v2.0>`_ 支持 ESP-IDF v3.3.2, v4.0 和 v4.1。

--------------

加入DuerOS是否会将esp32-lyrat开发板的录音功能全程占用？
----------------------------------------------------------

  目前的设计是全程占用录音数据。但是你可以通过把 ``I2S_stream`` 的 ``multi_output`` 功能 enable, 让录音的数据通过这个通道输出到你想要的地方。

--------------

ESP32-LyraT V4.3 不支持 dueros 吗，烧进去 dueros 固件，机器一直重启？
-----------------------------------------------------------------------

  设置ram为64M或是设置为自动就行了。
  ``Component config -> ESP32 Specific -> SPI RAM config -> Type of SPIRAM in use->select ESP-PSRAM64``

--------------

ESP-ADF 支持语音识别关键词自定义开发吗？
----------------------------------------

  暂时语音训练接口还没有开放出来，大家可以直接使用 “嗨 乐鑫” ，这个唤醒词是 Free 的，如果目前大家有定制需求，可以发送邮件至 Sales@espressif.com 咨询。

--------------

使用 ESP32-LyraTD-MSC V2.1 开发板跑 Alexa 例程，把固件下载到开发板中，重启后板子没有反应，无法配置 Wi-Fi 等后续操作？ ADF 例程是否支持 ESP32-LyraTD-MSC 类型的开发板？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Alexa 你需要使用 https://github.com/espressif/esp-avs-sdk/releases/download/v1.0b1r3/esp-prov-v2.apk 进行配网
  - ADF 已经支持 ESP32-LyraTD-MSC ，先将 ``ADF git submodule update`` ，后可以直接使用 demo 编译

--------------

ESP32 关于语音识别方面,要能本地化,能否推荐相应的开发板?
----------------------------------------------------------------------------

  - `ESP-Skainet <https://github.com/espressif/esp-skainet>`_ 是乐鑫推出的智能语音助手，目前支持唤醒词识别和命令词识别。
  - 要运行 ESP-Skainet，您需要有一个集成了音频输入模块的 ESP32 开发板。 在示例中，我们使用 ESP32-LyraT-Mini 或 ESP32-Korvo V1.1。

---------------

ESP32 是否有同时支持 MIC 和 AUX 拾音的开发板？
------------------------------------------------------------------------------

  - ESP32-lyraT-4.3 开发板支持 MIC 和 AUX 拾音。ESP32-lyraT4.3 开发板说明`参见 <https://docs.espressif.com/projects/esp-adf/zh_CN/latest/get-started/get-started-esp32-lyrat.html#esp32-lyrat-v4-3>`__。
