#!/usr/bin/env python3

# ARCHIVO CLIENTE DE PRUEBA PARA EL SOFTWARE

from EncryptX.N4Lib import encripNFour
from EncryptX import key_generator
#import DBmanipulate
from EncryptX import cleaner


#encripNFour.module_help()

def line_to_structure (FILE):
    # ESTRUCTURA UN MNENSAJE DE LINEA
    # FILE -> archivo a estructurar y codificar

    print(FILE)
    # SE GENERAN LAS LLAVES CORRESPONDIENTES
    key_password = key_generator.gen_privkey(64)
    pubkey = key_generator.gen_publickey(key_password)


    f_io = open(FILE, "r")	# EN ESTE CASO ENCRIPTAREMOS EL CONTENIDO DE UN ARCHIVO

    data_to_encrypt = str("".join(f_io.readlines()))         # VALOR QUE SE DARA PARA GENERAR EL HASH
    hash = encripNFour.hash_msg_gen(data_to_encrypt)	# GENERANDO EL HASH

    # SE GUARDA LA LLAVE PRIVADA Y EL HASH EN LA DB
    i = key_generator.savedbKey(key_password, hash)

    # SE ENCRIPTA EL MENSAJE
    encrip_msg = encripNFour.encode(data_to_encrypt, encripNFour.validation_key(key_password))

    # SE GUARDA EL MENSAJE Y EL HASH EN LA DB
    encripNFour.savedbMsg(encrip_msg, hash)


    key_generator.saveKeyOnFile(key_password)	# GUARDA LA LLAVE EN UN ARCHIVO DE TEhashTO


    decodeval = encripNFour.decode(encrip_msg, encripNFour.validation_key(pubkey))

    encripNFour.update(encrip_msg, hash)
    key_generator.update(hash, key_generator.gen_privkey(64))

    cleaner.clean()


    # ===== PROCESO DE ESTRUCTURACION ===== #
    counter = 0
    before  = 0
    after   = 2

    PAIRS_LIST = [] # Lista con los pares asignados

    # Se crea la lista de los pares
    data_buff = []
    for i in encrip_msg:

        for char in i:
            counter += 1

            data_buff.append(char)
            #print(pair, counter)

            if counter == 2:
                val = str("".join(data_buff))
                PAIRS_LIST.append(val)

                data_buff = []

                after += 2
                counter = 0

    # Se crea escructura
    line        = []
    line_buff   = []
    lenght      = int(32 - 1)    # Limite de pares en una misma linea

    remanent = len(PAIRS_LIST)  # variable dinamica
    total = remanent    # variable estatica

    for i in PAIRS_LIST:
        counter += 1
        remanent -= 1

        #print(i, counter, "QUEDAN: ", remanent)
        if counter < int(lenght + 1):
            # Si es menor al limite sigue agregando...
            line_buff.append(i)
        elif counter == int(lenght + 1):
            # Si es igual al limite agrega el ultimo digito y mete lista a line...
            line_buff.append(i)

            line.append(str(" ".join(line_buff) + "\n"))
            #print("\n" + " ".join(line_buff) + "\n")
            line_buff = []

            if remanent <= lenght:
                line_buff = PAIRS_LIST[int(total - remanent):]
                line.append(str(" ".join(line_buff) + "\n"))

            counter = 0

    structure = "".join(line)
    #print(structure)
    return structure

#====================================================================================================#
#====================================================================================================#
#====================================================================================================#
#====================================================================================================#
#====================================================================================================#
#====================================================================================================#


"""
# SE GENERAN LAS LLAVES CORRESPONDIENTES
key_password = key_generator.gen_privkey(64)
pubkey = key_generator.gen_publickey(key_password)



data_to_encrypt = "".join(f_io.readlines())
hash = encripNFour.hash_msg_gen(data_to_encrypt)	# GENERANDO EL HASH
#print("HASH:", hash)

# SE GUARDA LA LLAVE PRIVADA Y EL HASH EN LA DB
i = key_generator.savedbKey(key_password, hash)

# SE ENCRIPTA EL MENSAJE
encrip_msg = encripNFour.encode(data_to_encrypt, encripNFour.validation_key(key_password))

# SE GUARDA EL MENSAJE Y EL HASH EN LA DB
encripNFour.savedbMsg(encrip_msg, hash)


f_io.close()	# SE CIERRA EL ARCHIVO. TODOS LOS DATOS YA ESTAN ALAMCENADOS EN EL PROGRAMA LOCAL

#print("|==> **MENSAJE CODIFICADO Y LLAVE: \n-> {a}\n-> {b}".format(a = encrip_msg, b = key_password))
key_generator.saveKeyOnFile(key_password)	# GUARDA LA LLAVE EN UN ARCHIVO DE TEhashTO

#print("LONGITUD DE LLAVE PRIVADA: {}".format(len(key_password)))

#print("\nLLAVE PUBLICA: {}".format(pubkey))
#print("LONGITUD DE LLAVE PUBLICA: {}".format(len(pubkey)))

decodeval = encripNFour.decode(encrip_msg, encripNFour.validation_key(pubkey))
#print("\nMENSAJE DESENCRIPTADO: \n{}".format(decodeval))

encripNFour.update(encrip_msg, hash)
key_generator.update(hash, key_generator.gen_privkey(64))

cleaner.clean()


# ===== PROCESO DE PRUEBA ===== #
#print(encrip_msg)

counter = 0
before  = 0
after   = 2

PAIRS_LIST = [] # Lista con los pares asignados

# Se crea la lista de los pares
data_buff = []
for i in encrip_msg:

    for char in i:
        counter += 1

        data_buff.append(char)
        #print(pair, counter)

        if counter == 2:
            val = str("".join(data_buff))
            PAIRS_LIST.append(val)

            data_buff = []

            after += 2
            counter = 0

# Se crea escructura


line        = []
line_buff   = []
lenght      = int(32 - 1)    # Limite de pares en una misma linea

remanent = len(PAIRS_LIST)  # variable dinamica
total = remanent    # variable estatica
#print(remanent)

for i in PAIRS_LIST:
    counter += 1
    remanent -= 1

    #print(i, counter, "QUEDAN: ", remanent)
    if counter < int(lenght + 1):
        # Si es menor al limite sigue agregando...
        line_buff.append(i)
    elif counter == int(lenght + 1):
        # Si es igual al limite agrega el ultimo digito y mete lista a line...
        line_buff.append(i)

        line.append(str(" ".join(line_buff) + "\n"))
        #print("\n" + " ".join(line_buff) + "\n")
        line_buff = []

        if remanent <= lenght:

            #print("===== TERMINANDO LISTA =====")
            #print("QUEDAN: ", remanent)
            #print("SE HAN INSERTADO: ", int(total - remanent))

            line_buff = PAIRS_LIST[int(total - remanent):]

            #print(" ".join(line_buff))
            line.append(str(" ".join(line_buff) + "\n"))


        counter = 0

structure = "".join(line)

# Se guarda el archivo estructurado
save_file = open("saved.dla", "w", encoding = "utf8")
save_file.write(structure)
save_file.close()
"""

# ESTRUCTURADO -> 1L
#print(structure)
def structure_to_line (msg):
    # msg -> mensaje estructurado a desestructurar y decodificar
    on_line = []
    structure = msg

    final_line = ""
    for i in structure:
        if i != "\n" and i != " ":
            on_line.append(i)

        final_line = "".join(on_line)

    decode_line = encripNFour.decode(final_line, True)

    return decode_line
# LISTO

#d_msg = structure_to_line(structure)
#print(d_msg)


#print(encripNFour.decode(d_msg, True))

#print("LA LLAVE ASOCIADA ES: {}".format(DBmanipulate.DB().getKey()))

if __name__ == "__main__":
    print("ejecutand")
    lib = open("data_to_structure.cache", "r", encoding="utf8")

    datos = ""

    for i in lib.readlines():
        datos = datos + i
    print(datos)

    listo = structure_to_line(datos)
    print(listo)
