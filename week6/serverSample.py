from socket import *
import sys # untuk melakukan exit program dengan sys.exit()

# membuat socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1) # menerima maksimal satu koneksi client

while True:
    print('Ready to serve...')
    
    # menerima koneksi dari client
    connectionSocket, addr = serverSocket.accept()
    
    try:
        # menerima pesan HTTP request dari client
        message = connectionSocket.recv(1024).decode()
        if not message:
            continue
            
        # index.html, hello.html
        # message = /GET /index.html HTTP /1.1
        # mengambil baris /index.html
        message = message.split()[1]
        
        # membuka index.html serta menghilangkan "/"
        filename = message[1:]
        f = open("week6/"+filename, "r")
        outputData = f.read()
        
        # kirim respon HTTP 200 OK ke client
        connectionSocket.send(
            "HTTP/1.1 200 OK\r\n\r\n".encode()
        )
        
        # mengirimkan isi file ke client
        for i in range(0, len(outputData)): 
            connectionSocket.send(outputData[i].encode())
        connectionSocket.send("\r\n".encode())
        
        # menutup koneksi dengan client
        connectionSocket.close()
        
    except IOError:
        # mengirimkan response 404 jika file tidak ada di direktori
        connectionSocket.send(
            "HTTP/1.1 404 Not Found\r\n\r\n".encode()
        )
        connectionSocket.send(
            "<html><body><h1>404 Not Found</h1></body></html>\r\n".encode()
        )
        
        # menutup koneksi dengan client
        connectionSocket.close()

    # menutup server socket setelah selesai melayani satu client
    serverSocket.close()
    sys.exit() # keluar dari program setelah selesai melayani satu client