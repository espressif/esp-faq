Peripherals
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

--------------

Taken ESP-WROOM-S2 as the slave device and STM32 as MCU, is it possible to download through SPI interface?
---------------------------------------------------------------------------------------------------------------

  No, we use UART0 to download by default. You can also design OTA support yourself in firmware.

--------------

What is the maximum speed supported by the SDIO interface?
------------------------------------------------------------

  The maximum clock speed supported by the hardware SDIO slave module is 50 MHz. As SDIO specifies use of quad data lines, the effective maximum bit rate is 200 Mbps.

--------------

Does the hardware SDIO interface support SD cards?
----------------------------------------------------

  Please note that the SDIO hardware only supports the device or slave profile, i.e. it cannot act as a host to control SDIO devices such as SD cards.

--------------

When certain RTC peripherals（SARADC1，SARADC2，AMP，HALL） are powered on, the inputs of GPIO36 and GPIO39 will be pulled down for approximately 80 ns. 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  When enabling power for any of these peripherals, ignore input from GPIO36 and GPIO39. 

--------------

When the LEDC is in decremental fade mode, a duty overflow error can occur.
-----------------------------------------------------------------------------------------------

  - This issue is automatically worked around in the LEDC driver since the ESP-IDF commit IDb2e264e and will be part of the ESP-IDF V3.1 release. 
  - When using LEDC, avoid the concurrence of following three cases: 
    1. The LEDC is in decremental fade mode;
    2. The scale register is set to 1;
    3. The duty is 2\ :sup:`LEDC_HSTIMERx_DUTY_RES` or 2\ :sup:`LEDC_LSTIMERx_DUTY_RES`. 

--------------

When the CAN controller enters reset mode or when the CAN controller undergoes bus-off recovery, the REC is still permitted to change， how to solve?
------------------------------------------------------------------------------------------------------------------------------------------------------

  When entering reset mode, the CAN controller should set the the LISTEN_ONLY_MODE to freeze the REC. The desired mode of operation should be restored before exiting reset
  mode or when bus-off recovery completes. 

--------------

When the CAN controller undergoes the bus-off recovery process, the controller must monitor 128 occurrences of the bus free signal before it can become error active again, how to solve?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  When undergoing bus-off recovery, an error warning interrupt does not necessarily indicate  the completion of recovery. Users should check the ``STATUS_NODE_BUS_OFF`` bit to verify
  whether bus-off recovery has completed. 

--------------

Upon completion of bus-off recovery, the next message that the CAN controller transmits may be erroneous?
-------------------------------------------------------------------------------------------------------------------------

  Upon detecting the completion of bus-off recovery (via the error warning interrupt), the CAN controller should enter then exit reset mode so that the controller’s internal signals are reset. 

--------------

Receiving an erroneous data frame can cause the data bytes of the next received data frame to be invalid, how to solve?
--------------------------------------------------------------------------------------------------------------------------------------------------

  Users can detect the errata triggering condition (i.e., bit or stuff error in the data or CRC field) by setting the ``INTERRUPT_BUS_ERR_INT_ENA`` and checking the
  ``ERROR_CODE_CAPTURE_REG`` when a bus error interrupt occurs. If the errata condition is met, the following workarounds are possible: 

    - The CAN controller can transmit a dummy frame with 0 data bytes to reset the controller’s internal signals. It is advisable to select an ID for the dummy frame that
      can be filtered out by all nodes on the CAN bus. 
    - Hardware reset the CAN controller (will require saving and restoring the current register values). 
  
--------------

The ESP32 GPIO peripheral may not trigger interrupts correctly if multiple GPIO pads are configured with edge-triggered interrupts, how to solve?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - Workaround 1: 

    - Follow the steps below to trigger a GPIO interrupt on a rising edge: 

      1. Set the GPIO interrupt type to high.
      2. Set the interrupt trigger type of the CPU to edge. 
      3. After the CPU services the interrupt, change the GPIO interrupt type to low. A second interrupt occurs at this time, and the CPU needs to ignore the interrupt service routine. 

    - Similarly, follow the steps below to trigger a GPIO interrupt on a falling edge: 

      1. Set the GPIO interrupt type to low.
      2. Set the interrupt trigger type of the CPU to edge.
      3. After the CPU services the interrupt, change the GPIO interrupt type to high. A second interrupt occurs at this time, and the CPU needs to ignore the interrupt service routine.

  - Workaround 2: 

    Assuming GPIO0 ~ GPIO31 is Group1 and GPIO32 ~ GPIO39 is Group2. 

      - If an edge-triggered interrupt is configured in either group then no other GPIO
        interrupt of any type should be configured in the same group.
      - Any number of level-triggered interrupts can be configured in a single group, if no
        edge-triggered interrupts are configured in that group. 
