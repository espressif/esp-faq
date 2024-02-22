Document contribution
=====================

:link_to_translation:`zh_CN:[中文]`

We welcome all the contributions to esp-faq project, such as fixing bugs, adding new documents and etc. We will accept new requests via `Github Pull Requests <https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests>`_.

Commit process
--------------------

This section provides a brief overview of the ``Add new items`` and ``Modify contents`` processes. For the specific requirements during the processes, please refer to the links provided.

Here, we do not provide further operational instructions on ``git``, please see `Git learning material <https://git-scm.com/book/en/v2>`_.

Add new items
~~~~~~~~~~~~~~~~~~~~

1. `Create a new branch`_ following the `Branch naming conventions`_;
2. Find the corresponding ``*.rst`` file locally or on web IDE, then add new items according to the template formats;
3. After your writing finished, you can check the document in the preview interface and build it using `Local build environment`_ to see if it has any formatting issues;
4. Push your branch to github and commit a pull request following the `Commit message standards`_;
5. If all the abovementioned steps are finished following requirements, then you can `Submit a merge request`_;
6. After all the review comments resolved and new pull requests updated, then this process is fully completed.

Modify contents
~~~~~~~~~~~~~~~~~~~~~~

1. `Create a new branch`_ locally following the `Branch naming conventions`_;
2. Find the corresponding ``*.rst`` file locally or on web IDE, then modify the desired contents;
3. After the modification finished, you can check the document in the preview interface and build it using the `Local build environment`_ to see if it has any formatting issues;
4. Push your branch to github and commit a pull request following the `Commit message standards`_;
5. If all the abovementioned steps are finished following requirements, then you can `Submit a merge request`_;
6. After all the review comments resolved and new pull requests updated, this process is fully completed.

Create a new branch
-----------------------

All the new branches are based on the **master branch**, so please make sure your current branch is the one you expect to merge.

For example:

.. code:: text


    git status #To see the status of your current branch
    git checkout -b add/artificial-intelligence_camera_model #To add new contents about "artificial-intelligence camera model"

Branch naming conventions
-------------------------------

- Add a new item: ``add/artificial-intelligence_{q&a}``, ``{q&a}`` is the brief English name of the file. For example, if you expect to add a new item as ``artificial intelligence camera model``, then the branch name should be: ``add/artificial-intelligence_camera_model``.

- Modify contents: ``mod/artificial-intelligence_q&a``, ``q&a`` is the brief English name of the file. For example, if you expect to modify the contents about ``artificial intelligence camera model``, then the branch name should be: ``mod/artificial-intelligence_camera_model``.

Q&A Guidelines
--------------------

Please add new Q&A items and do updates according to the guidelines as follows:

**General guideline:**

- If you are going to add a new Q&A item, always remember to add a separate line after the previous one as "-------------------".

**For questions:**

- Illustrate questions clearly, for example:

  - When flashing firmware to ESP32-S2, an error occurred as “A fatal error occurred: Invalid head of packet (0x50)”? **(NOT Clear)**
  - When flashing firmware to ESP32-S2, an error occurred as “A fatal error occurred: Invalid head of packet (0x50)”. How to resolve such issue? **(Preferable)**

- Do not make the question too long. If this is the case, extract the main question as the title and describe the background and details below.

**For answers:**

- If there will be code in the text, use code box to separate it with the main text.
- If an answer only includes one sentence, there is no need to write a list, just use a regular paragraph.
- Use lists to separate items or to enumerate sequential items:

  - Use numbered lists for items that are in a required order (such as step-by-step instructions) or for items that are referred to by item number.
  - Use bulleted lists for items that are in no required order.

- Provide introductory phrase before a list to indicate the meaning or purpose of the list, and place a colon ":" at the end of it.
- If two items are alternatives, use a bullet list (not numbered list) and indicate their relationship in the introductory phrase.
- Always add two spaces before an listed item or paragraph in the answer.
- When a separate notice or explanatory paragraph follows a item, indent that separate material to the text of the parent list item.
- Follow list punctuation rules described in `Espressif Manual of Style <https://espressifsystems.sharepoint.com/sites/Documentation/Lists/Internal%20Document/DispForm.aspx?ID=1&e=eApbSw>`_, Section Punctuation in Lists.

For more guidance on the rules of list formatting, please refer to `ESP-Docs > Writing Documentation <https://docs.espressif.com/projects/esp-docs/en/latest/writing-documentation/index.html>`__. Please refer to the text and image example templates below.

Q&A example
~~~~~~~~~~~~~~~~~~~~~~~

  .. code:: text


    --------------
    
    Does Espressif have any AI image recognition products?
    --------------------------------------------------------

      Yes, we already have the ESP-EYE development board. With ESP32 as its main control chip, ESP-EYE supports various types of cameras, such as 0v2640, 3660, 5640 and etc.


Q&A figure example
~~~~~~~~~~~~~~~~~~~~~~~~~

  .. code:: text


    --------------

    curses.h: No such file or directory？
    -------------------------------------------

    Screenshot: support ESP8266 chip, but ESP8266_RT

    .. figure:: _static/application-solution/android-application/case_two_kconfig_error.png
        :align: center
        :width: 900
        :height: 100

    Solution: sudo apt-get install libncurses5-dev

Local build environment
----------------------------

-  Use ubuntu or Debian system as test environment, and configure your python version to ``3.7``.
-  It is recommended to use python virtual environment or docker environment.

.. code:: shell


    # Install python3.7 and virtual environment 

    sudo apt-get install python3.7 python3.7-venv

    # Create virtual environment 

    python3.7 -m venv ~/.pyenv3_7

    # Activate virtual environment

    source ~/.pyenv3_7/bin/activate

    # Upgrade pip

    pip install --upgrade pip

    # Install pip component

    pip install -r docs/requirements.txt

    # build the Chinese version

    cd docs/cn/ && make html && cd -

    # Build the English version

    cd docs/en/ && make html && cd -

    # Exit virtual environment

    deactivate

Commit message standards
-----------------------------

Please add commit messages on your branch to explain what you have added/modified/deleted. Each commit has one message, for example:

.. code:: text


    artificial-intelligence: add esp-eye support those camera models

    1. esp-eye support those camera models.

The first line of the commit message should be like "Q&A category: add/fix/modify/delete something". And this line should be started with the file name you updated, for example:

``artificial-intelligence: esp-eye support those camera models.``

If more information should be added into the commit message, please add it in the later commits after the first line.

A good commit message should tell why this update came up, thus making others get to know about this project when reading these commit logs. It may seem like a waste of time to write a good commit message, but it will be useful for you when trying to know why something changed.

Submit a merge request
----------------------------

Once your updates finished, you can conduct the first commit of your branch. Please add more commits if you need to do further updates. After finishing all the commits on this branch, you are ready to submit a merge request.

We use the github "Merge Requests" function to merge your branch into the master, the steps include:

1. Push your branch to the github repository;
2. Go to `esp-faq <https://github.com/espressif/esp-faq>`_ and click "New pull request";
3. Select the branch that you created and waited for merge, and fill detailed information in the "Merge Request".

Please see `IDF Contribution Guide <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/contribute/index.html>`_.

Merge request specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Title:

.. code:: text

    add: a brief overview

- Description:

  Describe the updates of this merge request in points.

- For example：

Title:

.. code:: text

    artificial-intelligence: add esp-eye support those camera models.

Description:

.. code:: text


    1. add esp-eye support those camera models.
