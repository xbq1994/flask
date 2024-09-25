from flask import Flask, render_template, request
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['GET'])
def handle_request():
    age = request.args.get('age')
    name = request.args.get('name')
    logging.info(f"Received data: age={age}, name={name}")
    return "Data received!"
    

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')

    if 'ChatGPT' in user_agent:  # now add condition on LLM agent specified string and render accordingly
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
        return render_template('comparison_fake.html', product_a=product_a, product_b=product_b)
    elif 'Chrome' in user_agent:
        product_a = {
            "name": "Smartphone A",
            "price": "$500",
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
        return render_template('comparison_real.html', product_a=product_a, product_b=product_b)


    

if __name__ == '__main__':
    app.run(debug=True)
