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

--------------

How to improve the distance and strength of Wi-Fi signals for ESP32-WROVER-E? (Application scenario: Wi-Fi probe)
-----------------------------------------------------------------------------------------------------------------------

  - In terms of software, you can either set the maximum transmit power by API `esp_wifi_set_max_tx_power() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv425esp_wifi_set_max_tx_power6int8_t>`_, or set that via menuconfig: ``Component config -> PHY -> Max Wi-Fi TX power(dBm)`` (the default transmit power is 20 dBm).
  - If the transmit power has been set to the maximum, you can improve the effeciency the antenna and receiving device.
  
    - You can consider adjusting the placement direction of the module so that the stronger radiation direction of the antenna points to the receiving device to make the farthest radiation distance.
    - Make sure there is no metal or blocking object near the antenna of the module, no PCB on the back of the antenna, and the Wi-Fi signal is not interfered by other signals of the whole machine.
    - If the PCB antenna is not effective, you can use the IE series module with an external IPEX antenna with higher directional gain.
    - The receiving device can also increase the antenna radiation efficiency.

---------------

How to write phy_init data to Flash ?
---------------------------------------------------------------------------------------------------

  :CHIP\: ESP32 :

 - You can write via the power limit tool. Please download the `ESP_RF_TEST Tool <https://www.espressif.com/sites/default/files/tools/ESP_RF_Test_CN.zip>`_, unzip the package and open the EspRFTestTool_v2.6_Manual.exe file, then click ``help ---> Tool help ---> PowerLimitTool help`` for detailed operations.
