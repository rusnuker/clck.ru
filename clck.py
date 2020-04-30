import os
def main():
	likePayload = input('URL: ')
	r = requests.get("http://clck.ru/--", params={"url": likePayload})
	print(r.text)
try:
	import requests
	main()
except ImportError:
	os.system("pip install requests")
	os.system("pip2 install requests")
	os.system("pip3 install requests")
	import requests
	main()