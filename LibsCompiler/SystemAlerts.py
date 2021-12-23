from tkinter import messagebox
from tkinter import *
from tkinter import ttk

def __vbs_mode (m_dict):
    # Despliegue de mensajes usando Visual Basic Script (VBS)
    message_line = ""
    msg_counter = 0
    #print(m_dict)

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
    print(script_code)

    error_file = open("messagebox.vbs", "w")
    error_file.write('x = MsgBox({}, 16, "Error de compilacion")'.format(script_code))
    error_file.close()

    import subprocess
    subprocess.call(["start", "messagebox.vbs"], shell = True)


def alert_emergent (title, msg):
    messagebox.showerror(title, msg)


def deploy (msg, mode="cli"):
    # Despliega los mensajes de alerta del sistema
    # Modos de alerta:
    # cli       -> linea de comandos (por defecto)
    # windowed  -> modo visual

    if mode == "cli":
        if type(msg) == list:
            # En caso de recibir una lista
            error_counter = 0

            for i in msg:
                error_counter += 1

            print("SE HAN ENCONTRADO:", error_counter, "ERRORES")
            print("".join(msg))
        elif type(msg) == str:
            # En caso de recibir una cadena
            print(msg)
        elif type(msg) == dict:
            # En caso de recibir un diccionario (METODO USADO)
            for i in msg:
                print("".join(msg[i]))

    elif mode == "windowed":
        # Programar modo ventana
        if type(msg) == dict:
            __vbs_mode(msg)
        else:
            alert_emergent("Error", "Tipo de dato no admitido")
