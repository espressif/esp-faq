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
--------------------------------------------------------------------------------------

  AD sampling can be triggered in the callback of the MCPWM timer events ``on_ful```, ``on_empty``, ``on_stop``. Additionally, AD sampling can also be triggered in the callback of the MCPWM comparator event ``on_reach``.

---------------

Can ESP32-S3 generate fully complementary PWM with accurate clock and duty cycle and adjustable dead band?
---------------------------------------------------------------------------------------------------------------------

  By measurement, ESP32-S3 can generate complementary output waveforms with the frequency of 10 k, the duty cycle accuracy of 1 us and the dead band accuracy of 100 ns by MCPWM.

-------------

Does the ESP32-S3 support driving eight servos?
--------------------------------------------------------------------------------------------------------------------------

  Yes. As ESP32-S3 supports two MCPWM controllers, which includes three operators each, and each operator has two generators and two comparators. So, if each generator independently uses a comparator, it can produce a total of 2*3*2=12 PWM outputs with independently adjustable duty cycles, which can naturally meet the needs of eight servos.


What are the advantages of MCPWM compared to LEDC?
--------------------------------------------------------------------------------------------------------------------------

  MCPWM supports complementary PWM output, center alignment, dead time insertion, carrier modulation, fault, capture events, etc., which are more advantageous in digital motor control, digital power supply, and FOC scenarios.
