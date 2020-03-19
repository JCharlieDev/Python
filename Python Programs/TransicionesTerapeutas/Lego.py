import tkinter as tk
from tkinter import messagebox
from tkinter import *

def validar():
    if entrada4.get()=="kodigo":
        abrirventana2()
    else:
        messagebox.showwarning("Cuidado", "Contraseña incorrecta")

def borrar():
    ventana5=tk.Tk()
    ventana5.title("Ventana 2.3")
    ventana5.iconbitmap("Ite.ico")
    ventana5.geometry("800x600")
    ventana5.configure(background="white")

    e1=tk.Label(ventana5, text="Confirmacion:", bg="white", fg="black")
    e1.pack(padx="5",pady="5",ipadx="5",ipady="5")
    e2=tk.Label(ventana5, text="¿Estas seguro de borrar la informacion?", bg="white", fg="black")
    e2.pack(padx="5",pady="5",ipadx="5",ipady="5")
    boton=tk.Button(ventana5,text="Si",fg="Black")
    boton.pack(padx="5",pady="5",ipadx="5",ipady="5")
    boton1=tk.Button(ventana5,text="No",fg="Black",command=ventana5.destroy)
    boton1.pack(padx="5",pady="5",ipadx="5",ipady="5")
    e3=tk.Label(ventana5, text="Si elegiste si, despues clickear boton (Cerrar), y los cambios se guardaran", bg="white", fg="black")
    e3.pack(padx="5",pady="5",ipadx="5",ipady="5")
    boton4=tk.Button(ventana5,text="Cerrar",fg="Black",command=ventana5.destroy)
    boton4.pack(padx="5",pady="5",ipadx="5",ipady="5")
    ventana5.mainloop()  
        
def abrirventana2():
        ventana.withdraw()
        win=tk.Toplevel()
        win.iconbitmap("Ite.ico")
        win.geometry("800x600")
        win.configure(background="white")
        win.title("Ventana 2")
        e3=tk.Label(win,text="Opciones de administrador",bg="white",fg="black")
        e3.pack(padx="5",pady="5",ipadx="5",ipady="5",fill=tk.X)
        e4=tk.Label(ventana, text="Opciones:", bg="white", fg="black")
        e4.pack(padx="10",pady="10",ipadx="10",ipady="10")
        boton=tk.Button(win,text="1-Alta:",fg="Black",command=abrirventana21)
        boton.pack(padx="5",pady="5",ipadx="5",ipady="5")
        boton1=tk.Button(win,text="2-Baja:",fg="Black",command=abrirventana22)
        boton1.pack(padx="5",pady="5",ipadx="5",ipady="5")
        boton4=tk.Button(win,text="3-Modificar:",fg="Black",command=abrirventana25)
        boton4.pack(padx="5",pady="5",ipadx="5",ipady="5")
        Boton2=tk.Button(win,text="Regresar",command=abrirventana1)
        Boton2.pack(padx="5",pady="5",ipadx="5",ipady="5")
        Boton3=tk.Button(win,text="Cerrar",command=win.destroy)
        Boton3.pack(padx="5",pady="5",ipadx="5",ipady="5")
        
        
def abrirventana22():
    
    ventana5=tk.Tk()
    ventana5.title("Ventana 2.2")
    ventana5.iconbitmap("Ite.ico")
    ventana5.geometry("800x600")
    ventana5.configure(background="white")

    e1=tk.Label(ventana5, text="Baja de terapeuta:", bg="white", fg="black")
    e1.pack(padx="5",pady="5",ipadx="5",ipady="5")
    var=tk.StringVar(ventana5)
    var.set("1 Terapeuta-Alias-")
    opciones=['1 Terapeuta-Alias', '2 Terapeuta-Alias','3 Terapeuta-Alias','4 Terapeuta-Alias']
    opcion=tk.OptionMenu(ventana5,var,*opciones)
    opcion.config(width=20)
    opcion.pack(side="left",padx=30, pady=30)
    boton=tk.Button(ventana5,text="Borrar",fg="Black",command=borrar)
    boton.pack(padx="5",pady="2",ipadx="5",ipady="5")
    boton2=tk.Button(ventana5,text="Cerrar",fg="Black",command=ventana5.destroy)
    boton2.pack(padx="5",pady="2",ipadx="10",ipady="10")
  


    ventana5.mainloop()  



def abrirventana25():
    
    ventana5=tk.Tk()
    ventana5.title("Ventana 2.2")
    ventana5.iconbitmap("Ite.ico")
    ventana5.geometry("800x600")
    ventana5.configure(background="white")

    e1=tk.Label(ventana5, text="Elige terapeuta a modificar:", bg="white", fg="black")
    e1.pack(padx="5",pady="5",ipadx="5",ipady="5")
    var=tk.StringVar(ventana5)
    var.set("1 Terapeuta-Alias-")
    opciones=['1 Terapeuta-Alias', '2 Terapeuta-Alias','3 Terapeuta-Alias','4 Terapeuta-Alias']
    opcion=tk.OptionMenu(ventana5,var,*opciones)
    opcion.config(width=20)
    opcion.pack(side="left",padx=30, pady=30)
    boton=tk.Button(ventana5,text="Modificar",fg="Black",command=abrirventana24)
    boton.pack(padx="5",pady="2",ipadx="5",ipady="5")
    boton2=tk.Button(ventana5,text="Cerrar",fg="Black",command=ventana5.destroy)
    boton2.pack(padx="5",pady="2",ipadx="10",ipady="10")
  
    ventana5.mainloop()  

def abrirventana24():
    
    ventana23=tk.Tk()
    ventana23.title("Ventana 2.1")
    ventana23.iconbitmap("Ite.ico")
    ventana23.geometry("800x600")
    ventana23.configure(background="white")
    e8=tk.Label(ventana23,text="Modificacion del terapeuta:",bg="white",fg="black")
    e8.pack(padx="5",pady="5",ipadx="5",ipady="5",fill=tk.X)
    e1=tk.Label(ventana23, text="Nombre:", bg="white", fg="black")
    e1.pack(padx="5",pady="2",ipadx="5",ipady="5")
    entrada1=tk.Entry(ventana23)
    entrada1.pack(fill=tk.X,padx="5",pady="2",ipadx="5",ipady="5")
    e4=tk.Label(ventana23, text="Apellido:", bg="white", fg="black")
    e4.pack(padx="5",pady="2",ipadx="5",ipady="5")
    entrada4=tk.Entry(ventana23)
    entrada4.pack(fill=tk.X,padx="5",pady="2",ipadx="5",ipady="5")
    e2=tk.Label(ventana23, text="Institucion:", bg="white", fg="black")
    e2.pack(padx="5",pady="2",ipadx="5",ipady="5")
    entrada2=tk.Entry(ventana23)
    entrada2.pack(fill=tk.X,padx="5",pady="2",ipadx="5",ipady="5")
    e3=tk.Label(ventana23, text="Especialidad:", bg="white", fg="black")
    e3.pack(padx="5",pady="2",ipadx="5",ipady="5")
    entrada3=tk.Entry(ventana23)
    entrada3.pack(fill=tk.X,padx="5",pady="2",ipadx="5",ipady="5")
    
    e5=tk.Label(ventana23, text="Correo:", bg="white", fg="black")
    e5.pack(padx="5",pady="2",ipadx="5",ipady="5")
    entrada5=tk.Entry(ventana23)
    entrada5.pack(fill=tk.X,padx="5",pady="2",ipadx="5",ipady="5")
    e6=tk.Label(ventana23, text="Telefono:", bg="white", fg="black")
    e6.pack(padx="5",pady="2",ipadx="5",ipady="5")
    entrada6=tk.Entry(ventana23)
    entrada6.pack(fill=tk.X,padx="5",pady="2",ipadx="5",ipady="5")
    e7=tk.Label(ventana23, text="Cedula:", bg="white", fg="black")
    e7.pack(padx="5",pady="2",ipadx="5",ipady="5")
    entrada7=tk.Entry(ventana23)
    entrada7.pack(fill=tk.X,padx="5",pady="2",ipadx="5",ipady="5")
    
    boton=tk.Button(ventana23,text="Guardar",fg="Black")
    boton.pack(padx="5",pady="5",ipadx="5",ipady="5")
    boton2=tk.Button(ventana23,text="Cerrar",fg="Black",command=ventana23.destroy)
    boton2.pack(padx="5",pady="5",ipadx="10",ipady="10")
    ventana23.mainloop()

def abrirventana21():
    
    ventana21=tk.Tk()
    ventana21.title("Ventana 2.1")
    ventana21.iconbitmap("Ite.ico")
    ventana21.geometry("800x600")
    ventana21.configure(background="white")
    e8=tk.Label(ventana21,text="Alta del terapeuta:",bg="white",fg="black")
    e8.pack(padx="5",pady="5",ipadx="5",ipady="5",fill=tk.X)
    e1=tk.Label(ventana21, text="Nombre:", bg="white", fg="black")
    e1.pack(padx="5",pady="2",ipadx="5",ipady="5")
    entrada1=tk.Entry(ventana21)
    entrada1.pack(fill=tk.X,padx="5",pady="2",ipadx="5",ipady="5")
    e4=tk.Label(ventana21, text="Apellido:", bg="white", fg="black")
    e4.pack(padx="5",pady="2",ipadx="5",ipady="5")
    entrada4=tk.Entry(ventana21)
    entrada4.pack(fill=tk.X,padx="5",pady="2",ipadx="5",ipady="5")
    e2=tk.Label(ventana21, text="Institucion:", bg="white", fg="black")
    e2.pack(padx="5",pady="2",ipadx="5",ipady="5")
    entrada2=tk.Entry(ventana21)
    entrada2.pack(fill=tk.X,padx="5",pady="2",ipadx="5",ipady="5")
    e3=tk.Label(ventana21, text="Especialidad:", bg="white", fg="black")
    e3.pack(padx="5",pady="2",ipadx="5",ipady="5")
    entrada3=tk.Entry(ventana21)
    entrada3.pack(fill=tk.X,padx="5",pady="2",ipadx="5",ipady="5")
    
    e5=tk.Label(ventana21, text="Correo:", bg="white", fg="black")
    e5.pack(padx="5",pady="2",ipadx="5",ipady="5")
    entrada5=tk.Entry(ventana21)
    entrada5.pack(fill=tk.X,padx="5",pady="2",ipadx="5",ipady="5")
    e6=tk.Label(ventana21, text="Telefono:", bg="white", fg="black")
    e6.pack(padx="5",pady="2",ipadx="5",ipady="5")
    entrada6=tk.Entry(ventana21)
    entrada6.pack(fill=tk.X,padx="5",pady="2",ipadx="5",ipady="5")
    e7=tk.Label(ventana21, text="Cedula:", bg="white", fg="black")
    e7.pack(padx="5",pady="2",ipadx="5",ipady="5")
    entrada7=tk.Entry(ventana21)
    entrada7.pack(fill=tk.X,padx="5",pady="2",ipadx="5",ipady="5")
    
    boton=tk.Button(ventana21,text="Guardar",fg="Black")
    boton.pack(padx="5",pady="2",ipadx="5",ipady="5")
    boton2=tk.Button(ventana21,text="Cerrar",fg="Black",command=ventana21.destroy)
    boton2.pack(padx="5",pady="2",ipadx="10",ipady="10")
    ventana21.mainloop()

def abrirventana1():
    
        ventana=tk.Tk()
        ventana.title("Ventana 1")
        ventana.iconbitmap("Ite.ico")
        ventana.geometry("800x600")
        ventana.configure(background="white")
        
        e9=tk.Label(ventana, text="Login:(Administrador)", bg="white", fg="black")
        e9.pack(padx="5",pady="1",ipadx="5",ipady="5")
        e1=tk.Label(ventana, text="Usuario:", bg="white", fg="black")
        e1.pack(padx="5",pady="1",ipadx="5",ipady="5")
        entrada1=tk.Entry(ventana)
        entrada1.pack(fill=tk.X,padx="5",pady="5",ipadx="5",ipady="5")
        e4=tk.Label(ventana, text="Contraseña:", bg="white", fg="black")
        e4.pack(padx="5",pady="5",ipadx="5",ipady="5")
        entrada4=tk.Entry(ventana)
        entrada4.pack(fill=tk.X,padx="5",pady="5",ipadx="5",ipady="5")
        boton=tk.Button(ventana,text="Validar",fg="Black",command=validar)
        boton.pack(padx="5",pady="5",ipadx="5",ipady="5")
        boton3=tk.Button(ventana,text="Cerrar",fg="Black",command=cerrarventana)
        boton3.pack(padx="5",pady="5",ipadx="5",ipady="5")
        
        e10=tk.Label(ventana, text="Login:(Terapeuta)", bg="white", fg="black")
        e10.pack(padx="5",pady="5",ipadx="5",ipady="5")
        e6=tk.Label(ventana, text="Usuario:", bg="white", fg="black")
        e6.pack(padx="5",pady="5",ipadx="5",ipady="5")
        entrada6=tk.Entry(ventana)
        entrada6.pack(fill=tk.X,padx="5",pady="5",ipadx="5",ipady="5")
        e7=tk.Label(ventana, text="Contraseña:", bg="white", fg="black")
        e7.pack(padx="5",pady="5",ipadx="5",ipady="5")
        entrada7=tk.Entry(ventana)
        entrada7.pack(fill=tk.X,padx="5",pady="5",ipadx="5",ipady="5")
        boton1=tk.Button(ventana,text="Validar",fg="Black",command=validar2)
        boton1.pack(padx="5",pady="5",ipadx="5",ipady="5")
        boton4=tk.Button(ventana,text="Cerrar",fg="Black",command=ventana.destroy)
        boton4.pack(padx="5",pady="5",ipadx="5",ipady="5")
        
        
        ventana.mainloop()

def validar2():
    if entrada7.get()=="cancerbero":
        abrirventana31()
    else:
        messagebox.showwarning("Cuidado", "Contraseña incorrecta")

def abrirventana31():
        ventana.withdraw()
        win=tk.Toplevel()
        win.iconbitmap("Ite.ico")
        win.geometry("800x600")
        win.configure(background="white")
        win.title("Ventana 2")
        e3=tk.Label(win,text="Opciones del terapeuta",bg="white",fg="black")
        e3.pack(padx="5",pady="5",ipadx="5",ipady="5",fill=tk.X)
        e4=tk.Label(ventana, text="Opciones:", bg="white", fg="black")
        e4.pack(padx="10",pady="10",ipadx="10",ipady="10")
        boton=tk.Button(win,text="1-Alta:(Paciente)",fg="Black",command=abrirventana32)
        boton.pack(padx="5",pady="5",ipadx="5",ipady="5")
        boton1=tk.Button(win,text="2-Sesiones de terapia:",fg="Black",command=abrirventana38)
        boton1.pack(padx="5",pady="5",ipadx="5",ipady="5")
        boton4=tk.Button(win,text="3-Estadistico:",fg="Black",command=abrirventana40)
        boton4.pack(padx="5",pady="5",ipadx="5",ipady="5")
        Boton2=tk.Button(win,text="Regresar",command=abrirventana1)
        Boton2.pack(padx="5",pady="5",ipadx="5",ipady="5")
        Boton3=tk.Button(win,text="Cerrar",command=win.destroy)
        Boton3.pack(padx="5",pady="5",ipadx="5",ipady="5")

def abrirventana32():
        ventana.withdraw()
        win=tk.Toplevel()
        win.iconbitmap("Ite.ico")
        win.geometry("800x600")
        win.configure(background="white")
        win.title("Ventana 2")
        e3=tk.Label(win,text="Opciones del paciente",bg="white",fg="black")
        e3.pack(padx="5",pady="5",ipadx="5",ipady="5",fill=tk.X)
        e4=tk.Label(ventana, text="Opciones:", bg="white", fg="black")
        e4.pack(padx="10",pady="10",ipadx="10",ipady="10")
        boton=tk.Button(win,text="1-Alta",fg="Black",command=abrirventana33)
        boton.pack(padx="5",pady="5",ipadx="5",ipady="5")
        boton1=tk.Button(win,text="2-Baja",fg="Black",command=abrirventana34)
        boton1.pack(padx="5",pady="5",ipadx="5",ipady="5")
        boton4=tk.Button(win,text="3-Modificacion:",fg="Black",command=abrirventana35)
        boton4.pack(padx="5",pady="5",ipadx="5",ipady="5")
        Boton3=tk.Button(win,text="Cerrar",command=win.destroy)
        Boton3.pack(padx="5",pady="5",ipadx="5",ipady="5")

def abrirventana33():
    
    ventana21=tk.Tk()
    ventana21.title("Ventana 2.1")
    ventana21.iconbitmap("Ite.ico")
    ventana21.geometry("800x600")
    ventana21.configure(background="white")
    e8=tk.Label(ventana21,text="Alta del paciente:",bg="white",fg="black")
    e8.pack(padx="5",pady="5",ipadx="5",ipady="5",fill=tk.X)
    e1=tk.Label(ventana21, text="Nombre:", bg="white", fg="black")
    e1.pack(padx="5",pady="2",ipadx="5",ipady="5")
    entrada1=tk.Entry(ventana21)
    entrada1.pack(fill=tk.X,padx="5",pady="2",ipadx="5",ipady="5")
    e4=tk.Label(ventana21, text="Apellido:", bg="white", fg="black")
    e4.pack(padx="5",pady="2",ipadx="5",ipady="5")
    entrada4=tk.Entry(ventana21)
    entrada4.pack(fill=tk.X,padx="5",pady="2",ipadx="5",ipady="5")
    e2=tk.Label(ventana21, text="Edad:", bg="white", fg="black")
    e2.pack(padx="5",pady="2",ipadx="5",ipady="5")
    entrada2=tk.Entry(ventana21)
    entrada2.pack(fill=tk.X,padx="5",pady="2",ipadx="5",ipady="5")
    e3=tk.Label(ventana21, text="Diagnostico (Medico):", bg="white", fg="black")
    e3.pack(padx="5",pady="2",ipadx="5",ipady="5")
    entrada3=tk.Entry(ventana21)
    entrada3.pack(fill=tk.X,padx="5",pady="2",ipadx="5",ipady="5")
    
    e5=tk.Label(ventana21, text="Tratamiento (Terapeuta)", bg="white", fg="black")
    e5.pack(padx="5",pady="2",ipadx="5",ipady="5")
    entrada5=tk.Entry(ventana21)
    entrada5.pack(fill=tk.X,padx="5",pady="2",ipadx="5",ipady="5")
    
    
    boton=tk.Button(ventana21,text="Guardar",fg="Black")
    boton.pack(padx="5",pady="2",ipadx="5",ipady="5")
    boton2=tk.Button(ventana21,text="Cerrar",fg="Black",command=ventana21.destroy)
    boton2.pack(padx="5",pady="2",ipadx="10",ipady="10")
    ventana21.mainloop()    

def abrirventana34():
    
    ventana5=tk.Tk()
    ventana5.title("Ventana 2.2")
    ventana5.iconbitmap("Ite.ico")
    ventana5.geometry("800x600")
    ventana5.configure(background="white")

    e1=tk.Label(ventana5, text="Baja del paciente:", bg="white", fg="black")
    e1.pack(padx="5",pady="5",ipadx="5",ipady="5")
    var=tk.StringVar(ventana5)
    var.set("1 Paciente-Alias-")
    opciones=['1 Paciente-Alias', '2 Paciente-Alias','3 Paciente-Alias','4 Paciente-Alias']
    opcion=tk.OptionMenu(ventana5,var,*opciones)
    opcion.config(width=20)
    opcion.pack(side="left",padx=30, pady=30)
    boton=tk.Button(ventana5,text="Borrar",fg="Black",command=borrar2)
    boton.pack(padx="5",pady="2",ipadx="5",ipady="5")
    boton2=tk.Button(ventana5,text="Cerrar",fg="Black",command=ventana5.destroy)
    boton2.pack(padx="5",pady="2",ipadx="10",ipady="10")
  


    ventana5.mainloop()  

def abrirventana35():
    
    ventana5=tk.Tk()
    ventana5.title("Ventana 2.2")
    ventana5.iconbitmap("Ite.ico")
    ventana5.geometry("800x600")
    ventana5.configure(background="white")

    e1=tk.Label(ventana5, text="Elige paciente a modificar:", bg="white", fg="black")
    e1.pack(padx="5",pady="5",ipadx="5",ipady="5")
    var=tk.StringVar(ventana5)
    var.set("1 Paciente-Alias-")
    opciones=['1 Paciente-Alias', '2 Paciente-Alias','3 Paciente-Alias','4 Paciente-Alias']
    opcion=tk.OptionMenu(ventana5,var,*opciones)
    opcion.config(width=20)
    opcion.pack(side="left",padx=30, pady=30)
    boton=tk.Button(ventana5,text="Modificar",fg="Black",command=abrirventana33)
    boton.pack(padx="5",pady="2",ipadx="5",ipady="5")
    boton2=tk.Button(ventana5,text="Cerrar",fg="Black",command=ventana5.destroy)
    boton2.pack(padx="5",pady="2",ipadx="10",ipady="10")
  
    ventana5.mainloop()  

def borrar2():
    ventana5=tk.Tk()
    ventana5.title("Ventana 2.3")
    ventana5.iconbitmap("Ite.ico")
    ventana5.geometry("800x600")
    ventana5.configure(background="white")

    e1=tk.Label(ventana5, text="Confirmacion:", bg="white", fg="black")
    e1.pack(padx="5",pady="5",ipadx="5",ipady="5")
    e2=tk.Label(ventana5, text="¿Estas seguro de borrar la informacion?", bg="white", fg="black")
    e2.pack(padx="5",pady="5",ipadx="5",ipady="5")
    boton=tk.Button(ventana5,text="Si",fg="Black")
    boton.pack(padx="5",pady="5",ipadx="5",ipady="5")
    boton1=tk.Button(ventana5,text="No",fg="Black",command=ventana5.destroy)
    boton1.pack(padx="5",pady="5",ipadx="5",ipady="5")
    e3=tk.Label(ventana5, text="Si elegiste si, despues clickear boton (Cerrar), y los cambios se guardaran", bg="white", fg="black")
    e3.pack(padx="5",pady="5",ipadx="5",ipady="5")
    boton4=tk.Button(ventana5,text="Cerrar",fg="Black",command=ventana5.destroy)
    boton4.pack(padx="5",pady="5",ipadx="5",ipady="5")
    ventana5.mainloop()  

def abrirventana38():
    
    ventana5=tk.Tk()
    ventana5.title("Ventana 2.2")
    ventana5.iconbitmap("Ite.ico")
    ventana5.geometry("800x600")
    ventana5.configure(background="white")

    e1=tk.Label(ventana5, text="Elegir paciente en terapia:", bg="white", fg="black")
    e1.pack(padx="5",pady="5",ipadx="5",ipady="5")
    var=tk.StringVar(ventana5)
    var.set("1 Paciente-Alias-")
    opciones=['1 Paciente-Alias', '2 Paciente-Alias','3 Paciente-Alias','4 Paciente-Alias']
    opcion=tk.OptionMenu(ventana5,var,*opciones)
    opcion.config(width=20)
    opcion.pack(side="left",padx=30, pady=30)
    e2=tk.Label(ventana5, text="Calibracion de dispositivo (Avanzada).", bg="white", fg="black")
    e2.pack(padx="5",pady="5",ipadx="5",ipady="5")
    boton3=tk.Button(ventana5,text="Seleccionar",fg="Black",command=abrirventana39)
    boton3.pack(padx="5",pady="2",ipadx="10",ipady="10")
    boton2=tk.Button(ventana5,text="Cerrar",fg="Black",command=ventana5.destroy)
    boton2.pack(padx="5",pady="2",ipadx="10",ipady="10")
  
    ventana5.mainloop()  

def abrirventana39():
    
    ventana21=tk.Tk()
    ventana21.title("Ventana 2.1")
    ventana21.iconbitmap("Ite.ico")
    ventana21.geometry("800x600")
    ventana21.configure(background="white")
    e8=tk.Label(ventana21,text="Calibracion de dispositivo:",bg="white",fg="black")
    e8.pack(padx="5",pady="1",ipadx="5",ipady="1",fill=tk.X)
    e1=tk.Label(ventana21, text="Angulo Calculado (Dispositivo 1)", bg="white", fg="black")
    e1.pack(padx="5",pady="1",ipadx="5",ipady="1")
    e4=tk.Label(ventana21, text="Cadera:", bg="white", fg="black")
    e4.pack(padx="5",pady="1",ipadx="5",ipady="1")
    entrada4=tk.Entry(ventana21)
    entrada4.pack(fill=tk.X,padx="5",pady="2",ipadx="5",ipady="1")
    e2=tk.Label(ventana21, text="Rodilla:", bg="white", fg="black")
    e2.pack(padx="5",pady="1",ipadx="5",ipady="5")
    entrada2=tk.Entry(ventana21)
    entrada2.pack(fill=tk.X,padx="5",pady="2",ipadx="5",ipady="1")
    e3=tk.Label(ventana21, text="Tobillo:", bg="white", fg="black")
    e3.pack(padx="5",pady="1",ipadx="5",ipady="1")
    entrada3=tk.Entry(ventana21)
    entrada3.pack(fill=tk.X,padx="5",pady="1",ipadx="5",ipady="1")
    
    e15=tk.Label(ventana21, text="Porcentaje de reduccion %", bg="white", fg="black")
    e15.pack(padx="5",pady="1",ipadx="5",ipady="1")
    entrada15=tk.Entry(ventana21)
    entrada15.pack(fill=tk.X,padx="5",pady="1",ipadx="5",ipady="1")
    
    e11=tk.Label(ventana21, text="Angulo Maximo Terapia (Dispositivo 2)", bg="white", fg="black")
    e11.pack(padx="5",pady="1",ipadx="5",ipady="1")
    e5=tk.Label(ventana21, text="Cadera:", bg="white", fg="black")
    e5.pack(padx="5",pady="1",ipadx="5",ipady="1")
    entrada5=tk.Entry(ventana21)
    entrada5.pack(fill=tk.X,padx="5",pady="2",ipadx="5",ipady="1")
    
    e6=tk.Label(ventana21, text="Rodilla:", bg="white", fg="black")
    e6.pack(padx="5",pady="1",ipadx="5",ipady="1")
    entrada6=tk.Entry(ventana21)
    entrada6.pack(fill=tk.X,padx="5",pady="2",ipadx="5",ipady="1")
    e12=tk.Label(ventana21, text="Tobillo:", bg="white", fg="black")
    e12.pack(padx="5",pady="1",ipadx="5",ipady="1")
    entrada12=tk.Entry(ventana21)
    entrada12.pack(fill=tk.X,padx="5",pady="2",ipadx="5",ipady="1")
    e14=tk.Label(ventana21, text="Tiempo de terapia (min):", bg="white", fg="black")
    e14.pack(padx="5",pady="1",ipadx="5",ipady="1")
    entrada14=tk.Entry(ventana21)
    entrada14.pack(fill=tk.X,padx="5",pady="1",ipadx="5",ipady="1")
    boton=tk.Button(ventana21,text="Guardar-Iniciar",fg="Black")
    boton.pack(padx="5",pady="1",ipadx="5",ipady="1")
    boton2=tk.Button(ventana21,text="Cerrar",fg="Black",command=ventana21.destroy)
    boton2.pack(padx="5",pady="1",ipadx="5",ipady="1")
    boton3=tk.Button(ventana21,text="Opinion Online",fg="Black",command=ventanaopinion)
    boton3.pack(padx="5",pady="1",ipadx="5",ipady="1")
    ventana21.mainloop()    

def abrirventana40 ():

    ventana=tk.Tk()
    ventana.title("Ventana 1")
    ventana.iconbitmap("Ite.ico")
    ventana.geometry("800x600")
    ventana.configure(background="white")
    
    e9=tk.Label(ventana, text="Estadisticas", bg="white", fg="black")
    e9.pack(padx="5",pady="1",ipadx="5",ipady="5")
    
    #miImagen=tk.PhotoImage(file="Excel.png")
    #Declaramos una imagen y indicamos ubicacion
    #Label1= Label(ventana, image=miImagen)
    #Indicamos su localizacion y el tipo de objeto que se mostrara
    #Label1.pack()
    ventana.mainloop()
    
    #image=tk.PhotoImage(file="logo.png")
   # image=image.subsample(4,8)
   # Label=tk.Label(image=image)
    #Label.place(x=0,y=0,relwidth=1.0,relheight=1.0)
    #Label.pack()
    
    
    
    
    
   


def ventanaopinion():
    ventana21=tk.Tk()
    ventana21.title("Ventana 2.1")
    ventana21.iconbitmap("Ite.ico")
    ventana21.iconbitmap("Ite.ico")
    ventana21.geometry("800x600")
    ventana21.configure(background="white")
    e8=tk.Label(ventana21,text="¿Como me siento?",bg="white",fg="black")
    e8.pack(padx="5",pady="1",ipadx="5",ipady="5",fill=tk.X)
    boton=tk.Button(ventana21,text="Bien",fg="Blue")
    boton.pack(padx="5",pady="1",ipadx="5",ipady="5")
    boton2=tk.Button(ventana21,text="Mal",fg="Red",command=ventana21.destroy)
    boton2.pack(padx="5",pady="1",ipadx="10",ipady="10")
    boton3=tk.Button(ventana21,text="Cerrar",fg="Red",command=ventana21.destroy)
    boton3.pack(padx="5",pady="1",ipadx="10",ipady="10")
    
def cerrarventana():
    ventana.destroy()

ventana=tk.Tk()
ventana.title("Ventana 1")
ventana.iconbitmap("Ite.ico")
ventana.geometry("800x600")
ventana.configure(background="white")


image=tk.PhotoImage(file="logo.png")
image=image.subsample(4,8)
Label=tk.Label(image=image)
#Label.place(x=0,y=0,relwidth=1.0,relheight=1.0)
Label.pack()


e9=tk.Label(ventana, text="Login:(Administrador)", bg="white", fg="black")
e9.pack(padx="5",pady="1",ipadx="5",ipady="5")
e1=tk.Label(ventana, text="Usuario:", bg="white", fg="black")
e1.pack(padx="5",pady="1",ipadx="5",ipady="5")
entrada1=tk.Entry(ventana)
entrada1.pack(fill=tk.X,padx="5",pady="5",ipadx="5",ipady="5")
e4=tk.Label(ventana, text="Contraseña:", bg="white", fg="black", font=20)
e4.pack(padx="5",pady="5",ipadx="5",ipady="5")
entrada4=tk.Entry(ventana)
entrada4.pack(fill=tk.X,padx="5",pady="5",ipadx="5",ipady="5")
boton=tk.Button(ventana,text="Validar",fg="Black",command=validar)
boton.pack(padx="5",pady="5",ipadx="5",ipady="5")
boton3=tk.Button(ventana,text="Cerrar",fg="Black",command=cerrarventana)
boton3.pack(padx="5",pady="5",ipadx="5",ipady="5")

e10=tk.Label(ventana, text="Login:(Terapeuta)", bg="white", fg="black")
e10.pack(padx="5",pady="5",ipadx="5",ipady="5")
e6=tk.Label(ventana, text="Usuario:", bg="white", fg="black")
e6.pack(padx="5",pady="5",ipadx="5",ipady="5")
entrada6=tk.Entry(ventana)
entrada6.pack(fill=tk.X,padx="5",pady="5",ipadx="5",ipady="5")
e7=tk.Label(ventana, text="Contraseña:", bg="white", fg="black")
e7.pack(padx="5",pady="5",ipadx="5",ipady="5")
entrada7=tk.Entry(ventana)
entrada7.pack(fill=tk.X,padx="5",pady="5",ipadx="5",ipady="5")
boton1=tk.Button(ventana,text="Validar",fg="Black",command=validar2)
boton1.pack(padx="5",pady="5",ipadx="5",ipady="5")
boton4=tk.Button(ventana,text="Cerrar",fg="Black",command=ventana.destroy)
boton4.pack(padx="5",pady="5",ipadx="5",ipady="5")



ventana.mainloop()
