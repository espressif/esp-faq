Two-Wire Automotive Interface (TWAI)
====================================

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

What are the considerations when using the ESP32 TWAI® controller?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Please refer to the `ESP32 Series SoC Errata <https://www.espressif.com/sites/default/files/documentation/esp32_errata_en.pdf>`_ > Section *ESP32 TWAI Errata*.

--------------

Does ESP32-S3 support CAN-FD?
----------------------------------------------------------------------

  The ESP32-S3 itself does not integrate a CAN-FD controller, but users can still use a CAN-FD controller with an SPI interface, such as the MCP2518FD.

--------------

Does ESP32 support interrupt mode for CAN reception?
----------------------------------------------------------------------

  The TAWI driver already uses interrupt reception, and automatically stores the received information into the RX queue.
