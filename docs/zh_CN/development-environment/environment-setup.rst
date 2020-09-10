环境搭建
========

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

ESP32-S2 搭建环境时使用 “idf.py set-target esp32-s2” 指令时，显示 “Error: No such command 'set-target' ” 为什么？
-----------------------------------------------------------------------------------------------------------------

-  因为 esp-idf 是从 release/v4.2 版本开始适配 ESP32-S2
   的，所以如果在之前的 esp-idf 版本上去搭建 ESP32-S2
   环境会出现错误，例如使用指令 “idf.py set-target esp32-s2” 时，会报错
   “Error: No such command 'set-target' ” 。
-  建议使用 esp-idf release/v4.2 及以后版本进行 ESP32-S2
   的测试开发。更多请参考 `ESP32-S2
   入门指南 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s2/get-started/>`__

--------------

idf.py menuconfig 编译报 "Configuring incomplete , errors occured" 的错误信息如何解决呢？
-----------------------------------------------------------------------------------------

查看 cmake 版本，使用camke --version 进行查看， 如果低于 3.10.0
版本，我们认为是低版本， 建议更新 cmake 版本

-  下载 cmake ：https://cmake.org/download/

-  操作参考链接：http://www.mamicode.com/info-detail-2594302.html

--------------

Windows 下 使用 ESP-IDF Tools 2.3 工具安装 master 版本的 esp-idf 出现错误：Installation has failed with exit code 2 是什么原因？
--------------------------------------------------------------------------------------------------------------------------------

此报错跟网络环境有关，该网路环境下无法流畅的下载 github 仓库，导致电脑
SDK 下载失败 。

--------------

windows 下使用 `esp-idf-tools-setup-2.3.exe <link:https://dl.espressif.com/dl/esp-idf-tools-setup-2.3.exe>`__ 搭建环境，make menuconfig 出现如下错误：
------------------------------------------------------------------------------------------------------------------------------------------------------

.. code:: shell

    -- Warning: Did not find file Compiler/-ASM Configure
    -- Configuring incomplete , erros occurred !

-  出现此错误的原因是没有因为未找到编译工程，可以切换目录到
   esp-idf/get-started/hello\_world 示例中进行测试验证。
