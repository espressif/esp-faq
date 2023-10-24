Android Application
===================

:link_to_translation:`zh_CN:[中文]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

--------------

Why is the application unable to scan Wi-Fi or Bluetooth signals?
------------------------------------------------------------------------------------------------

  - For systems after Android 6.0, location permission (android.permission.ACCESS_FINE_LOCATION) needs to be requested.
  - For systems after Android 9.0, in addition to requesting location permission, GPS needs to be turned on.
  - For systems after Android 12.0, scanning permission (android.permission.BLUETOOTH_SCAN) needs to be requested.

--------------

Why does scanning Wi-Fi and Bluetooth signals require location permission?
-------------------------------------------------------------------------------------

  - For mobile devices, when GPS signals are unavailable or inaccurate, Wi-Fi and Bluetooth signals can be used to locate users. Therefore, applications need to first obtain location permission to use these signals to determine the device's location.

  - In addition, Wi-Fi and Bluetooth signals may also obtain relevant information about nearby Wi-Fi networks and Bluetooth devices, such as the device's MAC address, to identify specific devices. Since applications can determine the user's current location by parsing Wi-Fi and Bluetooth information, Google has added location permission requirements to relevant APIs after Android 6.0 for privacy. Although some operating systems have introduced MAC address randomization in the latest versions to protect user privacy, applications still need location permission to access these signals.

  - In summary, to use Wi-Fi and Bluetooth signals to locate users or obtain information about nearby devices, applications need to obtain location permission. This can protect user privacy and security, ensuring that only expected operations will be performed.

--------------

While the application needs to inherit the Application class from the third-party library, what if it also needs to inherit MultiDexApplication?
-------------------------------------------------------------------------------------------------------------------------------------------------------------

  You can call MultiDex.install(this) in the onCreate() method of the Application class.

--------------

Why does the application report an error when sending an HTTP request?
-------------------------------------------------------------------------

  In higher versions of Android, encrypted requests, such as HTTPS, need to be used. If you need to send an HTTP request, you can add android:usesCleartextTraffic="true" under the application tag in AndroidMenifest.xml.

--------------

How to migrate the application's signature file to PKCS12?
------------------------------------------------------------

  You can use the following syntax of the ``keytool`` command:

  keytool -importkeystore -srckeystore [source file] -destkeystore [generated file] -deststoretype pkcs12

  In the above command, the meanings of each parameter are as follows:

  - ``-importkeystore``: Import a keystore entry from another keystore.
  - ``-srckeystore [source file]``: Specifies the source keystore file to import from.
  - ``-destkeystore [generated file]``: Specifies the target keystore file to be generated.
  - ``-deststoretype pkcs12``: Specifies that the type of the generated target keystore is in PKCS12 format.

--------------

How to check the application's log without installing Android Studio?
-----------------------------------------------------------------------------

  - 1. Install the adb tool.
  - 2. Execute the following command in the command terminal.

  .. code:: bash

    pid=`adb shell ps | grep package name | awk '{print $2}'`
    adb logcat | grep --color=auto $pid

--------------

How to add module version information in Module's BuildConfig?
---------------------------------------------------------------

  The latest Android Studio does not automatically add VERSION_NAME information when compiling the Module. If you need this information, you can add the following command in the corresponding build.gradle of the Module:

  .. code:: groovy

    android {
        defaultConfig {
            buildConfigField "String", "VERSION_NAME", "\"YOUR_MODULE_VERSION\""
        }
    }
