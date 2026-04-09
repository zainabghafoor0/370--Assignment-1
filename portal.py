#!/usr/bin/env python3

import os
import time
import html

TIMEOUT = 5

cookie_header = os.environ.get("HTTP_COOKIE", "")
cookies = {}

if cookie_header:
    parts = cookie_header.split(";")
    for part in parts:
        if "=" in part:
            key, value = part.strip().split("=", 1)
            cookies[key] = value

user_email = cookies.get("user_email")
last_activity = cookies.get("last_activity")

print("Content-Type: text/html")

if not user_email or not last_activity:
    print()
    print("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Portal</title>
</head>
<body>
<h1>Please log in</h1>
<p>You are not logged in.</p>
<p><a href="login.html">Go to Login</a></p>
</body>
</html>""")
    raise SystemExit

try:
    last_activity = int(last_activity)
except ValueError:
    print()
    print("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Portal</title>
</head>
<body>
<h1>Session error</h1>
<p>Invalid session data. Please log in again.</p>
<p><a href="login.html">Go to Login</a></p>
</body>
</html>""")
    raise SystemExit

now = int(time.time())

if now - last_activity > TIMEOUT:
    print("Set-Cookie: user_email=; expires=Thu, 01 Jan 1970 00:00:00 GMT; Path=/")
    print("Set-Cookie: last_activity=; expires=Thu, 01 Jan 1970 00:00:00 GMT; Path=/")
    print()
    print("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Session Expired</title>
</head>
<body>
<h1>Session expired</h1>
<p>You were inactive too long. Please log in again.</p>
<p><a href="login.html">Go to Login</a></p>
</body>
</html>""")
else:
    print(f"Set-Cookie: last_activity={now}; Path=/")
    print()
    print(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Portal</title>
</head>
<body>
<h1>Welcome to the portal</h1>
<p>You are logged in as {html.escape(user_email)}.</p>
<p>Your session is still active.</p>
<p><a href="portal.py">Refresh Portal</a></p>
<p><a href="logout.py">Logout</a></p>
</body>
</html>""")