# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 02:18:55 2019

@author: Lucas De La Fuente P.
""" 

# 1. Escribe un código en Python que sea capaz de extraer el texto de cada uno.
import pytesseract
from PIL import Image
from PIL import ImageFilter
import sys 
from pdf2image import convert_from_path 
import os 
import re


# filenameIn: PDF a procesar
# fileTextOut: archivo que contendra el texto extraido
def procesar_imagen(filenameIn, fileTextOut):
    
    array_texto_pdf = []
    # primero convertimos el PDF a imagenes
    # guardar todas las paginas del PDF en una variable
    pages = convert_from_path(filenameIn, 500)
    
    # contador de imagenes
    image_counter = 1
    
    # nombre del archivo a procesar:
    nombre_original = os.path.splitext(filenameIn)[0]
    
    # recorrer las paginas 
    for page in pages: 
      
        # Setear nombre de imagenes que se crearan 
        # estas seran: 
        # {nombre_original}_1.jpg 
        # {nombre_original}_2.jpg 
        # .... 
        filename = nombre_original + "_" + str(image_counter)+".jpg"
          
        # Guardar la imagen de la pagina en el disco
        page.save(filename, 'JPEG') 
      
        # Incrementar el contador de imagenes 
        image_counter = image_counter + 1
      

    # Variable que contendra el numero total de imagenes creadas
    filelimit = image_counter-1    
      
    # abrimos archivo donde se guardara el resultado en modo append
    # para que todo el contenido quede solo en ese archivo
    f = open(fileTextOut, "a") 
    
    for i in range(1, filelimit + 1): 
  
        # Setear nombre de imagenes que se crearon 
        # estas son: 
        # {nombre_original}_1.jpg 
        # {nombre_original}_2.jpg 
        # .... 
        filename = nombre_original + "_" + str(i)+".jpg"
              
        # Reconocer el texto como string en la imagen usando pytesserct 
        # image = Image.open(filename)
        # image.filter(ImageFilter.SHARPEN)
        text = str(((pytesseract.image_to_string(Image.open(filename), lang='spa')))) 
      
        # reemplazar todo '-\n' a ''. 
        text = text.replace('-\n', '')     
      
        # Finalmente, escribir el texto procesado al archivo de salida.
        f.write(text) 
        
        # agrega el texto al array
        array_texto_pdf.append(text)
        
  
    # Cerrar el archivo una vez se escribio todo el texto. 
    f.close() 
    return array_texto_pdf


# Archivo AC0AV8Q7cIeH
array_texto_pdf = procesar_imagen("D:\Documentos\Python Scripts\desafio-legalbot\parte-2\AC0AV8Q7cIeH.pdf", "D:\Documentos\Python Scripts\desafio-legalbot\AC0AV8Q7cIeH.txt")
string_texto_pdf = ' '.join(array_texto_pdf)
string_texto_pdf = string_texto_pdf.replace("\n", " ")
string_texto_pdf


# Archivo AC0b5mWFT80k
array_texto_pdf = procesar_imagen("D:\Documentos\Python Scripts\desafio-legalbot\parte-2\AC0b5mWFT80k.pdf", "D:\Documentos\Python Scripts\desafio-legalbot\AC0b5mWFT80k.txt")
string_texto_pdf = ' '.join(array_texto_pdf)
string_texto_pdf = string_texto_pdf.replace("\n", " ")
string_texto_pdf
    
# Archivo AC0BM1JVwL5E
array_texto_pdf = procesar_imagen("D:\Documentos\Python Scripts\desafio-legalbot\parte-2\AC0BM1JVwL5E.pdf", "D:\Documentos\Python Scripts\desafio-legalbot\AC0BM1JVwL5E.txt")
string_texto_pdf = ' '.join(array_texto_pdf)
string_texto_pdf = string_texto_pdf.replace("\n", " ")
string_texto_pdf

# Archivo AC0bz22goMBe
array_texto_pdf = procesar_imagen("D:\Documentos\Python Scripts\desafio-legalbot\parte-2\AC0bz22goMBe.pdf", "D:\Documentos\Python Scripts\desafio-legalbot\AC0bz22goMBe.txt")
string_texto_pdf = ' '.join(array_texto_pdf)
string_texto_pdf = string_texto_pdf.replace("\n", " ")
string_texto_pdf

# Archivo AC0DAolIfAoV
array_texto_pdf = procesar_imagen("D:\Documentos\Python Scripts\desafio-legalbot\parte-2\AC0DAolIfAoV.pdf", "D:\Documentos\Python Scripts\desafio-legalbot\AC0DAolIfAoV.txt")
string_texto_pdf = ' '.join(array_texto_pdf)
string_texto_pdf = string_texto_pdf.replace("\n", " ")
string_texto_pdf


# 2. Escribe una función que tenga como input el texto extraído en la parte (a) y como output el domicilio de la sociedad.

def obtener_domicilio(string_texto):
        
    # punto 3. valida string de "DOMICILIO:" O "DOMICILIO :"
    if "DOMICILIO:" in string_texto:
        # primero separamos el texto por "DOMICILIO:"
        domicilio_split = string_texto.split('DOMICILIO:')
    elif "DOMICILIO :" in string_texto:
        # primero separamos el texto por "DOMICILIO :"
        domicilio_split = string_texto.split('DOMICILIO :')
    
    # obtenemos la segunda parte de este array y lo dividimos por sus comas
    domicilio_split = domicilio_split[1].split(',')
    
    # de este array obtenemos la primera parte concatenada con la segunda, lo que nos dara
    # el domicilio de la Sociedad
    domicilio_sociedad = domicilio_split[0] + "," + domicilio_split[1]
    
    return domicilio_sociedad.strip()

obtener_domicilio(string_texto_pdf)


# 3. ¿Puedes extraer con la misma función de la parte (a) los textos de los PDF en la carpeta "parte-2-b"? 
# ¿Qué es lo distinto, si es que no pudiste? ¿Se te ocurre una forma de resolverlos?

# no pude con todos los archivos ya que en la funcion estaba dividiendo
# el texto por "DOMICILIO:" y algunos de estos archivos contenian "DOMICILIO :"
# por lo tanto modifique la funcion para que valide en caso de que el string contenga "DOMICILIO:" lo divide bajo ese criterio
# en caso contrario si el string contiene "DOMICILIO :" que lo divida con ese criterio.

# Archivo AC0dGWO3zf1k
array_texto_pdf = procesar_imagen("D:\Documentos\Python Scripts\desafio-legalbot\parte-2-b\AC0dGWO3zf1k.pdf", "D:\Documentos\Python Scripts\desafio-legalbot\AC0dGWO3zf1k.txt")
string_texto_pdf = ' '.join(array_texto_pdf)
string_texto_pdf = string_texto_pdf.replace("\n", " ")
string_texto_pdf

obtener_domicilio(string_texto_pdf)

# Archivo AC0FdbwH7YOU
array_texto_pdf = procesar_imagen("D:\Documentos\Python Scripts\desafio-legalbot\parte-2-b\AC0FdbwH7YOU.pdf", "D:\Documentos\Python Scripts\desafio-legalbot\AC0FdbwH7YOU.txt")
string_texto_pdf = ' '.join(array_texto_pdf)
string_texto_pdf = string_texto_pdf.replace("\n", " ")
string_texto_pdf

obtener_domicilio(string_texto_pdf)
    
# Archivo AC0g0Wdb1M1D
array_texto_pdf = procesar_imagen("D:\Documentos\Python Scripts\desafio-legalbot\parte-2-b\AC0g0Wdb1M1D.pdf", "D:\Documentos\Python Scripts\desafio-legalbot\AC0g0Wdb1M1D.txt")
string_texto_pdf = ' '.join(array_texto_pdf)
string_texto_pdf = string_texto_pdf.replace("\n", " ")
string_texto_pdf

obtener_domicilio(string_texto_pdf)

# Archivo AC0IL7L5uSzC
array_texto_pdf = procesar_imagen("D:\Documentos\Python Scripts\desafio-legalbot\parte-2-b\AC0IL7L5uSzC.pdf", "D:\Documentos\Python Scripts\desafio-legalbot\AC0IL7L5uSzC.txt")
string_texto_pdf = ' '.join(array_texto_pdf)
string_texto_pdf = string_texto_pdf.replace("\n", " ")
string_texto_pdf

obtener_domicilio(string_texto_pdf)

# Archivo AC0lTLIqbr7a
array_texto_pdf = procesar_imagen("D:\Documentos\Python Scripts\desafio-legalbot\parte-2-b\AC0lTLIqbr7a.pdf", "D:\Documentos\Python Scripts\desafio-legalbot\AC0lTLIqbr7a.txt")
string_texto_pdf = ' '.join(array_texto_pdf)
string_texto_pdf = string_texto_pdf.replace("\n", " ")
string_texto_pdf

obtener_domicilio(string_texto_pdf)


