================================================================================
LIBRARY MANAGEMENT SYSTEM - SETUP COMPLETE!
================================================================================

PROJECT LOCATION:
C:\Users\owusu\Documents\LibraryManagementSystem

FILES CREATED:
 app.py (Main application)
 templates/base.html
 templates/login.html
 templates/register.html
 templates/dashboard.html
 templates/books.html
 templates/add_book.html
 templates/edit_book.html
 templates/my_books.html
 templates/users.html
 templates/reports.html

DEPENDENCIES INSTALLED:
 Flask 3.1.2

================================================================================
HOW TO RUN THE APPLICATION
================================================================================

OPTION 1 (Easiest):
-------------------
Double-click the file on your Desktop:
   RUN_LIBRARY_SYSTEM.bat

OPTION 2 (Manual):
------------------
1. Open Command Prompt
2. Run these commands:
   cd C:\Users\owusu\Documents\LibraryManagementSystem
   python app.py

3. Open your web browser and go to:
   http://127.0.0.1:5000

4. Login with default admin account:
   Username: admin
   Password: admin123

================================================================================
FEATURES AVAILABLE
================================================================================

FOR ALL USERS:
- Login/Register
- Browse books
- Search books by title, author, or category
- Issue available books
- View your issued books
- Return books (with automatic fine calculation)

FOR ADMIN USERS:
- Add new books
- Edit book details
- Delete books
- Manage users
- View reports (popular books, recent activity)
- Access dashboard with statistics

================================================================================
NOTES
================================================================================

- Books are issued for 14 days
- Late returns incur a fine of $5 per day
- The database (library.db) will be created automatically on first run
- All data is stored locally in SQLite database

================================================================================
