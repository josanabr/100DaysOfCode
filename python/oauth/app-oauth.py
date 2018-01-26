from flask import Flask, redirect, url_for, session
from flask_oauth import OAuth
import os
import urllib
import ssl
 
# You must configure these 3 values from Google APIs console
# https://code.google.com/apis/console
GOOGLE_CLIENT_ID = 'SU_CLIENT_ID'
GOOGLE_CLIENT_SECRET = 'SU_CLIENT_SECRET'
REDIRECT_URI = '/oauth2callback'  # one of the Redirect URIs from Google APIs console
 
SECRET_KEY = 'development key'
DEBUG = True
 
app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
oauth = OAuth()
 
google = oauth.remote_app('google',
                          base_url='https://www.google.com/accounts/',
                          authorize_url='https://accounts.google.com/o/oauth2/auth',
                          request_token_url=None,
                          request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email',
                                                'response_type': 'code'},
                          access_token_url='https://accounts.google.com/o/oauth2/token',
                          access_token_method='POST',
                          access_token_params={'grant_type': 'authorization_code'},
                          consumer_key=GOOGLE_CLIENT_ID,
                          consumer_secret=GOOGLE_CLIENT_SECRET)
 
@app.route('/')
def index():
    access_token = session.get('access_token')
    if access_token is None:
        return redirect(url_for('login'))
 
    access_token = access_token[0]
    from urllib2 import Request, urlopen, URLError, HTTPError
 
    headers = {'Authorization': 'OAuth '+access_token}
    # No es una practica segura pero permite que la aplicacion funcione
    # Fuente: https://goo.gl/9UrvH7
    context = ssl._create_unverified_context()
    req = Request('https://www.googleapis.com/oauth2/v1/userinfo',
                  None, headers)

    try:
        res = urlopen(req, context=context)
    except URLError as e:
        print("URLError")
        print(e.reason)
    except HTTPError, e:
        if e.code == 401:
            # Unauthorized - bad token
            session.pop('access_token', None)
            return redirect(url_for('login'))
 
    return res.read()
 
 
@app.route('/login')
def login():
    callback=url_for('authorized', _external=True)
    return google.authorize(callback=callback)
 
 
 
@app.route(REDIRECT_URI)
@google.authorized_handler
def authorized(resp):
    access_token = resp['access_token']
    session['access_token'] = access_token, ''
    return redirect(url_for('index'))
 
 
@google.tokengetter
def get_access_token():
    return session.get('access_token')
 
 
def main(port=5000):
    app.run(host='0.0.0.0', port=port)
 
 
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    main()

