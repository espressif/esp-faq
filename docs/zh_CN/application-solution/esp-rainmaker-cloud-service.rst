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

  - 目前 ESP RainMaker 通过云云对接的形式完成了对 Alexa App、Google Home App 的支持，通过 `ESP HomeKit SDK <https://github.com/espressif/esp-homekit-sdk>`_ 对接了苹果的 家庭 App。在上述 App 中添加设备后即可使用对应的语音助手完成语音控制。建议使用 `homekit_switch <https://github.com/espressif/esp-rainmaker/tree/master/examples/homekit_switch>`_ 进行测试，该 Demo 将已开关的产品形态出现在上述所有 App 中。
  - Alexa 部分请参考 `Alexa 所支持的语音指令 <https://www.amazon.com/Espressif-Systems-ESP-RainMaker/dp/B0881W7RPV/>`_ 
  - Google Assistant 部分请参考 `Google Assistant 所支持的语音指令 <https://assistant.google.com/services/a/uid/0000001421a84610?hl=en_us&source=web>`_ 
  - Siri 部分请参考 `Siri 所支持的语音指令 <https://support.apple.com/zh-cn/HT208280>`_ 

--------------

RainMaker 设备的证书如何获取？是否有管理后台？
------------------------------------------------

  - 在方案验证阶段，您可以使用 `claiming <https://rainmaker.espressif.com/docs/claiming.html>`_ 服务获取证书，`RainMaker 设备固件开发仓库 <https://github.com/espressif/esp-rainmaker>`_ 中提供的 Demo 都默认启用了该服务。在量产阶段，您必选先完成私有化部署，可以咨询 `乐鑫商务 <https://www.espressif.com/zh-hans/contact-us/sales-questions>`_ 来获取更为详细的批量生成证书指导及部署事宜。
  - 目前 ESP RainMaker 方案提供了一个 `在线网页 <https://dashboard.rainmaker.espressif.com>`_ 查看设备信息，并支持通过该网页下发 OTA 任务及查看 `ESP insight <https://github.com/espressif/esp-insights>`_ 数据。

--------------

ESP RainMaker 固件侧代码开发与腾讯云、阿里云的开发模式有什么不同？
------------------------------------------------------------------

 - 腾讯云、阿里云通常是在控制台创建产品，随后创建设备模型，而 RainMaker 则在设备侧通过 API 创建模型，连接网络后将模型发送给云。
 - 腾讯云、阿里云的连接认证阶段通常有 2 种形式：使用证书/三元组(四元组)或使用动态注册。ESP RainMaker 仅支持证书的形式。
 - RainMaker 设备固件开发 SDK 基于成熟的 ESP-IDF 开发框架，对配网、OTA 升级、本地控制等功能做了整合，进行基本的配置即可使用，您不需要移植其他第三方 SDK，直接编写应用层代码即可，该部分完全开源。
 - RainMaker 云中间件基于 AWS 无服务器计算 (Amazon Serverless Computing) 构建，开发者无需在云中编写任何代码、也无需进行任何配置即可使用，该部分不开源。
 - RainMaker App 提供 iOS 与 Android 两个版本，App 可根据设备上报的配置自动加载 UI 及图标，同时也将完整展示设备的物模型，用户可以直接在 App 上更改这些属性。App 将协助用户完成设备的网络配置、本地发现、创建定时任务，该部分完全开源。

--------------

ESP RainMaker 公有云与 ESP RainMaker 私有云有什么区别？
------------------------------------------------------------------

  - ESP RainMaker 是乐鑫提供的一套连接 AWS 的方案，该方案利用了 AWS 提供的一些云产品实现了设备接入、管理、维护、分析功能，乐鑫针对这个方案提供了 App、固件侧的源代码。同时为了方便您测试体验，我们部署了一套公共服务，任何开发者都可以免费使用，我们称之为 ESP RainMaker 公有云，在没有特别申明的情况下，此页面中的 ESP RainMaker 均代指公有云。
  - 如果您想将 ESP RainMaker 部署在自己的 AWS 账号上，首先您需联系 `乐鑫商务 <https://www.espressif.com/zh-hans/contact-us/sales-questions>`_ 以开放相关服务的访问权限，然后可参考 `ESP RainMaker 部署资料 <http://customer.rainmaker.espressif.com/docs/intro/>`_ 完成私有化部署。在完成私有化部署后您将拥有自己的账户体系，管理后台，同时相关 AWS 服务器运营费用（如果有）也将从您的账户中扣除，此时我们称之为 ESP RainMaker 私有云。

--------------

Nova Home 跟 ESP RainMaker 有什么关系？
--------------------------------------------

  - Nova Home 是一套私有部署的 ESP RainMaker 平台，与公有 ESP RainMaker 独立，账户不互通，是一套面向终端客户评估方案的平台。
  - Nova Home 平台提供专用 Nova Home App，此 App 对 UI、icon 做了相关优化，增加了一些业务侧逻辑，目前以通用固件的形式对接了插座、开关、球泡灯等电工照明产品，提供固件及 App，如您希望接入试用可以联系 `乐鑫商务 <https://www.espressif.com/zh-hans/contact-us/sales-questions>`_ 获取更多详细信息。

--------------

除 Github 外是否有其他途径拉取 ESP RainMaker 源码？
----------------------------------------------------

  - Gitee 已定期自动同步 `固件开发仓库 <https://gitee.com/EspressifSystems/esp-rainmaker>`_。如果您需要在 Gitee 拉取 App 源码请联系 `乐鑫商务 <https://www.espressif.com/zh-hans/contact-us/sales-questions>`_，我们将尽快为您同步。
  - 您可以使用 `esp-gitee-tools <https://gitee.com/EspressifSystems/esp-gitee-tools>`_ 完成 RainMaker 设备固件开发仓库中子模块的拉取。

--------------

CLI 工具如何使用？
-------------------

  - 如果您调试的为公有 ESP RainMaker，可以直接使用 CLI 目录下的 rainmaker.py 脚本。
  - 如果您调试的为私有 ESP RainMaker，需要将 serverconfig.py (cli/rmaker_lib/serverconfig.py) 脚本中的 HOST 的替换为您服务器的 URL BASE。

--------------

ESP RainMaker App 执行 Claiming 时出现了错误该如何处理？
--------------------------------------------------------

  - Claiming 提示非网络相关的错误时一般为账户存在问题，例如账户被禁用、申请证书的额度已满，请联系 `乐鑫商务 <https://www.espressif.com/zh-hans/contact-us/sales-questions>`_ 来获取进一步的支持。

--------------

ESP RainMaker 中节点、节点属性、设备、设备属性、服务、参数都是什么？有什么用？
-------------------------------------------------------------------------------

  - 节点 (node)：节点可以类比成一个产品，拥有一个 node id 作为标识符，是 ESP RainMaker 框架中最小操作单位。
  - 节点属性 (node attribute)：节点属性用来更好的描述与定义节点的功能。
  - 设备 (device)：设备是用户层面可控制的具体实体，如开关、球泡灯、温度传感器、风扇，一个节点下允许挂载多个设备，此时节点将作为虚拟网关使用。
  - 设备属性 (device attribute)：与节点属性类似，这些元数据用来更好的描述与定义设备的功能。
  - 服务 (service)：从结构上与设备一样，主要区别在于服务不需要用户进行可见的操作，如 OTA 升级，它拥有一些状态，这些状态不需要由用户操作与管理。
  - 参数 (parameter)：参数用来实现设备与服务的功能，如球泡灯的电源状态、亮度、颜色，OTA 过程中的状态更新。 

  上述这些概念可以很好的定义与描述产品的功能，与阿里云、腾讯云在控制台创建的设备模型类似。

--------------

ESP RainMaker 是否支持设备与设备之间的联动？
-----------------------------------------------

  - 支持，在 ESP RainMaker 中称为 Automation Trigger and Actions (自动触发与响应)，但设置触发的对象为节点与节点并非设备与设备，通过 `addAutomationTriggerAction <https://swaggerapis.rainmaker.espressif.com/#/Automation%20Trigger%20and%20Actions/addAutomationTriggerAction>`_ 进行设置，该功能运行在云端，一旦符合预设的规则便会自动发送响应给目标节点。

--------------

ESP RainMaker 是否支持 App 端的消息推送？
-----------------------------------------------

  - 支持，ESP RainMaker 的消息推送框架基于 GCM(Google Cloud Messaging) 与 APNs(Apple Push Notification service)。在国内建议使用 iOS 手机或装有 Google 服务框架的 Android 手机来测试。

--------------

ESP RainMaker 是否支持带时间戳数据的上报及后续的分析？
-------------------------------------------------------------

  - 支持，设备支持按时间戳上报数据，云侧支持按时间点过滤并拉取数据。在 ESP RainMaker 中该数据称为 Time Series data （时间序列数据），使用单独的 MQTT 主题上报，云端以完成集成，通过 `tsdata <https://swaggerapis.rainmaker.espressif.com/#/Time%20Series%20Data/GetTSData>`_ 拉取数据，设备固件侧可提供测试代码，请联系 `乐鑫商务 <https://www.espressif.com/zh-hans/contact-us/sales-questions>`_ 获取。

--------------

ESP RainMaker App 与 Nova Home App 可以从哪获取？
-------------------------------------------------------------

  - iOS 手机可以在 App store 中搜索 ESP RainMaker、Nova Home 获取 
  - Android 手机在 Play Store 中搜索 ESP RainMaker、Nova Home 获取
  - ESP RainMaker App Android 版本源码仓库中附带 apk 文件，请参考 `ESP RainMaker App 发布版本 <https://github.com/espressif/esp-rainmaker-android/releases>`_

  如果你访问上述网站困难可联系 `乐鑫商务 <https://www.espressif.com/zh-hans/contact-us/sales-questions>`_ 获取最新安装包。
