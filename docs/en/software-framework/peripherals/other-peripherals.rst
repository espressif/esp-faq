Other Peripherals
=================

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

Can the REF_TICK clock frequency be modified?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32 | ESP32-S2 | ESP32-C3:

  No, the REF_TICK clock is fixed.

--------------

Does ESP32 support PCI-E protocol?
-----------------------------------------------------

  No, it doesn't.

-------------------

Does the `screen <https://github.com/espressif/esp-iot-solution/tree/master/examples/screen>`__ example support 9-bit bus and 18-bit color depth when tested with the ILI9488 LCD screen?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Theoretically, the ILI9488 LCD can support 9-bit bus and 18-bit color depth, but currently our driver can only support up to 8-bit bus and 16-bit color depth. You can modify the driver by yourself according to the ILI9488 LCD manual to implement the support.