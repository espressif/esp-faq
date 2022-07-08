SPIFFS 文件系统
=======================

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

使用 FAT 文件系统时文件名稍微长一点的文件无法打开，该如何处理？
--------------------------------------------------------------------------------------------------------------------------------------------------

  - 可以在 ``menuconfig`` -> ``Component config`` -> ``FAT Filesystem support`` -> ``Long filename support 中进行修改，选择 ``Long filename buffer in heap`` 或 ``Long filename buffer on stack`` 配置项。然后可以在 ``Component config`` -> ``FAT Filesystem support`` -> ``Max long filename length`` 中修改最大的文件名长度。

---------------

SPIFFS 支持磁盘加密吗？
---------------------------------------------------------------

  :CHIP\: ESP32, ESP32S2, ESP32S3, ESP32C3:

  - SPIFFS 分区无法加密。但 SPIFFS 建立在 flash 上，可以使用 flash 加密对该部分的数据进行加密。
  
----------------

如何将 ESP32 设备的 key 和 certs 存储到 spiffs 中呢？
---------------------------------------------------------

 可将文件生成 SPIFFS 镜像后烧录到对应分区，可参考 `SPIFFS 文件系统 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/storage/spiffs.html#spiffsgen-py/>`_。
