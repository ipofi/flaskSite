from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>Home</h2>"


@app.route("/about-us")
def aboutUs():
    return "<h2>About us</h2>"


@app.route("/contact-us")
def contactUs():
    return "<h2>Contact Us</h2>"


@app.route("/products")
def products():
    return "<h2>Products</h2>"

@app.route("/services")
def services():
    return "<h2>Services</h2>"
