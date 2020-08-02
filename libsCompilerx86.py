#!/usr/bin/env python3

import os
import sys
from io import open
import subprocess


# # NOTE: PERFECCIONAR QUE AUTOMATICAMENTE SE CAMBIEN LOS TABS POR '?'
# # NOTE: AGREGAR EL SISTEMA DE ENCRIPTACION N-4

def textReplaceEncode (text):
	"""
	? = UNA TABULACION
	¿ = UN ESPACIO
	"""
	string = str(text)
	text_replace = string.replace("\t", "?")
	return text_replace

try:
	""" LECTURA Y EJECUCION DLA"""
	class DLACodeFile (object):
		"""docstring for DLACodeFile"""

		def readSegmentCode (self, dlatoread, block, referential):
			"""Retorna el segmento de codigo seleccionado"""
			# dlatoread 	= archivo a leer
			# block			= bloque en que se encuentra el codigo
			# referential	= referential del codigo

			filetoread = dlatoread

			id_locations = []	# GUARDA LAS COORDENADAS DEL CODIGO A USAR
			num_lines = 0		# GUARDA LA CANTIDAD DE LINEAS QUE HAY EN EL ARCHIVO
			text_lines = {}		# ALMACENA EL CODIGO CORRESPONDIENTE A CADA LINEA DEL ARCHIVO
			z = 0				# LINEA EN LA QUE SE ENCUENTRA EL REFERENCIAL

			if os.path.exists(filetoread):
				fileaction = open(filetoread, "r")
				# ANALIZA EL ARCHIVO PARA ENCONTRAR LOS BEGIN Y END
				for actual_line in fileaction.readlines():
					wactual_line = actual_line.lstrip()

					# # NOTE: AGREGAR FUNCION DE ESCANEAR Y REGISTRAR TODOS LOS REFERENCIALES DE LA LIBRERIA

					num_lines += 1
					text_lines[num_lines] = wactual_line # ALMACENAJE DE LINEAS EN EL DICCIONARIO

					# BUSCA EL SEGMENTO A LEER
					if wactual_line == "@[referential : {}] (\n".format(referential):
						print("REFERENCIAL ENCONTRADOOOOOO")
						z = num_lines

					if wactual_line == "BEGIN\n":
						print("====INICIO DE LINEA ENCONTRADO===", wactual_line)
						id_locations.append(num_lines)	# AGREGA COORDENADA
					elif wactual_line == "END\n":
						print("====FIN DE LINEA ENCONTRADO===", wactual_line)
						id_locations.append(num_lines)	# AGREGA COORDENADA
					elif wactual_line == "\n":
						None
					else:
						print("LEYENDO LINEA ACTUAL:", wactual_line.strip())

					letters_list = []

					for a in actual_line:
						if a == "\t":
							letters_list.append(textReplaceEncode(a))
					print(a)
					print(letters_list)


				print(letters_list)

				fileaction.close()

				x = 0
				y = 0
				# COMENZAR EL PROCESO DE LECTURA Y ALMACENADO DEL SEGMENTO DE CODIGO
				if text_lines[z+1] == "BEGIN\n":
					print("ES CORRECTOOOOO")
					x = z+1
					val = id_locations.index(z+1)
					print("EL BEGIN SE ENCUENTRA EN: {}".format(x))
					y = id_locations[val+1]
					print("EL END SE ENCUENTRA EN: {}".format(y))

				parser = []


				while x < y:
					print(text_lines[x])
					parser.append(text_lines[x])
					x += 1

				parser.remove("BEGIN\n")	# ELIMINAMOS UN ELEMENTO BASURA DEL PARSER
				chars_list = []	# SE ALMACENAN LOS CARACTERES

				for p_objetcts in parser:
					# EXAMINADOR LEXICO DE CARACTERES DE CADA OBJETO DEL PARSER
					for char in p_objetcts:
						if char == "?":
							chars_list.append("\t")
						else:
							chars_list.append(char)	# SEPARA TODOS LOS CARACTERES

				print(chars_list)
				print("".join(chars_list))

				print(parser)
				print(id_locations)
				print(text_lines)
				print("ARCHIVO LEYENDO:", filetoread)
				print("CANTIDAD DE LINEAS DEL ARCHIVO: {}".format((num_lines)))
				print("REFERENCIAL ENCONTRADO EN: {}".format(z))


				final_value = "".join(chars_list)
				fname = "fCodeCache.py"

				# SI YA EXISTE EL ARCHIVO CON EL MISMO NOMBRE
				if os.path.exists(fname) == True:
					f_ret = open(fname, "w")
					f_ret.write(final_value)
					f_ret.close()
					"""
				elif os.path.exists(fname) == False:
					new_fname =

					f_ret = open(new_fname, "w")
					f_ret.write(final_value)
					f_ret.close()
					"""
				else:
					None

				# EJECUTA EL CODIGO SELECCIONADO
				subprocess.call(["python", fname])
			else:
				print("=> LA LIBRERIA SELECCIONADA NO EXISTE\n=> LEYENDO ARCHIVO: {}".format(filetoread))


		def readBlockCode (self):
			"""Retorna todo un bloque de codigo seleccionado"""
			pass


	"""LECTURA Y EJECUCION HDLA"""
	# trabajar con los HDLA despues de haber acabado y hacer funcionar los DLA
	class HDLACodeFile(object):
		"""docstring for HDLACodeFile"""
		def readSegmentCode (self):
			# retorna un segmento de codigo
			pass

		def readBlockCode (self):
			# retorna todo un bloque de codigo
			pass
except TabError as e:
	print("ERROR DE TABULACION")
