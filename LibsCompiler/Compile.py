#!/usr/bin/env python3
# encoding: utf-8

import os
from LibsCompiler.DLA import headers as headers
import random
from LibsCompiler.SystemAlerts import deploy


# # NOTE: Funcion terminada
def __dir_generator (app_name):
	# Genera los directorios de cache para el programa
	series = []

	for serie in range(4):
		bit_list 	= []
		bit_serie	= ""

		for i in range(8):
			bit_list.append(str(random.randint(0, 9)))
		bit_serie = str("".join(bit_list))

		series.append(bit_serie)

	OBJ_DIRECTION = "-".join(series)
	return OBJ_DIRECTION



# # NOTE: Funcion terminada
def __dir_existent (app_name):
	# Obtiene la existencia de un directorio

	# 08183152-88156487-68415653-76289143{PROGRAMA-CACHE}
	# -------- -------- -------- -------- -------- -----
	#  Serie 1	Serie 2	 Serie 3  Serie 4  Nombre  sufijo
	#
	# Estructura para nombramiento de carpetas
	# Serie 1-4 -> direccion

	cache_direction = ""
	dirs_lists = os.listdir()

	if len(dirs_lists) == 0:
		# Genera el root del cache de los programas
		direction = str(__dir_generator(app_name) + "{" + str(app_name.replace(" " ,"")) + "-CACHE" + "}")
		os.mkdir(direction)
		cache_direction = direction
	elif len(dirs_lists) >= 1:
		list_names = []

		for i in dirs_lists:
			name = i[36:-7]
			list_names.append(name)

		if not str(app_name.replace(" " ,"")) in list_names:
			# Genera el root del cache de los programas
			direction = str(__dir_generator(app_name) + "{" + str(app_name.replace(" " ,"")) + "-CACHE" + "}")
			os.mkdir(direction)
			cache_direction = direction
		else:
			# Busca el directorio ya existente
			for route in dirs_lists:
				dname 	= route[36:-7]
				apn 	= str(app_name.replace(" " ,""))
				if dname == apn:
					direction = route

	cache_direction = direction
	os.chdir(cache_direction)

	return cache_direction




# # NOTE: Comanzar a trabajar en funcion
def debug (dla_name):
	"""Debug de la libreria para detectar errores"""
	# Retorna:
	# * True en caso de pasar la prueba con exito
	# * False en caso de lo contrario
	return_dir = os.getcwd()
	os.chdir(str(os.getcwd())[:-12])
	fails_count = 0	# Conteo de errores en el proceso

	approbed_list = {
		"main_headers" :False,
		"headers_parser" : False,
		"language" : False
	}

	ERRORS_LIST =  {
		"NameError" : "EL NOMBRE REFERENCIADO NO ES VALIDO",
		"UnexpectedToken" : "NO SE ESPERABA",
		"HeaderMissing" : "NO HA SIDO DECLARADA LA CABECERA"
	}

	# Almacenado de lineas
	DICT_LINES 	= {}
	counter		= 1

	# Cabeceras principales
	APPROBED_MAINHEADERS = {
		"name" : False,
		"propietary_program" : False,
		"language" : False
	}

	f_open = open(dla_name, "r")
	read_action = f_open.readlines()

	for actual_line in read_action:
		OBJ_LINE = actual_line.lstrip()
		DICT_LINES[counter] = OBJ_LINE
		counter += 1

	# Proceso Uno - revisar los Headers
	for i in DICT_LINES:
		if str(DICT_LINES[i])[:7] == "#define":
			string = str(DICT_LINES[i])[:-1]

			predead_string 	= []
			dead_string		= []

			predead_string = string.split()

			for arg in predead_string[0:4]:
				dead_string.append(arg)

			last_arg = str(" ".join(predead_string[4:]))
			dead_string.append(last_arg)

			DEAD_DICT 	= {}
			c 			= 0
			for x in dead_string:
				DEAD_DICT[c] = x
				c += 1

			# Comenzar con el proceso parser del segundo argumento (privacidad)
			if dead_string[1] != "public__" and dead_string[1] != "private__":
				deploy(str("EN LINEA {l_n} EN ARCHIVO {file}: \n\t{line}*** {error}: '{arg}' {text}".format(file = dla_name, l_n = i, line = DICT_LINES[i],arg = dead_string[1], error = "NameError", text = ERRORS_LIST["NameError"])))
				fails_count += 1
			# Comprobacion de existencia de cabeceras principales
			if dead_string[2] == "propietary_program":
				APPROBED_MAINHEADERS["propietary_program"] = True
			if dead_string[2] == "name":
				APPROBED_MAINHEADERS["name"] = True
			if dead_string[2] == "language":
				APPROBED_MAINHEADERS["language"] = True
			# Analizador del 4to aargumento (simbolo de asignacion "=")
			if dead_string[3] != "=":
				deploy(str("EN LINEA {l_n} EN ARCHIVO {file}: \n\t{line}*** {error}: '{arg}' {text}".format(file = dla_name, l_n = i, line = DICT_LINES[i],arg = dead_string[3], error = "UnexpectedToken", text = ERRORS_LIST["UnexpectedToken"])))
				fails_count += 1

	# *** # Aqui va el CheckOut Process # *** #
	for i in APPROBED_MAINHEADERS:
		# APROBACION DE CABECERAS PRINCIPALES
		if APPROBED_MAINHEADERS[i] == True:
			fails_count += 0
		else:
			deploy(str("EN ARCHIVO {file}: \n*** {error}: {text} '{arg}'".format(file = dla_name, arg = i, error = "HeaderMissing", text = ERRORS_LIST["HeaderMissing"])))
			fails_count += 1


	# Conteo de fallos
	status = False
	if fails_count >= 1:
		status = False
	else:
		status = True


	os.chdir(return_dir)
	return status



# # NOTE: Funcion estable / falta terminar
def run (lib_data):
	"""Compila y ejecuta la liberia una vez que pasa el Debug"""
	lib_name	= lib_data[0]	# Nombre del archivo de la DLA
	lib_content	= lib_data[1]	# Codigo a ejecutar
	f_name		= ""
	program_lib = headers.get(lib_name, "propietary_program")	# Programa "Dueño" de la libreria

	root_1	= ".cache/"
	root_2	= "temp/"

	if not os.path.exists(root_1):
		os.mkdir(root_1)
		os.chdir(root_1)
		os.mkdir(root_2)
		os.chdir(root_2)
	else:
		os.chdir(root_1)
		if not os.path.exists(root_2):
			os.mkdir(root_2)
			os.chdir(root_2)
		else:
			os.chdir(root_2)

	# Ejecucion
	if debug(lib_name) == True:
		deploy("Debug exitoso")

		# Se extrae el nombre del programa propietario de los headers
		__dir_existent(program_lib)
		code = str("".join(lib_content)).replace("¶", "\t")

		code_cache_file = open("fCodeCache.py", "w")
		code_cache_file.write(code)
		code_cache_file.close()

		import subprocess
		subprocess.call(["python", "fCodeCache.py"])
