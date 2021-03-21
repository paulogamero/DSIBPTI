#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 10:07:33 2021

@author: paulogamero
"""
# ATIVIDADE: EXERCITANDO 1 - PARTE 02
# AUTOR: Paulo Gamero

import docx
import nltk
from nltk import PorterStemmer, LancasterStemmer, word_tokenize, RSLPStemmer

## stemmig do pt
rslp = RSLPStemmer()
nltk.download('rslp') #stemmer para portuges

## Abrir o arquivo
arquivo = 'C:\\Users\\Usuario\\Dropbox\\Pos\\Pós DataScience\\4 - Análise de textos com R e Python\\Dados\\Noticia_2.docx'
doc = docx.Document(arquivo)

# 02 - Lista de parágrafos
texto_full = []
for paragrafo in doc.paragraphs:
    texto_full.append(paragrafo.text)

# Seleção do 2° e 3° parágrafo
p_2e3 = texto_full[2:4]

# Tokenizar a lista de paragrafos
tokens = word_tokenize(' '.join(p_2e3))

## RSLP
rslp = RSLPStemmer()
stemms_rslp = []
for i in tokens:
    stemms_rslp.append(rslp.stem(i))

## Poter
poter = PorterStemmer()
stemms_poter = []
for i in tokens:
    stemms_poter.append(poter.stem(i))

## Lancaster
lancaster = LancasterStemmer()
stemms_lanc = []
for i in tokens:
    stemms_lanc.append(lancaster.stem(i))