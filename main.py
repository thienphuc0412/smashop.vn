import webbrowser
import threading
import os
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from database import DataBase, User

app = Flask(__name__)
db = DataBase()

# Bật chế độ debug
app.config['DEBUG'] = True
# Thiết lập secret key cho session
app.config['SECRET_KEY'] = 'smashopee'  # Thay đổi thành một key phức tạp và bí mật

# Khởi tạo LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'loginPage'

@login_manager.user_loader
def load_user(user_id):
    return db.get_user(user_id)

# Địa chỉ server Flask
HOST = "127.0.0.1"
PORT = 4662

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def loginPage():
    # Nếu user đã đăng nhập, chuyển hướng về trang chủ
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template("login.html")

@app.route("/signup")
def signupPage():
    # Nếu user đã đăng nhập, chuyển hướng về trang chủ
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template("signup.html")

@app.route("/shop")
def shopPage():
    return render_template("shop.html")

#route giao tiếp với client
@app.route("/contact")
def contactusPage():
    return render_template("contactus.html")

@app.route("/about")
def aboutPage():
    return render_template("about.html")

@app.route("/cart")
@login_required
def cartPage():
    return render_template("cart.html")

@app.route("/api/login", methods=['POST'])
def login():
    data = request.get_json()
    
    # Kiểm tra dữ liệu đầu vào
    if not all(key in data for key in ['username', 'password']):
        return jsonify({
            'success': False,
            'message': 'Thiếu thông tin đăng nhập'
        }), 400
    
    # Kiểm tra đăng nhập
    user = db.check_login(
        username=data['username'],
        password=data['password']
    )
    
    if user:
        login_user(user)
        return jsonify({
            'success': True,
            'message': 'Đăng nhập thành công'
        })
    else:
        return jsonify({
            'success': False,
            'message': 'Tên đăng nhập hoặc mật khẩu không đúng'
        }), 401

@app.route("/api/logout")
@login_required
def logout():
    logout_user()
    return jsonify({
        'success': True,
        'message': 'Đăng xuất thành công'
    })

@app.route("/api/signup", methods=['POST'])
def signup():
    data = request.get_json()
    
    # Kiểm tra dữ liệu đầu vào
    if not all(key in data for key in ['username', 'password', 'email']):
        return jsonify({
            'success': False,
            'message': 'Thiếu thông tin đăng ký'
        }), 400
    
    # Gọi hàm tạo user từ database
    success, message = db.create_user(
        username=data['username'],
        password=data['password'],
        email=data['email']
    )
    
    status_code = 200 if success else 400
    return jsonify({
        'success': success,
        'message': message
    }), status_code

# Chỉ mở trình duyệt nếu đây là tiến trình chính (tránh auto-reload)
def open_browser():
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":  # Chỉ chạy khi Flask khởi động lần đầu
        webbrowser.open(f"http://{HOST}:{PORT}/", new=2)

if __name__ == "__main__":
    threading.Thread(target=open_browser).start()
    app.run(host=HOST, port=PORT)