# BruteGeorge
Penetration testing in 8 numbers password modems/router

INSTRUCCIONES EN ESPAÑOL

1. ¿QUÉ HACE BRUTEGEORGE?
BruteGeorge es un software desarrollado en Python3 en Kali Linux (no sé si funcionará en Windows o Ubuntu, pueden probarlo) que teniendo un archivo .cap con el handshake obtenido con aircrack nos ayuda a sacar el password si sabemos que tiene 8 caracteres numéricos.

Todavía a día de hoy hay modems/routers que tienen este sistema de contraseñas. Si editamos el código podemos modificarlo a nuestro antojo para colocar menos o más caracteres siempre que sean numéricos.

2. ¿Cómo funciona BruteGeorge?
Lo que hace es mediante un MENU nos da a elegir entre la opción 23 de modo BruteGeorge que empezará desde el número 00000000 al 99999999 algo que depende del equipo que tengamos tardará más o menos. Por otra parte podemos elegir entre varias opciones si queremos escanear un rango determinado.

3. ¿Que requerimientos o dependencias necesito?
No es necesario tener más que Kali Linux porque necesitamos Aircrack-ng para el escaneo y Crunch para generar los diccionarios. Como he dicho antes el archivo .cap lo obtenemos de Aircrack-ng (ver cualquier tutorial para aprender a sacarlo) y Crunch no genera el diccionario.

Una de las cosas buenas de BruteGeorge es que Crunch genera un archivo de diccionario llamado diccionario.txt que ocupa 95 MB y que se va renovando, de este modo, no es necesario disponer de una cantidad enorme de espacio en disco duro.

4. Cómo lo ejecuto.
Escriba en la terminal de linux:  python3 brutegeorge.py
Es necesario tener el archivo .cap en el mismo directorio que BruteGeorge

5. Modo optimización.
Con la opción 9 del Menú podemos optimizar Kali Linux para que vaya más rápido. Mucho ojo, mirar el código antes de ejecutar porque para algunas opciones necesitas ser root. Añade al fichero /etc/sysctl.conf unas mejoras para el rendimiento e instala el software preload, deberá reiniciar depués.




ENGLISH INSTRUCTIONS.

1. WHAT DOES BRUTEGEORGE DO?
BruteGeorge is a software developed in Python3 on Kali Linux (I don't know if it will work on Windows or Ubuntu, you can try it) that having a .cap file with the handshake obtained with aircrack helps us to get the password if we know that it has 8 numeric characters.

Even today there are modems / routers that have this password system. If we edit the code we can modify it at will to place fewer or more characters provided they are numeric.

2. How does BruteGeorge work?
What it does is by means of a MENU it gives us to choose between option 23 in BruteGeorge mode that will start from the number 00000000 to 99999999 something that depends on the equipment we have, it will take more or less. On the other hand, we can choose between several options if we want to scan a certain range.

3. What requirements or dependencies do I need?
It is not necessary to have more than Kali Linux because we need Aircrack-ng for the scan and Crunch to generate the dictionaries. As I said before the .cap file is obtained from Aircrack-ng (see any tutorial to learn how to remove it) and Crunch does not generate the dictionary.

One of the great things about BruteGeorge is that Crunch generates a dictionary file called dictionary.txt that is 95 MB in size and is refreshed, so you don't need a huge amount of hard disk space.

4. How do I run it?
Type in linux terminal: python3 brutegeorge.py
You need to have the .cap file in the same directory as BruteGeorge

5. Optimization mode.
With option 9 of the Menu we can optimize Kali Linux so that it goes faster. Be careful, look at the code before executing because for some options you need to be root. Add some performance improvements to the /etc/sysctl.conf file and install the preload software, you will have to reboot later.
