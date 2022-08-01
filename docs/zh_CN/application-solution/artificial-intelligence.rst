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

  当前 ESP-EYE 主控芯⽚为 ESP32，可兼容 0V2640，OV3660，OV5640，OV7725 等多款摄像头。
  详见：`esp32-camera Github <https://github.com/espressif/esp32-camera/tree/master/sensors>`_。

--------------

ESP-WHO 支持使用 ESP-IDF 哪些版本？
-----------------------------------------------------------------------------

  请前往 `ESP-WHO Github <https://github.com/espressif/esp-who>`_ 获取最新信息。

--------------

如何查看 ESP-FACE 组件的 API 参考？
------------------------------------------------------------------------

  - 人脸检测介绍：`MTMN <https://github.com/espressif/esp-face/blob/master/face_detection/README.md>`_ 与 `FRMN <https://github.com/espressif/esp-face/blob/master/face_recognition/README.md>`_。
  - 关于 API 的使用实例，可以参考 ESP-WHO 中的 `example <https://github.com/espressif/esp-who>`_。

--------------

请问微信小程序 ESP-EYE 有相关资料吗？
---------------------------------------------------------------------------

  - ESP-EYE 微信小程序的介绍及示例：`recognition_wechat <https://github.com/espressif/esp-who/tree/master/examples/single_chip/face_recognition_wechat>`_。
  - esp-eye demo 微信小程序的开源资料：`EspEyeForWeChat <https://github.com/EspressifApp/EspEyeForWeChat>`_。

----------------------

`esp-skainet <https://github.com/espressif/esp-skainet>`_ 示例支持哪些语言呢？
----------------------------------------------------------------------------------------

  - 目前仅支持中文和英文。

----------------------

`ESP-DL <https://github.com/espressif/esp-dl>`_ 支持哪些模型框架？
----------------------------------------------------------------------------------------

  - 目前支持 mxnet、 pytorh、 tensorflow 三个平台的模型。

----------------------

`ESP-DL <https://github.com/espressif/esp-dl>`_ 支持上述三个平台的所有的模型吗？
----------------------------------------------------------------------------------------

  - 模型中所有的算子须为 ESP-DL 所支持的算子。有关支持的算子，请参考 `layer <https://github.com/espressif/esp-dl/tree/master/include/layer>`。

----------------------

`ESP-DL <https://github.com/espressif/esp-dl>`_ 模型文件支持放在 SD 卡中吗？
----------------------------------------------------------------------------------------

  - 支持放在 SD 卡中。

----------------------
