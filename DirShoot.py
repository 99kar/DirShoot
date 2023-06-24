# Script by : 99kar
# Github : https://github.com/99kar
# DirShoot v1
import time
import os
import sys
import requests

BLACK = '\033[1;30m'
RED = '\033[1;31m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
MAGENTA = '\033[1;35m'
CYAN = '\033[1;36m'
WHITE = '\033[1;37m'
RESET = '\033[1;39m'

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)

def clear():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS y Linux
        os.system('clear')

def banner():
	print()
	print(BLUE + " ██████  ██ ██████  " + YELLOW + "███████ ██   ██  ██████   ██████  ████████")
	print(BLUE + " ██   ██ ██ ██   ██ " + YELLOW + "██      ██   ██ ██    ██ ██    ██    ██")
	print(BLUE + " ██   ██ ██ ██████  " + YELLOW + "███████ ███████ ██    ██ ██    ██    ██")
	print(BLUE + " ██   ██ ██ ██   ██ " + YELLOW + "     ██ ██   ██ ██    ██ ██    ██    ██")
	print(BLUE + " ██████  ██ ██   ██ " + YELLOW + "███████ ██   ██  ██████   ██████     ██")
	print(BLUE + "▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃" + YELLOW + "▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃")
	print()
	print(BLUE + "                  --> " + YELLOW + "Script by 99kar")
	print(BLUE + "                  --> " + YELLOW + "https://github.com/99kar")
	print()

def main():
	print()
	url = input(BLUE + "[" + YELLOW + "?" + BLUE + "] " + WHITE + "URL del sitio (https://ejemplo.com/ http://ejemplo.com/) " + BLUE + ": " + WHITE)
	diccionario = input(BLUE + "[" + YELLOW + "?" + BLUE + "] " + WHITE + "Archivo de diccionario (aprete enter si no tiene uno) " + BLUE + ": " + WHITE)
	slowprint(GREEN + "[+] Iniciando escaneo")
	time.sleep(1)
	clear()
	if diccionario == "":
		print(GREEN + "URL : " + url + " | Archivo : diccionario.txt")
		diccionario = "diccionario.txt"
	else:
		print(GREEN + "URL : " + url + " | Archivo : " + diccionario)
	os.system("touch output.txt")
	try:
		with open(diccionario, 'r') as archivo:
			for linea in archivo:
				urlFinal = url + linea.strip()
				try:
					response = requests.head(urlFinal)
					if response.status_code == 200:
						print(WHITE + "[ " + GREEN + "SUCCESS" + WHITE + " ] Encontrado : " + urlFinal)
						with open("output.txt", 'a') as archivo:
							archivo.write(urlFinal+"\n")
					else:
						print(WHITE + "[ " + RED + str(response.status_code) + WHITE + " ] No existe : " + urlFinal)
				except requests.exceptions.RequestException as e:
					print("Error al acceder a la URL:", e)
	except FileNotFoundError:
		print(RED + "[-] El archivo no existe")
	except IOError:
		print(RED + "[-] Error al leer el archivo")


if __name__ == "__main__":
	clear()
	banner()
	main()
