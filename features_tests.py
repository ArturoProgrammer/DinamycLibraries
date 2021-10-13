import os
from sys import argv

if __name__ == '__main__':
    file = open(argv[1], "r")
    f_content = file.readlines()
    block = argv[2]
    ref = argv[3]

    print("EN:", block)
    print("BUSCANDO:", ref)

    LINES_DICT          = {}    # { numero de linea : contenido de linea }
    counter             = 1     # Contador de lineas
    important_elements  = []    # Lista con elementosimprotantes (begin, end, block, ref)
    b_line              = 0     # Linea en la que esta el block que se esta buscando

    for a in f_content:
        a = a.lstrip()

        LINES_DICT[counter] = a

        if a[:6] == "block:":
            print("BLOQUE: {} ENCONTRADO".format(a))
            print(a[8:-6])
            important_elements.append(counter)
            if a[8:-6] == block:
                b_line = counter
                print("****BLOCK LISTOOOOOOOOOOO****")
        counter += 1

    print(important_elements)
    print(LINES_DICT)
