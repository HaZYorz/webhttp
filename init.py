from flask import Flask, render_template  # 新增导入render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')  # 改为返回HTML模板

if __name__ == '__main__':
    app.run(debug=True, port=8080)