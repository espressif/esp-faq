AI 应用
=======

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

AI 图像识别产品可兼容哪些摄像头？
---------------------------------

  当前 ESP-EYE 主控芯⽚为 ESP32，可兼容 0V2640，OV3660，OV5640，OV7725 等多款摄像头（详情请见 `esp32-camera Github <https://github.com/espressif/esp32-camera/tree/master/sensors>`_）。

--------------

esp-who 是否⽀持 IDF 4.1？
--------------------------

  暂不支持，目前仅⽀持 IDF v3.3.1 和 v4.0.0（esp-who commit: ``2470e47 Update esp32-camera``\ ），但是会陆续支持其他版本 IDF，请在 `ESP-WHO Github <https://github.com/espressif/esp-who>`_ 获取最新信息。

--------------

esp-face组件的api参考？
---------------------------------

  - `关于人脸检测API介绍 <https://github.com/espressif/esp-face/blob/master/face_detection/README.md>`_
  - `关于人脸识别API介绍 <https://github.com/espressif/esp-face/blob/master/face_recognition/README.md>`_
  - 关于API的使用实例，可以参考ESP-WHO中的 `example <https://github.com/espressif/esp-who>`_

--------------

请问微信小程序esp-eye有相关资料吗?
------------------------------------

  - esp-eye 微信小程序的介绍及示例在这里：`recognition_wechat <https://github.com/espressif/esp-who/tree/master/examples/single_chip/face_recognition_wechat>`_
  - esp-eye demo 微信小程序的开源资料：`EspEyeForWeChat <https://github.com/EspressifApp/EspEyeForWeChat>`_
  - 另外，“乐鑫信息科技”微信订阅号也曾发布关于小程序的文章《ESP32解锁新平台，人脸识别小程序上线》，欢迎关注～
