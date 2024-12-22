import socket #Mengimpor modul python yang menyediakan kemampuan komunikasi jaringan

#Tabel dns sederhana untuk mencari nama domain dan mendapatkan alamat IP yang sesuai
DNS_TABLE = {
    'www.google.com': '142.250.188.14', #'192.168.1.1', adalah rentang IP Private untuk jaringan internal (cth: wifi)
    'www.twitter.com': '104.244.42.1', #'104.244.42.129', '192.168.1.2', 
    'www.yahoo.com': '74.6.231.21' #'192.168.1.3'
}

#Mengikat soket ke alamat 'localhost' pada port 53 (Port standar untuk server DNS)
server_socket = socket.socket (socket.AF_INET, socket. SOCK_DGRAM)
server_socket.bind(('localhost', 53)) # Domain Name System (DNS)

print('DNS Telah terhubung...') #Mencetak pesan pada konsol

#Memulai perulangan tak terbatas yang dimana server akan terus berjalan dan menangani permintaan DNS yang masuk
while True: 
    #Menerima data (permintaan DNS) dari klien dan menyimpannya dalam variable 'data', juga menangkap alamat klien dan menyimpannya dalam variabel 'address'
    data, address = server_socket.recvfrom (1024) #Ukuran Max-1024 byte
    domain_name = data.decode() #Menjadikan data decode menjadi string
    if domain_name in DNS_TABLE: #Memeriksa nama domain yang diterima ada dalam kamus DNS_TABLE
        ip_address = DNS_TABLE [domain_name]
    else: #Jika nama domain tidak ditemeukan baris ini yang akan dieksekusi
        ip_address = 'IP Address Tidak Di Temukan!!' #Menugaskan string ke variable ip_address

    #Mengirim alamat IP (baik alamat IP yang sebenarnya atau pesan "tidak ditemukan") kembali ke klien
    server_socket.sendto (ip_address.encode (), address)