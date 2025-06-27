Zigbee
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

Does the Zigbee protocol stack of ESP32-H2 and ESP32-C6 support automatic frequency hopping under interference?
---------------------------------------------------------------------------------------------------------------

  The Zigbee protocol does not mandate automatic frequency hopping. However, this functionality can be implemented at the application layer: by periodically monitoring channel quality, the system can detect severe interference and coordinate a network-wide migration to a different channel.
