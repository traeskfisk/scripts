# This will check if you are connected to desired IP.
# If you are not connected to the IP the script will kill your internet connection.

import requests
import subprocess
import time

ipget = "https://api.ipify.org?format=json"
q = requests.get(ipget)
ip = q.text
ip = ip.split(':')[1]
ip = ip.split('"')[1]
ip = ip.strip()

def check():
    try:
        x = subprocess.check_output('whois '+ip, shell=True)
        vpn = x
        if "OVPN-SE-NET" in vpn: # Substitute to your VPN provider.
            print "Connected to VPN."
            print "No need to kill internet connection."
            print "Going to sleep for 2 seconds before checking again.\n"
            time.sleep(2)
        else:
            print "Not connected to VPN."
            print "Killing internet connection."
            z = subprocess.call('wall "Internet connection killed, VPN down."', shell=True)
            y = subprocess.call('ifconfig wlp2s0 down', shell=True) # Change wlp2s0 to your interface.
            exit(1)
    except:
        pass

while (1):
    check()
