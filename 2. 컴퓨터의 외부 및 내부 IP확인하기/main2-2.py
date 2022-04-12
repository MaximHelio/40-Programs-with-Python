# socket으로 외부 사이트에 접속하고, 접속된 정보를 바탕으로 IP를 확인할 수 있음
# 조금 더 정확하게 내부 IP를 확인하는 방법

import socket

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443))

print(in_addr.getsockname()[0])
