from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from datetime import datetime, timedelta
from functools import wraps
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'library-secret-key-2025')

def init_db():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(255) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        role VARCHAR(50) NOT NULL,
        email VARCHAR(255))''')
    c.execute('''CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL,
        category VARCHAR(100),
        status VARCHAR(50) DEFAULT 'Available')''')
    c.execute('''CREATE TABLE IF NOT EXISTS issued_books (
        issue_id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER,
        user_id INTEGER,
        issue_date DATE,
        due_date DATE,
        return_date DATE,
        fine DECIMAL(10,2) DEFAULT 0,
        FOREIGN KEY (book_id) REFERENCES books(book_id),
        FOREIGN KEY (user_id) REFERENCES users(user_id))''')
    
    # Insert default admin
    c.execute("SELECT * FROM users WHERE username='admin'")
    if not c.fetchone():
        c.execute("INSERT INTO users VALUES (NULL, 'admin', 'admin123', 'admin', 'admin@library.com')")
    
    # Check if books already exist
    c.execute("SELECT COUNT(*) as count FROM books")
    book_count = c.fetchone()[0]
    
    # If no books exist, add sample books
    if book_count == 0:
        sample_books = [
            # Self-Help Books
            ("Atomic Habits", "James Clear", "Self-Help"),
            ("The 7 Habits of Highly Effective People", "Stephen Covey", "Self-Help"),
            ("How to Win Friends and Influence People", "Dale Carnegie", "Self-Help"),
            ("The Power of Now", "Eckhart Tolle", "Self-Help"),
            ("Think and Grow Rich", "Napoleon Hill", "Self-Help"),
            ("The Subtle Art of Not Giving a F*ck", "Mark Manson", "Self-Help"),
            ("You Are a Badass", "Jen Sincero", "Self-Help"),
            ("The Four Agreements", "Don Miguel Ruiz", "Self-Help"),
            ("Mindset: The New Psychology of Success", "Carol Dweck", "Self-Help"),
            ("Daring Greatly", "Brené Brown", "Self-Help"),
            ("The Miracle Morning", "Hal Elrod", "Self-Help"),
            ("Can't Hurt Me", "David Goggins", "Self-Help"),
            ("The Alchemist", "Paulo Coelho", "Self-Help"),
            ("Man's Search for Meaning", "Viktor Frankl", "Self-Help"),
            ("The 5 AM Club", "Robin Sharma", "Self-Help"),
            
            # Financial Literacy Books
            ("Rich Dad Poor Dad", "Robert Kiyosaki", "Financial Literacy"),
            ("The Total Money Makeover", "Dave Ramsey", "Financial Literacy"),
            ("The Intelligent Investor", "Benjamin Graham", "Financial Literacy"),
            ("The Millionaire Next Door", "Thomas Stanley", "Financial Literacy"),
            ("Your Money or Your Life", "Vicki Robin", "Financial Literacy"),
            ("The Richest Man in Babylon", "George Clason", "Financial Literacy"),
            ("I Will Teach You to Be Rich", "Ramit Sethi", "Financial Literacy"),
            ("The Simple Path to Wealth", "JL Collins", "Financial Literacy"),
            ("Money Master the Game", "Tony Robbins", "Financial Literacy"),
            ("The Psychology of Money", "Morgan Housel", "Financial Literacy"),
            ("Broke Millennial", "Erin Lowry", "Financial Literacy"),
            ("The Automatic Millionaire", "David Bach", "Financial Literacy"),
            ("Unshakeable", "Tony Robbins", "Financial Literacy"),
            ("The Little Book of Common Sense Investing", "John Bogle", "Financial Literacy"),
            ("Financial Freedom", "Grant Sabatier", "Financial Literacy"),
            ("The Index Card", "Helaine Olen", "Financial Literacy"),
            ("Get Good with Money", "Tiffany Aliche", "Financial Literacy")
        ]
        
        for title, author, category in sample_books:
            c.execute("INSERT INTO books VALUES (NULL, ?, ?, ?, 'Available')", (title, author, category))
        
        print(f" Added {len(sample_books)} sample books to the database")
    
    conn.commit()
    conn.close()

# Initialize database on startup
init_db()

def get_db():
    conn = sqlite3.connect('library.db')
    conn.row_factory = sqlite3.Row
    return conn

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'role' not in session or session['role'] != 'admin':
            flash('Admin access required')
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        conn = get_db()
        user = conn.execute('SELECT * FROM users WHERE username=? AND password=?',
                           (request.form['username'], request.form['password'])).fetchone()
        conn.close()
        if user:
            session['user_id'] = user['user_id']
            session['username'] = user['username']
            session['role'] = user['role']
            return redirect(url_for('dashboard'))
        flash('Invalid credentials')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        conn = get_db()
        try:
            conn.execute('INSERT INTO users VALUES (NULL, ?, ?, ?, ?)',
                        (request.form['username'], request.form['password'], 'student', request.form['email']))
            conn.commit()
            flash('Registration successful!')
            return redirect(url_for('login'))
        except:
            flash('Username exists')
        finally:
            conn.close()
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    conn = get_db()
    stats = {
        'total_books': conn.execute('SELECT COUNT(*) as c FROM books').fetchone()['c'],
        'available': conn.execute('SELECT COUNT(*) as c FROM books WHERE status="Available"').fetchone()['c'],
        'issued': conn.execute('SELECT COUNT(*) as c FROM issued_books WHERE return_date IS NULL').fetchone()['c'],
        'users': conn.execute('SELECT COUNT(*) as c FROM users').fetchone()['c']
    }
    conn.close()
    return render_template('dashboard.html', **stats)

@app.route('/books')
@login_required
def books():
    search = request.args.get('search', '')
    conn = get_db()
    if search:
        books = conn.execute('SELECT * FROM books WHERE title LIKE ? OR author LIKE ?',
                            (f'%{search}%', f'%{search}%')).fetchall()
    else:
        books = conn.execute('SELECT * FROM books').fetchall()
    conn.close()
    return render_template('books.html', books=books, search=search)

@app.route('/books/add', methods=['GET', 'POST'])
@login_required
@admin_required
def add_book():
    if request.method == 'POST':
        conn = get_db()
        conn.execute('INSERT INTO books VALUES (NULL, ?, ?, ?, ?)',
                    (request.form['title'], request.form['author'], request.form['category'], 'Available'))
        conn.commit()
        conn.close()
        flash('Book added')
        return redirect(url_for('books'))
    return render_template('add_book.html')

@app.route('/books/edit/<int:book_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_book(book_id):
    conn = get_db()
    if request.method == 'POST':
        conn.execute('UPDATE books SET title=?, author=?, category=? WHERE book_id=?',
                    (request.form['title'], request.form['author'], request.form['category'], book_id))
        conn.commit()
        conn.close()
        flash('Book updated')
        return redirect(url_for('books'))
    book = conn.execute('SELECT * FROM books WHERE book_id=?', (book_id,)).fetchone()
    conn.close()
    return render_template('edit_book.html', book=book)

@app.route('/books/delete/<int:book_id>')
@login_required
@admin_required
def delete_book(book_id):
    conn = get_db()
    conn.execute('DELETE FROM books WHERE book_id=?', (book_id,))
    conn.commit()
    conn.close()
    flash('Book deleted')
    return redirect(url_for('books'))

@app.route('/books/issue/<int:book_id>', methods=['POST'])
@login_required
def issue_book(book_id):
    conn = get_db()
    book = conn.execute('SELECT * FROM books WHERE book_id=? AND status="Available"', (book_id,)).fetchone()
    if book:
        issue_date = datetime.now().date()
        due_date = issue_date + timedelta(days=14)
        conn.execute('INSERT INTO issued_books VALUES (NULL, ?, ?, ?, ?, NULL, 0)',
                    (book_id, session['user_id'], issue_date, due_date))
        conn.execute('UPDATE books SET status="Issued" WHERE book_id=?', (book_id,))
        conn.commit()
        flash('Book issued')
    else:
        flash('Book not available')
    conn.close()
    return redirect(url_for('books'))

@app.route('/my-books')
@login_required
def my_books():
    conn = get_db()
    issued = conn.execute('''SELECT ib.*, b.title, b.author FROM issued_books ib
                            JOIN books b ON ib.book_id = b.book_id
                            WHERE ib.user_id=? AND ib.return_date IS NULL''',
                         (session['user_id'],)).fetchall()
    conn.close()
    return render_template('my_books.html', issued_books=issued)

@app.route('/books/return/<int:issue_id>')
@login_required
def return_book(issue_id):
    conn = get_db()
    issue = conn.execute('SELECT * FROM issued_books WHERE issue_id=?', (issue_id,)).fetchone()
    if issue:
        return_date = datetime.now().date()
        due_date = datetime.strptime(issue['due_date'], '%Y-%m-%d').date()
        fine = max(0, (return_date - due_date).days * 5)
        conn.execute('UPDATE issued_books SET return_date=?, fine=? WHERE issue_id=?',
                    (return_date, fine, issue_id))
        conn.execute('UPDATE books SET status="Available" WHERE book_id=?', (issue['book_id'],))
        conn.commit()
        flash(f'Book returned. Fine: ${fine}' if fine > 0 else 'Book returned')
    conn.close()
    return redirect(url_for('my_books'))

@app.route('/users')
@login_required
@admin_required
def users():
    conn = get_db()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('users.html', users=users)

@app.route('/users/delete/<int:user_id>')
@login_required
@admin_required
def delete_user(user_id):
    if user_id == session['user_id']:
        flash('Cannot delete own account')
        return redirect(url_for('users'))
    conn = get_db()
    conn.execute('DELETE FROM users WHERE user_id=?', (user_id,))
    conn.commit()
    conn.close()
    flash('User deleted')
    return redirect(url_for('users'))

@app.route('/reports')
@login_required
@admin_required
def reports():
    conn = get_db()
    popular = conn.execute('''SELECT b.title, b.author, COUNT(ib.issue_id) as cnt
                             FROM books b LEFT JOIN issued_books ib ON b.book_id = ib.book_id
                             GROUP BY b.book_id ORDER BY cnt DESC LIMIT 10''').fetchall()
    recent = conn.execute('''SELECT u.username, b.title, ib.issue_date, ib.return_date
                            FROM issued_books ib JOIN users u ON ib.user_id = u.user_id
                            JOIN books b ON ib.book_id = b.book_id
                            ORDER BY ib.issue_date DESC LIMIT 10''').fetchall()
    conn.close()
    return render_template('reports.html', popular_books=popular, recent_activity=recent)

if __name__ == '__main__':
    app.run(debug=True)
