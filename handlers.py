from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_server_addr():
    return 'http://93.173.76.253'
    # return 'https://lct.localcloudtech.com'


if __name__ == '__main__':
   app.run()
