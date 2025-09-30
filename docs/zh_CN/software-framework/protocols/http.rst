HTTP
====

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

ESP8266 ⽀持 HTTP 服务端吗？
-----------------------------------------

  ⽀持。ESP8266 在 SoftAP 和 Station 模式下都可以作服务端。

  - 在 SoftAP 模式下，ESP8266 的服务端 IP 地址是 192.168.4.1。
  - 如果 Station 模式，服务端的 IP 地址为路由器分配给 ESP8266 的 IP。
  - 如果基于 SDK 进行⼆次开发，可参考相关应用示例。
  - 如果使⽤ AT 指令，需使⽤ ``AT+CIPSERVER`` 开启服务端。

--------------

如何使用 ``esp_http_client`` 发送块 (chunked) 数据？
-----------------------------------------------------------------------------------

  - 可以通过 `HTTP Stream <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/protocols/esp_http_client.html#http-stream>`_ 的方式，将 ``esp_http_client_open()`` 的 ``write_len``　参数设置为 -1，代码中会自动将 ``Transfer-Encoding`` 设置为 ``chunked``，参考 `esp_http_client.c <https://github.com/espressif/esp-idf/blob/master/components/esp_http_client/esp_http_client.c>`_ 中的 ``http_client_prepare_first_line()``。
  - 可使用如下代码：

    .. code-block:: c

      static void http_post_chunked_data()
      {
          esp_http_client_config_t config = {
          .url = "http://httpbin.org/post",
          .method = HTTP_METHOD_POST, // This is NOT required. write_len < 0 will force POST anyway
        };
        char buffer[MAX_HTTP_OUTPUT_BUFFER] = {0};
        esp_http_client_handle_t client = esp_http_client_init(&config);

        esp_err_t err = esp_http_client_open(client, -1); // write_len=-1 sets header "Transfer-Encoding: chunked" and method to POST
        if (err != ESP_OK) {
          ESP_LOGE(TAG, "Failed to open HTTP connection: %s", esp_err_to_name(err));
          return;
        }

        // Post some data
        esp_http_client_write(client, "5", 1); // length
        esp_http_client_write(client, "\r\n", 2);
        esp_http_client_write(client, "Hello", 5); // data
        esp_http_client_write(client, "\r\n", 2);
        esp_http_client_write(client, "7", 1); // length
        esp_http_client_write(client, "\r\n", 2);
        esp_http_client_write(client, " World!", 7);  // data
        esp_http_client_write(client, "\r\n", 2);
        esp_http_client_write(client, "0", 1);  // end
        esp_http_client_write(client, "\r\n", 2);
        esp_http_client_write(client, "\r\n", 2);


        // After the POST is complete, you can examine the response as required using:
        int content_length = esp_http_client_fetch_headers(client);
        ESP_LOGI(TAG, "content_length: %d, status_code: %d", content_length, esp_http_client_get_status_code(client));

        int read_len = esp_http_client_read(client, buffer, 1024);
        ESP_LOGI(TAG, "receive %d data from server: %s", read_len, buffer);
        esp_http_client_close(client);
        esp_http_client_cleanup(client);
      }

-----------------------------------------------------------------------------------------------------

ESP32 作为 HTTP 客户端，可以设置 cookie 的方式吗？
----------------------------------------------------------------------------------------------------------------

  ESP32 本身没有直接设置 cookie 的 API，但可以通过 `esp_http_client_set_header <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/protocols/esp_http_client.html#_CPPv426esp_http_client_set_header24esp_http_client_handle_tPKcPKc>`_ 向 HTTP 头里添加 cookie 等头数据的方式来设置 cookie。

----------------

ESP32 作为 HTTP 服务器时，如何设置可同时连接的客户端个数上限？如果客户端连接个数超出上限，会出现怎样的情况？
--------------------------------------------------------------------------------------------------------------------------------

  - 通过配置 ``httpd_config_t`` 结构体里的 ``max_open_sockets`` 即可设置同时连接的客户端最大个数。
  - 如果存在客户端连接个数超出上限的情况，可以把 ``httpd_config_t`` 结构体里的 ``lru_purge_enable`` 参数设置为 true。这个参数设置为 true 的作用是如果没有可用的套接字（这个套接字由 ``max_open_sockets`` 决定)，就会清除最少使用的那个套接字从而接受最新的套接字。

----------------

ESP32 是否有至少在 HTTP/2 上实现 gRPC 客户端的示例？
--------------------------------------------------------------------------------------------------------------------------------

  目前还没有。

----------------

在 ESP-IDF 中，如何通过 HTTP 下载文件里的某一特定段（即在头部添加 ``Range:bytes`` 信息）？
--------------------------------------------------------------------------------------------------------------------------------

  可以参考 `esp http client 示例 <https://github.com/espressif/esp-idf/tree/v4.4.1/examples/protocols/esp_http_client>`_ 里的 ``http_partial_download`` 函数。

----------------

ESP 模块作为本地 HTTP/HTTPS Server，浏览器端访问时会返回 `Header fields are too long for server to interpret` 错误如何解决？
-----------------------------------------------------------------------------------------------------------------------------------

  - 出现这个问题的原因是浏览器端 URL 过长，而底层 buffer 分配的长度不够，这部分可以通过修改 menuconfig 的配置来增大 HTTP 头部长度，默认是 512 字节，可以将其调整为更大的数据，比如 1024 字节，具体操作步骤如下：

    - ``idf.py menuconfig`` > ``Component config`` > ``HTTP Server`` > ``(1024)Max HTTP Request Header Length``
    - ``idf.py menuconfig`` > ``Component config`` > ``HTTP Server`` > ``(1024)Max HTTP URI Length``

----------------

HTTP request 返回 "HTTP_HEADER: Buffer length is small to fit all the headers" 错误如何解决？
--------------------------------------------------------------------------------------------------------------------------------

  - 请将 ``esp-idf/components/esp_http_client/include/esp_http_client.h`` 文件中的 ``esp_http_client_config_t`` 结构体里的成员变量 ``buffer_size_tx`` 调整为 1024 字节或更大。

--------------

执行 ``esp_http_client_perform`` 函数后，为何调用 ``esp_http_client_read_response`` 读取的数据长度总是为 0？
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ``esp_http_client_perform`` 函数已包含数据读取操作，因此在其执行后不应再调用 ``esp_http_client_read_response``。若需获取数据，应在事件处理程序中处理 ``HTTP_EVENT_ON_DATA`` 事件。

--------------

调用 ``esp_http_client_open`` 后，再调用 ``esp_http_client_write`` 会发生什么？
--------------------------------------------------------------------------------------------------------------------------------------------------

  调用 ``esp_http_client_write`` 会立即向服务端发送数据。通常，如果调用了 ``esp_http_client_perform``，数据会在 HTTP 事件中通过 ``HTTP_EVENT_ON_DATA`` 传递给应用层。如果要通过 ``esp_http_client_read`` 获取数据，则必须经过 ``esp_http_client_open->esp_http_client_write->esp_http_client_fetch_headers`` 之后，``esp_http_client_read`` 才有数据。

--------------

如何在 HTTP 请求处理函数里区分请求是从 WiFi 发过来的，还是从以太网口发过来的？
-------------------------------------------------------------------------------------------------------------------------------

  在请求处理程序里通过 ``httpd_req_to_sockfd`` 获取文件描述符 (fd)，然后调用 ``getsockname`` 获取本端地址，从地址判断是哪个网卡。

--------------

通过 HTTP 下载文件时，偶尔会出现失败并报错 "couldn’t get hostname"，是什么原因？
------------------------------------------------------------------------------------------------------------------------------------

  这个错误通常是由于 DNS 请求没有成功发送，或者 WiFi 未能接收到 DNS 响应。建议通过抓包分析来确认问题。

--------------

HTTP 下载失败的情况下，如何确认问题？
------------------------------------------------------------------------------------------------------------------------------

  首先需要根据日志判断下载失败的原因。如果是超时或者连接断开问题，可以通过抓包来确认 TCP 流是否正常。

--------------

如何通过 ESP HTTP 上传灰度图像？
-------------------------------------------------------------------------

  HTTP "Content-Type" 可作如下修改：
  ::

      esp_http_client_set_header(http_client_cam, "Content-Type", "application/octet-stream");

  也可以在本地将图像转换为 JPEG 格式后，继续使用 ``image/jpeg`` 作为 "Content-Type"。如果上传时出现 ``HTTP 500`` 错误，建议检查图像格式是否正确，并确保服务器支持该格式。

--------------

ESP 设备如何管理 HTTPS 证书的过期问题？
----------------------------------------------------------------------------------------------------------------

  通常通过 OTA 更新证书。建议将证书嵌入到 app.bin，然后通过 OTA 更新 app.bin 来更新证书。

--------------

当 HTTPD 任务出现栈溢出时，应如何解决？
----------------------------------------------------------------------------------------------

  可以增大 ``HTTPD_DEFAULT_CONFIG`` 的 ``stack_size`` 来解决此问题。具体参考 `示例代码 <https://github.com/espressif/esp-idf/blob/master/components/esp_http_server/include/esp_http_server.h#L55>`_。

--------------

HTTP/HTTPS 请求时，ESP-IDF 底层的 URL 编码遵循什么规范？
----------------------------------------------------------------------------------------------

  ESP-IDF 的底层 URL 编码没有完全按照 RFC-3986 规范自动编码，通常需要用户事先对 URL 进行编码再传入。

--------------

http_data 的 status code 是 200，但是 content_length 为 0 是否正常？
----------------------------------------------------------------------------------------------

  这种情况可能是正常的，特别是当响应是分块传输编码（chunked transfer encoding）时，``content_length`` 可能不会提供准确的数据长度信息。使用 ``esp_http_client_get_chunk_length`` 获取实际长度，或在回调中处理数据。

--------------

设备运行 https 一段时间后，观察到最小堆内存下降，是否是遇到了内存泄漏？
----------------------------------------------------------------------------------------------

  不一定。若剩余内存稳定，可能只是峰值内存使用增加（如 TCP 处于 TIME_WAIT 状态未释放）。可设置 ``SO_LINGER`` 选项强制关闭连接释放资源。
