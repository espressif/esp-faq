摄像头应用方案
==============

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

ESP32 系列芯片支持哪种类型的摄像头？
---------------------------------------

  - 有关 ESP32、ESP32-S2 和 ESP32-S3 系列支持的摄像头型号，请参阅 `ESP32 Camera Driver <https://github.com/espressif/esp32-camera/blob/master/README.md>`_。
  - 有关 ESP32-P4 系列支持的摄像头型号，请参阅 `espressif-camera-sensors-component <https://github.com/espressif/esp-video-components/tree/master/esp_cam_sensor#espressif-camera-sensors-component>`_。

--------------

摄像头输出图像都有什么格式？
------------------------------

  图像格式主要由摄像头决定，如果某个摄像头支持多个图像格式，如 RGB565、RGB888、YUV422、JPEG 等，需要通过配置摄像头的寄存器来选择输出格式。

--------------

摄像头支持哪些参数调整？
-------------------------

  图像数据传输速度 (PCLK)、摄像头输出格式、分辨率、输出图像大小、白平衡、GAMMA 校正等摄像头自带的图像模式参数调整。

--------------

摄像头中 MCLK 和 PCLK 的关系是什么，两者有何区别？
------------------------------------------------------------

  - MCLK 是整个摄像头系统的主时钟，控制着整个系统的同步和频率。在摄像头芯片内部，MCLK 用于控制各个模块的时序，例如预处理器、数字信号处理器、像素数组和数据输出接口等。通常情况下，MCLK 的频率由主控芯片的系统时钟和摄像头内部的分频器共同决定，常见的频率有 6 MHz、12 MHz、24 MHz、48 MHz 等。
  - PCLK 是用来控制像素输出的时钟信号。在摄像头输出图像时，每个像素的输出都需要一个时序信号，PCLK 就是用来控制这个时序的信号。具体来说，PCLK 的上升沿表示一个像素的数据已经输出，下降沿表示下一个像素的数据即将输出，这样就形成了一个像素数据的序列。
  - MCLK 在摄像头内经过倍频/分频（根据摄像头配置决定）后得到 PCLK。通常情况下，PCLK 的频率是 MCLK 的一半或一半的整数倍，例如在 24 MHz 的 MCLK 下，PCLK 的频率可以为 12 MHz、6 MHz 等。

--------------

摄像头的 PCLK 是不是越高越好？
------------------------------

  - 理论上，PCLK 速度越高，数据传输越快，但实际使用中，PCLK 越高也意味着对芯片的处理速度要求越高。
  - 当前 ESP32 和 ESP32-S2 芯片并口通信是通过 I2S 接口实现的，过高的 PCLK 会导致并口数据无法同步，出现图像抖动甚至花屏的现象。
  - ESP32-S3 使用独立的 LCD—CAM 接口，可以支持更高的 PCLK 频率。

   - ESP32 的 PCLK 上限为 8 MHz。
   - ESP32-S2 的 PCLK 上限为 32 MHz。
   - ESP32-S3 的 PCLK 上限为 40 MHz。

--------------

ESP32 系列芯片支持 MIPI 接口吗？
--------------------------------

  - ESP32-P4 支持 MIPI 接口。

--------------

ESP32 系列芯片支持 USB2.0 接口吗？
----------------------------------

  - ESP32-S2 和 ESP32-S3 支持 USB2.0 全速接口（12 Mbps）。此外，ESP32-P4 还支持 USB2.0 高速接口（480 Mbps）。

--------------

摄像头中 YUV/RGB 的传输速度为何会比 JPEG 慢？
---------------------------------------------

  - 因为 YUV/RGB 数据量比 JPEG 的数据量大。
  - 例如：对于 320 × 240 的屏幕尺寸，YUV422 的输出为 153.6 K，而 JPEG 压缩后仅需约 10 K。

--------------

摄像头应用中，有哪些影响帧率的因素？
--------------------------------------

  在摄像头应用中，影响帧率的因素主要包括：

  - 分辨率：分辨率越高，每帧需要采集和传输的像素数据就越多，因此帧率就会下降。
  - 图像格式：常见的图像格式包括 RGB565、RGB888、YUV422、JPEG 等，不同的图像格式在图像质量和数据压缩方面存在差异，这些差异会直接影响帧率。
  - 图像处理：如果需要对每帧图像进行处理，如降噪、增强、压缩等操作，会占用更多的处理时间，降低帧率。
  - 传输带宽：传输带宽越窄，每帧需要传输的数据就越少，因此帧率就会下降。
  - 处理器性能：处理器性能越低，每帧需要处理的数据量就越难以承受，因此帧率就会下降。

  因此，在摄像头应用中，需要根据具体的应用场景和需求，权衡这些因素，以达到最佳的帧率和图像质量。

--------------

摄像头运行失败如何排查？
------------------------

  - 无法识别摄像头型号：

   - 检查管脚是否对应正确，重点关注 XCLK、SIOC、SIOD。
   - XCLK 输入的时钟频率太低或摄像头供电不正常，导致摄像头无法正常运行。
   - SIOC 和 SIOD 上挂载太多设备，导致轮询读到率先返回的地址 ID 不是摄像头而是其他设备。此情况建议固定摄像头 ID，以去除轮询步骤。

  - 摄像头识别到了型号，没有图像显示：

   - 检查摄像头数据管脚是否有信号，MCLK 是否正常输入。
   - 摄像头寄存器参数配置正确。

  - 摄像头图像显示不正常：

   - 检查代码，查看输出格式是 RGB、YUV 还是 JPEG，是否符合接收端需要的格式。
   - 尝试降低 PCLK 频率。

--------------

ESP32 支持传输视频流吗？
--------------------------------

  - 视频流的传输操作分为二进制传输和视频流编解码。

   - 二进制传输：ESP32 支持二进制传输，此处是否支持取决于传输的网络带宽。目前 ESP32 TCP 的带宽为 20 MB/s，请参考 `Wi-Fi 测试数据 <https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/wifi.html#id52>`_。
   - 视频流编解码：ESP32 暂不支持视频流编解码。

--------------

ESP-EYE 的出厂固件在哪里？
------------------------------------------------------------------------

  请参考 `ESP-EYE 的出厂固件 <https://github.com/espressif/esp-who/tree/master/default_bin>`_。

--------------

Camera 方案相关的示例存放在哪里？
------------------------------------------------------------------------

  - 请参考 `ESP-WHO <https://github.com/espressif/esp-who>`_。
  - 请参考 `esp-iot-solution <https://github.com/espressif/esp-iot-solution/tree/master/examples/camera>`_。
  - 请参考 `esp-dev-kits <https://github.com/espressif/esp-dev-kits>`_。
  - 要查看 ESP32-P4 系列的常用示例，请前往 `esp-video/examples <https://github.com/espressif/esp-video-components/tree/master/esp_video/examples>`_。
  - 有关 ESP32-P4 系列与 LCD 屏幕结合使用的示例，请前往 `esp-iot-solution/examples/camera/video_lcd_display <https://github.com/espressif/esp-iot-solution/tree/master/examples/camera/video_lcd_display>`_。

--------------

ESP32 支持 12 位 DVP 接口的摄像头吗？
-----------------------------------------------------------------

  不支持，目前驱动只支持 8 位的 DVP 接口。

-----------------

ESP32 是否支持使用不带 JEPG 编码的摄像头来获取 JPEG 图像？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  如果摄像头本身不支持 JPEG 编码，可以参考我们提供的 `esp-iot-solution/examples/camera/pic_server <https://github.com/espressif/esp-iot-solution/tree/master/examples/camera/pic_server>`_ 例程，在 ESP32 设备上实现软件 JPEG 编码。该方法通过软件对 YUV422 或 RGB565 数据进行编码，得到 JPEG 图像。

--------------

ESP-EYE 上的 200 万像素的 OV2640 摄像头是否可以改成只输出 30 万像素的图片？
------------------------------------------------------------------------------------------------------------------

  可以, 在初始化时通过配置 `frame_size <https://github.com/espressif/esp32-camera/blob/master/driver/include/sensor.h#L110>`_ 的值来指定摄像头要输出的分辨率大小。

--------------

ESP32 支持全局快门的摄像头吗？
-----------------------------------------------------------------

  支持，目前支持的摄像头型号为 SC031GS、SC132GS，其他摄像头需要额外增加驱动支持。

--------------

ESP32 使用 DVP 摄像头通过 RTSP 传输 1080P 的视频可以达到多少帧？
------------------------------------------------------------------------------------------------------------------

  暂未测试 1080P 的情况。目前 720P 可以达到 20 FPS.

--------------

ESP32-S3 只支持 MJPEG 编码，但在实现 rtsp/rtmp 推流的时候需要支持 H264/H265 格式的编码，请问是否有支持 H264/H265 格式的编码？
----------------------------------------------------------------------------------------------------------------------------------------------------------------

  目前 ESP32-S3 不支持硬件加速的 H.264/H.265 编码。但是，可以使用软件编码器，例如 FFmpeg 库和 x264/x265 库，将从 OV2640 采集到的 MJPEG 帧转换为 H.264/H.265 编码帧。转换的性能取决于处理器性能，可能会影响帧率。

--------------

ESP32/ESP32-S3 是否有适配支持广角的摄像头？
-----------------------------------------------------------------

  有适配，可以参考 BF3005、OV5640 这两款摄像头。

--------------

ESP32-S2 从上电到显示摄像头图像需要 5 秒，是否有改善的空间？
-----------------------------------------------------------------

  有改善的空间，参考如下：

  - 尝试去掉 ``esp_camera_init()`` 里的一些延时函数。
  - 更改 ``menuconfig`` > ``component config`` > ``camera configuration`` 里的 sccb 的时钟频率为 400000。

--------------

ESP32 可以直接给 GC0308 摄像头提供 24 MHz 频率吗？
------------------------------------------------------------------------

  恐怕不行。经测试，ESP32 提供给 GC0308 的 XCLK 最大的稳定测试值为 20 MHz。

--------------

ESP32/ESP32-S3 是否支持 MMS 串流协议？
-----------------------------------------------------------------

  ESP32 和 ESP32-S3 本身并不直接支持 MMS 协议。MMS (Microsoft Media Server) 是一种由微软开发的流媒体传输协议，主要用于 Windows Media Player 的网络流媒体播放。ESP32 和 ESP32-S3 支持的流媒体协议有 RTSP 和 SIP。如果需要将 ESP32 或 ESP32-S3 用于支持 MMS 协议的场景，可以考虑使用支持 MMS 协议的中间件或转换器。

--------------

使用 ESP32-S3 调试 GC2145 摄像头时，发现支持的最大分辨率为 1024x768，若是调至更大的分辨率，如 1280x720，会提示 cam_hal: EV-EOF-OVF 错误，有什么解决方法？
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  这种情况下，需要降低 GC2145 的 PCLK。可以尝试配置更小的 XCLK，以及调试该摄像头的 PLL 时钟系数。

--------------

ESP32-S3 是否支持 GB28181 协议？
----------------------------------------------------------------------------

  ESP32-S3 本身不直接支持 GB28181 协议，但可以通过将 ESP32-S3 与外部电路和软件结合来实现该协议的支持。因为 GB28181 是一种视频监控设备之间的通信协议，可以使用 ESP32-S3 的网络功能和外部电路，例如视频编码器、音频编解码器和传感器，来实现 GB28181 的功能。同时需要进行相关的软件开发，以实现 GB28181 协议的解析和数据传输。

--------------

ESP32/ESP32-S2/ESP32-S3 是否有通过摄像头识别二维码的参考？
----------------------------------------------------------------------------

  有，可以参考 ESP-WHO 里的 `code recognition <https://github.com/espressif/esp-who/tree/master/examples/code_recognition>`_。

--------------

想为 OV5640 传感器添加 SD 卡接口和摄像头接口，但发现 ESP32 中不同外设的一些管脚存在冲突，请提供摄像头接口和 SD 卡接口的管脚。
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  `ESP-WROVER-KIT 开发板 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/esp32/get-started-wrover-kit-v3.html>`__ 中有 Camera 和 SD 卡电路，可以参考 `ESP-WROVER-KIT V3 入门指南的管脚配置 <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/esp32/get-started-wrover-kit-v3.html>`__。

--------------

当前适配的摄像头传感器没有适合我的需求的，能否增加一个指定型号的摄像头驱动？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  可以。请先通过 `技术支持 <https://www.espressif.com/en/contact-us/technical-inquiries>`__ 渠道与乐鑫的工程师确认需求，选定摄像头传感器的型号后，我们将为您提供对应的摄像头传感器的驱动程序。

--------------

如何增加一个自定义的分辨率？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  假设您需要的分辨率为 640x240，可以通过下述两种方法使用自定义分辨率：
  - 配置 sensor 工作在典型的分辨率 640x480 上，然后只使用其中的上半部分数据 (640x240)。
  - 在 `esp32-camera/driver/include/sensor.h <https://github.com/espressif/esp32-camera/blob/master/driver/include/sensor.h#L92>`__ 中增加标识 FRAMESIZE_640*240，然后在 `esp32-camera/driver/sensor.c <https://github.com/espressif/esp32-camera/blob/master/driver/sensor.c#L31>`__ 中增加该分辨率的长度与宽度的定义 {640, 240，ASPECT_RATIO_16X9}。这种方式需要 sensor 的驱动支持自定义分辨率才能正常工作。


--------------

如何修改摄像头传感器的寄存器配置？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  假设您需要更改 OV5640 传感器的寄存器配置，可以通过下述两种方法实现：
  - 直接在 esp32-camera/sensors/ov5640.c 的 reset() 函数中使用 write_reg() 配置相关的寄存器。
  - 在应用层通过 set_reg() 函数配置相关的寄存器：

  .. code-block:: c

    //初始化摄像头
    esp_err_t ret = esp_camera_init(&camera_config);
    sensor_t *s = esp_camera_sensor_get();
    s->set_reg(s, 0xFFFA, 0xFF, 0xA1);

--------------

esp32-camera 中触发 "cam_hal: EV-VSYNC-OVF" 是什么原因？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  这是传感器触发的帧同步信号过快导致的问题。可以按照下面的步骤进行排查：
  - 运行 `esp-iot-solution/examples/camera/pic_server <https://github.com/espressif/esp-iot-solution/tree/master/examples/camera/pic_server>`_ 示例。如果该示例能够正常运行，则说明该问题不是硬件问题。
  - 检查初始化传感器时指定的 XCLK 和分辨率的大小。分辨率变小或是 XCLK 变大，均可能导致传感器触发的帧同步信号过快。请注意，传感器使用的 XCLK 应该和当前指定的分辨率大小匹配。

-------------------

基于 ESP32-S3 的 Camera 应用出现如下警告日志，是什么原因？
------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: c

    W (7232) cam_haL:FB-OVF
    W (7242) cam_haL:FB-OVF
    W (7492) cam_haL:FB-OVF
    W (7512) cam_haL:FB-OVF
    W (7762) cam_haL:FB-OVF
    W (7772) cam_haL:FB-OVF
    W (8022) cam_haL:FB-OVF
    W (8042) cam_haL:FB-OVF

  如上警告日志代表帧 buffer 溢出，可能是由于帧率太快导致，可以尝试降低 XCLK（注意 ESP32S3 的 XCLK 默认从 80 MHz 的时钟上分频得到，因此 XCLK 的大小必须可以被 80 MHz 整除）。
  特别地，如果 sensor 在 JPEG 模式工作，可以尝试在 menuconfig 中增大 `Custom JPEG mode frame size (bytes)` 选项的值来增大 jpeg recv buffer 的大小。

-------------------

ESP32-Camera 的两种 capture 模式的区别是什么？
------------------------------------------------------------------------------------------------------------------------------

  Camera sensor 在初始化后将图像数据推送到 ESP32 的接收器上。

  - 当配置的接收模式为 CAMERA_GRAB_WHEN_EMPTY 时，只要有空闲的 frame_buffer，后台的驱动程序就将图像数据写入到 frame_buffer 中。当所有的 frame_buffer 用尽时，Camera sensor 推送的新的图像数据将因为没有可用的 frame_buffer 而被迫地丢弃。
  - 当配置的接收模式为 CAMERA_GRAB_LATEST 时，应用层能获取的 frame_buffer 的个数是 fb_count - 1，这是因为后台的驱动程序会占用一个 frame_buffer，并且尝试刷新最新的数据到这个 frame_buffer 中。

  注意，拍摄的行为并不是发生在调用 "esp_camera_fb_get" 时。拍摄的动作是持续进行的，我们只能控制后台使用的 frame_buffer 来获取新的数据，因此如果想要立即获取一个新的图像，可以尝试执行下面的代码：

  .. code-block:: c

    //向后台驱动程序返回一个 frame_buffer
    esp_err_t ret = esp_camera_fb_return(esp_camera_fb_get());
    //后台程序自动将新的图像数据刷新到 frame_buffer，然后应用层可以获取到 frame_buffer 中的数据
    fb = esp_camera_fb_get();

-------------

基于 `esp32-camera <https://github.com/espressif/esp32-camera>`_ SDK 如何实现跳帧？
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  可使用 `esp_camera_fb_return(esp_camera_fb_get());` 舍弃当前帧，即跳过当前获取的旧帧。

-------------

ESP32-S3 能否接两路摄像头并分屏显示？  
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ESP32-S3 可以接两个 SPI 接口的摄像头（分辨率比较小，240*320）。DVP 接口的话，无法同时使用多摄像头，ESP32-P4 更适合。

-------------

ESP32-S3 是否支持 10 位 DVP 摄像头？  
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  通常 10 bit DVP 摄像头可以允许仅接收其高 8 bit，仍旧可以获取正常图像。
