
import platform
import os
os.system('termux-setup-storage')
os.system('git pull')
try:os.system('touch ua.txt')
except:pass
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("IGHEDI").login_kamu()
elif 'aarch' in arc:
	__import__("IGHEDI").license()
else:
	exit(f' Unknow device machine {arc}')
