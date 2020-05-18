# Format guide

* [中文版](./README_CN.md)

## New document

* Copy the new file `new.md` Chinese and English documents to the cn and en directories respectively.
* Add a new folder in the _static directory to store document pictures.
* Add the document index path in the index.rst file.

  ``` rst
  ESP-FAQ
  =============

  .. role:: bolditalics
  :class: bolditalics

  | Espressif FAQ (Frequently Asked Questions).

  .. toctree::
  :hidden:

  NEW <new>>
  ```

## Add Q & A

* Organize Q & A according to sample template.

  ``` Markdown
  ## SDK ESP-IDF support ESP8266 chip

  - `Q:`
    - SDK ESP-IDF support ESP8266 chip?

  - `A:`SDK
    - ESP-IDF SDK not support ESP8266 chip, but ESP8266_RTOS_SDK SDK release/v3.0 and later versions have been replaced with ESP-IDF style, and some components are already compatible.
    ```

* Add Q & A question pairs to corresponding categories in the `*. Md` document.
