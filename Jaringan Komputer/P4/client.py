import socket  # Import library socket untuk mengakses fungsi jaringan

HOST = '127.0.0.1'  # Menentukan alamat IP tujuan yang akan dihubungi (localhost)
PORT = 5555  # Menentukan nomor port yang akan digunakan untuk koneksi

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Membuat objek socket dengan alamat IPv4 dan tipe koneksi TCP

sock.connect((HOST, PORT))  # Menghubungkan socket dengan alamat dan port yang telah ditentukan

while True:  # Loop tak terbatas untuk mengirim dan menerima pesan
    message = input("Message: ")  # Membaca pesan dari pengguna
    input()  # Mengabaikan input kosong (sepertinya ini adalah kesalahan)
    sock.send(message.encode('utf-8'))  # Mengirim pesan ke server setelah mengenkripsi dalam format UTF-8

    reply = sock.recv(1024).decode('utf-8')  # Menerima pesan dari server, mendekripsi dari UTF-8, dan menyimpan dalam variabel 'reply'
    print(f"Received: {reply}")  # Mencetak pesan yang diterima dari server
