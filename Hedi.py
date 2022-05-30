import os, sys,platform
try:
    __import__("IGHEDI64").login_kamu()
except Exception as e:
    exit(str(e))
