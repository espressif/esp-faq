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
---------------------------------------------------

  No. If you want to use this function, it is recommended to choose ESP32 or ESP32-S2 chips instead. For ESP32 examples, please refer to `i2C_self_test <https://github.com/espressif/esp-idf/tree/master/examples/peripherals/i2c/i2c_self_test>`_.

--------------

Is ESP8266 I2C realized via software programming?
-----------------------------------------------------------------------

  Yes, ESP8266 I2C is realized via GPIO software programming.

--------------

When the I2C of the ESP32 series chip is operating (especially in fast mode), spikes often occur on the data lines, especially after the falling edge of the 8th/9th clock. Is this normal?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The spike on the data line at the 8th/9th clocks is caused by the I2C master-slave control handover. It is a normal phenomenon and is mentioned in the I2C protocol.

------------------------

How can I realize data are received by ESP32 series chips, which are used as the I2C master, only after these data are processed by the slave? For example, when ESP32 chips read data through ``i2c_master_read_to_device``, the slave should return data immediately after receiving the command. However, some slave devices wait for a while to return data after receiving the command.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  This can be realized by dividing ``i2c_master_read_device`` into the following three steps:

    1. Input commands and address: ``i2c_cmd_link_create_static`` > ``i2c_master_start`` > ``i2c_master_write_byte`` > ``i2c_master_cmd_begin`` > ``i2c_cmd_link_delete_static``
    2. Delay
    3. Read data of the slave: ``i2c_cmd_link_create_static`` > ``i2c_master_read`` > ``i2c_master_stop`` > ``i2c_master_cmd_begin`` > ``i2c_cmd_link_delete_static``

--------------

When using ESP32 series chip, can we configure GPIO32 and GPIO33 as I2C_SDA and I2C_SCL respectively?
------------------------------------------------------------------------------------------------------------------------------------------------------

  Yes. I2C pins of the ESP32 chip can be remapped by any available GPIOs. Please refer to "4.2 Peripheral Pin Configurations" of `ESP32 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`__. If you do not need an external 32.768 KHz crystal, you can use GPIO32 and GPIO33 as I2C pins.
