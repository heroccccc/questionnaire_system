from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.config.from_object('main.config')

db = SQLAlchemy(app)

import main.views