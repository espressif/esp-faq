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

What should be paid attention in ESP32 ESD test?
----------------------------------------------------------

  - Stable 3.3 V voltage is necessary in the ESD test. Too long EN trace may lead to reboot.
  - Please check the voltages of air discharge and contact discharge if the module does not work.