import sqlite3

# Connect to the database
conn = sqlite3.connect(r"C:\Users\owusu\Documents\LibraryManagementSystem\library.db")
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL,
    email VARCHAR(255))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    category VARCHAR(100),
    status VARCHAR(50) DEFAULT 'Available')''')

cursor.execute('''CREATE TABLE IF NOT EXISTS issued_books (
    issue_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    user_id INTEGER,
    issue_date DATE,
    due_date DATE,
    return_date DATE,
    fine DECIMAL(10,2) DEFAULT 0,
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id))''')

# Add admin user if not exists
cursor.execute("SELECT * FROM users WHERE username='admin'")
if not cursor.fetchone():
    cursor.execute("INSERT INTO users VALUES (NULL, 'admin', 'admin123', 'admin', 'admin@library.com')")

# Self-Help Books
self_help_books = [
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
    ("The 5 AM Club", "Robin Sharma", "Self-Help")
]

# Financial Literacy Books
finance_books = [
    ("Rich Dad Poor Dad", "Robert Kiyosaki", "Financial Literacy"),
    ("The Total Money Makeover", "Dave Ramsey", "Financial Literacy"),
    ("The Intelligent Investor", "Benjamin Graham", "Financial Literacy"),
    ("Think and Grow Rich", "Napoleon Hill", "Financial Literacy"),
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

# Insert books
all_books = self_help_books + finance_books

for title, author, category in all_books:
    # Check if book already exists
    cursor.execute("SELECT * FROM books WHERE title=? AND author=?", (title, author))
    if not cursor.fetchone():
        cursor.execute("INSERT INTO books VALUES (NULL, ?, ?, ?, 'Available')", (title, author, category))
        print(f"Added: {title} by {author}")
    else:
        print(f"Already exists: {title}")

conn.commit()
conn.close()

print(f"\n Successfully added {len(all_books)} books!")
print(f"  - {len(self_help_books)} Self-Help books")
print(f"  - {len(finance_books)} Financial Literacy books")
print("\nDatabase updated at: C:\\Users\\owusu\\Documents\\LibraryManagementSystem\\library.db")
