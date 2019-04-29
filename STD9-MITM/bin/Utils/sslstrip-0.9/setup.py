#!/usr/bin/env python
import sys, os, shutil
from distutils.core import setup, Extension


shutil.copyfile("sslstrip.py", "sslstrip/sslstrip")

setup  (name        = 'sslstrip',
        version     = '1.0',
        description = 'A MITM tool that implements Moxie Marlinspike\'s HTTPS stripping attacks.',
        author = 'ZebliveD',
        author_email = 'zdark426@gmail.com',
        url = 'http://www.thoughtcrime.org/software/sslstrip/',
        license = 'GPL',
        packages  = ["sslstrip"],
        package_dir = {'sslstrip' : 'sslstrip/'},
        scripts = ['sslstrip/sslstrip'],
        data_files = [('share/sslstrip', ['README', 'COPYING', 'lock.ico'])],
       )

print "Cleaning up..."
try:
    removeall("build/")
    os.rmdir("build/")
except:
    pass

try:
    os.remove("sslstrip/sslstrip")
except:
    pass

def capture(cmd):
    return os.popen(cmd).read().strip()

def removeall(path):
	if not os.path.isdir(path):
		return

	files=os.listdir(path)

	for x in files:
		fullpath=os.path.join(path, x)
		if os.path.isfile(fullpath):
			f=os.remove
			rmgeneric(fullpath, f)
		elif os.path.isdir(fullpath):
			removeall(fullpath)
			f=os.rmdir
			rmgeneric(fullpath, f)

def rmgeneric(path, __func__):
	try:
		__func__(path)
	except OSError, (errno, strerror):
		pass
