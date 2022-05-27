import random
import time

caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]

chiffres = ['0','1','2','3','4','5','6','7','8','9']

chioooce = input("Wallet ou Paypal ? (w/p) > ")

if chioooce == "w":
	fake = input("Ton wallet id > ")
	print("Recherche...")
	time.sleep(2)
	print("Wallet Trouver !")
	time.sleep(1)
	print("lancement...")
	time.sleep(3)
if chioooce == "p":
	fake = input("Ton PayPal me (paypal.me/xxxxx) > ")
	print("Recherche du paypal...")
	time.sleep(3)
	print("Compte trouvé !")
	time.sleep(1)
	print("Lancement du mineur...")
	time.sleep(1.5)

while True:
	btc = ""
	cents = ""
	for i in range(300000):
		codewallet = ""
		for i in range (30):
			codewallet = f"{codewallet}{random.choice(caracteres)}"
		print(f"[{codewallet}] > 0.0000 BTC")
	for i in range(1):
		btc = f"{btc}{random.choice(chiffres)}"
	for i in range(4):
		cents = f"{cents}{random.choice(chiffres)}"
	print(f"[{codewallet}] > {btc}.{cents} BTC")
	u = input("[!] Appuie sur entrer pour continuer !")