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


What kinds of cameras can be used on AI image recognition products?
----------------------------------------------------------------------

  With ESP32 as its main control chip, ESP-EYE supports various types of cameras, such as 0V2640, OV3660, OV5640, OV7725 and etc (See `esp32-camera Github <https://github.com/espressif/esp32-camera/tree/master/sensors>`_).


Which versions of ESP-IDF are supported by ESP-WHO??
--------------------------------------------------------------------------------------

  The subsequent supported versions will be updated on `ESP-WHO Github <https://github.com/espressif/esp-who>`_.

------------------------------------------------------------------

What languages are supported by the `esp-skainet <https://github.com/espressif/esp-skainet>`_ demo ?
--------------------------------------------------------------------------------------------------------------------------------------

  - Only Chinese and English currently.

------------------------------------------------------------------

What model frameworks does `ESP-DL <https://github.com/espressif/esp-dl>`_ support?
-------------------------------------------------------------------------------------------------------------------------------

  - Currently, `ESP-DL <https://github.com/espressif/esp-dl>`_ supports models from mxnet, pytorh, and tensorflow.

--------------

Does `ESP-DL <https://github.com/espressif/esp-dl>`_ support all models of the three platforms mentioned above?
-------------------------------------------------------------------------------------------------------------------------------

  - ESP-DL supports models in which all the operators are supported by ESP-DL. Please check `layer <https://github.com/espressif/esp-dl/tree/master/include/layer>` for the supported operators.

--------------

Do the model files of `ESP-SKAINET <https://github.com/espressif/esp-skainet>`_ support being placed on the SD card? 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Support.

----------------------
