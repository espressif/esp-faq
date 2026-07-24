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

When using the VoIP feature of ESP-ADF, how can I eliminate call echo?
-----------------------------------------------------------------------

  - Espressif provides an Acoustic Echo Cancellation (AEC) algorithm. For details, please refer to the `algorithm examples <https://github.com/espressif/esp-adf/tree/release/v2.x/examples/advanced_examples/algorithm>`_. For new designs, the `ESP32-S3-Korvo-2 development board <https://espressif-docs.readthedocs-hosted.com/projects/esp-adf/en/latest/design-guide/dev-boards/user-guide-esp32-s3-korvo-2.html>`_ is recommended.
  - Note that AEC performance depends not only on software parameter configuration and debugging, but also on hardware design, such as distortion-free playback, noise-free recording, and a valid echo reference signal. For existing designs, you can also refer to the `ESP32-Lyrat-Mini development board <https://espressif-docs.readthedocs-hosted.com/projects/esp-adf/en/latest/design-guide/dev-boards/get-started-esp32-lyrat-mini.html>`_.

--------------

How can I troubleshoot hardware issues when AEC or wake-up performance is poor?
------------------------------------------------------------------------------------------

  If AEC or wake-up performance is poor, first verify that the hardware recording and playback path is working correctly:

  - On the device, flash the `esp_audio_analyzer_app <https://github.com/espressif/esp-adf/tree/master/adf_examples/checks/esp_audio_analyzer_app>`_ example for capture and self-check.
  - Then use the web analysis tool `ESP Audio Analyzer <https://audio-tools.espressif.com.cn/>`_ to check spectrum, distortion, noise, and other metrics to help locate hardware issues.

--------------

Is there a reference example for accessing Baidu Speech or large language models?
--------------------------------------------------------------------------------------------

  Please refer to the `dueros example <https://github.com/espressif/esp-adf/tree/release/v2.x/examples/dueros>`_.

--------------

Does the official VoIP example provided by Espressif support RTP?
---------------------------------------------------------------------------------------------------

  - In ESP-ADF, the default VoIP implementation is based on SIP, and the protocol uses RTP.
  - You can use the `VoIP example <https://github.com/espressif/esp-adf/tree/release/v2.x/examples/protocols/voip>`_ under ESP-ADF.

--------------

Is the SIP protocol in ESP-ADF open-source?
----------------------------------------------

  The protocol is currently not open-source and is provided for external use as a library.

--------------

Can ESP-ADF examples implement volume adjustment for Bluetooth headsets?
-------------------------------------------------------------------------------------------------

  Yes. This feature depends on the Classic Bluetooth AVRCP protocol. You can refer to the `pipeline_bt_sink <https://github.com/espressif/esp-adf/tree/release/v2.x/examples/player/pipeline_bt_sink>`_ or `pipeline_a2dp_sink_stream <https://github.com/espressif/esp-adf/tree/release/v2.x/examples/player/pipeline_a2dp_sink_stream>`_ examples. Chips that support Classic Bluetooth (such as ESP32 and ESP32-S31) can use this solution.

--------------

I want to use a sensor on the I2C of ESP32-LyraT. Is there an example on how to read I2C device data?
------------------------------------------------------------------------------------------------------------------

  Please refer to the `i2c example <https://github.com/espressif/esp-idf/tree/722043f734fa556d66d57473ac266fb1d0ec5ad2/examples/peripherals/i2c>`_.

--------------

How to output 32-bit I2S audio data?
-------------------------------------

  Please refer to the following code:

  .. code:: c

    i2s_stream_cfg_t i2s_writer_cfg = I2S_STREAM_CFG_DEFAULT();
    i2s_writer_cfg.type = AUDIO_STREAM_WRITER;
    i2s_writer_cfg.stack_in_ext = true;
    i2s_writer_cfg.task_core = 1;
    i2s_writer_cfg.need_expand = true;
    i2s_writer_cfg.expand_src_bits = 16;
    i2s_writer = i2s_stream_init(&i2s_writer_cfg);

--------------

Why do I always get an error when compiling example/get-started/play-mp3 with ESP-ADF and ESP-IDF v4.1?
--------------------------------------------------------------------------------------------------------

  Error log: ``fatal error: audio_type_def.h: No such file or directory``

  - The file audio_type_def.h is located in the esp-adf-libs of ESP-ADF. If this file cannot be found during the compilation process, it indicates that ESP-ADF v2.4 may not have been correctly detected, especially the submodules may not have been updated.
  - To correctly detect ESP-ADF v2.4, please follow the steps described in `Update to a stable release version <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/versions.html#updating-to-stable-release>`_.
  - Try executing the following commands and recompile.

    .. code:: shell

      cd $ADF_PATH
      git fetch
      git checkout v2.4
      git submodule update --init --recursive

--------------

Where can I check the ESP-IDF version supported by ESP-ADF?
-----------------------------------------------------------------------

  Please refer to the `ESP-IDF versions supported by ESP-ADF <https://github.com/espressif/esp-adf/blob/release/v2.x/README.md#idf-version>`__.

--------------

Will integrating DuerOS occupy the recording function of the development board throughout the process?
-------------------------------------------------------------------------------------------------------------------

  The current design occupies the recording data throughout the process. However, you can enable the ``multi_output`` function of ``I2S_stream`` to output the recording data to the desired location through this channel.

--------------

Does ESP-ADF support customizing voice recognition wake-up words?
---------------------------------------------------------------------------

  The voice training interface has not yet been opened. You can directly use the free wake-up word "Hi, Espressif". For wake-up and other voice solutions, ESP32-S3 series development boards (such as Korvo-2) are recommended. If you have customization requirements, please email sales@espressif.com for details.

--------------

Does ESP-ADF support running Alexa examples on the ESP32-LyraTD-MSC v2.1 development board?
--------------------------------------------------------------------------------------------------------

  - ESP-ADF does not directly support Alexa examples. For Alexa examples, please refer to `esp-va-sdk <https://github.com/espressif/esp-avs-sdk>`_.
  - Please note that since the second half of 2024, Alexa has disabled the host-side (built-in) voice interface. If you need to connect to the Alexa voice ecosystem in the future, you can try using the ACK or Matter solution.

--------------

Please recommend a development board for local voice recognition.
--------------------------------------------------------------------------------------------------------------------------

  The `ESP32-S3-Korvo-2 development board <https://espressif-docs.readthedocs-hosted.com/projects/esp-adf/en/latest/design-guide/dev-boards/user-guide-esp32-s3-korvo-2.html>`_ is recommended first. You can also refer to the `ESP32-Lyrat-Mini development board <https://espressif-docs.readthedocs-hosted.com/projects/esp-adf/en/latest/design-guide/dev-boards/get-started-esp32-lyrat-mini.html>`_.

---------------

Is there a development board that supports both MIC and AUX pickup?
---------------------------------------------------------------------------

  The `ESP32-lyraT-4.3 development board <https://docs.espressif.com/projects/esp-adf/en/latest/design-guide/dev-boards/get-started-esp32-lyrat.html>`__ supports both MIC and AUX pickup.

---------------

How can I implement call functionality with ESP-ADF?
------------------------------------------------------------------------------------------

  You can refer to the VoIP example `VoIP <https://github.com/espressif/esp-adf/tree/release/v2.x/examples/protocols/voip>`__. For new designs, ESP32-S3 series development boards are recommended.

---------------

What speaker power do Espressif audio development boards support?
------------------------------------------------------------------------------------------------

  - Development boards use the NS4150 PA by default, generally up to 3 W.
  - You may change the PA design according to your needs.

---------------

Does Espressif's voice wake-up solution have specific requirements regarding environmental noise?
-------------------------------------------------------------------------------------------------------------------------------

  The current Espressif voice solution can meet the environmental requirements of a signal-to-noise ratio of less than 5 dB. For some fixed noise scenarios, it can even be less than 0 dB (need to be optimized for the actual product).

---------------------

If there is an AUX input on the development board, can the MIC still be used to pick up sound?
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
      audio_hal_ctrl_codec(board_handle->audio_hal, AUDIO_HAL_CODEC_MODE_DECODE, AUDIO_HAL_CTRL_START);   // If you want to pick up sound from the MIC, modify this configuration option.

---------------------

When designing an audio development board with the ESP32-WROVER-B module and ES8311, which pins can be selected for the MCLK clock?
----------------------------------------------------------------------------------------------------------------------------------------------

  - On classic ESP32, MCLK only supports GPIO0, GPIO1, and GPIO3, with GPIO0 recommended by default. See the CLK_OUT* entries in the IO_MUX table of the `ESP32 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`__.
  - You can refer to the design of the `schematic of ESP32-LyraT-Mini <https://dl.espressif.com/dl/schematics/SCH_ESP32-LYRAT-MINI_V1.2_20190605.pdf>`_.
  - For allocation of pins, please refer to `ESP32-LyraT-Mini V1.2 Hardware Reference <https://docs.espressif.com/projects/esp-adf/en/latest/design-guide/board-esp32-lyrat-mini-v1.2.html>`_.

----------------

Can a single I2S interface realize simultaneous playback and recording?
-----------------------------------------------------------------------------------------------

  Yes. You can refer to the `ESP32-LyraT getting started guide <https://docs.espressif.com/projects/esp-adf/en/latest/design-guide/dev-boards/get-started-esp32-lyrat.html>`_.

----------------

Do Espressif modules support Spotify Connect?
---------------------------------------------------

  If needed, please contact sales@espressif.com for details.

----------------

Can ESP-DSP fft run 4096, 8192, and more samples?
-------------------------------------------------

  Yes, it supports up to 32 K samples. The maximum value can be configured in menuconfig. For example, in the `fft demo <https://github.com/espressif/esp-dsp/tree/master/examples/fft>`_, the configuration steps are ``idf.py menuconfig`` > ``Component config`` > ``DSP Library`` > ``Maximum FFT length`` > ``(*)32768``.

---------------

How to connect a microphone?
--------------------------------------

  - For a digital microphone, connect it to the I2S peripheral.
  - For an analog microphone, some chips can use the ADC peripheral; considering recording quality, an external ADC/codec is recommended.

--------------

Is analog or digital audio output supported?
---------------------------------------------------------

  - Some chips (such as classic ESP32) support DAC and PWM analog audio output, which can be used to play simple audio such as prompt tones. PWM demonstration code: `esp-iot-solution <https://github.com/espressif/esp-iot-solution/tree/master/examples/audio/wav_player>`__.
  - I2S digital audio output with an external codec is recommended. For pin details, please refer to the datasheet of the corresponding chip.

----------------

What audio formats does ESP-ADF support?
------------------------------------------------

  Supported audio formats include MP3, AAC, FLAC, WAV, OGG, OPUS, AMR, G.711, and more. For details, please refer to the instructions under the `ESP-ADF <https://github.com/espressif/esp-adf>`_ SDK.

---------------

How to decode compressed audio?
------------------------------------------------------

  Please refer to the examples in the `esp-adf/examples/player <https://github.com/espressif/esp-adf/tree/release/v2.x/examples/player>`_ folder.

---------------

Where is the code example for `ESP-LED-Strip <https://www.espressif.com/en/news/ESP-LEDStrip>`_?
-------------------------------------------------------------------------------------------------

  The corresponding code examples are stored in ESP-ADF. Please refer to the `led_pixels example <https://github.com/espressif/esp-adf/tree/release/v2.x/examples/display/led_pixels>`_.

------------

Is online voice recognition supported?
---------------------------------------------

  Yes. Please refer to the `esp-adf/examples/dueros <https://github.com/espressif/esp-adf/tree/release/v2.x/examples/dueros>`_ example. For wake-up and other voice interaction scenarios, the ESP32-S3 series is recommended.

-------------

Can Wi-Fi and FFT be used simultaneously?
-----------------------------------------------------------------------------------------------------------------

  Wi-Fi and FFT can be used simultaneously. For example, Wi-Fi functionality can be directly added to the `rhythm light example <https://github.com/espressif/esp-adf/tree/release/v2.x/examples/display/led_pixels>`__ with FFT functionality.

-----------------

What does the ``RECORD_HARDWARE_AEC`` macro mean when it is True or False in the ESP-ADF SDK?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The ``RECORD_HARDWARE_AEC`` macro being True or False indicates whether the development board has a hardware AEC (Acoustic Echo Cancellation) circuit. True means it has one; False means it does not.

---------------

Are there any recommended product models and application references for developing an outdoor pure voice intercom solution based on Espressif's products?
---------------------------------------------------------------------------------------------------------------------------------------------------------------

  For pure voice intercom solutions, the `ESP32-S3 <https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf>`_ series is recommended for development. For application software, refer to the `esp-adf/examples/protocols/voip <https://github.com/espressif/esp-adf/tree/release/v2.x/examples/protocols/voip>`__ example.

-------------

What is the difference between software AEC (Acoustic Echo Cancellation) and hardware AEC in the ESP-ADF audio application development framework?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The difference between hardware AEC and software AEC lies in the source of the reference signal. If the reference signal comes from a chip other than the main controller (such as ES8311 or ES7210), it is hardware AEC; if the main controller itself replicates the reference signal for echo cancellation, it is software AEC.

--------------

Is Voice Activity Detection (VAD) supported?
----------------------------------------------------------------------------------------------------------------------------------

  Yes.

  - On most products, VAD can be implemented through software algorithms combined with I2S/PDM microphone input. For details, please refer to `esp-sr/include/esp32c5/esp_vad.h <https://github.com/espressif/esp-sr/blob/master/include/esp32c5/esp_vad.h>`__.
  - Some products (such as ESP32-P4) feature a built-in hardware VAD unit, which can detect voice activity by configuring the LP I2S and VAD drivers. For more details, please refer to `esp-sr/include/esp32p4/esp_vad.h <https://github.com/espressif/esp-sr/blob/master/include/esp32p4/esp_vad.h>`__.
  - For VAD support on other products, please check under `esp-sr/include <https://github.com/espressif/esp-sr/blob/master/include>`__.
