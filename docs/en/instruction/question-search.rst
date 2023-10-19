Question search
===============

:link_to_translation:`zh_CN:[中文]`

This instruction includes the following two parts：

- Question search techniques
- Question classification framework

Question Search Techniques
-----------------------------

Currently, there are mainly two searching techniques: 

- Search keywords
- Exclude a specific keyword

Search key words
~~~~~~~~~~~~~~~~~~~

Extract keywords from your question and search for them, then the search results should list the best matches.

For example, if you expect to ask a question as ``What is the Bluetooth LE Throughput for ESP32?``

Then just searching keywords such as ``ESP32``, ``BLE`` and ``throughput`` should give you the result.

Exclude a Specific Keyword
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add a tag ``-`` into the search content in the format: ``keyword -excluded keyword``. By doing so, the search results will not show the specific keyword you excluded.

For example, if you search ``ESP32 -ble``, then any results with ``ble`` inside will not be shown.

Question Classification Categories
------------------------------------

Once you have mastered the above mentioned ``question search techniques``, you can use the categories in ESP-FAQ for reference to extract keywords for the questions you expect to ask and then search for them. The framework of ESP-FAQ categories is shown as follows:

- :doc:`Development environment <../development-environment/index>`
- :doc:`Application solution <../application-solution/index>`
- :doc:`Software framework <../software-framework/index>`
- :doc:`Hardware related <../hardware-related/index>`
- :doc:`Test verification <../test-verification/index>`
- :doc:`Commercial FAQ <../commercial-faq/index>`
