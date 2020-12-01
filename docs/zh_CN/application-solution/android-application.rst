安卓应用
========

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

为什么 APP 无法扫描到 Wi-Fi 或者蓝牙信号？
------------------------------------------------

  - Android 6.0 之后的系统需要申请位置权限（android.permission.ACCESS_FINE_LOCATION）
  - Android 9.0 之后的系统除了申请位置权限，还需要打开 GPS

--------------

为什么扫描 Wi-Fi 和蓝牙信号需要位置权限？
------------------------------------------------

  - APP 有可能通过解析 Wi-Fi 和蓝牙信息来获取您当前所在的位置，Google 为了您的隐私考虑，Android 6.0 之后的相关 API 加入了位置权限需求

--------------

APP 需要继承第三方库中的 Application 类，但同时需要继承 MultiDexApplication 怎么办？
----------------------------------------------------------------------------------------

  - 在您的 Application 类的 onCreate() 方法中调用 MultiDex.install(this) 即可

--------------

APP 发送 http 请求报错是为什么？
----------------------------------------

  - Android 高版本中需要使用加密请求例如 https，若你依然需要发送 http 请求，在 AndroidMenifest.xml 中 application 标签下添加 android:usesCleartextTraffic="true" 即可

--------------

怎么把 APP 的签名文件迁移到 pkcs12 ？
-------------------------------------------

  - keytool -importkeystore -srckeystore 源文件 -destkeystore 生成文件 -deststoretype pkcs12

--------------

在不安装 Android Studio 的情况下怎么查看 APP 的 log 输出？
------------------------------------------------------------------
  - 1. 安装 adb 工具
  - 2. 在命令终端执行下述命令

.. code:: bash

  pid=`adb shell ps | grep 包名 | awk '{print $2}'`
  adb logcat | grep --color=auto $pid
