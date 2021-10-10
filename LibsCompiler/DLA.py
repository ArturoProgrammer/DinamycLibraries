#!/usr/bin/env python3
# encoding: utf-8

import os
import sys
from io import open

# # NOTE: PERFECCIONAR QUE AUTOMATICAMENTE SE CAMBIEN LOS TABS POR '¶'
# # NOTE: IMPLEMENTAR EL SISTEMA DE ENCRIPTACION N-X


def textReplaceEncode (text):
	"""
	? = UNA TABULACION
	¿ = UN ESPACIO
	"""
	string = str(text)
	text_replace = string.replace("\t", "¶")
	return text_replace



class read (object):
	# # NOTE: Funcion terminada
	def segment (self, dlatoread, block, referential):
		#print("SE UBICA CON EXITO")
		"""Retorna una tupla con el nombre de la libreria y el codigo a ejecutar"""
		# dlatoread 	= archivo a leer
		# block			= bloque en que se encuentra el codigo	
		# referential	= referential del codigo

		filetoread = dlatoread

		tab_valor		= "¶"
		id_locations 	= []	# GUARDA LAS COORDENADAS DEL CODIGO A USAR
		text_lines 		= {}	# ALMACENA EL CODIGO CORRESPONDIENTE A CADA LINEA DEL ARCHIVO
		num_lines 		= 0		# GUARDA LA CANTIDAD DE LINEAS QUE HAY EN EL ARCHIVO
		z 				= 0		# LINEA EN LA QUE SE ENCUENTRA EL REFERENCIAL

		if os.path.exists(filetoread):
			fileaction = open(filetoread, "r")
			# ANALIZA EL ARCHIVO PARA ENCONTRAR LOS BEGIN Y END
			for actual_line in fileaction.readlines():
				wactual_line = actual_line.lstrip()

				# # NOTE: AGREGAR FUNCION DE ESCANEAR Y REGISTRAR TODOS LOS REFERENCIALES DE LA LIBRERIA

				num_lines += 1
				text_lines[num_lines] = wactual_line # ALMACENAJE DE LINEAS EN EL DICCIONARIO

				# BUSCA EL SEGMENTO A LEER
				# @[referential : = 16 caracteres
				# MODIFICAR METODO DE BUSQUEDA - eliminar limitacion de nombramiento de solo 2 caracteres
				if wactual_line == "@[referential : {}] (\n".format(referential):
					#print("REFERENCIAL ENCONTRADOOOOOO")
					z = num_lines
				if wactual_line == "BEGIN\n":
					#print("===INICIO DE LINEA ENCONTRADO===", wactual_line)
					id_locations.append(num_lines)	# AGREGA COORDENADA
				elif wactual_line == "END\n":
					#print("===FIN DE LINEA ENCONTRADO===", wactual_line)
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
				parser.append(text_lines[x])
				x += 1

			parser.remove("BEGIN\n")	# ELIMINAMOS UN ELEMENTO BASURA DEL PARSER
			chars_list = []	# SE ALMACENAN LOS CARACTERES

			for p_objetcts in parser:
				# EXAMINADOR LEXICO DE CARACTERES DE CADA OBJETO DEL PARSER
				for char in p_objetcts:
					if char == tab_valor:
						chars_list.append("\t")
					else:
						chars_list.append(char)	# SEPARA TODOS LOS CARACTERES

			#print(chars_list)
			#print("".join(chars_list))

			#print("* Codigo OBJ: ", parser)
			#print("* IDs en: ", id_locations)
			#print("*/*: ", text_lines)
			#print("ARCHIVO LEYENDO:", filetoread)
			#print("CANTIDAD DE LINEAS DEL ARCHIVO: {}".format((num_lines)))
			#print("REFERENCIAL ENCONTRADO EN: {}".format(z))

			final_value = parser

			# Retorna una tupla con valores
			# ( NOMBRE DE LA LIBRERIA , CODIGO DEL SEGMENTO A EJECUTAR )
			return dlatoread, final_value




class headers():
	# HEADERS DEL SISTEMA
	# * name 		* multiuse
	# * libpart		* proprietary_program
	#
	# Estatus:
	# * public__	Para cabeceras de acceso publico
	# * private__	Para cabeceras de acceso privado
	

	# # NOTE: Funcion terminada
	def get(dfile, head_t):
		"""Obtiene el header indicado"""
		HEADER_VALUE	= ""
		LINES_LIST		= []

		f = open(dfile, "r")
		f_content = f.readlines()
		
		flines = []
		for a in f_content:
			flines.append(a)

		# Se enlistan los headers
		headers_list = []	# Lista de los headers
		for line in flines:
			if line[:7] == "#define":
				headers_list.append(line)


		# Se comienza a buscar el header objetivo
		for a in headers_list:
			predead_string	= []
			dead_string		= [] # Linea de cabecera separada

			predead_string = a.split()

			for i in predead_string[0:4]:
				dead_string.append(i)

			fal_ext = str(" ".join(predead_string[4:]))

			dead_string.append(fal_ext)

			if dead_string[2] == head_t and dead_string[1] == "public__":
				HEADER_VALUE = dead_string[4]
				HEADER_VALUE = HEADER_VALUE[1:-1]
	
		return HEADER_VALUE



	def set(head_info):
		"""Graba los datos del header en un dla"""
		# head_info	<- { privacy : priv , name : value }
		# ejemplo:
		# 	{ "privacy" : "private" , "libpart" : "part-1" }

		pass
