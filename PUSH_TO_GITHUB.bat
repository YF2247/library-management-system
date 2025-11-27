@echo off
echo ========================================
echo Push to GitHub
echo ========================================
echo.

cd C:\Users\owusu\Documents\LibraryManagementSystem

set /p username="Enter your GitHub username: "

echo.
echo Adding remote repository...
git remote add origin https://github.com/%username%/library-management-system.git

echo.
echo Setting main branch...
git branch -M main

echo.
echo Pushing to GitHub...
git push -u origin main

echo.
echo ========================================
echo Successfully pushed to GitHub!
echo ========================================
echo.
echo Your repository: https://github.com/%username%/library-management-system
echo.
echo Next: Deploy to Render or Railway (see DEPLOYMENT.md)
echo.
pause
