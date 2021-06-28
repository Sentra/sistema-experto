from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.tix import *
from knowledge import generate_dishes
from formulas import BasalMetabolicRate


#GUI
root = Tk()
root.geometry("600x320")
root.title("Corporis")
root.config(bg = "grey19")

#Variables
nombre = StringVar()
sexo = StringVar(value = "Masculino")
edad = IntVar() 
altura = IntVar() 
peso = IntVar() 
actividad_fisica = StringVar(value = "1 vez por semana")
gluten = StringVar(value = "Si")
azucar = StringVar(value = "Si")


def recomendar():
    nombreG = nombre.get()
    sexoG = sexo.get()
    edadG = edad.get()
    alturaG = altura.get()
    pesoG = peso.get()
    actividad_fisicaG = actividad_fisica.get()
    glutenG = gluten.get()
    azucarG = azucar.get()

    #validaciones 
    if (nombreG == ''): 
        messagebox.showwarning(message="Debe ingresar un nombre.", title="Información incorrecta")
        return
    elif (edadG <= 0 or edadG > 100): 
        messagebox.showwarning(message="Debe ingresar una edad correcta.", title="Información incorrecta")
        return
    elif (alturaG <= 0 or alturaG >= 240):
        messagebox.showwarning(message="Debe ingresar una altura correcta.", title="Información incorrecta")
        return
    elif (pesoG <= 30 or pesoG >= 500):
        messagebox.showwarning(message="Debe ingresar un peso correcto.", title="Información incorrecta")
        return   

    #calcular el tmb
    TMB = BasalMetabolicRate(sexoG, pesoG, alturaG, edadG)
    print("TMB: ", TMB)
    days = 5
    dishes = generate_dishes(days, TMB)   
    print("Dishes", dishes)

    newWindow = Toplevel(root)
    newWindow.title("Plan de dietas personalizado")
    newWindow.geometry("600x320")
    newWindow.config(bg = "grey19")
    textNombre = "Bienvenido, " + nombreG
    textCalorias = "Tu plan de dieta le permite consumir " + str(TMB) + " por día"

    textTotalCaloriasL = "Calorias: " + str(dishes[0][1])
    textTotalCaloriasMA = "Calorias: " + str(dishes[1][1])
    textTotalCaloriasMI = "Calorias: " + str(dishes[2][1])
    textTotalCaloriasJ = "Calorias: " + str(dishes[3][1])
    textTotalCaloriasV = "Calorias: " + str(dishes[4][1])

    mensNombre = Label(newWindow, text = textNombre, font = ("white", 30), bg = "grey19", fg = "white")
    mensNombre.place(x = 30, y = 10)
    mensPlan = Label(newWindow, text = textCalorias, font = ("white", 15), bg = "grey19", fg = "white")
    mensPlan.place(x = 30, y = 60)

    mensLunes = Label(newWindow, text = "Lunes", font = ("white", 10), bg = "grey19", fg = "white")
    mensLunes.place(x = 30, y = 110)
    mensLunesD = Label(newWindow, text = dishes[0][0][0], font = ("white", 10), bg = "grey19", fg = "white")
    mensLunesD.place(x = 30, y = 140)
    mensLunesA = Label(newWindow, text = dishes[0][0][1], font = ("white", 10), bg = "grey19", fg = "white")
    mensLunesA.place(x = 30, y = 170)
    mensLunesC = Label(newWindow, text = dishes[0][0][2], font = ("white", 10), bg = "grey19", fg = "white")
    mensLunesC.place(x = 30, y = 200)
    mensLunesCA = Label(newWindow, text = textTotalCaloriasL, font = ("white", 10), bg = "grey19", fg = "white")
    mensLunesCA.place(x = 30, y = 230)

    mensMartes = Label(newWindow, text = "Martes", font = ("white", 10), bg = "grey19", fg = "white")
    mensMartes.place(x = 150, y = 110)
    mensMartesD = Label(newWindow, text = dishes[1][0][0], font = ("white", 10), bg = "grey19", fg = "white")
    mensMartesD.place(x = 150, y = 140)
    mensMartesA = Label(newWindow, text = dishes[1][0][1], font = ("white", 10), bg = "grey19", fg = "white")
    mensMartesA.place(x = 150, y = 170)
    mensMartesC = Label(newWindow, text = dishes[1][0][2], font = ("white", 10), bg = "grey19", fg = "white")
    mensMartesC.place(x = 150, y = 200)
    mensMartesCA = Label(newWindow, text = textTotalCaloriasMA, font = ("white", 10), bg = "grey19", fg = "white")
    mensMartesCA.place(x = 150, y = 230)

    mensMiercoles = Label(newWindow, text = "Miércoles", font = ("white", 10), bg = "grey19", fg = "white")
    mensMiercoles.place(x = 270, y = 110)
    mensMiercolesD = Label(newWindow, text = dishes[2][0][0], font = ("white", 10), bg = "grey19", fg = "white")
    mensMiercolesD.place(x = 270, y = 140)
    mensMiercolesA = Label(newWindow, text = dishes[2][0][1], font = ("white", 10), bg = "grey19", fg = "white")
    mensMiercolesA.place(x = 270, y = 170)
    mensMiercolesC = Label(newWindow, text = dishes[2][0][2], font = ("white", 10), bg = "grey19", fg = "white")
    mensMiercolesC.place(x = 270, y = 200)
    mensMiercolesCA = Label(newWindow, text = textTotalCaloriasMI, font = ("white", 10), bg = "grey19", fg = "white")
    mensMiercolesCA.place(x = 270, y = 230)

    mensJueves = Label(newWindow, text = "Jueves", font = ("white", 10), bg = "grey19", fg = "white")
    mensJueves.place(x = 390, y = 110)
    mensJuevesD = Label(newWindow, text = dishes[3][0][0], font = ("white", 10), bg = "grey19", fg = "white")
    mensJuevesD.place(x = 390, y = 140)
    mensJuevesA = Label(newWindow, text = dishes[3][0][1], font = ("white", 10), bg = "grey19", fg = "white")
    mensJuevesA.place(x = 390, y = 170)
    mensJuevesC = Label(newWindow, text = dishes[3][0][2], font = ("white", 10), bg = "grey19", fg = "white")
    mensJuevesC.place(x = 390, y = 200)
    mensJuevesCA = Label(newWindow, text = textTotalCaloriasJ, font = ("white", 10), bg = "grey19", fg = "white")
    mensJuevesCA.place(x = 390, y = 230)

    mensViernes = Label(newWindow, text = "Viernes", font = ("white", 10), bg = "grey19", fg = "white")
    mensViernes.place(x = 510, y = 110)
    mensViernesD = Label(newWindow, text = dishes[4][0][0], font = ("white", 10), bg = "grey19", fg = "white")
    mensViernesD.place(x = 510, y = 140)
    mensViernesA = Label(newWindow, text = dishes[4][0][1], font = ("white", 10), bg = "grey19", fg = "white")
    mensViernesA.place(x = 510, y = 170)
    mensViernesC = Label(newWindow, text = dishes[4][0][2], font = ("white", 10), bg = "grey19", fg = "white")
    mensViernesC.place(x = 510, y = 200)
    mensViernesCA = Label(newWindow, text = textTotalCaloriasV, font = ("white", 10), bg = "grey19", fg = "white")
    mensViernesCA.place(x = 510, y = 230)
    
mensTitulo = Label(root, text="Dieta Personalizada", font = ("white", 30), bg = "grey19", fg="white")
mensTitulo.place(x=30, y=10)
mensNombre = Label(root, text="Nombre", bg = "grey19", fg="white")
mensNombre.place(x=30, y=70)
entryNombre = Entry(root, textvariable = nombre, width=20)
entryNombre.place(x=30, y=100)
mensSexo = Label(root, text="Sexo", bg = "grey19", fg="white")
mensSexo.place(x=180, y=70)
combSexo = ttk.Combobox(root, values=["Masculino", "Femenino"], state='readonly', textvariable = sexo)
combSexo.place(x=180, y=100)
mensEdad = Label(root, text="Edad", bg = "grey19", fg="white")
mensEdad.place(x=350, y=70)
entryEdad = Entry(root, textvariable = edad, width=10)
entryEdad.place(x=350, y=100)
mensAltura = Label(root, text="Altura (cm)", bg = "grey19", fg="white")
mensAltura.place(x=450, y=70)
entryAltura = Entry(root, textvariable = altura, width=10)
entryAltura.place(x=450, y=100)
mensPeso = Label(root, text="Peso (kg) ", bg = "grey19", fg="white")
mensPeso.place(x=30, y=150)
entryPeso = Entry(root, textvariable = peso, width=10)
entryPeso.place(x=30, y=180)
mensActividad = Label(root, text="Actividad física ", bg = "grey19", fg="white")
mensActividad.place(x=150, y=150)
combActividad = ttk.Combobox(root, values=["1 vez por semana", "2-3 veces por semana", "3-5 veces por semana", "Ejercicio diario"], state='readonly', textvariable=actividad_fisica)
combActividad.place(x=150, y=180)
mensGluten = Label(root, text="Gluten ", bg = "grey19", fg="white")
mensGluten.place(x=320, y=150)
combGluten = ttk.Combobox(root, values=["Si", "No"], state='readonly', textvariable=gluten, width=10)
combGluten.place(x=320, y=180)
mensAzucar = Label(root, text="Azúcar ", bg = "grey19", fg="white")
mensAzucar.place(x=430, y=150)
combAzucar = ttk.Combobox(root, values=["Si", "No"], state='readonly', textvariable=azucar, width=10)
combAzucar.place(x=430, y=180)


botonRecomendar =Button(root,text="Recomendar", command = recomendar, width=75) #recomendar -> funcion que retorna plan de dietas
botonRecomendar.place(x=30, y=260)

root.mainloop()
