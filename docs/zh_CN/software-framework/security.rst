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
----------------------------------------

  ESP8266 固件放置在外部 flash，数据可被外部读取。并且 ESP8266 不支持 flash 加密，所有数据均为明文。

--------------

ESP8285 是否可以固件加密？
------------------------------------

  - ESP8285 芯片自身未有固件加密功能，无法完成固件加密。
  - ESP32 及 ESP32-S2 芯片支持固件加密功能，用户可以考虑使用这两款芯片。
  - 如仍需使用 ESP8285，用户可以选择外置加密芯片完成部分数据加密。

--------------

secure boot v1 和 secure boot v2 有什么区别？
--------------------------------------------------------------
  
  secure boot v2 相较于 secure boot v1 主要做了以下方面的改进：
  - bootloader 和 app 使用相同的签名格式。
  - bootloader 和 app 使用统一的签名密钥。

  当前，仅 ESP32 v3.0 以下版本推荐使用 `secure boot v1 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/security/secure-boot-v1.html>`_，ESP32 v3.0 及以上版本、ESP32-C3、ESP32-S2 和 ESP32-S3 推荐使用 `secure boot v2 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/security/secure-boot-v2.html>`_。

--------------

开启 secure boot 后，为什么编译报错缺少文件？
-----------------------------------------------------------------------

  错误日志：/Makefile.projbuild:7：/f/ESP32Root/secure_boot_signing_key.pem。

  报错原因：security boot 是固件签名校验的功能，该功能需要生成密钥对。
  - 启用 secure boot v1 时生成密钥对的方法请参考 `secure boot v1 生成密钥 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/security/secure-boot-v1.html#generating-secure-boot-signing-key>`_。
  - 启用 secure boot v2 时生成密钥对的方法请参考 `secure boot v2 生成密钥 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/security/secure-boot-v2.html#generating-secure-boot-signing-key>`_。

--------------

模组使能 secure boot 后是否可以再次烧录？
-------------------------------------------------------

  - 若 secure boot v1 配置为 one-time，则仅支持烧录一次，不可以再重新烧录 bootloader 固件。
  - 若 secure boot v1 配置为 reflashable，则可以重新烧录 bootloader 固件。
  - secure boot v2 允许重新烧录 bootloader 和 app 固件。

--------------

模组使能 flash encrypted，重新烧录后出现 ``flash read error`` 错误。如何解决？
-----------------------------------------------------------------------------------------------

  模组开启加密功能后将不支持明文固件烧录，常见的错误请参考 `重新烧录可能出现的错误 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/security/flash-encryption.html#id9>`_。可以通过 `espefuse <https://docs.espressif.com/projects/esptool/en/latest/esp32/espefuse/index.html>`_ 脚本关闭加密后再次烧录明文数据，或者参考 `flash 加密示例 <https://github.com/espressif/esp-idf/tree/master/examples/security/flash_encryption>`_，将加密后的固件数据烧录到设备上。
  
  .. note::
      
      flash encrypted 加密开关存在次数限制。

--------------

ESP32 打开 flash 加密和 secure boot 后，如何关闭？
--------------------------------------------------------------------------

  - 如果您使用的是 one-time flash (Release) 模式，那么 flash 加密和 secure boot 都是不能关闭的。
  - 如果您使用的是 reflashable (Development (NOT SECURE)) 模式，那么 flash 加密可以关闭，请参见 `关闭 Flash 加密 <https://docs.espressif.com/projects/esp-idf/zh_CN/v4.4.2/esp32/security/flash-encryption.html#id16>`_；secure boot 不能关闭。

--------------

ESP32 保护固件安全的方式有哪些？
------------------------------------------

  - ESP32 支持 flash 加密与 secure boot。
  - flash 加密参考文档：`flash 加密 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/security/flash-encryption.html>`_。
  - 安全引导参考文档：`secure boot <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/security/secure-boot-v1.html>`_。
  - 安全引导 V2 参考文档：`v3.0 版本芯片的安全引导 V2 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/secure-boot-v2.html>`_。

--------------

ESP32 启动 flash 加密后进行 GDB 调试，为何会不断复位重启？
---------------------------------------------------------------------------------------------------------

  - ESP32 启动了 flash 加密或 secure Boot 后，默认将会禁用 JTAG 调试，请参见 `注意事项和补充内容 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/jtag-debugging/tips-and-quirks.html#jtag-debugging-security-features>`_。
  - 可以通过 esptool 工具包中的 ``espefuse.py summary`` 脚本指令读取当前芯片 JTAG 状态。 

---------------

ESP32 芯片如何开启 Flash 加密？
-------------------------------------------------------------------------------------------------------------------

  - 在 ESP-IDF 编译配置中，通过 menuconfig 或 idf.py menuconfig 中的 ``Security features`` --> ``Enable flash encryption on boot (READ DOCS FIRST)`` 修改。
  - 请参见 `Flash 加密说明 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/security/flash-encryption.html#flash>`_。

-------------

ESP32 的 GPIO0 拉低后无法进入下载模式，日志打印 "download mode is disable" 是什么原因？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP32 芯片上电打印 "download mode is disable" 日志，说明该芯片的 UART 下载模式 (UART download mode) 已被禁用。您可以检查该芯片 `eFuse <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/system/efuse.html?highlight=download%20mode>`_ 中的 ``UART_DOWNLOAD_DIS`` 位，查看该模式是否被禁用。
  - 注意，启用 flash 加密的量产模式后，UART 下载模式将默认被禁用。更多信息，请参考 `UART ROM download mode <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-reference/kconfig.html#config-secure-uart-rom-dl-mode>`_。
  
----------------

在 Arduino 开发环境中使用 ESP32 能开启 secure boot 功能吗？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 不能，如果要使用 Arduino 进行开发，开启 secure boot 功能的唯一方法是将 Arduino 作为 IDF 组件使用。

-------------

secure boot 和 flash 加密的使用场景有哪些？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 启用 secure boot 后，设备将仅加载运行指定密钥签名后的固件。因此，启用 secure boot 可以避免设备加载非法的固件、防止对设备刷写未经授权的固件。
  - 启用 flash 加密后，flash 上存储固件的分区以及被标识为 “encrypeted" 的分区中的数据将被加密。因此，启用 flash 加密可以避免 flash 上的数据被非法查看，并且从 flash 上拷贝的固件数据无法应用到其他设备上。

------------

secure boot 和 flash 加密中涉及的存储在 eFuse 数据有哪些？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - secure boot v1 中使用的存储在 eFuse 数据请参考 `secure boot v1 efuses <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/security/secure-boot-v1.html#background>`_。
  - secure boot v2 中使用的存储在 eFuse 数据请参考 `secure boot v2 efuses <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/security/secure-boot-v2.html#efuse-usage>`_。
  - flash 加密中使用的存储在 eFuse 数据请参考 `flash 加密 efuses <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/security/flash-encryption.html#efuses>`_。

------------

启用 secure boot 失败，提示 “Checksum failure”，怎么解决？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 启用 secure boot 后，bootloader.bin 的大小将增大，请检查引导加载程序分区的大小是否足够存放编译得到的 bootloader.bin。更多说明请参考 `引导加载程序大小 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/bootloader.html#bootloader-size>`_。


启用 NVS 加密失败，提示 ``nvs: Failed to read NVS security cfg: [0x1117] (ESP_ERR_NVS_CORRUPT_KEY_PART)``，怎么解决？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 启用 NVS 加密前，建议先使用烧录工具擦除一次 flash，然后烧录包含使能 NVS 加密的固件。


启用 flash 加密后，提示 ``esp_image: image at 0x520000 has invalid magic byte (nothing flashed here)``，怎么解决？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 启用 flash 加密后，将尝试对所有 app 类型的分区的数据进行加密，当 app 分区中没有存储对应的 app 固件时，将提示该 log。您可以在启用 flash 加密时对所有 app 类型的分区烧录预编译的 app 固件来避免出现这种警告。

使能 ``CONFIG_EFUSE_VIRTUAL`` 选项后，开启 flash 加密，为何相关数据未被加密？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Virtual eFuses 功能目前仅仅用于测试 eFuse 数据的更新，启用该功能后，flash 加密功能并未完全开启。

可以向一个未使能 flash 加密的设备中通过 OTA 更新一个使能了 flash 加密的 app 固件吗？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 可以，请在编译时取消选中 ``Check Flash Encryption enabled on app startup``。

如何撤销 secure boot 的 key？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 撤销 secure boot key 的操作是在 ``new_app.bin`` 固件中完成的。首先 ``new_app.bin`` 必须附带两个签名。然后，下发 ``new_app.bin`` 到设备上。最后，当旧的签名校验通过后，通过 ``new_app.bin`` 中的 ``esp_ota_revoke_secure_boot_public_key()`` 执行撤销旧 key 的操作。注意，如果您使用了 OTA 回滚方案，请在 ``esp_ota_mark_app_valid_cancel_rollback()`` 返回 ``ESP_OK`` 后再调用 ``esp_ota_revoke_secure_boot_public_key()``。 更多说明请参考 `Key Revocation <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32c3/security/secure-boot-v2.html?highlight=esp_ota_revoke_secure_boot_public_key#key-revocation>`_。

启用 secure boot 或者 flash 加密（开发模式）后，无法烧录新固件，提示 ``Failed to enter Flash download mode``，怎么解决？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 这种提示通常代表您使用的烧录命令不正确。请使用 ``idf.py`` 脚本执行 ``idf.py bootloader``、``idf.py app`` 命令编译 ``bootloader.bin``、``app.bin``。然后根据编译后的提示使用 ``idf.py`` 执行烧录命令。如果还不能烧录程序，请使用 ``espefuse.py -p PORT summary`` 命令查看当前设备的 eFuse，并检查 ``flash download mode`` 是否是 enable 状态。

-------------------

在配置了 ESP-IDF 环境的终端里输入 ``espefuse.py read_protect_efuse BLOCK3`` 指令对 Efuse BLOCK3 进行读保护后，再输入 ``esp_efuse_read_block()`` 读取 Efuse BLOCK3 的数据，数据全为 0x00，是什么原因？
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Efuse BLOCK3 被读保护之后就不能再被读取了。

----------------------------------------

如何通过预烧录 eFuse 的方式使能 secure boot 或者 flash 加密？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  默认情况下，可以通过向设备中烧录使能了 secure boot 或者 flash 加密的固件来启用 secure boot 或者 flash 加密。用户也可以通过下述两种通过预烧录 eFuse 的方式使能 secure boot 或者 flash 加密：
  - `flash_download_tool <https://www.espressif.com/zh-hans/support/download/other-tools>`__ 在使能 secure boot 或者 flash 加密时会自动预烧录 eFuse.
  - 通过使用 `espsecure.py <https://docs.espressif.com/projects/esptool/en/latest/esp32/espsecure/index.html>`__ 和 `espefuse.py <https://docs.espressif.com/projects/esptool/en/latest/esp32/espefuse/index.html>`__ 来生成密钥以及烧录对应的 eFuse 存储块。

------------

启用 Secure Boot 后，使用 ``idf.py build`` 命令无法烧录新的 bootloader.bin？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  启用 Secure Boot 后，请使用 ``idf.py bootloader`` 命令编译新的 bootloader.bin。然后通过 ``idf.py -p (PORT) bootloader-flash`` 命令烧录新的 bootloader.bin。

------------

启用 Secure Boot 或者 flash 加密后，如何查看设备中关于安全特性的信息？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  请使用 ``esptool.py --no-stub get_security_info`` 命令查看设备的安全信息。

------------

启用 Secure Boot 或者 flash 加密后，OTA 时应该注意什么？
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 启用 Secure Boot 后，你必须对 OTA 要使用的新固件进行签名，否则新固件无法被应用到设备上；
  - 启用 flash 加密后，在生成新固件时，请保持使能 flash 加密的选项。
  