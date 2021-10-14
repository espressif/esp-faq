功耗测试指南
============

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

ESP32 deep sleep 唤醒为何需要重启？
-----------------------------------

  深度睡眠（deep sleep）唤醒都是需要重新启动，是因为深度睡眠时 CPU 电源域掉电，唤醒后需要重新引导固件并加载至内存。在深度睡眠（deep sleep）时 RTC 内存保持供电，可以将需要保留的应用信息保存其中，在唤醒后进行加载保留信息。


--------------

休眠⽅式有哪⼏种？有什么区别？
------------------------------

  有 Modem-sleep、Light-sleep 和 Deep-sleep 三种休眠⽅式。

  - Modem-sleep：Wi-Fi 协议中规定的 Station Legacy Fast 休眠⽅式，Station 发送 NULL 数据帧通知 AP 休眠或唤醒。Station 连接上 AP 之后⾃动开启，进⼊休眠状态后关闭射频模块，休眠期间保持和 AP 的连接，AP 断开连接后Modem-sleep 不⼯作。ESP32 Modem-sleep 进 ⼊休眠状态后，还可以选择降低 CPU 时钟频率，进 ⼀步降低电流。
  - Light-sleep：基于 Modem-sleep 的 Station 休眠⽅式。与 Modem-sleep 的不同之处在于进⼊休眠状态后，不仅关闭 RF 模块，还暂停 CPU 和部分系统时钟退出休眠状态后，CPU 继续运⾏。
  - Deep-sleep：⾮ Wi-Fi 协议规定的休眠⽅式。进⼊休眠状态后，关闭除 RTC 模块外的所有其他模块；退出休眠状态后，整个系统重新运⾏（类似于系统重启）。休眠期间不保持到 AP的连接。

--------------

ESP32 deep sleep 可以通过任意 RTC_GPIO 唤醒吗？
------------------------------------------------

  是的，RTC_GPIO 管脚配置可以参考 `ESP32 datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_cn.pdf>`_ V2.2 章节。
