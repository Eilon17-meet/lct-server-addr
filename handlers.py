from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_server_addr():
    return 'https://109.186.174.98:5000'


if __name__ == '__main__':
   app.run()