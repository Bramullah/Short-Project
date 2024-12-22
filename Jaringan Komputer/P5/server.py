import socket
import threading
import os

# Tentukan konstanta-konstanta terkait server
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 6000
BUFFER_SIZE = 4096

# Fungsi untuk mengirimkan file ke klien yang terhubung
def send_file(conn, addr, filename):
    # Dapatkan ukuran file
    filesize = os.path.getsize(filename)
    # Kirim ukuran file ke klien
    conn.send(str(filesize).encode())
    # Terima respons dari klien
    response = conn.recv(BUFFER_SIZE)

    # Jika klien mengakui (mengirimkan "OK"), mulai mengirimkan file
    if response == b"OK":
        with open(filename, "rb") as f:
            data = f.read(BUFFER_SIZE)
            # Kirim data file dalam potongan-potongan hingga seluruh file terkirim
            while data:
                conn.send(data)
                data = f.read(BUFFER_SIZE)
        # Tutup koneksi setelah mengirimkan file
        conn.close()

# Fungsi untuk menunggu koneksi masuk dari klien
def wait_for_connection(server_socket):
    while True:
        # Terima koneksi baru
        conn, addr = server_socket.accept()
        print(f"[+] {addr[0]}:{addr[1]} terhubung.")

        # Terima nama file yang diminta oleh klien
        filename = conn.recv(BUFFER_SIZE).decode()
        print(f"[-] {filename} diminta oleh {addr[0]}:{addr[1]}.")

        # Jika file yang diminta ada, kirim sinyal "OK" ke klien dan mulai kirim file
        if os.path.exists(filename):
            conn.send(b"OK")
            t = threading.Thread(target=send_file, args=(conn, addr, filename))
            t.start()
        # Jika file tidak ditemukan, kirim sinyal "ERR" ke klien dan tutup koneksi
        else:
            conn.send(b"ERR")
            conn.close()

# Fungsi utama untuk menjalankan server
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(5)
    print(f"[*] Mendengarkan di {SERVER_HOST}:{SERVER_PORT}")
    
    # Panggil fungsi untuk menunggu koneksi masuk
    wait_for_connection(server_socket)

# Jalankan program jika ini adalah file utama yang dieksekusi
if __name__ == "__main__":
    main()