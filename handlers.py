from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_server_addr():
    return 'https://93.173.76.253:8080'
    # return 'https://lct.localcloudtech.com'


if __name__ == '__main__':
   app.run()
