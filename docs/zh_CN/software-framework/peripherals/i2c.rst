I2C 驱动程序
================

:link_to_translation:`en:[English]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

--------------

ESP8266 是否支持 I2C 从机模式？
-------------------------------------------------

  不支持，如果要使用此功能，推荐使用 ESP32 或者 ESP32-S2 芯片。ESP32 参考示例： `i2C_self_test <https://github.com/espressif/esp-idf/tree/release/v5.1/examples/peripherals/i2c/i2c_self_test>`_。

--------------

ESP8266 I2C 是软件模拟的吗？
-------------------------------------

  ESP8266 I2C 是使用 GPIO 软件模拟。

--------------

当 ESP32 芯片 I2C 在工作时（尤其是处于快速模式时），数据线上经常出现一些尖峰，往往在第 8/9 个时钟的下降沿之后，这是否正常？
---------------------------------------------------------------------------------------------------------------------------------------------

  发生在 8/9 个时钟时数据线上的尖峰是由于 I2C 主从机控制权交接导致的，属于 I2C 协议里提到的正常现象。

--------------

ESP32 芯片作为 I2C 主机怎样才能等待从机处理数据后再接收？例如通过 ``i2c_master_read_to_device`` 读取数据时, 需要从机接受命令后立即返回数据，但是实际的一些从机设备接收到命令后需要等待一段时间才能返回数据。
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  可以自行将 ``i2c_master_read_device`` 拆分成三部分进行实现：

    1. 写命令和地址：``i2c_cmd_link_create_static`` > ``i2c_master_start`` > ``i2c_master_write_byte`` > ``i2c_master_cmd_begin`` > ``i2c_cmd_link_delete_static``
    2. 延时
    3. 读从机数据：``i2c_cmd_link_create_static`` > ``i2c_master_read`` > ``i2c_master_stop`` > ``i2c_master_cmd_begin`` > ``i2c_cmd_link_delete_static``

--------------

使用 ESP32 芯片时，能否将 GPIO32 和 GPIO33 分别配置为 I2C_SDA 和 I2C_SCL？
----------------------------------------------------------------------------------------------------------------------------------------------

  可以，ESP32 的 I2C 管脚可以使用任何空闲的 GPIO 进行重映射。请参阅 `ESP32 技术规格书 <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf>`_ 的 2.2 小节，管脚概述部分。如果不需要外部 32.768 kHz 晶振，则可以使用 GPIO32 和 GPIO33 作为 I2C 管脚。
