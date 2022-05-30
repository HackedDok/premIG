import os, sys,platform
try:
    __import__("IGHEDI").login_kamu()
except Exception as e:
    exit(str(e))
