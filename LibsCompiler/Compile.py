#!/usr/bin/env python3
# encoding: utf-8

import os
from LibsCompiler.head import headers as headers
import random
from LibsCompiler.SystemAlerts import deploy
from difflib import SequenceMatcher


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
def debug (dla_name, alerts = True):
	"""Debug de la libreria para detectar errores"""
	# Retorna:
	# * True en caso de pasar la prueba con exito
	# * False en caso de lo contrario

	return_dir = os.getcwd()
	dir = str(os.getcwd())[:-12]


	if dir[-4:] != "Dina":
		os.chdir(str(os.getcwd())[:-12])

	fails_count = 0	# Conteo de errores en el proceso
	# Si el conteo de errores es mayor a 1, no se ejecuta el programa
	# Retorna : Error

	# Lista de aprobacion de cabeceras
	approbed_list = {
		"main_headers" :False,
		"headers_parser" : False,
		"language" : False
	}

	# Lista de errores que puede retornar el compilador
	ERRORS_LIST =  {
		"NameError" : "EL NOMBRE REFERENCIADO NO ES VALIDO",
		"UnexpectedToken" : "NO SE ESPERABA",
		"HeaderMissing" : "NO HA SIDO DECLARADA LA CABECERA",
		"TokenAbsent" : "HACE FALTA EL TOKEN",
		"MissingName" : "NO SE HA DECLARADO EL NOMBRE REFERENCIADO"
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

	MSG_ERROR_DICT = {}
	# Diccionario con los errores salientes durante la compilacion
	# Estructura:
	# { counter : [ "primera parte" , "segunda parte" , "tercera parte"] }


	f_open = open(dla_name, "r")
	read_action = f_open.readlines()

	for actual_line in read_action:
		OBJ_LINE = actual_line.lstrip()
		DICT_LINES[counter] = OBJ_LINE
		counter += 1

	# Proceso Uno - revisar los Headers
	HEADER_EXPECTED_MATCH = "#define p__  = ''"
	for i in DICT_LINES:
		match_percent = SequenceMatcher(None, HEADER_EXPECTED_MATCH, DICT_LINES[i]).ratio()

		if match_percent >= 0.41:
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

			revisado = False
			if dead_string[0] != "#define":
				if str(dead_string[0])[:1] != "#":
					miss_tkn = "#"
					RETURN_ERROR = []

					part_one = "En la linea {l_n} del archivo {file}:".format(file = dla_name, l_n = i)
					part_two = "\t{line}".format(line = str(DICT_LINES[i])[:-1])
					part_three = "*** {error}: {text} '{arg}'".format(arg = miss_tkn, error = "TokenAbsent", text = ERRORS_LIST["TokenAbsent"])

					RETURN_ERROR.append(part_one)
					RETURN_ERROR.append(part_two)
					RETURN_ERROR.append(part_three)

					fails_count += 1
					MSG_ERROR_DICT[fails_count] = RETURN_ERROR
					revisado = True
				else:
					if str(dead_string[0])[1:] != "define":
						revisado = True
						RETURN_ERROR = []

						part_one = "En la linea {l_n} del archivo {file}:".format(file = dla_name, l_n = i)
						part_two = "\t {line}".format(line = str(DICT_LINES[i])[:-1])
						part_three = "*** {error}: {text} '{arg}'".format(arg = dead_string[0], error = "NameError", text = ERRORS_LIST["NameError"])

						RETURN_ERROR.append(part_one)
						RETURN_ERROR.append(part_two)
						RETURN_ERROR.append(part_three)

						fails_count += 1
						MSG_ERROR_DICT[fails_count] = RETURN_ERROR

				if revisado == False:
					if str(dead_string[0])[1:] != "define":
						RETURN_ERROR = []

						part_one = "En la linea {l_n} del archivo {file}:".format(file = dla_name, l_n = i)
						part_two = "\t {line}".format(line = str(DICT_LINES[i])[:-1])
						part_three = "*** {error}: {text} '{arg}'".format(arg = dead_string[0], error = "NameError", text = ERRORS_LIST["NameError"])

						RETURN_ERROR.append(part_one)
						RETURN_ERROR.append(part_two)
						RETURN_ERROR.append(part_three)

						fails_count += 1
						MSG_ERROR_DICT[fails_count] = RETURN_ERROR

			# Comenzar con el proceso parser del segundo argumento (privacidad)
			if dead_string[1] != "public__" and dead_string[1] != "private__":
				RETURN_ERROR = []

				part_one = "En la linea {l_n} del archivo {file}:".format(file = dla_name, l_n = i)
				part_two = "\t {line}".format(line = str(DICT_LINES[i])[:-1])
				part_three = "*** {error}: {text} '{arg}'".format(arg = dead_string[1], error = "NameError", text = ERRORS_LIST["NameError"])

				RETURN_ERROR.append(part_one)
				RETURN_ERROR.append(part_two)
				RETURN_ERROR.append(part_three)

				fails_count += 1
				MSG_ERROR_DICT[fails_count] = RETURN_ERROR

			# Comprobacion de existencia de cabeceras principales
			if dead_string[2] == "propietary_program":
				APPROBED_MAINHEADERS["propietary_program"] = True
			if dead_string[2] == "name":
				APPROBED_MAINHEADERS["name"] = True
			if dead_string[2] == "language":
				APPROBED_MAINHEADERS["language"] = True
			# Analizador del 4to argumento (simbolo de asignacion "=")
			if dead_string[3] != "=":
				RETURN_ERROR = []

				part_one = "En la linea {l_n} del archivo {file}:".format(file = dla_name, l_n = i)
				part_two = "\t {line}".format(line = str(DICT_LINES[i])[:-1])
				part_three = "*** {error}: {text} '{arg}'".format(arg = dead_string[3], error = "UnexpectedToken", text = ERRORS_LIST["UnexpectedToken"])

				RETURN_ERROR.append(part_one)
				RETURN_ERROR.append(part_two)
				RETURN_ERROR.append(part_three)

				fails_count += 1
				MSG_ERROR_DICT[fails_count] = RETURN_ERROR

	TOKENS_LIST	= [
		"@", "[", "]", "(", ")", "{", "}", ":", ";"
	]

	# Proceso Dos - revisar los bloques
	# # # TODO: HACER
	BLOCK_REFERENTIAL_MATCH	= "block: '' ; {\n"
	for i in DICT_LINES:
		match_percent = SequenceMatcher(None, BLOCK_REFERENTIAL_MATCH, DICT_LINES[i]).ratio()

		# Si la coincidencia es igual o mayor a 0.5, sabemos que se trata de una linea de block
		if match_percent >= 0.5:
			string = DICT_LINES[i]
			string = string.split()
			dead_string	= []

			# # TODO: HACER
			if string[0] != "block:":
				RETURN_ERROR = []

				part_one = "En la linea {l_n} del archivo {file}:".format(file = dla_name, l_n = i)
				part_two = "\t {line}".format(line = str(DICT_LINES[i])[:-1])
				part_three = "*** {error}: {text} '{arg}'".format(arg = string[0], error = "NameError", text = ERRORS_LIST["NameError"])

				RETURN_ERROR.append(part_one)
				RETURN_ERROR.append(part_two)
				RETURN_ERROR.append(part_three)

				fails_count += 1
				MSG_ERROR_DICT[fails_count] = RETURN_ERROR

			# # NOTE: 1 - COMPROBAR AUSENCIA DE TOKENS
			if str(string[1])[0] != "'" or str(string[1])[-1] != "'":
				miss_tkn = "'"
				RETURN_ERROR = []

				part_one = "En la linea {l_n} del archivo {file}:".format(file = dla_name, l_n = i)
				part_two = "\t {line}".format(line = str(DICT_LINES[i])[:-1])
				part_three = "*** {error}: {text} {arg}".format(arg = miss_tkn, error = "TokenAbsent", text = ERRORS_LIST["TokenAbsent"])

				RETURN_ERROR.append(part_one)
				RETURN_ERROR.append(part_two)
				RETURN_ERROR.append(part_three)

				fails_count += 1
				MSG_ERROR_DICT[fails_count] = RETURN_ERROR

			if string[2] != ";":
				miss_tkn = ";"
				RETURN_ERROR = []

				part_one = "En la linea {l_n} del archivo {file}:".format(file = dla_name, l_n = i)
				part_two = "\t {line}".format(line = str(DICT_LINES[i])[:-1])
				part_three = '*** {error}: {text} "{arg}"'.format(arg = miss_tkn, error = "TokenAbsent", text = ERRORS_LIST["TokenAbsent"])

				RETURN_ERROR.append(part_one)
				RETURN_ERROR.append(part_two)
				RETURN_ERROR.append(part_three)

				fails_count += 1
				MSG_ERROR_DICT[fails_count] = RETURN_ERROR
			if string[-1] != "{":
				miss_tkn = "{"
				RETURN_ERROR = []

				part_one = "En la linea {l_n} del archivo {file}:".format(file = dla_name, l_n = i)
				part_two = "\t {line}".format(line = str(DICT_LINES[i])[:-1])
				part_three = '*** {error}: {text} "{arg}"'.format(arg = miss_tkn, error = "TokenAbsent", text = ERRORS_LIST["TokenAbsent"])

				RETURN_ERROR.append(part_one)
				RETURN_ERROR.append(part_two)
				RETURN_ERROR.append(part_three)

				fails_count += 1
				MSG_ERROR_DICT[fails_count] = RETURN_ERROR


	# Proceso Tres - revisar los segmentos
	expected_string = ["@", "[", ":", "]", "("]
	SEGMENT_REFERENTIAL_MATCH = '@[referential : ""] ('

	for i in DICT_LINES:
		match_percent = SequenceMatcher(None, SEGMENT_REFERENTIAL_MATCH, DICT_LINES[i]).ratio()

		if match_percent >= 0.6:
			string = str(DICT_LINES[i])[:-1]	# Cadena de linea

			predead_string 	= []	# Lista de cadena pre-muerta
			ref_arg 		= ""
			tokens			= []	# Tokens presentes en la cadena
			predead_string = string.split()

			for a in predead_string:
				for char in a:
					if char in expected_string:
						tokens.append(char)
						#print(char)

			# Comprobador de errores en caso de faltar algun token en la linea
			miss_tkn = ""
			if len(tokens) != 5:
				tkns_index = []

				for a in tokens:
					for b in expected_string:
						if a == b:
							tkns_index.append(expected_string.index(b))

				for index in tkns_index:
					actual = index
					expected = int(ind + 1)

					try:
						if tkns_index.index(expected) != expected:
							pass
					except ValueError:
						if expected != 5:
							miss_tkn = expected_string[expected]
				if miss_tkn == '':
					# # NOTE: SOLUCIONAR ERROR DE COMPATIBILIDAD
					miss_tkn = "@"
					RETURN_ERROR = []

					part_one = "En la linea {l_n} del archivo {file}:".format(file = dla_name, l_n = i)
					part_two = "\t{line}".format(line = str(DICT_LINES[i])[:-1])
					part_three = "*** {error}: {text} {arg}".format(arg = miss_tkn, error = "TokenAbsent", text = ERRORS_LIST["TokenAbsent"])

					RETURN_ERROR.append(part_one)
					RETURN_ERROR.append(part_two)
					RETURN_ERROR.append(part_three)

					fails_count += 1
					MSG_ERROR_DICT[fails_count] = RETURN_ERROR

			# # TODO: COMPLETAR PROCESO PARSER DE SEGMENTOS
			# * HACER Y TERMINAR PROCESO DE SEMANTICA
			words_list	= []
			for posit in predead_string:
				word = []
				for char in posit:
					if not char in expected_string:
						word.append(char)
				if len(word) != 0:
					word = str("".join(word))
					words_list.append(word)

			if len(words_list) == 2:
				if words_list[0] != "referential":
					RETURN_ERROR = []

					part_one = "En la linea {l_n} del archivo {file}:".format(file = dla_name, l_n = i)
					part_two = "\t {line}".format(line = str(DICT_LINES[i])[:-1])
					part_three = "*** {error}: {text} '{arg}'".format(arg = words_list[0], error = "NameError", text = ERRORS_LIST["NameError"])

					RETURN_ERROR.append(part_one)
					RETURN_ERROR.append(part_two)
					RETURN_ERROR.append(part_three)

					fails_count += 1
					MSG_ERROR_DICT[fails_count] = RETURN_ERROR

				if str(words_list[1])[0] != '"' or str(words_list[1])[-1] != '"':
					miss_tkn = '"'
					RETURN_ERROR = []

					part_one = "En la linea {l_n} del archivo {file}:".format(file = dla_name, l_n = i)
					part_two = "\t {line}".format(line = str(DICT_LINES[i])[:-1])
					part_three = '*** {error}: {text} "{arg}"'.format(arg = miss_tkn, error = "TokenAbsent", text = ERRORS_LIST["TokenAbsent"])

					RETURN_ERROR.append(part_one)
					RETURN_ERROR.append(part_two)
					RETURN_ERROR.append(part_three)

					fails_count += 1
					MSG_ERROR_DICT[fails_count] = RETURN_ERROR

			else:
				if "referential" in words_list:
					RETURN_ERROR = []

					part_one = "En la linea {l_n} del archivo {file}:".format(file = dla_name, l_n = i)
					part_two = "\t {line}".format(line = str(DICT_LINES[i])[:-1])
					part_three = "*** {error}: {text}".format(error = "MissingName", text = ERRORS_LIST["MissingName"])

					RETURN_ERROR.append(part_one)
					RETURN_ERROR.append(part_two)
					RETURN_ERROR.append(part_three)

					fails_count += 1
					MSG_ERROR_DICT[fails_count] = RETURN_ERROR

				else:
					RETURN_ERROR = []

					part_one = "En la linea {l_n} del archivo {file}:".format(file = dla_name, l_n = i)
					part_two = "\t {line}".format(line = str(DICT_LINES[i])[:-1])
					part_three = "*** {error}: {text} '{arg}'".format(arg = words_list[0], error = "NameError", text = ERRORS_LIST["NameError"])

					RETURN_ERROR.append(part_one)
					RETURN_ERROR.append(part_two)
					RETURN_ERROR.append(part_three)

					fails_count += 1
					MSG_ERROR_DICT[fails_count] = RETURN_ERROR

			# * INCLUIR PARSER DE CIERRE DE TOKENS ")" y "}"


	# *** # Aqui va el CheckOut Process # *** #
	for hi in APPROBED_MAINHEADERS:
		# APROBACION DE CABECERAS PRINCIPALES
		if APPROBED_MAINHEADERS[hi] == True:
			fails_count += 0
		else:
			RETURN_ERROR = []

			part_one = "En la linea {l_n} del archivo {file}:".format(file = dla_name, l_n = hi)
			part_two = "\t {line}".format(line = "Headers")
			part_three = "*** {error}: {text} '{arg}'".format(arg = hi, error = "HeaderMissing", text = ERRORS_LIST["HeaderMissing"])

			RETURN_ERROR.append(part_one)
			RETURN_ERROR.append(part_two)
			RETURN_ERROR.append(part_three)

			fails_count += 1
			MSG_ERROR_DICT[fails_count] = RETURN_ERROR

	# Conteo de fallos
	status = False
	if fails_count >= 1:
		status = False
		# Modo para despliegue de errores
		if alerts == True: deploy(MSG_ERROR_DICT, mode="windowed", type="COMPILE")
		# ESTATUS DE PARAMETRO MODE
		# * windowed	* cli (default)
	else:
		status = True

	os.chdir(return_dir)
	return status



# # NOTE: Funcion en proceso / Corrobar para concluir
def blockSearch (lib_file, block_name):
	# Valida la existencia del bloque a buscar
	# lib_file		= nombre del archivo a leer
	# block_name	= nombre del bloque a buscar
	i 		= 0
	blc_x	= 0
	blc_y	= 0

	f_io 	= open(lib_file, "r")
	content = f_io.readlines()


	# Se buscan todos los bloques del archivo
	i_fake 		= 0
	ALL_BLOCKS	= []

	for line in content:
		i_fake += 1
		line = line[:-1]

		BLOCK_REFERENTIAL_MATCH = "block: ' ' ; {"
		match_percent = SequenceMatcher(None, BLOCK_REFERENTIAL_MATCH, line).ratio()

		if match_percent >= 0.6:
			ALL_BLOCKS.append(i_fake)	# Se guarda la posicion de inicio
		if line == "}":
			ALL_BLOCKS.append(i_fake)	# Se guarda la posicion de cierre


	BLOCK_REFERENTIAL = "block: '", block_name, "' ; {"
	b = []
	for a in BLOCK_REFERENTIAL:
		b.append(a)
	BLOCK_REFERENTIAL = "".join(b)

	# Se revisa el codigo para buscar las coordenadas correspondientes
	for line in content:
		i += 1
		line = line[:-1]	# Se elimina el caracter de salto (\n)

		if line == BLOCK_REFERENTIAL:
			blc_x = i
		if line == "}":
			if blc_x != 0:
				blc_y = ALL_BLOCKS[ALL_BLOCKS.index(blc_x) + 1]

	f_io.close()

	block_coord = (blc_x, blc_y)

	if block_coord == (0, 0):
		deploy("No existe el bloque {}".format(block_name), type="GENERAL", mode="windowed")
		return block_coord
	else:
		return block_coord



# # NOTE: Funcion estable / falta terminar
def run (lib_data):
	"""Compila y ejecuta la liberia una vez que pasa el Debug"""
	# En caso de recibir una tupla (ejecucion de segmento)
	# DECLARACION DE VARIABLES GLOBALES
	lib_name	=	""	# Nombre del archivo de la DLA
	lib_content	=	""	# Codigo a ejecutar

	# LISTA CON LOS LENGUAJES SOPORTADOS
	# # NOTE: Los lenguajes se escriben con el mismo nombre que se registran en los headers
	SUPORTTED_LANGUAGES = [
		"python"
	]

	# En caso de recibir una tupla (ejecucion de segmento)
	if isinstance(lib_data, tuple) == True:
		lib_name	= lib_data[0]
		lib_content	= lib_data[1]
		f_name		= ""

	# En caso de recibir una lista (ejecucion de bloque)
	if isinstance(lib_data, list) == True:
		lib_name	= lib_data[0][0]
		# Declaracion de lib_content
		contents = []
		for i in lib_data:
			code = i[1]
			contents.append(str("".join(code)))
		lib_content = contents	# Todos los segmendos de codigo del bloques

	program_lib	= headers.get(lib_name, "propietary_program")	# Programa "Dueño" de la libreria
	lang_lib 	= headers.get(lib_name, "language", forced = True)	# Lenguaje en la que esta escrita la libreria
	
	return_dir = os.getcwd()

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
		deploy("==== Debug exitoso!! ====")

		if lang_lib in SUPORTTED_LANGUAGES:
			# En caso de ser un lenguaje soportado por el sistema...
			if lang_lib == "python":
				# En caso de ejecutar python...

				# Se extrae el nombre del programa propietario de los headers
				__dir_existent(program_lib)
				code = str("".join(lib_content)).replace("¶", "\t")

				code_cache_file = open("fCodeCache.py", "w")
				code_cache_file.write(code)
				code_cache_file.close()

				import subprocess
				subprocess.call(["python", "fCodeCache.py"])

				os.chdir(return_dir)
		else:
			deploy(f"W!: El lenguaje {lang_lib} de la libreria no es soportado por el sistema", mode = "windowed")
