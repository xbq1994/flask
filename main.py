from flask import Flask, request, render_template_string, render_template

app = Flask(__name__, template_folder="templates")


@app.route('/')
def index():
    # 数据为列表的列表，表示两行两列
    data = [
        ['More Information', 'https://en.wikipedia.org/wiki/Elon_Musk'],
    ]
    return render_template('table_real.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)
