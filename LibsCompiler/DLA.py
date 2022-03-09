#!/usr/bin/env python3
# encoding: utf-8

import os
import sys
from io import open
from difflib import SequenceMatcher
from LibsCompiler.SystemAlerts import deploy
import LibsCompiler.Compile
import LibsCompiler.head

# # NOTE: PERFECCIONAR QUE AUTOMATICAMENTE SE CAMBIEN LOS TABS POR '¶'
# # NOTE: IMPLEMENTAR EL SISTEMA DE ENCRIPTACION N-X


def textReplaceEncode (text):
	string = str(text)
	text_replace = string.replace("\t", "¶")
	return text_replace




def saveFile (name, content, mode):
	# <==== AÑADIR FUNCION DE ESTRUCTURACION ====> #
	"""
	import client_test as file_module
	content_ready = file_module.line_to_structure(content)
	"""
	content_ready = content

	#print(content_ready)

	file_write = open(name, mode)
	file_write.write(content_ready)
	file_write.close()




class Read (object):
	"""Lectura de Librerias DLA"""
	# # NOTE: Funcion terminada
	# ---> LEE Y EJECUTA UN SEGMENTO DE CODIGO
	def segment (self, dlatoread, block, referential):
		#print("SE UBICA CON EXITO")
		"""Retorna una tupla con el nombre de la libreria y el codigo a ejecutar"""
		# dlatoread 	= archivo a leer
		# block			= bloque en que se encuentra el codigo
		# referential	= referential del codigo

		# <==== SECCION CATEGORIA 1 ====> #
		# SE CREA CACHE DE SOLO LECTURA
		import client_test as file_module
		f_act = open(dlatoread, "r", encoding="utf8")

		dt = ""
		for i in f_act.readlines():
			#print(i[:-1])
			dt = dt + i
		x = str("".join(dt))
		listo = file_module.structure_to_line(x)
		print(listo)
		f_act.close()
		name_lib_cache = str(dlatoread[:-4] + ".cache")
		print(name_lib_cache)

		cache_intermediario = open(name_lib_cache, "w", encoding="utf8")
		cache_intermediario.write(listo)
		cache_intermediario.close()

		filetoread = name_lib_cache	# Jumper intermediario



		tab_valor		= "¶"	# VALOR AL QUE ES EQUIVALENTE UN TAB
		id_locations 	= []	# GUARDA LAS COORDENADAS DEL CODIGO A USAR
		text_lines 		= {}	# ALMACENA EL CODIGO CORRESPONDIENTE A CADA LINEA DEL ARCHIVO
		num_lines 		= 0		# GUARDA LA CANTIDAD DE LINEAS QUE HAY EN EL ARCHIVO
		z 				= 0		# LINEA EN LA QUE SE ENCUENTRA EL REFERENCIAL

		if os.path.exists(filetoread):
			fileaction = open(filetoread, "r")

			# ---> SE EJECUTA EL COMPILADOR ANTES QUE NADA
			if LibsCompiler.Compile.debug(filetoread, alerts=False) == False:
				pass
				# Se termina el programa

			# ---> ANALIZA EL ARCHIVO PARA ENCONTRAR TODOS LOS BEGIN Y END
			block_on_line = 0

			# ---> SE CREA LA LISTA DE SOLO LAS LINEAS QUE SE VAN A LEER
			blc_coord = LibsCompiler.Compile.blockSearch(filetoread, block)
			if blc_coord != (0, 0):
				BLOCK_LINES_LIST	= []
				BLL_COUNTER			= 0

				coord_x = blc_coord[0]
				coord_y = blc_coord[1]

				for i in fileaction.readlines():
					BLL_COUNTER += 1
					if BLL_COUNTER >= coord_x and BLL_COUNTER <=coord_y:
						BLOCK_LINES_LIST.append(i)
			else:
				## PROGRAM END ##
				sys.exit()

			exist = []	# Flags: Existencia del referencial en el bloque
			for actual_line in BLOCK_LINES_LIST:
				wactual_line = actual_line.lstrip()

				# # NOTE: AGREGAR FUNCION DE ESCANEAR Y REGISTRAR TODOS LOS REFERENCIALES DE LA LIBRERIA


				num_lines += 1
				text_lines[num_lines] = wactual_line # ALMACENAJE DE LINEAS EN EL DICCIONARIO


				"""
				# ---> BUSCA EL BLOQUE A LEER
				if wactual_line[:6] == "block:":
					#print(wactual_line)
					if wactual_line[8:-6] == block:
						#print("BLOQUE {} ENCONTRADO EN {}".format(block, num_lines))
						block_on_line = num_lines
					else:

				if wactual_line[:1] == "}":
					#print(wactual_line, "EN LINEA:", num_lines)
					pass
				"""

				# ---> BUSCA EL SEGMENTO (REFERENCIAL) A LEER
				SEGMENT_REFERENTIAL_MATCH = '@[referential : ""] ('
				match_percent = SequenceMatcher(None, SEGMENT_REFERENTIAL_MATCH, wactual_line).ratio()


				if match_percent >= 0.5:
					#print("HEMOS ENCONTRADO UN REFERENCIAL")
					if wactual_line[:1] == "@":
						if len(wactual_line.split()) == 4:
							if wactual_line[17:-5] == referential:
								z = num_lines
								exist.append(True)
							else:
								exist.append(False)


				if wactual_line == "BEGIN\n":
					id_locations.append(num_lines)	# AGREGA COORDENADA
				elif wactual_line == "END\n":
					id_locations.append(num_lines)	# AGREGA COORDENADA
				elif wactual_line == "\n":
					None
				else:
					#print("LEYENDO LINEA ACTUAL:", wactual_line.strip())
					pass

				letters_list = []
				for char_in_line in actual_line:
					if char_in_line == "\t":
						letters_list.append(textReplaceEncode(char_in_line))
					#print("***", char_in_line)

			#print(letters_list)

			fileaction.close()

			x = 0
			y = 0
			# COMENZAR EL PROCESO DE LECTURA Y ALMACENADO DEL SEGMENTO DE CODIGO
			if text_lines[z+1] == "BEGIN\n":
				#print("ES CORRECTOOOOO")
				x = z+1
				val = id_locations.index(z+1)
				#print("EL BEGIN SE ENCUENTRA EN: {}".format(x))
				y = id_locations[val+1]
				#print("EL END SE ENCUENTRA EN: {}".format(y))

			parser = []

			while x < y:
				#print(text_lines[x])
				if str(text_lines[x])[:2] == "Â¶":
					OBJ_LINE = text_lines[x].replace("Â¶", "\t")
					parser.append(OBJ_LINE)
				elif str(text_lines[x])[:1] == "¶":
					OBJ_LINE = text_lines[x].replace("¶", "\t")
					parser.append(OBJ_LINE)
				else:
					parser.append(text_lines[x])
				x += 1


			try:
				parser.remove("BEGIN\n")	# ELIMINAMOS UN ELEMENTO BASURA DEL PARSER
			except ValueError:
				pass

			chars_list = []	# SE ALMACENAN LOS CARACTERES

			for p_objetcts in parser:
				# EXAMINADOR LEXICO DE CARACTERES DE CADA OBJETO DEL PARSER
				for char in p_objetcts:
					if char == tab_valor:
						chars_list.append("\t")
					else:
						chars_list.append(char)	# SEPARA TODOS LOS CARACTERES

			final_value = parser

			# ---> Analiza las banderas de existencia del referencial
			true_c = 0
			for flag in exist:
				if flag == True: true_c += 1


			if true_c == 1:
				pass
			elif true_c >= 1:
				deploy("Existen multiples segmentos con el referencial '{}', en el bloque '{}', de la libreria '{}'".format(referential, block, dlatoread), type="GENERAL", mode="windowed")
				sys.exit()
			elif true_c == 0:
				deploy("No existe el referencial '{}', en el bloque '{}', de la libreria '{}'".format(referential, block, dlatoread), type="GENERAL", mode="windowed")
				sys.exit()

			# Retorna una tupla con valores
			# ( NOMBRE DE LA LIBRERIA , CODIGO DEL SEGMENTO A EJECUTAR )
			return filetoread, final_value


	# # NOTE: Funcion aparentemente terminada
	# ---> LEE Y EJECUTA TODOS LOS SEGMENTOS DE UN BLOQUE SECUENCIALMENTE O EN ORDEN ESPECIFICO
	def block (self, dlatoread, block, ORDER = []):
		# ***** En caso de no existir un orden de ejecucion *****
		filetoread		= dlatoread		# Libreria a leer
		lines_counter	= 0				# Contador de lineas del bloque
		ALL_REF_LIST	= []			# Todos los referenciales del bloque
		ALL_SEGM_LIST	= []			# Lista con todo el codigo de los segmentos a ejecutar

		# ---> SE EJECUTA EL COMPILADOR ANTES QUE NADA
		if LibsCompiler.Compile.debug(filetoread, alerts=True) == False:
			pass
		else:
			# En caso de NO existir un orden de ejecucion ...
			if ORDER == []:
				file_action = open(filetoread, "r")

				# LOCALIZADOR DE BLOQUE
				DICT_LINES = {}

				blc_coord = LibsCompiler.Compile.blockSearch(filetoread, block)
				if blc_coord != (0, 0):
					BLOCK_LINES_LIST	= []
					BLL_COUNTER			= 0

					coord_x = blc_coord[0]
					coord_y = blc_coord[1]

					for i in file_action.readlines():
						BLL_COUNTER += 1
						if BLL_COUNTER >= coord_x and BLL_COUNTER <= coord_y:
							DICT_LINES[BLL_COUNTER] = i[:-1]
				else:
					sys.exit() ## PROGRAM END ##

				file_action.close()

				# ---> REGISTRA TODOS LOS SEGMENTOS DEL BLOQUE
				for line in DICT_LINES:
					match_percent = SequenceMatcher(None, '@[referential : " "] (', DICT_LINES[line]).ratio()
					if match_percent >= 0.6:
						ref_name = str(DICT_LINES[line])[18:-4]
						ALL_REF_LIST.append(ref_name)

				# ---> EXTRAE CADA SEGMENTO Y LOS REGISTRA EN LA LISTA
				for referentials in ALL_REF_LIST:
					sc_tuple = self.segment(filetoread, block, referentials)
					ALL_SEGM_LIST.append(sc_tuple)

				return ALL_SEGM_LIST


			# En caso de existir un orden de ejecucion ...
			elif ORDER != []:
				file_action = open(filetoread, "r")

				# LOCALIZADOR DE BLOQUE
				DICT_LINES = {}

				blc_coord = LibsCompiler.Compile.blockSearch(filetoread, block)
				if blc_coord != (0, 0):
					BLOCK_LINES_LIST	= []
					BLL_COUNTER			= 0

					coord_x = blc_coord[0]
					coord_y = blc_coord[1]

					for i in file_action.readlines():
						BLL_COUNTER += 1
						if BLL_COUNTER >= coord_x and BLL_COUNTER <= coord_y:
							DICT_LINES[BLL_COUNTER] = i[:-1]
				else:
					sys.exit() ## PROGRAM END ##

				file_action.close()

				# ---> Se crea diccionario ordenado
				ORDER_DICT = {}
				for i in ORDER:
					ORDER_DICT[i] = ""

				# ---> EXTRAE CADA SEGMENTO Y LOS REGISTRA EN LA LISTA
				for referential in ORDER_DICT:
					sc_tuple = self.segment(filetoread, block, referential)
					ALL_SEGM_LIST.append(sc_tuple)

				return ALL_SEGM_LIST



class Write (object):
	"""Escritura de DLA; .dlib -> .dla"""
	# # NOTE: Funcion en proceso
	# ---> ESCRIBE LA DLA APARTIR DE UN DLIB (script)
	def __init__ (self, dlatowrite, blc_input, ref_input):
		# SE CREA PRIMERO ARCHIVO DE CACHE PARA LECTURA


		# Apertura de .dlib para lectura
		file_read 	= open(dlatowrite, "r")
		file_action	= file_read.readlines()

		LIB_EXISTS = False


		# <=== INICIO DE SECCION COMPROBADORA DE EXISTENCIA ===> #
		ESPEC_NAME		= str(dlatowrite[:-5] + ".dla")
		EXISTENT_FLAG	= [False, False]	# P.1 -> Bloque / P.2 -> Segmento

		# IDENTIFICADOR DE END's
		# 1 --> Analizamos la existencia de la libreria ...
		if os.path.exists(ESPEC_NAME):
			LIB_EXISTS = True
			file_read = open(ESPEC_NAME, "r")
			file_action_dla = file_read.readlines()


			# 2 --> Buscador existente de bloque...
			DICT_BUFFER	= {}	# Diccionario buffer de las lineas a tratar
			buff_count	= 0 	# Contador a utilizar en el buffer
			BLOCK_MATCH = "block: '" + blc_input + "' ; {"
			coords		= [0,0]	# Coordenadas en las que se encuentra el bloque a tratar


			block_coords_list = []
			for line in file_action_dla:
				buff_count += 1
				DICT_BUFFER[buff_count] = line
				
				match_percent = SequenceMatcher(None, BLOCK_MATCH, line[:-1]).ratio()
				
				if match_percent >= 1.0:
					EXISTENT_FLAG[0] = True
					coords[0] = buff_count
					block_coords_list.append(buff_count)
				
				if EXISTENT_FLAG[0] == True and line == "}\n":
					block_coords_list.append(buff_count)
					coords[1] = buff_count

			x = 0
			y = 0

			if EXISTENT_FLAG[0] != False:
				coords[1] = block_coords_list[int(block_coords_list.index(coords[0])) + 1]
				x = int(coords[0])
				y = int(coords[1])


			# 2.1 Una vez ubicadas las coordenadas del bloque se convierte dict -> list
			BUFFER_BLOCK_LIST = []

			for i in DICT_BUFFER:
				BUFFER_BLOCK_LIST.append(DICT_BUFFER[i])

			BLOCK_SELECTED_LINES = BUFFER_BLOCK_LIST[int(x - 1):int(y)]
			#print(BLOCK_SELECTED_LINES)

			buff_count = 0 	# Retornamos contador a 0...

		
			# 3 --> Buscador existente de segmento...
			SEGMENT_MATCH = '@[referential : "' + ref_input + '"] ('

			segment_coord_list = [0,0]

			for i in range(x, y):
				line = DICT_BUFFER[i]
				match_percent = SequenceMatcher(None, SEGMENT_MATCH, DICT_BUFFER[i][1:-1]).ratio()

				if match_percent >= 1.0:
					EXISTENT_FLAG[1] = True
					segment_coord_list[0] = i

				if EXISTENT_FLAG[1] == True and line == "\t)\n":
					segment_coord_list[1] = i

		# <=== FIN DE SECCION COMPROBADORA DE EXISTENCIA ===> #


			file_read.close()


		# Extrae lineas de codigo
		LIST_READY 				= []
		LINES_DICT 				= {}
		LINES_DICT["LOGS_LIST"] = []
		counter 				= 0
		PRE_LIST 				= []
		LAST_END_LOCAT			= 0 	# Index del ultimo END


		# <=== SECCION DE LOGS (HEADERS) P.1 ===> #

		# Extrae los LOGS y registra las lineas
		for line in file_action:
			if line[0:2] == "=>":
				LINES_DICT["LOGS_LIST"].append(line[4:-1])
			else:
				counter += 1
				LINES_DICT[counter] = line


		# <=== SECCION DE SEGMENT ===> #
		for line in LINES_DICT:
			if line != "LOGS_LIST":
				PRE_LIST.append(LINES_DICT[line])

		for i in PRE_LIST:
			val = i.replace("\t", "¶")
			LIST_READY.append("\t\t" + val)	# Datos a escribir
		file_read.close()	# Se cierra hilo de lectura
		
		BODY_DATA_SEGMENT = """
\t@[referential : "{AB}"] (
\t\tBEGIN
{AC}
\t\tEND
\t)
""".format(AB = ref_input, AC = "".join(LIST_READY))

		

		# <=== SECCION DE LOGS (HEADERS) P.2 ===> #
		"""
		# LOGS PRINCIPALES:
		# * MASTER_PROGRAM	-> propietary_program
		# * NAME 			-> name
		# * PROG_LANGUAGE 	-> language
		"""
		
		DICT_LOGS_VALS		= {}
		DICT_LOGS 			= LINES_DICT["LOGS_LIST"]
		CONTROL_POINTS_DICT	= {}
		for log in DICT_LOGS:
			CONTROL_POINTS = []

			#log = log.replace(" ", "")

			char_counter = 0
			for char in log:
				char_counter += 1
				if char == ";" or char == ")":
					CONTROL_POINTS.append(char_counter)

			CONTROL_POINTS_DICT[log] = CONTROL_POINTS


		"""
		for log in DICT_LOGS:
			for index in CONTROL_POINTS:
				print(log, index, ";", log[2:index])
		"""

		for log in CONTROL_POINTS_DICT:
			position	= 0
			PREVIOUS	= 0
			count 		= 0

			HEADER_VALS = {
				"H_NAME" : "",
				"PRIVACY" : "",
				"VALUE" : ""
			}

			header = ""
			for POINT in CONTROL_POINTS_DICT[log]:
				position += 1
				count += 1

				if count == 1:
					# Dato 1 / Nombre de cabecera
					log_frag = log[PREVIOUS:POINT].replace("(", "")
					log_frag = log_frag.replace(")", "")
					log_frag = log_frag.replace(";", "")
					log_frag = log_frag.replace('"', "")

					# Detector de headers
					if log_frag ==  "MASTER_PROGRAM":
						header = "propietary_program"
					elif log_frag == "NAME":
						header = "name"
					elif log_frag == "PROG_LANGUAGE":
						header = "language"
					elif log_frag ==  "REQUIRE":
						header = "require"

					DICT_LOGS_VALS[header] = HEADER_VALS
					DICT_LOGS_VALS[header]["H_NAME"] = header
				elif count == 2:
					# Dato 2 / Valor
					log_frag = log[PREVIOUS:POINT].replace("(", "")
					log_frag = log_frag.replace(")", "")
					log_frag = log_frag.replace(";", "")
					log_frag = log_frag.replace('"', "")

					DICT_LOGS_VALS[header]["VALUE"] = log_frag
				elif count == 3:
					# Dato 3 / Privacidad
					log_frag = log[PREVIOUS:POINT].replace("(", "")
					log_frag = log_frag.replace(")", "")
					log_frag = log_frag.replace(";", "")
					log_frag = log_frag.replace('"', "")

					DICT_LOGS_VALS[header]["PRIVACY"] = log_frag
				elif count == 4:
					# Reinicio de conteo
					count = 0
					header = ""


				PREVIOUS = POINT

		# Crea y llena el formato de las cabeceras
		HEADER_LINES_LIST = []

		for i in DICT_LOGS_VALS:
			name = DICT_LOGS_VALS[i]["H_NAME"]
			val  = DICT_LOGS_VALS[i]["VALUE"]
			priv = DICT_LOGS_VALS[i]["PRIVACY"]

			line_format = str("#define {c}__ {a} = '{b}'\n".format(a = name, b = val[1:], c = priv[1:]))
		
			HEADER_LINES_LIST.append(line_format)

		HEADERS_DATA_SEGMENT = """
{A}
""".format(A = str("".join(HEADER_LINES_LIST)))

		string = "block: '" + blc_input + "' ; {"


		# <=== SECCION DE ENSAMBLE ===> #

		BLOCK_DATA_SEGMENT = """
{first}
{body}
{last}
""".format(first = string, body = BODY_DATA_SEGMENT, last = "}")


		FINAL_DLA = """
{headers}
{blocks}
""".format(headers = HEADERS_DATA_SEGMENT, blocks = BLOCK_DATA_SEGMENT)


		#####################################################
		#													#
		# TOMA DE DECISIONES FINALES 						#
		# PARA DETERMINAR EL CASO DE AÑADIR O SOBRE ESRIBIR #
		# UN SEGMENTO SE DEBE EVALUAR LA FLAG EXISTENT_FLAG #
		#													#
		#####################################################

		if LIB_EXISTS == True:
			if EXISTENT_FLAG[0] == True:
				# En caso de que exista el bloque...
				# -> Buscar segmento...
				if EXISTENT_FLAG[1] == True:
					# # NOTE: SOBREESCRITURA DE SEGMENTO LISTA
					# <===> NO MODIFICAR <===> #

					# En caso de que exista el segmento...
					# -> Se sobreescribe segmento
					#print("EL SEGMENTO SI EXISTE")
					#print("Se reescribiran las lineas:", segment_coord_list, "que corresponden al referencial:", ref_input)

					last_replace_start	= int(segment_coord_list[1]) + 1
					last_replace_end	= len(DICT_BUFFER)


					for i in range(segment_coord_list[0], segment_coord_list[1] + 1):
						DICT_BUFFER.pop(i)

					first_replace_start = int(segment_coord_list[0])
					#print(first_replace_start)
					#print(BODY_DATA_SEGMENT)

					old_beg_list = []
					old_end_list = []


					# Se asignan valores de old_beg_list
					for i in range(1, first_replace_start):
						line = DICT_BUFFER[i]
						old_beg_list.append(line)


					# Se asignan valores de olg_end_list
					for i in range(last_replace_start, int(last_replace_end) + 1):
						line = DICT_BUFFER[i]
						old_end_list.append(line)

					old_beg = str("".join(old_beg_list))
					old_end = str("".join(old_end_list))

					NEW_DATA_SEGMENT = """
{OLD_BEGIN}
{NEW}
{OLD_END}
""".format(OLD_BEGIN = old_beg[:-1], NEW = BODY_DATA_SEGMENT[1:-1], OLD_END = old_end)
					FINAL_DLA = NEW_DATA_SEGMENT[1:-1]
					#print(FINAL_DLA)
					#print("**************************GRABANDO**************************")
					saveFile(ESPEC_NAME, FINAL_DLA, "w")
					print("AQUI 1")

				else:
					# # NOTE: ADICION DE SEGMENTO EN BLOQUE EXISTENTE LISTO
					# <===> NO MODIFICAR <===> #

					# En caso de que no exista el segmento...
					# -> Crear segmento debajo del ultimo segmento del bloque
					print("NO EXISTE EL SEGMENTO {} EN EL BLOQUE {}".format(ref_input, blc_input))

					
					insert_start_index = int(block_coords_list[1] - 1)
					insert_finish_index = int(block_coords_list[-1])

					old_beg_list = []
					old_end_list = []

					for i in range(1, insert_start_index):
						line = DICT_BUFFER[i]
						old_beg_list.append(line)

					for i in range(insert_start_index, int(insert_finish_index) + 1):
						line = DICT_BUFFER[i]
						old_end_list.append(line)


					old_beg = str("".join(old_beg_list))
					old_end = str("".join(old_end_list))

					NEW_DATA_SEGMENT = """
{OLD_BEGIN}
{NEW}
{OLD_END}
""".format(OLD_BEGIN = old_beg, NEW = BODY_DATA_SEGMENT, OLD_END = old_end)
				FINAL_DLA = NEW_DATA_SEGMENT[1:-1]
				#print(FINAL_DLA)
				saveFile(ESPEC_NAME, FINAL_DLA, "w")
				print("AQUI 2")

			else:
				# # NOTE: ADICION DE BLOQUE Y SEGMENTO NO EXISTENTES LISTO
				# <===> NO MODIFICAR <===> #

				# En caso de que no exista el bloque...
				# -> Hacer bloque
				# -> Hacer segmento
				#print("NO EXISTE EL BLOQUE")

				FINAL_DLA = BLOCK_DATA_SEGMENT[:]
				saveFile(ESPEC_NAME, FINAL_DLA, "a")
				print("AQUI 3")

		else:
			# Si la libreria no existe...
			# # NOTE: CREACION DE DLA LISTA 
			# <===> NO MODIFICAR <===> #

			# -> Crea la libreria
			# -> Inyecta headers
			# -> Crea bloque
			# -> Crea segmento
			#print("NO EXISTE LA LIBRERIA")

			# Creacion de DLA
			saveFile(ESPEC_NAME, FINAL_DLA[2:-1], "w")
			print("AQUI 4")

		# GUARDADO CON ENCRIPTACION ESTRUCTURADA
		import client_test as file_module
		X = file_module.line_to_structure(ESPEC_NAME)

		file_ready_to_save = open(ESPEC_NAME, "w", encoding="utf8")
		file_ready_to_save.write(X)
		file_ready_to_save.close()

		print(X)
