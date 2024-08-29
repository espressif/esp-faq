Wi-Fi
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

--------------

Do ESP32 and ESP8266 support Chinese SSID for Wi-Fi?
------------------------------------------------------------

  Both ESP32 and ESP8266 support Chinese SSID, but you need to use corresponding libraries and implement some settings. It should be noted you need to make special configurations when using Chinese SSID as Chinese characters occupy different numbers of bytes.

  For ESP32, you can use the Wi-Fi related API provided by ESP-IDF. When connecting AP, you can use the fuction `esp_wifi_set_config() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv419esp_wifi_set_config16wifi_interface_tP13wifi_config_t>`_ to set Wi-Fi. The SSID parameter can be set to Chinese characters. For example,

  .. code-block:: c

    wifi_config_t wifi_config = {
      .sta = {
          .ssid = "你好，世界",
          .password = "password123",
      },
    };
    ESP_ERROR_CHECK(esp_wifi_set_config(ESP_IF_WIFI_STA, &wifi_config));


--------------

How much time does an ESP32 scan take?
------------------------------------------------

  The total time for scanning depends on:

  - Active scan (by default) or passive scan.
  - The time spent on each channel is 120 ms for active scanning and 360 ms for passive scanning.
  - The country code and configured channel range from 1~13 channels (by default).
  - Fast scan (by default) or full-channel scan.
  - Station mode or Station-AP mode, and if any active connections are currently maintained.

  By default, channels 1 to 11 use active scans, and channels 12 to 13 use passive scans.

  - In the absence of connection in Station mode, the total time for a full-channel scan is: 11*120 + 2*360 = 2040 ms.
  - With active connections in Station mode or Station-AP mode, the total time for a full-channel scan is: 11*120 + 2*360 + 13*30 = 2430 ms.

--------------

[Scan] Do Espressif's products support boundary scans?
--------------------------------------------------------------

  No, they don't.

--------------

What is the definition for Wi-Fi channel? Can I select any channel of my choice?
------------------------------------------------------------------------------------------

  - A Wi-Fi channel is a frequency range used for wireless communication. Different countries and regions have regulations on the available Wi-Fi channels. For example, in North America, the Wi-Fi channel ranges from 1 to 11, while in Europe, the Wi-Fi channel ranges from 1 to 13. For more details, please refer to `ESP8266 Wi-Fi Channel Selection Guidelines <https://www.espressif.com/sites/default/files/documentation/esp8266_wi-fi_channel_selection_guidelines_en.pdf>`_.

--------------

[LWIP] With ESP-IDF v4.1, how to configure ESP32's IP address when it is in SoftAP mode?
------------------------------------------------------------------------------------------------

  Since ESP-IDF v4.1 and later versions do not have TCP/IP interfaces anymore, it is recommended to use the `ESP-NETIF <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_netif.html>`_ interface instead.

  Code example：

  .. code-block:: c

    {
        ...
        esp_netif_t *ap_netif = esp_netif_create_default_wifi_ap();
        char* ip= "192.168.5.241";
        char* gateway = "192.168.5.1";
        char* netmask = "255.255.255.0";
        esp_netif_ip_info_t info_t;
        memset(&info_t, 0, sizeof(esp_netif_ip_info_t));

        if (ap_netif)
        {
            ESP_ERROR_CHECK(esp_netif_dhcps_stop(ap_netif));
            info_t.ip.addr = esp_ip4addr_aton((const char *)ip);
            info_t.netmask.addr = esp_ip4addr_aton((const char *)netmask);
            info_t.gw.addr = esp_ip4addr_aton((const char *)gateway);
            esp_netif_set_ip_info(ap_netif, &info_t);
            ESP_ERROR_CHECK(esp_netif_dhcps_start(ap_netif));
        }
        ...
    }

--------------

[LWIP] How to configure ESP32's static IP when it is in Station mode？
----------------------------------------------------------------------------------

  Since ESP-IDF v4.2 and later versions do not have tcp/ip interfaces anymore, it is recommended to use the `ESP-NETIF <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_netif.html>`_ interface instead. The code example is as follows：

  .. code-block:: c

    esp_netif_t *sta_netif = esp_netif_create_default_wifi_sta();
    if (sta_netif)
    {
        esp_netif_ip_info_t info_t = {0};
        esp_netif_dhcpc_stop(sta_netif);

        info_t.ip.addr = ESP_IP4TOADDR(192, 168, 3, 23);
        info_t.gw.addr = ESP_IP4TOADDR(192, 168, 3, 1);
        info_t.netmask.addr = ESP_IP4TOADDR(255, 255, 255, 0);
        esp_netif_set_ip_info(sta_netif, &info_t);
    }
    esp_netif_dns_info_t dns_info = {0};

--------------

[LWIP] How to configure the Option contents of DHCP Server in ESP-IDF?
-----------------------------------------------------------------------------------------

  Since ESP-IDF v4.1 and later versions do not have TCP/IP interfaces anymore, it is recommended to use the `ESP-NETIF <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_netif.html>`_ interface instead. You can also refer to this example when dealing with DHCP Client configuration. The code example is as follows:

  .. code-block:: c

    // Set up the handle for softap netif
    esp_netif_t *ap_netif = esp_netif_create_default_wifi_ap();

    // ESP_NETIF_IP_ADDRESS_LEASE_TIME, DHCP Option 51, Set the lease time for distributed IP address
    uint32_t dhcps_lease_time = 60; // The unit is min
    ESP_ERROR_CHECK(esp_netif_dhcps_option(ap_netif,ESP_NETIF_OP_SET,ESP_NETIF_IP_ADDRESS_LEASE_TIME,&dhcps_lease_time,sizeof(dhcps_lease_time)));

    // ESP_NETIF_DOMAIN_NAME_SERVER , DHCP Option 6, Set DNS SERVER
    // Set the local domain DNS first
    esp_netif_dns_info_t dns_info = {0};
    dns_info.ip.u_addr.ip4.addr = ESP_IP4TOADDR(8,8,8,8);
    ESP_ERROR_CHECK(esp_netif_set_dns_info(ap_netif,ESP_NETIF_DNS_MAIN,&dns_info));

    uint8_t dns_offer = 1; // Pass 1 to make the modified DNS take effect, if it is 0, then it means the gw ip of softap is used as the DNS server (0 by default)
    ESP_ERROR_CHECK(esp_netif_dhcps_option(ap_netif,ESP_NETIF_OP_SET,ESP_NETIF_DOMAIN_NAME_SERVER,&dns_offer,sizeof(dns_offer)));

    // ESP_NETIF_ROUTER_SOLICITATION_ADDRESS, DHCP Option 3 Router, Pass 0 to make the DHCP Option 3(Router) un-shown (1 by default)
    uint8_t router_enable = 0;
    ESP_ERROR_CHECK(esp_netif_dhcps_option(ap_netif,ESP_NETIF_OP_SET,ESP_NETIF_ROUTER_SOLICITATION_ADDRESS,&router_enable, sizeof(router_enable)));

    // ESP_NETIF_SUBNET_MASK, DHCP Option 1, Configure the subnet mask
    // If it fails to configure the subnet mask via ESP_NETIF_SUBNET_MASK, please make modifications using esp_netif_set_ip_info

--------------

[Performance] How to test the bit rate of Wi-Fi modules?
--------------------------------------------------------------------------

  Please use the example `iperf <https://github.com/espressif/esp-idf/tree/v4.4.4/examples/wifi/iperf>`_ in ESP-IDF for testing.

--------------

[LWIP] What is the default IP address of ESP8266 SoftAP?
---------------------------------------------------------------------------

  The default network segment used by ESP8266 SoftAP is 192.168.4.\*.

--------------

Why do I have problem connecting to router with IP 192.168.4.X in SoftAP + Station mode?
----------------------------------------------------------------------------------------------

  The default network segment used by ESP8266 SoftAP is 192.168.4.\*, and its IP address is 192.168.4.1. When connecting ESP8266 to the router of 192.168.4.X, it cannot distinguish whether this address indicates its own SoftAP or the external router.

--------------

[Connect] How many devices is ESP8266 able to connect in SoftAP mode?
--------------------------------------------------------------------------------------

  The ESP8266 chip in SoftAP mode supports connecting eight devices at most. This is because the NAT (Network Address Translation) mechanism used by the ESP8266 chip in SoftAP mode only supports eight devices at most.
  However, it should be noted that each connected device will occupy a certain amount of bandwidth and resources. Therefore, we recommend connecting four devices as too many devices may affect the performance and stability of the Wi-Fi module.

--------------

Do ESP8266/ESP32/ESP32-S2/S3/C2/C3 support web/SoftAP provisioning?
-----------------------------------------------------------------------------------------

  Yes.

  - For ESP8266, please refer to example `ESP8266 softap_prov <https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/provisioning/legacy/softap_prov>`_.
  - For ESP32/ESP32-S2/S3/C2/C3, please refer to example `ESP32/ESP32-S2/S3/C2/C3 wifi_prov_mgr <https://github.com/espressif/esp-idf/tree/master/examples/provisioning/wifi_prov_mgr>`_.

--------------

[Connect] How do ESP8266 and ESP32 hide SSID in SoftAP mode?
-------------------------------------------------------------------------

  To hide ESP8266 or ESP32 as SSID in SoftAP mode, you can use the following methods:

  Use the `esp_wifi_set_config() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv419esp_wifi_set_config16wifi_interface_tP13wifi_config_t>`_ function to configure the SSID and password in SoftAP mode and whether to hiding them. For example, the following code sets the SSID to "MySoftAP", the password to "MyPassword", and set .ssid_hidden = 1 to hide the SSID:

  .. code-block:: c

    wifi_config_t config = {
      .ap = {
        .ssid = "MySoftAP",
        .ssid_len = strlen("MySoftAP"),
        .password = "MyPassword",
        .max_connection = 4,
        .authmode = WIFI_AUTH_WPA_WPA2_PSK
        .ssid_hidden = 1
      },
    };
    esp_wifi_set_config(WIFI_IF_AP, &config);

  Then use `esp_wifi_start() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv414esp_wifi_startv>`_ function to starts Wi-Fi.

--------------

Does the buffer parameter in `esp_wifi_802.11_tx <https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/api-reference/wifi/esp_wifi.html?highlight=esp_wifi_802.11_tx#_CPPv417esp_wifi_80211_tx16wifi_interface_tPKvib>`_ interface include FCS?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  No, the FCS frame is generated automatically by hardware.

--------------

What is the supported Wi-Fi frequency band and power meter for ESP-WROOM-32D?
-------------------------------------------------------------------------------------------

  The Wi-Fi frequency band is 2412 ~ 2484 MHz, and the available channels and corresponding operating frequencies can be configured in software. There are default values in power meter, and it can also be configured by software. For detailed guidance, please refer to `ESP32 Phy Init Bin Parameter Configuration Guide <https://www.espressif.com/sites/default/files/documentation/esp32_phy_init_bin_parameter_configuration_guide_en.pdf>`_.

--------------

What is the maximum value of ESP32 Wi-Fi RF power？
-----------------------------------------------------------

  The output RF power of ESP32 can be set to 20 dBm at maximum.
  Please note that the maximum output power may vary in different countires and regions. Please ensure that you comply with local rules and regulations when using ESP32. In addition, high power output also influence battery life and Wi-Fi signal stability. As a result, you should confirm the output power depending on applications and requirements.

--------------

How does ESP32 adjust Wi-Fi TX power?
--------------------------------------------

  - Configure ``Component config`` > ``PHY`` > ``Max Wi-Fi TX power(dBm)`` via menuconfig, and the max value is 20 dBm.
  - Use API `esp_err_t esp_wifi_set_max_tx_power(int8_t power);`.

--------------

[Connect] How many devices is ESP32 able to connect in AP mode?
--------------------------------------------------------------------------

  Up to 10 devices in AP mode. It is configured to support four devices by default.

--------------

[Connect] How do Wi-Fi modules rank signal strength levels based on RSSI values？
--------------------------------------------------------------------------------------------

  We do not have a rating for RSSI signal strength. You can take the calculation method from Android system for reference if you need a standard for classification.

  .. code-block:: java

    @UnsupportedAppUsage
    private static final int MIN_RSSI = -100;

    /** Anything better than or equal to this will show the max bars. */
    @UnsupportedAppUsage
    private static final int MAX_RSSI = -55;

    public static int calculateSignalLevel(int rssi, int numLevels) {
      if(rssi <= MIN_RSSI) {
        return 0;
      } else if (rssi >= MAX_RSSI) {
        return numLevels - 1;
      } else {
        float inputRange = (MAX_RSSI -MIN_RSSI);
        float outputRange = (numLevels - 1);
        return (int)((float)(rssi - MIN_RSSI) * outputRange / inputRange);
      }
    }

--------------

[Connect] Why does ESP32 disconnect from STA when it is in Soft-AP mode?
------------------------------------------------------------------------------------

  - By default, the ESP32 will disconnect from the connected STA if it doesn't receive any data from this STA for continuous 5 minutes. This time can be modified via API `esp_wifi_set_inactive_time <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv426esp_wifi_set_inactive_time16wifi_interface_t8uint16_t>`_.

  - Note: esp_wifi_set_inactive_time is a newly added API.

    - master commit: ``63b566eb27da187c13f9b6ef707ab3315da24c9d``
    - 4.2 commit: ``d0dae5426380f771b0e192d8ccb051ce5308485e``
    - 4.1 commit: ``445635fe45b7205497ad81289c5a808156a43539``
    - 4.0 commit: ``0a8abf6ffececa37538f7293063dc0b50c72082a``
    - 3.3 commit: ``908938bc3cd917edec2ed37a709a153182d511da``

--------------

[Connect] While ESP32 connecting Wi-Fi, how can I determine the reason of failure by error codes?
------------------------------------------------------------------------------------------------------------

  For ESP-IDF v4.0 and later versions, please refer to the following codes to get the reason：

  .. code-block:: c

    if (event_base == WIFI_EVENT && event_id == WIFI_EVENT_STA_DISCONNECTED) {
      wifi_event_sta_disconnected_t *sta_disconnect_evt = (wifi_event_sta_disconnected_t*)event_data;
      ESP_LOGI(TAG, "wifi disconnect reason:%d", sta_disconnect_evt->reason);
      esp_wifi_connect();
      xEventGroupClearBits(s_wifi_event_group, CONNECTED_BIT);
    }

  When the callback function receives the ``WIFI_EVENT_STA_DISCONNECTED`` event, the failure reason can be obtained through the ``reason`` variable of the structure `wifi_event_sta_disconnected_t <https://github.com/espressif/esp-idf/blob/5454d37d496a8c58542eb450467471404c606501/components/esp_wifi/include/esp_wifi_types_generic.h#L815>`__.

  - ``WIFI_REASON_AUTH_EXPIRE``: This code is returned during the auth phase when the STA sends an auth but do not received any auth reply from the AP within the specified time. The possibility of this code occurrence is low.

  - ``WIFI_REASON_AUTH_LEAVE``: This code is sent by AP, normally because the AP is disconnected from the STA for some reason.

  -  ``WIFI_REASON_4WAY_HANDSHAKE_TIMEOUT`` or ``WIFI_REASON_HANDSHAKE_TIMEOUT``: Wrong password.

     ``WIFI_REASON_4WAY_HANDSHAKE_TIMEOUT`` is the standard generalized error code, while ``WIFI_REASON_HANDSHAKE_TIMEOUT`` is a customized error code. The main difference is: ``WIFI_REASON_4WAY_HANDSHAKE_TIMEOUT`` occurs when the router tells the device the password is wrong; ``WIFI_REASON_HANDSHAKE_TIMEOUT`` occurs when the device itself performs a timeout mechanism without being informed about the wrong password by the router.

  - ``WIFI_REASON_CONNECTION_FAIL``: This code is returned during the scan phase when the STA scanned a matched AP while the AP is in the blacklist. This is probably because that the AP has actively disconnected from the STA last time or something wrong happened when the STA connecting the AP.

--------------

Does ESP32 perform domain name resolution each time it connects to the server?
------------------------------------------------------------------------------------------

  The domain name is resolved via DNS within the stack, and the resolved data will be cached within the specified time. The cache time is based on the TTL data obtained from the DNS server, which is a parameter filled when configuring the domain name, usually 10 minutes.

--------------

[Connect] What does the number after the state machine switch in Wi-Fi log mean?
-------------------------------------------------------------------------------------------

  eg: run -> init (fc0), fc0 means the STA has received the deauth frame and reason is password error.

    - c0 indicates the received frame type (00 indicates a timeout)
    - f indicates reason

  Frame type: [a0 disassoc], [b0 auth], [c0 deauth].

--------------

[Connect] What does bcn_timeout, ap_probe_send_start mean？
----------------------------------------------------------------------

  The STA does not receive the Beacon frame within the specified time (6 s by default for ESP32, equals to 60 Beacon Intervals).
  - The reason could be:

    - Insufficient memory. "ESP32_WIFI_MGMT_SBUF_NUM" is not enough (there will be errors like "esf_buf: t=8, l=beacon_len, ..." in the log). You can check this by typing the heap size when received a Disconnect event.
    - The AP did not send a beacon. This can be checked by capturing beacons from AP.
    - Rssi too low. When the Rssi value is too low in complex environments, the STA may not receive the beacon. This can be checked by retrieving Rssi values via ``esp_wifi_sta_get_ap_info``.
    - Hardware related issues. Bad package capturing performance.

  When there is a bcn_timeout, the STA will try to send Probe Request for five times. If a Probe Response is received from the AP, the connection will be kept, otherwise, the STA will send a Disconnect event and the connection will fail.

--------------

[Connect] How to reconnect Wi-Fi after it disconnected?
----------------------------------------------------------------

  Call `esp_wifi_connect <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv416esp_wifi_connectv>`_ after received the ``WIFI_EVENT_STA_DISCONNECTED`` event.

--------------

[Connect] When does ESP32 disconnect from SoftAP in station mode？
----------------------------------------------------------------------------

  By default, the ESP32 will disconnect from the AP if it does not receive any beacon for 6 s. This time can be modified via `esp_wifi_set_inactive_time <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv426esp_wifi_set_inactive_time16wifi_interface_t8uint16_t>`_.

--------------

[Scan] Why does the STA cannot find any AP sometimes during the scanning?
--------------------------------------------------------------------------------------

  There are many possible reasons why ESP32 and ESP8266 cannot scan any AP, and some common reasons and solutions are listed below.

  - The AP is too far away or the signal is too weak, while Wi-Fi of ESP32 and ESP8266 can only work within a certain range. If the AP is too far away or the Wi-Fi signal is too weak, ESP32 and ESP8266 may not be able to scan the AP. You can move ESP32 or ESP8266 closer to the AP or use a signal amplifier to enhance the signal strength.
  - SSID of the AP is hidden. SSID of some APs may be hidden, so they will not be broadcasted to nearby devices. In this case, ESP32 and ESP8266 cannot scan these APs. You can connect these APs by inputting their SSID and passwords manually.
  - The AP is overloaded or malfunctioning. If the AP is overloaded or malfunctioning, it may not be able to handle new connection requests, and thus ESP32 and ESP8266 cannot connect to the AP. You can try to wait for a while and then scan the AP again.
  - ESP32 or ESP8266 has some software issues. Sometimes, software issues of ESP32 or ESP8266 may cause problems with scanning for APs. In this case, you can try to reset ESP32 or ESP8266 and restart Wi-Fi. If this method does not work, you may need to update the firmware of ESP32 or ESP8266.
  - Other reasons include wireless interference, security settings, and network configuration. These reasons may also affect Wi-Fi of ESP32 or ESP8266. In this case, you need to carefully check the Wi-Fi environment and implement corresponding settings.

--------------

[Scan] What is the maximum number of APs that can be scanned？
-------------------------------------------------------------------------

  There is no limit to the maximum number of APs that can be scanned. The number depends on how many APs are around and configurations of the scanning parameters, such as the time spent on each channel, the longer time spent on each channel the more likely it is to find all the APs.

--------------

[Scan] Can I choose to connect the best AP when there are multiple APs with identical ssid/password during the scan？
--------------------------------------------------------------------------------------------------------------------------------

  By default, the scan type is WIFI_FAST_SCAN, which makes the STA always connects the first AP during the scan. If you expect to connect the best AP, please set scan_method to WIFI_ALL_CHANNEL_SCAN and configure sort_method to determine whether to choose the AP with the strongest RSSI or connect to the most secure AP.

--------------

[Scan] How to configure scan_method in the wifi_sta_config_t structure? What is the difference between all_channel_scan and fast_scan?
-------------------------------------------------------------------------------------------------------------------------------------------------------

  all_channel_scan and fast_scan are used to find the appropriate AP before connecting. The scan_method is set to fast_scan by default, which is mainly used together with threshold to filter APs with weak signal or encryption.

  - When fast_scan is set, the STA will stop scanning once it finds the first matched AP and then connect to it, so as to save time for connection.
  - When all_channel_scan is set, the STA will scan all channels and store four APs with the best signal or the most secure encryption according to the sorting method configured in sort_method. After the scan is completed, the STA will connect one of the four APs with the best signal or the most secure encryption.

--------------

[LWIP] How to get error code of the socket?
---------------------------------------------------

  - For ESP-IDF v4.0 and later versions: use the value of `errno` directly to get the error code after the socket API returns failure.
  - For previous versions of ESP-IDF v4.0: call `getsockopt(sockfd, SOL_SOCKET, SO_ERROR, …)` to get the error code after the socket API returns failure, otherwise you may get wrong error code when multiple sockets operate simultaneously.

--------------

[LWIP] What is the default keep-alive time of TCP?
------------------------------------------------------------

  By default, a TCP keep-alive message will be sent every 75 seconds for 9 times if no TCP message is received for two consecutive hours. Then, if there is still no message received, the LWIP will disconnect from the TCP.

  The keep-alive time can be configured via socket option.

--------------

[LWIP] What is the retransmission interval of TCP？
--------------------------------------------------------

  When ESP32 acts as the sender, the initial retransmission interval of the TCP protocol is usually set to 3 seconds. If the receiver does not send an ACK message, the next retransmission interval will be determined based on the Jacobson algorithm. The retransmission interval will be exponentially increased. Specially, it will be increased by 2, 4, 8, 16, 32 seconds gradually. This retransmission interval is not fixed and you can adjust it by changing some parameters such as timeout time and the size of sliding window.

--------------

[LWIP] What is the maximum number of sockets that can be created?
-------------------------------------------------------------------------

  Up to 16, default is 10.

--------------

[Sleep] What kinds of sleeping mode does ESP32 have? What are the differences?
----------------------------------------------------------------------------------------

  - There are mainly three sleeping modes: Modem sleep, Light sleep and Deep sleep.

    - Modem sleep: the station WMM sleeping mode specified in the Wi-Fi protocol (the station sends NULL data frame to tell the AP to sleep or wake up). The Modem sleep mode is enabled automatically after the station connected to AP. After entering this mode, the RF block is disabled and the station stays connected with the AP. The Modem sleep mode will be disabled after the station disconnected from the AP. The ESP32 can also be configured to decrease the CPU's clock frequency after entering Modem sleep mode to further reduce its current.
    - Light sleep: this is a station sleep mode based on Modem sleep mode. The difference between is that, besides for the RF block being disabled, the CPU will also be suspended in this mode. After exiting from Light sleep mode, the CPU continues to operate from where it stopped.
    - Deep sleep: a sleeping mode un-specified in the Wi-Fi protocol. During Deep sleep mode, all the blocks except for RTC is disabled, and the station cannot be connected to AP. After exiting from this mode, the whole system will restart to operate (similar to system restart).

--------------

[Sleep] How can I enable the dynamic frequency scaling function for ESP32 in Modem-sleep mode?
---------------------------------------------------------------------------------------------------------------

  You can enable this function by selecting  ``menuconfig`` > ``Component Config`` > ``Power Management`` > ``Support for power management`` > ``Enable dynamic frequency scaling (DFS) at startup (NEW)``.

--------------

[Sleep] How low can the speedstep function go for ESP32 in modem sleep mode？
----------------------------------------------------------------------------------------

  For now, the CPU clock can go down to as low as 40 MHz.

--------------

[Sleep] What affects the average current of ESP32 in modem sleep mode?
---------------------------------------------------------------------------------

  The modem sleep mode of ESP32 is achieved by setting wakeup cycles. ESP32 opens RF functions to communicate during every cycle and closes these functions in the rest of the time.

  The average current of this mode is influenced by several factors, including:

  - Wakeup cycle: A shorter wakeup cycle means the chip will be waked up more frequently, which increases the average current.
  - Signal quality: If the Wi-Fi signal is weak, the chip will keep trying to reconnect or send data, which will increase the average current.  Using communication protocols with bigger transmission power will also increase the average current.
  - Hardware configuration: The hardware configuration of the chip also affects power consumption, such as the number of CPU cores, CPU clock frequency, CPU idle time ratio, power supply voltage, external crystal oscillator, etc. All of these factors influence the size of average current.
  - Other factors include whether the testing router accurately sends beacon timestamps, whether too many broadcast packets have been sent, whether peripheral modules are working, etc.

--------------

[Sleep] Why the average current measured in modem sleep mode is a bit high?
---------------------------------------------------------------------------------

  - A lot of Wi-Fi data sent and received during the test. The more data there is, the less chance there will be for entering sleeping mode and the higher average current will be.
  - The time when the router sends out beacon is not accurate. The station needs to wake up and monitor the beacon regularly, thus it will wait longer if the beacon time is not accurate. In this way, the station has less time in sleeping mode and the average current will be high.
  - There are peripheral modules working during the test. Please close them before the test.
  - The station+SoftAP mode is enabled. During modem sleep state, the current will only be lower in station-only mode.

--------------

[Sleep] Why the average current measured in light sleep mode is a bit high?
-------------------------------------------------------------------------------------

  Besides for the reasons listed in the last question, the possible reasons also could be:

  - The application layer code is running continuously, thus the CPU does not get chance to suspend.
  - The application layer has enabled ets timer or esp timer and the timeout interval is short, thus the CPU does not get chance to suspend.

--------------

[Sleep] What kinds of power-saving modes does ESP32 have? What are the differences?
---------------------------------------------------------------------------------------------------------------------------------------

  There are mainly three modes: minimum modem power-saving, maximum modem power-saving, and no power save modes.

  - Minimum modem: default type. In this mode, the station wakes up to receive beacon every DTIM period, which is equal to (DTIM * 102.4) ms. For example, if the DTIM of the router is 1, the station will wake up every 100 ms.
  - Maximum modem: in this mode, the interval to receive beacons is determined by the ``listen_interval`` parameter in ``wifi_sta_config_t``. The interval is equal to (listen interval * 102.4) ms. For example, if the DTIM of the router is 1, and the listen interval is 10, the station will wake up every 1 s.
  - No power save: no power save.

--------------

Does ESP8266 support 802.11k/v/r protocol?
---------------------------------------------------

  For now, the ESP8266 only supports 802.11k and 802.11v, please refer to example `roaming <https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/wifi/roaming>`__.

--------------

Does ESP32 Wi-Fi support roaming between different APs with the same SSID?
---------------------------------------------------------------------------

  Yes, currently it supports 802.11k and 802.11v protocols. Please refer to the example `roaming <https://github.com/espressif/esp-idf/tree/master/examples/wifi/roaming>`__.

--------------

[Connect] After the NONOS_SDK updated from version `2.1.0` to `2.2.2`, why does the connecting time become longer？
----------------------------------------------------------------------------------------------------------------------------------

  Please update to version `master`, which has solved the incompatibility issue between the CCMP encryption and some APs.

--------------

How does ESP32 receive and transmit Wi-Fi 802.11 packets?
---------------------------------------------------------------

  - By using the following APIs:

  .. code-block:: c

    esp_err_t esp_wifi_80211_tx(wifi_interface_t ifx, const void *buffer, int len, bool en_sys_seq);
    esp_wifi_set_promiscuous_rx_cb(wifi_sniffer_cb);

  - The abovementioned APIs are also used in the ESP-MDF project, please refer to `mconfig_chain <https://github.com/espressif/esp-mdf/blob/master/components/mconfig/mconfig_chain.c>`_.

--------------

[Connect] The ESP32 and ESP8266 failed to connect to router, what could be the reasons？
-----------------------------------------------------------------------------------------------

  - Please check if the SSID or password is wrong.
  - There could be errors in different Chinese codes, so it is not recommended to use an SSID written in Chinese.
  - The settings of bssid_set. If the MAC address of the router does not need to be identified, the stationConf.bssid_set should be configured to 0.
  - It is recommended to define the wifi_config field in wifi_config_t using the static variable `static`.

--------------

[Connect] What kind of networking methods does ESP8266 have？
-----------------------------------------------------------------------

  - SmartConfig mode: using SmartConfig. The device scans feature pack in sniffer mode.
  - SoftAP mode: the device enables SoftAP and sends SSID and password after the phone connects to SoftAP and set up a stable TCP/UDP connection.
  - WPS mode: an additional button should be added on the device; or using the phone to enable WPS after it connected to SoftAP.

--------------

[Connect] What are the specifications of Wi-Fi parameters when using SmartConfig?
------------------------------------------------------------------------------------------------------

  SmartConfig is a method of configuring Wi-Fi parameters via local network broadcasting. Users can send Wi-Fi account and password to the device through a matching APP. SmartConfig network configuration has some requirements on Wi-Fi parameters:

    - SSID name: Supports Chinese characters and English letters, digits, with a maximum length of 32 bytes.
    - Wi-Fi password: 8-64 digits, case-sensitive.
    - Wi-Fi security encryption: Currently, SmartConfig supports WPA, WPA2, and WEP encryption methods, and does not support open methods without encryption.

--------------

[Connect] Does ESP8266 Wi-Fi support WPA2 enterprise-level encryption？
------------------------------------------------------------------------------

  - Yes. Please refer to example `wpa2_enterprise <https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/wifi/wpa2_enterprise>`_.
  - To build RADIUS server, you can use `FreeRADIUS <https://freeradius.org/documentation/>`_.

--------------

[Connect] What are the low-power modes for ESP32 to maintain its connection to Wi-Fi?
-----------------------------------------------------------------------------------------------

  - In such scenarios, the chip switches between Active mode and Modem-sleep mode automatically, making the power consumption also varies in these two modes.
  - The ESP32 supports Wi-Fi keep-alive in Light-sleep mode, and the auto wakeup interval is determined by the DTIM parameter.
  - Please find examples in ESP-IDF - > examples - > wifi - > power_save.

--------------

Do Espressif's chips support WPA3?
-----------------------------------------

  - ESP32 series: WPA3 is supported from esp-idf release/v4.1 and enabled by default. Go to menuconfig > Component config > Wi-Fi for configuration.
  - ESP8266: WPA3 is supported from the release/v3.4 branch of ESP8266_RTOS_SDK and enabled by default. Go to menuconfig > Component config > Wi-Fi for configuration.

--------------

[Connect] How does the device choose AP when there are multiple identical SSIDs in the current environment?
----------------------------------------------------------------------------------------------------------------------

  - The device connects to the first scanned AP.
  - If you expect to sort APs by signal quality and etc., use the scan function to filter manually.
  - If you expect to connect to a specified AP, add BSSID information in connection parameters.

--------------

[Connect] Does ESP8266 have repeater solutions?
-----------------------------------------------------------

  - We have not officially released such application solutions yet.
  - For relay related applications, please find on github. The relay rates should be set basing on real tests.

--------------

What is the retransmission time for ESP32's data frame and management frame？Can this be configured？
-----------------------------------------------------------------------------------------------------------

  The retransmission time is 31 and it can not be configured.

--------------

How to customize the hostname for ESP32？
----------------------------------------------

  - Taking ESP-IDF V4.2 as an example, you can go to menuconfig > Component Config > LWIP > Local netif hostname, and type in the customized hostname.
  - There may be a slight difference on naming in different versions.

--------------

How to obtain 802.11 Wi-Fi packets？
----------------------------------------

  - Please refer to `Wireshark User Guide <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/wireshark-user-guide.html>`_ in ESP-IDF Programming Guide.
  - Please note that the wireless network interface controller (WNIC) that you use should support the Monitor mode.

--------------

Does ESP32 Wi-Fi support PMF (Protected Management Frames) and PFS (Perfect Forward Secrecy)？
-----------------------------------------------------------------------------------------------------

  The PMF is supported both in WPA2 and WPA3, and PFS is supported in WPA3.

--------------

Why does ESP8266 print out an AES PN error log when using esptouch v2?
------------------------------------------------------------------------------

  This occurs when ESP8266 has received retransmitted packets from the router for multiple times. However, this will not affect your usage.

----------------------

Does ESP32 WFA certification support multicast?
--------------------------------------------------------------------------------------------

  No. It is recommended to refer to the ASD-1148 method of testing.

---------------

When using ESP32 to establish a hotspot, can I scan all APs and the occupied channels first, and then select the smallest and cleanest channel to establish my own AP?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - You can scan all APs and occupied channels before establishing a hotspot. Refer to the API esp_wifi_scan_get_ap_records.
  - It cannot be performed automatically. You need to customize the channel selection algorithm to implement such operation.

---------------------

I'm scanning Wi-Fi on an ESP32 device using release/v3.3 version of ESP-IDF. When there are some identical SSIDs, same SSID names will show in the Wi-Fi list repeatedly. Is there an API to filter such repeated names?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  No, same SSID names cannot be filtered out since identical SSID names may not mean identical servers. Their BSSID may not be the same.

-----------------------

Does ESP8266 support EDCF (AC) scheme?
----------------------------------------------------------------------------------------------------

  The master version of ESP8266-RTOS-SDK supports EDCF (AC) applications, but no application examples are provided for now. You can enable Wi-Fi QoS configuration in ``menuconfig -> Component config -> Wi-Fi`` to get support.

---------------------

I'm using the master version of ESP8266-RTOS-SDK to open the WiFi Qos application to get EDCF support. How does ESP8266 decide which data packet should be allocated to the EDCF AC category?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  It can be determined by setting ``IPH_TOS_SET(iphdr, tos)``.

-----------------

Using ESP32, how to configure the maximum Wi-Fi transmission speed and stability without considering memory and power consumption?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  To configure the maximum Wi-Fi transmission speed and stability, please refer to `How to improve Wi-Fi performance <https://docs.espressif.com/projects/esp-idf/en/release-v4.3/esp32/api-guides/wifi.html#how-to-improve-wi-fi-performance>`_ in ESP-IDF programming guide and set the relevant configuration parameters in ``menuconfig``. The option path can be found by searching "/" in the ``menuconfig`` interface. The optimal configuration parameters need to be tested according to the actual environment.

------------------------

In Wi-Fi SoftAP mode, how many Station devices can ESP8266 be connected at most?
-------------------------------------------------------------------------------------------------------------------------------

  ESP8266 supports up to 8 Station device connections.

---------------------

How to get CSI data when using ESP32 device in Station mode?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - CSI data can be obtained by calling 'esp_wifi_set_csi_rx_cb()'. See description in `API <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv422esp_wifi_set_csi_rx_cb13wifi_csi_cb_tPv>`_.
  - For specific steps, please refer to `Espressif CSI examples <https://github.com/espressif/esp-csi>`_.

-------------------

In AP + STA mode, after an ESP32 is connected to Wi-Fi, will the Wi-Fi connection be affected if I enable or disable its AP mode?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  After an ESP32 is connected to Wi-Fi in AP + STA dual mode, AP mode can be enabled or disabled at will without affecting Wi-Fi connection.

-------------------

I'm using ESP-IDF release/v3.3 for ESP32 development, but only bluetooth function is needed, how to disable Wi-Fi function through software?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Please call ``esp_wifi_stop()`` to disable the Wi-Fi function. For API description, please see `esp_err_t esp_wifi_stop(void) <https://docs.espressif.com/projects/esp-idf/en/release-v3.3/api-reference/network/esp_wifi.html?highlight=wifi_stop#_CPPv413esp_wifi_stopv>`_.
  - If you need to reclaim the resources occupied by Wi-Fi, call ``esp_wifi_deinit()``. For API description, please see `esp_err_t esp_wifi_deinit(void) <https://docs.espressif.com/projects/esp-idf/en/release-v3.3/api-reference/ network/esp_wifi.html?highlight=wifi_deinit#_CPPv415esp_wifi_deinitv>`_.
  - Here is a simple example:

  .. code-block:: c

    #include "esp_wifi.h"
    #include "esp_bt.h"

    void app_main()
    {
      // Turn off Wi-Fi functionality
      esp_wifi_stop();

      // Initializing Bluetooth functionality
      esp_bt_controller_config_t bt_cfg = BT_CONTROLLER_INIT_CONFIG_DEFAULT();
      esp_bt_controller_init(&bt_cfg);
      esp_bt_controller_enable(ESP_BT_MODE_BTDM);

      // ...
    }

  In this example, the esp_wifi_stop() function is called to turn off Wi-Fi and then to initialize Bluetooth. It should be noted that once Wi-Fi is stopped, Wi-Fi related APIs cannot be used.


----------------------

In ESP-IDF, the ``esp_wifi_80211_tx()`` interface can only be used to send data packets, is there a corresponding function to receive packets?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Please use callback function to received data packets as follows:

  .. code-block:: c

    esp_wifi_set_promiscuous_rx_cb(wifi_sniffer_cb);
    esp_wifi_set_promiscuous(true);

  - The above data receive method is also used in another open-sourced project, please see `esp-mdf <https://github.com/espressif/esp-mdf/blob/master/components/mconfig/mconfig_chain.c>`_.

---------------

What are the reasons for the high failure rate of esptouch networking?
------------------------------------------------------------------------------------------

  :CHIP\: ESP32, ESP32S2, ESP32S3, ESP32C3, ESP8266:

  - The same hotspot is connected too many people.
  - The signal quality of the hotspot connected by cell phone is poor.
  - The router does not forward multicast data.
  - The router has enabled dual-band integration, and the phone is connected to the 5G frequency band.

----------------

How to optimize the IRAM when ESP32 uses Wi-Fi?
-----------------------------------------------------------------------------------

  You can disable ``WIFI_IRAM_OPT``, ``WIFI_RX_IRAM_OPT`` and ``LWIP_IRAM_OPTIMIZATION`` in menuconfig to optimize IRAM space, but this will degrade Wi-Fi performance.

--------------

How to test ESP32's Wi-Fi transmission distance?
-----------------------------------------------------------------------------------------------

  You can use the `iperf example <https://github.com/espressif/esp-idf/tree/master/examples/wifi/iperf>`_ and configure the ESP32 device to iperf UDP mode. Then, you can distance the device continuously to see at which point the Wi-Fi data transmission rate will drop to 0.

---------------------

What is the maximum length of Wi-Fi MTU for an ESP32 and how to change it?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The maximum Wi-Fi MTU length for ESP32 is 1500. You can change this value in the LwIP component by ``netif`` > ``mtu``. However, it is not recommended to change this value.

---------------

During the on-hook test for an ESP32 device, the following log shows. What does it mean?
--------------------------------------------------------------------------------------------

  log：

  .. code-block:: text

    [21-01-27_14:53:56]I (81447377) wifi:new:<7,0>, old:<7,2>, ap:<255,255>, sta:<7,0>, prof:1
    [21-01-27_14:53:57]I (81448397) wifi:new:<7,2>, old:<7,0>, ap:<255,255>, sta:<7,2>, prof:1
    [21-01-27_14:53:58]I (81449417) wifi:new:<7,0>, old:<7,2>, ap:<255,255>, sta:<7,0>, prof:1
    [21-01-27_14:53:59]I (81450337) wifi:new:<7,2>, old:<7,0>, ap:<255,255>, sta:<7,2>, prof:1

  - The value after ``new`` represents the current primary and secondary channel; the value after ``old`` represents the last primary and secondary channel; and the value after ``ap`` represents the primary and secondary channel of the current ESP32 AP, which will be 255 if softAP is not enabled; the value after ``sta`` represents primary and secondary channel of the current ESP32 sta; and ``prof`` is the channel of ESP32's softAP stored in NVS.
  - For the numerical values represented by the secondary channel, please refer to `wifi_second_chan_t <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv420esp_wifi_set_channel7uint8_t18wifi_second_chan_t>`__.
  - The above log indicates that router is switching between HT20 and HT40 minus. You can check the Wi-Fi bandwidth setting of the router.

-----------------

How to disable AP mode when ESP32 is in AP + STA mode?
-------------------------------------------------------------------------------------------------------------------------------------

  - This can be done through the configuration of ``esp_wifi_set_mode(wifi_mode_t mode);`` function.
  - Just call ``esp_wifi_set_mode(WIFI_MODE_STA);``.

----------------

After ESP32 used the Wi-Fi function, are all ADC2 channels unavailable?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  When an ESP32 device is using Wi-Fi function, the ADC2 pins that are not occupied by Wi-Fi can be used as normal GPIOs. You can refer to the official `ADC Description <https://docs.espressif.com/projects/esp-idf/en/v4.4.2/esp32/api-reference/peripherals/adc.html#analog-to-digital-converter-adc>`_.

-----------------------------------------------------------------------------------------------------

How do I set the country code for a Wi-Fi module ?
-----------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP8266 | ESP32 | ESP32 | ESP32-C3:

  Please call `esp_wifi_set_country <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html? highlight=esp_wifi_set_country#_CPPv420esp_wifi_set_countryPK14wifi_country_t>`_ to set the country code.

---------------

When using ESP32 as a SoftAP and have it connected to an Iphone, a warning prompts as "low security WPA/WPA2(TKIP) is not secure. If this is your wireless LAN, please configure the router to use WPA2(AES) or WPA3 security type", how to solve it?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  :IDF\: release/v4.0 and above:

  - You can refer to the following code snippet:

    .. code-block:: c

      wifi_config_t wifi_config = {
          .ap = {
              .ssid = EXAMPLE_ESP_WIFI_SSID,
              .ssid_len = strlen(EXAMPLE_ESP_WIFI_SSID),
              .channel = EXAMPLE_ESP_WIFI_CHANNEL,
              .password = EXAMPLE_ESP_WIFI_PASS,
              .max_connection = EXAMPLE_MAX_STA_CONN,
              .authmode = WIFI_AUTH_WPA2_PSK,
              .pairwise_cipher = WIFI_CIPHER_TYPE_CCMP
          },
      };

  - WIFI_AUTH_WPA2_PSK is AES, also called CCMP. WIFI_AUTH_WPA_PSK is TKIP. WIFI_AUTH_WPA_WPA2_PSK is TKIP+CCMP.

---------------

Since ESP32's Wi-Fi module only supports 2.4 GHz of bandwidth, can Wi-Fi networking succeed when using a multi-frequency router with both 2.4 GHz and 5 GHz of bandwidth？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Please set your router to multi-frequency mode (can support 2.4 GHz and 5 GHz for one Wi-Fi account), and the ESP32 device can connect to Wi-Fi normally.

---------------

How to obtain the RSSI of the station connected when ESP32 is used in AP mode?
-------------------------------------------------------------------------------------

  - You can call API `esp_wifi_ap_get_sta_list <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html?highlight=esp_wifi_ap_get_sta_list#_CPPv424esp_wifi_ap_get_sta_listP15wifi_sta_list_t>`_, please refer to the following code snippet:

    .. code-block:: c

      {
          wifi_sta_list_t wifi_sta_list;
          esp_wifi_ap_get_sta_list(&wifi_sta_list);
          for (int i = 0; i < wifi_sta_list.num; i++) {
              printf("mac address: %02x:%02x:%02x:%02x:%02x:%02x\t rssi:%d\n",wifi_sta_list.sta[i].mac[0], wifi_sta_list.sta[i].mac[1],wifi_sta_list.sta[i].mac[2],
                        wifi_sta_list.sta[i].mac[3],wifi_sta_list.sta[i].mac[4],wifi_sta_list.sta[i].mac[5],wifi_sta_list.sta[i].rssi);
          }
      }

  - The RSSI obtained by ``esp_wifi_ap_get_sta_list`` is the average value over a period of time, not real-time RSSI. The previous RSSI has a weight of 13, and the new RSSI has a weight of 3. The RSSI is updated when it is or larger than 100ms, the old rssi_arg is used when updating as: ``rssi_avg = rssi_avg*13/16 + new_rssi * 3/16``.

---------------

Does ESP32 support FTM(Fine Timing Measurement)?
-------------------------------------------------------------------------------

  - No, it doesn't. FTM needs hardware support, but ESP32 doesn't have it.
  - ESP32-S2 and ESP32-C3 can support FTM in hardware.
  - ESP-IDF can support FTM from v4.3-beta1.
  - For more information and examples of FTM, please refer to `FTM <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/api-guides/wifi.html#fine-timing-measurement-ftm>`_.

---------------

When ESP32 is in STA+AP mode, how to specify whether using STA or AP interface to send data?
------------------------------------------------------------------------------------------------------

  **Background:**

  The default network segment of ESP32 as AP is 192.168.4.x, and the network segment of the router to which ESP32 as STA is connected is also 192.168.4.x. The PC connects to the ESP32 AP and creates a tcp server. In this case, the tcp connection between ESP32 as tcp client and PC as tcp server cannot be established successfully.

  **Solutions:**

  - It is possible for ESP32 to specify whether to use STA or AP interface for data transmission. Please see example `tcp_client_multi_net <https://github.com/espressif/esp-idf/tree/master/examples/protocols/sockets/tcp_client_multi_net>`_, in which both ethernet and station interface are used and each can be specified for data transmission.
  - There are two ways to bind socket to an interface:

    - use netif name (use socket option SO_BINDTODEVICE)
    - use netif local IP address (get IP address of an interface via esp_netif_get_ip_info(), then call bind())

.. note::

  - The tcp connection between ESP32 and PC can be established when an ESP32 is bound to the STA interface, while the connection cannot be established when it is bound to the AP interface.
  - By default, the tcp connection between ESP32 and mobile phone can be established(the mobile phone as a station is connected to ESP32).

---------------------------------------------------------------------------------------

ESP8266 `wpa2_enterprise <https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/wifi/wpa2_enterprise>`_ How to enable Wi-Fi debugging function?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Open menuconfig via ``idf.py menuconfig`` and configure the following parameters:

    .. code-block:: c

      menuconfig==>Component config ==>Wi-Fi ==>
      [*]Enable WiFi debug log ==>The DEBUG level is enabled (Verbose)
      [*]WiFi debug log submodule
      [*] scan
      [*] NET80211
      [*] wpa
      [*] wpa2_enterprise

      menuconfig==>Component config ==>Supplicant ==>
      [*] Print debug messages from WPA Supplicant

-----------------------------------------------------------------------------------------------------

Is there a standard for the number of Wi-Fi signal frames?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP8266 | ESP32 | ESP32 | ESP32-C3:

  There is no such standard for now. You can do the calculation by yourself based on the received RSSI. For example, if the received RSSI range is [0,-96], and the required signal strength is 5, then [0~-20] is the full signal, and so on.

--------------

What is the current progress of WFA bugs fixing?
--------------------------------------------------------------------------------------------
  :CHIP\: ESP32 | ESP32-S2 | ESP32-C3 |  ESP8266:

  For more details, please refer to the `Wi-Fi Security Notice <https://www.espressif.com/sites/default/files/advisory_downloads/AR2021-003%20Security%20Advisory%20for%20WFA%20vulnerability%20EN_0.pdf>`_ on the Espressif official website.

-----------------------------------------------------------------------------------------------------

When Wi-Fi connection failed, what does the error code mean?
---------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32:

  - Any error occurred during the Wi-Fi connection will cause it coming to init status, and there will be a hexadecimal number in the log, e.g., ``wifi:state, auth-> init(200)``. The first two digits indicate error reasons while the last two digits indicate the type code of the received or transmitted management frame. Common frame type codes are 00 (received nothing, timeout), A0 (disassoc), B0 (auth) and C0 (deauth).
  - Error reasons indicated by the first two digits can be found in `Wi-Fi Reason Code <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/wifi.html#wi-fi-reason-code>`__. The last two digits can be checked in frame management code directly.

---------------------

When using ESP32's Release/v3.3 of SDK to download the Station example, the device cannot be connected to an unencrypted Wi-Fi. What is the reason?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - In the example, it is by default to connect to an encrypted AP as:

    .. code-block:: c

      .threshold.authmode = WIFI_AUTH_WPA2_PSK,

  - If you need connect to an unencrypted AP, please set the following parameter to 0:

    .. code-block:: c

      .threshold.authmode = 0,

  - For AP mode selection instructions, please refer to `esp_wifi_types <https://github.com/espressif/esp-idf/blob/release/v3.3/components/esp32/include/esp_wifi_types.h>`_.

------------------

What is the maximum PHY rate of Wi-Fi communication of ESP32-S2 chip?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The theoretical maximum PHY rate of ESP32-S2 Wi-Fi communication is 150 Mbps.

------------------------------------------------------------------------------------------------------------------------------------------------------

Does ESP modules support EAP-FAST?
-------------------------------------------------------------------------------------------------------------------------------------
  :CHIP\: ESP32 | ESP32-S2 | ESP32-C3 :

  Yes, please refer to `wifi_eap_fast <https://github.com/espressif/esp-idf/tree/master/examples/wifi/wifi_eap_fast>`_ demo.

---------------

Does ESP modules support the WiFi NAN (Neighbor Awareness Networking) protocol?
---------------------------------------------------------------------------------------------
  :CHIP\: ESP8266 | ESP32 | ESP32-C3 | ESP32-S2 | ESP32-S3:

  No.

---------------------

When using ESP32 with release/v3.3 version of ESP-IDF. When configuring the router, is there an API to directly tell that the entered password is wrong?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - There is no such API. According to the Wi-Fi protocol standard, when the password is wrong, the router will not clearly tell the Station that the 4-way handshake is due to the password error. Under normal circumstances, the password is obtained in 4 packets (1/4 frame, 2/4 frame, 3/4 frame, 4/4 frame). When the password is correct, the AP will send 3/4 frames, but when the password is wrong, the AP will not send 3/4 frame but send 1/4 frame instead. However, when the AP sends 3/4 frame which is lost in the air for some reason, the AP will also re-send 1/4 frame. Therefore, for Station, it is impossible to accurately distinguish between these two situations. In the end, it will report a 204 error or a 14 error.
  - Please refer to `Wi-Fi reason code <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/wifi.html#wi-fi-reason-code>`__.

-----------------------

When testing the Station example of ESP32 base on v4.4 version of ESP-IDF, how to support WPA3 encryption mode?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Open ``menuconfig → Component config → Wi-Fi → Enable WPA3-Personal`` configuration;
  - Set ``capable = true`` in ``pmf_cfg`` in the application code;
  - Please refer to `Wi-Fi Security <https://docs.espressif.com/projects/esp-idf/en/release-v4.4/esp32/api-guides/wifi-security.html#wi-fi-security>`_ for more descriptions.

--------------

How does ESP32 speed up the Wi-Fi connection?
--------------------------------------------------------------------------------

  You can try the following approaches:

  - Set the CPU frequency to the maximum to speed up the key calculation speed. In addition, you can also set the flash parameters to ``QIO, 80MHz``, which will increase power consumption.
  - Disable ``CONFIG_LWIP_DHCP_DOES_ARP_CHECK`` to greatly reduce the time of getting IP. But there will be no checking on whether there is an IP address conflict in the LAN.
  - Open ``CONFIG_LWIP_DHCP_RESTORE_LAST_IP``, and save the IP address obtained last time. When DHCP starts, send DHCP requests directly without performing DHCP discover.
  - Use fixed scanning channel.

---------------------

Does ESP32 WPA2 Enterprise Authentication support Cisco CCKM mode?
-----------------------------------------------------------------------------------------------------

  This mode is currently not supported, even though the enumeration in esp_wifi_driver.h has WPA2_AUTH_CCKM.

--------------------------------------------------------------------------------------------------

Using wpa2_enterprise (EAP-TLS method), what is the maximum length supported for client certificates?
-----------------------------------------------------------------------------------------------------------------------------------------------------------

  Up to 4 KB.

------------------------

Does ESP8089 support Wi-Fi Direct mode?
------------------------------------------------------------------------------------------------------------

  Yes, but ESP8089 can only use the default fixed firmware and cannot be used for secondary development.

--------------

How does ESP32 connect to an AP whose RSSI does not fall below the configured threshold when there are multiple APs in the environment?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  In ESP32 staion mode, there is a `wifi_sta_config_t <https://docs.espressif.com/projects/esp-idf/en/release-v4.1/api-reference/network/esp_wifi.html#_CPPv4N13wifi_config_t3staE>`_ structure with 2 variables underneath, i.e., `sort_method <https://docs.espressif.com/projects/esp-idf/en/release-v4.1/api-reference/network/esp_wifi.html#_CPPv4N17wifi_sta_config_t11sort_methodE>`_ and `threshold <https://docs.espressif.com/projects/esp-idf/en/release-v4.1/api-reference/network/esp_wifi.html#_CPPv4N17wifi_sta_config_t9thresholdE>`_. The RSSI threshold is configured by assigning values to these two variables.

--------------

ESP32 Wi-Fi has a beacon lost and sends 5 probe requests to the AP after 6 seconds. If the AP does not respond, disconnection will be caused. Can this 6 seconds be configured?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Use API `esp_wifi_set_inactive_time <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv426esp_wifi_set_inactive_time16wifi_interface_t8uint16_t>`__ to configure the time.

--------------

Does ESP32 Wi-Fi work with PSRAM?
------------------------------------------------------------------------------------------------------

  For information on using Wi-Fi with PSRAM, please refer to `Using PSRAM <https://docs.espressif.com/projects/esp-idf/en/v4.4.1/esp32/api-guides/wifi.html#using-psram>`_.

-----------------

[Connect] How to troubleshoot the issue that ESP32 series of products cannot connect to the router over Wi-Fi from the hardware and software aspects?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Please follow the steps below to troubleshoot the issue:

  - Firstly, use the `Wi-Fi error code <https://docs.espressif.com/projects/espressif-esp-faq/en/latest/software-framework/wifi.html#connect-while-esp32-connecting-wi-fi-how-can-i-determine-the-reason-of-failure-by-error-codes>`_ to determine the possible cause for the failure.
  - Then, try connecting another device, such as a phone, to the router to determine whether this is a problem with the router or ESP32.

    - If the phone cannot connect to the router either, please check if there is any problem with the router.
    - If it can, please check whether there is any issue with ESP32.

  - Steps to troubleshoot router issues:

    - Check whether the router is in the stage of power off and rebooting. In this stage, the router cannot be connected. Please do not connect to it until it is initialized.
    - Check whether the configured SSID and PASSWORD are consistent with those of the router.
    - Check whether the router can be connected after being configured in OPEN mode.
    - Check whether the router can connect to other routers.

  - Steps to troubleshoot ESP32 issues:

    - Troubleshoot the ESP32 hardware:

      - Check whether the issue occurs only in a specific ESP32. If it occurs in a small number of specific ESP32 devices, identify how likely the issue is to occur and compare the hardware differences between them and regular ESP32 devices.

    - Troubleshoot the ESP32 software:

      - Check whether the Wi-Fi connection works using the `station example <https://github.com/espressif/esp-idf/tree/v4.4.1/examples/wifi/getting_started/station>`_ in ESP-IDF. The example has a reconnecting mechanism by default, so please watch if ESP32 can connect to Wi-Fi as it is trying reconnecting.
      - Check whether the configured SSID and PASSWORD are consistent with those of the router.
      - Check whether ESP32 can connect to the router when the router is configured in OPEN mode.
      - Check whether ESP32 can connect to Wi-Fi after calling the API ``esp_wifi_set_ps(WIFI_PS_NONE)`` additionally before executing the code for connecting to Wi-Fi.

  - If all the above steps still fail to locate the issue, please capture Wi-Fi packets for further analysis by referring to `Espressif Wireshark User Guide <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/wireshark-user-guide.html>`_.

-----------------

After being connected to the router, ESP32 prints ``W (798209) wifi:<ba-add>idx:0 (ifx:0, f0:2f:74:9b:20:78), tid:0, ssn:154, winSize:64`` and ``W (798216) wifi:<ba-del>idx`` several times every 5 minutes and consumes much more power. Why?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - This log does not indicate any issue. It is related to the Wi-Fi block acknowledgment mechanism. ``ba-add`` means the ESP32 received an add block acknowledgment request frame from the router. ``ba-del`` means the ESP32 received a delete block acknowledgment request frame from the router. Frequent printing of this log suggests that the router has been sending packets.
  - If this log is printed periodically every five minutes, it may indicate that the router is updating the group secret key. You could double-check it according to the following steps:

    - Print log in `wpa_supplicant_process_1_of_2() <https://github.com/espressif/esp-idf/blob/v4.4.1/components/wpa_supplicant/src/rsn_supp/wpa.c#L1519>`_ to check if this function is called every 5 minutes when the group key is updated every 5 minutes.
    - In the router's Wi-Fi configuration interface, check if there is the ``Group Key Update Time`` option and it is set to 5 minutes.

-------------------

Why can't ESP32 keep the Wi-Fi sending rate at a fixed value with the function `esp_wifi_config_80211_tx_rate() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv429esp_wifi_config_80211_tx_rate16wifi_interface_t15wifi_phy_rate_t>`_ to maintain stable transmission?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - `esp_wifi_config_80211_tx_rate() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv429esp_wifi_config_80211_tx_rate16wifi_interface_t15wifi_phy_rate_t>`_ is used to configure the sending rate of `esp_wifi_80211_tx() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv417esp_wifi_80211_tx16wifi_interface_tPKvib>`_.
  - To set and fix the Wi-Fi sending rate, use the function `esp_wifi_internal_set_fix_rate <https://github.com/espressif/esp-idf/blob/v4.4.1/components/esp_wifi/include/esp_private/wifi.h#L267>`_.

-----------------

How do I debug the ESP32 station that is connected to a router but does not get an IP properly?
------------------------------------------------------------------------------------------------------------------------------------------------------

  - Open the debug log of DHCP in lwIP, go to ESP-IDF menuconfig, and configure ``Component config`` > ``LWIP`` > ``Enable LWIP Debug(Y)`` and ``Component config -> LWIP`` > ``Enable DHCP debug messages(Y)``.
  - Earlier IDF versions do not have the above options, so please refer to `lwipopts.h <https://github.com/espressif/esp-idf/blob/v4.0.1/components/lwip/port/esp32/include/lwipopts.h>`_ line 806 and 807, to change ``LWIP_DBG_OFF`` to ``LWIP_DBG_ON`` in both lines of code as follows.

    .. code-block:: c

      #define DHCP_DEBUG LWIP_DBG_ON
      #define LWIP_DEBUG LWIP_DBG_ON

-----------------

When ESP32 works as a softAP, the station connected to it does not get the IP. How to debug?
--------------------------------------------------------------------------------------------------------------------------------------------------------

  To open the debug log of DHCP in lwIP for debugging, please go to `dhcpserver.c <https://github.com/espressif/esp-idf/blob/v4.0.1/components/lwip/apps/dhcpserver/dhcpserver.c#L63>`_ and change ``#define DHCPS_DEBUG 0`` to ``#define DHCPS_DEBUG 1``.

-----------------

In ESP-IDF menuconfig, after ``Component config`` > ``PHY`` > ``Max Wi-Fi TX power(dBm)`` is configured to adjust the Wi-Fi transmit power, what is the actual power? For example, what is the actual maximum transmit power when the option is configured to 17 dBm?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - For ESP32, the actual maximum transmit power in the example is 16 dBm. For the mapping rules, please refer to the function `esp_wifi_set_max_tx_power() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv425esp_wifi_set_max_tx_power6int8_t>`_.
  - For ESP32-C3, the maximum transmit power value configured in menuconfig is the actual maximum power value.

-----------------

ESP-IDF currently supports connecting to Chinese SSID routers with UTF-8 encoding. Is there a way to connect to Chinese SSID routers with GB2312 encoding?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Yes, please keep the encoding method of the ESP device consistent with that of the router. In this case, make the ESP device also use the GB2312-based Chinese SSID.

-----------------

After connecting to the router, ESP32 consumes much power in an idle state, with an average current of about 60 mA. How to troubleshoot the issue?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Please capture Wi-Fi packets for further analysis. See `espressif Wireshark User Guide <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/wireshark-user-guide.html>`_. After the packets are captured, check whether the NULL data packet sent by the device contains ``NULL(1)``. If ``NULL(1)`` is sent every 10 seconds, it means that ESP32 is interacting with the router in keepalive mode.
  - You can also check the ``TIM(Traffic Indication Map)`` field of the beacon packet in the captured packets. If ``Traffic Indication`` is equal to 1, it means Group Frames Buffered. In this case, ESP32 will turn on RF, resulting in higher power consumption.

-----------------

How to configure the Wi-Fi country code when the ESP end product needs to be sold worldwide?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Different Wi-Fi country codes need to be set for different countries.
  - The default country code configuration can be used for most countries, but it is not compatible with some special cases. The default country code is ``CHINA {.cc="CN", .schan=1, .nchan=13, policy=WIFI_COUNTRY_POLICY_AUTO}``. While in the ESP-IDF v5.0 or later version, the dafualt one has been changed to ``"01" (world safe mode) {.cc="01", .schan=1, .nchan=11, .policy=WIFI_COUNTRY_POLICY_AUTO}）``. Since channels 12 and 13 are passively scanned by default, they do not violate the regulations of most countries. Besides, the country code of the ESP product is automatically adapted to the router that it is connected to. When disconnected from the router, it automatically goes back to the default country code.

  .. note::

    - There is a potential issue. If the router hides the SSID and is on channel 12 or 13, the ESP end product can not scan the router. In this case, you need to set ``policy=WIFI_COUNTRY_POLICY_MANUAL`` to enable ESP end products to actively scan on channels 12 and 13.
    - Some countries, such as Japan, support channels 1-14, and channel 14 only supports 802.11b. ESP end products cannot connect to routers on channel 14 by default.

-----------------

Sometimes the rate drops or even a disconnection occurs after a period of iperf testing. What is the reason and how to solve it?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Possible reasons:

    - Bad network environment.
    - Incompatibility between the computer or mobile phone and the ESP32-S2 or ESP32-S3 softAP.
    - Modem-sleep affects throughput. In earlier IDF version before v5.1, it is recommended to manually disable Modem-sleep when conducting iperf testing.

  - Solutions:

    - In the case of a bad network environment, change the network environment or test in a shielded box.
    - In the case of incompatibility, disable ``menuconfig`` > ``Component config`` > ``Wi-Fi`` > ``WiFi AMPDU RX``. If disconnections occur again, disable ``menuconfig`` > ``Component config`` > ``Wi-Fi`` > ``WiFi AMPDU TX``.
    - In the case of Modem-sleep, disable Modem-sleep by ``esp_wifi_set_ps(WIFI_PS_NONE)``.

  .. note::

    - AMPDU stands for Aggregated MAC Protocol Data Unit and is a technique used in the IEEE 802.11n standard to increase network throughput.
    - When ``WiFi AMPDU RX`` is disabled, the device will not receive AMPDU packets, which will affect the RX performance of the device.
    - When ``WiFi AMPDU TX`` is disabled, the device will not send AMPDU packets, which will affect the TX performance of the device.

---------------

Why is this log frequently printed when the phone connects to the ESP32-S3 that works as the Wi-Fi AP based on the ESP-IDF v5.0 SDK?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    พ (13964) wifi:<ba-del>idx
    ฟ (13964) wifi:<ba-add>idx:2 (ifx:1, 48:2c:a0:7b:4e:ba), tid:0, ssn:5, winSize:64

  This is because A-MPDU is created and deleted all the time. The printing is only auxiliary and does not affect communication. If you need to hide this log, add the following code before the Wi-Fi initialization code.

  .. code-block:: c

    esp_log_level_set("wifi", ESP_LOG_ERROR);

--------------

Does ESP32 support the coexistence of the network port (LAN8720) and Wi-Fi (Wifi-AP)?
-------------------------------------------------------------------------------------------------------

  Yes, this can be achieved by writing the detection events of both connections as one.

-----------------

How can I optimize ESP32's slow IP address acquisition after Wi-Fi is connected in a weak network environment or interference environment?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - You can disable Modem-sleep using `esp_wifi_set_ps(WIFI_PS_NONE);` after Wi-Fi start, and enable Modem-sleep after getting the event `IP_EVENT_STA_GOT_IP`.
  - For the situation of reconnection after disconnection, you can manually disable Modem-sleep before connection, and enable it after getting the event `IP_EVENT_STA_GOT_IP`.
  - Note: This optimization is not applicable for Wi-Fi/BT coexistence scenarios.

-----------------

When ESP32/ESP32-S2/ESP32-S3 series chips work in SoftAP mode, they are susceptible to disconnect from mobile phones and PCs of other manufacturers when they are communicating with each other. How can I optimize this situation?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - It is recommended to turn off ``WiFi AMPDU RX`` and ``WiFi AMPDU TX`` options in menuconfig.
  - You can further confirm the cause by packet capture.

---------------

What is the value range of ESP32 Wi-Fi TX power?
------------------------------------------------------------------------------------------------------------

  - It ranges from 2 to 20 dBm. In ESP-IDF, you can use ``esp_wifi_set_max_tx_power()`` to set the maximum of TX power, and use ``esp_wifi_get_max_tx_power()`` to the get the maximal TX power supported by the system.
  - It should be noted that setting TX power too high may affect system stability and battery life, and may also violate wireless regulations in some countries and regions, so it should be used with caution. For more details, please refer to `esp_wifi_set_max_tx_power() API <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv425esp_wifi_set_max_tx_power6int8_t>`__.

--------------

How do I get Wi-Fi RSSI when using ESP32?
------------------------------------------------------------------------------------------------------------

  When using ESP32 as a station in ESP-IDF release/v4.1, you can use the following code example to obtain the RSSI of the connected AP:

  .. code-block:: c

    wifi_ap_record_t ap_info;
    if (esp_wifi_sta_get_ap_info(&ap_info) == ESP_OK) {
      int rssi = ap_info.rssi;
      // handle rssi
    }

  The ``wifi_ap_record_t`` structure contains information about the connected AP, including SSID, BSSID, channel, and encryption type. The RSSI field represents the RSSI value of the AP. Call ``esp_wifi_sta_get_ap_info()`` to get the information of this structure.
  For details of the API, please refer to `esp_err_t esp_wifi_sta_get_ap_info(wifi_ap_record_t *ap_info) <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv424esp_wifi_sta_get_ap_infoP16wifi_ap_record_t>`_.

--------------

Does ESP32 support WPA3-Enterprise?
------------------------------------------------------------------------------------------------------------

  - ESP32 supports WPA/WPA2/WPA3/WPA2-Enterprise/WPA3-Enterprise/WAPI/WPS and DPP. For more details, please refer to `ESP32 Wi-Fi Feature List <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/wifi.html#esp32-wi-fi-feature-list>`__.
  - esp-idf release/v5.0 has provided `wifi_enterprise example <https://github.com/espressif/esp-idf/tree/v5.0/examples/wifi/wifi_enterprise>`__, which supports setting WPA3-Enterprise mode for testing. You can configure it as following: ``idf.py menuconfig`` > ``Example Configuration`` > ``Enterprise configuration to be used`` > ``WPA3_ENT``.

---------------

Does ESP modules support WAPI (Wireless LAN Authentication and Privacy Infrastructure)?
---------------------------------------------------------------------------------------------------------------------------------

  Supported, please refer to the `Wi-Fi Feature List <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/wifi.html#esp32-wi-fi-feature-list>`__.

-----------

How can I increase the time for scanning routers when using ESP32 as the Wi-Fi Station to connect routers?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - In ESP32, by defualt, channels 1 ~ 11 are active scanning, while channels 12 ~ 13 are passive scanning. Active and passive scanning require different amounts of time. For more details, please refer to `Wi-Fi scan configuration <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/wifi.html#scan-configuration>`_. The default duration for active scanning is 120 ms per channel, while for passive scanning, it is 360 ms per channel. You can call the following function before calling ``esp_wifi_start()`` to increase the time for scanning routers:

  .. code-block:: c

      extern void scan_set_act_duration(uint32_t min, uint32_t max);
      extern void scan_set_pas_duration(uint32_t time);
      scan_set_act_duration(50, 500);
      scan_set_pas_duration(500);

  - Or you can modify the active scanning time and passive scanning time by changing related parameters in the structure ``wifi_ap_record_t``.

  .. note::

    - A typical beacon interval is 102.4 ms, so it is recommended to set the active scanning time bigger than this value, which should be at least 120 ms.
    
-------------

Does ESP32 support LDPC?
---------------------------------------------------------------------------------------------------------------

  Yes. No additional configuration or calling is required as it is already implemented in the driver.

-------------

Does the ESP module support WAPI AS?
---------------------------------------------------------------------------------------------------------------

  Not supported. WAPI has two authentication methods, i.e., certificate authentication and pre-shared key authentication. Currently, the ESP module only supports pre-shared key authentication (WAPI-PSK), while WAPI AS is used for certificate authentication.

-------------

When encountering the error message ``Error occurred during sending: errno 12`` during UDP transmission testing, what should I do to resolve it?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - errno 12 indicates insufficient space. This issue occurs when there is a mismatch in processing speed between the upper and lower layers. The upper-layer application continuously generates a large amount of data and sends it to the UDP protocol for transmission. However, the underlying network or the receiving end cannot keep up with the sending speed, resulting in insufficient space.
  - To address this problem, you can handle this return value by implementing appropriate measures. For example, upon receiving this return value, the upper layer can initiate a resend mechanism or introduce a delay to slow down the sending speed.

---------------

Does the ESP module support Wi-Fi HaLow functionality?
------------------------------------------------------------------------------------------------------------------

  No, Wi-Fi HaLow is based on the 802.11ah protocol.

--------------

How to prevent any radio frequency waves from being sent in ESP32 Wi-Fi Scan mode?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Use the `esp_wifi_scan_start() <https://docs.espressif.com/projects/esp-idf/en/release-v5.2/esp32/api-reference/network/esp_wifi.html?highlight=wifi_scan#_CPPv419esp_wifi_scan_startPK18wifi_scan_config_tb>`_ API to set ESP32 to passive scan mode `WIFI_SCAN_TYPE_PASSIVE <https://docs.espressif.com/projects/esp-idf/en/release-v5.2/esp32/api-reference/network/esp_wifi.html?highlight=wifi_scan#_CPPv4N16wifi_scan_type_t22WIFI_SCAN_TYPE_PASSIVEE>`_.

-------------

What is the default 802.11 Wi-Fi protocol when the ESP32-C6 is in Wi-Fi AP mode?
----------------------------------------------------------------------------------------------------------------------------------------------

  - When ESP32-C6 enables Wi-Fi AP mode, it uses the mixed mode of 802.11b/g/n by default. The protocol can be set via `esp_wifi_set_protocol() <https://docs.espressif.com/projects/esp-idf/en/v5.1.2/esp32c6/api-reference/network/esp_wifi.html#_CPPv421esp_wifi_set_protocol16wifi_interface_t7uint8_t>`_.

-------------------

Why can't the ESP32 Wi-Fi Station connect to a Wi-Fi hotspot in 2.4 GHz Enhanced Open mode?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Connection to 2.4 GHz Wi-Fi hotspots in Enhanced Open mode is only supported on ESP-IDF  release/v5.2 and above. Additionally, the ``Component config > ``Wi-Fi`` > ``Enable OWE STA`` configuration option should be enabled. For more information, please refer to the `Wi-Fi Enhanced Open <https://github.com/espressif/esp-idf/blob/release/v5.2/docs/en/api-guides/wifi-security.rst#wi-fi-enhanced-open>`_ guide.

--------------

How to determine whether the connected Wi-Fi applies Wi-Fi 4 or Wi-Fi 6？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - You can use `esp_wifi_sta_get_negotiated_phymode(wifi_phy_mode_t *phymode) <https://github.com/espressif/esp-idf/blob/5f4249357372f209fdd57288265741aaba21a2b1/components/esp_wifi/include/esp_wifi.h#L1454>`__ to obtian the mode of the current connected station. Here is an example:
    
  .. code-block:: c

      wifi_phy_mode_t phymode;
      esp_wifi_sta_get_negotiated_phymode(&phymode);
      printf("111=%d\n",phymode);
  
  - If the printed value is 3, it indicates the connection with the station applies Wi-Fi 4. If the printed value is 5, it indicates the connection is based on Wi-Fi 6.

--------------

Does ESP32-S3 support AP and STA working simultaneously?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
  - Yes. Please refer to the example `softap_sta <https://github.com/espressif/esp-idf/tree/v5.2/examples/wifi/softap_sta>`_.

--------------

Does the ESP Wi-Fi module support power save mode in SoftAp mode?
------------------------------------------------------------------------------------------------------------------------------------
 
  This feature is currently not supported.

--------------

What is the maximum ranging bandwidth supported by ESP32S3 FTM?
----------------------------------------------------------------------------------------------------------------------------------------
  
  ESP32S3 FTM supports maximum ranging bandwidth up to 40 MHz.

--------------

Do ESP chips support one STA conducting FTM with multiple APs at the same time?
------------------------------------------------------------------------------------------------------------------------------------
 
  Not supported. STA can only perform FTM with one AP at a time.

-------------

In WiFi Station mode, which WiFi mode will ESP32-C6 use to establish a connection with the router when both WiFi 4 and WiFi 6 modes are enabled on the router?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ESP32-C6 will prioritize establishing a connection with the router using WiFi 6.

-----------------

In WiFi AP mode, how many WiFi Station devices can ESP32-C2 series products support at most?
-------------------------------------------------------------------------------------------------------------------------------------------------

  - Due to hardware limitations, ESP32-C2 can support up to four WiFi Station connections in WiFi AP mode.
  - The maximum number of connections supported in WiFi AP mode varies between different chips. For details, please refer to `esp-idf/components/esp_wifi/include/esp_wifi_types.h <https://github.com/espressif/esp-idf/blob/a322e6bdad4b6675d4597fb2722eea2851ba88cb/components/esp_wifi/include/esp_wifi_types.h#L379>`_.

---------------

Does ESP32 support WPA3 WiFi AP mode?
-----------------------------------------------------------------------------------------------------------------------

  Yes. ESP-IDF v5.1 and above support WPA3 WiFi AP mode. Please refer to the description in `ESP-IDF v5.1 Release <https://github.com/espressif/esp-idf/releases/tag/v5.1>`_.

---------------

Do ESP chips support Short GI in SoftAP mode?
------------------------------------------------------------------------------------------------------------------------------------
 
  This feature is currently not supported.

---------------

Do STA and AP need to establish a connection first before executing FTM?
-----------------------------------------------------------------------------------------------------------------

  No connection establishment is required, and the STA can directly initiate FTM through the AP. It is recommended to scan the AP first to confirm whether it supports FTM Responder mode. For specific operations, you can refer to the `FTM example <https://github.com/espressif/esp-idf/tree/master/examples/wifi/ftm>`_ in the esp-idf/wifi directory.

---------------

Do ESP chips support uAPSD in SoftAP mode?
------------------------------------------------------------------------------------------------------------------------------------
 
  uAPSD is a Wi-Fi capability that provides more power consumption savings on the client, in low periodic latency-sensitive traffic modes (such as VoIP). ESP chips currently do not support this feature.

-----------------

When enabling WiFi AP mode on products based on Espressif series, is it possible to set up automatic channels?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Espressif series products use the WiFi SoftAP mode, which does not support automatic channel settings.

-------------

Do ESP series products support roaming in Wi-Fi AP mode?
-----------------------------------------------------------------------------------------------------------------------

  - No, ESP series products only support connecting to routers with roaming features in Wi-Fi Station mode.
  - Software Reference: `esp-idf/examples/wifi/roaming <https://github.com/espressif/esp-idf/tree/release/v5.3/examples/wifi/roaming>`_.
