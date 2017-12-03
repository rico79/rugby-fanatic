from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

