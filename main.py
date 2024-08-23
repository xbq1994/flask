from flask import Flask, request, render_template_string, render_template
import logging

app = Flask(__name__, template_folder="templates")
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():

    user_agent = request.headers.get('User-Agent')
    if 'ChatGPT' in user_agent:  # now add condition on LLM agent specified string and render accordingly
        app.logger.info(f'Accessed: {request.path} from {request.remote_addr} and User_agent: {user_agent} and Template: {"alex_fake.html"}')
        data = [
            {"name": "Alice", "age": 30, "city": "New York"},
            {"name": "Bob", "age": 24, "city": "Los Angeles"},
            {"name": "Charlie", "age": 29, "city": "Chicago"}
        ]
        return render_template("table_real.html", data=data)
    elif 'Chrome' in user_agent:
        app.logger.info(f'Accessed: {request.path} from {request.remote_addr} and User_agent: {user_agent} and Template: {"alex_real.html"}')
        data = [
            {"name": "Alice", "age": 30, "city": "New York"},
            {"name": "Bob", "age": 24, "city": "Los Angeles"},
            {"name": "Charlie", "age": 29, "city": "Chicago"}
        ]
        return render_template("table_real.html", data=data)
    else:
        app.logger.info(f'Accessed: {request.path} from {request.remote_addr} and User_agent: {user_agent} and Template: {"empty"}')
        return render_template("alex_real.html")

if __name__ == '__main__':
    app.run(debug=True)
