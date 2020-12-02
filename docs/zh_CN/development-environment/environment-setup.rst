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

  - 因为 esp-idf 是从 release/v4.2 版本开始适配 ESP32-S2 的，所以如果在之前的 esp-idf 版本上去搭建 ESP32-S2 环境会出现错误，例如使用指令 “idf.py set-target esp32-s2” 时，会报错 “Error: No such command 'set-target' ” 。
  - 建议使用 esp-idf release/v4.2 及以后版本进行 ESP32-S2 的测试开发。更多请参考 `ESP32-S2 入门指南 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s2/get-started/>`_。

--------------

idf.py menuconfig 编译报 "Configuring incomplete , errors occured" 的错误信息如何解决呢？
-----------------------------------------------------------------------------------------

  查看 cmake 版本，使用camke --version 进行查看， 如果低于 3.10.0 版本，我们认为是低版本， 建议更新 cmake 版本：

  - 下载 cmake ：https://cmake.org/download/
  - 操作参考链接：http://www.mamicode.com/info-detail-2594302.html

--------------

Windows 下使用 ESP-IDF Tools 2.3 工具安装 master 版本的 esp-idf 出现错误：Installation has failed with exit code 2 是什么原因？
--------------------------------------------------------------------------------------------------------------------------------

  此报错跟网络环境有关，该网路环境下无法流畅的下载 github 仓库，导致电脑 SDK 下载失败。

--------------

Windows 下使用 `esp-idf-tools-setup-2.3.exe <link:https://dl.espressif.com/dl/esp-idf-tools-setup-2.3.exe>`__ 搭建环境，make menuconfig 出现如下错误：
------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code:: shell

    -- Warning: Did not find file Compiler/-ASM Configure
    -- Configuring incomplete , erros occurred !

  出现此错误的原因是没有因为未找到编译工程，可以切换目录到 esp-idf/get-started/hello\_world 示例中进行测试验证。

--------------

Windows 下使用 `esp-idf-tools-setup-2.2.exe <link:https://dl.espressif.com/dl/esp-idf-tools-setup-2.2.exe>`__ 安装过程中，出现 python 工具异常：
------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code:: text

    Installation has failed with exit code 1

  - 更新一下工具链：https://dl.espressif.com/dl/esp-idf-tools-setup-2.3.exe
  - 并且删除 idf_tools.py 中过时的选项 "--no-site-packages"

--------------

Windows 下安装编译环境出现 ``Download failed: 安全频道支持出错``？
------------------------------------------------------------------

  这是因为 Windows 系统已经默认不开启对 SSl3.0 的支持。
  修改方法：在 `控制面版` 中找到 ``internet 选项``，并在其打开的窗口中选择 ``高级``，最后在 ``设置`` 中勾选 ``使用 SSL 3.0``。

--------------

Windows 下执行export.bat，提示cmake、gdbgui版本错误：
---------------------------------------------------------
  .. code:: text

    -- C:\Users\xxxx\.espressif\tools\cmake\3.16.4\bin
    -- The following Python requirements are not satisfied:
    -- gdbgui>=0.13.2.0

  这个问题是由于上游的 gdbgui 发生了更新，并且导致与低版本的 python 不兼容，目前的解决方法是：手动修改 esp-idf 根目录下的 ``requirements.txt``，找到 gdbdui 那条，修给成：``gdbgui==0.13.2.0``

--------------

将版本从v3.3更新至最新版本后，使用 idf.menuconfig 及 idf.build 报错：
-------------------------------------------------------------------------

  - 按照 `快速入门 <link:https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html>`__ 重新搭建一下环境
  - 把 hello_world 目录下的 build 和 sdkconfig 删除

--------------

如果同时要开发 esp32 和 esp8266 ,该怎样设置 ``PATH`` 和 ``IDF_PATH`` ？
------------------------------------------------------------------------

  - PATH 是没有影响的，可以放在一起: export PATH="$HOME/esp/xtensa-esp32-elf/bin:$HOME/esp/xtensa-lx106-elf/bin:$PATH"
  - IDF_PATH 的话，可以在工程的 Makefile 里强制指定：
    在基于 esp32 的工程项目里使用： ``IDF_PATH = $(HOME)/esp/esp-idf`` ； 在基于 esp8266 的工程项目里使用： ``IDF_PATH = $(HOME)/esp/ESP8266_RTOS_SDK``
