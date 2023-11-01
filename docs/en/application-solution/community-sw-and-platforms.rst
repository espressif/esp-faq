Community Software and Platforms
================================

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

Can ESP32-SOLO-1 be developed using the Arduino software?
---------------------------------------------------------

  - Currently, ESP32-SOLO-1 is not supported for development in the Arduino software.
  - If you still prefer to build your code with Arduino, use "Arduino-esp32" as a `component of ESP-IDF <https://github.com/espressif/arduino-esp32/blob/master/docs/source/esp-idf_component.rst>`_ for development and testing.
