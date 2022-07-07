Two-Wire Automotive Interface (TWAI)
====================================

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

When the TWAI® controller enters reset mode or when the TWAI controller undergoes bus-off recovery, the REC is still permitted to change. How to resolve such issue?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  When entering reset mode, the TWAI controller should set the ``LISTEN_ONLY_MODE`` to freeze the REC. The desired mode of operation should be restored before exiting reset mode or when bus-off recovery completes. 

--------------

When the TWAI® controller undergoes the bus-off recovery process, the controller must monitor 128 occurrences of the bus free signal before it can become error active again. How to resolve such issue?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  When undergoing bus-off recovery, an error warning interrupt does not necessarily indicate the completion of recovery. Users should check the ``STATUS_NODE_BUS_OFF`` bit to verify whether bus-off recovery has completed. 

--------------

Upon completion of bus-off recovery, the next message that the TWAI® controller transmits may be erroneous?
---------------------------------------------------------------------------------------------------------------------------------------------------

  Upon detecting the completion of bus-off recovery (via the error warning interrupt), the CAN controller should enter then exit reset mode so that the controller’s internal signals are reset. 

--------------

When the TWAI® Controller receives an erroneous data frame, the data bytes of the next received data frame become invalid, how to resolve such issue?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Users can detect the errata triggering condition (i.e., bit or stuff error in the data or CRC field) by setting ``INTERRUPT_BUS_ERR_INT_ENA`` and checking ``ERROR_CODE_CAPTURE_REG`` when a bus error interrupt occurs. If the errata condition is met, the following workarounds are possible: 

  - The TWAI controller can transmit a dummy frame with 0 data byte to reset the controller’s internal signals. It is advisable to select an ID for the dummy frame that can be filtered out by all nodes on the TWAI bus. 
  - Hardware reset the TWAI controller (will require saving and restoring the current register values). 
