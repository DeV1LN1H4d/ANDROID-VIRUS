import os
while True:
	print("\033[0;32m"+"Installing pkg.......")
	os.system("gem install lolcat")
	os.system("pkg install ruby")
	os.system("clear")
	os.system("lolcat .bn.txt")
	print("\033[1;94m"+"""Dₑᵥₑₗₒₚₑd By:𝒟𝑒𝒱𝟣𝐿 𝒩𝟣𝐻𝟦𝒹""")
	print("\033[0;36m"+"""""")
	print(" [1] VIRUS DOWNLOAD\n [2] VIRUS LINK")
	a=str(input(" [>] Select Your Option:"))
	if a=="1":
		os.system("python3 VIRUS")
		a=input()
	elif a=="2":
		os.system("python3 SMS")
		a=input()
	else:
		print("\033[1;92m"+"[!] Invalid option!")
		print("\033[0;31m"+"Press Enter to Continue...")
		a=input()