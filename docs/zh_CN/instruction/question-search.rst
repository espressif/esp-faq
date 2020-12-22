问题搜索
========

:link_to_translation:`en:[English]`

此指南目前有以下两个部分： 

- 搜索问题技巧 
- 问题分类框架

搜索问题技巧
------------

目前可以归纳出以下 2 种搜索问题的技巧：

- 搜索关键词 
- 排除某个关键词

搜索关键词
~~~~~~~~~~

将问题中的关键词提取出来并搜索它们，此时搜索结果会得到最匹配的结果。


比如问题为：``ESP32 的 Bluetooth LE 吞吐量是多少？``

此时搜索：``ESP32``、``BLE`` 和 ``吞吐量`` 等关键字为宜。

排除某个关键词
~~~~~~~~~~~~~~

在搜索内容中添加一个标识符 ``-``, 格式为： ``关键词  -排除关键词``。此时搜索结果不会出现有排除关键词的结果。

比如搜索：``ESP32 -ble``。任何搜索结果中有 ``ble`` 的结果将会被过滤。

问题分类框架
------------

在掌握上述 ``搜索问题技巧`` 后，可以利用 ESP-FAQ 已经做好的分类来提取想搜索问题里的关键词并搜索。以下是此网站的框架： 


ESP-FAQ

.. toctree::
   :maxdepth: 1


   Development environment <../development-environment/index>
   Application solution <../application-solution/index>
   Software framework <../software-framework/index>
   Hardware related <../hardware-related/index>
   Test verification <../test-verification/index>
   Commercial FAQ <../commercial-faq/index>
