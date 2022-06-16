Provisioning
============

:link_to_translation:`zh_CN:[中文]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

-----------------------

Can I add any broadcast data I want to Android ESP-Touch (e.g., add a device ID so that ESP32 can receive this ID)?
------------------------------------------------------------------------------------------------------------------------------------------------------

  - No, the data content sent under the current ESP-Touch protocol is fixed and cannot be customized.
  - If you expect to send customized data, it is recommended to use BluFi, which is the networking protocol based on Bluetooth LE. Please refer to the following references for BluFi:

    - Android APP：https://github.com/EspressifApp/EspBlufiForAndroid.
    - iOS APP：https://github.com/EspressifApp/EspBlufiForiOS.
