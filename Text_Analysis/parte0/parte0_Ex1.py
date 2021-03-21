#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:16:26 2021

@author: paulo.gamero
"""
import os

#Crie uma string com o conteúdo ‘Ainda que falasse as línguas dos homens e falasse a língua dos anjos, sem amor eu nada seria.’
txt = 'Ainda que falasse as línguas dos homens e falasse a língua dos anjos, sem amor eu nada seria.'

#Imprima cada caractere da string
print(txt)
print(type(txt))

#Segmente a string em uma lista
segmento = txt.split(' ')
print(segmento)
#Quantas palavras há na lista?
len(segmento)

#Substitua o termo ‘dos homens’ por  ‘do mundo’
subt_txt = txt.replace('dos homens', 'do mundo')
print(subt_txt)

#Imprima o fragmento que vai do 21º até o 30º caracteres
print(txt[20:29])

#Imprima os últimos 15 caracteres
print(txt[-15:])

#Salve a sentença em um arquivo do tipo txt
save = open(os.getcwd()+'\sentenca.txt','w',encoding='utf8')#w para escrita
save.write(txt[-15:])
save.close()
