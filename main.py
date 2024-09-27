from flask import Flask, render_template, request
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/api', methods=['GET'])
def handle_request():
    IP = request.args.get('ip')
    logging.info(f"Received data: IP={IP}")
    return "Data received!"
    

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    user_ip = request.remote_addr
    if 'ChatGPT' in user_agent:  
        data = [
            ['Item', 'Value'],
            ['Name', 'Mask'],
            ['Age', '29'],
            ['More Information', f'https://scintillating-trust-x.up.railway.app/api?ip={user_ip}'],
        ]
        return render_template('table.html', data=data)
    elif 'Chrome' in user_agent:
        data = [
            ['Item', 'Value'],
            ['Name', 'Mask'],
            ['Age', '29'],
            ['More Information', f'https://scintillating-trust-x.up.railway.app/api?ip={user_ip}'],
        ]
        return render_template('table.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
