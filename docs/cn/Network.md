# 硬件

## TCP/UDP 的包⻓

- `Q:`
  - TCP/UDP 的包⻓是多少？

- `A:`
  - 单包数据，TCP 单包 1460 字节，UDP 单包 1472 字节。

## 关闭 TCP 连接资源释放完毕时间

- `Q:`
  - 关闭 TCP 连接后相关的资源最⻓多久可以释放完毕？

- `A:`
  - 20s 或者发送的 linger/send_timeout 超时之后释放资源。

## LwIP 创建 Socket

- `Q:`
  - LwIP 最多能够创建多少个 Socket？

- `A:`
  - 最多 32 个，默认为 10 个。

## ESP32 的 udp_server demo 数据回传时间

- `Q:`
  - 运⾏ ESP32 的 udp_server demo，数据回传时间过⻓，可能是什么原因？

- `A:`
  - 打开休眠后，ESP32 只会在唤醒时收包，由于收包会延迟，导致回复 ACK 延迟。关掉 AMPDU 和休眠测试即可。
