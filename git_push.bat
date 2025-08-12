@echo off
setlocal enabledelayedexpansion

:: Display git status
echo ===== Git Status =====
git status
echo ====================
echo.

:: Request commit message
set /p commit_msg="Enter commit message: "

:: Check if commit message is empty
if "!commit_msg!"=="" (
    echo Error: Commit message cannot be empty!
    pause
    exit /b 1
)

:: Execute git commands
echo.
echo Adding files...
git add .

echo.
echo Committing with message: "!commit_msg!"
git commit -m "!commit_msg!"

echo.
echo Pushing to remote...
git push origin master

echo.
echo ===== Complete =====
echo Successfully pushed to git!
pause