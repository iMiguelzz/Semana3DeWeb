menu= ["1. Agregar Producto",
       "2. Retirar Productos",
       "3. Modificar Producto",
       "4. Listar Producto",
       "5. Aumentar Stock",
       "6. Reducir Stock",
       "7. Salir"]

productos = ["Arroz", "Fideos","Azucar", "Aceite"]
precios = [3.50, 1.50, 4.00, 11.0]
stock = [30, 20, 20, 15]

def listar():
       print()
       print("|-----------------------------|")
       print("Listado de Productos de Almacen")
       print("|-----------------------------|")
       for i in range(len(productos)):
                print(i+1, productos[i],"\t",precios[i],"\t",stock[i])
              
def agregar():
       print()
       print("|-----------------------------|")
       print("Listado de Productos de Almacen")
       print("|-----------------------------|")
       newProducto = input("Ingrese Producto: ")
       newPrecio = float(input("Ingrese Precio: "))
       newStock = int(input("Ingrese Stock: "))
       productos.append(newProducto)
       precios.append(newPrecio)
       stock.append(newStock)
       print("Producto agregado en Almacen")
       
def retirar():
       print()
       print("|-----------------------------|")
       print("Listado de Productos de Almacen")
       print("|-----------------------------|")
       for i in range(len(productos)):
                print(i+1,productos[i],"\t",precios[i],"\t",stock[i])
       print("|-----------------------------|")
       op = int(input("Seleccione Producto a Retirar: "))
       productoRetirado = productos[op-1]
       del productos[op-1]
       del precios[op-1]
       del stock[op-1]
       print("Producto", productoRetirado, "retirado del Almacen")
       print()

def modificar():
       print()
       print("|-----------------------------|")
       print("Listado de Productos de Almacen")
       print("|-----------------------------|")
       for i in range(len(productos)):
                print(i+1,productos[i],"\t",precios[i],"\t",stock[i])
       print("|-----------------------------|")
       op = int(input("Seleccione Producto a Modificar: "))
       newProducto = input("Modificar el Nombre: ")
       newPrecio = float(input("Modificar Precio: "))
       newStock = int(input("Modificar Stock: "))
       productos[op-1] = newProducto
       precios[op-1] = newPrecio
       stock[op-1] = newStock
       print("Producto", op, "Modificado en Almacen")

def aumentarStock():
       print()
       print("|-----------------------------|")
       print("Listado de Productos de Almacen")
       print("|-----------------------------|")
       for i in range(len(productos)):
                print(i+1,productos[i],"\t",precios[i],"\t",stock[i])
       print("|-----------------------------|")
       op = int(input("Seleccione Producto a aumentar Stock: "))
       cantidad = int(input("Ingrese cantidad a aumentar: "))
       stock[op-1] += cantidad
       print("Stock del Producto", op, "Aumentado en Almacen")
       
def reducirStock():
       print()
       print("|-----------------------------|")
       print("Listado de Productos de Almacen")
       print("|-----------------------------|")
       for i in range(len(productos)):
                print(i+1,productos[i],"\t",precios[i],"\t",stock[i])
       print("|-----------------------------|")
       op = int(input("Seleccione Producto a reducir Stock: "))
       cantidad = int(input("Ingrese cantidad a reducir: "))
       if cantidad >= stock[op-1]:
              print("No hay suficiente stock para reducir")
       else:
              stock[op-1] -= cantidad
              print("Stock del Producto", op, "Reducido en Almacen")
       

#PROGRAMA PRINCIPAL
while(True):
       print("|-----------------------------|")
       print("| Menú Principal del Proyecto |")
       print("|-----------------------------|")
       for  i in range(7): 
                     print(menu[i])
       print("|-----------------------------|")
       opcion= int(input("Seleccione Opción: "))
       if (opcion == 1):
              agregar()
       elif (opcion == 2):
              retirar()
       elif (opcion == 3):
              modificar()
       elif (opcion == 4):
              listar()
       elif (opcion == 5):
              aumentarStock()
       elif (opcion == 6):
              reducirStock()
       elif ( opcion ==7):
              print("Muchas gracias por usar nuestra App")
              break