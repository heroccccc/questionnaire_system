from flask import request, redirect, url_for, render_template
from main import app

@app.route('/')
def main():
    return "Hello world"