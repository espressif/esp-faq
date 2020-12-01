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

iOS 蓝牙设备名称缓存问题
--------------------------------

  下面给出OC 和 Swift 的解决方法：

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

阿里飞燕平台 SDk 报错找不到 #import <IMLDeviceCenter/IMLDeviceCenter.h> 头文件
----------------------------------------------------------------------------------------

  - 把 ALLOW_NON_MODULAR_INCLUDES_IN_FRAMEWORK_MODULES 设为 YES  

----------

iOS 13.0 及以上版本 Wi-Fi 信息获取
----------------------------------------

  - 在 .plist 文件开启定位权限
  - Xcode 开启 Wi-Fi 权限
  - apple 官网申请 Identifiers Access Wi-Fi Information 权限
  - 手动请求定位权限
  - 导入系统框架 #import <SystemConfiguration/CaptiveNetwork.h> 获取 Wi-Fi 信息

----------

iOS 14.0 增加本地网络权限
----------------------------------------

  - 在 .plist 文件开启 NSLocalNetworkUsageDescription 权限

----------

AWS 生成 .p12 证书命令
----------------------------------------

  openssl pkcs12 -export -in /Users/xxx/Desktop/awscer/73bb87b879-certificate.pem.crt -inkey /Users/xxx/Desktop/awscer/73bb87b879-private.pem.key -CAfile /Users/xxx/Desktop/awscer/AmazonRootCA1.pem -out awsiot-identity.p12

----------

AWS SDK 自带登录注册验证码获取
----------------------------------------

  - 使用邮箱注册的账号在获取验证码时，由于网络原因需要等待较长时间才能收到（大概 2 ～ 4 小时左右）
  - 点击获取验证码之后不可重复点击，如有误操作旧验证码将失效
