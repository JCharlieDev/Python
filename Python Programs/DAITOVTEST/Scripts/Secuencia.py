from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Secuencia Tests")
root.geometry("500x300")

def intentos():



    intento = Toplevel()
    intento.title("Intento")
    intento.geometry("500x300")

    intento.focus_force()
    intento.grab_set()


    botonAcerto = Button(intento, text="Acerto")
    botonNoAcerto = Button(intento, text="No Acerto")

    botonAcerto.grid(row = 0, column = 0, ipadx = 50, pady = 10, padx = 10)
    botonNoAcerto.grid(row = 0, column = 1, ipadx = 50, pady = 10)

    # Label(root, text = response).pack()

    # if response == 1:
    #     Label(root, text = "You clicked Yes!").pack()
    # else:
    #     Label(root, text = "You clicked No...").pack()

Button(root, text = "Test Intento", command = lambda: intentos()).pack()



root.mainloop()




#
#         CA=0 #Contador de actividad
#         #Realizar cada Actividad dentro de la tarea
#         for Actividad in lista_Actividades:
#             if Actividad != "":
#                 #Buscar Info de prendas
#
#                 CA=CA+1
#
#                 Query="SELECT * FROM TB_ACTIVIDADES WHERE   Escenario = '"+ Escenario + "' AND Actividad = '"+ Actividad +"'"
#                 cursor.execute(Query)
#                 rows = cursor.fetchall()
#                 for row  in rows:
#                     Actividad1=row[2]
#                     PrendaSuperior=row[3]
#                     PS_Cierre=row[4]
#                     PS_NumCierres=row[5]
#                     PrendaInferior=row[6]
#                     PI_Cierre=row[7]
#                     PI_NumCierres=row[8]
#                     Zapato=row[9]
#                     Z_Cierre=row[10]
#                     Z_NumCierres=row[11]
#
# ####################### Inicio de Actividad (print en pantalla)  ##########################################
#
#             #Iniciar Actividad
#
#             Prefijo=""
#
#             if Actividad=="noche":
#                 Prefijo="N"
#             elif Actividad=="calor":
#                 Prefijo="C"
#             elif Actividad=="frio":
#                 Prefijo="F"
#             else:
#                 Prefijo="L"
#
#
#             #Encender luz
#             if ApoyoVisual==1:
#                 if Prefijo=="N":
#                     print ("encender foco noche")
#                 elif Prefijo=="C":
#                     print ("encender foco calor")
#                 elif Prefijo=="F":
#                     print ("encender foco frio")
#                 else:
#                     print("encender foco lluvia")
#
#
#             #Encender apoyo haptico
#             if ApoyoHaptico==1:
#                 if Prefijo=="C":
#                     print ("encender calentón")
#                 elif Prefijo=="F":
#                     print ("encender abanico")
#                 else:
#                     print("encender aspersor")
#
#             #Anunciar la actividad
#             if Prefijo!="N":
#                 titulo=self.titulos(Prefijo, CA,0,0)
#             else:
#                 titulo=self.titulos(Prefijo, 0,1,0)
#                 self.playvideo("F0_resized", "F0", 20)
#             print (titulo)
#
#             #Quitar la ropa anterior
#             if CA>1:
#                 print("quitar ropa anterior")
#
#             #Describir atuendo
#             titulo=self.titulos(Prefijo, 0,4,0)
#             self.playvideo("F3_resized", "F3", 20)
#             print (titulo)
#
#             titulo=self.titulos(Prefijo, 0,5,0)
#             self.playvideo("F4_resized", "F4", 20)
#             print (titulo)
#
#             titulo=self.titulos(Prefijo, 0,6,0)
#             self.playvideo("F11_resized", "F11", 20)
#             print (titulo)
#
#             if Prefijo!="N":
#                 titulo=self.titulos(Prefijo, 0,7,0)
#                 self.playvideo("F13_resized", "F13", 25)
#             print (titulo)
#
# ##            **************************************************************************************************************
#             #Prenda Superior
#
#             #revisar si el atuendo lleva prenda Superior
#             Query="SELECT PS FROM TB_ACTIVIDADES WHERE   Escenario = '"+ Escenario + "' AND Actividad = '"+ Actividad +"'"
#             cursor.execute(Query)
#             rows = cursor.fetchall()
#             for row  in rows:
#                  #print ("Tipo de prenda="+ str(row[0]))
#                  Prenda=row[0]
#
#             if (Prenda!=""):
#                  #Colocar prenda Superior
#                 PS=self.ColocarPrenda(Prefijo,"Superior")
#
#                 PS=1#BORRAR**
#                 if PS==1:
#                      print("La prenda Superior para: "+ Prefijo +" se ha colocado correctamente")
#
#                  #Revisar la cantidad de broches mediante query
#                 Query="SELECT PSNC FROM TB_ACTIVIDADES WHERE   Escenario = '"+ Escenario + "' AND Actividad = '"+ Actividad +"'"
#                 cursor.execute(Query)
#                 rows = cursor.fetchall()
#                 for row  in rows:
#                     print ("numero de broches="+ str(row[0]))
#                     CantidadBroches=row[0]
#
#                 if PS==1:
#                     #Abrochar prenda
#                     self.ColocarBrochesPrenda(Prefijo,CantidadBroches,"Superior")
#
# ##            **************************************************************************************************************
#             #Prenda Inferior
#
#             Query="SELECT PI FROM TB_ACTIVIDADES WHERE   Escenario = '"+ Escenario + "' AND Actividad = '"+ Actividad +"'"
#             cursor.execute(Query)
#             rows = cursor.fetchall()
#             for row  in rows:
#                 print ("Tipo de prenda="+ str(row[0]))
#                 Prenda=row[0]
#
#             if (Prenda!=""):
#
#                 #Colocar prenda Superior
#                 PI=self.ColocarPrenda(Prefijo,"Inferior")
#
#                 PI=1#BORRAR**
#                 if PI==1:
#                      print("La prenda Inferior para: "+ Prefijo +" se ha colocado correctamente")
#
#
#                  #Revisar la cantidad de broches mediante query
#                 Query="SELECT PINC FROM TB_ACTIVIDADES WHERE   Escenario = '"+ Escenario + "' AND Actividad = '"+ Actividad +"'"
#                 cursor.execute(Query)
#                 rows = cursor.fetchall()
#                 for row  in rows:
#                     print ("numero de broches en PI="+ str(row[0]))
#                     CantidadBroches=row[0]
#
#                 if PI==1:
#                     self.ColocarBrochesPrenda(Prefijo,CantidadBroches,"Inferior")
#
#             #Zapato1
#
#             #revisar si el atuendo lleva prenda Zapatos
#             Query="SELECT Z FROM TB_ACTIVIDADES WHERE   Escenario = '"+ Escenario + "' AND Actividad = '"+ Actividad +"'"
#             cursor.execute(Query)
#             rows = cursor.fetchall()
#             for row  in rows:
#                  print ("Tipo de prenda="+ str(row[0]))
#                  Prenda=row[0]
#
#             if (Prenda!=""):
#                  #Colocar primer zapatos
#                 Z=self.ColocarPrenda(Prefijo,"zapato")
#
#                 #Leer zapato Derecho e Izquierdo
#                 ZD=1#BORRAR**
#                 ZI=1#BORRAR**
#
#                 if ZD==1:
#                      print("El zapato para: "+ Prefijo +" se ha colocado correctamente")
#                 elif ZD==1:
#                      print("El zapato para: "+ Prefijo +" se ha colocado correctamente")
#
#                  #Revisar la cantidad de broches mediante query
#                 Query="SELECT ZNC FROM TB_ACTIVIDADES WHERE   Escenario = '"+ Escenario + "' AND Actividad = '"+ Actividad +"'"
#                 cursor.execute(Query)
#                 rows = cursor.fetchall()
#                 for row  in rows:
#                     print ("numero de broches="+ str(row[0]))
#                     CantidadBroches=row[0]
#
#                 if ZI==1:
#                     #Abrochar prenda
#                     print("Abrochar zapato Izquierdo")
#                     #self.ColocarBrochesPS(Prefijo,CantidadBroches,"zapato")
#                 elif ZD==1:
#
#                     print("Abrochar zapato Derecho ")
#
#             #Apagar apoyo haptico
#             print ("Apagar todos los apoyos hápticos")
#
#             #A jugar

###################### Fin de de Actividad (print en pantalla)  ########################################




























































#         #Abrir base de datos
#         conn = sqlite3.connect("D:\\GitHub Repos\\Python\\Python Programs\\DAITOVTEST\\Resources\\Database\\db_DAITOV2.db")
#         cursor = conn.cursor()
#         rows = cursor.fetchall()
#
#         #Leer Tarea
#         Query="SELECT * FROM TB_ProgramacionTarea WHERE   ID_Programacion = (SELECT MAX(ID_Programacion)  FROM TB_ProgramacionTarea);"
#
#         cursor.execute(Query)
#         rows = cursor.fetchall()
#
#         for row  in rows:
#             Id_Usuario=row[1]
#             Escenario=row[2]
#             #Apoyos activados
#             ApoyoAuditivo=row[3]
#             ApoyoVisual=row[4]
#             ApoyoHaptico=row[5]
#             #Leer las actividades
#             lista_Actividades=[row[6],row[7],row[8],row[9]]
#             print ("Id_Usuario=", Id_Usuario)
#             print ("Escenario=", Escenario)
#             print ("ApoyoAuditivo=", ApoyoAuditivo)
#             print ("ApoyoVisual=", ApoyoVisual)
#             print ("ApoyoHaptico=", ApoyoHaptico)
#             print("Secuencia=",lista_Actividades)
#
#
#         CA=0 #Contador de actividad
#         #Realizar cada Actividad dentro de la tarea
#         for Actividad in lista_Actividades:
#             if Actividad != "":
#                 #Buscar Info de prendas
#
#                 CA=CA+1
#
#                 Query="SELECT * FROM TB_ACTIVIDADES WHERE   Escenario = '"+ Escenario + "' AND Actividad = '"+ Actividad +"'"
#                 cursor.execute(Query)
#                 rows = cursor.fetchall()
#                 for row  in rows:
#                     Actividad1=row[2]
#                     PrendaSuperior=row[3]
#                     PS_Cierre=row[4]
#                     PS_NumCierres=row[5]
#                     PrendaInferior=row[6]
#                     PI_Cierre=row[7]
#                     PI_NumCierres=row[8]
#                     Zapato=row[9]
#                     Z_Cierre=row[10]
#                     Z_NumCierres=row[11]
#
# ####################### Inicio de Actividad (print en pantalla)  ##########################################
#
#             #Iniciar Actividad
#
#             Prefijo=""
#
#             if Actividad=="noche":
#                 Prefijo="N"
#             elif Actividad=="calor":
#                 Prefijo="C"
#             elif Actividad=="frio":
#                 Prefijo="F"
#             else:
#                 Prefijo="L"
#
#
#             #Encender luz
#             if ApoyoVisual==1:
#                 if Prefijo=="N":
#                     print ("encender foco noche")
#                 elif Prefijo=="C":
#                     print ("encender foco calor")
#                 elif Prefijo=="F":
#                     print ("encender foco frio")
#                 else:
#                     print("encender foco lluvia")
#
#
#             #Encender apoyo haptico
#             if ApoyoHaptico==1:
#                 if Prefijo=="C":
#                     print ("encender calentón")
#                 elif Prefijo=="F":
#                     print ("encender abanico")
#                 else:
#                     print("encender aspersor")
#
#             #Anunciar la actividad
#             if Prefijo!="N":
#                 titulo=self.titulos(Prefijo, CA,0,0)
#             else:
#                 titulo=self.titulos(Prefijo, 0,1,0)
#                 self.playvideo("F0_resized", "F0", 20)
#             print (titulo)
#
#             #Quitar la ropa anterior
#             if CA>1:
#                 print("quitar ropa anterior")
#
#             #Describir atuendo
#             titulo=self.titulos(Prefijo, 0,4,0)
#             self.playvideo("F3_resized", "F3", 20)
#             print (titulo)
#
#             titulo=self.titulos(Prefijo, 0,5,0)
#             self.playvideo("F4_resized", "F4", 20)
#             print (titulo)
#
#             titulo=self.titulos(Prefijo, 0,6,0)
#             self.playvideo("F11_resized", "F11", 20)
#             print (titulo)
#
#             if Prefijo!="N":
#                 titulo=self.titulos(Prefijo, 0,7,0)
#                 self.playvideo("F13_resized", "F13", 25)
#             print (titulo)
#
# ##            **************************************************************************************************************
#             #Prenda Superior
#
#             #revisar si el atuendo lleva prenda Superior
#             Query="SELECT PS FROM TB_ACTIVIDADES WHERE   Escenario = '"+ Escenario + "' AND Actividad = '"+ Actividad +"'"
#             cursor.execute(Query)
#             rows = cursor.fetchall()
#             for row  in rows:
#                  #print ("Tipo de prenda="+ str(row[0]))
#                  Prenda=row[0]
#
#             if (Prenda!=""):
#                  #Colocar prenda Superior
#                 PS=self.ColocarPrenda(Prefijo,"Superior")
#
#                 PS=1#BORRAR**
#                 if PS==1:
#                      print("La prenda Superior para: "+ Prefijo +" se ha colocado correctamente")
#
#                  #Revisar la cantidad de broches mediante query
#                 Query="SELECT PSNC FROM TB_ACTIVIDADES WHERE   Escenario = '"+ Escenario + "' AND Actividad = '"+ Actividad +"'"
#                 cursor.execute(Query)
#                 rows = cursor.fetchall()
#                 for row  in rows:
#                     print ("numero de broches="+ str(row[0]))
#                     CantidadBroches=row[0]
#
#                 if PS==1:
#                     #Abrochar prenda
#                     self.ColocarBrochesPrenda(Prefijo,CantidadBroches,"Superior")
#
# ##            **************************************************************************************************************
#             #Prenda Inferior
#
#             Query="SELECT PI FROM TB_ACTIVIDADES WHERE   Escenario = '"+ Escenario + "' AND Actividad = '"+ Actividad +"'"
#             cursor.execute(Query)
#             rows = cursor.fetchall()
#             for row  in rows:
#                 print ("Tipo de prenda="+ str(row[0]))
#                 Prenda=row[0]
#
#             if (Prenda!=""):
#
#                 #Colocar prenda Superior
#                 PI=self.ColocarPrenda(Prefijo,"Inferior")
#
#                 PI=1#BORRAR**
#                 if PI==1:
#                      print("La prenda Inferior para: "+ Prefijo +" se ha colocado correctamente")
#
#
#                  #Revisar la cantidad de broches mediante query
#                 Query="SELECT PINC FROM TB_ACTIVIDADES WHERE   Escenario = '"+ Escenario + "' AND Actividad = '"+ Actividad +"'"
#                 cursor.execute(Query)
#                 rows = cursor.fetchall()
#                 for row  in rows:
#                     print ("numero de broches en PI="+ str(row[0]))
#                     CantidadBroches=row[0]
#
#                 if PI==1:
#                     self.ColocarBrochesPrenda(Prefijo,CantidadBroches,"Inferior")
#
#             #Zapato1
#
#             #revisar si el atuendo lleva prenda Zapatos
#             Query="SELECT Z FROM TB_ACTIVIDADES WHERE   Escenario = '"+ Escenario + "' AND Actividad = '"+ Actividad +"'"
#             cursor.execute(Query)
#             rows = cursor.fetchall()
#             for row  in rows:
#                  print ("Tipo de prenda="+ str(row[0]))
#                  Prenda=row[0]
#
#             if (Prenda!=""):
#                  #Colocar primer zapatos
#                 Z=self.ColocarPrenda(Prefijo,"zapato")
#
#                 #Leer zapato Derecho e Izquierdo
#                 ZD=1#BORRAR**
#                 ZI=1#BORRAR**
#
#                 if ZD==1:
#                      print("El zapato para: "+ Prefijo +" se ha colocado correctamente")
#                 elif ZD==1:
#                      print("El zapato para: "+ Prefijo +" se ha colocado correctamente")
#
#                  #Revisar la cantidad de broches mediante query
#                 Query="SELECT ZNC FROM TB_ACTIVIDADES WHERE   Escenario = '"+ Escenario + "' AND Actividad = '"+ Actividad +"'"
#                 cursor.execute(Query)
#                 rows = cursor.fetchall()
#                 for row  in rows:
#                     print ("numero de broches="+ str(row[0]))
#                     CantidadBroches=row[0]
#
#                 if ZI==1:
#                     #Abrochar prenda
#                     print("Abrochar zapato Izquierdo")
#                     #self.ColocarBrochesPS(Prefijo,CantidadBroches,"zapato")
#                 elif ZD==1:
#
#                     print("Abrochar zapato Derecho ")
#
#             #Apagar apoyo haptico
#             print ("Apagar todos los apoyos hápticos")
#
#             #A jugar

###################### Fin de de Actividad (print en pantalla)  ########################################

