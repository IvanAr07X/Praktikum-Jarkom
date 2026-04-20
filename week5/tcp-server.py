from socket import * # import all
serverPort = 12000 # port number untuk server
serverSocket = socket(AF_INET, SOCK_STREAM) # membuat sebuah socket TCP

# bind socket ke port
serverSocket.bind(
    ('', serverPort)
)

# server siap menerima koneksi
serverSocket.listen(1)
print("[SYSTEM] server TCP siap digunakan")

running = True
while running:
    # menyetujui koneksi dari client
    connectionSocket, addr = serverSocket.accept()

    while True:
        # pesan yang diterima dari client berupa bytes yang akan decode
        message = connectionSocket.recv(2048).decode()

        # cek apakah "exit"
        if message.lower() == "exit":
            print("[SYSTEM] client ingin keluar")
            running = False
            break
        
        # mengubah pesan menjadi kapital
        modifiedMessage = message.upper()
        print("[SERVER] diterima: ", modifiedMessage)

        # mengirim pesan kembali ke client
        connectionSocket.send(
            modifiedMessage.encode()
        )
    
    # menutup koneksi dengan client
    connectionSocket.close()

# menutup socket server
serverSocket.close()