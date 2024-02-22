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
  - If you still prefer to use Arduino to build your code, you can use Arduino-esp32 as an `ESP-IDF component <https://docs.espressif.com/projects/arduino-esp32/en/latest/esp-idf_component.html>`_ for development and testing.
