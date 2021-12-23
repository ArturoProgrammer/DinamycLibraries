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
