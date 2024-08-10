#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('./data.db')
cursor = connection.cursor()
cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()
connection.close()

markup = ""

for user in users:
    markup += f"<p><b>{user[0]}</b>: {user[1]}</p>"


print(
    f"""\
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<body>
<h1>Hello, World!</h1>
<br>
{markup}
</body>
</html>"""
)








