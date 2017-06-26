from flask import Flask
from config import config

app = Flask(__name__)
app.config.from_object(config["production"]) #this can be changed to whatever mode you are in


from app import views, forms
