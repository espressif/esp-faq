# 环境搭建

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## idf.py menuconfig 编译报 "Configuring incomplete , errors occured" 的错误信息如何解决呢？

查看 cmake 版本，使用camke --version 进行查看， 如果低于 3.10.0 版本，我们认为是低版本， 建议更新 cmake 版本

- 下载 cmake ：https://cmake.org/download/

- 操作参考链接：http://www.mamicode.com/info-detail-2594302.html


