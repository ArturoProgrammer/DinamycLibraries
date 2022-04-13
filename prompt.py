import os
import sys
import LibsCompiler.DLA
import LibsCompiler.Compile
from difflib import SequenceMatcher


def cin (command):
	# Funcion para entrada de comandos

	"""
	# PRCOESO PARA AGREGAR UN NUEVO COMANDO
	#
	# * 1 : AGREGAR A KEYWORDS_LIST
	# * 2 : PROGRAMAR EN CONDICION DE KEY_CHECK
	# * 3 : REZARLE A DIOS QUE FUNCIONE
	#
	"""

	# SE PROCESA LA LINEA DE COMANDO A EJECUTAR - PARSER
	COMMAND_STRIP = {"MAIN_KEY" : "", "FLAGS" : []}

	data = []
	for flags in command.split("--"):
		#print(flags)
		data.append(flags)

	COMMAND_STRIP["MAIN_KEY"] 	= data[0]
	COMMAND_STRIP["FLAGS"] 		= data[1:]


	# SE PROCESA LA INFORMACION PARSEADA
	
	KEYWORDS_LIST	= ["READ", "WRITE", "DECONSTRUCT", "TREE"]
	KEY_CHECK		= False					# Flag - keyword existente
	REVAL_DATA		= ""					# Datos a retornar

	for keyword in KEYWORDS_LIST:
		match_percent = SequenceMatcher(None, keyword, list(COMMAND_STRIP["MAIN_KEY"].split())[0]).ratio()

		if match_percent == 1:
			KEY_CHECK = True

	if KEY_CHECK == False:
		print("PALABRA CLAVE INEXISTENTE")


	#####################################################################
	#																	#
	# PALABRAS CLAVE AÑADIDAS CON EXITO, LISTAS PARA EJECUCION:			#
	# * READ 		/	LECTURA DE DLA									#
	# * WRITE		/ 	ESCRITURA DE DLA								#
	#																	#
	#####################################################################
	
	if KEY_CHECK == True:
		keyword_i = list(COMMAND_STRIP["MAIN_KEY"].split())[0]

		if keyword_i == "READ":
			# PROCESO PARA REALIZAR ESCRITURA DE DLA
			"""
			# BANDERAS PARA EL COMANDO:
			# --SEGMENT
			# --BLOCK
			"""

			# ========= AÑADIR EL ARG_CHECKER ========= #

			file = str(list(COMMAND_STRIP["MAIN_KEY"].split())[1])[1:-1]
			segment = COMMAND_STRIP["FLAGS"][0][9:-2]		# Bloque a trabajar
			block = COMMAND_STRIP["FLAGS"][1][7:-1]			# Segmento a trabajar

			REVAL_DATA = LibsCompiler.DLA.Read().segment(file, block, segment)
		elif keyword_i == "WRITE":
			# COMANDO PARA LA ESCRITURA DE UN DLA
			"""
			# BANDERAS PARA EL COMANDO:
			# --SEGMENT
			# --BLOCK
			# --NO-CONSTRUCT
			"""

			file = str(list(COMMAND_STRIP["MAIN_KEY"].split())[1])[1:-1]
			segment = COMMAND_STRIP["FLAGS"][0][9:-2]		# Bloque a trabajar
			block = COMMAND_STRIP["FLAGS"][1][7:-1]			# Segmento a trabajar

			if "NO-CONSTRUCT" in COMMAND_STRIP["FLAGS"]:
				# No se construye la libreria
				print("no se construira libreria")
				NOC_BOOL_VAL = False
			else:
				# Se construye la libreria
				NOC_BOOL_VAL = True

			LibsCompiler.DLA.Write(file, block, segment, CONSTRUCT = NOC_BOOL_VAL)
		elif keyword_i == "DECONSTRUCT":
			# COMANDO PARA DECONSTRUIR UNA LIBRERIA
			"""
			# BANDERAS PARA EL COMANDO:
			# --LIB
			"""

			lib_tow = COMMAND_STRIP["FLAGS"][0][5:-1]
			print("DECONSTRUYENDO LA LIBRERIA {}".format(lib_tow))

			LibsCompiler.DLA.deconstruct(lib_tow, ext = ".txt")
		elif keyword_i == "TREE":
			# COMANDO PARA MOSTRAR EL ARBOL DE CONTENIDO DE UNA LIBRERIA
			"""
			# BANDERAS PARA EL COMANDO:
			# --LIB
			"""
			lib_tow = COMMAND_STRIP["FLAGS"][0][5:-1]

			# Deconstruimos la libreria para poder leer
			decons_lib = LibsCompiler.DLA.deconstruct(lib_tow)

			file = open(decons_lib, "r")

			for i in file.readlines():
				line = str(i[:-1])

				BLOCK_REFERENTIAL_MATCH = "block: '' ; {"
				match_percent = SequenceMatcher(None, BLOCK_REFERENTIAL_MATCH, line).ratio()
				if match_percent >= 0.6:
					print(" -- BLOCK: {}".format(line[8:-5]))


				SEGMENT_REFERENTIAL_MATCH = '@[referential : ""] ('
				match_percent = SequenceMatcher(None, SEGMENT_REFERENTIAL_MATCH, line).ratio()
				if match_percent >= 0.5:
					print(" ---- SEGMENT: {}".format(line[18:-4]))
			file.close()

			# Eliminamos residuos de cache
			LibsCompiler.DLA.delete_cache()


	# En caso que se requiera devolver algun valor...
	return REVAL_DATA