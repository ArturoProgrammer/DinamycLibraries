def interchanger (dla):
	# SOBRE ESCRIBE LA DLA DE ARCHIVO ESTRUCTURADO A TEXTO PLANO
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
	
	name_lib_cache = dla
	#print(name_lib_cache)


	cache_intermediario = open(name_lib_cache, "w", encoding="utf8")
	cache_intermediario.write(listo)
	cache_intermediario.close()


if __name__ == '__main__':
	interchanger("libreria de ejemplo.dla")