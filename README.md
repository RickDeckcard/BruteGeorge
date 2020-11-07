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
Con la opción 9 del Menú podemos optimizar Kali Linux para que vaya más rápido. Mucho ojo, mirar el código antes de ejecutar porque para algunas opciones necesitas ser root.

