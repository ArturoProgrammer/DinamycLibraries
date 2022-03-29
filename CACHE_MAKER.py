def interchanger (dla):
	# SOBRE ESCRIBE LA DLA DE ARCHIVO ESTRUCTURADO A TEXTO PLANO
	#print("LA LIBRERIA " + dla + " SI EXISTE")
	
	import client_test as file_module

	try:
		f_act = open(dla, "r", encoding="utf8")
	except UnicodeDecodeError as e:
		pass
	else:
		f_act = open(dla, "r")

	dt = ""
	for i in f_act.readlines():
		#print(i[:-1])
		dt = dt + i

	x = str("".join(dt))
	listo = file_module.structure_to_line(x)

	f_act.close()

	#print("\n{a} \n////////////////////////////\n{b}\n".format(a = x, b = listo))
	NAME_LIB_CACHE = dla
	#print(name_lib_cache)


	cache_intermediario = open(NAME_LIB_CACHE, "w", encoding="utf8")
	cache_intermediario.write(listo)
	cache_intermediario.close()

	return NAME_LIB_CACHE



def saveFileStructured (name, content, mode):
	# <==== AÑADIR FUNCION DE ESTRUCTURACION ====> #
	
	import client_test as file_module
	content_ready = file_module.line_to_structure(name)

	#print(content_ready)
	file_write = open(name, mode)
	file_write.write(content_ready)
	file_write.close()




if __name__ == '__main__':
	f = "libreria de ejemplo.dla"

	interchanger(f)

"""
	file = open(f, "r", encoding="utf8")

	list_c = []
	for i in file.readlines():
		list_c.append(i)

	ready = "".join(list_c)
	saveFileStructured(f, ready, "w")
"""