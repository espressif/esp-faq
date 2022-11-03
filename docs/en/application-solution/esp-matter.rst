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
---------------------------------------------------------------------------------

  - Please refer to `Espressif Matter Platforms <https://docs.espressif.com/projects/esp-matter/en/main/esp32/introduction.html#espressif-matter-platforms>`_.

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

When ESP32-C3 uses Ubuntu virtual machine to develop ESP Matter, it is found that according to `Matter official tutorial <https://github.com/project-chip/connectedhomeip/blob/master/docs/guides/python_chip_controller_building.md>`_, the network provision is unsuccessful. What could be the reason?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  It is not recommended to use a virtual machine for ESP Matter development, as the Matter Controller will use Bluetooth hardware where unknown errors may occur with the virtual machine. It is recommended to use Ubuntu 20.04 LTS and above hosts directly.

---------------------

How to apply for a Matter DAC?
-----------------------------------------------------------------------------------------------------------------

  There are three ways to apply for a Matter DAC:

  - Cooperate with an established PKI provider: Many organizations already have a certificate authority that they rely on to obtain their public key infrastructure certificates. In some cases, a Device Attestation Certificate (DAC) can be obtained from such a PKI provider.
  - Use your own PKI: Many organizations already have public key infrastructures for code signing, existing device authentication requirements, or other tasks that rely on asymmetric encryption, and public keys are distributed via digital certificates.
  - Cooperate with your platform vendor (Espressif): The platform vendor may embed a DAC in a chip or platform module using their VID/PID. CD is used to remap VID/PID using the dac_origin_vid/dac_origin_pid fields.

---------------------

Does ESP Matter have a test tool/test app?
-------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes, it is recommended to use `chip-tool <https://github.com/project-chip/connectedhomeip/blob/master/docs/guides/chip_tool_guide.md>`_. You can also refer to `Configuration test chip tool <https ://docs.espressif.com/projects/esp-matter/en/main/esp32/developing.html#test-setup-chip-tool>`_.

---------------------

Matter needs to use DCL in the network provision process. What is the specific function of DCL?
----------------------------------------------------------------------------------------------------------------------------------------------------

  - Matter DCL is a secure and encrypted distributed storage network based on blockchain technology, which allows the Connection Standards Alliance (CSA) and authorized suppliers to publish their Matter device information. It also allows the Matter ecosystem to query related information through DCL clients.
  - For simplicity, Matter DCL will be used for device verification and OTA.

---------------------

How to connect our Zigbee-based products with Matter through ESP chip?
----------------------------------------------------------------------------------------------------------------------------------------------------------

  - The device based on ZigBee technology is not a Matter standard device. At this time, it is necessary to bridge the ZigBee device through the Matter Bridge device to access the Matter network.
  - Matter Bridge devices can be implemented using an Espressif Wi-Fi chip + 802.15.4 chip. Matter Bridge For BLE Mesh devices can be implemented with one Espressif Wi-Fi chip + BLE chip, or only one Wi-Fi + BLE combo chip.

---------------------

Does Matter work with Samsung's smartthings?
-----------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes, please refer to `Configuration test smartthings official blog <https://blog.smartthings.com/roundups/smartthings-tests-matter-compatible-products-in-anticipation-of-new-smart-home-standard/>`_.
