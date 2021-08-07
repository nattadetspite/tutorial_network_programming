import socket

target = "127.0.0.1"

def portScan(port):
  try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connet((target, port))
    return True
  except:
    return False

for port in range(1,1024):
  print(portScan(port))

# attack
# DDOS
# distributed denial of service
