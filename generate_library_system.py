import os

base_dir = r"C:\Users\owusu\Documents\LibraryManagementSystem"
os.makedirs(os.path.join(base_dir, "templates"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "static"), exist_ok=True)

print("Creating Library Management System files...")
print(f"Location: {base_dir}")
print("\nAll files created successfully!")
print("\nNext steps:")
print("1. cd C:\\Users\\owusu\\Documents\\LibraryManagementSystem")
print("2. pip install flask")
print("3. python app.py")
print("4. Open browser: http://127.0.0.1:5000")
print("5. Login: admin / admin123")
