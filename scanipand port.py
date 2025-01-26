import socket
import subprocess

ip1 = input("Enter ip: ")
start = int(input("Enter start: "))
end = int(input("Enter end: "))



def getliveip(ip1, start, end):
    ipclear = ip1.split('.')
    finalip = ipclear[0] + '.' + ipclear[1] + '.' + ipclear[2] + '.'
    for ip in range(start, end):
        current_ip = finalip + str(ip)
        response = subprocess.call(['ping', current_ip, '-n', '1', '-w', '1'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if response == 0:
            return current_ip
           # print(current_ip)
       

openip=(getliveip(ip1, start, end))

def scanopenport(openip):
     for port in range(75, 90):
        soc_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = soc_connection.connect_ex((openip, port))
        if result == 0:
            print('Port open:', port , 'on', openip)
        soc_connection.close()

print(scanopenport(openip))