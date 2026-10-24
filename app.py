from flask import Flask

app = Flask(__name__)

# 首頁路由
@app.route('/')
def hello():
    return 'Hello, World!'

# /home 路由
@app.route('/home')
def home():
    return '<h1>Home Page</h1>'

# /about 路由
@app.route('/about')
def about():
    return '<h1>About Page</h1>'

if __name__ == '__main__':
    # debug=True 方便開發時存檔自動重啟並顯示錯誤
    app.run(debug=True)