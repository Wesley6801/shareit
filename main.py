import requests
from flask import Flask, render_template, url_for, flash, redirect, request
#print("testing style.yaml")

app = Flask(__name__)
app.config['SECRET_KEY'] = '766ad3b9779f8e26642e74331dbf694c'


@app.route("/")
def home():
    return "Welcome home"


@app.route("/register")
def register_page():
    pass


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
