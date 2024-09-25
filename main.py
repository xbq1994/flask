from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    product_a = {
        "name": "Smartphone A",
        "price": "$700",
        "battery_life": "24 hours",
        "camera": "48 MP",
        "processor": "A12 Chip",
        "storage": "128 GB"
    }

    product_b = {
        "name": "Smartphone B",
        "price": "$600",
        "battery_life": "20 hours",
        "camera": "64 MP",
        "processor": "A14 Chip",
        "storage": "256 GB"
    }

    return render_template('comparison.html', product_a=product_a, product_b=product_b)

if __name__ == '__main__':
    app.run(debug=True)
