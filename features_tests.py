from tkinter import *
from tkinter import ttk

mensajes_dict = {
    1 : ["EN LINEA 9 EN ARCHIVO ejemplo.dla:", "block: 'clase_prueba'  {", "*** TokenAbsent: HACE FALTA EL TOKEN ';'"],
    2 : ["EN LINEA 9 EN ARCHIVO ejemplo.dla:", "blck: 'clase_preba' ; {", "*** NameError: 'blck:' EL NOMBRE REFERENCIADO NO ES VALIDO"]
}


def tk_mode (msg):
    msg_dict = msg
    # Despliegue de mensajes atraves de tkinter
    root = Tk()

    for error in msg_dict:

        frm = ttk.Frame(root, padding=20)
        root.title("Error de Compilacion")
        frm.grid()

        c = 0
        part_one    = ""
        part_two    = ""
        part_three  = ""

        for e_msg in msg_dict:
            c += 1
            msg_list = msg_dict[e_msg]
            print("\n")
            part_one    = msg_list[0]
            part_two    = msg_list[1]
            part_three  = msg_list[2]

            print("\n{a}\n{b}\n{c}".format(a = part_one, b = part_two, c = part_three))

            """
            # Parametros de sticky:
            # -N    -NE     -E
            # -SE   -S      -SW
            # -W    NW      -center
            """

            ttk.Label(frm, text=part_one).grid(column=0, row=0, sticky=W)
            ttk.Label(frm, text=part_two).grid(column=0, row=1, sticky=W)
            ttk.Label(frm, text=part_three).grid(column=0, row=2, sticky=W)


    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=c+1, sticky=E)

    root.mainloop()

    print("\nEXISTEN {} ERRORES".format(c))



def vbs_mode (m_dict):
    # Despliegue de mensajes usando Visual Basic Script (VBS)
    message_line = ""
    msg_counter = 0

    for i in m_dict:
        msg_counter += 1


    #print(" & vbNewLine & ".join(mensajes_dict[3]))
    message_data = []
    for i in m_dict:
        string = m_dict[i]

        part_one = string[0]
        part_two = string[1]
        part_three = string[2]

        if i == msg_counter:
            line = str('"{}" & vbNewLine & "{}" & vbNewLine & "{}"'.format(part_one, part_two, part_three))
            message_data.append(line)
        else:
            line = str('"{}" & vbNewLine & "{}" & vbNewLine & "{}" & vbNewLine & '.format(part_one, part_two, part_three))
            message_data.append(line)


    script_code = "".join(message_data)

    error_file = open("messagebox.vbs", "w")
    error_file.write('x = MsgBox({}, 16, "Error de compilacion")'.format(script_code))
    error_file.close()

    import subprocess
    subprocess.call(["start", "messagebox.vbs"], shell = True)



# Secuencia de ejecucion
if __name__ == '__main__':
    #vbs_mode(mensajes_dict)
    tk_mode(mensajes_dict)
