from tkinter import messagebox

def alert_emergent (title, msg):
    messagebox.showerror(title, msg)

def deploy (msg):
    # Despliega los mensajes de alerta del sistema
    print(msg)
