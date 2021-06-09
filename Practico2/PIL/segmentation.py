#! /usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image  # Usando la libreria PIL

foto = Image.open('hoja.png')

if foto.mode != 'L':
    foto = foto.convert('L')

umbral = 200
datos = foto.getdata()
datos_binarios = []

for x in datos:
    if x < umbral:
        datos_binarios.append(0)
        continue
    datos_binarios.append(1)

nueva_imagen = Image.new('1', foto.size)
nueva_imagen.putdata(datos_binarios)
nueva_imagen.save('resultado.png')

im = Image.open('resultado.png')
im.show()

nueva_imagen.close()
foto.close()


