# 云平台

## 设备的⽣命周期

- `Q:`
  - 在乐鑫的云平台上，设备的⽣命周期是怎样的？

- `A:`
  - 烧录 master-device-key，出⼚。
  - 到达终端⽤户，使⽤ Airkiss/ESP_TOUCH 让设备联⽹，同时传递随机字符（token，App 产⽣）作为权限标识，设备上⽹之后调⽤ /v1/device/activate，同时把 token 传递给云端。
  - 终端⽤户使⽤ App 并且调⽤ /v1/device/authorize 接⼝（使⽤之前产⽣的随机 token），获得这个设备的所有权（成为 owner，获得对应的 owner key）。
  - 终端⽤户对设备的拥有本质上是对 device key 的拥有，对于每 ⼀个设备的控制，是通过对应的 device key 来操作的。
  - 终端⽤户使⽤ /v1/user/devices 列出拥有的设备以及对应的 device key，然后使⽤对应的 device key 做具体的操作。
  - 终端⽤户是 owner 的权限下，可以调⽤ /v1/device/share 接⼝分享设备给他⼈，对应的⽤户使⽤ /v1/device/authorize 接⼝得到授权。
