RF Related
=============

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

Does the RF performance of an ESP32 module degrade if it runs at a 2.8 V supply?
------------------------------------------------------------------------------------------------------------------------------

  Yes, its RF performance may become unstable. It is recommended that the supplied voltage follows the suggested operating voltage range specified in the `module's datasheet <https://www.espressif.com/en/support/documents/technical-documents>`_.

--------------

What are the modulation methods supported by Espressif's chips?
------------------------------------------------------------------------------

  - ESP8266 supports BPSK/QPSK/16QAM/64QAM/DBPSK/DQPSK/CCK.
  - ESP32 supports BPSK/QPSK/16QAM/64QAM/DBPSK/DQPSK/CCK/GFSK Π/4-DQPSK 8-DPSK.
  - ESP32-S2 supports BPSK/QPSK/16QAM/64QAM/DBPSK/DQPSK/CCK.
  - ESP32-C3 supports BPSK/QPSK/16QAM/64QAM/DBPSK/DQPSK/CCK/GFSK Π/4-DQPSK 8-DPSK.
  - ESP32-S3 supports BPSK/QPSK/16QAM/64QAM/DBPSK/DQPSK/CCK/GFSK Π/4-DQPSK 8-DPSK.

--------------

How can I get the RF related information (e.g., antenna specification, antenna pattern, etc.) for certification?
------------------------------------------------------------------------------------------------------------------------------

  For such information, please contact `Sales <https://www.espressif.com/en/contact-us/sales-questions>`_ for help.

--------------

Why does ESP32 automatically reduce its transmit power when it uses the RF Test Tool at 80 °C?
--------------------------------------------------------------------------------------------------------------------------------------------------

  - Temperature compensation is disabled by default when ESP32 runs the fixed frequency firmware. Therefore, the power reduces at a high temperature. To enable temperature compensation, please send ``txpwr_track_en 1 1 0`` to ESP32 through the default log serial port.

--------------

How to improve the receiving distance and strength of Wi-Fi signals for ESP32-WROVER-E? (Application scenario: Wi-Fi probe)
----------------------------------------------------------------------------------------------------------------------------------

  - By software, you can either set the maximum transmit power by API `esp_wifi_set_max_tx_power() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv425esp_wifi_set_max_tx_power6int8_t>`_, or set that via menuconfig: ``Component config`` > ``PHY`` > ``Max Wi-Fi TX power(dBm)`` (the default maximum transmit power is 20 dBm).
  - If the transmit power has been set to the maximum, you can improve the efficiency of the antenna and receiving devices by the following methods.
  
    - Adjust the module direction so that the stronger radiation direction of the antenna points to the receiving device to achieve the farthest radiation distance.
    - Make sure there is no metal or blocking object near the antenna of the module, no PCB on the back of the antenna, and the Wi-Fi signal is not interfered by other signals of the end device.
    - Use the IE series module with an antenna connector if the performance of the PCB antenna cannot meet requirements, so that an external antenna with higher directional gain can be connected.
    - Increase the radiation efficiency of the antenna in the receiving device.

---------------

How to write phy_init data to flash ?
---------------------------------------------------------------------------------------------------

  :CHIP\: ESP32 :

  - You can write it via the power limit tool. Please download the `ESP_RF_TEST Tool <https://www.espressif.com/sites/default/files/tools/ESP_RF_Test_EN.zip>`_, unzip the package, open the EspRFTestTool_vx.x_Manual.exe file, and then click ``help`` > ``Tool help`` > ``PowerLimitTool help`` for detailed operations.