# DEPLOYMENT GUIDE

## Quick Start - Push to GitHub

1. Open Command Prompt or PowerShell
2. Navigate to project:
   cd C:\Users\owusu\Documents\LibraryManagementSystem

3. Initialize Git (if not already done):
   git init
   git add .
   git commit -m "Initial commit: Library Management System"

4. Create a new repository on GitHub:
   - Go to https://github.com/new
   - Name it: library-management-system
   - Don't initialize with README (we already have one)
   - Click "Create repository"

5. Push to GitHub:
   git remote add origin https://github.com/YOUR_USERNAME/library-management-system.git
   git branch -M main
   git push -u origin main

## Deploy to Render (Recommended - Free Tier Available)

1. Go to https://render.com and sign up/login
2. Click "New +" and select "Web Service"
3. Connect your GitHub account
4. Select your library-management-system repository
5. Configure:
   - Name: library-management-system
   - Environment: Python 3
   - Build Command: pip install -r requirements.txt
   - Start Command: gunicorn app:app
   - Instance Type: Free
6. Click "Create Web Service"
7. Wait for deployment (2-3 minutes)
8. Your app will be live at: https://library-management-system-xxxx.onrender.com

## Deploy to Railway (Easy - Free Tier Available)

1. Go to https://railway.app and sign up/login
2. Click "New Project"  "Deploy from GitHub repo"
3. Select your library-management-system repository
4. Railway auto-detects the Procfile and deploys
5. Click "Generate Domain" to get your live URL
6. Your app will be live at: https://library-management-system-production.up.railway.app

## Deploy to Heroku (Classic Option)

1. Install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli
2. Open terminal and login:
   heroku login
3. Navigate to project:
   cd C:\Users\owusu\Documents\LibraryManagementSystem
4. Create Heroku app:
   heroku create your-library-app-name
5. Push to Heroku:
   git push heroku main
6. Open your app:
   heroku open

## Important Notes

- The .gitignore file prevents library.db from being pushed to GitHub
- On deployment, a new empty database will be created
- Default admin account (admin/admin123) will be auto-created
- You'll need to add books again on the deployed version
- For production, consider using PostgreSQL instead of SQLite

## Adding Books to Deployed App

After deployment, you can:
1. Login as admin
2. Manually add books through the web interface
3. Or modify app.py to include sample books on first run

## Security Recommendations for Production

1. Change the secret key in app.py:
   app.secret_key = 'your-random-secret-key-here'

2. Use environment variables:
   import os
   app.secret_key = os.environ.get('SECRET_KEY', 'fallback-secret-key')

3. Add password hashing (bcrypt)
4. Use PostgreSQL for production database
5. Enable HTTPS (most platforms do this automatically)

## Troubleshooting

- If deployment fails, check the build logs
- Ensure requirements.txt has correct versions
- Make sure Procfile has no file extension
- Verify Python version compatibility (3.8+)

## Making Updates

After making changes:
1. git add .
2. git commit -m "Description of changes"
3. git push origin main
4. Deployment platforms will auto-deploy the changes
