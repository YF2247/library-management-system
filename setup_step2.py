import os
base = r"C:\Users\owusu\Documents\LibraryManagementSystem\templates"
t = {}
t["books.html"] = """{% extends "base.html" %}
{% block content %}
<div class="d-flex justify-content-between mb-4">
    <h2>Books</h2>
    {% if session.role == 'admin' %}
    <a href="{{ url_for('add_book') }}" class="btn btn-primary">Add Book</a>
    {% endif %}
</div>
<form method="GET" class="mb-4">
    <div class="input-group">
        <input type="text" class="form-control" name="search" placeholder="Search" value="{{ search }}">
        <button class="btn btn-outline-secondary" type="submit">Search</button>
    </div>
</form>
<table class="table table-striped">
    <thead>
        <tr><th>ID</th><th>Title</th><th>Author</th><th>Category</th><th>Status</th><th>Actions</th></tr>
    </thead>
    <tbody>
        {% for book in books %}
        <tr>
            <td>{{ book.book_id }}</td>
            <td>{{ book.title }}</td>
            <td>{{ book.author }}</td>
            <td>{{ book.category }}</td>
            <td><span class="badge bg-{% if book.status == 'Available' %}success{% else %}warning{% endif %}">{{ book.status }}</span></td>
            <td>
                {% if session.role == 'admin' %}
                <a href="{{ url_for('edit_book', book_id=book.book_id) }}" class="btn btn-sm btn-warning">Edit</a>
                <a href="{{ url_for('delete_book', book_id=book.book_id) }}" class="btn btn-sm btn-danger" onclick="return confirm('Delete?')">Delete</a>
                {% endif %}
                {% if book.status == 'Available' %}
                <form method="POST" action="{{ url_for('issue_book', book_id=book.book_id) }}" style="display:inline;">
                    <button type="submit" class="btn btn-sm btn-success">Issue</button>
                </form>
                {% endif %}
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}"""

t["add_book.html"] = """{% extends "base.html" %}
{% block content %}
<h2 class="mb-4">Add Book</h2>
<div class="row">
    <div class="col-md-6">
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
            <button type="submit" class="btn btn-primary">Add Book</button>
            <a href="{{ url_for('books') }}" class="btn btn-secondary">Cancel</a>
        </form>
    </div>
</div>
{% endblock %}"""

t["edit_book.html"] = """{% extends "base.html" %}
{% block content %}
<h2 class="mb-4">Edit Book</h2>
<div class="row">
    <div class="col-md-6">
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
    </div>
</div>
{% endblock %}"""

t["my_books.html"] = """{% extends "base.html" %}
{% block content %}
<h2 class="mb-4">My Issued Books</h2>
<table class="table table-striped">
    <thead>
        <tr><th>Title</th><th>Author</th><th>Issue Date</th><th>Due Date</th><th>Actions</th></tr>
    </thead>
    <tbody>
        {% for book in issued_books %}
        <tr>
            <td>{{ book.title }}</td>
            <td>{{ book.author }}</td>
            <td>{{ book.issue_date }}</td>
            <td>{{ book.due_date }}</td>
            <td><a href="{{ url_for('return_book', issue_id=book.issue_id) }}" class="btn btn-sm btn-primary">Return</a></td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}"""

t["users.html"] = """{% extends "base.html" %}
{% block content %}
<h2 class="mb-4">Users</h2>
<table class="table table-striped">
    <thead>
        <tr><th>ID</th><th>Username</th><th>Email</th><th>Role</th><th>Actions</th></tr>
    </thead>
    <tbody>
        {% for user in users %}
        <tr>
            <td>{{ user.user_id }}</td>
            <td>{{ user.username }}</td>
            <td>{{ user.email }}</td>
            <td><span class="badge bg-info">{{ user.role }}</span></td>
            <td>
                {% if user.user_id != session.user_id %}
                <a href="{{ url_for('delete_user', user_id=user.user_id) }}" class="btn btn-sm btn-danger" onclick="return confirm('Delete?')">Delete</a>
                {% endif %}
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}"""

t["reports.html"] = """{% extends "base.html" %}
{% block content %}
<h2 class="mb-4">Reports</h2>
<div class="row">
    <div class="col-md-6">
        <h4>Popular Books</h4>
        <table class="table table-sm">
            <thead><tr><th>Title</th><th>Author</th><th>Issues</th></tr></thead>
            <tbody>
                {% for book in popular_books %}
                <tr><td>{{ book.title }}</td><td>{{ book.author }}</td><td>{{ book.cnt }}</td></tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
    <div class="col-md-6">
        <h4>Recent Activity</h4>
        <table class="table table-sm">
            <thead><tr><th>User</th><th>Book</th><th>Issue Date</th><th>Status</th></tr></thead>
            <tbody>
                {% for activity in recent_activity %}
                <tr>
                    <td>{{ activity.username }}</td>
                    <td>{{ activity.title }}</td>
                    <td>{{ activity.issue_date }}</td>
                    <td><span class="badge bg-{% if activity.return_date %}success{% else %}warning{% endif %}">{% if activity.return_date %}Returned{% else %}Issued{% endif %}</span></td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</div>
{% endblock %}"""

for name, content in t.items():
    with open(os.path.join(base, name), 'w') as f:
        f.write(content)
    print(f"Created: {name}")
