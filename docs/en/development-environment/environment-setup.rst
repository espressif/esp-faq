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

When setting up ESP32-S2 environment using command ``idf.py set-target esp32-s2``, an error occurred as “Error: No such command 'set-target'”. What could be the reason?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The esp-idf is adapted to ESP32-S2 from release/v4.2, thus setting up ESP32-S2 environment in previous versions will cause errors. In this case, when using command ``idf.py set-target esp32-s2``, there will be error as "Error: No such command 'set-target'".
  - It is recommended to perform tests and development on ESP32-S2 using esp-idf release/v4.2 and later versions. For more information, please refer to `ESP32-S2 Get Started <https://docs.espressif.com/projects/esp-idf/en/latest/esp32s2/get-started/>`_.

--------------

When using idf.py menuconfig to build, how to deal with errors as "Configuring incomplete, errors occured"?
--------------------------------------------------------------------------------------------------------------------------

  Please check your CMake version first using ``camke --version``. If it is lower than version 3.10.0, please update your CMake version:

  - Download CMake: https://CMake.org/download/.
  - For details, please refer to http://www.mamicode.com/info-detail-2594302.html.

--------------

When installing esp-idf version master using ESP-IDF Tools 2.3 in Windows system, an error occurred as: Installation has failed with exit code 2. What could be the reason?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  This is related to the bad network environment. The github repository cannot be downloaded smoothly under such network environment, causing the SDK failed downloading on your PC.

--------------

When setting up environment using `esp-idf-tools-setup-2.3.exe <link:https://dl.espressif.com/dl/esp-idf-tools-setup-2.3.exe>`_ in Windows system, errors occurred in "make menuconfig": 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code:: shell

    -- Warning: Did not find file Compiler/-ASM Configure
    -- Configuring incomplete, erros occurred!

  This is because the system could not find the compiling tool. You can test and verify this in example esp-idf/examples/get-started/hello_world.

--------------

When using `esp-idf-tools-setup-2.2.exe <link:https://dl.espressif.com/dl/esp-idf-tools-setup-2.2.exe>`_ in Windows system, a python error occurred during the installation:
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code:: text

    Installation has failed with exit code 1

  1. Update your tool chain: https://dl.espressif.com/dl/esp-idf-tools-setup-2.3.exe
  2. Remove the obsolete option "--no-site-packages" from idf_tools.py

--------------

What should I do if I get ``Download failed: security channel support error`` when installing build environment in Windows system?
-------------------------------------------------------------------------------------------------------------------------------------------------

  This is due to the Windows system has disabled the SSl3.0 support by default.
  
  Solution: Go to `Control Panel` and find ``Internet option``, select ``Advanced`` and check the ``use SSL 3.0`` option.

--------------

When executing export.bat in Windows system, what should I do if I get CMake, gdbgui version errors?
---------------------------------------------------------------------------------------------------------------------
  .. code:: text

    C:\Users\xxxx\.espressif\tools\cmake\3.16.4\bin
    The following Python requirements are not satisfied:
    gdbgui>=0.13.2.0

  This is because the upstream gdbgui has been updated, thus it is not compatible with the low version of python. The current solution is to manually modify the root file ``requirements.txt`` in esp-idf by changing the description of gdbgui version to ``gdbgui==0.13.2.0``.

--------------

Errors occurred when using idf.menuconfig and idf.build after updating the idf version from v3.3 to the latest one:
-----------------------------------------------------------------------------------------------------------------------------

  - Rebuild the environment following `Get Started <link:https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html>`_.
  - Remove build and sdkconfig under the hello_world directory.

--------------

How to configure ``PATH`` and ``IDF_PATH`` when developing ESP32 and ESP8266 simultaneously?
--------------------------------------------------------------------------------------------------------

  - For ``PATH``, there is no need to do extra configurations. You can put them together as: export PATH="$HOME/esp/xtensa-esp32-elf/bin:$HOME/esp/xtensa-lx106-elf/bin:$PATH".
  - For ``IDF_PATH``, you can specify it for separate chips as:
    
    In ESP32 related projects, use ``IDF_PATH = $(HOME)/esp/esp-idf``; in ESP8266 related projects, use ``IDF_PATH = $(HOME)/esp/ESP8266_RTOS_SDK``.
