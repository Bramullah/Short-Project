import socket #Mengimpor modul python yang menyediakan kemampuan komunikasi jaringan
SERVER_IP_ADDRESS = 'localhost' #Mendefinisikan variabel yang berisi alamat IP atau host server yang akan dikunjungi klien
DOMAIN_NAME = 'www.twitter.com' #Mendefinisikan variabel yang berisi domain yang akan dicari oleh klien

client_socket = socket.socket (socket.AF_INET, socket. SOCK_DGRAM) #Soket ini akan digunakan untuk komunikasi jaringan oleh klien
client_socket.sendto (DOMAIN_NAME.encode (), (SERVER_IP_ADDRESS, 53)) #Mengirim permintaan DNS ke server, diubah dalam bentuk byte dan dikirim pada port 53

#Menerima respons dari server, dan disimpan pada variable response dalam ukuran Max-1024 byte
response, _ = client_socket.recvfrom (1024)
ip_address = response.decode() #Respon yang diterima didekode menjadi string dan disimpan pada variable ip_address

print (f"Alamat IP dari {DOMAIN_NAME} adalah {ip_address}") #Mencetak alamat IP yang ditemukan dari nama domain yang dicari, dalam format string pada/ke konsol