from tkinter import *


ventana = Tk()
ventana.title('Registro de Productos')
ventana.config(bg='pink')

# Variables to store user inputs
nombre = StringVar()
precio = StringVar()
cantidad = StringVar()

# Input Fields and Labels
Label(ventana, text='Ingrese el nombre del producto:', bg='pink').pack(pady=5)
Entry(ventana, textvariable=nombre).pack()

Label(ventana, text='Ingrese el precio del producto:', bg='pink').pack(pady=5)
Entry(ventana, textvariable=precio).pack()

Label(ventana, text='Ingrese la cantidad:', bg='pink').pack(pady=5)
Entry(ventana, textvariable=cantidad).pack()

# This label display the results
registro = Label(ventana, text='', bg='pink', fg='black')
registro.pack(pady=10)

# Function. It register and display the items
def registrar():
    reg = f'''
    Producto: {nombre.get()}
    Precio: {precio.get()}
    Cantidad: {cantidad.get()}
    '''
    registro.config(text=reg)

# Button 
Button(ventana, text='Registrar', command=registrar).pack(pady=10)

# Window Size
ventana.geometry('300x250')
ventana.mainloop()
