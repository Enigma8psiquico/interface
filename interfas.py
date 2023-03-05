#!/usr/bin/env python
# 
# AUMENTAR EL LARGO DE LA ENTRADA DE LA DIRECCION 
import sys
import tkinter as tk
from PIL import ImageTk, Image

# Creamos la ventana principal
root = tk.Tk()


# Le damos un tamaño y posición inicial a la ventana
ancho = 600
alto = 510
root.geometry(f"{ancho}x{alto}+600+10")
root.resizable(height = 0,width = 0)

# Agregamos un título a la ventana
root.title("Mi Ventana")

frame = tk.Frame(root, background="#fbf1c7", height = alto, width = ancho )
frame.pack()


# TITULO IMAGEN DE LOGO    
img = Image.open("imagen.png")
img = img.resize((405, 110)) # ((ancho, alto))
img_tk = ImageTk.PhotoImage(img)
label = tk.Label(frame, image=img_tk)
label.place(x = 190, y = 10) # posicion en x and y



# {+} DECLARACION DE WIDGETS



# [+] CASILLA DE DNI 
dni = tk.Label(frame, text = " DNI ", font = ("",12))
dni.place(x = 20, rely = 0.2, anchor = "w")

entrada_dni = tk.Text(frame, height = 1, width = 14)
entrada_dni.place(x = 65, rely = 0.2, anchor = "w")


# [-]


# [+] Apellidos 
apellidos = tk.Label(frame, text = " Apellidos ", font = ("", 12)) 
apellidos.place(x = 20, rely = 0.3, anchor = "w")

entrada_apellidos = tk.Text(frame, height = 1, width = 20)
entrada_apellidos.place(x = 100, rely = 0.3, anchor = "w")

# [-]
# [+] NOMBRES
nombre = tk.Label(frame, text = " Nombres ", font = ("", 12) )
nombre.place(relx = 0.6, rely = 0.3, anchor = "e")

entrada_nombre = tk.Text(frame, height = 1, width = 20)
entrada_nombre.place(relx = 0.88, rely = 0.3, anchor = "e")

# [-]

# [+] DIRECCION 

direccion = tk.Label(frame, text = " Direccion ", font=("", 12))
direccion.place(x = 20, rely = 0.4, anchor = "w")

entrada_direccion = tk.Text(frame, height = 1, width = 30)
entrada_direccion.place(relx = 0.18, rely = 0.4, anchor = "w")
# [-]

# [+] TELEFONO

telefono = tk.Label(frame, text = " Telefono ", font = ("", 12))
telefono.place(x = 20, rely = 0.5, anchor = "w")

entrada_telefono = tk.Text(frame, height = 1, width = 40)
entrada_telefono.place(relx = 0.17, rely = 0.5, anchor = "w")

# [-]

# {-}


# {+} TABLA DE CONTENIDO
row = tk.Label(frame, text = " |     Cod_pro   |                    Descripcion                |      Unidad     |      Cantidad     |        Precio       |      Subtotal       | ")
row.place(x = 5, rely = 0.6, anchor = "w")



# [+] PRODUCTOS 
alicate = {
    "nombre": "Alicate",
    "precio" : 20,
    "unidades" : "por unidad"
}

martillo = {
    "nombre" : "Martillo",
    "precio" : 27,
    "unidades": "por unidad"

}


motosierra = {
    "nombre": "Motosierra",
    "unidades": "por unidad",
    "precio": 248
}


clavos = {
    "nombre":"Clavos",
    "unidades": "s/2 docena",
    "precio" : 2 # la docena
}

lima = {
    "nombre": "Lima",
    "unidades" : "por unidad",
    "precio": 23
}

destorillador_estrella = {
    "nombre":"Destornillador estrella",
    "unidades": "por unidad",
    "precio": 35
}

cinta_negra = {
    "nombre":"Cinta negra",
    "unidades": "s/5 por 3",
    "precio" : 5
}

taladro = { # nombre de herramienta
    "nombre":"Taladro",
    "unidades": "por unidad",
    "precio":220
}

brocha_grande = {
    "nombre": "Brocha grande",
    "unidades" : "unidad",
    "precio": 20
}

brocha_chica = {
    "nombre" : "Brocha chica",
    "unidades": "unidad",
    "precio":12
}

# aqui declaro de manera ordenada los productos disponibles en la TIENDITA DE DON PEPE

productos = {
    "001": alicate, # valor : nombre de herramienta
    "002": martillo,
    "003":motosierra,
    "004": clavos,
    "005":lima,
    "006":cinta_negra,
    "007":destorillador_estrella,
    "008":taladro,
    "009":brocha_chica,
    "010":brocha_grande
}

# [-] tabla de producto 




# [+] CASILLA 1
# (+) CODIGO DE PRODUCTO 1
casilla1 = tk.Text(frame, height = 1 , width = 8)
casilla1.place(x = 10, rely = 0.65, anchor = "w")

# (+) BLOQUE DE DESCRIPCION EN LA CASILLA 1 
descripcion1 = tk.Label(frame, bg = "#689d6a")
descripcion1.place(relx = 0.14, rely = 0.675, anchor = "w", height = 50, width = 170)

# (+) BLOQUE DE UNIDAD EN CASILLA 1
unidad1 = tk.Label(frame, bg = "#7c6f64")
unidad1.place(relx = 0.43, rely = 0.65, anchor = "w", width = 69)

# (+) BLOQUE DE CANTIDAD EN LA CANTIDAD 1
cantidad1 = tk.Text(frame, height = 1, width = 9)
cantidad1.place(relx = 0.55, rely = 0.65, anchor = "w")

# (+) BLOQUE DE PRECIO EN LA CASILLA 1 
precio1 = tk.Label(frame, bg = "#b57614")
precio1.place(relx = 0.69, rely = 0.65, anchor = "w", width = 77)

# (+) BLOQUE DE SUBTOTAL EN LA CASILLA 1 

subtotal1 = tk.Label(frame, bg = "#458588")
subtotal1.place(relx = 0.83, rely = 0.65, anchor = "w", width = 77)






# [+] CASILLA 2

# (+) CODIGO DE PRODUCTO 2
casilla2 = tk.Text(frame, height = 1, width = 8)
casilla2.place(x = 10, rely = 0.75, anchor = "w")

# (+) BLOQUE DE DESCRIPCION EN LA CASILLA 2 
descripcion2 = tk.Label(frame, bg = "#689d6a")
descripcion2.place(relx = 0.14, rely = 0.78, anchor = "w", height = 50, width = 170)

# (+) BLOQUE DE UNIDAD EN CASILLA 2
unidad2 = tk.Label(frame, bg = "#7c6f64")
unidad2.place(relx = 0.43, rely = 0.75, anchor = "w", width = 69)


# (+) BLOQUE DE CANTIDAD EN LA CANTIDAD 2
cantidad2 = tk.Text(frame, height = 1, width = 9)
cantidad2.place(relx = 0.55, rely = 0.75, anchor = "w")

# (+) BLOQUE DE PRECIO EN LA CASILLA 2
precio2 = tk.Label(frame, bg = "#b57614")
precio2.place(relx = 0.69, rely = 0.75, anchor = "w", width = 77)

# (+) BLOQUE DE SUBTOTAL EN LA CASILLA 1 

subtotal2 = tk.Label(frame, bg = "#458588")
subtotal2.place(relx = 0.83, rely = 0.75, anchor = "w", width = 77)





# [+] CASILLA 3
# (+) CODIGO DE PRODUCTO 3
casilla3 = tk.Text(frame, height = 1, width = 8)
casilla3.place(x = 10, rely = 0.85, anchor = "w")

# (+) BLOQUE DE DESCRIPCION EN LA CASILLA 3 
descripcion3 = tk.Label(frame, bg = "#689d6a")
descripcion3.place(relx = 0.14, rely = 0.884, anchor = "w", height = 50, width = 170)

# (+) BLOQUE DE UNIDAD EN CASILLA 3
unidad3 = tk.Label(frame, bg = "#7c6f64")
unidad3.place(relx = 0.43, rely = 0.851, anchor = "w", width = 69)

# (+) BLOQUE DE CANTIDAD EN LA CANTIDAD 3
cantidad3 = tk.Text(frame, height = 1, width = 9)
cantidad3.place(relx = 0.55, rely = 0.851, anchor = "w")

# (+) BLOQUE DE PRECIO EN LA CASILLA 3
precio3 = tk.Label(frame, bg = "#b57614")
precio3.place(relx = 0.69, rely = 0.851, anchor = "w", width = 77)

# (+) BLOQUE DE SUBTOTAL EN LA CASILLA 1 

subtotal3 = tk.Label(frame, bg = "#458588")
subtotal3.place(relx = 0.83, rely = 0.851, anchor = "w", width = 77)



# [+] CASILLA DEL TOTAL

# Cartelito de total
total = tk.Label(frame, text = "Total: s/0", font = ("",14,"bold" ))
total.place(relx = 0.96, rely = 0.904, anchor = "e")
# [-]


# FUNCION DE CALCULAR
# {+} BOTON DE CALCULAR
def calcular(): 
    # (+) Funcion de obtener informacion de los productos

    entrada_casilla1 = casilla1.get("1.0","end-1c") 
    entrada_casilla2 = casilla2.get("1.0","end-1c")
    entrada_casilla3 = casilla3.get("1.0","end-1c")

    # (-)


    # FILA 1
    try: # obteniendo datos
        # CASILLA 1
        descripcion1.config(text=productos[entrada_casilla1]["nombre"]) # DESCRIPCION
        unidad1.config(text=productos[entrada_casilla1]["unidades"]) # UNIDAD
        precio1.config(text=f's/{productos[entrada_casilla1]["precio"]}') # PRECIO
        
        cantidadCasilla1 =  cantidad1.get("1.0","end-1c") # obtenemos el valor de la casilla de "cantidad"
        
        # si no hay nada en la casilla de la cantidad entonces este que tome el valor de 1 asi haiga puesto solo el producto
        if  len(cantidadCasilla1) == 0:
            cantidadCasilla1 = 1
        
        # aqui calculamos el subtotal final con la cantidad que vamos a ingresar 
        subtotalcasilla1 = int(productos[entrada_casilla1]["precio"]) * int(cantidadCasilla1)
        subtotal1.config(text = subtotalcasilla1) # imprimimos el subtotal en su respectiva casilla

    except Exception as a: 
        # limpieza si no hay nada
        descripcion1.config(text="Producto no encontrado") # por si presionamos CALCULAR nos saldra este mensaje








    # FILA 2
    try: # obteniendo datos
        # CASILLA 2
        descripcion2.config(text=productos[entrada_casilla2]["nombre"]) # DESCRIPCION
        unidad2.config(text=productos[entrada_casilla2]["unidades"]) # UNIDAD
        precio2.config(text=f's/{productos[entrada_casilla2]["precio"]}') # PRECIO
        
        cantidadCasilla2 =  cantidad2.get("1.0","end-1c")
        
        if  len(cantidadCasilla2) == 0:
            cantidadCasilla2 = 1
        
        subtotalcasilla2 = int(productos[entrada_casilla2]["precio"]) * int(cantidadCasilla2)
        subtotal2.config(text = subtotalcasilla2) # imprimimos el subtotal en su respectiba casilla

    except Exception as a: 
        # limpieza si no hay nada
        descripcion2.config(text="Producto no encontrado")


    # FILA 3
    try: # obteniendo datos
        # CASILLA 3
        descripcion3.config(text=productos[entrada_casilla3]["nombre"]) # DESCRIPCION
        unidad3.config(text=productos[entrada_casilla3]["unidades"]) # UNIDAD
        precio3.config(text=f's/{productos[entrada_casilla3]["precio"]}') # PRECIO
        
        cantidadCasilla3 =  cantidad3.get("1.0","end-1c")
        
        if  len(cantidadCasilla3) == 0:
            cantidadCasilla3 = 1
        
        subtotalcasilla3 = int(productos[entrada_casilla3]["precio"]) * int(cantidadCasilla3)
        subtotal3.config(text = subtotalcasilla3)

    except Exception as a: 
        # limpieza si no hay nada
        descripcion3.config(text="Producto no encontrado")



    # SUMATORIA DE LOS SUBTOTALES

    # estos bloques sirven para intentar sumar los subtotales 
    try: 
        n1 = subtotalcasilla1
    except: # en el que si existe un error de valor 
        n1 = 0 # este sera igual a 0 

    try:
        n2 = subtotalcasilla2
    except:
        n2 = 0

    try:
        n3 = subtotalcasilla3
    except:
        n3 = 0    

    # asi podremos sumar 2 productos sin problemas 
    subtotales = n1 + n2 + n3

            

    # impresion de el total en la ventana 
    total.config(text = f" Total: s/{subtotales}", justify = tk.RIGHT)



# [+] BOTON DE CALCULAR
tk.Button(frame, text = " CALCULAR ", command = calcular, font = ("", 9)).place(relx = 0.67, rely = 0.965, anchor = "e")
# {-}





# [+] FUNCION DE LIMPIEZA 
def limpiar():
    #
    #  AQUI NO HAY MUCHO QUE DECIR SIMPLEMENTE BORRAMOS EL CONTENIDO 
    #  DE TODOS LOS OBJETOS DE LA VENTANA
    entrada_nombre.delete("1.0","end")        
    entrada_telefono.delete("1.0","end")
    entrada_dni.delete("1.0", "end")
    entrada_telefono.delete("1.0","end")
    
    descripcion1.config(text="")
    unidad1.config(text="")
    precio1.config(text="")
    subtotal1.config(text="")

    
    descripcion2.config(text="")
    unidad2.config(text="")
    precio2.config(text="")
    subtotal2.config(text="")

    
    descripcion3.config(text="")
    unidad3.config(text="")
    precio3.config(text="")
    subtotal3.config(text="")

    total.config(text = "Total s/")

    casilla1.delete("0.1","end")
    casilla2.delete("0.1","end")
    casilla3.delete("0.1","end")

    casilla1.delete("0.1","end")
    casilla2.delete("0.1","end")
    casilla3.delete("0.1","end")

    cantidad1.delete("0.1","end")
    cantidad2.delete("0.1","end")
    cantidad3.delete("0.1","end")



# [+] BOTON DE LIMPIEZA
tk.Button(frame, text = " LIMPIAR ", command = limpiar, font = ("", 9)).place(relx = 0.71, rely = 0.965, anchor = "w")
# [-]
    

tk.Label(frame, text = "By Arcanet ", font = ("yy")).place(x = 5 , rely = 0.95)

# Iniciamos el bucle principal de la aplicación para que la ventana sea visible
root.mainloop()


"""

    "n": arriba
    "s": abajo
    "e": derecha
    "w": izquierda
    "nw": arriba-izquierda
    "ne": arriba-derecha
    "sw": abajo-izquierda
    "se": abajo-derecha







"""
