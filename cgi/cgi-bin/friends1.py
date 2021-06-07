import cgi

reshtml = '''Content-Type: text/templates\n
<templates>
<head>
    <meta charset="UTF-8">
    <title>Friends CGI Demo (dynamic screen)</title>
</head>
<body>
<h3>Friends list for: <i>{}</i></h3>
Your name is: <b>{}</b><p>
You have <b>{}</b> friends.
</body>
</templates>
'''

form = cgi.FieldStorage()
who = form['person'].value
howmany = form['howmany'].value
print(reshtml.format(form, who, howmany))
