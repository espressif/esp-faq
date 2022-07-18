双线汽车接口 (TWAI)
======================

:link_to_translation:`en:[English]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

--------------

ESP32 当 TWAI® 控制器处于复位模式（即 RESET_MODE 位置 1 或由于总线关闭）或总线关闭恢复状态时，接收错误计数器 (REC) 的数值仍会变化，如何解决？
------------------------------------------------------------------------------------------------------------------------------------------------------

  进⼊复位模式时，应将 ``LISTEN_ONLY_MODE`` 置位，此时 REC 数值不会变化。退出复位模式前或总线关闭恢复完成时，再恢复正常的操作模式。

--------------

ESP32 当 TWAI® 控制器处于总线关闭恢复过程中时，必须等待总线上出现 128 次总线空闲信号（连续 11 个隐性位），才能再次进⼊主动错误状态，如何解决？
--------------------------------------------------------------------------------------------------------------------------------------------------------

  在总线关闭恢复过程中，错误报警限制中断并不⼀定指示恢复过程已完成。⽤户需检查 ``STATUS_NODE_BUS_OFF`` 位来验证恢复过程是否完成。

--------------

ESP32 总线关闭恢复完成后，TWAI® 控制器下⼀次发送的数据可能出错（即不符合 TWAI 数据帧格式），如何解决？
----------------------------------------------------------------------------------------------------------------------------

  ⼀旦通过错误报警限制中断检测到总线关闭恢复完成，TWAI 控制器应先进⼊复位模式来复位控制器的内部信号，随后退出复位模式。

--------------

ESP32 TWAI® 接收到错误的数据帧可能导致下⼀次接收到的数据字节⽆效，如何解决？
----------------------------------------------------------------------------------------------

  ⽤户可以通过置位 INTERRUPT_BUS_ERR_INT_ENA 并在接收到总线错误中断时，读取 ``ERROR_CODE_CAPTURE_REG`` 来检测错误类型及错误位置。如果符合错误产⽣条件（在数据段或 CRC 字段发⽣位错误或填充错误），可以采⽤以下两种解决⽅法：

    - TWAI 控制器可以发送 0 字节的空数据帧来复位 TWAI 控制器的内部信号。建议给空数据帧分配⼀个不会被任何 TWAI 总线上的节点接收的 ID。
    - 硬件复位 TWAI 控制器（需要保存并恢复当前寄存器的数值）。