#!/usr/bin/python
import cgi, os
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
fileitem = form['filename']
if fileitem.filename:
   fn = os.path.basename(fileitem.filename)
   open('/tmp/' + fn, 'wb').write(fileitem.file.read())
   message = 'The File "' + fn + '" has Been uploaded successfully'
else:
   message = 'Error in uploading File'
print """\
Content-Type: text/html\n
<html>
<body>
   <p>%s</p>
</body>
</html>
""" % (message,)
#This file will print the success or error message after uploading a file