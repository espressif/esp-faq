# 功耗

## 休眠方式

- `Q:`
  - 休眠⽅式有哪⼏种？有什么区别？

- `A:`
  - 有 Modem-sleep、Light-sleep 和 Deep-sleep 三种休眠⽅式。
  - Modem-sleep
    - Wi-Fi 协议中规定的 Station Legacy Fast 休眠⽅式，Station 发送 NULL 数据帧通知 AP 休眠或唤醒
    - Station 连接上 AP 之后 ⾃动开启，进 ⼊休眠状态后关闭射频模块，休眠期间保持和 AP 的连接，AP 断开连接后 Modem-sleep 不⼯作
    - ESP32 Modem-sleep 进 ⼊休眠状态后，还可以选择降低 CPU 时钟频率，进 ⼀步降低电流
  - Light-sleep
    - 基于 Modem-sleep 的 Station 休眠 ⽅式
    - 与 Modem-sleep 的不不同之处在于进⼊休眠状态后，不仅关闭 RF 模块，还暂停 CPU 和部分系统时钟退出休眠状态后，CPU 继续运⾏
  - Deep-sleep
    - ⾮ Wi-Fi 协议规定的休眠⽅式
    - 进⼊休眠状态后，关闭除 RTC 模块外的所有其他模块
    - 退出休眠状态后，整个系统重新运⾏（类似于系统重启）
    - 休眠期间不保持到 AP 的连接
