# Library Management System

A full-stack web application for managing library operations including book cataloging, user management, book issuance, and returns with automated fine calculation.

## Features

### For All Users
- User registration and authentication
- Browse and search books by title, author, or category
- Issue available books
- View issued books
- Return books with automatic fine calculation ($5/day for late returns)

### For Admin Users
- Add, edit, and delete books
- Manage user accounts
- View comprehensive reports
  - Popular books statistics
  - Recent activity logs
- Access dashboard with real-time statistics

## Tech Stack

- **Backend**: Python Flask
- **Database**: SQLite
- **Frontend**: HTML, CSS, Bootstrap 5
- **Icons**: Bootstrap Icons

## Installation

### Local Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/library-management-system.git
cd library-management-system
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to `http://127.0.0.1:5000`

6. Login with default admin credentials:
   - Username: `admin`
   - Password: `admin123`

## Deployment

### Deploy to Render

1. Push your code to GitHub
2. Go to [Render](https://render.com) and create a new Web Service
3. Connect your GitHub repository
4. Use these settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. Deploy!

### Deploy to Railway

1. Push your code to GitHub
2. Go to [Railway](https://railway.app) and create a new project
3. Connect your GitHub repository
4. Railway will auto-detect the Procfile and deploy

### Deploy to Heroku

1. Install Heroku CLI
2. Login: `heroku login`
3. Create app: `heroku create your-app-name`
4. Push: `git push heroku main`

## Project Structure

```
library-management-system/
 app.py                 # Main application file
 library.db            # SQLite database (auto-generated)
 requirements.txt      # Python dependencies
 Procfile             # Deployment configuration
 .gitignore           # Git ignore rules
 templates/           # HTML templates
    base.html
    login.html
    register.html
    dashboard.html
    books.html
    add_book.html
    edit_book.html
    my_books.html
    users.html
    reports.html
 static/              # Static files (CSS, JS, images)
```

## Database Schema

### Users Table
- user_id (Primary Key)
- username (Unique)
- password
- role (admin/student)
- email

### Books Table
- book_id (Primary Key)
- title
- author
- category
- status (Available/Issued)

### Issued Books Table
- issue_id (Primary Key)
- book_id (Foreign Key)
- user_id (Foreign Key)
- issue_date
- due_date
- return_date
- fine

## Features in Detail

### Book Management
- Add new books with title, author, and category
- Edit existing book information
- Delete books from the system
- Track book availability status

### User Management
- User registration with email validation
- Role-based access control (Admin/Student)
- Admin can manage all user accounts

### Issuance System
- Books issued for 14-day period
- Automatic due date calculation
- Real-time availability tracking
- Fine calculation: $5 per day for late returns

### Reports & Analytics
- Most popular books by issue count
- Recent activity timeline
- User statistics
- Book availability metrics

## Security Features

- Password-protected authentication
- Session management
- Role-based access control
- SQL injection prevention using parameterized queries

## Future Enhancements

- [ ] Email notifications for due dates
- [ ] Book reservation system
- [ ] Advanced search filters
- [ ] Export reports to PDF/Excel
- [ ] Book cover images
- [ ] Reading history
- [ ] Book recommendations
- [ ] Mobile responsive design improvements
- [ ] Password hashing (bcrypt)
- [ ] API endpoints for mobile app

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Your Name - [GitHub Profile](https://github.com/YOUR_USERNAME)

## Acknowledgments

- Bootstrap for UI components
- Flask documentation and community
- All the amazing open-source contributors
