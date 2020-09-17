贡献指南
========

:link_to_translation:`en:[English]`

我们欢迎对 esp-faq 项目做出贡献-修复错误，添加文档。我们通过 `Github Pull Requests <https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests>`_ 接受贡献。

1 提交流程
----------

这一节，是对 ``新增问题`` 和 ``修改问题`` 两个操作的流程简要介绍，流程中涉及的环节具体要求，请点击链接查看。

针对 ``git`` 相关操作不做具体的介绍，可以查看 `Git相关教程 <https://git-scm.com/book/zh/v2>`_。

1.1 新增问题
~~~~~~~~~~~~

1. 在本地 `新建分支 <#2-新建分支>`__，遵循 `分支命令规范 <#3-分支命令规范>`__；
2. 在本地或者 web IDE 找到与问题类型对应的 ``*.rst`` 文件，根据模板格式新增问题；
3. 编辑完成后，打开预览界面查看显示结果是否符合预期，可以使用 `本地编译工具 <#5-本地编译环境>`_ 编译文档，并检查生成网页是否满足；
4. 遵循 `提交信息规范 <#6-提交信息规范>`_，推送到 github 后并提交 Pull Requests；
5. 若满足上述预期，则 `提交合并请求 <#7-提交合并请求>`__；
6. 待文档所有讨论解决并成功提交 PR，即完成新增问题的流程。

1.2 修改问题
~~~~~~~~~~~~

1. 在本地 `新建分支 <#2-新建分支>`_，遵循 `分支命令规范 <#3-分支命令规范>`_；
2. 在本地或者 web IDE 找到与问题类型对应的 ``*.rst`` 文件，修改期望修改的问题；
3. 编辑完成后，打开预览界面查看显示结果是否符合预期，可以使用 `本地编译工具 <#5-本地编译环境>`_ 编译文档，并检查生成网页是否满足；
4. 遵循 `提交信息规范 <#6-提交信息规范>`__，推送到 github 后并提交 Pull Requests；
5. 若满足上述预期，则 `提交合并请求 <#7-提交合并请求>`__；
6. 待文档所有讨论解决并成功提交 PR，即完成修改的流程。

2 新建分支
----------

新建分支都基于 主分支 进行；操作时，请留意当前所在分支是否为你期望合入的分支。

操作示例:

.. code:: text


    git status #查看当前分支
    git checkout -b add/artificial-intelligence_camera_model，用于新增问题 "artificial-intelligence camera model"

3 分支命名规范
--------------

- 新增问题：``add/artificial-intelligence_{q&a}``, ``{q&a}`` 使用文件名的英语简要，例如

  新增 ``artificial intelligence camera model`` 问题，分支名：``add/artificial-intelligence_camera_model``

- 修改问题：``mod/artificial-intelligence_q&a``, ``q&a`` 使用文件名的英语简要，例如

  修改 ``artificial intelligence camera model`` 问题，分支名：``mod/artificial-intelligence_camera_model``

4 问题编辑规范
--------------

参考问题模板。

4.1 问题模块示例
~~~~~~~~~~~~~~~~

.. code:: text


    ---

    乐鑫是否已有 AI 图像识别的产品？
    =============================

    ..
     已有标准开发板 ESP-EYE，主控芯⽚为 ESP32

    乐鑫已有标准开发板 ESP-EYE，主控芯⽚为 ESP32，可兼容 0v2640，3660，5640 等多款摄像头。

4.2 问题图片示例
~~~~~~~~~~~~~~~~

.. code:: text


    ---

    curses.h: No such file or directory?
    =====================================

    ..
     问题截图：support ESP8266 chip, but ESP8266_RT

    .. figure:: _static/application-solution/android-application/case_two_kconfig_error.png
        :align: center
        :width: 900
        :height: 100

    解决方法 ：sudo apt-get install libncurses5-dev

5 本地编译环境
--------------

-  测试验证环境使用 ubuntu 或 debian 系统，配置 python 环境为 ``3.7``。
-  推荐使用 python 虚拟环境，或者 docker 环境。

.. code:: shell


    # 安装 python3.7 与虚拟环境 

    sudo apt-get install python3.7 python3.7-venv

    # 创建虚拟环境 

    python3.7 -m venv ~/.pyenv3_7

    # 激活虚拟环境 

    source ~/.pyenv3_7/bin/activate

    # 更新 pip

    pip install --upgrade pip

    # 安装 pip 组件

    pip install -r docs/requirements.txt

    # 编译中文版本 

    cd docs/cn/ && make html && cd -

    # 编译英文版本 

    cd docs/en/ && make html && cd -

    # 退出虚拟环境 

    deactivate

6 提交信息规范
--------------

在分支上添加提交信息，以说明添加/修改/删除问题功能。每个提交都有一条消息，例如：

.. code:: text


    artificial-intelligence: add esp-eye support those camera models

    1. esp-eye support those camera models.

提交信息的第一行应类似于“问题类别：添加/修复/删除/更改内容”。第一行以提交要更改的文件名的名称开头。例如：

``artificial-intelligence: esp-eye support those camera models.``

要添加有关该提交的更多详细信息，请将其放在第一行之后的提交消息中。

一个好的 git 提交消息讲述了一个为什么发生更改的故事，因此，阅读提交日志的人可以了解项目的开发。编写良好的提交信息现在看来似乎是在浪费时间，但是在将来尝试了解某些原因更改时，这对您和您的同事很有用（对我们的客户也有用）。

7 提交合并请求
--------------

一旦完成修改就可以对分支进行第一次提交，如果您需要进行更多的更改，请进行更多提交。完成您对该分支的所有提交后，提交合并请求。

我们使用 github 合并请求功能将分支合并到主分支中，步骤：

1. 将您的分支推送到 github 仓库；
2. 转到 `esp-faq <https://github.com/espressif/esp-faq>`_，然后单击 “New pull request”；
3. 选择您刚创建准备合并的分支，然后填写“合并请求”详细信息。

参考：`IDF贡献代码 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/contribute/index.html>`__

7.1 提交合并请求相关规范
~~~~~~~~~~~~~~~~~~~~~~~~

- Title 要求:

.. code:: text

    add: 简要描述

- Description 要求:

  分点描述该合并修改的信息。

- 示例：

Title:

.. code:: text

    artificial-intelligence: add esp-eye support those camera models.

Description:

.. code:: text


    1. add esp-eye support those camera models.

