# SmaShop - Dự án Clone Shopee

## 📝 Tổng Quan
SmaShop là một dự án web thương mại điện tử được xây dựng dựa trên mô hình của Shopee, với các tính năng cốt lõi được đơn giản hóa. Dự án này tập trung vào việc tạo ra một nền tảng cho phép người dùng vừa có thể mua sắm vừa có thể tạo cửa hàng riêng để bán hàng.

## 🏗️ Cấu Trúc Trang Web

### 1. Trang Chủ (Homepage)
- Hiển thị danh sách các shop và sản phẩm
- Giao diện tìm kiếm và lọc sản phẩm

### 2. Hệ Thống Tài Khoản
- Trang đăng nhập
- Trang đăng ký

### 3. Khu Vực Người Bán (Seller Area)
- My Shop: Quản lý gian hàng và upload sản phẩm
- My Orders: Quản lý đơn hàng với các trạng thái:
  - Đã đặt
  - Đang đóng hàng
  - Đang vận chuyển
  - Đã nhận hàng
- Dashboard: Thống kê và quản lý doanh thu

### 4. Khu Vực Người Mua (Buyer Area)
- Buyer Orders: Theo dõi đơn hàng đã đặt
- Giỏ hàng và thanh toán

## 🛠️ Stack Công Nghệ

### Frontend
- **Framework CSS:** Bootstrap 5.3
- **Icons:** Font Awesome 6.4
- **Typography:** Google Font - Open Sans
- **Color Scheme:** 
  ```css
  :root {
    --primary-color: #ee4d2d;    /* Shopee Orange */
    --secondary-color: #ffffff;   /* White */
    --text-color: #222222;       /* Dark Text */
    --light-orange: #fef6f5;     /* Light Orange Background */
    --border-color: #efefef;     /* Border Color */
  }
  ```

### Backend
- **Server Environment:** XAMPP (Apache + MySQL + PHP)
- **Database:** MySQL
  - Schemas được định nghĩa trước
  - Dữ liệu demo có sẵn
- **API Communication:** XMLHttpRequest (XHR)

### Development Tools
- **Local Development:** XAMPP
- **Version Control:** Git

## 📋 Kế Hoạch Phát Triển

### Phase 1: Thiết lập Cơ bản
1. Khởi tạo project với cấu trúc thư mục
2. Thiết lập database schema
3. Tạo template và layout cơ bản

### Phase 2: Xây dựng Core Features
1. Hệ thống Authentication
2. Trang chủ và hiển thị sản phẩm
3. Chức năng My Shop
4. Hệ thống đơn hàng

### Phase 3: Advanced Features
1. Dashboard thống kê
2. Tìm kiếm và lọc nâng cao
3. Tối ưu hiệu năng

### Phase 4: Testing & Deployment
1. Testing
2. Bug fixing
3. Documentation
4. Deployment

## 🔄 Database Schema (Cơ bản)

```sql
-- Users Table
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(255),
    email VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Shops Table
CREATE TABLE shops (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    shop_name VARCHAR(100),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Products Table
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    shop_id INT,
    name VARCHAR(200),
    price DECIMAL(10,2),
    description TEXT,
    stock INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (shop_id) REFERENCES shops(id)
);

-- Orders Table
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    buyer_id INT,
    shop_id INT,
    status ENUM('pending', 'processing', 'shipping', 'completed'),
    total_amount DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (buyer_id) REFERENCES users(id),
    FOREIGN KEY (shop_id) REFERENCES shops(id)
);
```

## 📈 Kế Hoạch Mở Rộng (Future Features)
- Tích hợp thanh toán online
- Hệ thống đánh giá và review
- Chat trực tiếp giữa người mua và người bán
- Mobile responsive design
- Tối ưu SEO

## 🤝 Đóng góp
Dự án đang trong giai đoạn phát triển và chào đón mọi đóng góp từ cộng đồng.

## 📝 License
MIT License