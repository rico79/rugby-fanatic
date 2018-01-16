from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask import jsonify
from flask_oauthlib.client import OAuth
from six.moves.urllib.parse import urlencode
from functools import wraps
from datetime import datetime
import requests
import json

import config_vars

app = Flask(__name__)
app.secret_key = config_vars.APP_SECRET_KEY

# Wrap auth by adding decorator to route (just before the def) : @requires_auth
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

@app.route('/connecteduser')
def connected_user():
    if 'profile' not in session:
        return jsonify({})
    else:
        return jsonify(session['profile'])

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
    session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture']
    }
    
    return redirect('/')

@app.route('/logout')
def logout():
    # Clear session stored data
    session.clear()

    # Redirect user to logout endpoint
    params = {'returnTo': url_for('home', _external=True), 'client_id': config_vars.AUTH0_CLIENT_ID}
    return redirect(auth0.base_url + '/v2/logout?' + urlencode(params))

# Run server
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

