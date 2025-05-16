from flask import Flask, render_template  # 新增导入render_template

app = Flask(__name__)

# 路由功能，根据访问的路径不同，返回不同的页面
@app.route('/')
def hello_world():
    return render_template('index.html')  # 改为返回HTML模板
# 访问路径为/about时，返回about.html页面
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/greeting/<name>')
def greeting(name):
    return f'Hello, {name}!'
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)