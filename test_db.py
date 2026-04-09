#!/usr/bin/env python3

print("Content-Type: text/html")
print()

try:
    import pymysql

    conn = pymysql.connect(
        host="localhost",
        user="spectre_user",
        password="555555555",
        database="spectre_db"
    )

    print("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Database Test</title>
</head>
<body>
<h1>Database connection successful</h1>
</body>
</html>
""")

    conn.close()

except Exception as e:
    print("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Database Test</title>
</head>
<body>
<h1>Database connection failed</h1>
<pre>{}</pre>
</body>
</html>
""".format(e))