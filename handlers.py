'''
1. Update the ip address in the function get_server_addr().
2. Go to https://dashboard.heroku.com/apps/localcloudtech/deploy/github (heroku website).
3. Go down the page and click "Deploy Branch".
4. Wait until it's done.
'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_server_addr():
    return 'https://93.173.76.253'


if __name__ == '__main__':
   app.run()
