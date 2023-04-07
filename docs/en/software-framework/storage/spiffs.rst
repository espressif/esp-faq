SPIFFS Filesystem
=================

:link_to_translation:`zh_CN:[中文]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

---------------

Can SPIFFS partition be encrypted?
----------------------------------------------------------------

  :CHIP\: ESP32, ESP32S2, ESP32S3, ESP32C3:

  - SPIFFS does not provide native disk encryption. However, as SPIFFS is realized based on flash, the data can be encrypted using flash encryption. Standard encryption libraries such as mbedtls or OpenSSL can be used to encrypt and decrypt files in SPIFFS. When writing files, the data is encrypted first, and then written to SPIFFS. When reading files, data is first read from SPIFFS, and then decrypted using corresponding decryption algorithms.

-------------------

How do I store the keys and certs of ESP32 devices in SPIFFS?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  You can generate an SPIFFS image from files and flash it to the corresponding partition. See `SPIFFS Filesystem <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/storage/spiffs.html#spiffsgen-py>`_ for details.

--------------

Can ESP32 mount a SPIFFS file system partition in the external SPI flash？
---------------------------------------------------------------------------------------------

  Yes, this function has been added in ESP-IDF v4.0 and later versions. Please note that when two partitions are mounted to ESP32, it is not permitted for multiple tasks to write files into the same partition at the same time.
