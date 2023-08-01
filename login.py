import tkinter as tk
import psycopg2
from tkinter import messagebox

def get_connection():
    # Повертає з'єднання з базою даних
    conn = psycopg2.connect(
        database="your_database",
        user="your_username",
        password="your_password",
        host="your_addres",
        port="default_5432",
        sslmode='disable'
    )
    return conn

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Підключення до бази даних
    conn = get_connection()

    # Перевірка довжини логіну та паролю
    if len(username) < 4 or len(password) < 5:
        messagebox.showerror("Помилка", "Логін повинен мати мінімум 4 символа, а пароль - мінімум 5 символів!")
        return

    # Ваша логіка перевірки авторизації з використанням бази даних

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result is not None:
        messagebox.showinfo("Успіх", "Авторизація пройшла успішно!")
    else:
        messagebox.showerror("Помилка", "Невірний логін або пароль!")

# Перевірка, чи логін вже існує в базі даних
def check_unique_login(username):
    conn = get_connection()

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    return result is None


def register():
    username = entry_username.get()
    password = entry_password.get()

    # Підключення до бази даних
    conn = get_connection()
    # Перевірка довжини логіну та паролю
    if len(username) < 4 or len(password) < 5:
        messagebox.showerror("Помилка", "Логін повинен мати мінімум 4 символа, а пароль - мінімум 5 символів!")
        return

     # Перевірка унікальності логіну
    if not check_unique_login(username):
        messagebox.showerror("Помилка", "Користувач з таким логіном вже існує!")
        return

    # Перевірка на розмір букв у логіні
    if not username.islower():
        messagebox.showerror("Помилка", "Логін повинен складатися з малих літер!")
        return

    # Ваша логіка реєстрації з використанням бази даних

    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    cursor.close()
    conn.close()

    messagebox.showinfo("Успіх", "Ви успішно зареєстровані!")

# Створення головного вікна
root = tk.Tk()
root.title("Авторизація - Реєстрація")
root.geometry("250x150") 
root.resizable(width=False, height=False)
root.configure(bg="gray")  # Задній фон сірий

# Елементи інтерфейсу
label_username = tk.Label(root, text="Логін:", bg="gray", fg="white")  # Текст білим
label_password = tk.Label(root, text="Пароль:", bg="gray", fg="white")  # Текст білим
entry_username = tk.Entry(root, bg="black", fg="white")  # Поле для вводу чорне
entry_password = tk.Entry(root, show="*", bg="black", fg="white")  # Поле для вводу чорне

# Кнопка Увійти
button_login = tk.Button(root, text="Увійти", bg="green", fg="white", activebackground="green", activeforeground="white", command=login)
# Кнопка Зареєструватися
button_register = tk.Button(root, text="Зареєструватися", bg="blue", fg="white", activebackground="blue", activeforeground="white", command=register)

# Розміщення елементів
label_username.pack()
entry_username.pack()
label_password.pack()
entry_password.pack()
button_login.pack(pady=3)  # Відступ між кнопками
button_register.pack(pady=2)  # Відступ між кнопками

# Запуск головного циклу
root.mainloop()