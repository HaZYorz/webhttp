# 学习收获

## Flask路由

### POST请求
- 通过设置方法为POST来接收POST请求
- 可以通过request.form来获取请求数据
- 由于flask不能区分请求内容，需要**content-type**来区分请求内容类型

```http
# 请求包内容示例
Post /submit HTTP/1.1
Host: 127.0.0.1:8080
Content-Type:application/x-www-form-urlencoded

str=hello

```

