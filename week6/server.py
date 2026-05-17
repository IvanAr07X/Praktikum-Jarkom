from socket import *
import threading # membuat thread untuk menangani banyak client

def handle_client(connectionSocket):
    try:
        # menerima pesan user
        message = connectionSocket.recv(1024).decode()

        # jika pesan user tidak kosong
        if not message:
            connectionSocket.close()
            return

        # index.html, hello.html
        # message = /GET /index.html HTTP /1.1
        # mengambil baris /index.html
        message = message.split()[1]
        
        # membuka index.html serta menghilangkan "/"
        filename = message[1:]
        f = open("week6/"+filename, "r")
        outputData = f.read()
        
        # kirim respon
        connectionSocket.send(
            "HTTP/1.1 200 OK\r\n\r\n".encode()
        )

        # kirim data
        connectionSocket.sendall(outputData.encode())

        # tutup koneksi
        connectionSocket.close()

    except IOError:
        # kirim respon bila tidak ditemukan
        connectionSocket.send(
            "HTTP/1.1 404 Not Found\r\n\r\n".encode()
        )

        # kirim data 404
        connectionSocket.send(
            "<html><body><h1>404 Not Found</h1></body></html>".encode()
        )

        # tutup koneksi
        connectionSocket.close()

# membuat socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(5) # dapat menerima sebanyak lima client
print("[SYSTEM] server is running....")

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"[SYSTEM] client {addr} is connected")
    
    # membuat thread dan target thread, beserta parameternya
    thread = threading.Thread(
        target=handle_client,
        args=(connectionSocket,)
    )
    # menjalankan
    thread.start()