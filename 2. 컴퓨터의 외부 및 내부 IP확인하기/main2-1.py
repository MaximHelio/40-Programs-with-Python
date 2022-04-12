# 컴퓨터가 연결된 접속정보를 받아올 때 사용하는 모듈을 불러옴
import socket

# 연결된 소켓의 이름을 가져와 in_addr 변수와 바인딩
in_addr = socket.gethostbyname(socket.gethostname())

# in_addr을 출력하여 내부 IP를 확인 
# 이 방법의 경우, 가상 환경 등을 사용하여 여러 개의 환경이 있을 경우, 다른 환경의 IP가 출력될 수 있음.
# 정확한 IP를 알 수 없을 수도 있음
print(in_addr)