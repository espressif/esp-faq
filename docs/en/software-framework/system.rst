System
=======

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

How do I disable the watchdog if my application doesn't need it?
----------------------------------------------------------------------

  There are mainly two types of watchdogs in ESP-IDF: task watchdog and interrupt watchdog. You can disable both types of watchdogs in menuconfig. For more details, please refer to `Watchdogs <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html>`_.

--------------

What are the differences between RTOS SDK and Non-OS SDK?
-----------------------------------------------------------

  The main differences are as follows:

  **Non-OS SDK**

  - Non-OS SDK mainly uses timers and callback functions to implement nesting of various functional events, triggering specific functions under certain conditions. Non-OS SDK uses the espconn interface for network operations, and users need to develop software according to the usage rules of the espconn interface.

  **RTOS SDK**

  - RTOS SDK is based on FreeRTOS, a multi-tasking OS. You can use the standard FreeRTOS interfaces to implement resource management, loop operations, execution delay, inter-task messaging and synchronization, and other task-oriented process design approaches. For specific interface usage methods, refer to the usage instructions on the official FreeRTOS website or the book USING THE FREERTOS REAL TIME KERNEL - A Practical Guide.
  - The network operation interface of RTOS SDK is the standard lwIP API. RTOS SDK provides a package which enables BSD Socket API interface. You can directly use the socket API to develop software applications, and port other applications from other platforms using socket API, effectively reducing the learning and development cost arising from platform switch.
  - RTOS SDK introduces the cJSON library whose functions make it easier to parse JSON packets.
  - RTOS is compatible with Non-OS SDK in Wi-Fi interfaces, SmartConfig interfaces, Sniffer related interfaces, system interfaces, timer interfaces, FOTA interfaces and peripheral driver interfaces, but does not support the AT implementation.

--------------

Why does the log output ets_main.c when ESP8266 starts?
---------------------------------------------------------

  If ESP8266 prints ``ets_main.c`` when it starts, it indicates there are no programs that can be operated. Please check the binary file and burn address if you encounter this issue.

--------------

Why do I get compile errors when using IRAM_ATTR in Non-OS SDK?
----------------------------------------------------------------

  If you need to execute a function in IRAM, you don't need to add the ``ICACHE_FLASH_ATTR`` macro, then this function is executed in IRAM.

--------------

Where is the main function of ESP8266?
---------------------------------------

  ESP8266 SDK does not provide the main function. The main function is stored in the first-stage bootloader in ROM, which is used to load the second-stage bootloader. The entry function of the second-stage bootloader is ets_main. After startup, the user_init in the user application will be loaded to lead the user application.

--------------

Which part of ESP8266 partition-tables should be paid special attention to?
-------------------------------------------------------------------------------------

  Compared to those of ESP32, partition-tables of ESP8266 have some special requirements on OTA partitions due to cache characteristics of ESP8266. For details, please refer to `Offset & Size of ESP8266 Partition Tables <https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/api-guides/partition-tables.html#offset-size>`__。

--------------

Is it possible to compile the binaries in application layer and bottom layer separately?
-------------------------------------------------------------------------------------------------

  No, they cannot be compiled separately.

--------------

What should I pay attention to when using flash of ESP32 module at 80 MHz?
----------------------------------------------------------------------------

  Espressif modules have undergone stability tests before they are sold, and they support the frequency of 80 MHz. According to stability test data, operating flash at the frequency of 80 MHz will not affect the service life and stability.

--------------

How can I download programs into a single-core module using ESP-IDF?
--------------------------------------------------------------------

  When compiling the program, use the ``make menuconfig`` command to enter the configuration interface, and make the following configuration to download the program on a single-core module. Please note that in the configuration interface, press Y to enable, and N to disable.

  ``Component config`` > ``FreeRTOS`` > ``Run FreeRTOS only on first core``

--------------

How to enable the dual-core mode of ESP32 with ESP-IDF?
--------------------------------------------------------

  ESP-IDF is generally configured in dual-core mode by default. You can switch between the single and dual cores in menuconfig: ``menuconfig`` > ``Component config`` > ``FreeRTOS`` > ``Run FreeRTOS only on first core``. ESP32 is in the single-core mode if this option is enabled, and is in the dual-core mode if it is disabled (default).

--------------

Can the ESP32-D0WD chip store user programs?
-------------------------------------------------------

  No, user programs must be stored in the external flash. The on-chip ROM cannot store user programs. The program stored in the ROM is the chip's first-stage bootloader. To protect the factory program from being damaged, this area is read-only.

--------------

Will the data in PSRAM be lost when ESP32 enters low power mode?
-----------------------------------------------------------------

  - In Modem-sleep/Light-sleep mode, the data in PSRAM will not be lost.
  - In Deep-sleep mode, the CPU and most peripherals will lose power, and the data in PSRAM will be lost.

--------------

Is the ESP32 CPU system time generated by the system tick clock? What is the precision?
----------------------------------------------------------------------------------------------

  The CPU system time is generated by the internal 64-bit hardware timer CONFIG_ESP_TIMER_IMPL of esp_timer, which has a microsecond-level time resolution. For details, please see `High Precision Clock Description <https://docs.espressif.com/projects/esp-idf/en/v4.4.2/esp32/api-reference/system/esp_timer.html#obtaining-current-time>`_.

--------------

How can I modify the clock frequency of ESP32's flash and PSRAM?
--------------------------------------------------------------------

  Modify it in menuconfig:

  - flash clock frequency: ``menuconfig`` > ``Serial flasher config`` > ``Flash SPI speed``.
  - PSRAM clock frequency: ``Component config`` > ``ESP32-specific`` > ``SPI RAM config`` > ``Set RAM clock speed``.

--------------

When using ESP32-SOLO-1 modules, what settings should I make to run ESP-IDF on a single-core module?
--------------------------------------------------------------------------------------------------------

  First, you need to use the ``menuconfig`` command to enter the configuration interface, and then enable the option ``Component config`` > ``FreeRTOS`` > ``Run FreeRTOS only on first core`` to run ESP-IDF on a single-core module.

--------------

Can time_t be configured to be 64 bits in ESP-IDF? (It is currently 32 bits)
----------------------------------------------------------------------------

  ESP-IDF uses a 64-bit signed integer to represent time_t starting from release v5.0. For details, please see `Unix Time 2038 Overflow <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/system_time.html#unix-time-2038-overflow>`_.

--------------

How does the firmware distinguish whether the main chip is ESP8285 or ESP8266?
-------------------------------------------------------------------------------

  External tools such as `esptool <https://github.com/espressif/esptool>`_ are typically used to read the chip type. You can read the corresponding register bits of the chip in the firmware according to the Python code example, and then calculate to determine the result.

  .. code-block:: python

    def get_efuses(self):
    # Return the 128 bits of ESP8266 efuse as a single Python integer
    return (self.read_reg(0x3ff0005c) << 96 | self.read_reg(0x3ff00058) << 64 | self.read_reg(0x3ff00054) << 32 | self.read_reg(0x3ff00050))

    def get_chip_description(self):
      efuses = self.get_efuses()
      is_8285 = (efuses & ((1 << 4) | 1 << 80)) != 0  # One or the other efuse bit is set for ESP8285
      return "ESP8285" if is_8285 else "ESP8266EX"

--------------

Can ESP32 load library files as dynamic libraries?
---------------------------------------------------

  ESP32 does not support loading library files as dynamic libraries. It only supports static libraries.

------------------

How can I reduce the IRAM occupied by the ESP32 system?
---------------------------------------------------------

  - Please disable ``menuconfig`` > ``Component config`` > ``LWIP`` > ``Enable LWIP IRAM optimization`` by typing ``N``.
  - Please change the configurations in ``menuconfig`` > ``Compiler option`` > ``Optimization Level`` > ``Optimize for size (-Os)``.
  - Please disable ``WiFi IRAM speed optimization (N)`` and ``WiFi RX IRAM speed optimization (N)`` in ``menuconfig`` > ``Component config`` > ``wifi``.
  - For more details, please refer to `Minimizing RAM Usage <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/performance/ram-usage.html>`__。

----------------------

What is the low voltage reset threshold of the ESP32 chip?
-----------------------------------------------------------

  The brownout voltage threshold ranges from 2.43 V to 2.80 V, which can be set in ``menuconfig`` > ``Component config`` > ``ESP32-specific`` > ``Brownout voltage level``.

----------------

Why is ESP32 automatically woken up in the light sleep example?
--------------------------------------------------------------------------

  In the light sleep example, two wake-up methods are used by default as follows:

  .. code-block:: c

    esp_sleep_enable_timer_wakeup(2000000);     // Automatically wake up after 2 seconds
    esp_sleep_enable_gpio_wakeup();             // GPIO wake-up

  By default, the GPIO wake-up method wakes ESP32 up when GPIO0 is in the low level. When GPIO0 is low, ESP32 is in the wake-up state. When GPIO0 is high, ESP32 automatically enters the Light-sleep mode. If you need to maintain the Light-sleep mode for a long time, you can command out automatic wake-up after 2 seconds and only enable GPIO wake-up.

---------------------

When testing ESP32 deep_sleep example, why does the program crash into a dead loop when const int wakeup_time_sec = 3600?
------------------------------------------------------------------------------------------------------------------------------

  The program crashes because the int type parameter `wakeup_time_sec` overflows during the operation of wakeup_time_sec * 1000000.

  .. code-block:: c

    const uint64_t wakeup_time_sec = 3600;
    printf("Enabling timer wakeup, %lldn",wakeuo_time_sec);

------------------

How many system reset methods does ESP32 have?
-----------------------------------------------

  ESP32 has several system reset methods, including the following:

  - Software Reset: In the application program, you can perform a software reset by calling the esp_restart() function.
  - External Reset: ESP32 can be reset by external hardware circuits, such as pressing the RESET button, unstable power supply voltage, etc.
  - Hardware Watchdog Reset: When ESP32 encounters a deadlock or other abnormal conditions during operation, the hardware watchdog module will automatically trigger a reset.
  - Brownout Reset: When the system voltage is unstable or the power supply voltage is relatively low, ESP32's built-in power management module will automatically trigger a reset.
  - Exception Reset: When ESP32 encounters a CPU exception during operation, such as accessing illegal memory, running illegal instructions, etc., it will trigger an exception reset.
  - JTAG Reset: When debugging ESP32 with a JTAG debugger, you can reset it through the JTAG reset signal.
  - For more details, see Section 4.1.2 Reset Sources in `ESP32 Technical Reference Manual <https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf>`__.

--------------

Why does ESP8266-NONOS-V3.0 SDK output the following error?
--------------------------------------------------------------------------------

  .. code-block:: text

    E:M 536
    E:M 1528

  - The log starting with E:M is caused by insufficient remaining memory.

--------------

Can ESP32 use the entire 8 MB of PSRAM memory?
--------------------------------------------------

  - Yes.
  - Since the maximum cache mapping space is 4 MB, only 4 MB of PSRAM can be used by mapping, and the remaining space can be used through API.
  - For details, please refer to the example `himem <https://github.com/espressif/esp-idf/tree/master/examples/system/himem>`_.

--------------

After ESP8266 AT connects to AP, the system enters into Modem-sleep by default, but the current does not drop significantly. What are the reasons?
--------------------------------------------------------------------------------------------------------------------------------------------------------------

  - After the AT firmware connects to the AP, ESP8266 will enter into Modem-sleep mode automatically, and the power consumption will fluctuate between 15 mA ~ 70 mA.
  - If the power consumption does not fluctuate between 15 mA ~ 70 mA, and the current does not show a waveform in the oscilloscope, please refer to the following suggestions:
    - Erase the device flash and re-flash the AT firmware.
    - Capture network packets to analyze whether there are devices that frequently send broadcast packets in the current network environment. If yes, you can test with a router (AP) in another network environment.

--------------

Can ESP32 permanently change the MAC address?
----------------------------------------------

  - The MAC address that comes with the chip cannot be modified. The eFuse supports users to write their own MAC address.
  - The customized MAC address can be obtained by calling API in the firmware, and it can be set to replace the default address in the system.
  - For detailed configuration, please refer to `mac-address <https://docs.espressif.com/projects/esp-idf/en/release-v5.0/esp32/api-reference/system/misc_system_api.html#mac-address>`_.
  - In addition, Espressif provides a service to burn the MAC address provided by the user before the chip leaves the factory. If you have such requirements, please email sales@espressif.com.

--------------

How can ESP8266 verify all.bin as an illegal file during OTA upgrade?
---------------------------------------------------------------------

  **Background:**

  - all.bin is generated by merging bootloader.bin, partition.bin, and app.bin.
  - ota.bin is the object bin file used for OTA upgrade.

  When using `simple_ota_example <https://github.com/espressif/ESP8266_RTOS_SDK/tree/master/examples/system/ota/simple_ota_example>`_ for OTA upgrade, if you mistakenly download all.bin from the server and write it into the OTA partition, the device will repeatedly restart.

  **Cause analysis:**

  The code does not verify all.bin, resulting in writing illegal bin files into the OTA partition.

  **Solution:**

  all.bin can be judged as an illegal bin file by turning on sha256 verification. The configuration is as follows: ``Component config`` > ``App update`` > ``[*] Check APP binary data hash after downloading``.

--------------

Where are the release notes after the ESP-IDF version is updated?
-------------------------------------------------------------------

  For the release notes, please see `GitHub release note <https://github.com/espressif/esp-idf/releases>`_.

--------------

Does ESP8266 have a detailed register manual?
----------------------------------------------

  Please refer to `ESP8266 TRM <https://www.espressif.com/sites/default/files/documentation/esp8266-technical_reference_en.pdf>`_ > Appendix.

---------------

ESP32 cannot start normally after enabling Secure Boot and outputs the following error. What is the reason for it?
-------------------------------------------------------------------------------------------------------------------------

  .. code-block:: text

    csum err:0x9a!=0x5f
    ets_main.c 371
    ets Jun  8 2016 00:22:57
    rst:0x10 (RTCWDT_RTC_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
    configsip: 0, SPIWP:0xee
    clk_drv:0x00,q_drv:0x00,d_drv:0x00,cs0_drv:0x00,hd_drv:0x00,wp_drv:0x00
    mode:DIO, clock div:2
    load:0x3fff0030,len:4
    load:0x3fff0034,len:9372
    load:0x40078000,len:19636

  This may be because the Bootloader become larger after enabling Secure Boot, and the bin file is overwritten when the firmware is burned. You can check the size of the Bootloader after Secure Boot. For example, you can try to increase the offset of the partition table to 0xF000.

--------------

How does ESP8266 save data during a software reboot?
---------------------------------------------------------

  - If writing or modifying operations are not frequent, flash can be used to store data. This area is relatively larger than memory and easy to be adjusted.
  - If the data is small, RTC Memory can be used to store related data. Please see the interface in esp_system.h in the branch of Rel 2.1 (refer to usage instructions) system_rtc_mem_read.
  - If neither of the above can meet the requirements, you can also choose the external RTC memory, which can interact with I2C and SPI.
  - It is recommended to write the data to flash when the writing frequency is not high, because the data will not lose when the power is off.

--------------

What timers are available on ESP8266?
--------------------------------------

  - ESP8266 has a hardware timer that can generate interrupts. Calling API in NONOS SDK and RTOS SDK are slightly different.
  - Software timer:

    - The API os_timer in NONOS is a DSR process, which cannot generate interrupts, but can generate tasks. Tasks will be queued according to the ordinary level.
    - In RTOS, you can use the software timer in FreeRTOS, which is more flexible.

--------------

What is the purpose of the watchdog on ESP8266?
------------------------------------------------

  - In order to provide system stability and cope with the operating environment with multiple conflicts, ESP8266 integrates a 2-level watchdog mechanism, including software watchdog and hardware watchdog.
  - Both watchdogs are enabled by default. HW WDT is always running. If the HW WDT is not reset, the MCU will be reset after about 6 seconds.
  - SW WDT will reset the MCU in about 1.5 seconds. You can enable/disable SW WDT, but you cannot enable/disable HW WDT. Because you must reset the SW WDT before you can reset the HW WDT at the same time.
  - The watchdog can be configured by modifying ``make menuconfig`` > ``Component config`` > ``Common ESP-related`` > ``Invoke panic handler on Task Watchdog timeout``.

--------------

What should be paid attention to when using ``user_init`` in ESP8266?
-----------------------------------------------------------------------------------

  - ``wifi_set_ip_info`` and ``wifi_set_macaddr`` only take effect when called in ``user_init``. They do not take effect when called elsewhere.
  - It is recommended to call ``system_timer_reinit`` in ``user_init``. Otherwise, you need to re-arm all timers after calling it.
  - If ``wifi_station_set_config`` is called in ``user_init``, the underlying layer will automatically connect to the corresponding router, and there is no need to call ``wifi_station_connect`` to connect. Otherwise, you need to call ``wifi_station_connect`` to connect.
  - ``wifi_station_set_auto_connect`` sets whether to automatically connect to the recorded router when powered on. For example, if the automatic connection function is turned off, and it is called in ``user_init``, then the router will not be automatically connected when powered on this time. If it is called elsewhere, the router will not be automatically connected when powered on next time.

-----------------

Why does the system keep restarting after ESP32 enables both ``Enable debug tracing of PM using GPIOs`` and ``Allow .bss segment placed in external memory``?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The ``Enable debug tracing of PM using GPIOs`` configuration option needs to be enabled during GDB debugging and cannot be used simultaneously with the ``Allow .bss segment placed in external memory`` configuration option.
  - Because ``Enable debug tracing of PM using GPIOs`` uses GPIO16 and GPIO17 by default, which conflicts with the PSRAM interface (also default to GPIO16 and GPIO17).

-----------------------

Why does the program trigger RTCWDT_RTC_RESET when ESP32 bootloader in ESP-IDF v3.3 version runs app bin in v3.1 version?
--------------------------------------------------------------------------------------------------------------------------------

  - The bootloader v3.3 enables the WDT watchdog and turns off the WDT watchdog when the application (app) is running.
  - However, bootloader v3.1 does not enable the WDT watchdog, so the application (app) does not have the WDT watchdog mechanism, which leads to bootloader v3.3 triggering the WDT watchdog reset when guiding the application (app) v3.1.
  - You can disable ``BOOTLOADER_WDT_ENABLE`` in ``menuconfig`` to turn off the WDT watchdog in bootloader v3.3.

-------------------

Does the ESP32 chip come with a unique chip_id from the factory?
-----------------------------------------------------------------

  The ESP32 chip does not have a unique chip_id, but it has a globally unique MAC address by default, which can be used to replace the chip_id.

--------------

How to check ESP8266 reset cause?
------------------------------------

  Please refer to `ESP8266 Exception Restart Causes <https://www.espressif.com/sites/default/files/documentation/esp8266_reset_causes_and_common_fatal_exception_causes_en.pdf>`_.

-----------------

How can I optimize the size of binary files compiled by ESP32?
---------------------------------------------------------------

  The bin file compiled for ESP32 usually includes application code, partition table, ESP-IDF firmware, and other data. To optimize the size of it, the following methods can be adopted:

  - Configure compilation options: GCC compilation can be optimized by configuring ``idf.py menuconfig`` > ``Compiler options`` > ``Optimization level (Optimize for size(-Os))``.
  - Optimize code: The application code can be optimized, such as adopting more efficient algorithms and data structures, simplifying code logic and process, improving code reuse rate, adjusting log level, reducing unnecessary log printing, and reducing code file size.
  - It should be noted that when optimizing the size of the bin file, the optimization effect and program function need to be balanced to avoid excessive optimization causing program exceptions or incomplete functions. It is recommended to refer to the official documents and examples when optimizing the size of the bin file, and follow the relevant regulations and standards.

  For more details, please refer to `Minimizing Binary Size <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/performance/size.html>`__.


-----------------

Does ESP32 have an API for rebooting the system?
-------------------------------------------------

  - You can use the API ``esp_restart()`` to reboot the system. For related instructions, please refer to `documentation <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/misc_system_api.html#_CPPv411esp_restartv>`__.

--------------

What is the reason for the exception log ``invalid header: 0xffffffff`` of ESP32?
-----------------------------------------------------------------------------------------------

  The ESP32 chip usually prints this exception log in the following situations:

  - The power-on and power-off timing of the chip is incorrect, and some areas of the chip are not fully reset.
  - There is an exception in the firmware in flash, such as incomplete firmware burning.
  - The flash device is damaged and cannot read the correct data.
  - The chip's own cache is turned off or damaged and cannot read firmware data.

--------------

What is the timed mechanism to wake up ESP8266 from deep sleep?
-----------------------------------------------------------------

  In Deep-sleep mode, connect GPIO16 (XPD_DCDC) to EXT_RSTB. After the sleep time is reached, GPIO16 outputs a low level to the EXT_RSTB pin, and the chip is reset and awakened.

----------------------------------------

Why is the ESP32 RAM obtained using ``heap_caps_get_free_size`` about 300 KB, instead of the 520 KB provided in the manual?
------------------------------------------------------------------------------------------------------------------------------------------------------

  - This is because the memory is pre-allocated to various function modules at system startup, and the remaining memory after system startup is about 300 KB.
  - If the remaining memory is insufficient, you can choose a module with PSRAM, and allocate the memory in the PSRAM.

--------------

How to perform OTA upgrade via LAN app for ESP32 & ESP8266?
------------------------------------------------------------

  - Devices within the LAN can configure to enable the HTTP service, and send the provided firmware download link to the device through other methods (UDP, CoAP, MQTT, etc.).
  - The device can complete the OTA update through the traditional URL OTA method, and the application example is provided in the SDK.

-----------------

How can I modify the GPIO used by the serial port for log output in ESP32?
---------------------------------------------------------------------------------

  - Configure ``menuconfig`` > ``Component Config`` > ``ESP System Settings`` > ``Channel for console output`` > ``Custom UART``, and select custom UART pin.
  - Go back to the previous level, you will see the options of ``UART TX on GPIO#`` and ``UART RX on GPIO#``. By modifying these two options, you can change the GPIO used by the serial port for log output.

-----------------

ESP8266 uses MQTT ssl_mutual_auth to communicate. Why does the following error occur during OTA?
---------------------------------------------------------------------------------------------------------------------

  .. code::text

    W(50083) _http_event_handler：HTTP_EVENT_DISCONNECTED
    E(50089)esp_https_ota：Failed to open HTTP connection：28674
    E(50095)gateway_https_ota：Firmware upgrade failed
    E(50179)esp-tls-mbedtls: mbedtls_ssl_setup returned -0x7f00
    E(50181)esp-tls-mbedtls: mbedtls_ssl_handle failed
    E(50194)esp-tls：Failed to open a new connection

  - The error 0x7f00 is due to insufficient memory. It is recommended to use HTTP for OTA.

-----------------

There are NVS options in ESP32's ``menuconfig`` > ``Component config``. Why are the configuration items are empty?
------------------------------------------------------------------------------------------------------------------------------

  - The NVS option in ``menuconfig`` > ``Component config`` is to configure the NVS encryption function, and the prerequisite for this function is to enable flash encryption.
  - After configuring the option ``menuconfig`` > ``security features`` > ``enable flash encryption on boot option``, you can see the NVS configuration options.

--------------

Does ESP32 undergo a random watchdog reset after power-up or waking up from Deep-sleep?
----------------------------------------------------------------------------------------

  - The watchdog reset on power-up cannot be bypassed by software, but ESP32 starts normally after reset.
  - The watchdog reset after waking up from Deep-sleep is automatically bypassed in ESP-IDF v1.0 and higher versions.
  - After waking up from Deep-sleep, the CPU can immediately execute a program in RTC fast memory. The program in RTC fast memory bypasses the watchdog reset after waking up from Deep-sleep by clearing the illegal access flag of cache MMU. Specifically, it

    - Sets the ``PRO_CACHE_MMU_IA_CLR`` bit of the ``DPORT_PRO_CACHE_CTRL1_REG`` register to 1.
    - Clears this bit.

--------------

When the ESP32 CPU uses cache to access external SRAM, if these operations need to be processed by the CPU at the same time, will read and write errors occur?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - This problem cannot be automatically bypassed by software.
  - For ESP32 version 0, when CPU uses cache to access external SRAM, it can only perform unidirectional operations, that is, it can only perform write operations or read operations to SRAM. These two operations cannot be realized alternatively.
  - Use the MEMW instruction: after the read operation, add the ``__asm__("MEMW")`` instruction, and then initiate the write operation before the CPU pipeline is cleared.

--------------

ESP32 CPU may freeze when it switches directly from 240 MHz to 80/160 MHz. How can I solve it?
-----------------------------------------------------------------------------------------------------------

  - It is recommended to use the following two modes:

    (1) 2 MHz <-> 40 MHz <-> 80 MHz <-> 160 MHz
    (2) 2 MHz <->40 MHz <->240 MHz
  - This issue has been fixed in chip version 1.

--------------

For ESP32 pads with both GPIO and RTC_GPIO functions, the pull-up and pull-down resistors can only be controlled by the RTC_GPIO pull-up and pull-down registers. How can I solve it?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The GPIO driver in ESP-IDF v2.1 and higher versions automatically bypasses this issue.
  - Both GPIO and RTC_GPIO use the RTC_GPIO register.

--------------

As the flash startup speed is slower than that of the chip reading flash, ESP32 may randomly reset the watchdog once after power-on or waking up from Deep-sleep. How can I solve it?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Use a faster flash instead, requiring the time from flash power-on to being readable to be less than 800 μs. This method can bypass the watchdog reset when the chip is powered on and wakes up from Deep-sleep.
  - The issue of watchdog reset after waking up from Deep-sleep is automatically bypassed in ESP-IDF v2.0 and higher versions (the delay time can be configured as needed). Specifically, CPU first reads the instructions in the RTC fast memory after waking up from Deep-sleep, and then reads the flash after waiting for a while.

--------------

When the ESP32 CPU accesses the external SRAM, there is a small probability of causing reading and writing errors. How can I solve it?
---------------------------------------------------------------------------------------------------------------------------------------------------

  .. code::text

    store.x at0, as0, n
    load.y at1, as1, m
    Where store.x represents x-bit write operation, load.y represents y-bit read operation, and the external SRAM addresses accessed by as0+n and as1+m are same.

  - When x>=y, insert 4 nop instructions between store.x and load.y.
  - When x<y, insert a memw instruction between store.x and load.y.

--------------

For a dual-core ESP32 chip, when one CPU's bus is reading address space A, and the other CPU's bus is reading address space B, the CPU reading address space B may encounter an error. How can I solve it?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - When one CPU is reading address space A, avoid another CPU initiating a read operation on address space B through locking and interrupting.
  - Before one CPU reads address space A, add an operation of this CPU reading address space B (non-FIFO address space, such as 0x3FF40078), and ensure that the operations of reading address space B and reading address space A are atomic.

--------------

The ESP32 CPU resets the interrupt signal of the CAN controller by reading the ``INTERRUPT_REG`` register. If the CAN controller happens to generate a transmission interrupt signal within the same APB clock cycle, the transmission interrupt signal is lost. How can I solve it?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  From the transmission request is initiated till the data transmission completes, each time after reading ``INTERRUPT_REG``, you should check the ``STATUS_TRANSMIT_BUFFER`` bit. If the bit is set and ``CAN_TRANSMIT_INT_ST`` is not set, the transmission interrupt signal will be lost. In ESP32, the interrupt signal of the CAN controller can be reset by reading the ``INTERRUPT_REG`` register. However, if the CAN controller generates a transmission interrupt signal within the same APB clock cycle, the interrupt signal may be lost because ESP32 may have cleared it when reading the register within this clock cycle. To solve this problem, the following methods can be used:

  - Add delay: Before reading the ``INTERRUPT_REG`` register, a certain delay can be added to ensure that the interrupt signal of the CAN controller has been cleared. The appropriate delay can be determined through test and adjustment.
  - Use interrupt handler: An interrupt handler can be used to handle the interrupt signal of the CAN controller and avoid reading the ``INTERRUPT_REG`` register within the same APB clock cycle. The interrupt handler can respond to the interrupt signal of the CAN controller in time to ensure that the signal will not be lost.
  - Use other registers: Other registers can be used to reset the interrupt signal of the CAN controller to avoid reading the ``INTERRUPT_REG`` register within the same APB clock cycle. For example, the ``CANCTRL`` register or ``ERRCNT`` register can be used.

  It should be noted that when using the above methods, it is necessary to choose and implement the appropriate one according to the specific application scenario and requirements. At the same time, sufficient testing and verification of software and hardware are also required to ensure the reliability and stability of the system. When resetting the interrupt signal of the CAN controller in ESP32, it is necessary to avoid losing the interrupt signal to ensure the normal operation of the system.

--------------

When the program meets the following conditions simultaneously, ESP32 v3.0 will be live-locked, causing the CPU to remain in a memory access state and unable to continue executing instructions. How can this be resolved?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Please refer to `ESP32 Series SoC Errata <https://www.espressif.com/sites/default/files/documentation/esp32_errata_en.pdf>`__ > subsection 3.15.

--------------

The ESP32 CPU has restrictions when accessing the address spaces ``0x3FF0_0000 ~ 0x3FF1_EFFF`` and ``0x3FF4_0000 ~ 0x3FF7_FFFF``. How can this be resolved?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Please refer to `ESP32 Series SoC Errata <https://www.espressif.com/sites/default/files/documentation/esp32_errata_en.pdf>`__ > subsection 3.16.

------------------

How can I turn off log output in ESP32？
---------------------------------------------

  - You can turn off the bootloader log by setting ``menuconfig`` > ``bootloader config`` > ``bootloader log verbosity`` to ``No output``.
  - You can turn off the program log by setting ``menuconfig`` > ``Component config`` > ``log output`` > ``Default log verbosity`` to ``No output``.
  - For ESP-IDF release/v4.3 and earlier versions, you can turn off UART0 output log by ``menuconfig`` > ``Component Config`` > ``Common ESP-related`` > ``Channel for console output`` > ``None``.
  - For ESP-IDF release/v4.4 and later versions, you can turn off UART0 output log by ``Component config`` > ``ESP System Settings`` > ``Channel for console output`` > ``None``.

------------------

Can the data stored in RTC Memory run when ESP8266 is in Deep-sleep mode?
-------------------------------------------------------------------------------------

  When ESP8266 is in Deep-sleep mode, only the RTC timer continues to work. The data saved in the RTC Memory will not run, but can still be saved here. However, the data saved in RTC memory will lose after ESP8266 is powered off.

------------------

What is the maximum length of the NVS Key for ESP32?
------------------------------------------------------

  - The maximum length of the NVS key for ESP32 is 15 characters, which cannot be changed. Please see the description of `key-value pair <https://docs.espressif.com/projects/esp-idf/en/release-v4.3/esp32/api-reference/storage/nvs_flash.html#id4>`_.
  - But you can use the value of `nvs_set_str() <https://docs.espressif.com/projects/esp-idf/en/release-v4.3/esp32/api-reference/storage/nvs_flash.html#_CPPv411nvs_set_str12nvs_handle_tPKcPKc>`_ to store data.

------------------

Does cJSON in ESP-IDF release/v4.2 support uint64_t data parsing?
---------------------------------------------------------------------------

  No. The cJSON library has restrictions on parsing long integers, and the longest type it can parse is the Double type.

---------------

Given that the GDB debugging function is working before the flash encryption is disabled, then why does the device keep restarting during the GDB debugging after the flash encryption is enabled?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The JTAG debugging function will be disabled by default when flash encryption or secure boot is enabled. For more information, please refer to `JTAG with Flash Encryption or Secure Boot <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/jtag-debugging/tips-and-quirks.html#jtag-with-flash-encryption-or-secure-boot>`_.

---------------

When ESP32 uses mobile hotspot for OTA firmware download, if the data switch is turned off for a few seconds and then turned on again, the program will always be stuck in OTA (the same applies when unplugging and plugging the WAN cable when using a router). Why?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - This is a normal situation based on the protocol. When using the ``esp_https_ota`` component to run OTA, you can set the network timeout value ``http_config->timeout_ms`` to 10 ~ 30 seconds (not recommended to be too small), and enable ``http_config->keep_alive_enable`` to see if there are any errors at the link layer.
  - If you are using a self-implemented OTA module, please set a timeout value via the ``select`` configuration or enable the TCP keep-alive mechanism to detect the link layer.

------------------

Which GPIOs can be used to wake up ESP32-C3 in Deep-sleep mode?
----------------------------------------------------------------

  Only GPIO0 ~ GPIO5 in VDD3P3_RTC domain can be used to wake up ESP32-C3 from Deep-sleep mode. Please read Chapter 5.9.1 Power Supplies of GPIO Pins in `ESP32-C3 Technical Reference Manual <https://www.espressif.com/sites/default/files/documentation/esp32-c3_technical_reference_manual_en.pdf>`_.

---------------------

When using the ESP-WROOM-02D module with a battery for power supply, are there any risks in frequently formatted reading and writing flash as the battery is low (the module barely starts up)?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Frequent formatting and read/write operations on flash in low power situations may have some risks. It may not work properly or be susceptible to cause errors under low power conditions. In addition, frequent formatting and read/write operations on flash in this situation may lead to the following risks:

  - Data loss or corruption: flash may not be able to write data properly under low power conditions. Frequent formatting and read/write operations may result in data loss or corruption.
  - Module crash or damage: Frequent formatting and read/write operations on flash in low power conditions will consume the module's power, which may cause the module to crash or damage.

  Therefore, it is recommended to minimize access and operations on flash in low power conditions and avoid frequent formatting and read/write operations. If formatting and read/write operations are necessary, ensure that the module has sufficient power, backup data before the operation to prevent data loss, use low power mode and optimize code to minimize power consumption.

---------------------

How can I check the maximum stack size used by a thread for ESP32?
--------------------------------------------------------------------------

  You can call the `UBaseType_t uxTaskGetStackHighWaterMark(TaskHandle_t xTask) <https://www.freertos.org/uxTaskGetStackHighWaterMark.html>`_ function to check it. This function will return the minimum remaining stack space after the task is started.

-------------------

Why does ESP32 print the "SW_CPU_RESET" log?
---------------------------------------------------------------------

  On ESP32, printing the "SW_CPU_RESET" log is usually caused by the program terminating abnormally.
  ESP32 has two built-in processor cores, namely the main core and the auxiliary core. In some cases, if the program is executed on the main core and some abnormal situations occur, such as accessing illegal addresses or unhandled interrupts, it may cause the main core to enter an abnormal state and restart. When this happens, ESP32 will print the "SW_CPU_RESET" log on the serial terminal (UART).
  In addition, when developing applications using ESP-IDF, you may also call the ``esp_restart()`` function in the application program to restart ESP32. In this case, ESP32 will also print the "SW_CPU_RESET" log on the serial terminal.
  It should be noted that the appearance of the "SW_CPU_RESET" log does not necessarily mean that there is a problem with the program or ESP32 hardware. It may just be a normal phenomenon caused by some abnormal situations. However, if the program frequently encounters exceptions and restarts, debugging and troubleshooting are needed. The cause of the problem can be determined by checking the program log and the status of the hardware device.

----------------

For ESP32 products, when testing NVS separately, I found it occupies a lot of memory. What is the reason?
--------------------------------------------------------------------------------------------------------------

  Please check the partition table settings. It is recommended to set a smaller NVS data partition in the partition table to test. The larger the NVS data partition setting, the more memory it will occupy.

-----------------------------------------------------------------------------------------------------

How do I change the system time of a module?
---------------------------------------------

  :CHIP\: ESP32 | ESP32 | ESP32-C3:

  - You can use the ``time()`` interface in C libraray to set the system time.

----------------------------------------------------------------------------------------

During the OTA upgrade process, an ``ESP_ERR_OTA_VALIDATE_FAILED`` error occurred after calling ``esp_ota_end``. How can I troubleshoot such issue?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32:

  - Generally it is caused by the error content in the downloaded firmware. You can dump out such content via `read_flash <https://docs.espressif.com/projects/esptool/en/latest/esp32/esptool/basic-commands.html#read-flash-contents-read-flash>`_ in `esptool <https://github.com/espressif/esptool>`_ from your module. Then use the Beyond Compare tool to compare the two bin files in hexadecimal to see which part of the bin file is downloaded incorrectly.

-------------

How does ESP8266-RTOS-SDK store data to RTC memory?
-------------------------------------------------------

  - The definition method of storing data in RTC memory is as follows:

  .. code:: text

      #define RTC_DATA_ATTR _SECTION_ATTR_IMPL(".rtc.data", __COUNTER__)

  - Please refer to the description in `esp_attr.h <https://github.com/espressif/ESP8266_RTOS_SDK/blob/release/v3.4/components/esp8266/include/esp_attr.h>`_.

---------------

After waking up from Deep-sleep mode, where does ESP8266 boot?
---------------------------------------------------------------------

  After ESP8266 wakes up from Deep-sleep mode, the device will boot up from ``user_init``. Please refer to the description in `esp_deep_sleep() <https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/api-reference/system/sleep_modes.html?highlight=deep#_CPPv414esp_deep_sleep8uint64_t>`__.

---------------

When will the RTC clock be reset?
----------------------------------

  Any reset (except the power-up reset) or sleep mode settings will not reset the RTC clock.

-------------------

Can ESP32 be woken up by pulling EN low after entering Deep-sleep mode with the ``AT+GSLP`` command?
-------------------------------------------------------------------------------------------------------------

  - Yes, but it is not recommended.
  - Waking up from Deep-sleep mode can be realized by RTC_GPIO. Please refer to `ESP32 Technical Reference Manual <https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf>`_.

----------------

When multiple threads want to use the watchdog of ESP32, should each thread enable the watchdog individually?
-------------------------------------------------------------------------------------------------------------------

  Yes, please see `Task watchdog instructions <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/wdts.html?highlight=wdt#task-watchdog-timer>`_.

-----------------------------

How to enter Light-sleep mode with ESP8266-RTOS-SDK release/v3.3?
------------------------------------------------------------------

  - First set the wake-up mode of Light-sleep mode, please refer to `ESP8266_RTOS_SDK/components/esp8266/include/esp_sleep.h <https://github.com/espressif/ESP8266_RTOS_SDK/blob/release/v3.3/components/esp8266/include/esp_sleep.h>`_.
  - Then use the `esp_light_sleep_start() <https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/api-reference/system/sleep_modes.html?highlight=esp_light_sleep_start%28%29#_CPPv421esp_light_sleep_startv>`_ API to enter Light-sleep mode.
  - For the program implementation logic, please refer to `esp-idf/examples/system/light_sleep/main/light_sleep_example_main.c <https://github.com/espressif/esp-idf/blob/release/v4.2/examples/system/light_sleep/main/light_sleep_example_main.c>`__.
  - For API descriptions about sleep modes in ESP8266-RTOS-SDK, please see `Sleep modes API Reference <https://docs.espressif.com/projects/esp8266-rtos-sdk/en/release-v3.3/api-reference/system/sleep_modes.html#sleep-modes>`_.

-----------------------------

How can I wake up ESP8266 from Deep-sleep mode?
------------------------------------------------

  ESP8266 can only be awakened from Deep-sleep mode via RTC Timer. The timing duration is set by user via ``esp_deep_sleep()``, and GPIO16 (XPD_DCDC) should be connected to EXT_RSTB through a 0 Ω resistor to support such function. Please refer to `related API descriptions <https://docs.espressif.com/ projects/esp8266-rtos-sdk/en/latest/api-reference/system/sleep_modes.html?highlight=deep#_CPPv414esp_deep_sleep8uint64_t>`_.

-----------------

When using the ESP32-WROVER\ :sup:`*` module, there is a problem of battery jitter or abnormal power-off and power-on, causing the system to crash and fail to wake up. What is the reason?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Application scenario: When sleeping, the current is about 12 uA. When the battery is unplugged or the product is shaken, it will cause power failure, but there is still electricity in the capacitor. The process of ESP32 discharging from 3.3 V to 0 V, and then powering on to restore 3.3 V will cause ESP32 to be unable to wake up.

  - Please check whether the chip VCC and EN meet the power-on timing requirements.
  - When using the ESP32-WROVER\ :sup:`*` module for sleep, if there is unstable power supply voltage or abnormal power off, it may cause problems with the power management unit of the chip, leading to inability to wake up normally.
  - Consider adding a reset chip to ensure normal timing.
  - For the power-on and reset timing description of ESP32, please refer to the `ESP32 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf>`_.

  \ :sup:`*` indicates that the product is in EOL status.

--------------

How can I flash a customized MAC address?
-------------------------------------------

  You can start by understanding the MAC mechanics of ESP modules, please refer to `Introduction to Mac Addresses <https://docs.espressif.com/projects/esp-idf/en/latest/api-reference/system/system.html?highlight=MAC% 20address/>`_. There are currently two options for burning customized MAC addresses:

  - Option 1: directly flash it into eFuse blk3.
  - Option 2: Store in flash. It is not recommended to store the MAC address in the default NVS partition. It is recommended to create a customized NVS partition for storing customized Mac addresses. For more information on customized MAC addresses, please refer to `base_mac_address <https://github.com/espressif/esp-idf/tree/master/examples/ system/base_mac_address/>`_.

---------------

When ESP32 uses esp_timer, network communication or Bluetooth communication is abnormal. What is the reason?
---------------------------------------------------------------------------------------------------------------------

  - esp_timer is a high-precision hardware timer component, and some background components also use it to complete some system tasks. When using esp_timer, please do not call delay and blocking APIs in the callback function of the timer, and try to ensure that the function is executed as quickly as possible, so as not to affect the performance of other system components.
  - If you do not require high timing accuracy, please use the timer component `xTimer <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/freertos_idf.html#timer-api>`__ in FreeRTOS.

--------------

With ESP32, are there any return instructions if I skip to a function using the ``jump`` instruction in ULP？
----------------------------------------------------------------------------------------------------------------

  For ULP CPU instructions list and corresponding specifications, please see `ULP Coprocessor Instruction Set <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/ulp_instruction_set.html>`_. Normally, a general register is used for return instructions to store backup PC addresses for later jumping backs. Since there are only four general registers in ULP for now, please make proper use of them.

--------------

How to adjust the warning level for project build?
------------------------------------------------------

  When building the project, it is found that some warnings being treated as errors, causing build failure, as follows:

  .. code:: text

    error: format '%d' expects argument of type 'int *', but argument 3 has type 'uint32_t *' {aka 'long unsigned int *'} [-Werror=format=]

  For the error above, you can modify compilation flags at a component level (in the CMakeLists.txt file in a component) or at a project level (in the CMakeLists.txt file in a project). These two ways have roughly the same effect.

  - To modify compilation flags for a specific component, use the standard CMake function ``target_compile_options``. Please refer to `Controlling Component Compilation <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/build-system.html#controlling-component-compilation>`_. For an example of ``target_compile_options`` at the component level, please see `CMakeLists.txt#L3 <https://github.com/espressif/esp-idf/blob/4d14c2ef2d9d08cd1dcbb68a8bb0d76a666e2b4b/examples/bluetooth/bluedroid/ble/ble_ancs/main/CMakeLists.txt#L3>`_.
  - To modify compilation flags for the whole project, either use standard CMake function ``add_compile_options`` or IDF-specific function ``idf_build_set_property`` to set ``COMPILE_OPTIONS`` property. Please refer to `overriding-default-build-specifications <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/build-system.html#overriding-default-build-specifications>`_.

-----------------

The firmware compiled based on the ESP-IDF SDK varies as it contains the information about ``IDF_PATH`` and compilation time. How to remove that information?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - For SDK v5.0 and the above versions, you can enable the ``CONFIG_APP_REPRODUCIBLE_BUILD`` configuration option. In doing so, the application built upon ESP-IDF does not depend on the build environment and both the .elf file and .bin file of the application remain unchanged even if the following variables change:

    - Directory where the project is located
    - Directory where ESP-IDF is located (IDF_PATH)
    - Build time

    Please refer to the `Reproducible Builds <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/reproducible-builds.html#reproducible-builds>`_ description.

  - For SDK versions below v5.0, you can disable ``CONFIG_APP_COMPILE_TIME_DATE=n`` to remove the built timestamp information and enable ``COMPILER_HIDE_PATHS_MACROS=y`` to hide ``IDF_PATH``.

-------------------

When I downloaded the official application hello_world using ESP32-S3-DevKitM-1, the following error occurred. What is the reason for that?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code:: text

    ESP-ROM:esp32s3-20210327
    Build:Mar 27 2021
    rst:0x7 (TG0WDT_SYS_RST),boot:0x8 (SPI_FAST_FLASH_BOOT)
    Saved PC:0x40043ac8
    Invalid chip id. Expected 9 read 4. Bootloader for wrong chip?
    ets_main.c 329


  - The current error may be related to the chip version on the development board or to the fact that the software version of the ESP-IDF SDK is not the official production version. The chip (ROM) bootloader expects the chip ID is 9, which is the production version of the chip (not a test version). However, in the secondary bootloader header, it sees the chip ID is 4, which is the beta version of the chip. Please refer to the description in `esp-idf/issues/7960 <https://github.com/espressif/esp-idf/issues/7960>`_.
  - The actual version of the chip can be obtained by the command ``esptool.py chip_id``. If the chip version is the production version, this error is related to the version of the used ESP-IDF SDK. For ESP32-S3 series products, ESP-IDF release/v4.4 and later are necessary.

--------------

What is the accuracy of the internal 150 kHz RTC of ESP32 series chips?
------------------------------------------------------------------------------

  The accuracy of the internal 150 kHz RTC of ESP32 series chips is ±5%.

-------------

What versions of ESP-IDF SDK are supported by ESP32-D0WDR2-V3 chip?
------------------------------------------------------------------------

  The supported ESP-IDF versions are: v4.4.1, v4.3.3, v4.2.3, v4.1.3.

---------------

When testing OTA applications based on the ESP32 chip, can I delete the default factory partition in the partition table and set the address of the OTA_0 partition to 0x10000?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Yes. Please note that the offsets of partitions of any app type have to be aligned to 0x10000 (64K).

Why can't the ``espefuse.py burn_key`` command be used to burn ESP32-C3 eFuse BLOCK3?
-------------------------------------------------------------------------------------------

  - ``espefuse.py burn_key`` can only burn data to eFuse blocks of the KEY_DATA type. However, BLOCK3 of ESP32-C3 is of the USR_DATA type by default.
  - You can burn data to eFuse blocks of the USR_DATA type with ``espefuse.py burn_block_data``.

-------------

Why I encountered the following error after I run the firmware based on the ESP-IDF SDK?
--------------------------------------------------------------------------------------------------------

  .. code:: text

    ***ERROR*** A stack overflow in task sys_evt has been detected.

  The error is caused by insufficient system_event task stack. You can try to resolve it by increasing ``Component config`` > ``ESP System Setting`` > ``Event loop task stack size``. However, the overflow occurs because too much logic is being processed within system_event. It is not recommended as it might lead to delayed handling of subsequent events. We suggest forwarding this event to other tasks for processing, either through a queue or other operations.

----------------------------

How to solve the issue of being unable to parse due to spaces in the specified url during Wi-Fi OTA?
--------------------------------------------------------------------------------------------------------------------------------------------------------

  Spaces can be replaced with ``+`` or ``%20`` to solve this issue.

------------------------

How to get the version number of newlib of ESP-IDF?
----------------------------------------------------------------------------------------------------------------------------------------------

  - There are two ways to obtain the version number:

    - 1. Run `xtensa-esp32-elf-gcc -dM -E -x c - <<< "#include <_newlib_version.h>" | grep NEWLIB_VERSION` command to obtain the newlib version number. The printed log should be similar to the following: `#define _NEWLIB_VERSION "4.1.0"`.
    - 2. Search for the newlib version in the toolchain version and find the toolchain version used by ESP-IDF. For example, for ESP-IDF v5.0, you can get the version of the toolchain is esp2021-r1 from `xtensa esp32 elf <https://docs.espressif.com/projects/esp-idf/en/v5.0/esp32/api-guides/tools/idf-tools.html#xtensa-esp32-elf>`__. Go to the release note page of `this toolchain version <https://github.com/espressif/crosstool-NG/releases/tag/esp-2022r1>`__, it can be seen from the link that the newlib version is v4.1.0.

--------------

Does ESP32-P4 support floating-point arithmetic?
-------------------------------------------------------------------------------------------

  - The HP CPU of ESP32-P4 supports floating-point arithmetic, but the LP CPU does not.

-----------

What are the ESP-IDF versions supported by different series of ESP32 chip versions?
-------------------------------------------------------------------------------------------------------------------

  - Please refer to the `ESP-IDF version compatibility with Espressif chip versions <https://github.com/espressif/esp-idf/blob/master/COMPATIBILITY_EN.md>`_ description.

------------

How to check the descriptions of error codes defined in ESP-IDF?
------------------------------------------------------------------------------------------------------------------------------------

  - See: `Error Code Reference <https://docs.espressif.com/projects/esp-idf/en/v5.0.3/esp32c3/api-reference/error-codes.html#error-codes-reference>`__.

------------

Why does the following error occur during firmware operation? What could be the common reason?
----------------------------------------------------------------------------------------------

  .. code:: text

    Guru Meditation Error: Core  1 panic'ed (Unhandled debug exception).
    Debug exception reason: Stack canary watchpoint triggered (zcr_task)

  - The aforementioned log error is usually caused by a stack overflow. You can try increasing the stack size of the zcr_task task.
  - For more information on software exception explanations, refer to `Severe Errors <https://docs.espressif.com/projects/esp-idf/en/v5.2/esp32/api-guides/fatal-errors.html#id1>`__.

---------------------------------------------

Does the ESP chip support using the `esp-bootloader-plus <https://github.com/espressif/esp-bootloader-plus>`__ compression upgrade scheme to upgrade other MCUs?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  No, it's not possible. Compression update for other MCUs is something the user needs to consider. In the compression update of ESP32, the decompression occurs during the bootloader stage, instead of the app stage, so it cannot directly decompress data for other MCUs. However, you can first decompress the data in ESP32 apps, and then send the decompressed data to other MCUs. You can implement this process by yourself. For details, please refer to `xz_decompress_file <https://github.com/espressif/esp-iot-solution/tree/master/examples/utilities/xz_decompress_file>`__ decompression example.

------------

When developing applications based on ESP32, how can I obtain information such as task status, task priority, remaining task stack, and the core used by the task?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - You can use the `vTaskList() <https://docs.espressif.com/projects/esp-idf/en/v5.2.1/esp32s3/api-reference/system/freertos_idf.html#_CPPv49vTaskListPc>`_ function based on FreeRTOS to get relevant information.

------------------

How to obtain the CPU usage of a task when developing applications with ESP32?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - You can use `vTaskGetRunTimeStats() <https://docs.espressif.com/projects/esp-idf/en/v5.2.1/esp32s3/api-reference/system/freertos_idf.html#_CPPv420vTaskGetRunTimeStatsPc>`__ based on FreeRTOS to get the CPU usage of system tasks.

------------------

After downloading the firmware, ESP32 fails to start normally, and the log shows the following information. What could be the reason?
------------------------------------------------------------------------------------------------------------------------------------------------------

  .. code:: text

   E(88)flash parts: partition 0 invalid magic number 0x5e9
   E(95)boot: Failed to verify partition table
   E(100)boot: load partition table error!

  - The above error is usually caused by a mismatch between the address of the downloaded ``partition-table.bin`` and the software setting for ``Partition Table`` > ``Offset of partition table``. In other words, the downloaded address of ``partition-table.bin`` is incorrect.
  - After the project is built, a ``build`` folder is created. Insider the ``build`` folder, there is a ``flash_project_args`` file, which stores the ``bin`` file generated by the project compilation and the corresponding download address information.

---------------

Does it support redirecting the UART0 output logs of ESP32 to the file system?
-----------------------------------------------------------------------------------------------------------------------------------------------------

  Yes. UART0 output logs can be redirected to a file through the `esp_log_set_vprintf <https://docs.espressif.com/projects/esp-idf/en/v5.2.2/esp32/api-reference/system/log.html?highlight=esp_log_set_%20vprintf#_CPPv419esp_log_set_vprintf14vprintf_like_t>`_ API.

----------------

Can the ESP32 BootLoader, which is configured to run in single-core mode, be upgraded to dual-core mode via OTA?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
  - ESP32 does not support this. Each CPU in ESP32 has an independent cache, and the MMU configuration related to the cache is set during the BootLoader. If the BootLoader is configured for single-core mode, but the MMU for the second core is not configured, it will cause an instruction fetch error.
  - Support is available for ESP32-S3 and ESP32-P4. These two chips feature two cores that share the same cache, which eliminates the aforementioned issue. Therefore, they support upgrading from single-core to dual-core mode.

----------------

Does the ESP32 series chip support OTA firmware updates via File Transfer Protocol (FTP)?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
  The default example does not support TLS-based FTP and only implements basic socket programming. However, ESP32 series chips do support TLS-based FTP, and users can implement this feature if needed.

----------------

After using the native_ota_example for an OTA upgrade, why does the device enter the ESP_OTA_IMG_UNDEFINED event, with the ota_state value printed as -1, even though the firmware works normally?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
  This may be due to the application rollback feature not being enabled in menuconfig. Please ensure that the application rollback feature is enabled in the configuration to avoid this issue.
