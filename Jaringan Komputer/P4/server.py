import socket  # Import library socket untuk mengakses fungsi jaringan

HOST = '127.0.0.1'  # Menentukan alamat IP server (localhost)
PORT = 5555  # Menentukan nomor port yang akan digunakan untuk koneksi

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Membuat objek socket dengan alamat IPv4 dan tipe koneksi TCP

sock.bind((HOST, PORT))  # Mengikat socket server ke alamat dan port yang telah ditentukan
sock.listen()  # Mendengarkan koneksi yang masuk

client, address = sock.accept()  # Menerima koneksi dari klien dan mendapatkan informasi klien

while True:  # Loop tak terbatas untuk menerima dan mengirim pesan
    message = client.recv(1024).decode('utf-8')  # Menerima pesan dari klien, mendekripsi dalam format UTF-8, dan menyimpan dalam variabel 'message'
    print(f"Received from {address}: {message}")  # Mencetak pesan yang diterima beserta alamat klien

    reply = input("Reply: ")  # Membaca pesan balasan dari server
    client.send(reply.encode('utf-8'))  # Mengirim pesan balasan ke klien setelah mengenkripsi dalam format UTF-8
