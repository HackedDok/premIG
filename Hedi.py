import platform
import os
os.system('termux-setup-storage')
os.system('git pull')
try:os.system('mkdir result')
try:os.system('touch ua.txt')
except:pass
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("IGHEDI64").login_kamu()
elif 'aarch' in arc:
	__import__("IGHEDI32").login_kamu()
else:
	exit(f' Unknown device machine {arc}')
