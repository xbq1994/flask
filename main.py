from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')

    if 'Mobile' in user_agent:
        return render_template_string("<h1>Mobile Version</h1><p>You are using a mobile device.</p>")
    elif 'Chrome' in user_agent:
        return render_template_string("<h1>Chrome Browser</h1><p>桂桂快睡觉.</p>")
    else:
        return render_template_string("<h1>Desktop Version</h1><p>You are using a desktop device.</p>")

if __name__ == '__main__':
    app.run(debug=True)
