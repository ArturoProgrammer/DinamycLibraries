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



def alert_emergent (w_title, msg, type):
    """
    Despliega mensajes de alerta de forma grafica
    Parametros:
    * w_title: titulo de la ventana [str]
    * msg: mensaje a mostrar [str, dict, list]
    * type: tipo de mensaje [str]

    Valores acepatados para parametro type:
    * COMPILE: error de compilacion o debug
    * GENERAL: mensaje de alerta general (default)
    """

    # Despliegue de mensajes atraves de tkinter
    root = Tk()
    root.title(w_title)
    #root.geometry("500x300")


    # Si es error de compilacion...
    if isinstance(msg, dict) == True and type == "COMPILE":
        msg_dict = msg
        c = 0
        for error in msg_dict:
            frm = ttk.Frame(root, padding=10)
            #frm.grid()

            part_one    = ""
            part_two    = ""
            part_three  = ""

            c += 1
            msg_list = msg_dict[error]

            part_one    = msg_list[0]
            part_two    = msg_list[1]
            part_three  = msg_list[2]

            # Se imprimen los mensajes de errores como prueba para corrobar
            # que funcionan a la perfeccion
            #print("\n{a}\n{b}\n{c}".format(a = part_one, b = part_two, c = part_three))

            """
            # Parametros de sticky:
            # -N    -NE     -E
            # -SE   -S      -SW
            # -W    NW      -center
            """

            L_ONE = ttk.Label(frm, text=part_one)       # P1
            L_TWO = ttk.Label(frm, text=part_two)       # P2
            L_THREE = ttk.Label(frm, text=part_three)   # P3

            L_ONE.pack()
            L_THREE.pack(after=L_ONE)
            L_TWO.pack(after=L_ONE, before=L_THREE)

            frm.pack()

            #ttk.Label(frm, text=part_one).grid(column=0, row=0, sticky=W)   # P1
            #ttk.Label(frm, text=part_two).grid(column=0, row=1, sticky=W)   # P2
            #ttk.Label(frm, text=part_three).grid(column=0, row=2, sticky=W) # P3

        #ttk.Label(frm, text=str("Se registraron un total de {} errores".format(c))).grid(column=0, sticky=SW)
        #ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=c+4, sticky=SE)
        print("*****IMPOSIBLE DE COMPILAR*****")
        if c >= 2:
            print("\n--> EXISTEN {} ERRORES".format(c))
        elif c == 1:
            print("\n--> EXISTE {} ERROR".format(c))

        B_EXIT = ttk.Button(frm, text="Ok", command=root.destroy)
        B_EXIT.pack(side=RIGHT)
        ttk.Label(frm, text=str("Se registraron un total de {} errores".format(c))).pack(before=B_EXIT, side=LEFT)

    root.mainloop()



def deploy (msg, mode="cli", type="GENERAL"):
    # Despliega los mensajes de alerta del sistema
    # Modos de alerta:
    # cli       -> linea de comandos (por defecto)
    # windowed  -> modo visual

    alert_type = type

    if mode == "cli":
        if isinstance(msg, list) == True:
            # En caso de recibir una lista
            error_counter = 0

            for i in msg:
                error_counter += 1

            print("SE HAN ENCONTRADO:", error_counter, "ERRORES")
            print("".join(msg))
        elif isinstance(msg, str) == True:
            # En caso de recibir una cadena
            # (cadena = debug exitoso)
            pass
        elif isinstance(msg, dict) == True:
            # En caso de recibir un diccionario (METODO USADO)
            #print("\n\n{}\n\n".format(msg))
            for i in msg:
                print("".join(msg[i]))

    elif mode == "windowed":
        # Programar modo ventana (funcion: alert_emergent)
        if isinstance(msg, dict) == True:
            alert_emergent("Error de Compilacion", msg, type=alert_type)
