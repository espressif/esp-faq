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

Is it possible to compile the binaries in application layer and bottom layer separately?
--------------------------------------------------------------------------------------------

  No, they cannot be compiled separately.

--------------

My application does not really need the watchdog timer, can I disable it?
----------------------------------------------------------------------------

  The current SDK allows disabling the software watchdog only. The following methods can be taken to avoid watchdog reset when user program occupies CPU for too long:

  - If your routine needs a time frame of duration between software reset and hardware watchdog reset, you may use system_soft_wdt_stop () to disable the software watchdog. After the program has been executed, you can restart the software watchdog with system_soft_wdt_restart ().
  - You may feed the watchdog in between your codes by adding system_soft_wdt_feed () so that the watchdog is updated before it issues a reset.

  The hardware watchdog interrupt interval is 0.8*2048 ms, that is 1638.4 ms. The interrupt handling interval is 0.8*8192 ms, equal to 6553.6 ms. The interrupt handling interval is the time limit to feed the watchdog after the interrupt occurs. If the interrupt handling interval expires, it will trigger a hardware watchdog reset. As a result, in the cases where there is only hardware watchdog, if a program runs for over 6553.6 ms, then it could cause a hardware watchdog reset. If the program runs for over 8192 ms, then it will invoke a watchdog reset for sure.

  The software watchdog is based on MAC timer and task arrangement. The interrupt interval is 1600 ms, so is the interrupt handling interval. As a result, in the cases where there are both software and hardware watchdogs, if a program runs for over 1600 ms, it could cause a software watchdog reset. If the program runs for over 3200 ms, it will invoke a watchdog reset for sure.

--------------

What are the differences between RTOS SDK and Non-OS SDK?
-----------------------------------------------------------
  The main differences are as follows:

  - Non-OS SDK

     Non-OS SDK uses timers and callbacks as the main way to perform various functions - nested events and functions triggered by certain conditions. Non-OS SDK uses the espconn network interface; users need to develop their software according to the usage rules of the espconn interface.

  - RTOS SDK

     1. FreeRTOS SDK is based on FreeRTOS , a multi-tasking OS. You can use the standard FreeRTOS interfaces to realize resource management, recycling operations, execution delay, inter-task messaging and synchronization, and other task-oriented process design approaches. For the specifics of interface methods, please refer to the official website of FreeRTOS or the book USING THE FreeRTOS REAL TIME KERNEL-A Practical Guide.
     2. The network operation interface in RTOS SDK is the standard lwIP API. RTOS SDK provides a package which enables BSD Socket API interface. Users can directly use the socket API to develop software applications; and port other applications from other platforms using socket API to ESP8266, effectively reducing the learning and development cost arising from platform switch.
     3. RTOS SDK introduces cJSON library whose functions make it easier to parse JSON packets.
     4. RTOS is compatible with Non-OS SDK in Wi-Fi interfaces, SmartConfig interfaces, Sniffer related interfaces, system interfaces, timer interface, FOTA interfaces and peripheral driver interfaces, but does not support the AT implementation.

--------------

Why do I get compile errors when using IRAM_ATTR in Non-OS SDK?
-------------------------------------------------------------------

  The default function attribute is IRAM_ATTR in Non-OS SDK. Therefore, if you want the function to reside in IRAM, please leave out the ``ICACHE_FLASH_ATTR`` attribution in the function definition/declaration.

--------------

Where is main function in ESP8266?
-----------------------------------

  - ESP8266 SDK does not provide main function.
  - Main function is stored in first-stage bootloader in ROM, which is used to load second-stage bootloader.
  - The entry function of the second-stage bootloader is ets_main. After startup, the user_init in the user application will be loaded to lead the user to the program.

---------------------

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

Why do different ESP32 modules have different flash erase time?
----------------------------------------------------------------------------------------------------------------------------------------------

  - This is caused by different type of flash models. Some module of flash don't have a mechanism for passing empty blocks when erasing, so it takes longer time.
  
---------------------

Which GPIOs can be used to wake up ESP32-C3 from Deep-Sleep mode?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Only GPIO0 ~ GPIO5 in VDD3P3_RTC domain can be used to wake up ESP32-C3 from Deep-sleep mode. Please read Chapter 5.9.1 Power Supplies of GPIO Pins in `ESP32-C3 Technical Reference Manual <https://www.espressif.com/sites/default/files/documentation/esp32-c3_technical_reference_manual_en.pdf>`_.

------------------

When using the ESP-WROOM-02D module with a battery for power supply, are there any risks in frequently formatted reading and writing flash as the battery is low (the module barely starts up)?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - In low power conditions, if the flash is frequently operated, it may accept error commands and then erase the flash at the wrong address. It is recommended to not to operate the flash when the power is off, and please ensure a stable power supply.

---------------------

How to check the maximum stack size used by a thread for ESP32?
------------------------------------------------------------------------------------------------------------------

  - You can call the `UBaseType_t uxTaskGetStackHighWaterMark(TaskHandle_t xTask) <https://www.freertos.org/uxTaskGetStackHighWaterMark.html>`_ function. This function will return the minimum remaining stack space after the task is started.

----------------

What is the meaning of the " SW_CPU_RESET" log when using ESP32? 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - "SW_CPU_RESET" is the software reset log. For example, calling the "esp_restart()" API will print this log.

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

  - Generally it is caused by the error content in the downloaded firmware. You can dump out such content via `read_flash <https://github.com/espressif/esptool#read-flash-contents-read_flash>`_ in `esptool <https://github.com/espressif/esptool>`_ from your module. Then use the Beyond Compare tool to compare the two bin files in hexadecimal to see which part of the bin file is downloaded incorrectly.

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
  