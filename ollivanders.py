link de replit: https://replit.com/join/pfthjroafy-azul-esmeraldae

#Crea un programa que registre los clientes que entran a una tienda y cuántos de ellos compran varitas. 
#Debe registrar qué clientes compraron qué varitas. Las opciones de varitas son: 
    #1. Varita de Saúco, 
    #2. Varita de Espino, 
    #3. Varita de Sauce 
    #4. Varita de Acebo

total_de_clientes = 0
total_compras = 0
varitas_por_compra = [0,0,0,0]

while True:  
    nombre = input("Ingresa tu nombre o escribe 'salir' para terminar: ")
  
    if nombre.lower() == 'salir':
        break 
    total_de_clientes += 1

    print("Opciones de varitas:")
    print("1. Varita de Saúco")
    print("2. Varita de Espino")
    print("3. Varita de Sauce")
    print("4. Varita de Acebo")

    while True:
        try:
            varita = int(input("¿Qué varita desea comprar?? "))
            if 1 <= varita <= 4:
                break
            else:
              print("Opción no valida")
        except ValueError:
          print("Opción no valida")
   
    if varita == 1:
      varitas_por_compra[0] += 1
      print("Usted ha comprado la Varita de Saúco ")
    elif varita == 2:
      varitas_por_compra[1] += 1
      print("Usted ha comprado la  Varita de Espino")
    elif varita == 3:
      varitas_por_compra[2] += 1
      print("Usted ha comprado la Varita de Sauce")
    elif varita == 4:
      varitas_por_compra[3] += 1
      print("Usted ha comprado la Varita de Acebo")

  
#Dar resulatdos
print(f"Total de clientes: {total_de_clientes}")
print(f"Total de varitas compradas: {total_compras}")
print("Compras por varita:")
print(f"Varita de Saúco: {varitas_por_compra[0]}")
print(f"Varita de Espino: {varitas_por_compra[1]}")
print(f"Varita de Sauce: {varitas_por_compra[2]}")
print(f"Varita de Acebo: {varitas_por_compra[3]}")
