# ESP-FAQ Framework

* [中文版](./README_CN.md)

ESP-FAQ is a summary document for common problems launched by Espressif.

## ESP-FAQ Document framework

### language support

* The document framework supports reStructuredText and Markdown lightweight markup languages.

### Document structure

``` bash
docs
├── _static
│   ├── espressif-logo.svg    # Web log
│   └── theme_overrides.css   # Web Style Sheet
├── zh_CN
│   ├── get-started           # Set started
│   ├── application-solution  # Application solution
│   ├── hardware-selection    # Hardware selection
│   ├── sdk-framework         # Sdk framework
│   ├── test-verification     # Test verification
│   ├── config.py             # Sphinx config
│   ├── Makefile              # Compile file
│   └── index.rst             # Home
└── en
    ├── get-started           # get started
    ├── application-solution  # Application solution
    ├── hardware-selection    # Hardware selection
    ├── sdk-framework         # Sdk framework
    ├── test-verification     # Test verification
    ├── config.py             # Sphinx config
    ├── Makefile              # Compile file
    └── index.rst             # Home
```

### format guide

* Please read the code [format guide](docs/README.md)

## Resources

* Documentation for the latest version: https://docs.espressif.com/projects/esp-faq/. This documentation is built from the docs directory of this repository.

* The esp32.com forum is a place to ask questions and find community resources.

* Check the Issues section on github if you find a bug or have a feature request. Please check existing Issues before opening a new one.

* If you're interested in contributing to ESP-FAQ, please check the Contributions Guide.
