#!/usr/bin/env python3

import cgi
import html
import pymysql
import time

form = cgi.FieldStorage()
email = form.getfirst("email", "").strip()
password = form.getfirst("password", "")

print("Content-Type: text/html")

if email == "" or password == "":
    print()
    print("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Login Failed</title>
</head>
<body>
<h1>Login failed</h1>
<p>Email and password are required.</p>
<p><a href="login.html">Back to Login</a></p>
</body>
</html>""")
    raise SystemExit

try:
    conn = pymysql.connect(
        host="localhost",
        user="spectre_user",
        password="555555555",
        database="spectre_db"
    )

    cursor = conn.cursor()
    sql = "SELECT id, email, password_hash FROM users WHERE email = %s"
    cursor.execute(sql, (email,))
    user = cursor.fetchone()

    if user is not None:
        user_id, db_email, db_password = user

        if password == db_password:
            now = int(time.time())

            print(f"Set-Cookie: user_email={db_email}; Path=/")
            print(f"Set-Cookie: last_activity={now}; Path=/")
            print()

            print(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Login Success</title>
</head>
<body>
<h1>Login successful</h1>
<p>Welcome, {html.escape(db_email)}.</p>
<p><a href="portal.py">Go to Portal</a></p>
<p><a href="logout.py">Logout</a></p>
</body>
</html>""")
        else:
            print()
            print("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Login Failed</title>
</head>
<body>
<h1>Login failed</h1>
<p>Incorrect password.</p>
<p><a href="login.html">Back to Login</a></p>
</body>
</html>""")
    else:
        print()
        print("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Login Failed</title>
</head>
<body>
<h1>Login failed</h1>
<p>Email not found.</p>
<p><a href="login.html">Back to Login</a></p>
</body>
</html>""")

    cursor.close()
    conn.close()

except Exception as e:
    print()
    print(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Login Error</title>
</head>
<body>
<h1>Database error</h1>
<pre>{html.escape(str(e))}</pre>
<p><a href="login.html">Back to Login</a></p>
</body>
</html>""")