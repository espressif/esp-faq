HTTP
=====

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

Does ESP8266 support HTTP hosting?
-------------------------------------------------------

  Yes, it does. ESP8266 can run as a server in both SoftAP and Station modes.

  - When running as a server in SoftAP mode, clients can directly access the ESP8266 host or server at 192.168.4.1 (default) IP address.
  - When the server is accessed via a router, the IP address should be the one allocated to the ESP8266 by the router.
  - When using SDK to write native code, please refer to relevant examples.
  - When using AT commands, start a server using ``AT+CIPSERVER`` command.

--------------

How to use ``esp_http_client`` to send chunked data?
-----------------------------------------------------------------------------------

  - Please use `HTTP Stream <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/protocols/esp_http_client.html#http-stream>`_ by setting the  ``write_len`` parameter of ``esp_http_client_open()`` to -1. Then the "Transfer-Encoding" will be set to "chunked" automatically，please see ``http_client_prepare_first_line()`` in　`esp_http_client.c <https://github.com/espressif/esp-idf/blob/master/components/esp_http_client/esp_http_client.c>`_.
  - The code snippet is listed below for your reference：

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

Is there a way to set cookies when ESP32 operates as an HTTP client?
----------------------------------------------------------------------------------------------------------------

  ESP32 itself does not have an API for setting cookies directly, but you can use `esp_http_client_set_header <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/protocols/esp_http_client.html#_CPPv426esp_http_client_set_header24esp_http_client_handle_tPKcPKc>`_ to add cookies to the HTTP header.

----------------

How do I set the maximum number of clients that are allowed for connection when ESP32 serves as an HTTP server? What will happen if the number exceeds the limit?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The maximum number of client connections can be set by configuring ``max_open_sockets`` in the ``httpd_config_t`` structure.
  - If the number of clients exceeds the limit, you can set the ``lru_purge_enable`` parameter in the ``httpd_config_t`` structure to true. In doing so, if there is no socket available (which is determined by max_open_sockets), the least used socket will be cleared to accept the coming one.

----------------

Does ESP32 have an example of implementing a gRPC client over HTTP/2 and above versions?
--------------------------------------------------------------------------------------------------------------------------------

  Not yet.

----------------

How to download a specific segment of a file over HTTP in ESP-IDF (i.e., add ``Range:bytes`` information to the header)?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Please refer to the ``http_partial_download`` function in the `esp http client example <https://github.com/espressif/esp-idf/tree/v4.4.1/examples/protocols/esp_http_client>`_.

----------------

When the ESP module acts as a local HTTP/HTTPS Server, it returns the `Header fields are too long for server to interpret` error if it is accessed by the browser. Why?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - The reason for this problem is that the URL is too long for the browser, and the underlying buffer is not big enough. You can increase the HTTP header length by modifying the menuconfig configuration. You can change the default value, which is 512 bytes, to a larger size, for example, 1024 bytes. The specific steps are as follows:

    - ``idf.py menuconfig`` > ``Component config`` > ``HTTP Server`` > ``(1024)Max HTTP Request Header Length``
    - ``idf.py menuconfig`` > ``Component config`` > ``HTTP Server`` > ``(1024)Max HTTP URI Length``

----------------

How can I resolve the error of `HTTP_HEADER: Buffer length is small to fit all the headers` returned by HTTP request?
--------------------------------------------------------------------------------------------------------------------------------

  - Please change the member ``buffer_size_tx`` of the structure ``esp_http_client_config_t`` in the file `esp-idf/components/esp_http_client/include/esp_http_client.h` to 1024 bytes or larger.

--------------

Why is the data length always 0 when calling ``esp_http_client_read_response`` after executing the ``esp_http_client_perform`` function?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  The ``esp_http_client_perform`` function already handles data reading internally, so calling ``esp_http_client_read_response`` afterward is not necessary and will not yield the expected data length. To obtain the data, please handle the ``HTTP_EVENT_ON_DATA`` event in the event handler.

--------------

What happens when ``esp_http_client_write`` is called after calling ``esp_http_client_open``?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  Calling ``esp_http_client_write`` will immediately send data to the server. Typically, if ``esp_http_client_perform`` is called, the data will be passed to the application layer through ``HTTP_EVENT_ON_DATA`` in the HTTP event. If data is to be obtained using ``esp_http_client_read``, it must go through ``esp_http_client_open->esp_http_client_write->esp_http_client_fetch_headers``, after which``esp_http_client_read`` will contain data.

--------------

How to distinguish whether an HTTP request is sent from WiFi or from the Ethernet in the HTTP request handler?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  In the request handler, you can get the file descriptor (fd) using ``httpd_req_to_sockfd``, then call ``getsockname`` to get the local address. Based on the address, you can determine which network interface card is being used.

--------------

When downloading files via HTTP, occasionally there will be a failure with an error message "couldn’t get hostname". What could be the reason?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  This error is usually due to the failure of sending a DNS request, or WiFi not receiving a DNS response. It is recommended to confirm the problem through packet capture analysis.

--------------

In the event of an HTTP download failure, how to identify the cause?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  First, analyze the logs to determine the cause of the download failure. If it is due to timeout or network disconnection issues, you can confirm whether the TCP stream is normal by capturing packets.

--------------

How to Upload a Grayscale Image via ESP HTTP?
------------------------------------------------------------------------------------------------

  The HTTP "Content-Type" can be modified as follows:
  ::

      esp_http_client_set_header(http_client_cam, "Content-Type", "application/octet-stream");

  Alternatively, you can convert the image to JPEG format locally and continue using ``image/jpeg`` as the "Content-Type". If an ``HTTP 500`` error occurs during upload, verify that the image format is correct and ensure that the server supports this format.

--------------

How does an Espressif device handle HTTPS certificate expiration?
--------------------------------------------------------------------------------------------------

  Certificates are usually updated via OTA. It is recommended to embed the certificates into app.bin, and then update app.bin through an OTA update to refresh the certificates.

--------------

How to resolve stack overflow in the HTTPD task?
----------------------------------------------------------------------------------------------------

  To address this issue, increase the ``stack_size`` in ``HTTPD_DEFAULT_CONFIG``. For details, refer to the `example code <https://github.com/espressif/esp-idf/blob/master/components/esp_http_server/include/esp_http_server.h#L55>`_.

--------------

What specification does ESP-IDF follow for URL encoding in HTTP/HTTPS requests?
----------------------------------------------------------------------------------------------

  The underlying URL encoding in ESP-IDF does not fully comply with the RFC-3986 specification for automatic encoding. Typically, users need to pre-encode the URL before passing it in.

--------------

If the status code of http_data is 200 but the content_length is 0, is this normal?
----------------------------------------------------------------------------------------------

  This situation may be normal, especially when the response uses chunked transfer encoding. In such cases, ``content_length`` may not be the accurate length. Use ``esp_http_client_get_chunk_length`` to obtain the actual length, or handle the data within the callback.

--------------

After running HTTPS for some time, a decrease in minimum heap memory is observed. Could this be a memory leak?
-------------------------------------------------------------------------------------------------------------------

  Not necessarily. If the remaining memory is stable, the behavior may simply indicate higher peak memory usage (e.g., TCP is in the TIME_WAIT state and not released). You can set the ``SO_LINGER`` option to force close the connection and release resources.
