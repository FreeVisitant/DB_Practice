from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:V1s1t%40nt@localhost/DB_Bank'
db = SQLAlchemy(app)

print("Flask y SQLAlchemy corren como el viento.")
