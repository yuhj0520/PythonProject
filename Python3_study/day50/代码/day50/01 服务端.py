import socket


server = socket.socket()
server.bind(('127.0.0.1',8080))
server.listen(5)


"""
b'GET / HTTP/1.1\r\n 请求首行
Host: 127.0.0.1:8080\r\n  请求头
Connection: keep-alive\r\n
Upgrade-Insecure-Requests: 1\r\n
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n
Sec-Fetch-Site: none\r\n
Sec-Fetch-Mode: navigate\r\n
Sec-Fetch-User: ?1\r\n
Sec-Fetch-Dest: document\r\n
Accept-Encoding: gzip, deflate, br\r\n
Accept-Language: zh-CN,zh;q=0.9\r\n
Cookie: csrftoken=KYJnVBLPpJxwt09TOmTXzpb5qkFJwHVxVGpi0NxEGIg4z5VUuazZ1O2RMwSisu14\r\n
\r\n
请求体
'

"""

while True:
    conn, addr = server.accept()
    data = conn.recv(1024)
    print(data)  # 二进制数据  bytes类型
    # 构造出符合HTTP协议格式的数据  无需掌握
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    # conn.send(b'<h1>hello baby~</h1>')

    # 读取文件内容再返回
    with open('a.txt','rb') as f:
        conn.send(f.read())
    conn.close()


