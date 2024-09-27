from flask import Flask, render_template, request
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['GET'])
def handle_request():
    IP = request.args.get('IP')
    logging.info(f"Received data: IP={IP}")
    return "Data received!"
    

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    if 'ChatGPT' in user_agent:  
        user_ip = request.remote_addr
        return render_template('alex_fake.html', ip=user_ip)
    elif 'Chrome' in user_agent:
        return render_template('alex_real.html')


if __name__ == '__main__':
    app.run(debug=True)
