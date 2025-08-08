import pymongo
from pymongo import MongoClient
from datetime import datetime
import json
import os
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user_data):
        self.user_id = user_data['user_id']
        self.username = user_data['username']
        self.email = user_data['email']
    
    def get_id(self):
        return self.user_id

class DataBase:
    def __init__(self):
        try:
            self.client = MongoClient('mongodb://localhost:27017/')
            self.db = self.client['smashop']  # Tên database là 'smashop'
            # Đảm bảo collection counters tồn tại với giá trị khởi tạo
            if not self.db.counters.find_one({"_id": "user_id"}):
                self.db.counters.insert_one({
                    "_id": "user_id",
                    "sequence_value": 0
                })
        except Exception as e:
            print(f"Lỗi kết nối MongoDB: {e}")
    
    def get_next_sequence_value(self, sequence_name):
        """Lấy và tăng giá trị sequence"""
        sequence_document = self.db.counters.find_one_and_update(
            {"_id": sequence_name},
            {"$inc": {"sequence_value": 1}},
            return_document=True
        )
        return sequence_document["sequence_value"]
    
    def get_user(self, user_id):
        """Lấy thông tin user theo ID"""
        user_data = self.db.users.find_one({"user_id": user_id})
        if user_data:
            return User(user_data)
        return None

    def check_login(self, username, password):
        """Kiểm tra thông tin đăng nhập"""
        user_data = self.db.users.find_one({
            "username": username,
            "password": password  # Trong thực tế nên so sánh password đã mã hóa
        })
        if user_data:
            return User(user_data)
        return None

    def create_user(self, username, password, email):
        try:
            # Kiểm tra xem username đã tồn tại chưa
            if self.db.users.find_one({"username": username}):
                return False, "Tên đăng nhập đã tồn tại"
            
            # Kiểm tra email đã tồn tại chưa
            if self.db.users.find_one({"email": email}):
                return False, "Email đã được sử dụng"
            
            # Lấy ID mới cho user
            user_id = self.get_next_sequence_value("user_id")
            # Format ID thành chuỗi 3 số
            formatted_id = f"{user_id:03d}"
            
            # Tạo user mới
            user = {
                "user_id": formatted_id,
                "username": username,
                "password": password,  # Trong thực tế nên mã hóa password
                "email": email,
                "created_at": datetime.now()
            }
            
            # Thêm vào database
            self.db.users.insert_one(user)
            return True, "Đăng ký thành công"
            
        except Exception as e:
            return False, f"Lỗi khi tạo tài khoản: {str(e)}"
