import os
while True:
	os.system("clear")
	print("\033[0;36m"+"""
	
 █████  ███    ██ ██████  ██████   ██████  ██ ██████        ██    ██ ██ ██████  ██    ██ ███████ 
██   ██ ████   ██ ██   ██ ██   ██ ██    ██ ██ ██   ██       ██    ██ ██ ██   ██ ██    ██ ██      
███████ ██ ██  ██ ██   ██ ██████  ██    ██ ██ ██   ██ █████ ██    ██ ██ ██████  ██    ██ ███████ 
██   ██ ██  ██ ██ ██   ██ ██   ██ ██    ██ ██ ██   ██        ██  ██  ██ ██   ██ ██    ██      ██ 
██   ██ ██   ████ ██████  ██   ██  ██████  ██ ██████          ████   ██ ██   ██  ██████  ███████ 
                                                                                                       
	""")
	print("\033[1;94m"+"""Dₑᵥₑₗₒₚₑd By:DEVILNIHAD""")
	print("\033[0;36m"+"""""")
	print(" [1] VIRUS DOWNLOAD\n [2] VIRUS LINK")
	a=str(input(" [>] Select Your Option:"))
	if a=="1":
		os.system("python3 VIRUS")
		a=input()
	elif a=="2":
		os.system("python3 DRL")
		a=input()
	else:
		print("\033[1;92m"+"[!] Invalid option!")
		print("\033[0;31m"+"Press Enter to Continue...")
		a=input()