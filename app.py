from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask_oauthlib.client import OAuth
from six.moves.urllib.parse import urlencode
from functools import wraps
from datetime import datetime
import requests
import json

import config_vars

app = Flask(__name__)

# Wrap auth
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'profile' not in session:
            # Redirect to Login page here
            return redirect('/')
        
        return f(*args, **kwargs)
        
    return decorated

# Set Authentication
oauth = OAuth(app)
auth0 = oauth.remote_app(
    'auth0',
    consumer_key=config_vars.AUTH0_CLIENT_ID,
    consumer_secret=config_vars.AUTH0_CLIENT_SECRET,
    request_token_params={
        'scope': 'openid profile',
        'audience': config_vars.AUTH0_USERINFO
    },
    base_url=config_vars.AUTH0_DOMAIN,
    access_token_method='POST',
    access_token_url='/oauth/token',
    authorize_url='/authorize',
)

# Routes
@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/home')
def home_page():
    print('secret key : ' + config_vars.APP_SECRET_KEY)
    return render_template('home.html')

@app.route('/dashboard')
@requires_auth
def dashboard():
    return render_template('dashboard.html',
                           userinfo=session['profile'],
                           userinfo_pretty=json.dumps(session['jwt_payload'], indent=4))

@app.route('/login')
def login():
    return auth0.authorize(callback=config_vars.AUTH0_LOGIN_CALLBACK)

@app.route('/callback')
def callback_handling():
    # Handles response from token endpoint
    resp = auth0.authorized_response()
    if resp is None:
        raise Exception('Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        ))
    
    url = config_vars.AUTH0_USERINFO
    headers = {'authorization': 'Bearer ' + resp['access_token']}
    resp = requests.get(url, headers=headers)
    userinfo = resp.json()
    
    # Store user information in flask session.
    session['jwt_payload'] = userinfo
    
    session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture']
    }
    
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    # Clear session stored data
    session.clear()
    # Redirect user to logout endpoint
    params = {'returnTo': url_for('home', _external=True), 'client_id': config_vars.AUTH0_CLIENT_ID}
    return redirect(auth0.base_url + '/v2/logout?' + urlencode(params))

# Run server
if __name__ == '__main__':
    app.secret_key = config_vars.APP_SECRET_KEY
    app.run(debug=True, use_reloader=True)

