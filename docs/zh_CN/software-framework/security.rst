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
---------------------------------------

  ESP8266 固件由于放置在外部 flash，数据可被外部读取。并且 ESP8266 不支持 flash 加密，所有数据均为明文。

--------------

ESP8285 是否可以固件加密？
------------------------------------

  - ESP8285 芯片自身未有固件加密功能，无法完成固件加密。
  - ESP32 以及 ESP32-S2 芯片都有具备固件加密功能。
  - 也可选择外置加密芯片来完成部分数据加密。

--------------

开启 secure boot 后，编译报错缺少文件？
-----------------------------------------------------

  错误 log：/d/ESP32/esp-mdf/esp-idf/components/bootloader_support/Makefile.projbuild:7：/f/ESP32Root/secure_boot_signing_key.pem。

  报错原因：security boot 是固件签名校验的功能，该功能需要生成证书对。相关资料请参考 `这里 <https://blog.csdn.net/espressif/article/details/79362094>`_。

--------------

模组使能 secure boot 后是否可以再次烧录？
-------------------------------------------------------

  - secure boot 配置为 one-time，那么就只能烧录一次，不可以再重新烧录 bootloader 固件。
  - secure boot 配置为 reflashable，则可以重新烧录 bootloader 固件。

--------------

模组使能 flash encrypted，重新烧录后出现 ``flash read error`` 错误。如何解决？
-----------------------------------------------------------------------------------------------

  模组使能 flash encrypted 后，模组开启加密功能后将不支持明文固件烧录。可以通过 espefuse.py 脚本将加密关闭后再次烧录，或者已知密钥烧录密文。
  
  .. note::
      
      flash encrypted 加密开关存在次数限制，仅可重复 3 次。

--------------

ESP32 打开 flash 加密和 secure boot 后，如何关闭？
--------------------------------------------------------------------------

  - 如果您使用的是 one-time flash (Release) 模式，那么 flash 加密和 secure boot 都是不能关闭的。
  - 如果您使用的是 reflashable (Development (NOT SECURE)) 模式，那么 flash 加密可以关闭，请参见 `关闭 Flash 加密 <https://docs.espressif.com/projects/esp-idf/zh_CN/release-v4.1/security/flash-encryption.html#disabling-flash-encryption>`_；secure boot 不能关闭。

--------------

ESP32 保护固件安全的方式有那些？
------------------------------------------

  - ESP32 支持 flash encryption 与 secure boot。
  - flash 加密参考文档：`flash encryption <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/security/flash-encryption.html>`_。
  - 安全引导参考文档：`secure boot <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/secure-boot-v1.html>`_。
  - 安全引导 V2 参考文档：`ECO3 Chip secure boot V2 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/secure-boot-v2.html>`_。

--------------

ESP32 启动 flash 加密后进行 GDB 调试，为何会不断复位重启？
---------------------------------------------------------------------------------------------------------

  - ESP32 启动了 flash 加密或 secure Boot 后，默认将会禁用 JTAG 调试，请参见说明 `注意事项和补充内容 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/jtag-debugging/tips-and-quirks.html#jtag-with-flash-encryption-or-secure-boot>`_。
  - 可以通过 esptool 工具包中的 ``espefuse.py summary`` 脚本指令读取当前芯片 JTAG 状态。 
