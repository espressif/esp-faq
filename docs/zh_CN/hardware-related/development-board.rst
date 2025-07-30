开发板使用
==========

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

`ESP32-Korvo v1.1 <https://github.com/espressif/esp-skainet/blob/master/docs/zh_CN/hw-reference/esp32/user-guide-esp32-korvo-v1.1.md>`__ 开发板是否集成 LED driver 芯片？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  乐鑫出厂的 `ESP32-Korvo v1.1 <https://github.com/espressif/esp-skainet/blob/master/docs/zh_CN/hw-reference/esp32/user-guide-esp32-korvo-v1.1.md>`__ 开发板中集成了 LED driver 芯片。

--------------

`ESP-EYE <https://www.espressif.com/zh-hans/products/devkits/esp-eye/overview>`__ 开发板运行发热过高如何改善？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 降低功耗：如果摄像头并非实时开启，Wi-Fi 可以周期传输，空闲时间可以进入休眠模式以降低功耗。
  - 增大散热面积：可以通过在 ESP32 芯片上方增加散热片实现。

--------------

若开发板不使用 USB 供电，应如何使用管脚供电？
----------------------------------------------------------------------------------------------------------

  - 第一种方法："3V3 连接 3V3" + "GND 连接 GND"（如果开发板存在非 3.3 V 供电的器件，则该器件将无法使用）。
  - 第二种方法："5V 连接 5V" + "GND 连接 GND"。

  .. note:: 供电电流需要满足 500 mA。

--------------

开发板 `ESP32-Korvo-DU1906 <https://espressif-docs.readthedocs-hosted.com/projects/esp-adf/zh-cn/latest/design-guide/dev-boards/get-started-esp32-korvo-du1906.html>`__ 中 DU1906 芯片音频数据通过什么协议与 ESP32 交互？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  开发板 `ESP32-Korvo-DU1906 <https://espressif-docs.readthedocs-hosted.com/projects/esp-adf/zh-cn/latest/design-guide/dev-boards/get-started-esp32-korvo-du1906.html>`__ 中，DU1906 的音频数据通过 SPI 传给 ESP32。

--------------

是否有支持 POE 供电的以太网开发板？
---------------------------------------------------------------------------------------

  `ESP32-Ethernet-Kit <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/hw-reference/esp32/get-started-ethernet-kit.html>`_ 是支持 POE 供电的以太网开发板。

--------------

`ESP32-DevKitC <https://www.espressif.com/zh-hans/products/devkits/esp32-devkitc/overview>`__ 开发板 LED 灯不亮，设备管理器也无法找到该设备，可能是什么原因导致的？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 检查供电是否正常：插上 USB 线之后供电，用万用表测试引脚 VCC 和 GND 是否有电压。
  - 检查是否为特定开发板故障：检查其他的 `ESP32-DevKitC <https://www.espressif.com/zh-hans/products/devkits/esp32-devkitc/overview>`__ 开发板设备用该 USB 线是否正常。
  - 若尝试上述方法后仍无法找到原因，可以通过 USB 转 TTL 设备去接线，只需接 `ESP32-DevKitC <https://www.espressif.com/zh-hans/products/devkits/esp32-devkitc/overview>`__ 的 VCC、GND、TXD 引脚，测试是否为芯片问题，用串口助手查看是否能够打印日志。
  - 如果可以，请测试串口驱动芯片是否有电压，可以参考 `ESP32-DevKitC 原理图 <https://www.espressif.com/sites/default/files/documentation/esp32-devkitc-v4_reference_design_0.zip>`_。

--------------

文档中有提到 EN 按键，但在购买的开发板上没有找到该按键？
------------------------------------------------------------------------------------------------------------------------------------------------

  建议检查开发板是否有 Reset 按键，由于 EN 常用做复位功能，部分开发板丝印会标记为 Reset 按键。

---------------

使用 ESP32 开发板，连接 Windows 电脑后未在设备管理器中找到串口，有哪些原因？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

  使用 ESP32 开发板连接到 Windows 电脑后，如果在设备管理器中未找到串口，可能是以下几个原因：

  - 未安装驱动程序：在使用 ESP32 开发板连接 Windows 电脑前，需要安装驱动程序。如果没有安装驱动程序或者驱动程序安装不正确，开发板将无法被识别为串口设备。下载安装 `FT232R USB UART 驱动 <https://www.usb-drivers.org/ft232r-usb-uart-driver.html>`_。
  - USB 线松动或损坏：如果 USB 线松动或损坏，可能会导致开发板无法被正确识别。用户可以更换 USB 线或者检查 USB 线是否插紧，确保 USB 线与电脑之间的连接正常。
  - 开发板故障：如果以上两种情况都不存在，那么可能是开发板本身存在故障。用户可以尝试使用其他 USB 端口或者其他电脑进行连接测试，或者进行开发板的硬件检测和维修。

  需要注意的是，在进行开发板连接测试时，需要确认开发板的串口设置和驱动程序设置是否正确。有些开发板需要在串口设置中手动选择正确的端口号和波特率，才能正确连接到电脑。同时，一些驱动程序也需要手动设置端口号和波特率，确保与开发板设置一致。

---------------

使用 `ESP32-LyraT v4.3 <https://espressif-docs.readthedocs-hosted.com/projects/esp-adf/zh-cn/latest/design-guide/dev-boards/get-started-esp32-lyrat.html>`__ 音频开发板，长按 Boot 按键也很难进入下载模式，是什么原因？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  正确的做法是：长按 Boot 按键，然后按 RST 按键（此时 Boot 按键不松开），然后松开 RST 按键（此时 Boot 依然不松开），当进入下载模式开始下载后，即可松开 Boot 键。

---------------

使用 ESP-WROOM-02D 模组，复位信号持续多久后模组会进入复位状态？
-------------------------------------------------------------------------------------------------------------------------------------------------------

  当输入电平低于 0.6 V 并持续 200 μs 以上时，ESP-WROOM-02D 模组会重启。

---------------

`ESP32-LyraT-Mini <https://espressif-docs.readthedocs-hosted.com/projects/esp-adf/zh-cn/latest/design-guide/dev-boards/get-started-esp32-lyrat-mini.html>`__ 开发板的原理图中将 ES8311 codec 芯片的模拟量输出连接到了 ES7243 ADC 芯片的输入，这样做的目的是什么？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  AEC 回声参考信号的硬件回采电路将 Codec（ES8311）的 DAC 输出同时传输给喇叭 PA 和 ADC（ES7243）AINLP/N，随后将采集的信号送回 ESP32，用做 AEC 回声消除算法的参考信号。

----------------

使用 `ESP32-MINI-1 <https://www.espressif.com/sites/default/files/documentation/esp32-mini-1_datasheet_cn.pdf>`__ 模组，串口上电打印日志如下，是什么原因？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

      rst:0x10 (RTCWDT_RTC_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
      invalid header: 0xffffffff
      invalid header: 0xffffffff
      invalid header: 0xffffffff
      invalid header: 0xffffffff
      invalid header: 0xffffffff
      invalid header: 0xffffffff
      invalid header: 0xffffffff
      invalid header: 0xffffffff
      ets Jul 29 2019 12:21:46

  ESP32-MINI-1 模组打印如上日志是因为 flash 没有程序。

------------

`ESP32-S3-DevKitC-1 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32s3/hw-reference/esp32s3/user-guide-devkitc-1.html#esp32-s3-devkitc-1-v1-1>`_ 开发板的 RGB LED 连接的是哪个 GPIO?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - `ESP32-S3-DevKitC-1 v1.0 <https://dl.espressif.com/dl/SCH_ESP32-S3-DEVKITC-1_V1_20210312C.pdf>`_ 版本开发板的 RGB LED 连接的是 GPIO48。
  - `ESP32-S3-DevKitC-1 v1.1 <https://dl.espressif.com/dl/schematics/SCH_ESP32-S3-DevKitC-1_V1.1_20221130.pdf>`_ 版本开发板的 RGB LED 连接的是 GPIO38。
  - `ESP32-S3-DevKitC-1 v1.1 <https://dl.espressif.com/dl/schematics/SCH_ESP32-S3-DevKitC-1_V1.1_20221130.pdf>`_ 版本开发板将 RGB LED 管脚改为 GPIO38 是因为 `ESP32-S3R8V 芯片 <https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_cn.pdf>`_ 的 VDD_SPI 电压已设置为 1.8 V。所以，不同于其他 GPIO，该芯片在 VDD_SPI 电源域中的 GPIO47 和 GPIO48 的工作电压也为 1.8 V。
