from flask import Flask, request, render_template_string, render_template

app = Flask(__name__, template_folder="html_pages")

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    print(f'User-Agent: {user_agent}')
    
    if 'ChatGPT' in user_agent:  # now add condition on LLM agent specified string and render accordingly
        print("alex_fake.html is loaded")
        return render_template("alex_fake.html")
    elif 'Chrome' in user_agent:
        print("alex_real.html is loaded")
        return render_template("alex_real.html")
    else:
        return render_template_string("<h1>Desktop Version</h1><p>You are using a desktop device.</p>")

if __name__ == '__main__':
    app.run(debug=True)
