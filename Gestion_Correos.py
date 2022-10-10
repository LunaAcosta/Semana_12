from ast import Str
#from curses import use_default_colors
from distutils.util import strtobool
from tkinter import * 
import smtplib  # Esta Libreria nos va ayudar a poder enviar nuestro correo 
from tkinter import messagebox
from turtle import color, right, width
# Creamos nuestra ventana para enviar nuestro correos 
Interfaz = Tk()
Interfaz.iconbitmap(r'C:\Users\lunaa\OneDrive\Documentos\Python\Ensayo\gmail3.ico')
Interfaz.geometry("310x300")
Interfaz.config(bg="snow")
Interfaz.title('Mensaje nuevo')

# Creamos nuestra funcion para enviar nuestros mensajes 
def enviar ():
    try: 
        username = usuario.get() 
        password = contraseña.get()
        to = para.get()
        subject = asunto.get()
        body = cuerpo.get()
        if (username =="" or password== "" or to == "" or subject == "" or body ==""):
           messagebox.showerror("Error ","Se deben llenar los campos")

        else :
            mesaje = 'Subject: {}\n\n{}'.format(subject, body)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(username, password)
            server.sendmail(username, to, mesaje)
            #alerta.config(text= "El mensaje se ha enviado con exito", fg="green")
            messagebox.showinfo("Gestion de Envio ","Su menaje se ha enviado con exito")

    except Exception as e :
        alerta.config(text= " Error al enviar el mensaje",fg="red")
        print(e)


# Creamos una funcion quen os permita borrar el contenido de nuestro Entry 
def borrar ():
    usuario.delete(0, 'end')
    contraseña.delete(0, 'end')
    para.delete(0, 'end')
    asunto.delete(0, 'end')
    cuerpo.delete(0, 'end')
    alerta.destroy()


# Creamos todos nuestros Label 
Label(Interfaz, bg="snow", text="Envia tu correo", font=('Roboto', 15)).grid(row=0, sticky=N) # Primer Label 
Label(Interfaz,bg="snow", text="Llena Correctamente el siguiente formulario", font=('Roboto',11)).grid(row=1, sticky=N, padx=5, pady=10) # Segundo label

imagen = PhotoImage(file="gmail2.png")
Label(Interfaz,image=imagen, bg="snow").grid(row=2)

Label(Interfaz, bg="snow", text="Correo:", font=('Roboto',11)).grid(row=3, sticky=W, padx=5)
Label(Interfaz, bg="snow", text="Contraseña:", font=('Roboto',11)).grid(row=4, sticky=W, padx=5)
Label(Interfaz, bg="snow", text="Para:", font=('Roboto',11)).grid(row=5, sticky=W, padx=5)
Label(Interfaz, bg="snow", text="Asunto:", font=('Roboto',11)).grid(row=6, sticky=W, padx=5)
Label(Interfaz, bg="snow", text="Cuerpo:", font=('Roboto',11)).grid(row=7, sticky=W, padx=5)

alerta = Label(Interfaz, text="", font=('Roboto', 11), fg= "red")
alerta.grid(row=9, sticky=S)

# Creamos nuestros Entry
# Entry 
usuario = StringVar()  
contraseña = StringVar()
para = StringVar()
asunto = StringVar()
cuerpo = StringVar()

usuario = Entry(Interfaz, textvariable=usuario)
usuario.grid(row=3, column=0)

contraseña = Entry(Interfaz, textvariable=contraseña, show='*')
contraseña.grid(row=4, column=0)

para = Entry(Interfaz, textvariable=para)
para.grid(row=5, column=0)

asunto= Entry(Interfaz, textvariable=asunto)
asunto.grid(row=6, column=0)

cuerpo= Entry(Interfaz, textvariable=cuerpo)
cuerpo.grid(row=7, column=0)


# Creamos nuestro botones Botones 

Button(Interfaz, command= enviar, text="Enviar",  bg="deep sky blue" ).place(x=10, y= 250, width=80, height=30)
Button(Interfaz, command= borrar, text="Borrar" , bg="deep sky blue").place(x=130, y= 250, width=80, height=30)

Interfaz.mainloop()
