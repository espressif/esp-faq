工艺与 ESD 防护
=================

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

ESP32 ESD 测试注意事项有哪些？
-----------------------------------------------------------------------

  - ESP32 的 ESD（Electrostatic Discharge，静电放电）测试是为了确保 ESP32 设备在遭受静电放电时具有足够的耐受能力。注意事项如下：
    - ESD 测试应该在 ESD 实验室或者 ESD 防护区域进行，这些地方需要具备良好的接地保护和静电放电保护设施。
    - 在进行 ESD 测试时，应该使用符合国际标准的 ESD 测试设备，包括 ESD 发生器和 ESD 接地垫等，以确保测试结果的准确性。
    - 在进行 ESD 测试时，需要稳定的 3.3 V 电压，EN trace 如果太长，容易导致重启。
    - 应对 ESP32 设备进行多次测试，以验证其耐受能力的可靠性，并对测试结果进行记录和分析。
    - 如模组无反应，请确认测试的空气放电或接触放电的具体电压。
