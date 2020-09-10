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


Why is there a "no module named yaml" error when compiling ESP32-AT?
-----------------------------------------------------------------------

  Please install the yaml module by using ``python -m pip install pyyaml``.