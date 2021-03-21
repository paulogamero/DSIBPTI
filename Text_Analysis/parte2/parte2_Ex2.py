#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 10:18:15 2021

@author: paulogamero
"""
# ATIVIDADE: EXERCITANDO 2 - PARTE 02
# AUTOR: Paulo Gamero

import docx
import nltk
import os

arquivo = 'C:\\Users\\Usuario\\Dropbox\\Pos\\Pós DataScience\\4 - Análise de textos com R e Python\\Dados\\Noticia_1.docx'
doc = docx.Document(arquivo)

# 2) Lista de parágrafos
texto_p = []
for paragrafo in doc.paragraphs:
    texto_p.append(paragrafo.text)

# 3) Tokenizar
tokens_p = nltk.word_tokenize(''.join(texto_p))

# 4) POS
pos_tags = nltk.pos_tag(tokens_p)

with open(os.getcwd()+'\Paulo_POS_Noticia1.txt','w') as text_file:
    for t in pos_tags:
        text_file.write(str(t) + '\n')

# 5) NER
chuncks = nltk.ne_chunk(pos_tags, binary=True)
entitidades = []
rotulos = []
for chunck in chuncks:
   if hasattr(chunck,'label'):
       entitidades.append(' '.join(c[0] for c in chunck))
       rotulos.append(chunck.label())
       
entidades_com_rotulos = list(set(zip(entitidades,rotulos)))

with open(os.getcwd()+'\Paulo_NER_Noticia1.txt','w') as text_file:
    for c in entidades_com_rotulos:
        text_file.write(str(c)+'\n')