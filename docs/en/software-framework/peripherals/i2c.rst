Inter-Integrated Circuit (I2C)
==============================

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

Does ESP8266 support I2C slave mode?
--------------------------------------------------

  No. If you want to use this function, it is recommended to choose ESP32 or ESP32-S2 chips instead. For ESP32 examples, please refer to `i2C_self_test <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/i2c/i2c_self_test>`_.

--------------

Is ESP8266 I2C realized via software programming?
-----------------------------------------------------------------------

  Yes, ESP8266 I2C is realized via GPIO software programming.

--------------

When the I2C of the ESP32 series chip is operating (especially in fast mode), spikes often occur on the data lines, especially after the falling edge of the 8th/9th clock. Is this normal?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The spike on the data line at the 8th/9th clocks is caused by the I2C master-slave control handover. It is a normal phenomenon and is mentioned in the I2C protocol.