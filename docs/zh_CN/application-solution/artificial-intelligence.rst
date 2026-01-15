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
----------------------------------

  当前 ESP-EYE 主控芯⽚为 ESP32，可兼容 0V2640，OV3660，OV5640，OV7725 等多款摄像头。详见：`esp32-camera Github <https://github.com/espressif/esp32-camera/tree/master/sensors>`_。
  
  对于 ESP32-P4 系列，请参考 `esp-video-components <https://github.com/espressif/esp-video-components>`_ 获取支持的摄像头型号。

--------------

ESP-WHO 支持使用 ESP-IDF 哪些版本？
-----------------------------------------------------------------------------

  请前往 `ESP-WHO Github <https://github.com/espressif/esp-who>`_ 获取最新信息。

--------------

请问微信小程序 ESP-EYE 有相关资料吗？
---------------------------------------------------------------------------

  ESP-EYE demo 微信小程序的开源资料：`EspEyeForWeChat <https://github.com/EspressifApp/EspEyeForWeChat>`_。

----------------------

`esp-skainet <https://github.com/espressif/esp-skainet>`_ 示例支持哪些语言呢？
----------------------------------------------------------------------------------------

  目前仅支持中文和英文。

----------------------

`ESP-DL <https://github.com/espressif/esp-dl>`_ 支持哪些模型框架？
----------------------------------------------------------------------------------------

  ESP-DL 所使用的 ESP-PPQ 量化工具支持直接对 ONNX 模型进行量化。Pytorch 和 TensorFlow 需要先转换为 ONNX 模型，因此请确保你的模型可以转换为 ONNX 模型。

----------------------

`ESP-DL <https://github.com/espressif/esp-dl>`_ 支持上述三个平台（MXNet、Pytorch、TensorFlow）的所有的模型吗？
----------------------------------------------------------------------------------------------------------------------------------------------

  模型中所有算子必须为 ESP-DL 所支持的算子。有关支持的算子，请参考 `Operator Support State <https://github.com/espressif/esp-dl/blob/master/operator_support_state.md>`_。

----------------------

`ESP-SKAINET <https://github.com/espressif/esp-skainet>`_ 模型文件支持放在 SD 卡中吗？
----------------------------------------------------------------------------------------

  支持放在 SD 卡中。

----------------------

`ESP-SKAINET <https://github.com/espressif/esp-skainet>`_ 如何定制命令词？
------------------------------------------------------------------------------------

  定制命令词，请查看 `自定义命令词方法 <https://docs.espressif.com/projects/esp-sr/zh_CN/latest/esp32s3/speech_command_recognition/README.html#id4>`__。 

----------------------

如何降低 AI 语音模型的系统占用？
---------------------------------------

  可以选择关闭 AEC、AE、VAD 这三个功能。

----------------------

16 位量化模型和 8 位量化模型有什么区别？
------------------------------------------------

  16 位量化模型的精度更高，结果更准确。8 位量化模型更轻量化。

----------------------

AI 语音模型如何修改麦克风通道数量？
---------------------------------------

  可以在 AFE 中配置麦克风通道数和回采通道数。

----------------------

如何拿到开发板中采集到的实际音频？
---------------------------------------

  需要有 SD 卡接口，将音频文件存入到 SD 卡中。

----------------------

有关 `ESP-SR GitHub <https://github.com/espressif/esp-sr/tree/master>`__ 的学习资料存放在哪里？
---------------------------------------------------------------------------------------------------------------------

  请参考 `ESP-SR 用户指南 <https://docs.espressif.com/projects/esp-sr/zh_CN/latest/esp32s3/index.html>`_。

----------------------

有关 `ESP-DL <https://github.com/espressif/esp-dl>`__ 的学习资料存放在哪里？
---------------------------------------------------------------------------------------------------

  请参考如下教程：

  - `如何使用 ESP-DL 部署手势识别 <https://medium.com/the-esp-journal/hand-gesture-recognition-on-esp32-s3-with-esp-deep-learning-176d7e13fd37>`_。
  - `如何使用 ESP-DL 部署 Touch 手写数字识别 <https://developer.espressif.com/blog/2025/06/touchpad-digit-recognition>`_。
  - `行人检测 <https://github.com/espressif/esp-dl/tree/master/examples/pedestrian_detect>`_。
  - `人脸检测 <https://github.com/espressif/esp-dl/tree/master/examples/human_face_detect>`_。
  - `人脸识别 <https://github.com/espressif/esp-dl/tree/master/examples/human_face_recognition>`_。
  - `Yolo11N 目标检测 <https://github.com/espressif/esp-dl/tree/master/models/coco_detect>`_。
  - `猫脸识别 <https://github.com/espressif/esp-dl/tree/master/models/cat_detect>`_。
  - `颜色识别 <https://github.com/espressif/esp-dl/tree/master/models/color_detect>`_。
  - `轻量级目标检测框架 `ESP-Detection <https://github.com/espressif/esp-detection>`_。

-------------

ESP32-S3 如何自定义英文命令词进行识别？
-----------------------------------------------------------------------------------------------------------------

  - 对于 MultiNet6，需要准备 ``commands_en.txt`` 来自定义英文命令词。对于 MultiNet5，可使用 ``multinet_g2p.py`` 脚本将英文命令词转换为 multinet 可以识别的音素。具体请参考 `esp-sr/tool <https://github.com/espressif/esp-sr/tree/master/tool>`_。

-------------

如何提高 Yolo11 的检测效率？
----------------------------------

  - 尝试量化小分辨率的模型，但这将损失一些精度，具体请参考 `quantize_yolo11n <https://github.com/espressif/esp-dl/tree/master/examples/tutorial/how_to_quantize_model/quantize_yolo11n>`_。
  - 使用轻量级的检测模型框架 `esp-detection <https://github.com/espressif/esp-detection>`_。
