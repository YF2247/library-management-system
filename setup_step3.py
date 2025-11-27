import os
base = r"C:\Users\owusu\Documents\LibraryManagementSystem\templates"

templates = {
"base.html": """<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Library System{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css">
</head>
<body>
    {% if session.user_id %}
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container-fluid">
            <a class="navbar-brand" href="{{ url_for('dashboard') }}"><i class="bi bi-book"></i> Library</a>
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
                    <li class="nav-item"><span class="navbar-text me-3">{{ session.username }} ({{ session.role }})</span></li>
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
                <div class="alert alert-info alert-dismissible fade show">
                    {{ message }}
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                </div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        {% block content %}{% endblock %}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>""",

"login.html": """{% extends "base.html" %}
{% block content %}
<div class="row justify-content-center mt-5">
    <div class="col-md-4">
        <div class="card shadow">
            <div class="card-body">
                <h3 class="text-center mb-4"><i class="bi bi-book-fill"></i> Library System</h3>
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
{% endblock %}""",

"register.html": """{% extends "base.html" %}
{% block content %}
<div class="row justify-content-center mt-5">
    <div class="col-md-4">
        <div class="card shadow">
            <div class="card-body">
                <h3 class="text-center mb-4">Register</h3>
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
{% endblock %}""",

"dashboard.html": """{% extends "base.html" %}
{% block content %}
<h2 class="mb-4">Dashboard</h2>
<div class="row">
    <div class="col-md-3">
        <div class="card text-white bg-primary mb-3">
            <div class="card-body">
                <h5><i class="bi bi-book"></i> Total Books</h5>
                <h2>{{ total_books }}</h2>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card text-white bg-success mb-3">
            <div class="card-body">
                <h5><i class="bi bi-check-circle"></i> Available</h5>
                <h2>{{ available }}</h2>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card text-white bg-warning mb-3">
            <div class="card-body">
                <h5><i class="bi bi-arrow-right-circle"></i> Issued</h5>
                <h2>{{ issued }}</h2>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card text-white bg-info mb-3">
            <div class="card-body">
                <h5><i class="bi bi-people"></i> Users</h5>
                <h2>{{ users }}</h2>
            </div>
        </div>
    </div>
</div>
{% endblock %}"""
}

for name, content in templates.items():
    with open(os.path.join(base, name), 'w') as f:
        f.write(content)
    print(f"Created: {name}")

print("\n=== ALL FILES CREATED ===")
print("Location: C:\\Users\\owusu\\Documents\\LibraryManagementSystem")
print("\nTo run:")
print("1. cd C:\\Users\\owusu\\Documents\\LibraryManagementSystem")
print("2. python app.py")
print("3. Open browser: http://127.0.0.1:5000")
print("4. Login: admin / admin123")
