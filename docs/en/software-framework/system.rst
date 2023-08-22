System
======

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

My application does not really need the watchdog timer, can I disable it?
-----------------------------------------------------------------------------

There are two types of watchdog in ESP-IDF: task watchdog and interrupt watchdog. You can disable these two types of watchdog in menuconfig. For more details, please refer to `Watchdogs <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/get-started/index.html>`_.

--------------

What are the differences between RTOS SDK and Non-OS SDK?
-----------------------------------------------------------

  The main differences are as follows:

  **Non-OS SDK**

  - Non-OS SDK uses timers and callbacks as the main way to perform various functions - nested events and functions triggered by certain conditions. Non-OS SDK uses the espconn network interface; users need to develop their software according to the usage rules of the espconn interface.

  **RTOS SDK**

  - FreeRTOS SDK is based on FreeRTOS , a multi-tasking OS. You can use the standard FreeRTOS interfaces to realize resource management, recycling operations, execution delay, inter-task messaging and synchronization, and other task-oriented process design approaches. For the specifics of interface methods, please refer to the official website of FreeRTOS or the book USING THE FreeRTOS REAL TIME KERNEL-A Practical Guide.
  - The network operation interface in RTOS SDK is the standard lwIP API. RTOS SDK provides a package which enables BSD Socket API interface. Users can directly use the socket API to develop software applications; and port other applications from other platforms using socket API to ESP8266, effectively reducing the learning and development cost arising from platform switch.
  - RTOS SDK introduces cJSON library whose functions make it easier to parse JSON packets.
  - RTOS is compatible with Non-OS SDK in Wi-Fi interfaces, SmartConfig interfaces, Sniffer related interfaces, system interfaces, timer interface, FOTA interfaces and peripheral driver interfaces, but does not support the AT implementation.

--------------

Why does the log output ets_main.c when ESP8266 starts?
----------------------------------------------------------

  If ESP8266 prints ``ets_main.c`` when it starts, it indicates there are no programs that can be operated. Please check the binary file and burn address if you encounter this issue.

--------------

Why do I get compile errors when using IRAM_ATTR in Non-OS SDK?
-------------------------------------------------------------------

  The default function attribute is IRAM_ATTR in Non-OS SDK. Therefore, if you want the function to reside in IRAM, please leave out the ``ICACHE_FLASH_ATTR`` attribution in the function definition/declaration.

--------------

Where is main function in ESP8266?
-----------------------------------

  - ESP8266 SDK does not provide main function. Main function is stored in first-stage bootloader in ROM, which is used to load second-stage bootloader. The entry function of the second-stage bootloader is ets_main. After startup, the user_init in the user application will be loaded to lead the user to the program.

---------------------

Which part of ESP8266 partition-tables should be paid special attention to?
--------------------------------------------------------------------------------------------

  Compared to those of ESP32, partition-tables of ESP8266 have some special requirements on OTA partitions due to cache characteristics of ESP8266. For details, please refer to `Offset & Size of ESP8266 Partition Tables <https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/api-guides/partition-tables.html#offset-size>`__。

--------------

Is it possible to compile the binaries in application layer and bottom layer separately?
--------------------------------------------------------------------------------------------

  No, they cannot be compiled separately.

--------------

How can I to reduce the IRAM occupied by the ESP32 system?
--------------------------------------------------------------------

  - Please disable ``menuconfig`` > ``Component config`` > ``LWIP`` > ``Enable LWIP IRAM optimization`` by typing ``N``.
  - Please change the configurations in ``menuconfig`` > ``Compiler option`` > ``Optimization Level`` > ``Optimize for size (-Os)``.
  - Please disable ``WiFi IRAM speed optimization (N)`` and ``WiFi RX IRAM speed optimization (N)`` in ``menuconfig`` > ``Component config`` > ``wifi``.
  - For more details, please refer to `Minimizing RAM Usage <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/performance/ram-usage.html>`__。

----------------------

How can I optimize the size of binary files compiled by ESP32?
---------------------------------------------------------------

  - Please optimize GCC compilation by ``idf.py menuconfig`` > ``Compiler options`` > ``Optimization level (Optimize for size(-Os))``。
  - You can also optimize your code to improve the code reusability, and you can also adjust the log level to only print necessary logs.
  - For more details, please refer to `Minimizing Binary Size <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/performance/size.html>`__。


-----------------

How can I turn off log output in ESP32？
--------------------------------------------------------------------

  - You can turn off the bootloader log by setting ``menuconfig`` > ``bootloader config`` > ``bootloader log verbosity`` to ``No output``.
  - You can turn off the program log by setting ``menuconfig`` > ``Component config`` > ``log output`` > ``Default log verbosity`` to ``No output``.
  - For ESP-IDF release/v4.3 and earlier versions, you can turn off UART0 output log by ``menuconfig`` > ``Component Config`` > ``Common ESP-related`` > ``Channel for console output`` > ``None``.
  - For ESP-IDF release/v4.4 and later versions, you can turn off UART0 output log by ``Component config`` > ``ESP System Settings`` > ``Channel for console output`` > ``None``.

------------------

How to modify the GPIO used for log output on ESP32?
-------------------------------------------------------------------------------------------------

  - Go to ``menuconfig`` > ``Component Config`` > ``ESP System Settings`` > ``Channel for console output`` > ``Custom UART`` and select the UART port.
  - Go back to the previous level of menu, find the options `UART TX on GPIO#` and `UART RX on GPIO#`, and use them to modify the log output GPIO.

--------------

When ESP8266 is in Deep sleep mode, can the data stored in RTC Memory work?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - When ESP8266 is in Deep sleep mode, only the RTC timer continues to work. The data saved in the RTC Memory will not run, but can still be saved here. However, the data saved in RTC memory will lose after ESP8266 is powered off.

---------------------

What is the maximum length of the NVS Key for ESP32?
-------------------------------------------------------------------------------------------------------------------------

  - The maximum length of the NVS key for ESP32 is 15 characters, which cannot be changed. Please see the description of `key-value pair <https://docs.espressif.com/projects/esp-idf/en/release-v4.3/esp32/api-reference/storage/nvs_flash.html#id4>`_.
  - But you can use the value of `nvs_set_str() <https://docs.espressif.com/projects/esp-idf/en/release-v4.3/esp32/api-reference/storage/nvs_flash.html#_CPPv411nvs_set_str12nvs_handle_tPKcPKc>`_ to store data.

---------------------

Does the cJSON in ESP-IDF release/v4.2 support uint64_t data analysis?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - No. The cJSON library has restrictions on parsing long integers, and the longest type is Double.

---------------------

Given that the GDB debugging function is working before the flash encryption is disabled, then why does the device keeps restarting during the GDB debugging after the flash encryption is enabled?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The JTAG debugging function will be disabled by default when flash encryption or secure boot is enabled. For more information, please refer to `JTAG with Flash Encryption or Secure Boot <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/jtag-debugging/tips-and-quirks.html#jtag-with-flash-encryption-or-secure-boot>`_.

---------------------

While using mobile's hotpot for an ESP32 to download the OTA firmware, after a few seconds when turning of the hotspot and restarts ESP32, the program sticks in the OTA operation (the same situation for plugging and unplugging the wan port network cable when using a router), why?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - This is a normal situation based on the protocol. When using the `esp_https_ota` component to run OTA, you can set the network timeout value (via `http_config->timeout_ms`) to 10 ~ 30 s (not too low) and enable `http_config->keep_alive_enable` to see if there are any errors in the link layer.
  - If you are using an self-implemented OTA module, please set a timeout value via the `select` configuration or enable the TCP keep-alive mechanism to detect the link layer.

-----------------

Which GPIOs can be used to wake up ESP32-C3 from Deep-Sleep mode?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Only GPIO0 ~ GPIO5 in VDD3P3_RTC domain can be used to wake up ESP32-C3 from Deep-sleep mode. Please read Chapter 5.9.1 Power Supplies of GPIO Pins in `ESP32-C3 Technical Reference Manual <https://www.espressif.com/sites/default/files/documentation/esp32-c3_technical_reference_manual_en.pdf>`_.

------------------

When using the ESP-WROOM-02D module with a battery for power supply, are there any risks in frequently formatted reading and writing flash as the battery is low (the module barely starts up)?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Frequent formatting and read/write operations on flash storage in low power situations may have some risks. It may not work properly or be susceptible to cause errors under low power conditions. In addition, frequent formatting and read/write operations in this situation may lead to the following risks:

  - Data loss or corruption: Flash storage may not be able to write data properly under low power conditions. Frequent formatting and read/write operations may result in data loss or corruption.
  - Module crash or damage: Frequent formatting and read/write operations on flash storage in low power conditions will consume the module's power, which may cause the module to crash or damage.

  Therefore, it is recommended to minimize access and operations on flash storage in low power conditions and avoid frequent formatting and read/write operations. If formatting and read/write operations are necessary, ensure that the module has sufficient power, backup data before the operation to prevent data loss, use low power mode and optimize code to minimize power consumption.

---------------------

How to check the maximum stack size used by a thread for ESP32?
------------------------------------------------------------------------------------------------------------------

  - You can call the `UBaseType_t uxTaskGetStackHighWaterMark(TaskHandle_t xTask) <https://www.freertos.org/uxTaskGetStackHighWaterMark.html>`_ function. This function will return the minimum remaining stack space after the task is started.

----------------

What is the meaning of the " SW_CPU_RESET" log when using ESP32?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

  On ESP32, the "SW_CPU_RESET" log is usually caused by abnormal termination of the program. 
  ESP32 has two cores, the main core and the assistant core. In some cases, if the program is executed on the main core and some abnormal situations occur, such as accessing illegal addresses or unhandled interrupts, it may cause the main core to enter into an exception state and restart. When this happens, ESP32 will print the "SW_CPU_RESET" log on the serial terminal (UART).
  In addition, when developing applications using ESP-IDF, it is also possible to call the esp_restart() function in the application to restart ESP32. In this case, ESP32 will also print the "SW_CPU_RESET" log on the serial terminal.
  It should be noted that the appearance of the "SW_CPU_RESET" log does not necessarily mean that there is a problem with the program or ESP32 hardware. It may be a normal phenomenon caused by some abnormal situations. However, if the program frequently encounters exceptions and restarts, it is necessary to debug and troubleshoot the problem. You can determine the reason of the problem by checking the program log and hardware device status.

----------------

For ESP32 products, when testing NVS separately, I found it occupies a lot of memory. What is the reason?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Please check the partition table settings. It is recommended to set a smaller NVS data partition in the partition table to test. The larger the NVS data partition setting, the more memory it will occupy.

-----------------------------------------------------------------------------------------------------

How do I change the system time of a module ?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32 | ESP32 | ESP32-C3:

 - You can use the c language ``time()`` interface to set the system time.

---------------------------------------

During the OTA upgrade process, an ESP_ERR_OTA_VALIDATE_FAILED error occurred after calling esp_ota_end, how to troubleshoot such issue?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  :CHIP\: ESP32:

  - Generally it is caused by the error content in the downloaded firmware. You can dump out such content via `read_flash <https://docs.espressif.com/projects/esptool/en/latest/esp32/esptool/basic-commands.html#read-flash-contents-read-flash>`_ in `esptool <https://github.com/espressif/esptool>`_ from your module. Then use the Beyond Compare tool to compare the two bin files in hexadecimal to see which part of the bin file is downloaded incorrectly.

-------------------------

How does ESP8266-RTOS-SDK store data to RTC memory?
------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The definition method of storing data in RTC memory is as follows:

  .. code::text

    #define RTC_DATA_ATTR _SECTION_ATTR_IMPL(".rtc.data", __COUNTER__)

  - Please refer to the description in `esp_attr.h <https://github.com/espressif/ESP8266_RTOS_SDK/blob/release/v3.4/components/esp8266/include/esp_attr.h>`_.

-------------------------

After waking up from Deep-sleep mode, where does ESP8266 start boot?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - After ESP8266 wakes up from Deep-sleep mode, the device will boots up from ``user_init``. Please refer to the description in `esp_deep_sleep() <https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/api-reference/system/sleep_modes.html?highlight=deep#_CPPv414esp_deep_sleep8uint64_t>`__.

-------------------------

When will the RTC clock be reset?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Any reset (except the power-up reset) or sleep mode settings will not reset the RTC clock.

-------------------------

After using the ``AT+GSLP`` command to enter Deep-sleep mode for ESP32, can it be awakened by pulling down the EN pin?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes, but it is not recommended.
  - Deep-sleep wakeup can be awakened by RTC_GPIO. Please refer to `ESP32 Technical Reference Manual <https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf>`_.

-------------------

When multiple threads want to use the watchdog of ESP32, should each thread enable the watchdog individually?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes, please see `Task watchdog instructions <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/wdts.html?highlight=wdt#task-watchdog-timer>`_.

-------------------------

When using the release/v3.3 version of ESP8266-RTOS-SDK, how to enter Light-sleep mode?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - First set the wake-up mode of Light-sleep mode, please refer to `ESP8266_RTOS_SDK/components/esp8266/include/esp_sleep.h <https://github.com/espressif/ESP8266_RTOS_SDK/blob/release/v3.3/components/esp8266/include/esp_sleep.h>`_.

  - Then use the `esp_light_sleep_start() <https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/api-reference/system/sleep_modes.html?highlight=esp_light_sleep_start%28%29#_CPPv421esp_light_sleep_startv>`_ API to enter Light-sleep mode.

  - You can refer to the `esp-idf/examples/system/light_sleep/main/light_sleep_example_main.c <https://github.com/espressif/esp-idf/blob/release/v4.2/examples/system/light_sleep/main/light_sleep_example_main.c>`_ example for implementation logic.

  - Please read `API Reference <https://docs.espressif.com/projects/esp8266-rtos-sdk/en/release-v3.3/api-reference/system/sleep_modes.html#sleep-modes>`_ for API descriptions about sleep modes in ESP8266-RTOS-SDK.

-------------------------

How to wake up ESP8266 in Deep sleep mode?
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The ESP8266 can only be awakened from Deep sleep mode via RTC Timer, the timing duration is set by user via esp_deep_sleep, and GPIO16(XPD_DCDC) should be connected to EXT_RSTB through a 0 Ω resistor to support such function. Please refer to `related API descriptions <https://docs.espressif.com/ projects/esp8266-rtos-sdk/en/latest/api-reference/system/sleep_modes.html?highlight=deep#_CPPv414esp_deep_sleep8uint64_t>`_.

---------------------

When using the ESP32-WROVER module, there is a problem of battery jitter or abnormal power-off and power-on, causing the system to crash and fail to wake up. What is the reason?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Application scenario: The current is about 12 uA during sleep. When the battery is unplugged or the product is shaken, it will cause power failure, but there is still electricity in the capacitor. During the process of discharging ESP32 from 3.3 V to 0 V, ESP32 will fail to wake up when powered on again with 3.3 V.

  - Please check whether the chip VCC and EN meet the power-on sequence requirements.
  - Consider adding a reset chip to ensure normal timing.
  - For ESP32 power-on and reset timing description, please refer to `ESP32 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_.

--------------

How to flash a customized mac address?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - You can start by understanding the MAC mechanics of ESP modules, please refer to `Introduction to Mac Addresses <https://docs.espressif.com/projects/esp-idf/en/latest/api-reference/system/system.html?highlight=MAC% 20address/>`_. There are currently 2 options for burning customized MAC addresses:

  - Option 1: directly flash it into efuse blk3.
  - Option 2: Store in flash. It is not recommended to store the MAC address in the default NVS partition. It is recommended to create a customized NVS partition for storing customized Mac addresses. For more information on the use of customized MAC addresses, please refer to `base_mac_address <https://github.com/espressif/esp-idf/tree/master/examples/ system/base_mac_address/>`_.

----------------------

When ESP32 uses esp_timer, network communication or Bluetooth communication is abnormal. What is the reason?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - esp_timer is a high-precision hardware timer component, and some background components also use it to complete some system tasks. When using esp_timer, please do not call delay and blocking APIs in the callback function of the timer, and try to ensure that the function is executed as quickly as possible, so as not to affect the performance of other system components.
  - If you do not need very high time precision, please use the timer component `xTimer <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/freertos.html#timer-api>`_ in FreeRTOS.

--------------

With ESP32, are there any return instructions if I skip to a function using the ``jump`` instruction in ULP？
-----------------------------------------------------------------------------------------------------------------------------------------------

  Please see `here <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/ulp_instruction_set.html>`_ for ULP CPU instructions list and corresponding specifications. Normally, a general register is used for return instructions to store backup PC addresses for later jumping backs. Since there are only four general registers in ULP for now, please make proper use of them.

--------------

How to adjust the warning level for project build?
-------------------------------------------------------------------------------------------------

  When building the project, it is found that some warnings being treated as errors, causing build failure, as follows:

  .. code:: text

    error: format '%d' expects argument of type 'int *', but argument 3 has type 'uint32_t *' {aka 'long unsigned int *'} [-Werror=format=]

  For the error above, you can modify compilation flags at a component level (in component CMakeLists.txt) or at a project level (in project CMakeLists.txt). These two ways have roughly the same effect.

  - To modify compilation flags for a specific component, use the standard CMake function ``target_compile_options``. Please refer to `Controlling Component Compilation <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/build-system.html#controlling-component-compilation>`_. For an example of target_compile_options at the component level, please see `CMakeLists.txt#L3 <https://github.com/espressif/esp-idf/blob/4d14c2ef2d9d08cd1dcbb68a8bb0d76a666e2b4b/examples/bluetooth/bluedroid/ble/ble_ancs/main/CMakeLists.txt#L3>`_.
  - To modify compilation flags for the whole project, either use standard CMake function ``add_compile_options`` or IDF-specific function ``idf_build_set_property`` to set ``COMPILE_OPTIONS`` property. Please refer to `overriding-default-build-specifications <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/build-system.html#overriding-default-build-specifications>`_.

------------------

The firmware compiled based on the ESP-IDF SDK varies as it contains the information about ``IDF_PATH`` and compilation time. How to remove that information?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - For SDK v5.0 and the above versions, you can enable the ``CONFIG_APP_REPRODUCIBLE_BUILD`` configuration option. In doing so, the application built upon ESP-IDF does not depend on the build environment and both the .elf file and .bin file of the application remain unchanged even if the following variables change:

    - Directory where the project is located
    - Directory where ESP-IDF is located (IDF_PATH)
    - Build time

    Please refer to the `Reproducible Builds <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/reproducible-builds.html#reproducible-builds>`_ description.

  - For SDK versions below v5.0, you can disable ``CONFIG_APP_COMPILE_TIME_DATE=n`` to remove the built timestamp information and enable ``COMPILER_HIDE_PATHS_MACROS=y`` to hide ``IDF_PATH``.

--------------

When I downloaded the official application hello_world using ESP32-S3-DevKitM-1, the following error occurred. What is the reason for that?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code:: text

    ESP-ROM:esp32s3-20210327
    Build:Mar 27 2021
    rst:0x7 (TG0WDT_SYS_RST),boot:0x8 (SPI_FAST_FLASH_BOOT)
    Saved PC:0x40043ac8
    Invalid chip id. expected 9 read 4. bootloader for wrong chip?
    ets_main.c 329


  - The current error may be related to the chip version on the development board or to the fact that the software version of the esp-idf SDK is not the official production version. The chip (ROM) bootloader expects the chip ID is 9, which is the production version of the chip (not a test version). However, in the secondary bootloader header, it sees the chip ID is 4, which is the beta version of the chip. Please refer to the description in `esp-idf/issues/7960 <https://github.com/espressif/esp-idf/issues/7960>`_ .

  - The actual version of the chip can be obtained by the command ``esptool.py chip_id``. If the chip version is the production version, this error is related to the version of the used esp-idf SDK. For ESP32-S3 series products, esp-idf release/v4.4 and later are necessary.

----------------

What is the accuracy of the internal 150 kHz RTC of ESP32 series chips?
----------------------------------------------------------------------------------------------------------------------------------------------

  - The accuracy of the internal 150 kHz RTC of ESP32 series chips is ±5%.

--------------

What versions of esp-idf SDK are supported by ESP32-D0WDR2-V3 chip?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Supported IDF versions are: v4.4.1, v4.3.3, v4.2.3, and v4.1.3.

------------------

When I test OTA applications based on the ESP32 chip, can I delete the default factory partition in the partition table and set the address of the OTA_0 partition to 0x10000?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes. Please note that the offsets of partitions of any app type have to be aligned to 0x10000 (64K).

---------------------

Why can I not burn data to BLOCK3 of ESP32-C3 eFuse with ``espefuse.py burn_key``?
---------------------------------------------------------------------------------------------------------

  - ``espefuse.py burn_key`` can only burn data to eFuse blocks of the KEY_DATA type. However, BLOCK3 of ESP32-C3 is of the USR_DATA type by default.
  - You can burn data to eFuse blocks of the USR_DATA type with ``espefuse.py burn_block_data``.

------------------------

Why do different ESP32 modules have different flash erase time?
----------------------------------------------------------------------------------------------------------------------------------------------

  - This is caused by different type of flash models. Some module of flash don't have a mechanism for passing empty blocks when erasing, so it takes longer time.

--------------

Why I encountered the following error after I run the firmware based on the esp-idf SDK?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code:: text

    ***ERROR*** A stack overflow in task sys_evt has been detected.

  - The error is caused by insufficient system_event task stack. You can try to resolve it by increasing ``Component config`` > ``ESP System Setting`` > ``Event loop task stack size``. However, the overflow occurs because too much logic is being processed within system_event. It is not recommended as it might lead to delayed handling of subsequent events. We suggest forwarding this event to other tasks for processing, either through a queue or other operations.
