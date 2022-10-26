Motor Control Pulse Width Modulator (MCPWM)
===========================================

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

Does ESP32 support using the MCPWM Timer to trigger AD sampling?
-------------------------------------------------------------------------------------

  No, it does not.

---------------

Can ESP32-S3 generate fully complementary PWM with accurate clock and duty cycle and adjustable dead band?
---------------------------------------------------------------------------------------------------------------------

  By measurement, ESP32-S3 can generate complementary output waveforms with the frequency of 10 k, the duty cycle accuracy of 1 us and the dead band accuracy of 100 ns by MCPWM.