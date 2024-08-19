from flask import Flask, request, render_template_string, render_template

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')

    if 'ChatGPT' in user_agent:  # now add condition on LLM agent specified string and render accordingly
        return render_template("alex_fake.html")
    elif 'Chrome' in user_agent:
        return render_template("alex_real.html")
    else:
        return render_template_string("<h1>Desktop Version</h1><p>You are using a desktop device.</p>")

if __name__ == '__main__':
    app.run(debug=True)
