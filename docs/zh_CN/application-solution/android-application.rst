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
-------------------------------------------------

  - 对于 Android 6.0 之后的系统，需要申请位置权限 (android.permission.ACCESS_FINE_LOCATION)。
  - 对于 Android 9.0 之后的系统，除申请位置权限外，还需打开 GPS。
  - 对于 Android 12.0 之后的系统，需要申请扫描权限 (android.permission.BLUETOOTH_SCAN)。

--------------

为什么扫描 Wi-Fi 和蓝牙信号需要位置权限？
------------------------------------------------

  - 在移动设备中，当 GPS 信号不可用或不精确时，可以使用 Wi-Fi 和蓝牙信号定位用户。因此，应用程序需要首先获取位置权限，以使用这些信号来确定设备位置。

  - 此外，Wi-Fi 和蓝牙信号可能也会获取附近的 Wi-Fi 网络和蓝牙设备的相关信息，如设备的 MAC 地址，用于识别特定的设备。应用程序可以通过解析 Wi-Fi 和蓝牙信息来获取用户的当前位置，Google 为了您的隐私考虑，对 Android 6.0 之后的相关 API 加入了位置权限需求。尽管一些操作系统在最新版本中引入了 MAC 地址随机化技术来保护用户的隐私，应用程序仍然需要位置权限来访问这些信号。

  - 总之，为了使用 Wi-Fi 和蓝牙信号来定位用户或获取附近设备的信息，应用程序需要获得位置权限。这有助于保护用户的隐私和安全，并确保应用程序只能使用这些信号来执行预期的操作。

--------------

APP 需要继承第三方库中的 Application 类，但如需同时继承 MultiDexApplication 怎么办？
----------------------------------------------------------------------------------------

  - 在您的 Application 类的 onCreate() 方法中调用 MultiDex.install(this) 即可。

--------------

APP 发送 http 请求报错是为什么？
----------------------------------------

  - Android 高版本中需要使用加密请求，例如 https。若您需要发送 http 请求，在 AndroidMenifest.xml 中 application 标签下添加 android:usesCleartextTraffic="true" 即可。

--------------

怎么把 APP 的签名文件迁移到 pkcs12？
-------------------------------------------

  - keytool -importkeystore -srckeystore 源文件 -destkeystore 生成文件 -deststoretype pkcs12

--------------

在不安装 Android Studio 的情况下怎么查看 APP 的日志输出？
------------------------------------------------------------------

  - 1. 安装 adb 工具。
  - 2. 在命令终端执行下述命令。

  .. code:: bash

    pid=`adb shell ps | grep 包名 | awk '{print $2}'`
    adb logcat | grep --color=auto $pid

--------------

如何在 Module 的 BuildConfig 中添加模块版本信息？
------------------------------------------------------------------

  - 最新的 Android Studio 编译 Module 已经不会自动添加 VERSION_NAME 信息了，若需要该信息，可以在 Module 对应的 build.gradle 中添加以下命令：

  .. code:: groovy

    android {
        defaultConfig {
            buildConfigField "String", "VERSION_NAME", "\"YOUR_MODULE_VERSION\""
        }
    }
