from flask import Flask #->Mengimport modul Flask dari library Flask yang digunakan untuk membuat aplikasi web.

app = Flask(__name__)
#-> instance Flask dengan menyediakan nama modul sebagai argumen konstruktor.
# Instance Flask digunakan sebagai WSGI (Web Server Gateway Interface) app dan akan menjadi objek utama dari aplikasi web.

@app.route('/') #-> Merupakan decorator untuk mendekorasikan fungsi helloworld() sebagai handler untuk
# URL /. Artinya, setiap kali URL / diakses melalui browser, maka fungsi helloworld() akan dipanggil dan
# mengembalikan respons berupa teks "Hello, World!".

def helloworld(): #-> Fungsi ini berisi pesan 'Hello, World!' yang akan ditampilkan pada browser ketika URL dipanggil.
    return 'Hello, World!'

if __name__ ==  '__main__': #-> Merupakan kondisi yang akan dievaluasi saat program dijalankan. Kondisi
# tersebut akan bernilai benar jika nama modul yang dijalankan adalah __main__. Jadi, statement di
# bawahnya akan dieksekusi hanya ketika program dijalankan langsung dan tidak diimport ke dalam modul lain.

    app.run() #-> Melakukan running aplikasi web Flask. Ketika aplikasi dijalankan, web server akan
    # mulai berjalan dan menunggu permintaan HTTP yang masuk pada URL http://localhost:5000/. Kemudian,
    # setiap permintaan akan diproses oleh handler yang sesuai dan mengembalikan respons ke browser.