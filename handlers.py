from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_server_addr():
    # return 'http://109.186.174.98'
    return 'https://lct.localcloudtech.com'


if __name__ == '__main__':
   app.run()
