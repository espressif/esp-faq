AI 应用
=======

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

-  当前 ESP-EYE 主控芯⽚为 ESP32，可兼容 0V2640，OV3660， OV5640，
   OV7725 等多款摄像头（详见 `esp32-camera
   Github <https://github.com/espressif/esp32-camera/tree/master/sensors>`__
   ）

--------------

esp-who 是否⽀持 IDF 4.1？
--------------------------

-  暂不支持，目前仅⽀持 IDF v3.3.1 和 v4.0.0（esp-who commit:
   ``2470e47 Update esp32-camera``\ ）
-  esp-who 会陆续支持其他版本 IDF，请在 `ESP-WHO
   Github <https://github.com/espressif/esp-who>`__ 获得最新信息。

