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
      

