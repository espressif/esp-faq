Audio Application Framework
===========================

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

When using the VoIP feature of ESP-ADF, how to eliminate echo during calls between a mobile phone and an ESP32 device?
----------------------------------------------------------------------------------------------------------------------------------

  - Espressif provides an Acoustic Echo Cancelation (AEC) algorithm based on ESP32 and ESP32-S3 chips. For details, please refer to the `algorithm examples <https://github.com/espressif/esp-adf/tree/master/examples/advanced_examples/algorithm>`_.
  - Note that the effect of AEC not only depends on software parameter configuration and debugging, but also on hardware design, such as distortion-free playback, noise-free recording, and problem-free echo reference signal, etc. For this part, it is recommended to refer to the Espressif's design on the `ESP32-Lyrat-Mini development board <https://espressif-docs.readthedocs-hosted.com/projects/esp-adf/en/latest/design-guide/dev-boards/get-started-esp32-lyrat-mini.html>`_ and `ESP32-S3-Korvo-2 development board <https://espressif-docs.readthedocs-hosted.com/projects/esp-adf/en/latest/design-guide/dev-boards/user-guide-esp32-s3-korvo-2.html>`_.

--------------

Does the use of the ESP32-Korvo-DU1906 development board require the use of Baidu Cloud?
--------------------------------------------------------------------------------------------

  - The ESP32-Korvo-DU1906 development board example is only for testing with Baidu Cloud, and a Profile is required.
  - Please contact Baidu Cloud to check the relevant business access terms, see `Preparation for using voice services <https://cloud.baidu.com/doc/SHC/s/wk7bl9g8i>`_.

--------------

Does the official VoIP example provided by Espressif support RTP?
---------------------------------------------------------------------------------------------------

  - In ESP-ADF, the default VoIP provided is based on SIP, and the protocol utilizes RTP.
  - You can use the `VoIP example <https://github.com/espressif/esp-adf/tree/master/examples/protocols/voip>`_ under Espressif SDK ESP-ADF.

--------------

Is the SIP protocol in ESP-ADF open-source?
----------------------------------------------

  The protocol is currently not open-source and is provided for external calls in the form of a library.

--------------

Can ESP-ADF examples implement the volume adjustment function of Bluetooth headsets?
-------------------------------------------------------------------------------------------------

  Such as: pipeline_a2dp_sink_and_hfp, pipeline_a2dp_sink_stream, pipeline_bt_sink

  - Currently, ESP-ADF does not support AVRCP's tuning operation. ESP-IDF release/v4.0 and later releases have already supported this function. You can try to use the `a2dp_sink example <https://github.com/espressif/esp-idf/tree/v4.4.2/examples/bluetooth/bluedroid/classic_bt/a2dp_sink>`_ and `a2dp_source example <https://github.com/espressif/esp-idf/tree/v4.4.2/examples/bluetooth/bluedroid/classic_bt/a2dp_source>`_ in ESP-IDF.
  - The function will be directly supported in the ADF examples in the future.

--------------

I want to use a sensor on the I2C of ESP32-LyraT. Is there an example on how to read I2C device data?
------------------------------------------------------------------------------------------------------------------

  Please refer to the `i2c example <https://github.com/espressif/esp-idf/tree/722043f734fa556d66d57473ac266fb1d0ec5ad2/examples/peripherals/i2c>`_.

--------------

How to output 32-bit I2S audio data?
-------------------------------------

  Rewrite a my_i2s_write function to call i2s_write_expand, then replace the write function of the i2s_stream element with my_i2s_write in the form of audio_element_set_write_cb.

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

Why do I always get an error when compiling example/get-started/play-mp3 with ESP-ADF and ESP-IDF v4.1?
--------------------------------------------------------------------------------------------------------

  Error log: ``fatal error: audio_type_def.h: No such file or directory``

  - The file audio_type_def.h is located in the esp-adf-libs of ESP-ADF. If this file cannot be found during the compilation process, it indicates that ESP-ADF v2.4 may not have been correctly detected, especially the submodules may not have been updated.
  - To detect ESP-ADF v2.4, please follow the steps described in `Updating to Stable Release <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/versions.html#updating-to-stable-release>`_.
  - Try executing the following commands and recompile.

  .. code:: shell

    cd $ADF_PATH
    git fetch
    git checkout v2.4
    git submodule update --init --recursive

--------------

Is there an official version of ESP-ADF that supports ESP-IDF v4.4?
--------------------------------------------------------------------

  `ESP-ADF Release v2.4 <https://github.com/espressif/esp-adf/releases/tag/v2.4>`_ supports ESP-IDF v3.3, v4.1, v4.2, V4.3, and v4.4.

--------------

Will integrating DuerOS occupy the recording function of the ESP32-LyraT development board throughout the process?
-------------------------------------------------------------------------------------------------------------------

  The current design occupies the recording data throughout the process. However, you can enable the ``multi_output`` function of ``I2S_stream`` to output the recording data to the desired location through this channel.

--------------

Does ESP-ADF support the development of custom voice recognition keywords?
---------------------------------------------------------------------------

  The voice training interface has not yet been opened. You can directly use the free wake-up word "Hi, Espressif". If you have customization requirements, please email sales@espressif.com for details.

--------------

Does ESP-ADF support running Alexa examples on the ESP32-LyraTD-MSC v2.1 development board?
--------------------------------------------------------------------------------------------------------

  ESP-ADF does not directly support Alexa examples. For Alexa examples, please refer to `esp-va-sdk <https://github.com/espressif/esp-avs-sdk>`_.

--------------

Regarding voice recognition on ESP32, can you recommend a suitable development board for localization?
--------------------------------------------------------------------------------------------------------------------------

  We recommend using the `ESP32-Lyrat-Mini development board <https://espressif-docs.readthedocs-hosted.com/projects/esp-adf/en/latest/design-guide/dev-boards/get-started-esp32-lyrat-mini.html>`_ or the `ESP32-S3-Korvo-2 development board <https://espressif-docs.readthedocs-hosted.com/projects/esp-adf/en/latest/design-guide/dev-boards/user-guide-esp32-s3-korvo-2.html>`_ for localization.

---------------

Does ESP32 have a development board that supports both MIC and AUX pickup?
---------------------------------------------------------------------------

  The `ESP32-lyraT-4.3 development board <https://docs.espressif.com/projects/esp-adf/en/latest/design-guide/dev-boards/get-started-esp32-lyrat.html>`__ supports both MIC and AUX pickup.

---------------

How to implement call function using the ESP32-LyraT development board?
------------------------------------------------------------------------------------------

  Please refer to the voice call example `VoIP <https://github.com/espressif/esp-adf/tree/master/examples/advanced_examples/voip>`__.

---------------

What is the maximum power of supported speakers for ESP32 series audio development board?
------------------------------------------------------------------------------------------------

  - ESP32 development board uses NS4150 PA by default, and its maximum power is 3 W.
  - You may change the PA design according to needs.

---------------

Does Espressif's voice wake-up solution have specific requirements regarding environmental noise?
-------------------------------------------------------------------------------------------------------------------------------

  The current Espressif voice solution can meet the environmental requirements of a signal-to-noise ratio of less than 5 dB. For some fixed noise scenarios, it can even be less than 0 dB (need to be optimized for the actual product).

---------------------

If there is an AUX input on the ESP32's AI development board, can the MIC still be used to pick up sound?
--------------------------------------------------------------------------------------------------------------------------

  - The ESP-ADF development framework can choose various ways to pick up sound, including MIC input and Line-in.
  - The pickup method selection is as follows:

  .. code-block:: text

    typedef enum {
      AUDIO_HAL_CODEC_MODE_ENCODE = 1, /*! <select adc */      // MIC pickup
      AUDIO_HAL_CODEC_MODE_DECODE, /*! <select dac*/
      AUDIO_HAL_CODEC_MODE_BOTH, /*! <select both adc and dac */   //  MIC + speaker
      AUDIO_HAL_CODEC_MODE_LINE_IN, /*! <set adc channel */,             // microphone pickup
    } Audio_hal_codec_mode_t;

  - The pickup method configuration is as follows:

  .. code-block:: text

    audio_board_handle_t board_handle = audio_board_init();
    audio_hal_ctrl_codec(board_handle->audio_hal, AUDIO_HAL_CODEC_MODE_DECODE, AUDIO_HAL_CTRL_START);     //If you want to pick up sound with MIC, modify this configuration option.

---------------------

When designing an audio development board with the ESP32-WROVER-B module and ES8311, which pins can be selected for the MCLK clock?
----------------------------------------------------------------------------------------------------------------------------------------------

  - On the hardware side, MCLK can only use GPIO0, GPIO1, GPIO3 pins. You can check the IO_MUX table in the `ESP32 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`__, where GPIO0 is used by default.
  - You can refer to the design of the `schematic of ESP32-LyraT-Mini <https://dl.espressif.com/dl/schematics/SCH_ESP32-LYRAT-MINI_V1.2_20190605.pdf>`_.
  - For allocation of pins, please refer to `ESP32-LyraT-Mini V1.2 Hardware Reference <https://docs.espressif.com/projects/esp-adf/en/latest/design-guide/board-esp32-lyrat-mini-v1.2.html>`_.

----------------

Can the ESP32-WROVER-E module use a single I2S to realize simultaneous playback and recording?
-----------------------------------------------------------------------------------------------

  Yes. You can refer to the `ESP32-LyraT getting started guide <https://docs.espressif.com/projects/esp-adf/en/latest/design-guide/dev-boards/get-started-esp32-lyrat.html>`_.

----------------

Do Espressif modules support Spotify Connect?
---------------------------------------------------

  :CHIP\: ESP32 | ESP32-S2 | ESP32-S3 :

 Not supported yet. It is recommended to consider using dlna, which can achieve a similar effect.

----------------

When running the `korvo_du1906 <https://github.com/espressif/esp-adf/tree/master/examples/korvo_du1906>`_ example on an ESP32-Korvo-DU1906 board, a reboot caused the following error message: Guru Meditation Error: Core  0 panic'ed (IllegalInstruction). Exception was unhandled. How to resolve such issue?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Please check the power supply.
  - Provide power to the entire system. It is recommended to use at least a 5 V/2 A power adapter to ensure stable power supply.

----------------

Can ESP-DSP fft run 4096, 8192, and more samples?
-------------------------------------------------

  Yes, it supports up to 32 K samples. The maximum value can be configured in menuconfig. For example, in the `fft demo <https://github.com/espressif/esp-dsp/tree/master/examples/fft>`_, the configuration steps are ``idf.py menuconfig`` > ``Component config`` > ``DSP Library`` > ``Maximum FFT length`` > ``(*)32768``.

---------------

How to connect a microphone to ESP32?
--------------------------------------

  - You can connect I2S peripheral if it is a digital microphone.
  - You can connect ADC peripheral if it is an analog microphone.

--------------

Does ESP32 support analog audio or digital audio output?
---------------------------------------------------------

  - ESP32 supports DAC analog audio output, which can be used to play simple audio such as prompt tones.
  - ESP32 supports PWM analog audio output, which is slightly better than DAC. Demonstration code: `esp-iot-solution <https://github.com/espressif/esp-iot-solution/tree/master/examples/audio/wav_player>`__.
  - ESP32 also supports I2S digital audio output. For I2S configurable pins, please refer to `ESP32 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_ > Chapter Peripherals and Sensors.

----------------

What audio formats does the ESP32 chip support?
------------------------------------------------

  ESP32 supports audio formats such as MP3, AAC, FLAC, WAV, OGG, OPUS, AMR, G.711, etc. For more information, please refer to the instructions under `ESP-ADF <https://github.com/espressif/esp-adf>`_ SDK.

---------------

How to use the ESP32 chip to decode compressed audio?
------------------------------------------------------

  For applications using the ESP32 chip to decode compressed audio, refer to the examples in the `esp-adf/examples/recorder <https://github.com/espressif/esp-adf/tree/c50f3dc43bd754568d0f52dbc111b543f0baa5cd/examples/recorder>`_ folder.

---------------

Where is the code example for `ESP-LED-Strip <https://www.espressif.com/en/news/ESP-LEDStrip>`_?
-------------------------------------------------------------------------------------------------

  The corresponding code examples are stored in ESP-ADF. Please refer to the `led_pixels example <https://github.com/espressif/esp-adf/tree/master/examples/display/led_pixels>`_.

------------

Does ESP32 support online voice recognition?
---------------------------------------------

  Yes, it does. Please refer to the `esp-adf/examples/dueros <https://github.com/espressif/esp-adf/blob/master/examples/dueros/README.md>`_ example.

-------------

Does ESP32 support volume adjustment of Bluetooth headphones?
---------------------------------------------------------------------------------------------------------------

  - Yes. ESP32 uses the Bluetooth AVRCP tuning protocol. You can test the function with the `esp-adf/examples/player/pipeline_bt_sink <https://github.com/espressif/esp-adf/tree/master/examples/player/pipeline_bt_sink>`_ example.
