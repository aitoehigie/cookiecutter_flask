from flask import redirect, session, render_template, request, url_for, flash
from app import app
from .forms import * #bad practice

@app.route("/", methods=["GET", "POST"])
def index():
    return "Hello world"


