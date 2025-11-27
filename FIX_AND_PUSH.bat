@echo off
echo ========================================
echo Fixing Git Setup
echo ========================================
echo.

cd C:\Users\owusu\Documents\LibraryManagementSystem

echo Step 1: Removing incorrect remote...
git remote remove origin

echo.
echo Step 2: Adding correct remote...
git remote add origin https://github.com/YF2247/library-management-system.git

echo.
echo Step 3: Adding all project files...
git add .

echo.
echo Step 4: Creating commit...
git commit -m "Initial commit: Library Management System with 33 books"

echo.
echo Step 5: Pushing to GitHub...
git push -u origin main

echo.
echo ========================================
echo SUCCESS! Check GitHub:
echo https://github.com/YF2247/library-management-system
echo ========================================
pause
