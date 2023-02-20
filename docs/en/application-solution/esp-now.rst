ESP-NOW
=======

:link_to_translation:`zh_CN:[中文]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

-----------------

What is the one-to-one bit rate for ESP32 in ESP-NOW mode？
-------------------------------------------------------------------

  Test result:

  - Test board: ESP32_Core_board_V2.
  - Wi-Fi mode: station.
  - PHY rate is 1 Mbps by default.
  - Around 214 Kbps in opened environment.
  - Around 555 Kbps in shielding box.
  - If you require a higher rate, please configure by `esp_wifi_config_espnow_rate <https://docs.espressif.com/projects/esp-idf/en/v4.4.2/esp32/api-reference/network/esp_now.html#_CPPv427esp_wifi_config_espnow_rate16wifi_interface_t15wifi_phy_rate_t>`_.

--------------

What is ESP-NOW? What are its advantages and application scenarios?
--------------------------------------------------------------------------

  - `ESP-NOW <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_now.html>`_ is a connectionless communication protocol defined by Espressif.
  - In ESP-NOW, application data is encapsulated in action frames from different vendors and then transmitted from one Wi-Fi device to another without a connection.
  - ESP-NOW is ideal for smart lights, remote control devices, sensors and other applications.

--------------

Can Wi-Fi be used with ESP-NOW at the same time?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes, but it should be noted that the channel of ESP-NOW must be the same as that of the connected AP.

--------------------

How do I set the rate at which ESP-NOW data is sent?
--------------------------------------------------------------------------------------------------------------------------------------------

  Use the `esp_wifi_config_espnow_rate() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_now.html#_CPPv427esp_wifi_config_espnow_rate16wifi_interface_t15wifi_phy_rate_t>`_ function to configure the rate, such as ``esp_wifi_config_espnow_rate(WIFI_IF_STA, WIFI_ PHY_RATE_MCS0_LGI)``.

-----------------

ESP-NOW allows pairing with a maximum of 20 devices. Is there a way to control more devices?
---------------------------------------------------------------------------------------------------------------------------------------------------------

  You can use broadcast packets and provide the destination addresses in the payload. The number of addresses is not affected by the limited number. You only need to configure the correct broadcast address.

-----------------

What is the maximum number of devices that can be controlled by ESP-NOW?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

  This depends on the specific communication method:

  - If unicast packets are used, up to 20 devices can be paired and controlled at the same time.
  - If ESP-NOW encrypted mode is used, up to 6 devices can be paired and controlled at the same time.
  - If broadcast packets are used, theoretically there is no upper limit to the number of devices that can be controlled. You only need to configure the correct broadcast address and consider the interference issue when too many devices are paired.

-----------------

Do I need to connect a router for communication between ESP-NOW devices?
---------------------------------------------------------------------------------------------------------

  ESP-NOW interacts directly from device to device and does not require a router to forward data.

-----------------

Why does ESP-NOW limit the data length of each packet to 250 bytes? Can it be modified?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The maximum length cannot be changed. ESP-NOW uses one vendor-specific element field of action frame to transmit ESP-NOW data, whose length field is only 1 byte (0xff = 255) as defined by IEEE 802.11. Thus, the maximum length of ESP-NOW data is limited to 250 bytes.
  - Or try with API ``esp_wifi_80211_tx()`` to send and sniffer mode to receive, both could work only base on Wi-Fi stack and without TCP/IP stack.

---------------

What should I pay attention to when using ESP-NOW applications?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The device cannot switch channels after connecting to Wi-Fi, but can only transmit and receive data on the current Wi-Fi channel.
  - After the device enters the modem sleep mode, it cannot receive data from ESP-NOW.

---------------

How can I reduce power consumption when using ESP-NOW?
--------------------------------------------------------------------------------------------------------------------------

  You can use the following methods to reduce power consumption:

     - If you use ESP-IDF in versions earlier than v5.0, you can set the wake-up window size and interval to save power when the AP is not connected with `esp_now_set_wake_window() <https://docs.espressif.com/projects/esp-idf/en/release-v4.4/esp32/api-reference/network/esp_now.html#_CPPv423esp_now_set_wake_window8uint16_t>`__ and `esp_wifi_set_connectionless_wake_interval() <https://docs.espressif.com/projects/esp-idf/en/v4.4.4/esp32/api-reference/network/esp_wifi.html#_CPPv441esp_wifi_set_connectionless_wake_interval8uint16_t>`__. These two functions are used to set the wake-up window size and interval, respectively.

     - If you use ESP-IDF v5.0 or the latest master version, the functions are different from the other versions. Whether the AP is connected or not, you can use `esp_now_set_wake_window() <https://docs.espressif.com/projects/esp-idf/en/release-v5.0/esp32/api-reference/network/esp_now.html#_CPPv423esp_now_set_wake_window8uint16_t>`__ and `esp_wifi_connectionless_module_set_wake_interval() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv448esp_wifi_connectionless_module_set_wake_interval8uint16_t>`__ to set the wake-up window size and interval, respectively.

     - However, at the sending end and receiving end, how to synchronize the window parameters needs to be considered in the design of the application layer. In this way, the chip will wake up at every “interval” and work for a period of time equalling the value of "window size". (Under this situation, you need to configure CONFIG_ESP_WIFI_STA_DISCONNECTED_PM_ENABLE=y in sdkconfig.defaults)

-----------------

In addition to wireless communication through ESP-NOW, is there any other better way to realize one-to-one and one-to-many communication?
-------------------------------------------------------------------------------------------------------------------------------------------

   It can also be realized by using SoftAP + Station. The master device applies Wi-Fi SoftAP mode to establish connections with multiple slave devices (Wi-Fi Station) at the same time.

-----------------

Do ESP-NOW applications support sending packets over each Wi-Fi channel?
-----------------------------------------------------------------------------------------------------------------------------------------

   Yes, please refer to `ESP-NOW documentation <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_now.html>`__.

-----------------

Are there any special procedures if I use ESP-NOW for commercial purposes? Could you provide technical documentation on ESP-NOW? In order to evaluate the quality of wireless communication, I would like to know the following parameters, e.g., CSMA/CA, modulation method, and bit rate.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

- The application for ESP-NOW does not require any special procedures.
- For technical documentation, please refer to `ESP-NOW User Guide <https://www.espressif.com/sites/default/files/documentation/esp-now_user_guide_en.pdf>`__. You can use examples in `ESP-NOW SDK <https: //github.com/espressif/esp-now>`__ to test.
- The default bit rate of ESP-NOW is 1 Mbps.
