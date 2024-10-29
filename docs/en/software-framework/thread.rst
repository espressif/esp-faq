Thread
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

----------------

Does ESP32-H2, as an OpenThread RCP device, support building a Thread border router based on a Linux host?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Yes. ESP32-H2 can build an OpenThread border router via a Linux host. For detailed steps, please refer to: `OpenThread > Guides > Border Router > Raspberry Pi <https://openthread.google.cn/guides/border-router/raspberry-pi>`_.
  - On the Linux host side, please run the `ot-br-posix <https://github.com/openthread/ot-br-posix>`_ SDK; on the ESP32-H2 device side, please run the `esp-idf/examples/openthread/ot_rcp <https://github.com/espressif/esp-idf/tree/master/examples/openthread/ot_rcp>`_ example.
  - When `configuring the OpenThread RCP device <https://openthread.google.cn/guides/border-router/build#attach-and-configure-rcp-device>`_ on ESP32-H2, please set the UART baud rate to 460800 bps. The configuration command is as follows:

  .. code-block:: c

    OTBR_AGENT_OPTS="-I wpan0 -B wlan0 spinel+hdlc+uart:///dev/ttyUSB2?uart-baudrate=460800"
  
  - In addition, we also provide a solution for building a Thread border router based on the FreeRTOS system. For details, please refer to `OpenThread > Guides > Border Router > FreeRTOS <https://openthread.google.cn/guides/border-router/espressif-esp32>`_.

----------------

Does the ESP chip equipped with an IEEE 802.15.4 module and supporting Thread allow interaction in the form of AT-like commands?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Yes. OpenThread has released a public open-source `command line interface <https://github.com/openthread/openthread/tree/main/src/cli#openthread-cli-reference>`__, which can be used for networking and parameter configuration. To try a specific demo, please refer to the `ot_cli example <https://github.com/espressif/esp-idf/tree/master/examples/openthread/ot_cli>`__.
