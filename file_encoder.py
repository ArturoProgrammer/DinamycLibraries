from EncryptX.N4Lib import encripNFour
import EncryptX.key_generator


def init ():
	fdata = open("ejemplo.dla", "r")
	data = fdata.read()
	fdata.close()

	# SE GENERAN LAS LLAVES CORRESPONDIENTES
	key_password = EncryptX.key_generator.gen_privkey(256)
	pubkey = EncryptX.key_generator.gen_publickey(key_password)


	msg_hash = encripNFour.hash_msg_gen(data)	# GENERANDO EL HASH
	print("HASH DEL MENSAJE:", msg_hash)

	# SE GUARDA LA LLAVE PRIVADA Y EL HASH EN LA DB
	EncryptX.key_generator.savedbKey(key_password, msg_hash)

	# SE ENCRIPTA EL MENSAJE
	encrip_msg = encripNFour.encode(data, encripNFour.validation_key(key_password))

	# SE GUARDA EL MENSAJE Y EL HASH EN LA DB
	encripNFour.savedbMsg(encrip_msg, msg_hash)
	print("|==> **MENSAJE CODIFICADO: \n{a}\n".format(a = encrip_msg))

	# GUARDA LA LLAVE EN UN ARCHIVO DE 	TEXTO
	EncryptX.key_generator.saveKeyOnFile(key_password)

	print("*LLAVE PRIVADA: {}".format(key_password))
	print("*LLAVE PUBLICA: {}".format(pubkey))

	# DESENCRIPTAMOS EL MENSAJE
	decode_msg = encripNFour.decode(encrip_msg, encripNFour.validation_key(pubkey))
	print("\nMENSAJE DESENCRIPTADO: {}".format(decode_msg))


	#encripNFour.update(encrip_msg, msg_hash)
	#EncryptX.key_generator.update(msg_hash, EncryptX.key_generator.gen_privkey(32))