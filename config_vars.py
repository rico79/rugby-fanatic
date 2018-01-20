from os import environ as env

# APP
APP_SECRET_KEY = env.get('APP_SECRET_KEY', '')

# DATABASE
DB_HOST = env.get('DB_HOST', '')
DB_PORT = env.get('DB_PORT', 0)
DB_DBNAME = env.get('DB_DBNAME', '')
DB_USERNAME = env.get('DB_USERNAME', '')
DB_PASSWORD = env.get('DB_PASSWORD', '')

# AUTH0
AUTH0_DOMAIN = env.get('AUTH0_DOMAIN', '')
AUTH0_USERINFO = AUTH0_DOMAIN + '/userinfo'
AUTH0_LOGIN_CALLBACK = env.get('AUTH0_LOGIN_CALLBACK', '')
AUTH0_CLIENT_ID = env.get('AUTH0_CLIENT_ID', '')
AUTH0_CLIENT_SECRET = env.get('AUTH0_CLIENT_SECRET', '')