Environment setup
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

--------------

When setting up ESP32-S2 environment using command ``idf.py set-target esp32s2``, an error occurred as "Error: No such command 'set-target'". What could be the reason?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The ESP-IDF is adapted to ESP32-S2 from release/v4.2, thus setting up ESP32-S2 environment in previous versions will cause errors. In this case, when using command ``idf.py set-target esp32s2``, there will be error as "Error: No such command 'set-target'". It is recommended to perform tests and development on ESP32-S2 using ESP-IDF release/v4.2 and later versions. For more information, please refer to `ESP32-S2 Get Started <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s2/get-started/>`_.
  - To check which ESP chips are supported by different ESP-IDF versions, please refer to `ESP-IDF Release and SoC Compatibility <https://github.com/espressif/esp-idf#esp-idf-release-and-soc-compatibility>`_.

--------------

When installing ESP-IDF version master using ESP-IDF Tools 2.3 in Windows system, an error occurred as: Installation has failed with exit code 2. What could be the reason?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  This is related to the bad network environment. The Github repository cannot be downloaded smoothly under such network environment, causing SDK download failure on your PC. If you encounter Github access problems, it is recommended to use the **offline** version of the latest `ESP-IDF Windows Installer <https://dl.espressif.com/dl/esp-idf/>`_.

--------------

When setting up environment using `esp-idf-tools-setup-2.3.exe <link:https://dl.espressif.com/dl/esp-idf-tools-setup-2.3.exe>`_ on Windows, errors occurred when ``make menuconfig`` is executed: 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code:: shell

    -- Warning: Did not find file Compiler/-ASM Configure
    -- Configuring incomplete, errors occurred!

  This is because the system could not find the project to be compiled. You need to change directory to the ESP-IDF project before running commands to configure and compile the project. For example, to build the project hello world, go to ``esp-idf/examples/get-started/hello_world`` before running the commands.

--------------

When using `esp-idf-tools-setup-2.2.exe <link:https://dl.espressif.com/dl/esp-idf-tools-setup-2.2.exe>`_ in Windows system, a python error occurred during the installation:
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code:: text

    Installation has failed with exit code 1

  1. Update your tool chain: https://dl.espressif.com/dl/esp-idf-tools-setup-2.3.exe
  2. Remove the obsolete option "--no-site-packages" from idf_tools.py

--------------

What should I do if I get ``Download failed: security channel support error`` when installing build environment in the Windows system?
-------------------------------------------------------------------------------------------------------------------------------------------------

  This is because the Windows system has disabled the default support for SSl3.0.
  
  Solution: Go to `Control Panel` and find ``Internet option``, select ``Advanced``, and check the ``use SSL 3.0`` option.

--------------

When executing export.bat in Windows system, what should I do if I get CMake and gdbgui version errors?
---------------------------------------------------------------------------------------------------------------------
  .. code:: text

    C:\Users\xxxx\.espressif\tools\cmake\3.16.4\bin
    The following Python requirements are not satisfied:
    gdbgui>=0.13.2.0

  This is because the upstream gdbgui has been updated, thus it is not compatible with the low version of python. The current solution is to manually modify the root file ``requirements.txt`` in ESP-IDF by changing the description of gdbgui version to ``gdbgui==0.13.2.0``.

--------------

Errors occurred when using idf.menuconfig and idf.build after updating the ESP-IDF version from v3.3 to the latest one:
-----------------------------------------------------------------------------------------------------------------------------------

  - Rebuild the environment following `Get Started <link:https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html>`_.
  - Remove build directory ``build`` and configuration file ``sdkconfig`` under the hello_world directory.

--------------

How to configure ``PATH`` and ``IDF_PATH`` when developing ESP32 and ESP8266 simultaneously?
--------------------------------------------------------------------------------------------------------

  - For ``PATH``, there is no need to do extra configurations. You can put them together as: export PATH="$HOME/esp/xtensa-esp32-elf/bin:$HOME/esp/xtensa-lx106-elf/bin:$PATH".
  - For ``IDF_PATH``, you can specify it for separate chips as:
    
    In ESP32 related projects, use ``IDF_PATH = $(HOME)/esp/esp-idf``. In ESP8266 related projects, use ``IDF_PATH = $(HOME)/esp/ESP8266_RTOS_SDK``.

----------------

Do I need to use command ``idf.py set-target`` every time when switching to another project?
---------------------------------------------------------------------------------------------

  When building the project with ``idf.py build``, the target is determined as follows:

  1. If the build directory ``build`` already exists, the system will use the target the project was previously built for. It is stored in CMakeCache.txt file in the ``build`` directory.
  2. Alternatively, if the build directory doesn't exist, the system will check if the ``sdkconfig`` file exists, and use the target specified there.
  3. If both the build directory and ``sdkconfig`` file exist with different targets specified, the system will report an error. This shouldn't happen normally, unless ``sdkconfig`` was changed manually without deleting the build directory.
  4. If neither ``sdkconfig`` file nor build directory exists, it can be considered to use ``IDF_TARGET`` to set the target as a CMake variable or environment variable. If this variable is set and is different from the target specified in ``sdkconfig`` or in the build directory, the system will also report an error.
  5. Finally, if ``sdkconfig`` doesn't exist, build directory doesn't exist, and the target is not set via ``IDF_TARGET``, then the system will use the default value. The default value can be set in ``sdkconfig.defaults``.
  6. If the target isn't set using any of the above methods, then the system will build for ESP32 target.

  To answer your question:

  - ``idf.py set-target`` stores the selected target in the project's build directory and ``sdkconfig`` file, not in the terminal environment. So, once the project is configured and built once for a certain target, if you switch to a different directory and build another project, then come back, the target will not change, and will be the same as previously set for this project. And it's not necessary to run ``idf.py set-target`` again other than to switch to a different target.
  - If you want to make the project built for certain target by default, add ``CONFIG_IDF_TARGET="esp32s2"`` to the ``sdkconfig.defaults`` file of the project. After this, if ``sdkconfig`` file doesn't exist and build directory doesn't exist, idf.py build command will build for that target specified in ``sdkconfig.defaults``.
  - ``idf.py set-target`` command can still be used to override the default target set in ``sdkconfig.defaults``.

--------------

How to know the version of ESP-IDF, is it recorded in a certain document? 
----------------------------------------------------------------------------------------------------------------------------

  - Command line: You can obtain the version number by inputting ``idf.py --version`` in the terminal with an IDF environment. 
  - CMake script: You can obtain the version number through the variable ``${IDF_VERSION_MAJOR}.${IDF_VERSION_MINOR}.${IDF_VERSION_PATCH}``.
  - Code compilation: You can obtain the version number by calling ``esp_get_idf_version`` during code compilation or directly using the macro definition of version in "components/esp_common/include/esp_idf_version.h".

---------------

How to optimize ESP-IDF compilation in Windows environment?
---------------------------------------------------------------------------------------------------

  - Please add the directories of ESP-IDF source code and compiler ``.espressif`` to the exclusions of anti-virus program.

-------------------

Is there an esptool that can be used directly on Windows?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - You can go to `esptool --> Releases <https://github.com/espressif/esptool/releases>`_ and download the Windows version of the esptool from the Asset column on the drop-down page. 
