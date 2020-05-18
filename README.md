# ESP-FAQ Framework

* [中文版](./README_CN.md)

ESP-FAQ is a summary document for common problems launched by Espressif.

## ESP-FAQ Document framework

### language support

* The document framework supports reStructuredText and Markdown lightweight markup languages.

### Configure the environment and compile

* Test and verify the environment using ubuntu or debian system, configure the python environment to `3.7`.
* It is recommended to use python virtual environment, or docker environment.
  
  ``` shell
  # Install python3.7 and virtual environment
  sudo apt-get install python3.7 python3.7-venv

  # Create a virtual environment
  python3.7 -m venv ~/.pyenv3_7

  # Activate the virtual environment
  source ~/.pyenv3_7/bin/activate

  # Update pip
  pip install --upgrade pip
  
  # Install pip components
  pip install -r docs/requirements.txt
  
  # Compile the Chinese version
  cd docs/cn/ && make html && cd -

  # Compile the English version
  cd docs/en/ && make html && cd -

  # Exit the virtual environment
  deactivate

  ```

### Document structure

``` bash
docs
├── _static
│   ├── espressif-logo.svg    # web log
│   └── theme_overrides.css   # Web Style Sheet
├── cn
│   ├── config.py             # sphinx config
│   └── index.rst             # Home
│   └── Makefile              # Compile file
│   └── *.md                  # Specific documents
└── en
    ├── config.py             # sphinx config
    └── index.rst             # Home
    └── Makefile              # Compile file
    └── *.md                  # Specific documents
```

### format guide

* Please read the code [format guide](docs/README.md)

## Resources

* Documentation for the latest version: https://docs.espressif.com/projects/esp-faq/. This documentation is built from the docs directory of this repository.

* The esp32.com forum is a place to ask questions and find community resources.

* Check the Issues section on github if you find a bug or have a feature request. Please check existing Issues before opening a new one.

* If you're interested in contributing to ESP-FAQ, please check the Contributions Guide.
