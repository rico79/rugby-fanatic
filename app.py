from flask import Flask
from db import config_database
from auth import get_auth0_remote_app, auth_bp
import config_vars

app = Flask(__name__)
app.secret_key = config_vars.APP_SECRET_KEY

# connect to MongoDB
config_database(app)

# Connect auth0 remote application
get_auth0_remote_app(app)

# Register blueprints
app.register_blueprint(auth_bp)

# Index route
@app.route('/')
def home():
    return app.send_static_file('index.html')

# Run server
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

