# ESP-FAQ Framework

[![Documentation Status](https://readthedocs.com/projects/espressif-esp-faq/badge/?version=latest)](https://docs.espressif.com/projects/espressif-esp-faq/en/latest/?badge=latest)

* [中文版](./README_CN.md)

ESP-FAQ is a summary document for common problems launched by Espressif.

## Hosted Documentation

* English: https://docs.espressif.com/projects/espressif-esp-faq/en/latest/ (TODO)
* 中文: https://docs.espressif.com/projects/espressif-esp-faq/zh_CN/latest/

## ESP-FAQ Document framework

### language support

* The document framework supports reStructuredText and Markdown lightweight markup languages.

### Document structure

``` bash
docs
├── _static
│   ├── espressif-logo.svg       # Web logo
│   └── theme_overrides.css      # Web Style Sheet
├── zh_CN
│   ├── _static                  # Inline resources
│   ├── instruction              # Instruction
│   ├── commercial-faq           # Commercial faq
│   ├── development-environment  # Development environment
│   ├── application-solution     # Application solution
│   ├── hardware-related         # Hardware related
│   ├── software-framework       # Software framework
│   ├── test-verification        # Test verification
│   ├── config.py                # Sphinx config
│   ├── Makefile                 # Compile file
│   └── index.rst                # Home
└── en
    ├── _static                  # Inline resources
    ├── instruction              # Instruction
    ├── commercial-faq           # Commercial faq
    ├── development-environment  # Development environment
    ├── application-solution     # Application solution
    ├── hardware-related         # Hardware related
    ├── software-framework       # Software framework
    ├── test-verification        # Test verification
    ├── config.py                # Sphinx config
    ├── Makefile                 # Compile file
    └── index.rst                # Home
```

## Resources

* The [esp32.com forum](https://esp32.com/) is a place to ask questions and find community resources.

* [Check the Issues section on github](https://github.com/espressif/esp-faq/issues) if you find a bug or have a feature request. Please check existing Issues before opening a new one.

* If you're interested in contributing to ESP-IDF, please check the [Contributions Guide](https://docs.espressif.com/projects/espressif-esp-faq/en/latest/instruction/document-contribution.html).
