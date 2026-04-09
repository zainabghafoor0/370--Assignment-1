#!/usr/bin/env python3

print("Content-Type: text/html")
print("Set-Cookie: user_email=; expires=Thu, 01 Jan 1970 00:00:00 GMT; Path=/")
print("Set-Cookie: last_activity=; expires=Thu, 01 Jan 1970 00:00:00 GMT; Path=/")
print()

print("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Logout</title>
</head>
<body>
<h1>You have been logged out</h1>
<p><a href="login.html">Login again</a></p>
</body>
</html>""")