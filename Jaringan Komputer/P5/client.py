import socket
import os

# Tentukan parameter-parameter server
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 6000
BUFFER_SIZE = 4096

# Fungsi untuk menerima file dari server
def receive_file(conn, filename):
    with open(filename, "wb") as f:
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            f.write(data)
    conn.close()

# Fungsi utama
def main():
    # Membuat socket klien
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print(f"[*] Terhubung ke {SERVER_HOST}:{SERVER_PORT}")

    # Mengirimkan nama file ke server
    filename = input("[+] Masukkan nama file: ")
    client_socket.send(filename.encode())

    # Menerima respons dari server
    response = client_socket.recv(BUFFER_SIZE).decode()

    if response == "OK":
        # Menerima ukuran file dari server
        filesize = int(client_socket.recv(BUFFER_SIZE).decode())
        print(f"[-] Ukuran file: {filesize} byte.")
        client_socket.send(b"OK")

        # Menerima file dari server
        receive_file(client_socket, filename)
        print(f"[-] {filename} diterima dengan sukses.")
    else:
        print(f"[!] {filename} tidak ada di server.")

    # Menutup koneksi
    client_socket.close()

if __name__ == "__main__":
    main()