苹果应用
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

----------

iOS 蓝牙设备名称缓存问题如何解决？
------------------------------------------

  以下为 OC 和 Swift 的解决方法：

  OC

  .. code:: text

    (void)centralManager:(CBCentralManager *)central didDiscoverPeripheral:(CBPeripheral *)peripheral 
    advertisementData:(NSDictionary<NSString *,id> *)advertisementData 	RSSI:(NSNumber *)RSSI{
        NSString *localName = [advertisementData objectForKey:@"kCBAdvDataLocalName"];} 

  Swift

  .. code:: text

    func centralManager(_ central: CBCentralManager, didDiscover peripheral: CBPeripheral, 
    advertisementData: [String : Any], rssi RSSI: NSNumber) {
        let localName = advertisementData["kCBAdvDataLocalName"]}

----------

阿里飞燕平台 SDk 为何报错找不到 #import <IMLDeviceCenter/IMLDeviceCenter.h> 头文件？
----------------------------------------------------------------------------------------

  - 请将 ALLOW_NON_MODULAR_INCLUDES_IN_FRAMEWORK_MODULES 设为 YES。

----------

iOS 13.0 及以上版本如何获取 Wi-Fi 信息？
------------------------------------------------

  - 在 .plist 文件中开启定位权限。
  - Xcode 开启 Wi-Fi 权限。
  - Apple 官网申请 Identifiers Access Wi-Fi Information 权限。
  - 手动请求定位权限。
  - 导入系统框架 #import <SystemConfiguration/CaptiveNetwork.h> 获取 Wi-Fi 信息。

----------

iOS 14.0 如何增加本地网络权限？
-------------------------------------------

  - 在 .plist 文件中开启 NSLocalNetworkUsageDescription 权限。

----------

AWS 如何生成 .p12 证书？
----------------------------------------

  openssl pkcs12 -export -in /Users/xxx/Desktop/awscer/73bb87b879-certificate.pem.crt -inkey /Users/xxx/Desktop/awscer/73bb87b879-private.pem.key -CAfile /Users/xxx/Desktop/awscer/AmazonRootCA1.pem -out awsiot-identity.p12

----------

如何获取 AWS SDK 自带的登录注册验证码？
--------------------------------------------

  - 使用邮箱注册的账号在获取验证码时，由于网络原因，需要等待较长时间（大概 2 ～ 4 小时左右）才能收到。
  - 点击获取验证码之后不可重复点击，否则旧验证码将失效。

----------

APP 如何在后台扫描蓝牙（两种方式）？
--------------------------------------------

  - 第一种方式：扫描所有蓝牙设备。

  .. code:: text
  
    [self.cbCentralMgr scanForPeripheralsWithServices:nil options:nil];

  - 第二种方式：扫描指定 serviceUUID 蓝牙设备。

  .. code:: text

    [self.cbCentralMgr scanForPeripheralsWithServices:@[[CBUUID UUIDWithString:@"指定的serviceUUID"]] options:nil];

----------

如何解决 iOS 14.5 UDP 广播 sendto 返回 -1 的错误？
------------------------------------------------------------------------------------

  问题背景：

  - 手机系统升级到 iOS 14.5 之后，UDP 广播发送失败。
  - 项目中老版本使用 socket。
  - 项目中新版本使用 CocoaAsyncSocket。
  - 两种 UDP 发包方式都会报错：No route to host。

  报错具体内容如下：

  .. code:: text

    sendto: -1
    client: sendto fail, but just ignore it
    : No route to host
    
  问题解决：

  由于 192.168.0.255 广播地址只是当前本地地址，App 中需要动态改变前三段 192.168.0 本地地址，解决方法如下：

  .. code:: text

    NSString *localInetAddr4 = [ESP_NetUtil getLocalIPv4];
    NSArray *arr = [localInetAddr4 componentsSeparatedByString:@"."];
    NSString *deviceAddress4 = [NSString stringWithFormat:@"%@.%@.%@.255",arr[0], arr[1], arr[2]];

  发包过滤，只需要过滤地址最后一段是否为 255

  .. code:: text
  
    bool isBroadcast = [targetHostName hasSuffix:@"255"];

----------

如何解决 iPhone11 iOS 14.7 下载安装 App 后，点击图标，App 闪一下就回到了桌面的问题？
--------------------------------------------------------------------------------------------------------------------------

  可以从以下四个方面进行排查：

    - 项目中引入的音频动态库版本太老不兼容
    - 系统 API 在 iOS 15.0 以下版本不兼容
    - Xcode 版本太老
    - 电脑是 M1 芯片

----------

如何解决 iOS 国际化文本格式报错 `read failed: Couldn't parse property list because the input data was in an invalid format` 问题？
----------------------------------------------------------------------------------------------------------------------------------------------------------

  数据格式错误一般会有下面几种情况：

    - 末尾少了分号
    - 字符使用了全角字符（中文字符）
    - 中间少了 =
    - 少了双引号或者引号没有成对出现
    - 文本中出现了不必要的特殊字符

