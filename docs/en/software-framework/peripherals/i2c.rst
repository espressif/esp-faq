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

  Not supported. If you want to use this feature, we recommend using the ESP32 or ESP32-S2 chip. ESP32 example: `i2C_self_test <https://github.com/espressif/esp-idf/tree/release/v5.1/examples/peripherals/i2c/i2c_self_test>`_.

--------------

Is ESP8266 I2C realized via software programming?
-----------------------------------------------------------------------

  Yes, ESP8266 I2C is realized via GPIO software programming.

--------------

Is it normal for some spikes to frequently appear on the data line when the ESP32 chip I2C is working (especially in fast mode), often after the falling edge of the 8th/9th clock?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The spike on the data line at the 8th/9th clocks is caused by the I2C master-slave control handover. It is a normal phenomenon and is mentioned in the I2C protocol.

------------------------

How can the ESP32 chip, as an I2C master, wait for the slave to process the data before receiving it? For example, when reading data through ``i2c_master_read_to_device``, the slave needs to return data immediately after accepting the command, but in reality, some slave devices need to wait for a while after receiving the command before they can return data.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  This can be realized by dividing ``i2c_master_read_device`` into the following three steps:

    1. Input commands and address: ``i2c_cmd_link_create_static`` > ``i2c_master_start`` > ``i2c_master_write_byte`` > ``i2c_master_cmd_begin`` > ``i2c_cmd_link_delete_static``
    2. Delay
    3. Read data of the slave: ``i2c_cmd_link_create_static`` > ``i2c_master_read`` > ``i2c_master_stop`` > ``i2c_master_cmd_begin`` > ``i2c_cmd_link_delete_static``

--------------

When using the ESP32 chip, can GPIO32 and GPIO33 be configured as I2C_SDA and I2C_SCL respectively?
------------------------------------------------------------------------------------------------------------------------------------------------------

  Yes. The I2C pins of the ESP32 chip can be remapped by any available GPIO. Please refer to Section 2.2, Pin Overview of `ESP32 Series Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_. If an external 32.768 kHz crystal is not required, GPIO32 and GPIO33 can be used as I2C pins.
