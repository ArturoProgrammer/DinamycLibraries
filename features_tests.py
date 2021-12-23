from tkinter import *
from tkinter import ttk

mensajes_dict = {
    1 : ["EN LINEA 9 EN ARCHIVO ejemplo.dla:", "block: 'clase_prueba'  {", "*** TokenAbsent: HACE FALTA EL TOKEN ';'"],
    2 : ["EN LINEA 9 EN ARCHIVO ejemplo.dla:", "blck: 'clase_preba' ; {", "*** NameError: 'blck:' EL NOMBRE REFERENCIADO NO ES VALIDO"]
}


def tk_mode ():
    # Despliegue de mensajes atraves de tkinter
    root = Tk()

    frm = ttk.Frame(root, padding=80)
    frm.grid()
    ttk.Label(frm, text=msg).grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

    root.mainloop()



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
    vbs_mode(mensajes_dict)
