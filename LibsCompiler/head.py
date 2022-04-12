class headers():
	# HEADERS DEL SISTEMA
	# * name 		* multiuse
	# * libpart		* proprietary_program
	#
	# Estatus:
	# * public__	Para cabeceras de acceso publico
	# * private__	Para cabeceras de acceso privado

	# # NOTE: Funcion terminada
	def get(dfile, head_t, forced=False):
		"""Obtiene el header indicado"""

		# Parametros:
		# dfile		= Libreria
		# head_t 	= Header a buscar
		# forced	= Lectura forzada de header privado (terminar)

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
			
			elif dead_string[2] == head_t and dead_string[1] == "private__" and forced == False:
				print("W!: El header al que desea acceder es privado")

			elif dead_string[2] == head_t and dead_string[1] == "private__" and forced == True:
				HEADER_VALUE = dead_string[4]
				HEADER_VALUE = HEADER_VALUE[1:-1]

		#print("VALOR DE HEADER:", HEADER_VALUE)
		return HEADER_VALUE


	# # NOTE: Funcion terminada
	def set(head_info):
		"""Procesa los datos del header para generar linea de #define"""
		for i in head_info:
			name = head_info["H_NAME"]
			val  = head_info["VALUE"]
			priv = head_info["PRIVACY"]

			line_format = str("#define {c}__ {a} = '{b}'\n".format(a = name, b = val[1:], c = priv[1:]))

			return line_format
