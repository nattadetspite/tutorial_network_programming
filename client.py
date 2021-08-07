import socket
import threading

nickname = input("your name: ");

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1",5500))

def receive():
  while True:
    try:
      message = client.recv(1024).decode('ascii');
      if message == 'nickname':
        pass
      else:
        print(message)
    except:
      print('an connect error occured!')
      client.close()
      break;

def write():
  while True:
    try:
      message = f'{nickname}: {input("")}'
      client.send(message.encode('ascii'))

    except:
      print('an write error occured!')

rec_thread = threading.Thread(target=receive)
rec_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
