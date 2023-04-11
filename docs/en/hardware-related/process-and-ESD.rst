Process and ESD Protection
=================================

:link_to_translation:`zh_CN:[中文]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

----------------------

What should be paid attention to during the ESP32 ESD test?
-------------------------------------------------------------------------------------

  - The Electrostatic Discharge (ESD) test for ESP32 is conducted to ensure that the device has sufficient tolerance to withstand electrostatic discharge. The precautions are as follows:
    - ESD testing should be conducted in an ESD laboratory or ESD protection area, which should have good grounding protection and electrostatic discharge protection facilities.
    - When conducting ESD testing, please use ESD testing equipment that meets international standards, including ESD generators and ESD grounding mats, to ensure the accuracy of the test results.
    - When conducting ESD testing, please make sure you are using a stable 3.3 V voltage. If the EN trace is too long, it may cause a reboot.
    - ESP32 devices should be tested multiple times to verify the reliability of their tolerance, and the test results should be recorded and analyzed.
    - If the module does not respond, please check the voltage of the air discharge or contact discharge used in the test.
