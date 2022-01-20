import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

CORS(app)

root_dir = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(root_dir, 'database.db')

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + db_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
