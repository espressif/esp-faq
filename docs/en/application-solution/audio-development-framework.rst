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

  - Yes, you can refer to `ESP32-LyraT Development Board <https://docs.espressif.com/projects/esp-adf/en/latest/get-started/get-started-esp32-lyrat.html#esp32-lyrat-v4-3>`_.
  
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
