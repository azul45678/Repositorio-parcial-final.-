link de replit: https://replit.com/join/fgyfultwif-azul-esmeraldae

"""
Escribe un programa que detecte si se escribe 'Alexa' en un texto. Si se escribe más de una vez, el programa debería responder "Tranquilo, solo di mi nombre una vez". Tip: usa las funciones split() para separar el texto y count() para identificar las veces que dice Alexa.  
INPUT - OUTPUT
"""

def detectar_alexa(nombre, texto):
  palabras = texto.split()
  cuantas_alexas = palabras.count('Alexa')

  
  if cuantas_alexas == 1:
    print(f"HOLAAA {usuario}, soy Alexa")

  elif cuantas_alexas > 1:
    print("Tranquilo(a) {usuario}, solo di mi nombre una vez")
  else: 
    print("No has dicho mi nombre {usuario}")

usuario = input("Dime tu nombre: ")
texto_us = input("Escribe un nombre: ")

detectar_alexa(usuario, texto_us)




  
