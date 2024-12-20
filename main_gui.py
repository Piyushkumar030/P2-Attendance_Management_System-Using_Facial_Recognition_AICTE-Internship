import tkinter as tk
from tkinter import messagebox
import sqlite3
from attendance_capture import capture_attendance

# Connect to the SQLite database
def connect_db():
    return sqlite3.connect('user.db')

# Registration Function
def register():
    username = username_entry.get()
    password = password_entry.get()
    
    if not username or not password:
        messagebox.showerror("Error", "Username and Password are required!")
        return
    
    conn = connect_db()
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Success", "Registration successful!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists.")
    finally:
        conn.close()

# Login Function
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        messagebox.showinfo("Success", "Login successful!")
        open_main_window(user[0])
    else:
        messagebox.showerror("Error", "Invalid credentials.")

# Open Main Window After Login
def open_main_window(user_id):
    root.destroy()
    main_window = tk.Tk()
    main_window.title("Attendance Management System")
    main_window.geometry("800x600")
    
    from PIL import Image, ImageTk
    bg = Image.open("bg.jpg").resize((800, 600))
    bg_image = ImageTk.PhotoImage(bg)
    canvas = tk.Canvas(main_window, width=800, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=bg_image)
    
    mark_attendance_button = tk.Button(main_window, text="Mark Today's Attendance", font=("Arial", 14),
                                        command=lambda: capture_attendance(user_id))
    view_history_button = tk.Button(main_window, text="View Attendance History", font=("Arial", 14),
                                     command=lambda: view_attendance_history(user_id))
    
    canvas.create_window(400, 250, window=mark_attendance_button)
    canvas.create_window(400, 300, window=view_history_button)
    
    main_window.mainloop()

# View Attendance History
def view_attendance_history(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT date, time FROM attendance WHERE user_id = ?", (user_id,))
    records = cursor.fetchall()
    conn.close()
    
    history_window = tk.Toplevel()
    history_window.title("Attendance History")
    history_window.geometry("400x300")
    
    for record in records:
        tk.Label(history_window, text=f"Date: {record[0]}, Time: {record[1]}").pack()

# GUI Setup
root = tk.Tk()
root.title("Attendance Management System")
root.geometry("800x600")

from PIL import Image, ImageTk
bg = Image.open("bg.jpg").resize((800, 600))
bg_image = ImageTk.PhotoImage(bg)
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor="nw", image=bg_image)

tk.Label(root, text="Username:", font=("Arial", 14)).place(x=250, y=200)
username_entry = tk.Entry(root, font=("Arial", 14))
username_entry.place(x=350, y=200)

tk.Label(root, text="Password:", font=("Arial", 14)).place(x=250, y=250)
password_entry = tk.Entry(root, font=("Arial", 14), show="*")
password_entry.place(x=350, y=250)

register_button = tk.Button(root, text="Register", font=("Arial", 14), command=register)
register_button.place(x=300, y=300)

login_button = tk.Button(root, text="Login", font=("Arial", 14), command=login)
login_button.place(x=400, y=300)

root.mainloop()
