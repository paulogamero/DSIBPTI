#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:31:43 2021

@author: paulo.gamero
"""
import docx

doc = docx.Document('C:\\Users\\Usuario\\Dropbox\\Pos\\Pós DataScience\\4 - Análise de textos com R e Python\\Dados\\ROMANCE.docx')

#Crie uma lista com os parágrafos do documento 
paragrafos = []
for paragrafo in doc.paragraphs:
    paragrafos.append(paragrafo.text)
print(paragrafos)

#Quantos parágrafos o documento possui?
len(paragrafos)

#Imprima o conteúdo do 1º parágrafo  do texto
print(paragrafos[0])

#Imprima os parágrafos 3 a 6, inclusive
print(paragrafos[2:6])

#O termo ‘Machado’ está no documento?
if 'Machado' in paragrafos:
    print('O termo "Machado" está no documento')
else:
    print('O termo "Machado" não está no documento')
    
#Crie um  texto corrido a partir dos parágrafos lidos
full = ''.join(paragrafos)

#Substitua o termo ‘Batista’ por ‘João Batista’
full.replace('Batista', 'João Batista')
