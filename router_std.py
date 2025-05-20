from flask import Flask, render_template, request, make_response  

app = Flask(__name__)

# 路由功能，根据访问的路径不同，返回不同的页面
# 访问路径为根目录时，返回index.html页面
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
# 设置POST请求，接收参数
@app.route('/submit', methods=['POST'])
def submit():
    # get用法需要指出参数名，否则会报错
    post_data = request.form.get('str')  # 获取表单数据
    #print(post_data)  # 打印表单数据
    return f'Form submitted successfully,you submit:{post_data}'
# 响应参数，设置响应
@app.route('/response')
def response():
    response = make_response('这里是响应包的内容')  # 创建响应对象，指定响应包内容
    response.headers['X-Custom-Header'] = 'This is Flask'  # 设置响应头
    response.status_code = 114514  # 设置响应状态码
    return response

# 主程序，拉起服务
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)