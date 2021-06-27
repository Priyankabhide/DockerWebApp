#!/usr/bin/python3

import cgi
import subprocess as sp

print("content-type: text/html")
print()

f_input = cgi.FieldStorage()
command = f_input.getvalue("x")

print(sp.getoutput("sudo  " +  command))

