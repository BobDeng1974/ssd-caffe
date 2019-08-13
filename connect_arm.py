import socket
import time
from multiprocessing import Pipe, Process

def connect():
    HOST = "192.168.0.110"
    PORT = 8080

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))

    server.listen(1)
    conn, addr = server.accept()
    print("Connected by ", addr)



def socket_control_arm(object, coordinate):

    while 1:
        print("要抓取物品是%s,它的位置坐标为：" %object)
        print("获取到的X:")
        x = int(coordinate[0])
        print(x)
        print("获取到的Y:")
        y = int(coordinate[1])
        print(y)
        print("获取到的Z:")
        z = int(coordinate[2])
        print(z)
        coordinate_x = ""
        coordinate_y = ""
        coordinate_z = ""
        if x < 108:
            for i in range(x):
                coordinate_x += "0"
            for j in range(y):
                coordinate_y += "0"
            for k in range(z):
                coordinate_z += "0"
            msg = 1
            # input("是否进行抓取？ “是”请输入y ， “否” 请输入“no”。其他输入均为非法，将终止进程。\n")
            if msg == 1:
                conn.sendto(coordinate_x.encode(), addr)
                time.sleep(1)
                conn.sendto('\r'.encode(), addr)
                time.sleep(1)
                print(conn.recv(1024))
                conn.sendto(coordinate_y.encode(), addr)
                time.sleep(1)
                conn.sendto('\r'.encode(), addr)
                time.sleep(1)
                print(conn.recv(1024))
                conn.sendto(coordinate_z.encode(), addr)
                time.sleep(1)
                conn.sendto('\r'.encode(), addr)
                time.sleep(1)
                print(conn.recv(1024))
            elif msg == "no":
                exit_or_not = input("您确定要退出程序吗？退出请输入y，返回请输入其他任意值。\n")
                if exit_or_not == 'y':
                    break
                else:
                    print('您决定继续运行程序。请继续。')
                    continue
            else:
                break
        else:
            print("坐标输入非法，请重新输入。")
            continue

        print(conn.recv(1024))

    server.close()


def udp_server():
    BUFSIZE = 1024
    port = ('172.20.10.11', 6666)
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(port)
    while True:
        name, client_addr = server.recvfrom(BUFSIZE)
        break
    server.close()
    name = str(name, 'utf-8')
    return name


while True:
    connect()
    name = udp_server()
    time.sleep(0.5)
    socket_control_arm('abc', coordinate)


