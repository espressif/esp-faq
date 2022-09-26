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

请问微信小程序 ESP-EYE 有相关资料吗？
---------------------------------------------------------------------------

  esp-eye demo 微信小程序的开源资料：`EspEyeForWeChat <https://github.com/EspressifApp/EspEyeForWeChat>`_。

----------------------

`esp-skainet <https://github.com/espressif/esp-skainet>`_ 示例支持哪些语言呢？
----------------------------------------------------------------------------------------

  目前仅支持中文和英文。

----------------------

`ESP-DL <https://github.com/espressif/esp-dl>`_ 支持哪些模型框架？
----------------------------------------------------------------------------------------

  目前支持 mxnet、pytorch、tensorflow 三个平台的模型。

----------------------

`ESP-DL <https://github.com/espressif/esp-dl>`_ 支持上述三个平台(mxnet, pytorch, and tensorflow)的所有的模型吗？
----------------------------------------------------------------------------------------------------------------------------------------------

  模型中所有的算子须为 ESP-DL 所支持的算子。有关支持的算子，请参考 `layer <https://github.com/espressif/esp-dl/tree/master/include/layer>`_。

----------------------

`ESP-SKAINET <https://github.com/espressif/esp-skainet>`_ 模型文件支持放在 SD 卡中吗？
----------------------------------------------------------------------------------------

  支持放在 SD 卡中。

----------------------

`ESP-SKAINET <https://github.com/espressif/esp-skainet>`_ 如何定制命令词？
------------------------------------------------------------------------------------

  定制命令词，请查看 `ESP-SR GitHub <https://github.com/espressif/esp-sr/blob/master/docs/speech_command_recognition/README_cn.md>`_。 

----------------------

如何降低 AI 语音模型的系统占用？
---------------------------------------

  可以选择关闭 AEC、AE、VAD 这三个功能。

----------------------

16 位量化模型和 8 位量化模型有什么区别？
---------------------------------------

  16 位量化模型的精度更高，结果更准确。8 位量化模型更轻量化。

----------------------

AI 语音模型如何修改麦克风通道数量？
---------------------------------------

  可以在 AFE 中配置麦克风通道数和回采通道数。

----------------------

如何拿到开发板中采集到的实际音频？
---------------------------------------

  需要有 SD 卡接口，将音频文件存入到 SD 卡中。
