import os, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92m Congratulations ! Your Device Support This Tool\033[1;37m")
    os.system('xdg-open https://wa.me/+33751131565')
if __name__=='__main__':
	try:
                __import__("IGHEDI64").license()
		__import__("IGHEDI64").login_kamu()
	except Exception as e:
		exit(str(e))
elif bit == '32bit':
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
