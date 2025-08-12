@echo off
setlocal enabledelayedexpansion

:: Hiển thị trạng thái git
echo ===== Git Status =====
git status
echo ====================
echo.

:: Yêu cầu nhập tin nhắn commit
set /p commit_msg="Nhập tin nhắn commit: "

:: Kiểm tra xem người dùng có nhập tin nhắn không
if "!commit_msg!"=="" (
    echo Lỗi: Tin nhắn commit không được để trống!
    pause
    exit /b 1
)

:: Thực hiện các lệnh git
echo.
echo Đang thêm các file...
git add .

echo.
echo Đang commit với tin nhắn: "!commit_msg!"
git commit -m "!commit_msg!"

echo.
echo Đang push lên remote...
git push origin master

echo.
echo ===== Hoàn thành =====
echo Đã push lên git thành công!
pause