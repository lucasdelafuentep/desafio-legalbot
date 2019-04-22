# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 14:34:01 2019

@author: Lucas De La Fuente P.
"""
# 1.Guardar en un arreglo TODOS los links de los archivos PDF que aparecen en el día de actual. Aquellos del tipo Ver PDF (CVE-157XXXX)
import requests
page = requests.get("http://www.diariooficial.interior.gob.cl/edicionelectronica/empresas_cooperativas.php?date=18-04-2019&edition=42334")
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
import re
links = soup.find_all('a', text=re.compile("^Ver PDF \(CVE-157.*"))
array_links_pdf = [tag.get("href") for tag in links]
array_links_pdf

# 2.Guardar SOLO los links PDF de las CONSTITUCIONES (Dejar fuera Modificaciones y Disoluciones) del día actual.
constituciones = page.text.split('MODIFICACIÓN')
soupCons = BeautifulSoup(constituciones[0], 'html.parser')
links = soupCons.find_all('a', text=re.compile("^Ver PDF \(CVE-157.*"))
array_links_pdf_constituciones = [tag.get("href") for tag in links]
array_links_pdf_constituciones

# 3. Guardar en un arreglo TODOS los links de los archivos PDF de CONSTITUCIONES, MODIFICACIONES Y DISOLUCIONES del año 2018
links2018 = soup.find_all('a', href=re.compile("^http://www.diariooficial.interior.gob.cl/publicaciones/2018.*"))
array_links_pdf2018 = [tag.get("href") for tag in links]
array_links_pdf2018

# 4. Guardar en un arreglo TODOS los links de los archivos PDF de CONSTITUCIONES, MODIFICACIONES Y DISOLUCIONES del año 2016
links2016 = soup.find_all('a', href=re.compile("^http://www.diariooficial.interior.gob.cl/publicaciones/2016.*"))
array_links_pdf2016 = [tag.get("href") for tag in links]
array_links_pdf2016

# En caso de que se requiera obtener los links de los archivos PDF
# de las ediciones de los años 2018 y 2016 se podria implementar
# un ciclo que recorra todos los dias de esos años y que calcule el numero de edicion basado en el la resta de cantidad entre el numero edicion del
# dia actual y el dia en el cual se encuentra el ciclo
# concatenando el valor d-m-Y y el numero de edicion calculado en la url ej: http://www.diariooficial.interior.gob.cl/edicionelectronica/empresas_cooperativas.php?date={d}-{m}-{Y}&edition={numero de edicion}
# y luego realizar el filtro soup.find_all('a', text=re.compile("^Ver PDF \(CVE-157.*")) y agregar los valores del
# array [tag.get("href") for tag in links] en el array de links del año espécificado.
