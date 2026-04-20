# SOCKET = penjumlahan, pengurangan, perkalian, pembagian
from socket import * # import all

serverName = 'localhost' # IP address untuk server
serverPort = 12000 # port number untuk server

# membuat sebuah socket TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# menghubungkan socket ke server
clientSocket.connect(
    (serverName, serverPort)
)

print("[SYSTEM] masukkan pesan")

running = True
while running:
    # membaca input dari user
    message = input("> ")
    # mengirim pesan ke server
    # encode() digunakan untuk mengubah string menjadi bytes
    clientSocket.send(message.encode())

    # kalau exit = socket ditutup
    if message.lower() == "exit":
        print("[SYSTEM] keluar dari program")
        running = False
        break

    # menerima pesan dari server
    modifiedMessage = clientSocket.recv(2048) # 2048 = buffer size

    print("[SERVER] pesan: ", modifiedMessage.decode()) # decode() digunakan untuk mengubah bytes menjadi string

# menutup socket
clientSocket.close()
print("[SYSTEM] socket ditutup")