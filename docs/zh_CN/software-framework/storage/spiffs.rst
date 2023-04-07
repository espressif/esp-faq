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

---------------

SPIFFS 支持磁盘加密吗？
----------------------------------------------------------------

  :CHIP\: ESP32, ESP32S2, ESP32S3, ESP32C3:

  - SPIFFS 不提供原生的磁盘加密功能，但 SPIFFS 建立在 flash 上，可以使用 flash 加密对该部分的数据进行加密。可以使用标准的加密库，如 mbedtls 或 OpenSSL，来加密和解密 SPIFFS 中的文件。在写入文件时，先将数据进行加密，然后再写入 SPIFFS。在读取文件时，先从 SPIFFS 读取数据，然后再使用相应的解密算法进行解密。
  
----------------

如何将 ESP32 设备的 key 和 certs 存储到 SPIFFS 中呢？
---------------------------------------------------------

  可将文件生成 SPIFFS 镜像后烧录到对应分区，可参考 `SPIFFS 文件系统 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/storage/spiffs.html#spiffsgen-py>`_。

--------------

ESP32 是否可以在外挂的 SPI flash 中挂载 SPIFFS 文件系统分区？
---------------------------------------------------------------

  在 ESP-IDF v4.0 以及之后的版本添加了该功能。需要注意的是，当挂载了两个分区时，不能多个任务同时向一个分区写入文件。
