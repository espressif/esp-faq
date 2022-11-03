ESP Matter
==========

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

ESP 哪些模组可以接入 Matter？
-------------------------------------------

  - 请参考 `Espressif Matter 平台 <https://docs.espressif.com/projects/esp-matter/en/main/esp32/introduction.html#espressif-matter-platforms>`_。

------------------

想要上手 ESP Matter，有哪些学习资料？
-------------------------------------------

  可以参考：
  - `ESP Matter Github <https://github.com/espressif/esp-matter>`_
  - `Espressif Matter 系列博客 <https://zhuanlan.zhihu.com/p/469263457>`_
  - `Espressif Matter 方案视频 <https://www.bilibili.com/video/BV1sV4y1x74U>`_
  - `Espressif Matter Demo 视频 <https://www.bilibili.com/video/BV1ha411K7p2>`_
  

------------------

`ESP Matter <https://github.com/espressif/esp-matter>`_ 是否能在 Windows 上编译开发？
-------------------------------------------------------------------------------------------------------------------------------------

  - 目前无法在 Windows 上编译。同时，不建议使用虚拟机来进行 ESP Matter 开发，因为 Matter Controller 会使用蓝牙硬件，虚拟机可能会出现未知错误。建议使用 Linux 或 macOS 系统。

------------------

请问在哪里能找到 Matter 协议文档？
-----------------------------------------------------------------------

  现在 Matter 的标准协议已经公开，可以在 `CSA 联盟官网 <https://csa-iot.org/all-solutions/matter/>`_ 中 `提交申请并进行下载 <https://csa-iot.org/developer-resource/specifications-download-request/>`_。

---------------------

如何注册一个 ESP Matter 产品？
----------------------------------------------------------------------------------------------------------------------

  - 注册 Matter 产品需要首先成为 CSA 会员，产品在通过 Matter 认证测试之后，便可以在 CSA 中注册。

---------------------

ESP32-C3 使用 Ubuntu 虚拟机进行 ESP Matter 开发时，发现按照 `Matter 官方教程 <https://github.com/project-chip/connectedhomeip/blob/master/docs/guides/python_chip_controller_building.md>`_ 配网不成功，可能是什么原因？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  不建议使用虚拟机来进行 ESP Matter 开发，因为 Matter Controller 会使用蓝牙硬件，虚拟机可能会出现未知错误。建议直接使用 Ubuntu 20.04 LTS 及以上版本的主机。

---------------------

如何申请 Matter DAC?
----------------------------------------------------------------------------------------------------------------------

  有以下三种方式申请 Matter DAC:

  - 与已成立的 PKI 提供商合作：许多组织已经拥有一个证书颁发机构，他们依赖该证书颁发机构来获取其公钥基础结构证书。在某些情况下，可以从此类 PKI 提供商处获得设备证明证书 (DAC)。
  - 使用您自己的设备证明 PKI：许多组织已经拥有用于执行代码签名、现有设备认证要求或其他依赖非对称加密的任务的公钥基础设施，公钥通过数字证书分发。
  - 与您的平台供应商（Espressif）合作：平台供应商可能使用他们的 VID/PID 在芯片或平台模块中嵌入了 DAC。CD 用于使用 dac_origin_vid/dac_origin_pid 字段重新映射 VID/PID。

---------------------

ESP Matter 是否有测试工具/测试 APP?
----------------------------------------------------------------------------------------------------------------------

  - 有，推荐使用 `chip-tool <https://github.com/project-chip/connectedhomeip/blob/master/docs/guides/chip_tool_guide.md>`_，使用方式示例见 `配置测试 chip tool <https://docs.espressif.com/projects/esp-matter/en/main/esp32/developing.html#test-setup-chip-tool>`_。

---------------------

Matter 配网过程中需要用到 DCL，请问 DCL 的具体功能是什么？
----------------------------------------------------------------------------------------------------------------------

  - Matter DCL 是一种基于区块链技术的，安全加密的分布式存储网络，允许连接标准联盟 (CSA) 和授权供应商发布其 Matter 设备信息，并允许 Matter 生态通过 DCL 客户端查询相关信息。
  - 简化来说，Matter DCL 会用于设备验证及 OTA。

---------------------

我们的产品是基于 Zigbee 的，请问该如何通过 ESP 芯片来接入 Matter？
----------------------------------------------------------------------------------------------------------------------

  - 基于 ZigBee 技术实现的设备并不是 Matter 标准的设备，此时需要通过 Matter Bridge 设备桥接 ZigBee 设备来接入 Matter 网络。
  - Matter Bridge 设备可以使用一颗乐鑫的 Wi-Fi 芯片 + 802.15.4 芯片实现。Matter Bridge For BLE Mesh 设备可以使用一颗乐鑫的 Wi-Fi 芯片 + BLE 芯片实现，或者只用一颗 Wi-Fi + BLE combo 芯片实现。

---------------------

Matter 是否可以对接三星的 smartthings？
----------------------------------------------------------------------------------------------------------------------

  - 可以对接，请参考 `配置测试 smartthings 官方博客 <https://blog.smartthings.com/roundups/smartthings-tests-matter-compatible-products-in-anticipation-of-new-smart-home-standard/>`_。
