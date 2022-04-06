import os
import sys
import LibsCompiler.DLA
import LibsCompiler.Compile
from difflib import SequenceMatcher


def cin (command):
	# Funcion para entrada de comandos

	# SE PROCESA LA LINEA DE COMANDO A EJECUTAR - PARSER
	COMMAND_STRIP = {"MAIN_KEY" : "", "FLAGS" : []}

	data = []
	for flags in command.split("--"):
		#print(flags)
		data.append(flags)

	COMMAND_STRIP["MAIN_KEY"] 	= data[0]
	COMMAND_STRIP["FLAGS"] 		= data[1:]


	# SE PROCESA LA INFORMACION PARSEADA
	
	KEYWORDS_LIST	= ["READ", "WRITE"]
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
	# PALABRAS CLAVE AÑADIDAS CON EXITO LISTAS PARA EJECUCION:			#
	# * READ 		/	LECTURA DE DLA									#
	# * WRITE		/ 	ESCRITURA DE DLA								#
	#																	#
	#####################################################################
	
	if KEY_CHECK == True:
		keyword_i = list(COMMAND_STRIP["MAIN_KEY"].split())[0]

		if keyword_i == "READ":
			# PROCESO PARA REALIZAR ESCRITURA DE DLA
			file = str(list(COMMAND_STRIP["MAIN_KEY"].split())[1])[1:-1]
			segment = COMMAND_STRIP["FLAGS"][0][9:-2]		# Bloque a trabajar
			block = COMMAND_STRIP["FLAGS"][1][7:-1]			# Segmento a trabajar

			REVAL_DATA = LibsCompiler.DLA.Read().segment(file, block, segment)
		elif keyword_i == "WRITE":
			file = str(list(COMMAND_STRIP["MAIN_KEY"].split())[1])[1:-1]
			segment = COMMAND_STRIP["FLAGS"][0][9:-2]		# Bloque a trabajar
			block = COMMAND_STRIP["FLAGS"][1][7:-1]			# Segmento a trabajar

			LibsCompiler.DLA.Write(file, block, segment)


	# En caso que se requiera devolver algun valor...
	return REVAL_DATA