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

为 ESP32-S2 搭建环境时，使用 ``idf.py set-target esp32s2`` 指令，显示 "Error: No such command 'set-target'"，为什么？
----------------------------------------------------------------------------------------------------------------------------------------------------

  - 因为 ESP-IDF 是从 release/v4.2 版本开始适配 ESP32-S2 的，所以如果在之前的 ESP-IDF 版本上搭建 ESP32-S2 环境，就会出现错误。例如使用指令 ``idf.py set-target esp32s2`` 时，会报错 "Error: No such command 'set-target'"。建议使用 ESP-IDF release/v4.2 及以后版本进行 ESP32-S2 的测试开发。更多请参考 `ESP32-S2 入门指南 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32s2/get-started/>`_。
  - 不同 ESP-IDF 版本的 ESP 芯片支持情况，请查阅 `ESP-IDF Release and SoC Compatibility <https://github.com/espressif/esp-idf/blob/master/README_CN.md#esp-idf-%E4%B8%8E%E4%B9%90%E9%91%AB%E8%8A%AF%E7%89%87>`__。

--------------

Windows 下使用 ESP-IDF Tools 2.3 工具安装 master 版本的 ESP-IDF 出现错误：Installation has failed with exit code 2，是什么原因？
----------------------------------------------------------------------------------------------------------------------------------------------

  此报错跟网络环境有关，代表在该网络环境下无法流畅地拉取 Github 仓库，导致电脑 SDK 下载失败。如遇到 Github 访问问题，推荐使用最新 `Windows 安装工具 <https://dl.espressif.com/dl/esp-idf/>`_ 中的 **offline** 版本。

--------------

Windows 下使用 `esp-idf-tools <https://dl.espressif.com/dl/esp-idf/?idf=4.4>`_ 搭建环境，运行 ``make menuconfig`` 出现如下错误：
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code:: shell

    -- Warning: Did not find file Compiler/-ASM Configure
    -- Configuring incomplete, errors occurred!

  出现此错误的原因是未找到编译工程。您需要将目录切换至 ESP-IDF 工程后，再运行配置、编译等指令。例如，编译 hello world 工程时，需要将目录切换至 ``esp-idf/examples/get-started/hello_world``，然后再运行配置、编译等指令。

--------------

Windows 下使用 `esp-idf-tools <https://dl.espressif.com/dl/esp-idf/?idf=4.4>`_ 安装过程中，出现 python 工具异常：
------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code:: text

    Installation has failed with exit code 1

    
  此错误由网络环境不适合导致，请在使用工具时勾选 "通过 gitee 下载"。

--------------

Windows 下安装编译环境出现 ``Download failed: 安全频道支持出错``？
------------------------------------------------------------------

  这是因为 Windows 系统已经默认不开启对 SSl3.0 的支持。
  
  修改方法：在 `控制面版` 中找到 ``Internet 选项``，在其打开的窗口中选择 ``高级``，最后在 ``设置`` 中勾选 ``使用 SSL 3.0``。

--------------

Windows 下执行 export.bat，提示 CMake、gdbgui 版本错误：
------------------------------------------------------------------
  .. code:: text

    C:\Users\xxxx\.espressif\tools\cmake\3.16.4\bin
    The following Python requirements are not satisfied:
    gdbgui>=0.13.2.0

  这个问题是由于上游的 gdbgui 发生了更新，从而导致与低版本的 python 不兼容。目前的解决方法是：手动修改 ESP-IDF 根目录下的 ``requirements.txt``，找到 gdbdui 那条，修改成：``gdbgui==0.13.2.0``。

--------------

将版本从 v3.3 更新至最新版本后，使用 idf.menuconfig 及 idf.build 报错：
-------------------------------------------------------------------------

  - 请参照 `快速入门 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/get-started/index.html>`_ 重新搭建一下环境。
  - 删除 hello_world 项目文件夹下的编译目录 ``build`` 和配置文件 ``sdkconfig``。

--------------

如果同时要开发 ESP32 和 ESP8266，该怎样设置 ``PATH`` 和 ``IDF_PATH``？
------------------------------------------------------------------------

  - ``PATH`` 不受影响，可以放在一起: export PATH="$HOME/esp/xtensa-esp32-elf/bin:$HOME/esp/xtensa-lx106-elf/bin:$PATH"。
  - 对于 ``IDF_PATH``，可以在工程的 Makefile 里强制指定：
    
    在基于 ESP32 的工程项目里使用：``IDF_PATH = $(HOME)/esp/esp-idf``。在基于 ESP8266 的工程项目里使用：``IDF_PATH = $(HOME)/esp/ESP8266_RTOS_SDK``。

---------------

每一次切换项目时都需要重新调用 ``idf.py set-target`` 指令吗？
--------------------------------------------------------------------

  使用 ``idf.py build`` 编译项目时，target 的选择取决于：

  1. 如果编译目录 ``build`` 已经生成，系统将使用上一次编译时使用的 target。该参数存储于 ``build`` 文件夹中的 CMakeCache.txt 文件内。
  2. 如果还未生成编译目录，系统将检查 ``sdkconfig`` 文件，并使用其中定义的 target。
  3. 如果同时存在有编译目录和 ``sdkconfig`` 文件，且其中分别定义了不同的 target，系统将报错。但该情况一般不会发生，除非在未删除编译目录的情况下手动更改了 ``sdkconfig`` 文件。
  4. 如果 ``sdkconfig`` 文件或编译目录都不存在，可使用 ``IDF_TARGET`` 设置 target，作为 CMake 变量或环境变量。同样，如果该变量设置的 target 和 ``sdkconfig`` 文件或编译目录中定义的 target 不一致，系统也会报错。
  5. 最后，如果上述三种途径都未定义 target，系统将使用默认值。可在 ``sdkconfig.defaults`` 中设置默认的 target 值。
  6. 若未设定任何默认值，系统将使用 ESP32 进行编译。

  关于是否需要多次调用 ``idf.py set-target``：

  - ``idf.py set-target`` 指令会将配置的 target 值存储于项目下的编译目录和 ``sdkconfig`` 文件中，并非存储于终端环境。因此，一旦某个项目配置完成并使用 target 编译过一次后，你切换并编译了另一项目，再次切回上一项目时，其 target 不会改变，仍为上一次为这个项目配置的值，无需再次调用 ``idf.py set-target`` 指令重设。
  - 若想使项目自动编译某一默认的 target 值，请将默认值添加至项目的 ``sdkconfig.defaults`` 文件（如 ``CONFIG_IDF_TARGET="esp32s2"``）。此后，如果项目中未存在 ``sdkconfig`` 文件和编译目录，``idf.py build`` 将使用 ``sdkconfig.defaults`` 中定义的默认值进行编译。
  - ``idf.py set-target`` 指令定义的 target 值可覆盖 ``sdkconfig.defaults`` 中配置的值。

--------------

如何查看当前 ESP-IDF 的版本号，是否存在记录版本号的文件？
------------------------------------------------------------------------------------------------------------------------------

  - 命令行中获取版本号：可以通过在 IDF 环境中执行 ``idf.py --version`` 获取当前 IDF 版本号。
  - CMake 脚本中获取版本号：可以通过变量 ``${IDF_VERSION_MAJOR}.${IDF_VERSION_MINOR}.${IDF_VERSION_PATCH}`` 获取当前版本号。
  - 代码编译期间获取版本号：可以通过调用函数 ``esp_get_idf_version`` 查询，或直接使用 "components/esp_common/include/esp_idf_version.h" 中的版本号宏定义。

--------------

Windows 环境下 ESP-IDF 编译比较慢如何优化？
--------------------------------------------------------------------------------------------------

  - 请将 ESP-IDF 源码目录以及编译器目录 ``.espressif`` 添加到杀毒软件的排除项。
  
-----------------

是否有可以直接在 Windows 上使用的 esptool 工具？
---------------------------------------------------------------------------------------------------------------

  - 可以前往 `esptool ——> Releases <https://github.com/espressif/esptool/releases>`_，在下拉页面的 Asset 栏下载 Windows 版本的 esptool 工具。

-----------------

运行 `./install.sh` 时出现错误 `KeyError: 'idfSelectedId'` 可能是什么原因导致的？
---------------------------------------------------------------------------------------------------------------

  - 这是因为系统安装过 ESP-IDF v5.0 以上版本导致的，可以查看 `~/.espressif/idf-env.json` 文件中的配置。
  - 运行 `rm -rf ~/.espressif/idf-env.json` 解决。

-----------------

运行 `demo` 时出现包管理器组件依赖拉不下，出现失败 `Invaild manifest format`、 `Invalid dependency format`、 `unknown keys in dependency details: override_path`，可能是什么原因导致的？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 这是因为缺少组件依赖导致的，需要更新 `component-manager`。指令命令为 `pip install --upgrade idf-component-manager`。

--------------

使用 `ESP-IDf v4.4.8-Offline Installer 安装包 <https://dl.espressif.com/dl/esp-idf/?idf=4.4>`_ 安装 ESP-IDF CMD 环境后，直接编译 hello_world 例程，出现如下编译报错，是什么原因？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
  .. code:: text

    [1050/1065] Building C object esp-idf/main/CMakeFiles/__idf_main.dir/main.c.obj
    FAILED: esp-idf/main/CMakeFiles/__idf_main.dir/main.c.obj
    D:\esp\Espressif\tools\xtensa-esp32-elf\esp-2021r2-patch5-8.4.0\xtensa-esp32-elf\bin\xtensa-esp32-elf-gcc.exe: error: @-file refers to a directory
    [1058/1065] Building C object esp-idf/wifi_provisioning/CMakeFiles/__idf_wifi_provisioning.dir/src/scheme_softap.c.obj
    ninja: build stopped: subcommand failed.
    ninja failed with exit code 1

  - 从日志上看是在编译过程中缓存 `build/esp-idf/main/CMakeFiles/__idf_main.dir/ main.c.o.bj` 文件出错，这是在 ccache 调用编译器时生成的，与编译缓存有关。此问题在 v5.0 及之后的版本上做了修复。
  - 在 v4.4 版本的 ESP-IDF CMD 环境中，请使用 `idf.py --no-ccache build` 指令来编译工程。
  