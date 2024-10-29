Thread
======

:link_to_translation:`en:[English]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

----------------

ESP32-H2 作为 OpenThread RCP 设备，是否支持基于 Linux 主机来构建 Thread 边界路由器 (OpenThread border router) ？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - 支持。ESP32-H2 可以通过 Linux 主机构建 OpenThread 边界路由器，详细步骤请参考：`OpenThread > 指南 > 边界路由器 > 树莓派 <https://openthread.google.cn/guides/border-router/raspberry-pi?hl=cn>`_。
  - 在 Linux 主机端，请运行 `ot-br-posix <https://github.com/openthread/ot-br-posix>`_ SDK；在 ESP32-H2 设备端，请运行 `esp-idf/examples/openthread/ot_rcp <https://github.com/espressif/esp-idf/tree/master/examples/openthread/ot_rcp>`_ 例程。
  - 基于 ESP32-H2 `配置 OpenThread RCP 设备 <https://openthread.google.cn/guides/border-router/build?hl=cn#attach-and-configure-rcp-device>`_ 时，请将 UART 波特率设置为 460800 bps，配置命令如下：

  .. code-block:: c

    OTBR_AGENT_OPTS="-I wpan0 -B wlan0 spinel+hdlc+uart:///dev/ttyUSB2?uart-baudrate=460800"
  
  - 此外，我们还提供了基于 FreeRTOS 系统构建 Thread 边界路由器的方案。详情请参见 `OpenThread > 指南 > 边界路由器 > FreeRTOS <https://openthread.google.cn/guides/border-router/espressif-esp32?hl=cn>`_。

----------------

配备 IEEE 802.15.4 模块并支持 Thread 的 ESP 芯片是否支持通过类似 AT 指令的形式来进行交互？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  支持。OpenThread 发布了公用开源的 `命令行接口 <https://github.com/openthread/openthread/tree/main/src/cli#openthread-cli-reference>`__，可用于组网和参数配置。如果想体验具体的 Demo，可参考 `ot_cli 示例 <https://github.com/espressif/esp-idf/tree/master/examples/openthread/ot_cli>`__。
