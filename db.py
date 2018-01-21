from flask_pymongo import PyMongo
import config_vars

# Connect app to MongoDB
def config_database(app):
    app.config['MONGO_HOST'] = config_vars.DB_HOST
    app.config['MONGO_PORT'] = config_vars.DB_PORT
    app.config['MONGO_DBNAME'] = config_vars.DB_DBNAME
    app.config['MONGO_USERNAME'] = config_vars.DB_USERNAME
    app.config['MONGO_PASSWORD'] = config_vars.DB_PASSWORD

# Get app MongoDB
def get_mongodb(app):
    return PyMongo(app, config_prefix='MONGO')