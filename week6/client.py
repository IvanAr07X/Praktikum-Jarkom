import sys
from socket import *

# Memastikan argumen yang dimasukkan di terminal sesuai format
if len(sys.argv) != 4:
    print(
        "Penggunaan: python client.py <server_host> <server_port> <filename>"
    )
    sys.exit()

server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]

clientSocket = socket(AF_INET, SOCK_STREAM)

try:
    # Membuka koneksi TCP ke server
    clientSocket.connect((server_host, server_port))
    
    # Membuat format pesan HTTP GET request
    request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
    clientSocket.send(request.encode())
    
    # Menerima respons dari server
    response = ""
    while True:
        recv_data = clientSocket.recv(1024).decode()
        if not recv_data:
            break
        response += recv_data
        
    print("===== Balasan dari Server =====")
    print(response)
    
except Exception as e:
    print(f"Koneksi gagal: {e}")
finally:
    clientSocket.close() # Menutup koneksi dengan server