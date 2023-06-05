Artificial intelligence
=======================

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

What types of cameras are supported on AI image recognition products?
-------------------------------------------------------------------------------------

  With ESP32 as its main control chip, ESP-EYE supports various types of cameras, such as 0V2640, OV3660, OV5640, OV7725, etc. Please see `esp32-camera Github <https://github.com/espressif/esp32-camera/tree/master/sensors>`_.

--------------

Which versions of ESP-IDF are supported by ESP-WHO?
--------------------------------------------------------------------------------------

  The subsequent supported versions will be updated on `ESP-WHO Github <https://github.com/espressif/esp-who>`_.

------------------------------------------------------------------

Is there any information about the WeChat mini program of ESP-EYE?
---------------------------------------------------------------------------

  For open source resources of ESP-EYE mini program demo, please check `EspEyeForWeChat <https://github.com/EspressifApp/EspEyeForWeChat>`_.

----------------------

What languages are supported by the `esp-skainet <https://github.com/espressif/esp-skainet>`_ demo?
--------------------------------------------------------------------------------------------------------------------------------------

  Only Chinese and English currently.

------------------------------------------------------------------

What model frameworks does `ESP-DL <https://github.com/espressif/esp-dl>`_ support?
-------------------------------------------------------------------------------------------------------------------------------

  Currently, `ESP-DL <https://github.com/espressif/esp-dl>`_ supports models from mxnet, pytorch, and tensorflow.

--------------

Does `ESP-DL <https://github.com/espressif/esp-dl>`_ support all models of the three platforms mentioned above (mxnet, pytorch, and tensorflow)?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ESP-DL supports models in which all the operators are supported by ESP-DL. Please check `layer <https://github.com/espressif/esp-dl/tree/master/include/layer>`_ for the supported operators.

--------------

Can the model files of `ESP-SKAINET <https://github.com/espressif/esp-skainet>`_ be stored in the SD card? 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Yes.

----------------------

How to customize command words in `ESP-SKAINET <https://github.com/espressif/esp-skainet>`_?
------------------------------------------------------------------------------------------------------------------------------------------

  To customize command words, please see `ESP-SR GitHub <https://github.com/espressif/esp-sr/blob/master/docs/speech_command_recognition/README.md>`__. 

----------------------

How to reduce the system footprint of AI speech models?
------------------------------------------------------------------------------

  You can choose to turn off the three functions, namely AEC, AE, and VAD.

----------------------

What is the difference between a 16-bit quantization model and an 8-bit quantization model?
-------------------------------------------------------------------------------------------------------

  The 16-bit quantization model has higher precision and more accurate results, while the 8-bit quantization model is more lightweight.

----------------------

How does the AI voice model modify the number of microphone channels?
-------------------------------------------------------------------------------

  The number of microphone channels and the number of playback channels can be configured in the AFE.

----------------------

How do I get the actual audio captured in the development board?
--------------------------------------------------------------------

  To obtain the actual audio, an SD card interface is required to store the audio files to the SD card.

----------------------

Do you have relevant study materials for `ESP-SR GitHub <https://github.com/espressif/esp-sr/tree/master>`__?
---------------------------------------------------------------------------------------------------------------------------------------------------------

  Please refer to `ESP-SR User Guide <https://docs.espressif.com/projects/esp-sr/en/latest/esp32s3/index.html>`_.

----------------------

Do you have relevant study materials for `ESP-DL <https://github.com/espressif/esp-dl>`__?
-----------------------------------------------------------------------------------------------------

  Please refer to `How to deploy hand gesture recognition with ESP-DL <https://medium.com/the-esp-journal/hand-gesture-recognition-on-esp32-s3-with-esp-deep-learning-176d7e13fd37>`_.

-------------

How does ESP32-S3 customize English command words for recognition?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - For MultiNet6, you need to prepare ``commands_en.txt`` to customize English command words. For MultiNet5, you need to use the ``multinet_g2p.py`` script to convert English command words into phonemes that can be recognized by multinet. For details, please refer to `esp-sr/tool <https://github.com/espressif/esp-sr/tree/master/tool>`_.
