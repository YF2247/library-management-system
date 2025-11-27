import os

base = r"C:\Users\owusu\Documents\LibraryManagementSystem"
templates = os.path.join(base, "templates")

# Create base.html
with open(os.path.join(templates, "base.html"), "w") as f:
    f.write("""<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Library System{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    {% if session.user_id %}
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container-fluid">
            <a class="navbar-brand" href="{{ url_for('dashboard') }}">Library System</a>
            <div class="collapse navbar-collapse">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item"><a class="nav-link" href="{{ url_for('dashboard') }}">Dashboard</a></li>
                    <li class="nav-item"><a class="nav-link" href="{{ url_for('books') }}">Books</a></li>
                    <li class="nav-item"><a class="nav-link" href="{{ url_for('my_books') }}">My Books</a></li>
                    {% if session.role == 'admin' %}
                    <li class="nav-item"><a class="nav-link" href="{{ url_for('users') }}">Users</a></li>
                    <li class="nav-item"><a class="nav-link" href="{{ url_for('reports') }}">Reports</a></li>
                    {% endif %}
                </ul>
                <ul class="navbar-nav">
                    <li class="nav-item"><span class="navbar-text me-3">{{ session.username }}</span></li>
                    <li class="nav-item"><a class="nav-link" href="{{ url_for('logout') }}">Logout</a></li>
                </ul>
            </div>
        </div>
    </nav>
    {% endif %}
    <div class="container mt-4">
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                {% for message in messages %}
                <div class="alert alert-info">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        {% block content %}{% endblock %}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>""")

# Create login.html
with open(os.path.join(templates, "login.html"), "w") as f:
    f.write("""{% extends "base.html" %}
{% block content %}
<div class="row justify-content-center mt-5">
    <div class="col-md-4">
        <div class="card">
            <div class="card-body">
                <h3 class="text-center">Library System Login</h3>
                <form method="POST">
                    <div class="mb-3">
                        <label>Username</label>
                        <input type="text" class="form-control" name="username" required>
                    </div>
                    <div class="mb-3">
                        <label>Password</label>
                        <input type="password" class="form-control" name="password" required>
                    </div>
                    <button type="submit" class="btn btn-primary w-100">Login</button>
                </form>
                <div class="text-center mt-3">
                    <a href="{{ url_for('register') }}">Register</a>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}""")

# Create register.html
with open(os.path.join(templates, "register.html"), "w") as f:
    f.write("""{% extends "base.html" %}
{% block content %}
<div class="row justify-content-center mt-5">
    <div class="col-md-4">
        <div class="card">
            <div class="card-body">
                <h3 class="text-center">Register</h3>
                <form method="POST">
                    <div class="mb-3">
                        <label>Username</label>
                        <input type="text" class="form-control" name="username" required>
                    </div>
                    <div class="mb-3">
                        <label>Email</label>
                        <input type="email" class="form-control" name="email" required>
                    </div>
                    <div class="mb-3">
                        <label>Password</label>
                        <input type="password" class="form-control" name="password" required>
                    </div>
                    <button type="submit" class="btn btn-primary w-100">Register</button>
                </form>
                <div class="text-center mt-3">
                    <a href="{{ url_for('login') }}">Login</a>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}""")

# Create dashboard.html
with open(os.path.join(templates, "dashboard.html"), "w") as f:
    f.write("""{% extends "base.html" %}
{% block content %}
<h2>Dashboard</h2>
<div class="row mt-4">
    <div class="col-md-3">
        <div class="card text-white bg-primary">
            <div class="card-body">
                <h5>Total Books</h5>
                <h2>{{ total_books }}</h2>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card text-white bg-success">
            <div class="card-body">
                <h5>Available</h5>
                <h2>{{ available_books }}</h2>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card text-white bg-warning">
            <div class="card-body">
                <h5>Issued</h5>
                <h2>{{ issued_books }}</h2>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card text-white bg-info">
            <div class="card-body">
                <h5>Users</h5>
                <h2>{{ total_users }}</h2>
            </div>
        </div>
    </div>
</div>
{% endblock %}""")

# Create books.html
with open(os.path.join(templates, "books.html"), "w") as f:
    f.write("""{% extends "base.html" %}
{% block content %}
<div class="d-flex justify-content-between mb-3">
    <h2>Books</h2>
    {% if session.role == 'admin' %}
    <a href="{{ url_for('add_book') }}" class="btn btn-primary">Add Book</a>
    {% endif %}
</div>
<form method="GET" class="mb-3">
    <div class="input-group">
        <input type="text" class="form-control" name="search" placeholder="Search" value="{{ search }}">
        <button class="btn btn-secondary" type="submit">Search</button>
    </div>
</form>
<table class="table">
    <thead>
        <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Author</th>
            <th>Category</th>
            <th>Status</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {% for book in books %}
        <tr>
            <td>{{ book.book_id }}</td>
            <td>{{ book.title }}</td>
            <td>{{ book.author }}</td>
            <td>{{ book.category }}</td>
            <td><span class="badge bg-{{ 'success' if book.status == 'Available' else 'warning' }}">{{ book.status }}</span></td>
            <td>
                {% if session.role == 'admin' %}
                <a href="{{ url_for('edit_book', book_id=book.book_id) }}" class="btn btn-sm btn-warning">Edit</a>
                <a href="{{ url_for('delete_book', book_id=book.book_id) }}" class="btn btn-sm btn-danger" onclick="return confirm('Delete?')">Delete</a>
                {% endif %}
                {% if book.status == 'Available' %}
                <form method="POST" action="{{ url_for('issue_book', book_id=book.book_id) }}" style="display:inline">
                    <button class="btn btn-sm btn-success">Issue</button>
                </form>
                {% endif %}
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}""")

# Create add_book.html
with open(os.path.join(templates, "add_book.html"), "w") as f:
    f.write("""{% extends "base.html" %}
{% block content %}
<h2>Add Book</h2>
<form method="POST">
    <div class="mb-3">
        <label>Title</label>
        <input type="text" class="form-control" name="title" required>
    </div>
    <div class="mb-3">
        <label>Author</label>
        <input type="text" class="form-control" name="author" required>
    </div>
    <div class="mb-3">
        <label>Category</label>
        <input type="text" class="form-control" name="category" required>
    </div>
    <button type="submit" class="btn btn-primary">Add</button>
    <a href="{{ url_for('books') }}" class="btn btn-secondary">Cancel</a>
</form>
{% endblock %}""")

# Create edit_book.html
with open(os.path.join(templates, "edit_book.html"), "w") as f:
    f.write("""{% extends "base.html" %}
{% block content %}
<h2>Edit Book</h2>
<form method="POST">
    <div class="mb-3">
        <label>Title</label>
        <input type="text" class="form-control" name="title" value="{{ book.title }}" required>
    </div>
    <div class="mb-3">
        <label>Author</label>
        <input type="text" class="form-control" name="author" value="{{ book.author }}" required>
    </div>
    <div class="mb-3">
        <label>Category</label>
        <input type="text" class="form-control" name="category" value="{{ book.category }}" required>
    </div>
    <button type="submit" class="btn btn-primary">Update</button>
    <a href="{{ url_for('books') }}" class="btn btn-secondary">Cancel</a>
</form>
{% endblock %}""")

# Create my_books.html
with open(os.path.join(templates, "my_books.html"), "w") as f:
    f.write("""{% extends "base.html" %}
{% block content %}
<h2>My Issued Books</h2>
<table class="table">
    <thead>
        <tr>
            <th>Title</th>
            <th>Author</th>
            <th>Issue Date</th>
            <th>Due Date</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {% for book in issued_books %}
        <tr>
            <td>{{ book.title }}</td>
            <td>{{ book.author }}</td>
            <td>{{ book.issue_date }}</td>
            <td>{{ book.due_date }}</td>
            <td>
                <a href="{{ url_for('return_book', issue_id=book.issue_id) }}" class="btn btn-sm btn-primary">Return</a>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}""")

# Create users.html
with open(os.path.join(templates, "users.html"), "w") as f:
    f.write("""{% extends "base.html" %}
{% block content %}
<h2>Users</h2>
<table class="table">
    <thead>
        <tr>
            <th>ID</th>
            <th>Username</th>
            <th>Email</th>
            <th>Role</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {% for user in users %}
        <tr>
            <td>{{ user.user_id }}</td>
            <td>{{ user.username }}</td>
            <td>{{ user.email }}</td>
            <td>{{ user.role }}</td>
            <td>
                {% if user.user_id != session.user_id %}
                <a href="{{ url_for('delete_user', user_id=user.user_id) }}" class="btn btn-sm btn-danger" onclick="return confirm('Delete?')">Delete</a>
                {% endif %}
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}""")

# Create reports.html
with open(os.path.join(templates, "reports.html"), "w") as f:
    f.write("""{% extends "base.html" %}
{% block content %}
<h2>Reports</h2>
<div class="row">
    <div class="col-md-6">
        <h4>Popular Books</h4>
        <table class="table table-sm">
            <thead>
                <tr>
                    <th>Title</th>
                    <th>Author</th>
                    <th>Issues</th>
                </tr>
            </thead>
            <tbody>
                {% for book in popular_books %}
                <tr>
                    <td>{{ book.title }}</td>
                    <td>{{ book.author }}</td>
                    <td>{{ book.issue_count }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
    <div class="col-md-6">
        <h4>Recent Activity</h4>
        <table class="table table-sm">
            <thead>
                <tr>
                    <th>User</th>
                    <th>Book</th>
                    <th>Date</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                {% for activity in recent_activity %}
                <tr>
                    <td>{{ activity.username }}</td>
                    <td>{{ activity.title }}</td>
                    <td>{{ activity.issue_date }}</td>
                    <td>{{ 'Returned' if activity.return_date else 'Issued' }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</div>
{% endblock %}""")

print("All template files created successfully!")
print(f"Location: {templates}")
print("\nYou can now run: python app.py")
