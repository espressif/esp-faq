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


Does esp-who support IDF 4.1?
--------------------------------

  No. Currently, the esp-who only supports IDF V3.3.1 and V 4.0.0 (esp-who commit: ``2470e47 Update esp32-camera``). The subsequent supported versions will be updated on `ESP-WHO Github <https://github.com/espressif/esp-who>`_.