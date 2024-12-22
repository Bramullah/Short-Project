from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about_us')
def about_us():
    return 'This is about us'

if __name__ == '__main__':
    app.run(debug=True)