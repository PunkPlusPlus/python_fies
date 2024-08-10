import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

connection.commit()
connection.close()