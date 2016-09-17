import requests
import subprocess
import time
import os

# Check your IP.
ipget = "https://api.ipify.org?format=json"
q = requests.get(ipget)
ip = q.text
ip = ip.split(':')[1]
ip = ip.split('"')[1]
ip = ip.strip()

# Check if your IP is from your VPN provider.
# Kills the connected interface if not connected to your VPN.
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
            print "Killing internet connection.\n"
            z = subprocess.call('wall "Internet connection killed, VPN down."', shell=True)
            y = subprocess.call('ifconfig wlp2s0 down', shell=True) # Change wlp2s0 to your interface.
            os._exit(1)           
    except:
        print "Something went wrong."
        print "Shutting down internet to be on the safe side \n."
        z = subprocess.call('wall "Internet connection killed, something went wrong.", shell=True)
        y = subprocess.call('ifconfig wlp2s0 down', shell=True) # Change wlp2s0 to your interface.
        os._exit(1) 

while (1):
    check()
