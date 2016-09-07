import requests
import time
import subprocess

url = "https://api.ipify.org?format=json"
q = requests.get(url)
ip = q.text
ip = ip.split(':')[1]
ip = ip.split('"')[1]
ip = ip.strip()

vpn = "46.227.67.168"

def check():
    print "Sending request"
    try:
        ip
        if ip == vpn:
            print "Connected to VPN, no need to kill myself."
            print "Checking again in 5 seconds"
            print "Going to sleep\n"
            time.sleep(5)
        else:
            print "Not connected to VPN. Gonna kill myself."
            x = subprocess.call('shutdown now', shell=True)
            exit(1)
    except:
        x = subprocess.call('shutdown now', shell=True)
        exit(1)
while (1):
    check()
