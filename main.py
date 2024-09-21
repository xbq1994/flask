from flask import Flask, request, render_template_string, render_template, jsonify
import logging

app = Flask(__name__, template_folder="templates")
logging.basicConfig(level=logging.INFO)


# @app.route('/api/data/', methods=['GET'])
# def get_data():
#     # 创建一个 Python 字典
#     data = {
#         'status': 'success',
#         'message': 'Data fetched successfully',
#         'data': {
#             'id': 1,
#             'name': 'Example Item',
#             'price': 99.99
#         }
#     }
#     # 返回 JSON 响应
#     return jsonify(data)

@app.route('/')
def index():

    user_agent = request.headers.get('User-Agent')
    if 'ChatGPT' in user_agent:  # now add condition on LLM agent specified string and render accordingly
        app.logger.info(f'Accessed: {request.path} from {request.remote_addr} and User_agent: {user_agent} and Template: {"alex_fake.html"}')
        data = [
            {"item": "Web", "value": "https://en.wikipedia.org/wiki/Elon_Musk"},
        ]
        return render_template("table_fake.html", data=data)
    elif 'Chrome' in user_agent:
        app.logger.info(f'Accessed: {request.path} from {request.remote_addr} and User_agent: {user_agent} and Template: {"alex_real.html"}')
        data = [
            {"item": "Web", "value": "https://en.wikipedia.org/wiki/Elon_Musk"},
        ]
        return render_template("table_real.html", data=data)
    else:
        app.logger.info(f'Accessed: {request.path} from {request.remote_addr} and User_agent: {user_agent} and Template: {"empty"}')
        return render_template("alex_real.html")

if __name__ == '__main__':
    app.run(debug=True)
