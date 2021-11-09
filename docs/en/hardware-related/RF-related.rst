RF related
==========

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

If an ESP32 module is running under a 2.8 V supply, is there any degradation in its RF performance?
------------------------------------------------------------------------------------------------------------------------------

  Yes, its RF performance may become unstable. It is recommended that the voltage be supplied in accordance with the suggested operating voltage range specified in the `Module's Datasheet <https://www.espressif.com/en/support/documents/technical-documents>`_.

--------------

What are the modulation methods supported by Espressif's chips?
------------------------------------------------------------------------------

  - ESP8266 supports: BPSK/QPSK/16QAM/64QAM/DBPSK/DQPSK/CCK.
  - ESP32 supports: BPSK/QPSK/16QAM/64QAM/DBPSK/DQPSK/CCK/GFSK Π/4-DQPSK 8-DPSK.
  - ESP32-S2 supports: BPSK/QPSK/16QAM/64QAM/DBPSK/DQPSK/CCK.

--------------

How can I get the RF related information (e.g., antenna specification, antenna pattern, etc.) for certification?
------------------------------------------------------------------------------------------------------------------------------

  For such information, please contact `Sales <https://www.espressif.com/en/contact-us/sales-questions>`_ for help.

--------------

Why does ESP32 automatically reduce the transmit power when running at a high temperature of 80 °C when using the RF Test Tool?
--------------------------------------------------------------------------------------------------------------------------------------------------

  - The temperature compensation function on testing firmware with a fixed frequency is disabled by default. Therefore, when the temperature is high, the power will be lower. If you need to enable the temperature compensation, please send ``txpwr_track_en 1 1 0`` to ESP32 through the default log serial port.
