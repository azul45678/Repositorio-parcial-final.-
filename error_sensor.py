link de replit: https://replit.com/join/imxtfojnte-azul-esmeraldae

"""
Desarrolla un programa que calcule el porcentaje de error de un sensor de temperatura LM35 en un laboratorio. 
El programa debe detectar y almacenar las lecturas incorrectas, mostrando al final el porcentaje de veces que el sensor dio valores fuera del rango esperado (entre 10 y 40 grados Celsius).
"""

#Empezar con el código 
def calculo_porcentaje_error(lista_lecturas):
  lecturas_incorrectas = 0
  rango_esperado = range(10, 41)

  for lectura in lista_lecturas: 
    if lectura not in rango_esperado:
      lecturas_incorrectas += 1
  porcentaje_error = (lecturas_incorrectas / len(lista_lecturas)) * 100

#RESULATDOS

  print(f"Lecturas incorrectas: {lecturas_incorrectas}")
  print(f"Porcentaje de error: {porcentaje_error: .2f}%")

#Tem
lecturas_temperatura = [25, 28, 9, 35, 42, 18, 30, 10, 38, 22]
calculo_porcentaje_error(lecturas_temperatura)


