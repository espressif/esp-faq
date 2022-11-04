ESP RainMaker 云服务
========================

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

ESP RainMaker 有哪些资料可供方案评估与验证？
---------------------------------------------

  请参考如下链接：

  - `方案预览 <https://rainmaker.espressif.com/zh-hans/index.html>`_
  - `入门开发指南 <https://rainmaker.espressif.com/docs/get-started.html>`_
  - `API 指南 <https://rainmaker.espressif.com/docs/api.html>`_
  - `RainMaker 设备固件开发仓库 <https://github.com/espressif/esp-rainmaker>`_
  - `RainMaker Android App 开发仓库 <https://github.com/espressif/esp-rainmaker-android>`_
  - `RainMaker iOS App 开发仓库 <https://github.com/espressif/esp-rainmaker-ios>`_
  - `ESP RainMaker 部署资料 <http://customer.rainmaker.espressif.com/docs/intro/>`_

--------------

ESP RainMaker 对接了哪些语音平台? 支持哪些语音指令？
-----------------------------------------------------

  - 目前 ESP RainMaker 通过云云对接的形式完成了对 Alexa App 和 Google Home App 的支持，通过 `ESP HomeKit SDK <https://github.com/espressif/esp-homekit-sdk>`_ 对接了苹果的家庭 App。在上述 App 中添加设备后，即可使用对应的语音助手完成语音控制。建议使用 `homekit_switch <https://github.com/espressif/esp-rainmaker/tree/master/examples/homekit_switch>`_ 进行测试，该 Demo 将已开关的产品形态出现在上述所有 App 中。
  - Alexa 部分请参考 `Alexa 所支持的语音指令 <https://www.amazon.com/Espressif-Systems-ESP-RainMaker/dp/B0881W7RPV/>`_。
  - Google Assistant 部分请参考 `Google Assistant 所支持的语音指令 <https://assistant.google.com/services/a/uid/0000001421a84610?hl=en_us&source=web>`_。
  - Siri 部分请参考 `Siri 所支持的语音指令 <https://support.apple.com/zh-cn/HT208280>`_。

--------------

RainMaker 设备的证书如何获取？是否有管理后台？
------------------------------------------------

  - 在方案验证阶段，您可以使用 `Claiming 服务 <https://rainmaker.espressif.com/docs/claiming.html>`_ 获取证书，`RainMaker 设备固件开发仓库 <https://github.com/espressif/esp-rainmaker>`_ 中提供的 Demo 都默认启用了该服务。在量产阶段，您需要首先完成私有化部署，可以咨询 `乐鑫商务 <https://www.espressif.com/zh-hans/contact-us/sales-questions>`_ 来获取更为详细的批量生成证书指导及部署事宜。
  - 目前 ESP RainMaker 方案提供了一个 `在线网页 <https://dashboard.rainmaker.espressif.com>`_ 以查看设备信息，并支持通过该网页下发 OTA 任务及查看 `ESP insight <https://github.com/espressif/esp-insights>`_ 数据。

--------------

ESP RainMaker 固件侧代码开发与腾讯云、阿里云的开发模式有什么不同？
------------------------------------------------------------------

 - 腾讯云、阿里云通常是在控制台创建产品，随后创建设备模型；而 RainMaker 则在设备侧通过 API 创建模型，连接网络后将模型发送给云。
 - 腾讯云、阿里云的连接认证阶段通常有 2 种形式：使用证书/三元组（四元组）或使用动态注册。ESP RainMaker 仅支持证书的形式。
 - RainMaker 设备固件开发 SDK 基于成熟的 ESP-IDF 开发框架，对配网、OTA 升级、本地控制等功能做了整合，进行基本的配置即可使用。您不需要移植其他第三方 SDK，直接编写应用层代码即可，该部分完全开源。
 - RainMaker 云中间件基于 AWS 无服务器计算 (Amazon Serverless Computing) 构建，开发者无需在云中编写任何代码、也无需进行任何配置即可使用，该部分不开源。
 - RainMaker App 提供 iOS 与 Android 两个版本，App 可根据设备上报的配置自动加载 UI 及图标，同时也将完整展示设备的物模型，用户可以直接在 App 上更改这些属性。App 将协助用户完成设备的网络配置、本地发现、创建定时任务，该部分完全开源。

--------------

ESP RainMaker 公有云与 ESP RainMaker 私有云有什么区别？
------------------------------------------------------------------

  - ESP RainMaker 是乐鑫提供的一套连接 AWS 的方案，该方案利用了 AWS 提供的一些云产品实现了设备接入、管理、维护、分析功能，乐鑫针对这个方案提供了 App、固件侧的源代码。同时为了方便您测试体验，我们部署了一套公共服务，任何开发者都可以免费使用，我们称之为 ESP RainMaker 公有云。在没有特别申明的情况下，此页面中的 ESP RainMaker 均代指公有云。
  - 如果您想将 ESP RainMaker 部署在自己的 AWS 账号上，首先您需联系 `乐鑫商务 <https://www.espressif.com/zh-hans/contact-us/sales-questions>`_ 以开放相关服务的访问权限，然后可参考 `ESP RainMaker 部署资料 <http://customer.rainmaker.espressif.com/docs/intro/>`_ 完成私有化部署。在完成私有化部署后，您将拥有自己的账户体系及管理后台。此时，我们称之为 ESP RainMaker 私有云。

--------------

Nova Home 跟 ESP RainMaker 有什么关系？
--------------------------------------------

  - Nova Home 与公有 ESP RainMaker 所使用的服务器完全一致，账户互通，不同点在于 App 端。 
  - Nova Home App 相对于 ESP RainMaker App， 对 UI 界面及图标做了相关优化，增加了一些业务侧逻辑，目前以通用固件的形式对接了插座、开关、球泡灯等电工照明产品。如您希望接入试用，可以联系 `乐鑫商务 <https://www.espressif.com/zh-hans/contact-us/sales-questions>`_ 获取更多详细信息。

--------------

除 Github 外是否有其他途径拉取 ESP RainMaker 源码？
----------------------------------------------------

  - Gitee 已定期自动同步 `固件开发仓库 <https://gitee.com/EspressifSystems/esp-rainmaker>`_。如果您需要在 Gitee 拉取 App 源码，请联系 `乐鑫商务 <https://www.espressif.com/zh-hans/contact-us/sales-questions>`_，我们将尽快为您同步。
  - 您可以使用 `esp-gitee-tools <https://gitee.com/EspressifSystems/esp-gitee-tools>`_ 完成 RainMaker 设备固件开发仓库中子模块的拉取。

--------------

CLI 工具如何使用？
-------------------

  - 如果您调试的为公有 ESP RainMaker，可以直接使用 CLI 目录下的 rainmaker.py 脚本。
  - 如果您调试的为私有 ESP RainMaker，需要将 serverconfig.py (cli/rmaker_lib/serverconfig.py) 脚本中的 HOST 替换为您服务器的 URL BASE。

--------------

ESP RainMaker App 执行 Claiming 时出现了错误该如何处理？
--------------------------------------------------------

  Claiming 提示非网络相关的错误时，一般为账户存在问题，例如账户被禁用、申请证书的额度已满。请联系 `乐鑫商务 <https://www.espressif.com/zh-hans/contact-us/sales-questions>`_ 来获取进一步的支持。

--------------

ESP RainMaker 中节点、节点属性、设备、设备属性、服务、参数都是什么？有什么用？
-------------------------------------------------------------------------------

  - 节点 (node)：节点可以类比成一个产品，拥有一个 node id 作为标识符，是 ESP RainMaker 框架中的最小操作单位。
  - 节点属性 (node attribute)：节点属性用来更好地描述与定义节点的功能。
  - 设备 (device)：设备是用户层面可控制的具体实体，如开关、球泡灯、温度传感器、风扇。一个节点下允许挂载多个设备，此时节点将作为虚拟网关使用。
  - 设备属性 (device attribute)：与节点属性类似，这些元数据用来更好地描述与定义设备的功能。
  - 服务 (service)：从结构上与设备一样，主要区别在于服务不需要用户进行可见的操作，如在 OTA 升级中，就存在一些无需用户操作与管理的状态。
  - 参数 (parameter)：参数用来实现设备与服务的功能，如球泡灯的电源状态、亮度、颜色，以及 OTA 过程中的状态更新。  

  上述这些概念可以很好地定义与描述产品的功能，与阿里云、腾讯云在控制台创建的设备模型类似。

--------------

ESP RainMaker 是否支持设备与设备之间的联动？
-----------------------------------------------

  支持，在 ESP RainMaker 中称为自动触发与响应 (Automation Trigger and Actions)，但设置触发的对象为节点与节点而非设备与设备。通过 `addAutomationTriggerAction <https://swaggerapis.rainmaker.espressif.com/#/Automation%20Trigger%20and%20Actions/addAutomationTriggerAction>`_ 进行设置，该功能运行在云端，一旦符合预设的规则便会自动发送响应给目标节点。
  
--------------

ESP RainMaker 是否支持 App 端的消息推送？
-----------------------------------------------

  支持，ESP RainMaker 的消息推送框架基于 GCM (Google Cloud Messaging) 与 APNs (Apple Push Notification service)。在国内建议使用 iOS 手机或装有 Google 服务框架的 Android 手机来测试。

--------------

ESP RainMaker 是否支持带时间戳数据的上报及后续的分析？
-------------------------------------------------------------

  支持，设备支持按时间戳上报数据，云侧支持按时间点过滤并拉取数据。在 ESP RainMaker 中该数据称为时间序列数据 (Time Series data)，使用单独的 MQTT 主题上报，云端以完成集成。通过 `tsdata <https://swaggerapis.rainmaker.espressif.com/#/Time%20Series%20Data/GetTSData>`_ 拉取数据，可参考 ESP RainMaker 仓库中的 `温度传感器例程 <https://github.com/espressif/esp-rainmaker/tree/master/examples/temperature_sensor>`_。

--------------

ESP RainMaker App 与 Nova Home App 可以从哪获取？
-------------------------------------------------------------

  - iOS 手机可以在 App store 中搜索 ESP RainMaker、Nova Home 获取。
  - Android 手机在 Play Store 中搜索 ESP RainMaker、Nova Home 获取。
  - ESP RainMaker App Android 版本源码仓库中附带 apk 文件，请参考 `ESP RainMaker App 发布版本 <https://github.com/espressif/esp-rainmaker-android/releases>`_。

  如果访问上述网站困难，可联系 `乐鑫商务 <https://www.espressif.com/zh-hans/contact-us/sales-questions>`_ 获取最新安装包。

--------------

ESP RainMaker 中节点配置信息有什么用？与参数信息的区别是什么？如何查看？
-------------------------------------------------------------------------

  - 节点配置信息是用来描述节点的一组 JSON 格式的元数据。在 `示例配置 <https://rainmaker.espressif.com/docs/node-cloud-comm.html#appendix-sample-node-configuration>`_ 中，`devices` 描述了每个设备的类型、参数个数及每个参数的属性等。`devices` 的数据类型为 JSON 数组，这代表一个节点下允许存在多个设备，方便实现虚拟网关功能，此处未展示的 `services` 同理。节点配置信息使用单独的 `MQTT 主题 <https://rainmaker.espressif.com/docs/node-cloud-comm.html#mqtt>`_ 上报，设备每次连接到云都应首先上报该消息。
  - 参数信息用来展示设备及服务中参数的值，值的数据类型源自节点配置消息中对该参数数据类型的配置。当云或者设备需要更新参数时，就会对该信息进行更新。通过设备固件开发 SDK 创建参数时，节点配置信息中将同步更新该参数的配置。
  - 可以通过 CLI 工具查看节点配置信息与参数信息，在 CLI 中登录后使用 `getnodeconfig` 命令可获取节点配置信息，使用 `getparams` 可获取参数信息。
 
--------------

ESP RainMaker 中设备最多能上报多大的消息？
---------------------------------------------

  AWS 中 MQTT 一次性最大能接收 128 KB 的数据，ESP RainMaker 中无其他限制。但需要注意的是，AWS 对于 MQTT 消息计费采用条数与大小双重规则，当消息大小每超过 5 KB 时则视为 1 条消息，以此类推，若上报 11 KB 的消息则视为 3 条消息进行计费。具体计费规则请联系 `乐鑫商务 <https://www.espressif.com/zh-hans/contact-us/sales-questions>`_  获取。

--------------

ESP RainMaker App 中显示设备离线总是很慢，能否加快？
-----------------------------------------------------

  设备的离线检测基于 MQTT 心跳包超时时间，默认为 120 s，即最慢能够在 180 s 检测到离线。缩短心跳包发送时间虽然能够更快的检测到设备离线，但会增加消息条数。

--------------

ESP RainMaker 方案适配了哪些芯片？用哪个 IDF 版本编译？是否支持其他平台的芯片？
-------------------------------------------------------------------------------

  - RainMaker 设备固件开发 SDK 目前完成了对 ESP32 系列芯片适配。
  - ESP-IDF 版本需大于 v4.1，若使用 ESP32-C3 需切换到 v4.3 及以上，使用 ESP32-S3 需切换到 v4.4 及以上，使用 ESP32-C2 需切换到 v5.0 及以上。
  - 支持，RainMaker 设备固件开发 SDK 提供 `MQTT 适配层 <https://github.com/espressif/esp-rainmaker-common/tree/473417c053888d4ad89def7d856e75a366f74122>`_，需要您自行完成对接。

--------------

ESP RainMaker 方案中 Claiming 有 3 种形式，区别在哪？该如何选择？能否在私有部署使用中使用？
-------------------------------------------------------------------------------------------

  - 具体区别请查看 `Claiming 实现细节 <https://rainmaker.espressif.com/docs/claiming.html>`_。
  - 对带有蓝牙功能的芯片优先选择 `Self Claiming`，其次为 `Assisted Claiming` （`Self Claiming` 最近已更改为对所有 ESP32 系列芯片开放，并非仅仅适用于 ESP32-S2）。不带蓝牙功能的芯片选择 `Self Claiming`。若 `Assisted Claiming` 与 `Self Claiming` 均无法成功，则选择 `Host Driven Claiming` 或联系 `乐鑫商务 <https://www.espressif.com/zh-hans/contact-us/sales-questions>`_ 处理。
  - 不可使用，详细原因请查看 `为什么 Claiming 无法为私有服务器部署？ <http://customer.rainmaker.espressif.com/docs/faq/#why-doesnt-claiming-work-with-our-deployment>`_。

--------------

ESP RainMaker 支持哪些配网方式？这些配网如何实现？能否修改添加自己的配网逻辑？
---------------------------------------------------------------------------------

  - 目前支持蓝牙配网与 Soft Ap 配网。
  - 配网方案是通过 ESP-IDF 中的 `wifi_provisioning <https://github.com/espressif/esp-idf/tree/release/v4.3/components/wifi_provisioning>`_ 组件实现的。运行 RainMaker 设备固件开发仓库中的例程时，还将打印二维码，二维码中的信息包含该设备支持的配网方式及加密字符串，可以使用 ESP RainMaker App 扫描读取。
  - 可以添加自己的逻辑。需要注意的是，ESP RainMaker 中的配网通常指，设备连接 Wi-Fi 与完成用户绑定，无论如何自定义，都必须包含这两步。

--------------

ESP RainMaker App 在配网时有时会弹出配对选项，如何取消？
---------------------------------------------------------

  在 menuconfig 中将 Component config -> Wi-Fi Provisioning Manager 的下述选项关闭即可。
  
    [ ] Enable BLE bonding
  
    [ ] Enable BLE Secure connection flag
  
    [ ] Force Link Encryption during characteristic Read / Write 

--------------

ESP RainMaker 是否支持本地控制？
-----------------------------------

  支持通过 Wi-Fi 进行局域网下的本地通信，设备发现基于 mDNS 服务，通过 ESP-IDF 中的 `esp_local_ctrl <https://github.com/espressif/esp-idf/tree/release/v4.3/components/esp_local_ctrl>`_ 组件实现，RainMaker 示例均默认开启，可以通过下述方式查询当前网络下已启用本地控制的 ESP RainMaker 设备：
  
  - Windows 平台，请先下载安装 `Bonjour <https://support.apple.com/kb/DL999?locale=zh_CN>`_，随后在命令行中执行 `dns-sd -P _esp_local_ctrl._tcp`。
  - Linux 平台，在命令行中执行 `avahi-browse -r _esp_local_ctrl._tcp`。

  ESP RainMaker App 将实时扫描，并优先使用本地控制进行通信。更多本地控制的细节，请查阅开发指南中的 `本地控制章节 <https://rainmaker.espressif.com/docs/local-control.html>`_。

--------------

使用 ESP RainMaker Topic 方式进行 OTA 时，有时会报 `! The certificate is not correctly signed by the trusted CA`，这该如何处理 ？
----------------------------------------------------------------------------------------------------------------------------------

  请拉取最新的代码，并确认 OTA 时使用的为 `最新的 OTA 服务器证书 <https://github.com/espressif/esp-rainmaker/blob/master/components/esp_rainmaker/server_certs/rmaker_ota_server.crt>`_。如果确定为最新的证书则可尝试下述方案:
  
  1. 获取 OTA 使用的 URL。您可以在云下发给设备的 OTA 消息中找到 URL，格式通常为 `https://esp-rainmaker-ota-xxxx-dev.s3.us-west-1.amazonaws.com/users/xxx/firmwar/xxx/xxxxxxxxxx`。
  2. 查询该链接使用的 OTA 服务器证书。您需要使用 Linux 命令行执行 `openssl s_client -showcerts -verify 5 -connect esp-rainmaker-ota-xxxxx-dev.s3.us-west-1.amazonaws.com:443 < /dev/null`。
  3. 替换证书。如果一切正常，在执行完成第 2 步后，命令行中将打印多个证书，您需要选择并替换您当前使用的证书。

  如果上述方案仍然无法成功，可联系 `乐鑫商务 <https://www.espressif.com/zh-hans/contact-us/sales-questions>`_ 提供进一步解决方案。

--------------

`Swagger <https://swaggerapis.rainmaker.espressif.com/>`_ 上提供的 RESTful API 可以在线调试吗?
----------------------------------------------------------------------------------------------------------

  可以，点击每条 API 右侧的 `Try it out` 按钮即可。需要注意的是，如果 API 带有锁的图标意味着需要 accesstoken 才能执行，您需要先使用 `swaggerapis <https://swaggerapis.rainmaker.espressif.com/>`_ 里的 user login 进行登录，该接口将返回三组 token，随后点击页面上方的 Authorize 将 accesstoken 填入到页面中即可。

--------------

ESP RainMaker App 中的 UI 是如何确定的? 如何自定义呢？
-------------------------------------------------------------------

  - ESP RainMaker App 中所有 UI 的展示是由设备上报的 `node_config` 消息决定的，字段与 UI 的映射关系请查看开发指南中的 `标准参数 <https://rainmaker.espressif.com/docs/standard-types.html>`_ 章节。
  - 可以为每个参数根据数据类型指定不同的标准 UI，不同参数的添加顺序也将决定 App 上的显示顺序。如果需要我们支持更多不同风格的 UI，可联系 `乐鑫商务 <https://www.espressif.com/zh-hans/contact-us/sales-questions>`_ 处理。
