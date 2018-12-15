'''
1. Update the ip address in the function get_server_addr().
2. Click "Commit changes" green button (down this page).
3. Go to https://dashboard.heroku.com/apps/localcloudtech/deploy/github (heroku website).
4. Go down the page and click "Deploy Branch".
5. Wait until it's done.
'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_server_addr():
    return 'https://93.173.90.114'


if __name__ == '__main__':
   app.run()
