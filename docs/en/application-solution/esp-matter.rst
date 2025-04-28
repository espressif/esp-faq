ESP Matter
==========

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

Which ESP modules can be connected to Matter?
----------------------------------------------------------------------------------

  - Please refer to the `Espressif Matter Platform <https://docs.espressif.com/projects/esp-matter/en/latest/esp32/introduction.html#espressif-matter-platforms>`_.

------------------

What learning materials are available to get started with ESP Matter?
-----------------------------------------------------------------------------------------------

  You can refer to:

  - `ESP Matter Github <https://github.com/espressif/esp-matter>`_
  - `Espressif Matter series blog <https://blog.espressif.com/matter-38ccf1d60bcd>`_
  - `Espressif Matter solution video <https://www.bilibili.com/video/BV1sV4y1x74U>`_
  - `Espressif Matter Demo video <https://www.bilibili.com/video/BV1ha411K7p2>`_

------------------

Can I compile and develop `ESP Matter <https://github.com/espressif/esp-matter>`_ on Windows?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - It is currently not possible to compile on Windows. Also, it is not recommended to use a virtual machine for ESP Matter development, as the Matter Controller will use Bluetooth hardware where unknown errors may occur with the virtual machine. Using Linux or macOS systems directly are recommended.

------------------

Where can I find the Matter protocol documentation?
----------------------------------------------------------------------------------------------

  Currently, Matter's standard protocol has been made public, you can `submit a request and download <https://csa-iot.org/developer-resource/specifications-download-request/>`_ the documentation on the `CSA Alliance official website <https://csa-iot.org/all-solutions/matter/>`_.

---------------------

How to register an ESP Matter product?
--------------------------------------------------------------------------------------------------------------------------------------

  - To register a Matter product requires a CSA membership. After the product passes the Matter certification test, it can be registered with the CSA.

---------------------

When using Ubuntu virtual machine to develop ESP Matter on ESP32-C3, network provisioning failed when I followed the `Matter official tutorial <https://github.com/project-chip/connectedhomeip/blob/master/docs/guides/python_chip_controller_building.md>`_. What could be the reason?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  It is not recommended to use a virtual machine for ESP Matter development, as the Matter Controller will use Bluetooth hardware where unknown errors may occur with the virtual machine. It is recommended to use Ubuntu 20.04 LTS and above hosts directly.

---------------------

How to apply for a Matter DAC?
-----------------------------------------------------------------------------------------------------------------

  There are three ways to apply for a Matter DAC:

  - Cooperate with an established PKI provider: Many organizations already have a certificate authority that they rely on to obtain their public key infrastructure certificates. In some cases, a Device Attestation Certificate (DAC) can be obtained from such a PKI provider.
  - Use your own PKI: Many organizations already have public key infrastructures for code signing, existing device authentication requirements, or other tasks that rely on asymmetric encryption. And public keys are distributed via digital certificates.
  - Cooperate with your platform vendor (Espressif): The platform vendor may embed a DAC in a chip or platform module using their VID/PID. CD is used to remap VID/PID using the dac_origin_vid/dac_origin_pid fields.

---------------------

Does ESP Matter have a test tool/test app?
-------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes, it is recommended to use `chip-tool <https://github.com/espressif/connectedhomeip/tree/v1.0.0.2/examples/chip-tool>`__.

---------------------

Matter needs to use DCL in the network provision process. What is the specific function of DCL?
----------------------------------------------------------------------------------------------------------------------------------------------------

  - Matter DCL is a secure and encrypted distributed storage network based on blockchain technology, which allows the Connection Standards Alliance (CSA) and authorized suppliers to publish their Matter device information. It also allows the Matter ecosystem to query related information through DCL clients.
  - For simplicity, Matter DCL will be used for device verification and OTA.

---------------------

How to connect our Zigbee-based products with Matter through ESP chip?
----------------------------------------------------------------------------------------------------------------------------------------------------------

  - The device based on ZigBee technology is not a Matter standard device. At this time, you need to bridge the ZigBee device through the Matter Bridge device to access the Matter network.
  - Matter Bridge devices can be implemented using an Espressif Wi-Fi chip + 802.15.4 chip. Matter Bridge For BLE Mesh devices can be implemented with one Espressif Wi-Fi chip + BLE chip, or only one Wi-Fi + BLE combo chip.

---------------------

Does Matter work with Samsung's smartthings?
-----------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes, please refer to `Configuration test smartthings official blog <https://blog.smartthings.com/roundups/smartthings-tests-matter-compatible-products-in-anticipation-of-new-smart-home-standard/>`_.

---------------------

Can Matter-enabled ESP devices be remotely controlled using Amazon/Google/Apple voice devices? Do these voice devices need to support the Matter protocol? (For example: Saying "Turn off the light" to turn off the lights in the house)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Using Amazon/Google/Apple voice devices that support Matter protocol, it is possible to remotely control Mattter ESP devices. In addition, if other ecosystems also support the ecosystem of the Matter protocol, then the home hub devices such as speakers in this ecosystem can also control the Matter devices remotely.
  - The specific practical steps are: build a Matter application scenario for testing based on the `esp-matter <https://github.com/espressif/esp-matter>`_ SDK.
    - `Google Matter Test Method <https://developers.home.google.com/matter/get-started>`_
    - `Apple Matter Test Method <https://github.com/project-chip/connectedhomeip/blob/master/docs/guides/darwin.md>`_

-----------------

Does the product need to pass WiFi authentication and Bluetooth BQB authentication before submitting the Matter authentication?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes. Matter is a protocol that runs on other technologies such as Wi-Fi, Ethernet, Thread, and Bluetooth. Before the Matter authentication, the device must be pass the transport layer protocol authenticated. This requires not only the original Wi-Fi or Thread authentication, but also the BQB authentication of the Bluetooth SIG, given that Matter requires the use of Bluetooth for provisioning.

---------------

Where is the DAC (Device Attestation Certificate) pre-imported by ESP Matter module stored?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The DAC (Device Attestation Certificate) pre-imported by the ESP Matter module is stored in flash. In the Matter Pre-Provisioning service, the Matter DAC certificate is pre-flashed in the esp_secure_cert partition. An example of adding this partition to a partition table is as follows:

  .. code-block:: text

    # ESP-IDF Partition Table
    # Name,          Type, SubType, Offset,  Size, Flags
    esp_secure_cert, 0x3F,    ,     0xd000,  0x2000,  , # Never mark this as an encrypted partition

--------------

Can I configure Wi-Fi of ESP32 Matter devices by BLE？
--------------------------------------------------------------------------------------------------------------------------------------------------------------

  - ESP32 Matter devices can be provisioned via BLE, all application test examples under our `esp-matter <https://github.com/espressif/esp-matter>`_ SDK are configured through BLE. Please refer to section `2.2 Commissioning and Control <https://docs.espressif.com/projects/esp-matter/en/latest/esp32/developing.html#commissioning-and-control>`__ for instructions.

---------------

How to solve the following error when provisioning the device with the command ``pairing ble-wifi`` or ``pairing code-wifi`` using the light example in esp-matter via chiptool?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The error log is as follows:

    .. code-block:: text

      [1707138771.417762][46462:46464] CHIP:TOO: Pairing Failure: src/platform/Linux/BLEManagerImpl.cpp:664: CHIP Error 0x00000003: Incorrect state
      [1707138771.417789][46462:46464] CHIP:TOO: Run command failure: src/platform/Linux/BLEManagerImpl.cpp:664: CHIP Error 0x00000003: Incorrect state
      [1707138771.417820][46462:46464] CHIP:BLE: No adapter available for new connection establishment

  - The above error is due to the computer not having a Bluetooth adapter. Please use a computer with a Bluetooth adapter. Laptops generally come with a Bluetooth adapter. If you are using a desktop computer, you will need a Bluetooth dongle to provide Bluetooth functionality.

---------------------

How to generate and install Matter QR codes during mass production?
----------------------------------------------------------------------------------------------------------------------

  You can use the `esp-matter-mfg-tools <https://docs.espressif.com/projects/esp-matter/en/latest/esp32/production.html#the-esp-matter-mfg-tool-example>`__ tool to generate factory information for devices in batch. Then on the production line, flash the generated information and attach the corresponding QR code labels for each device. At the same time, record the mapping between each device's MAC address and its factory firmware for future traceability.
