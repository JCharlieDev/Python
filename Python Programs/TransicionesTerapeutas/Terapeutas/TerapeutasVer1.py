from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import ImageTk, Image


login = Tk()
login.title("Login")
login.geometry("500x300")

def quit_me():
    login.quit()
    login.destroy()

#   Regresa la imagen por que el recolector de basura de python la elimina.
def mostrarImagen():

    global logo
    global labelLogo

    logo = ImageTk.PhotoImage(Image.open(RUTA DEL LOGO))
    labelLogo = Label(login, image=logo)
    labelLogo.grid(row=0, column=0, columnspan=3)

#   Regresa a la ventana Login
def regresar(ventana):

    login.wm_deiconify()

    mostrarImagen()

    ventana.destroy()

def reintentar():

    reintentarLogin = Toplevel()
    reintentarLogin.title("Advertencia")
    reintentarLogin.geometry("250x100")

    #   labels

    labelRegresar = Label(reintentarLogin, text="Usuario o Contraseña incorrecta...")
    labelRegresar.grid(row=0, column=0, pady=(30, 0))

    #   Boton para regresar al Login

    botonOk = Button(reintentarLogin, text="Regresar", command= lambda: regresar(reintentarLogin))
    botonOk.grid(row=1, column=0, padx=(10, 0), pady=(10, 0), ipadx=50, columnspan= 3)

    reintentarLogin.protocol("WM_DELETE_WINDOW", lambda: quit_me())

def adminLogin():

    adminLog = Toplevel()
    adminLog.title("Administrador")
    adminLog.geometry("500x300")

    global logo

    logo = ImageTk.PhotoImage(Image.open(RUTA DEL LOGO))
    labelLogo = Label(adminLog, image=logo)
    labelLogo.grid(row=0, column=0, columnspan=3)

    def regresarAdmin(ventana):

        global logo

        logo = ImageTk.PhotoImage(
            Image.open(RUTA DEL LOGO))
        labelLogo = Label(adminLog, image=logo)
        labelLogo.grid(row=0, column=0, columnspan=3)

        adminLog.deiconify()

        ventana.destroy()

    def salirAdmin():
        login.protocol("WM_DELETE_WINDOW", lambda: quit_me())
        adminLog.quit()

    #   Añade un "Terapeuta" a la base de datos.
    def agregarUsuario():

        #   Metodo que sube datos del terapeuta a la base de datos. Tambien crea el usuario para el login.
        def subirUsuario():

            #   Crea y/o se conecta a la base de datos
            conn = sqlite3.connect(RUTA DE LA BASE DE DATOS)
            #   Crea la instancia de un cursos para navegar sobre la base de datos
            cursor = conn.cursor()

            #   Añade el usuario a la base de datos "terapeuta".
            cursor.execute("Insert INTO terapeuta VALUES (:Nombre, :Apellido, :Direccion, :Ciudad, :Estado, :IDTerapeuta)",
                           {
                                'Nombre': textBoxNombre.get(),
                               'Apellido': textBoxApellido.get(),
                               'Direccion': textBoxDireccion.get(),
                               'Ciudad': textBoxCiudad.get(),
                               'Estado': textBoxEstado.get(),
                               'IDTerapeuta': textBoxIdTerapeuta.get()
                           })

            #   Crea el usuario para poder hacer Login
            cursor.execute("Insert INTO login VALUES (:Usuario, :Contrasena, :IDTerapeuta)",
                           {
                                'Usuario': textBoxNombre.get(),
                               'Contrasena': textBoxContrasenaTer.get(),
                               'IDTerapeuta': textBoxIdTerapeuta.get()
                           })

            #   Limpia las cajas de texto.
            textBoxNombre.delete(0, END)
            textBoxApellido.delete(0, END)
            textBoxDireccion.delete(0, END)
            textBoxCiudad.delete(0, END)
            textBoxEstado.delete(0, END)
            textBoxIdTerapeuta.delete(0, END)
            textBoxContrasenaTer.delete(0, END)

            #   Muestra una ventana con un mensaje de que se añadieron los datos a la base de datos.
            messagebox.showinfo("Some Message Box", "Usuario agregado con exito!")

            #   Confirma los cambios
            conn.commit()
            #   Cierra la conexion
            conn.close()

        #   Crea la ventana del menu del administrador.
        agregarUsuarioAdmin = Toplevel()
        agregarUsuarioAdmin.title("Agregar usuario")
        agregarUsuarioAdmin.geometry("500x375")

        adminLog.withdraw()

        global logo
        global labelLogo

        logo = ImageTk.PhotoImage(
            Image.open(RUTA DEL LOGO))
        labelLogo = Label(agregarUsuarioAdmin, image=logo)
        labelLogo.grid(row=0, column=0, columnspan=3)

        labelNombre = Label(agregarUsuarioAdmin, text = "Nombre :")
        labelNombre.grid(row = 1, column = 0)

        labelApellido = Label(agregarUsuarioAdmin, text = "Apellido :")
        labelApellido.grid(row = 2, column = 0)

        labelDireccion = Label(agregarUsuarioAdmin, text = "Direccion :")
        labelDireccion.grid(row = 3, column = 0)

        labelCiudad = Label(agregarUsuarioAdmin, text = "Ciudad :")
        labelCiudad.grid(row = 4, column = 0)

        labelEstado = Label(agregarUsuarioAdmin, text = "Estado :")
        labelEstado.grid(row = 5, column = 0)

        labelIdTerapeuta = Label(agregarUsuarioAdmin, text = "IDTerapeuta :")
        labelIdTerapeuta.grid(row = 6, column = 0)

        labelContrasenaTer = Label(agregarUsuarioAdmin, text = "Contraseña :")
        labelContrasenaTer.grid(row = 7, column = 0)

        #   TextBoxes para la ventana "Agregar usuario".

        textBoxNombre = Entry(agregarUsuarioAdmin, width = 20)
        textBoxNombre.grid(row = 1, column = 1, padx = 10)

        textBoxApellido = Entry(agregarUsuarioAdmin, width=20)
        textBoxApellido.grid(row=2, column=1, padx=10)

        textBoxDireccion = Entry(agregarUsuarioAdmin, width=20)
        textBoxDireccion.grid(row=3, column=1, padx=10)

        textBoxCiudad = Entry(agregarUsuarioAdmin, width=20)
        textBoxCiudad.grid(row=4, column=1, padx=10)

        textBoxEstado = Entry(agregarUsuarioAdmin, width=20)
        textBoxEstado.grid(row=5, column=1, padx=10)

        textBoxIdTerapeuta = Entry(agregarUsuarioAdmin, width=20)
        textBoxIdTerapeuta.grid(row=6, column=1, padx=10)

        textBoxContrasenaTer = Entry(agregarUsuarioAdmin, width=20)
        textBoxContrasenaTer.grid(row=7, column=1, padx=10)

        #   Botones de la ventana "Agregar Usuario".

        botonAnterior = Button(agregarUsuarioAdmin, text = "Aceptar", command= lambda : subirUsuario())
        botonAnterior.grid(row=8, column = 0, padx=(10, 0), pady=(10, 0), ipadx=50)

        botonAnterior = Button(agregarUsuarioAdmin, text = "Regresar", command = lambda : regresarAdmin(agregarUsuarioAdmin))
        botonAnterior.grid(row=8, column = 1, padx=(10, 0), pady=(10, 0), ipadx=50)

        def salirPrograma():
            agregarUsuarioAdmin.quit()
            agregarUsuarioAdmin.destroy()

        agregarUsuarioAdmin.protocol("WM_DELETE_WINDOW", lambda : salirPrograma())

    #   Botones y acciones del administrador

    botonAgregar = Button(adminLog, text="Agregar Usuario", command = lambda : agregarUsuario())
    botonAgregar.grid(row=1, column=0, padx=(10, 0), pady=(10, 0), ipadx=50)

    botonBorrar = Button(adminLog, text="Actualizar Usuario")
    botonBorrar.grid(row=1, column=1, padx=(10, 0), pady=(10, 0), ipadx=50)

    botonActualizar = Button(adminLog, text="Borrar Usuario")
    botonActualizar.grid(row=2, column=0, padx=(10, 0), pady=(10, 0), ipadx=50)

    botonSalir = Button(adminLog, text="Salir", command= lambda: salirAdmin())
    botonSalir.grid(row=2, column=1, padx=(10, 0), pady=(10, 0), ipadx=85)

    botonRegresar = Button(adminLog, text="Regresar", command= lambda: regresar(adminLog))
    botonRegresar.grid(row=3, column=1, padx=(10, 0), pady=(10, 0), ipadx=85)

    adminLog.protocol("WM_DELETE_WINDOW", lambda: quit_me())

def terapeutaLogin(usuario, ID):

    def salirTerapeuta():
        login.protocol("WM_DELETE_WINDOW", lambda: quit_me())
        terapeutaLog.quit()

    terapeutaLog = Toplevel()
    terapeutaLog.title("Bienvenido " + str(usuario) + "!")
    terapeutaLog.geometry("500x300")

    global logo

    logo = ImageTk.PhotoImage(Image.open(RUTA DEL LOGO))
    labelLogo = Label(terapeutaLog, image=logo)
    labelLogo.grid(row=0, column=0, columnspan=3)

    #   Botones y acciones del administrador

    botonSalir = Button(terapeutaLog, text="Salir", command= lambda: salirTerapeuta())
    botonSalir.grid(row=2, column=1, padx=(10, 0), pady=(10, 0), ipadx=85)

    botonRegresar = Button(terapeutaLog, text="Regresar", command= lambda: regresar(terapeutaLog))
    botonRegresar.grid(row=2, column=2, padx=(10, 0), pady=(10, 0), ipadx=85)

    terapeutaLog.protocol("WM_DELETE_WINDOW", lambda: quit_me())

def cerrarLogin():
    login.destroy()

def ingresarLogin():

    usuario = textBoxUsuario.get()
    contrasena = textBoxContrasena.get()

    #   Se conecta a la base de datos
    conn = sqlite3.connect(RUTA DE BASE DE DATOS)
    #   Crea instancia de un cursor
    cursor = conn.cursor()

    def buscarUsuario(usuario):

        existeUsuario = cursor.execute("""SELECT Usuario"
                           "FROM login "
                           "WHERE Usuario = :Usuario""",
                                      {
                                          'Usuario': usuario
                                          #    'Contrasena': contrasena
                                      })

        if usuario == existeUsuario:
            return True
        else:
            return False

    def isAdmin(usuario, contrasena):

        if usuario == "admin" and contrasena == "admin":
            return True
        else:
            return False


    loginUsuario = cursor.execute("""SELECT Usuario"
                   "FROM login "
                   "WHERE Usuario = :Usuario""",
                   {
                       'Usuario': usuario
                       #    'Contrasena': contrasena
                   })

    tipoUsuario = loginUsuario.fetchone()

    loginContrasena = cursor.execute("""SELECT Contrasena"
                   "FROM login "
                   "WHERE Contrasena = :Contrasena""",
                   {
                       #    'Usuario': usuario
                       'Contrasena': contrasena
                   })

    tipoContrasena = loginContrasena.fetchone()

    idTerapeuta = cursor.execute("""SELECT IDTerapeuta"
                   "FROM login "
                   "WHERE Contrasena = :Contrasena AND Usuario = :Usuario""",
                   {
                       'Usuario': usuario,
                       'Contrasena': contrasena
                   })

    tipoIDTerapeuta = idTerapeuta.fetchone()

    def limpiarCampos():

        textBoxContrasena.delete(0, END)
        textBoxUsuario.delete(0, END)

    try:

        if isAdmin(tipoUsuario[0], tipoContrasena[0]) == True:

            adminLogin()

            limpiarCampos()

        elif tipoUsuario[0] == usuario and tipoContrasena[0] == contrasena:

            terapeutaLogin(tipoUsuario[0], tipoIDTerapeuta)

            limpiarCampos()

    except:

        if buscarUsuario(usuario) == False:

            limpiarCampos()

            reintentar()

    login.withdraw()

    #   Hace los cambios
    conn.commit()
    #   Cierra conexion
    conn.close()


#   Crea y/o se conecta a la base de datos
conn = sqlite3.connect(RUTA DE BASE DE DATOS)
#   Crea una instancia de un cursor (forma de acceder a los comandos de sqlite)
cursor = conn.cursor()

#   Crea tablas en la base de datos
#   Crea la tabla Login (Usuario y contraseña para acceder

# cursor.execute("""CREATE TABLE login (
#     Usuario text,
#     Contrasena text,
#     IDTerapeuta integer
#     )""")
#
#
# cursor.execute("INSERT INTO login VALUES (:Usuario, :Contrasena, :IDTerapeuta)",
#                {
#                    'Usuario': "Terapeuta2",
#                    'Contrasena': "Terapeuta2",
#                    'IDTerapeuta': "003"
#                })
# #   Crea tabla con datos de los terapeutas
#
# cursor.execute("""CREATE TABLE terapeuta (
#     Nombre text,
#     Apellido text,
#     Direccion text,
#     Ciudad text,
#     Estado text,
#     IDTerapeuta text
#     )""")



#   ###################### Elementos del Login #######################

#   Login Logo
global logo
global labelLogo

logo = ImageTk.PhotoImage(Image.open(RUTA DEL LOGO))
labelLogo = Label(login, image = logo)
labelLogo.grid(row = 0, column = 0, columnspan = 3)

#   Login labels y logo

labelUsuario = Label(login, text = "Usuario:")
labelUsuario.grid(row = 1, column = 0, pady = (30, 0))

labelContrasena = Label(login, text = "Contraseña:")
labelContrasena.grid(row = 2, column = 0, pady = (10, 0))

#   Cajas de texto de Login

textBoxUsuario = Entry(login, width = 25)
textBoxUsuario.grid(row = 1, column = 1, pady = (30, 0))

textBoxContrasena = Entry(login, width = 25, show = "*")
textBoxContrasena.grid(row = 2, column = 1, pady = (10, 0))

#   Botones del Login

botonAceptar = Button(login, text = "Ingresar", command = lambda : ingresarLogin())
botonAceptar.grid(row = 3, column = 0, padx = (10, 0), pady = (10, 0), ipadx = 50)

botonCerrar = Button(login, text = "Cerrar", command = lambda : cerrarLogin())
botonCerrar.grid(row = 3, column = 1, padx = (10, 0), pady = (10, 0), ipadx = 50)

#   ###################### Elementos del Login #######################

#   Hace los cambios
conn.commit()

#   Cierra Conexion
conn.close()
login.mainloop()