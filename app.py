from flask import Flask, render_template

app = Flask(__name__)

# Datos de ejemplo (puedes reemplazarlos con una base de datos)
items = [
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
    {"image": "static/images/item1.jpg", "text": "casio G-shock", "price": "€35"},
]

@app.route('/')
def index():
    return render_template("index.html", items=items)

if __name__ == "__main__":
    app.run(debug=True)
