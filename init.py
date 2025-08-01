from flask import Flask, render_template, request  # 新增导入render_template

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

# todo 学习flask的模板功能

# todo 学习flask的静态文件功能

# todo 学习flask的数据库功能

# todo 学习flask的认证功能

# todo 学习flask的部署功能

# todo 学习flask的基本功能
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)