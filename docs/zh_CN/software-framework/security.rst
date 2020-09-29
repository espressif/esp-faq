安全
====

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

ESP8266 的固件是否能被读取？
----------------------------

  ESP8266 固件由于放置在外部 flash, 数据可被外部读取。并且 ESP8266 不支持 flash 加密，所有数据均为明文。

--------------

ESP8285 是否可以固件加密？
----------------------------

  - ESP8285 芯片自身未有固件加密功能，无法完成固件加密。
  - ESP32 以及 ESP32-S2 芯片都有具备固件加密功能。
  - 也可选择外置加密芯片来完成部分数据加密。

--------------

开启 security boot 后, 编译报错缺少文件 ？
------------------------------------------

  错误 log：/d/ESP32/esp-mdf/esp-idf/components/bootloader\_support/Makefile.projbuild:7：/f/ESP32Root/secure\_boot\_signing\_key.pem。

  - 报错原因 security boot 是固件签名校验的功能，该功能需要生成证书对。相关资料 `参考 <https://blog.csdn.net/espressif/article/details/79362094>`_。

--------------

模组使能 Secure boot 是否可以再次烧录 ？
----------------------------------------

  - Secure boot 配置为 One-time，那么就只能烧录一次，不可以再重新 烧录 bootloader 固件。
  - Secure boot 配置为 Reflashable, 可以重新烧录 bootloader 固件。

--------------

模组使能 flash encrypted, 重新烧录后出现 ``flash read error`` 错误 ？
---------------------------------------------------------------------

  模组使能 flash encrypted, 重新烧录后，发现会出现 flash read error 的现象.

  - 模组使能 flash encrypted 后，模组开启加密功能后将不支持明文固件烧录。可以通过 espefuse.py 脚本将加密关闭后再次烧录，或者已知密钥烧录密文。注意: flash encrypted 加密开关存在次数，仅可重复 3 次。

--------------

ESP32 打开 flash 加密和 secure boot 后，如何关闭？
-------------------------------------------------------

  - 如果您使用的是 one-time flash（Release） 模式，那么 flash 加密和 secure boot 都是不能关闭的。
  - 如果您使用的是 reflashable （Development(NOT SECURE)）模式，那么 `flash 加密 <https://docs.espressif.com/projects/esp-idf/en/release-v4.1/security/flash-encryption.html#disabling-flash-encryption>`_ 可以关闭，secure boot 不能关闭。

--------------

ESP32 保护固件安全的方式有那些?
---------------------------------

  ESP32 支持 flash encryption 与 secure boot.
  - `flash encryption <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/security/flash-encryption.html>`_。
  - `secure boot <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/secure-boot-v1.html>`_。
  - `ECO3 Chip secure boot V2 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/secure-boot-v2.html>`_。
