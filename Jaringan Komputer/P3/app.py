from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return 'Hello, World!'

@app.route('/tentang')
def tentang():
    return 'Hai, ini adalah halaman tentang Saya (Ibrahim Bramullah)'

if __name__ == '__main__':
    app.run(debug=True)