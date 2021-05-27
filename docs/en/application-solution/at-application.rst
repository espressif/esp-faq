AT application
==============

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

Why is there a "no module named yaml" error when compiling ESP32-AT?
-----------------------------------------------------------------------

  Please install the yaml module by using ``python -m pip install pyyaml``.

--------------

Why are AT commands keep prompting "busy"?
-------------------------------------------
  The “busy” prompt indicates that the previous command has not been executed yet, and the system cannot respond to the current input. The processing mechanism of the AT commands is serial, i.e. one command at a time. 

  Any input through serial ports is considered to be a command input, so the system will also prompt “busy” or “ERROR” when there is any extra invisible character input.

  For example, when users enter AT+GMR (line break CR LF) + (space) through serial ports, the system will execute the command immediately, because the AT+GMR (line break CR LF) is already considered to be a complete AT command.

  Therefore, the space following the AT+GMR command will be treated as a second command. If AT+GMR has not been processed by the time of receiving the space, the system will prompt “busy”. However, if AT+GMR has been processed, the system will prompt “ERROR”, since space is an incorrect command.

--------------

Where can I get all the resources related to ESP32 AT?
--------------------------------------------------------

  - ESP32 AT bin files: https://www.espressif.com/zh-hans/support/download/at
  - ESP32 AT document: `ESP32 AT Instruction Set and Examples <https://docs.espressif.com/projects/esp-at/zh_CN/latest/AT_Command_Set/index.html>`_

   You can also develop more AT commands based on the core codes of Espressif AT commands. Please find more information on ESP32 AT demos on GitHub: https://github.com/espressif/esp-at.
