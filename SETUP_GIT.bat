@echo off
echo ========================================
echo Git Setup for Library Management System
echo ========================================
echo.

cd C:\Users\owusu\Documents\LibraryManagementSystem

echo Checking if Git is installed...
git --version
if errorlevel 1 (
    echo ERROR: Git is not installed!
    echo Please install Git from: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo.
echo Initializing Git repository...
git init

echo.
echo Adding files to Git...
git add .

echo.
echo Creating initial commit...
git commit -m "Initial commit: Library Management System with 33 books"

echo.
echo ========================================
echo Git repository initialized successfully!
echo ========================================
echo.
echo NEXT STEPS:
echo.
echo 1. Go to GitHub: https://github.com/new
echo 2. Create a new repository named: library-management-system
echo 3. DO NOT initialize with README (we already have one)
echo 4. Copy the repository URL
echo.
echo 5. Then run these commands (replace YOUR_USERNAME):
echo.
echo    git remote add origin https://github.com/YOUR_USERNAME/library-management-system.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo Or run: PUSH_TO_GITHUB.bat (after creating the repo)
echo.
pause
