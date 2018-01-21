from flask_oauthlib.client import OAuth
from flask import Blueprint
from flask import current_app
from flask import redirect
from flask import session
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask import jsonify
from six.moves.urllib.parse import urlencode
from functools import wraps
from datetime import datetime
import requests
import json
import config_vars
from db import mongodb

remote_apps = {}

# Wrap auth by adding decorator to route (just before the def) : @requires_auth
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'profile' not in session:
            # Redirect to Login page here
            return redirect('/login')
        
        return f(*args, **kwargs)
        
    return decorated

# Get Auth0 remote
def connect_auth0_remote_app(app):
    oauth = OAuth(app)
    remote_apps['auth0'] = oauth.remote_app(
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

# Blue print construction
auth_bp = Blueprint('auth_bp', __name__)

# Routes
@auth_bp.route('/connecteduser')
def connected_user():
    if 'profile' not in session:
        return jsonify({})
    else:
        return jsonify(session['profile'])

@auth_bp.route('/login')
def login():
    return remote_apps['auth0'].authorize(callback=config_vars.AUTH0_LOGIN_CALLBACK)

@auth_bp.route('/callback')
def callback_handling():
    # Handles response from token endpoint
    resp = remote_apps['auth0'].authorized_response()
    if resp is None:
        raise Exception('Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        ))
    
    url = config_vars.AUTH0_USERINFO
    headers = {'authorization': 'Bearer ' + resp['access_token']}
    resp = requests.get(url, headers=headers)
    userinfo = resp.json()

    #Set user profile
    userprofile = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture']
    }

    # Save user in db
    result = mongodb['db'].db.users.replace_one(
        {'user_id': userprofile['user_id']},
        userprofile,
        True,
    )
    
    # Store user information in flask session.
    if result.acknowledged :
        session['profile'] = userprofile
    
    return redirect('/')

@auth_bp.route('/logout')
def logout():
    # Clear session stored data
    session.clear()

    # Redirect user to logout endpoint
    params = {'returnTo': url_for('home', _external=True), 'client_id': config_vars.AUTH0_CLIENT_ID}
    return redirect(remote_apps['auth0'].base_url + '/v2/logout?' + urlencode(params))