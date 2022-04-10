import socket
import re

from http import HTTPStatus


with socket.socket() as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind(('127.0.0.1', 5000))
    s.listen(1)

    while True:
        conn, addr = s.accept()

        recv_bytes = conn.recv(1024)
        text = recv_bytes.decode('utf-8')
        split = text.split('\r\n')
        print(f'Message received\n"{recv_bytes}"')

        try:
            status_code = re.search(r'\?status=(\d+)', split[0]).group(1)
            status_name = HTTPStatus(int(status_code)).name
        except:
            print('Status code not exist')
            status_code = '200'
            status_name = HTTPStatus(int(status_code)).name
        status_line = 'HTTP/1.1 ' + status_code + ' ' + status_name

        headers = '\r\n'.join([
            status_line,
            'Content-Type: text/html; charset=UTF-8'
        ])
        body = 'Request method: ' + split[0].split(' ')[0] + '<br>Request Source: ' + str(addr) + '<br>'
        body += 'Response Status: ' + status_code + ' ' + status_name + '<br>' + '<br>'.join(split)
        resp = '\r\n\r\n'.join([
            headers,
            body
        ])
        if resp:
            print('sending data back to the client')
            conn.send(resp.encode('utf-8'))
        else:
            print(f'no data from {addr}')
            break
        conn.close()
