射频相关
========

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

ESP32 模组在 2.8 V 电源下运行，射频性能会有下降吗？
------------------------------------------------------------

  射频会不稳定。建议按照相应 `模组技术规格书 <https://www.espressif.com/zh-hans/support/documents/technical-documents>`_ 中说明的建议工作电压范围提供电压。

--------------

乐鑫芯片支持的调制方式有哪些？
---------------------------------------------------

  - ESP8266 芯片支持的调制方式有：BPSK/QPSK/16QAM/64QAM/DBPSK/DQPSK/CCK。
  - ESP32 芯片支持的调制方式有：BPSK/QPSK/16QAM/64QAM/DBPSK/DQPSK/CCK/GFSK Π/4-DQPSK 8-DPSK。
  - ESP32-S2 芯片支持的调制方式有：BPSK/QPSK/16QAM/64QAM/DBPSK/DQPSK/CCK。

--------------

如何获取乐鑫产品的 RF 相关的信息（如天线描述、天线辐射图等）用于认证？
--------------------------------------------------------------------------------------

  请联系 `商务 <https://www.espressif.com/zh-hans/contact-us/sales-questions>`_ 获取相关信息。

--------------

ESP32 使用 RF Test Tool 时为什么在高温 80 °C 下运行会自动降低发射功率？
----------------------------------------------------------------------------------------------------------------------

  - ESP32 的定频测试固件上电默认是不开温度补偿的，当温度较高时功率会变低，如果需要打开温度补偿就需要通过默认的 log 串口向 ESP32 发送 ``txpwr_track_en 1 1 0``。

--------------

ESP32-WROVER-E 模组如何提高 Wi-Fi 信号的接收距离和强度？(应用场景：Wi-Fi 探针)
-----------------------------------------------------------------------------------

  - 软件上可以通过 API `esp_wifi_set_max_tx_power() <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html#_CPPv425esp_wifi_set_max_tx_power6int8_t>`_ 设置最大发射功率。也可通过 menuconfig 进行配置：``Component config -> PHY -> Max Wi-Fi TX power(dBm)``，默认发射功率为最大值 20 dBm。
  - 若发射功率已设置为最大值，可从天线和接收设备考虑。

    - 可以考虑调整模组的摆放方向，使天线较强的辐射方向指向接收设备，使辐射距离最远。
    - 模组的天线附近没有金属或遮挡物，天线背面没有 PCB，Wi-Fi 信号未受整机其它信号干扰。
    - 如果 PCB 天线效果不好，可以考虑更换使用 IE 系列模组，使用定向增益更高的外置 IPEX 天线。
    - 接收设备也可以增加天线辐射效率。

---------------

如何烧写 phy_init 数据到 flash 中？
--------------------------------------------------------------------------------------------------

  :CHIP\: ESP32 :

  - 可以通过 power limit tool 烧写。下载 `ESP_RF_TEST Tool <https://www.espressif.com/sites/default/files/tools/ESP_RF_Test_CN.zip>`_，解压完成后，打开 EspRFTestTool_v2.6_Manual.exe，点击 ``help ---> Tool help ---> PowerLimitTool help`` 查看详细的操作步骤。
