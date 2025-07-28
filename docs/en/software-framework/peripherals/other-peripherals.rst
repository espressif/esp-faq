Other Peripherals
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

Can the REF_TICK clock frequency be modified?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

  :CHIP\: ESP32 | ESP32-S2 | ESP32-C3:

  No, the REF_TICK clock is fixed.

--------------

Does ESP32 support PCI-E protocol?
-----------------------------------------------------

  No, it doesn't.

-----------------

Does ESP32-P4 support video encoding and decoding?
-----------------------------------------------------------------------------------------

  Yes. ESP32-P4 Supports JPEG hardware encoding/decoding, H.264 hardware encoding, and H.264 software decoding.

-----------------

How to Use the Bit Manipulator on ESP32-P4?
-----------------------------------------------------------------------------------------

  The BitScrambler driver has been released. Please refer to `BitScrambler Driver <https://docs.espressif.com/projects/esp-idf/en/latest/esp32p4/api-reference/peripherals/bitscrambler.html>`_. The RMT peripheral now supports BitScrambler.
