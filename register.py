#!/usr/bin/env python3

import cgi
import html
import pymysql

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()
email = form.getfirst("email", "").strip()
password = form.getfirst("password", "")

print("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Register Result</title>
</head>
<body>""")

if email == "" or password == "":
    print("<h1>Registration failed</h1>")
    print("<p>Email and password are required.</p>")
    print('<p><a href="register.html">Back to Register</a></p>')
    print("</body></html>")
    raise SystemExit

try:
    conn = pymysql.connect(
        host="localhost",
        user="spectre_user",
        password="555555555",
        database="spectre_db"
    )

    cursor = conn.cursor()

    check_sql = "SELECT id FROM users WHERE email = %s"
    cursor.execute(check_sql, (email,))
    existing_user = cursor.fetchone()

    if existing_user is not None:
        print("<h1>Registration failed</h1>")
        print("<p>Email already exists.</p>")
        print('<p><a href="register.html">Back to Register</a></p>')
    else:
        insert_sql = "INSERT INTO users (email, password_hash) VALUES (%s, %s)"
        cursor.execute(insert_sql, (email, password))
        conn.commit()

        print("<h1>Registration successful</h1>")
        print("<p>Your account has been created.</p>")
        print('<p><a href="login.html">Go to Login</a></p>')

    cursor.close()
    conn.close()

except Exception as e:
    print("<h1>Registration failed</h1>")
    print(f"<pre>{html.escape(str(e))}</pre>")
    print('<p><a href="register.html">Back to Register</a></p>')

print("</body></html>")