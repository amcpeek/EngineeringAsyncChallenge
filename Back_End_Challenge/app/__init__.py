import os

from flask import Flask, render_template, redirect
from .config import Config
# from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def first_endpoint():
    return "Hello How are you?"
