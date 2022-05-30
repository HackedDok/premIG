import os, sys,platform
try:
    os.system("touch ua.txt")
    __import__("IGHEDI").login_kamu()
except Exception as e:
    exit(str(e))
