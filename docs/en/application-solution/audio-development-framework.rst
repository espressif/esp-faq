Audio development framework
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

What is the maximum power of supported speakers for ESP32 series audio development board?
--------------------------------------------------------------------------------------------------

  - ESP32 development board uses NS4150 PA by default, and its maximum power is 3 W according to its datasheet.

--------------------

Does Alexa solution have certain requirements for environmental noise?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The current Espressif voice solution can meet the environmental requirements of a signal-to-noise ratio of less than 5dB, and for some fixed noise scenarios, it can also be less than 0dB (need to be optimized for the actual product).

-----------------------

There is an AUX input on the ESP32 AI development board, can MIC be used to pick up the sound?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The ESP-ADF development framework can choose a variety of ways to pick up sound, including MIC input and Line-in.
  - The pick-up method is as follows:

  .. code-block:: text

    typedef enum {
      AUDIO_HAL_CODEC_MODE_ENCODE = 1, /*! <select adc */      // MIC pickup
      AUDIO_HAL_CODEC_MODE_DECODE, /*! <select dac*/
      AUDIO_HAL_CODEC_MODE_BOTH, /*! <select both adc and dac */   //  MIC + speaker
      AUDIO_HAL_CODEC_MODE_LINE_IN, /*! <set adc channel */,             // microphone pickup
    } Audio_hal_codec_mode_t;

  - The configuration of the pickup method is as follows:

  .. code-block:: text

    audio_board_handle_t board_handle = audio_board_init();
    audio_hal_ctrl_codec(board_handle->audio_hal, AUDIO_HAL_CODEC_MODE_DECODE, AUDIO_HAL_CTRL_START);   //To MIC pickup, please modify this configuration option.
      
---------------------

When using ESP32-WROVER-B module + ES8311 to design audio development board, which pins can be selected for MCLK clock?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - On the hardware side, MCLK can only use GPIO0, GPIO1, and GPIO3 pins. Other pins cannot be used. You can read `ESP32 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_ about CLK_OUT* pins in IO_MUX table. GPIO0 is used by default.
  - Please refer to the `schamatic of ESP32-LyraT-Mini  <https://dl.espressif.com/dl/schematics/SCH_ESP32-LYRAT-MINI_V1.2_20190605.pdf>`_.
  - For allocation of pins, please refer to `ESP32-LyraT-Mini V1.2 Hardware Reference <https://docs.espressif.com/projects/esp-adf/en/latest/design-guide/board-esp32-lyrat-mini-v1.2.html#esp32-lyrat-mini-v1-2-hardware-reference>`_.

------------------------

Can ESP32-WROVER-E module use one I2S line to realize simultaneous broadcasting and recording?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes, you can refer to `ESP32-LyraT Development Board <https://docs.espressif.com/projects/esp-adf/en/latest/design-guide/dev-boards/get-started-esp32-lyrat.html>`_.
  
---------------

Do Espressif modules support Spotify Connect?
---------------------------------------------------------------------------------------------------

  :CHIP\: ESP32 | ESP32-S2 | ESP32-S3 :

  - Not supported yet. It is suggested to try dlna, which has similar functions.

---------------

When running the `korvo_du1906 <https://github.com/espressif/esp-adf/tree/master/examples/korvo_du1906>`_ example on an ESP32-Korvo-DU1906 board, a reboot caused the following error message: `Guru Meditation Error: Core 0 panic'ed (IllegalInstruction). Exception was unhandled`. How to resolve such issue?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Please check the power supply. 
  - it is recommended that the system be connected to an at least 5 V/2 A power adapter for sufficient current supply.

---------------

Can ESP-DSP fft run 4096, 8192 and more samples?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes, up to 32 K samples are supported. The maximum number can be configured in menuconfig, e.g., for `fft demo <https://github.com/espressif/esp-dsp/tree/master/examples/fft>`_, go to ``idf.py menuconfig-->Component config-->DSP Library-->Maximum FFT length-->(*)32768``.

---------------

How to connect a microphone with ESP32?
-----------------------------------------------------

  - You can connect I2S peripheral if it is a digital microphone.
  - You can connect ADC peripheral if it is an analog microphone.

--------------

Does ESP32 support analog audio output or digital audio output?
-------------------------------------------------------------------------------------------

  - ESP32 supports DAC analog audio output for simple outputs such as tones. But if you use it for music playing, the effect will not be so desirable.
  - ESP32 supports PWM analog audio output, which has slightly better effect than DAC. The demo code is at `esp-iot-solution  <https://github.com/espressif/esp-iot-solution/tree/master/examples/audio/wav_player>`__.
  - ESP32 also supports I2S digital audio output. For I2S configurable pins, please see `ESP32 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_ > Chapter Peripherals and Sensors.

---------------------

What audio formats does the ESP32 chip support?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The ESP32 chip supports audio formats such as MP3, AAC, FLAC, WAV, OGG, OPUS, AMR, G.711, etc. Please refer to the `ESP-ADF <https://github.com/espressif/esp-adf>`_ SDK for instructions.
  
-----------------

How to use the ESP32 chip to decode compressed audio?
-----------------------------------------------------------------------------------------

  - Application examples that use the ESP32 chip to decode compressed audio can be found under the `esp-adf/examples/recorder <https://github.com/espressif/esp-adf/tree/c50f3dc43bd754568d0f52dbc111b543f0baa5cd/examples/recorder>`_ folder.

-----------------

Where is the code example for `ESP-LED-Strip <https://www.espressif.com/en/news/ESP-LEDStrip>`_?
----------------------------------------------------------------------------------------------------------------------------------------

   - Code examples for ESP-LED-Strip are provided in the ESP-ADF repo, please refer to `led_pixels example <https://github.com/espressif/esp-adf/tree/master/examples/display/led_pixels>`_.
